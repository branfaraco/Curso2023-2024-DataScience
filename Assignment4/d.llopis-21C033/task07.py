# -*- coding: utf-8 -*-
"""Task07.ipynb
# Daniel Llopis, 21C033

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fxBkJiY2pfKcbodiXPcCwGBalTZQBXz3

**Task 07: Querying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2023-2024/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

for s, p, o in g.triples((None, RDFS.subClassOf, ns.LivingThing)):
  print(s)

q1= prepareQuery('''SELECT DISTINCT ?subclass WHERE
{
?subclass rdfs:subClassOf ns:LivingThing.
}''',
initNs = {"rdfs": RDFS, "ns": ns}
)

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

for s,p,o in g.triples((None, RDF.type, ns.Person)):
    print(s)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2,p2,o2 in g.triples((None,RDF.type,s)):
        print(s2)

q2= prepareQuery('''SELECT DISTINCT ?person WHERE
{
  ?subclass rdfs:subClassOf* ns:Person.
  ?person rdf:type ?subclass.
}''',

initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)

for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of "Person" or "Animal" and all their properties including their class with RDFLib and SPARQL. You do not need to list the individuals of the subclasses of person**

"""

for s,p,o in g.triples((None, RDF.type, ns.Person)):
    for s2,p2,o2 in g.triples((s,None,None)):
      print(s2,p2,o2)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2,p2,o2 in g.triples((None,RDF.type,s)):
       for s3,p3,o3 in g.triples((s2,None,None)):
         print(s3,p3,o3)

for s,p,o in g.triples((None, RDF.type, ns.Animal)):
    for s2,p2,o2 in g.triples((s,None,None)):
      print(s2,p2,o2)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Animal)):
    for s2,p2,o2 in g.triples((None,RDF.type,s)):
       for s3,p3,o3 in g.triples((s2,None,None)):
         print(s3,p3,o3)

q3= prepareQuery('''SELECT DISTINCT ?person ?properties WHERE
{
  ?subclass rdfs:subClassOf* ns:Person.
  ?person rdf:type ?subclass.
  ?person ?properties ?values.
}''',
initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)

for r in g.query(q3):
  print(r)

q4= prepareQuery('''SELECT DISTINCT ?animal ?properties WHERE
{
  ?subclass rdfs:subClassOf* ns:Animal.
  ?animal rdf:type ?subclass.
  ?animal ?properties ?values.
}''',
initNs = {"rdfs": RDFS, "rdf": RDF, "ns": ns}
)

for r in g.query(q4):
  print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky**"""

q5 = prepareQuery('''
    SELECT ?personName
    WHERE {
        ?person rdf:type ns:Person .
        ?person ns:knows ?target .
        ?target ns:name "Rocky" .
        ?person ns:name ?personName .
    }
''',
initNs={"rdf": RDF, "ns": ns})

for result in g.query(q5):
    print(result.personName)

"""**Task 7.5: List the entities who know at least two other entities in the graph**"""

q6 = prepareQuery('''
    SELECT ?entityName
    WHERE {
        ?entity rdf:type ?type .
        ?entity ns:knows ?person1 .
        ?entity ns:knows ?person2 .
        FILTER (?person1 != ?person2) .
        ?entity ns:name ?entityName .
    }''',

initNs={"rdf": RDF, "ns": ns})

for r in g.query(q6):
    print(r.entityName)