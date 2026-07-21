import math
import matplotlib.pyplot as plt
def create_graph():
    nodes = ['s','a','b','c','d','f']
    edges = [
        ('s','a',18),
        ('s','c',15),
        ('a','c',6),
        ('a','b',9),
        ('c','d',7),
        ('b','d',10),
        ('c','b',14),
        ('b','f',28),
        ('d','f',36)
    ]
    adj = {n: [] for n in nodes}
    for u,v,w in edges:
        adj[u].append((v,w))
        adj[v].append((u,w))
    return nodes, edges, adj
def dijkstra_steps(nodes, adj, source):
    dist = {n: float('inf') for n in nodes}
    dist[source] = 0
    visited = set()
    steps = []
    while len(visited) < len(nodes):
        u = None
        min_val = float('inf')
        for n in nodes:
            if n not in visited and dist[n] < min_val:
                min_val = dist[n]
                u = n
        if u is None:
            break
        visited.add(u)
        changed_edges = []
        for v,w in adj[u]:
            if v not in visited:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed_edges.append((u,v))
        steps.append((visited.copy(), dist.copy(), u, changed_edges))
    return steps
def draw_graph(ax, nodes, edges, pos):
    for u,v,w in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y, color="gray")
        mx = (pos[u][0] + pos[v][0]) / 2
        my = (pos[u][1] + pos[v][1]) / 2
        ax.text(mx, my, str(w), color="black")
def draw_nodes(ax, nodes, pos, visited, current):
    for n in nodes:
        x,y = pos[n]
        color = "lightgray"
        if n in visited:
            color = "orange"
        if n == current:
            color = "blue"
        ax.scatter(x, y, s=800, c=color)
        ax.text(x, y, n, ha='center', va='center')
def draw_step(ax, nodes, edges, pos, visited, dist, current, changed_edges, step):
    draw_graph(ax, nodes, edges, pos)
    for u,v in changed_edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]
        ax.plot(x, y, color="red", linewidth=2)
    draw_nodes(ax, nodes, pos, visited, current)
    for n,(x,y) in pos.items():
        val = "∞" if dist[n] == float('inf') else str(dist[n])
        ax.text(x, y+0.25, val, color="green", ha='center')
    ax.set_title("Step " + str(step) + " (Selected: " + current + ")")
    ax.axis("off")
def show_steps(nodes, edges, steps):
    pos = {
        's': (0,3),
        'c': (-1.5,1.5),
        'a': (1.5,1.5),
        'd': (-1.5,-1.5),
        'b': (1.5,-1.5),
        'f': (0,-3)
    }
    total = len(steps)
    cols = math.ceil(math.sqrt(total))
    rows = math.ceil(total/cols)
    fig, axes = plt.subplots(rows, cols, figsize=(5*cols,4*rows))
    if total == 1:
        axes = [axes]
    elif hasattr(axes,"flat"):
        axes = list(axes.flat)
    for i in range(total):
        visited, dist, current, changed_edges = steps[i]
        draw_step(axes[i], nodes, edges, pos, visited, dist, current, changed_edges, i+1)
    for i in range(total, len(axes)):
        axes[i].remove()
    plt.tight_layout()
    plt.show()
nodes, edges, adj = create_graph()
steps = dijkstra_steps(nodes, adj, 's')
show_steps(nodes, edges, steps)