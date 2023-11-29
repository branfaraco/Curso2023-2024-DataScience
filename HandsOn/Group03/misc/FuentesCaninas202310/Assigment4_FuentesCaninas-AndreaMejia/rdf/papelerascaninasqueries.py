from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

dict_namespaces = {
"rr" : Namespace("http://www.w3.org/ns/r2rml#"),
"rml": Namespace("http://semweb.mmlab.be/ns/ql#"),
"ql" : Namespace("http://vocab.org/transit/terms/"),
"transit": Namespace("http://www.w3.org/2001/XMLSchema#"),
"wgs84_pos": Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#"),
"vocab": Namespace("http://example.org#"),
"dog-loc": Namespace("https://w3id.org/DogFriendlyMadrid/info/ontology/location#"),
"dog-det": Namespace("https://w3id.org/DogFriendlyMadrid/info/ontology/details#"),
"dog-ser": Namespace("https://w3id.org/DogFriendlyMadrid/info/ontology/services#"),
"schema-org": Namespace("http://schema.org/"),
"dbo": Namespace("https://dbpedia.org/ontology/"),
"rdfs": Namespace("http://www.w3.org/2000/01/rdf-schema#"),
"rdf": Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
"owl": Namespace("http://www.w3.org/2002/07/owl#")
}


g = Graph()

for shortcut, new_namespace in dict_namespaces.items():
    g.namespace_manager.bind(shortcut, new_namespace, override=False)

g.parse("papelerascaninas_data_clean.nt",format="nt")
#nos dan las clases que pertenecen
q1 = prepareQuery('''
SELECT ?id WHERE {
    ?id a ?e
}                      
''',
initNs = dict_namespaces
)
for r in g.query(q1):
  print(r.id)