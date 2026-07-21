import networkx as nx
import matplotlib.pyplot as plt
def dsatur_coloring(G):
    colors = {}
    while len(colors) < len(G.nodes()):
        uncolored = [v for v in G.nodes() if v not in colors]
        max_sat = -1
        chosen = None
        for node in uncolored:
            neighbour_colors = set()
            for neighbour in G.neighbors(node):
                if neighbour in colors:
                    neighbour_colors.add(colors[neighbour])
            sat_degree = len(neighbour_colors)
            if sat_degree > max_sat:
                max_sat = sat_degree
                chosen = node
            elif sat_degree == max_sat:
                if G.degree(node) > G.degree(chosen):
                    chosen = node
        used = set()
        for neighbour in G.neighbors(chosen):
            if neighbour in colors:
                used.add(colors[neighbour])
        color = 0
        while color in used:
            color += 1
        colors[chosen] = color
    return colors
G = nx.MultiGraph()
edges = [
    (1,2),
    (1,3),
    (2,3),
    (2,4),
    (3,4),
    (2,5),
    (4,5),
    (3,6),
    (4,6),
    (5,6),
    (5,7),
    (6,7),
    (7,8),
    (7,9),
    (7,10),
    (8,9),
    (8,9),
    (9,10),
    (9,10)
]
G.add_edges_from(edges)
colors = dsatur_coloring(G)
rgb = [
    "red",
    "green",
    "blue",
    "yellow",
]
node_colors = []
for node in G.nodes():
    node_colors.append(rgb[colors[node]])
pos = {
    1: (-6,0),
    2: (-4,1),
    3: (-4,-1),
    4: (-2,0),
    5: (0,1),
    6: (0,-1),
    7: (2,0),
    8: (5,1.5),
    9: (5,0),
    10: (5,-1.5)
}
plt.figure(figsize=(12,6))
nx.draw_networkx_nodes(
    G,
    pos,
    node_color=node_colors,
    edgecolors="black",
    node_size=1200
)
nx.draw_networkx_labels(
    G,
    pos,
    font_color="white",
    font_weight="bold"
)
normal_edges = []
parallel_89 = []
parallel_910 = []
for u, v, key in G.edges(keys=True):
    if (u == 8 and v == 9) or (u == 9 and v == 8):
        parallel_89.append((u, v, key))
    elif (u == 9 and v == 10) or (u == 10 and v == 9):
        parallel_910.append((u, v, key))
    else:
        normal_edges.append((u, v))
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=normal_edges,
    width=2
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(8,9)],
    width=2,
    connectionstyle="arc3,rad=0.2"
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(8,9)],
    width=2,
    connectionstyle="arc3,rad=-0.2"
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(9,10)],
    width=2,
    connectionstyle="arc3,rad=0.2"
)
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=[(9,10)],
    width=2,
    connectionstyle="arc3,rad=-0.2"
)
plt.title("Greedy Graph Colouring using DSATUR Algorithm")
plt.axis("off")
plt.show()