import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    (1,3), (1,4), (3,4),
    (3,2), (4,2),
    (2,5), (2,6),
    (3,5), (4,6), (5,6),
    (5,7), (6,7),
    (7,8), (7,9), (7,10),
    (8,9), (9,10)
]

G.add_edges_from(edges)

pos = {
    1:(0,3),
    3:(-1,2), 4:(1,2),
    2:(0,1),
    6:(-1,0), 5:(1,0),
    7:(2,-1),
    10:(3,-2), 9:(4,-2), 8:(5,-2)
}

# Greedy Coloring
colors = nx.coloring.greedy_color(
    G,
    strategy="largest_first"
)

# Chromatic number used by greedy algorithm
chromatic_number = max(colors.values()) + 1

# Convert color numbers into a list
node_colors = [colors[node] for node in G.nodes()]

# Labels with assigned colors
labels = {
    node: f"{node}\nColor {colors[node] + 1}"
    for node in G.nodes()
}


# Original Graph
plt.subplot(1,2,1)

nx.draw(
    G,
    pos,
    with_labels=True
)

plt.title("Original Graph")


# Colored Graph
plt.subplot(1,2,2)

nx.draw(
    G,
    pos,
    labels=labels,
    node_color=node_colors,
    cmap=plt.cm.Set3
)

plt.title(
    f"Greedy Graph Coloring\n"
    f"Chromatic Number = {chromatic_number}"
)

plt.tight_layout()
plt.show()