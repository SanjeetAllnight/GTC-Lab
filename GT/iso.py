import networkx as nx
import matplotlib.pyplot as plt

# Graph 1
G1 = nx.Graph()

edges1 = [
    (1,2), (1,5), (1,7),
    (2,8), (2,3),
    (3,4), (3,9),
    (4,5), (4,10),
    (5,6),
    (6,7), (6,10),
    (7,8),
    (8,9),
    (9,10)
]

G1.add_edges_from(edges1)

pos1 = {
    1:(-2,2), 2:(2,2), 3:(4,0), 4:(0,-2), 5:(-4,0),
    6:(-2,0), 7:(-1,1), 8:(1,1), 9:(1,0), 10:(0,-1)
}


# Graph 2
G2 = nx.Graph()

edges2 = [
    ("a","b"), ("a","g"), ("a","e"),
    ("b","c"), ("b","h"),
    ("c","d"), ("c","i"),
    ("d","e"), ("d","j"),
    ("e","f"),
    ("f","i"), ("f","j"),
    ("g","h"), ("g","i"),
    ("h","j")
]

G2.add_edges_from(edges2)

pos2 = {
    "a":(-2,2), "b":(2,2), "c":(4,0), "d":(0,-2), "e":(-4,0),
    "f":(-2,0), "g":(-1,1), "h":(1,1), "i":(1,0), "j":(0,-1)
}


# Isomorphism and properties
iso = nx.is_isomorphic(G1, G2)

cycles1 = list(nx.simple_cycles(G1))
cycles2 = list(nx.simple_cycles(G2))

tabledata = [
    ["Number of vertices", G1.number_of_nodes(), G2.number_of_nodes()],
    ["Number of edges", G1.number_of_edges(), G2.number_of_edges()],
    ["Degree sequence", [d for n,d in G1.degree()], [d for n,d in G2.degree()]],
    ["Connected", nx.is_connected(G1), nx.is_connected(G2)],
    ["Number of cycles", len(cycles1), len(cycles2)],
    ["All cycles", str(cycles1), str(cycles2)]
]


# Plot graphs
plt.figure(figsize=(14,10))

plt.subplot(2,2,1)
nx.draw(G1, pos1, with_labels=True)
plt.title("Graph 1")

plt.subplot(2,2,2)
nx.draw(G2, pos2, with_labels=True)
plt.title("Graph 2")


# Display properties
plt.subplot(2,1,2)
plt.axis("off")

table = plt.table(
    cellText=tabledata,
    colLabels=["Properties", "Graph 1", "Graph 2"],
    cellLoc="center",
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1,2)

if iso:
    plt.title("Graphs are Isomorphic!")
else:
    plt.title("Graphs are Not Isomorphic!")

plt.tight_layout()
plt.show()