5
# Analysis
 - The ontology must have a single namespace.
 - The resource naming strategy fo individuals is missing.
# Ontology
 - In OWL, having multiple domains (or ranges) means that the domain (or range) is the intersection of all the classes.  The current definitions of properties with multiple domains are wrong.
# RDF data
 - The file is not in its correct location in the repository.
 - The RDF file is not a valid NTriples file.
 - Districts have multiple months.
 - It doesn't make sense that a district has a month. Maybe it is not the correct class?
 - If you are only adding a datatype property with a value for a resource, maybe that resource is not needed and you just can include a datatype property in the original class.
 - "mes" is used as a class and as a property.
 - Verify that the class and property names used in the RDF data are the same as those used in the ontology.
# Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.

