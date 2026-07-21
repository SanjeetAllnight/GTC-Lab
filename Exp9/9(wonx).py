import matplotlib.pyplot as plt
nodes = [1,2,3,4,5,6,7]
edges = [
    (1,2), (1,3),
    (2,3), (2,4), (2,5),
    (3,4), (3,6),
    (4,5), (4,6),
    (5,6), (5,7),
    (6,7)
]
pos = {
    1: (0, 3),
    2: (-2, 1),
    3: (2, 1),
    4: (0, 0),
    5: (-2, -2),
    6: (2, -2),
    7: (0, -4)
}
def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph
def is_eulerian(graph):
    odd = 0
    for v in graph:
        if len(graph[v]) % 2 != 0:
            odd += 1
    return odd == 0
def remove_edge(graph, u, v):
    graph[u].remove(v)
    graph[v].remove(u)
def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)
def dfs_count(graph, v, visited):
    count = 1
    visited.add(v)
    for nbr in graph[v]:
        if nbr not in visited:
            count += dfs_count(graph, nbr, visited)
    return count
def is_valid_edge(graph, u, v):
    if len(graph[u]) == 1:
        return True
    visited = set()
    count1 = dfs_count(graph, u, visited)
    remove_edge(graph, u, v)
    visited = set()
    count2 = dfs_count(graph, u, visited)
    add_edge(graph, u, v)
    return count2 >= count1
def find_eulerian(graph):
    start = list(graph.keys())[0]
    for v in graph:
        if len(graph[v]) % 2 == 1:
            start = v
            break
    path = []
    def fleury(u):
        for v in list(graph[u]):
            if is_valid_edge(graph, u, v):
                path.append((u, v))
                remove_edge(graph, u, v)
                fleury(v)
    fleury(start)
    return path
def draw_graph(ax, highlight=None, title=""):
    for u, v in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y, color="gray")
    if highlight:
        for u, v in highlight:
            x = [pos[u][0], pos[v][0]]
            y = [pos[u][1], pos[v][1]]
            ax.plot(x, y, color="red", linewidth=2)
    for n in nodes:
        x, y = pos[n]
        ax.scatter(x, y, s=500)
        ax.text(x, y, str(n), ha='center', va='center', color='white')
    ax.set_title(title)
    ax.axis("off")
graph = build_graph(edges)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
draw_graph(ax[0], None, "Original Graph")
if is_eulerian(graph):
    path_edges = find_eulerian(graph.copy())
    draw_graph(ax[1], path_edges, "Eulerian Circuit")
else:
    draw_graph(ax[1], None, "Graph is not Eulerian")
plt.tight_layout()
plt.show()