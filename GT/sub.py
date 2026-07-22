import networkx as nx
import matplotlib.pyplot as plt
import random
G = nx.Graph()
edges = [
    ('A','B'), ('A','C'), ('A','D'),
    ('B','F'), ('B','H'),
    ('C','D'), ('C','G'), ('C','I'),
    ('D','G'), ('D','E'),
    ('E','G'), ('E','F'),
    ('F','H'),
    ('G','I'),
    ('H','I')
]
G.add_edges_from(edges)
pos = {
    'A': (0, 4),
    'B': (4, 3),
    'C': (-3, 1),
    'D': (-1, 2),
    'E': (1, 1),
    'F': (3, 1),
    'G': (-1, 0),
    'H': (4, -2),
    'I': (0, -3)
}
selected_nodes = random.sample(list(G.nodes()), 5)
induced = G.subgraph(selected_nodes).copy()

spanning = nx.minimum_spanning_tree(G)

edge_deleted = G.copy()
deleted_edges = random.sample(list(G.edges()), 3)
edge_deleted.remove_edges_from(deleted_edges)

plt.figure(figsize=(12, 10))
# Original Graph
plt.subplot(2, 2, 1)
nx.draw(G,pos, with_labels=True)
plt.title("Original Graph")
# Induced Subgraph
plt.subplot(2, 2, 2)
nx.draw(induced,pos)
plt.title(
    f"Induced Subgraph\nSelected Vertices: {selected_nodes}"
)
# Spanning Subgraph
plt.subplot(2, 2, 3)
nx.draw(spanning,pos,)
plt.title("Spanning Subgraph")
# Edge-Deleted Subgraph
plt.subplot(2, 2, 4)
nx.draw(edge_deleted,pos,)
plt.title(
    f"Edge-Deleted Subgraph\nDeleted Edges: {deleted_edges}"
)
plt.tight_layout()
plt.show()