import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
edges = [
    ('s','a',18), ('s','c',15), ('a','c',6),
    ('a','b',9), ('c','b',14), ('c','d',7),
    ('b','d',10), ('b','t',28), ('d','t',36)
]
G.add_weighted_edges_from(edges)
pos = {
    's':(-3,0), 'a':(-2,1), 'c':(-2,-1),
    'b':(1,1), 'd':(1,-1), 't':(2,0)
}
# Shortest paths from source s
distances, paths = nx.single_source_dijkstra(
    G, source='s', weight='weight'
)
# Plot graph
plt.figure(figsize=(10,8))
plt.subplot(2,1,1)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.title("Weighted Graph")
# Create shortest path table
plt.subplot(2,1,2)
plt.axis("off")
table_data = []
for vertex in G.nodes():
    table_data.append([
        vertex,
        distances[vertex],
        " -> ".join(paths[vertex])
    ])
plt.table(cellText=table_data,colLabels=["Vertex", "Minimum Distance", "Shortest Path"])
plt.title("Shortest Paths from Source s")
plt.tight_layout()
plt.show()

