import matplotlib.pyplot as plt
nodes = [1, 2, 3, 4, 5]
edges = [
    (1, 2), (2, 5), (5, 4), (4, 1),
    (1, 3), (2, 3), (4, 3), (5, 3)
]
pos = {
    1: (-1, 1),
    2: (1, 1),
    4: (-1, -1),
    5: (1, -1),
    3: (0, 0)
}
closed_walk = [(1, 2), (2, 3), (3, 1)]
path = [(1, 3), (3, 2), (2, 5)]
trail = [(1, 2), (2, 3), (3, 4), (4, 5)]
def draw_graph(ax, highlight_edges=None, title=""):
    for u, v in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y, color="gray")
    if highlight_edges:
        for u, v in highlight_edges:
            x = [pos[u][0], pos[v][0]]
            y = [pos[u][1], pos[v][1]]
            ax.plot(x, y, linewidth=3)
    for n in nodes:
        x, y = pos[n]
        ax.scatter(x, y, s=500)
        ax.text(x, y, str(n), ha='center', va='center', color='white')
    ax.set_title(title)
    ax.axis("off")
fig, ax = plt.subplots(2, 2, figsize=(10, 10))
draw_graph(ax[0, 0], None, "Original Graph")
draw_graph(ax[0, 1], closed_walk, "Closed Walk")
draw_graph(ax[1, 0], path, "Path")
draw_graph(ax[1, 1], trail, "Trail")
plt.tight_layout()
plt.show()