import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
edges = [
    ('a', 'b', 5),
    ('a', 'e', 7),
    ('a', 'c', 8),
    ('b', 'e', 5),
    ('b', 'f', 6),
    ('c', 'e', 3),
    ('c', 'd', 1),
    ('e', 'f', 3),
    ('e', 'g', 2),
    ('e', 'd', 4),
    ('f', 'g', 2),
    ('d', 'g', 3)
]
G.add_weighted_edges_from(edges)

pos = {
    'a': (-3, 0),
    'b': (-2, 2),
    'c': (-2, -2),
    'e': (0, 0),
    'f': (2, 2),
    'd': (2, -2),
    'g': (3, 0)
}

# Find MST using Kruskal's algorithm
MST = nx.minimum_spanning_tree(G,algorithm="kruskal",weight="weight")
# Get MST edges
mst_edges = list(nx.minimum_spanning_edges(G,algorithm="kruskal",weight="weight",data=True))
# Calculate total cost
total_cost = MST.size(weight="weight")


plt.figure(figsize=(14, 10))
plt.subplot(2, 2, 1)
nx.draw(G,pos)
weights = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G,pos,edge_labels=weights)
plt.title("Original Weighted Graph")


# -------------------------------
# Plot MST
# -------------------------------

plt.subplot(2, 2, 2)
nx.draw(MST,pos)
mst_weights = nx.get_edge_attributes(MST, "weight")
nx.draw_networkx_edge_labels(MST,pos,edge_labels=mst_weights)
plt.title(f"Minimum Spanning Tree\nTotal Cost = {total_cost}")


# -------------------------------
# Display Kruskal Steps
# -------------------------------

plt.subplot(2, 1, 2)
plt.axis("off")

steps = []
cost = 0

for i, (u, v, data) in enumerate(mst_edges):

    weight = data["weight"]
    cost += weight

    steps.append([
        i + 1,
        f"{u} - {v}",
        weight,
        cost
    ])

table = plt.table(
    cellText=steps,
    colLabels=[
        "Step",
        "Selected Edge",
        "Weight",
        "Cumulative Cost"
    ],
    cellLoc="center",
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

plt.title("Step-by-Step Kruskal MST Construction")

plt.tight_layout()
plt.show()