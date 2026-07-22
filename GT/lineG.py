import networkx as nx
import matplotlib.pyplot as plt

# Original Graph
G = nx.Graph()

edges = [
    ('A', 'E'),
    ('A', 'B'),
    ('E', 'B'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D')
]
G.add_edges_from(edges)

pos = {
    'A': (-2, 2),
    'E': (-2, -2),
    'B': (0, 0),
    'C': (2, 2),
    'D': (2, -2)
}

# Create Line Graph
L = nx.line_graph(G)

# Properties
properties = [
    ["Number of Vertices", G.number_of_nodes(), L.number_of_nodes()],
    ["Number of Edges", G.number_of_edges(), L.number_of_edges()],
    ["Degree Sequence",
     sorted([d for n, d in G.degree()], reverse=True),
     sorted([d for n, d in L.degree()], reverse=True)],
    ["Connected", nx.is_connected(G), nx.is_connected(L)],
    ["Number of Cycles",len(list(nx.simple_cycles(G))),len(list(nx.simple_cycles(L)))]
]

# Plot
plt.figure(figsize=(12, 9))

# Original Graph
plt.subplot(2, 2, 1)
nx.draw(G,pos,)
plt.title("Original Graph")


# Line Graph
plt.subplot(2, 2, 2)
posL = nx.spring_layout(L, seed=42)
nx.draw(L,posL)
plt.title("Line Graph")


# Properties Table
plt.subplot(2, 1, 2)
plt.axis("off")

table = plt.table(
    cellText=properties,
    colLabels=["Properties", "Original Graph", "Line Graph"]
)
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2)

plt.tight_layout()
plt.show()