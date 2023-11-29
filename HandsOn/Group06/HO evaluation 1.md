6
# Analysis
 - The analysis.html file does not contain the license of the dataset to be generated.
# Ontology
 - You don't need to define multiple ontologies; with one is just enough (and there should be only one).
 - Check that all class names start with capital letter.
 - The XML Schema datatypes are not correctly written.
 - The domain and/or range of some property is not defined.
 - In OWL, having multiple domains (or ranges) means that the domain (or range) is the intersection of all the classes.  The current definitions of properties with multiple domains are wrong.
# RDF data
 - Trim strings before adding them to the RDF.
 - Boolean data values are not encoded properly.
 - The URIs of points are not correct.
 - Datatypes are missing.
# Take into account that the review has been performed over a previous version of the hands-on. Some of the defects found may have been already fixed.
