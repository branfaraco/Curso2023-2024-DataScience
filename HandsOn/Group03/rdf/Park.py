from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

dict_namespaces = {
    "rr": Namespace("http://www.w3.org/ns/r2rml#"),
    "rml": Namespace("http://semweb.mmlab.be/ns/ql#"),
    "ql": Namespace("http://vocab.org/transit/terms/"),
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
}

g = Graph()

for shortcut, new_namespace in dict_namespaces.items():
    g.namespace_manager.bind(shortcut, new_namespace, override=False)

g.parse("./CareCenters.nt", format="nt")

q1 = prepareQuery(
    '''
    SELECT ?centro
    WHERE {
        ?centros rdf:type schema-org:ID .
        ?centros rdfs:label ?centro
    }
    ''',
    initNs=dict_namespaces
)

results = list(g.query(q1))

if not results:
    print("No results found.")
else:
    for r in results:
        print(r.centro)