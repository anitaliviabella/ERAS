from rdflib import Graph
import networkx as nx


# Load the Turtle file ontology
g = Graph()
g.parse("ERAS_ontology.ttl", format="ttl")

# Print the number of triples in the graph
print("Number of triples:", len(g))

# Iterate over each triple in the graph and print it
for subj, pred, obj in g:
    print(subj, pred, obj)

# You can also serialize the graph to different formats like RDF/XML, N-Triples, etc.
# For example, to serialize the graph to RDF/XML format:
g.serialize("knowledge_graph.rdf", format="xml")


