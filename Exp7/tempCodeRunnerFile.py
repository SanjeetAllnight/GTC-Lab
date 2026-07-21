import math
import matplotlib.pyplot as plt
import networkx as nx
def create_graph():
    G = nx.Graph()
    edges = [
        ('s', 'a', 18),
        ('s', 'c', 15),
        ('a', 'c', 6),
        ('a', 'b', 9),
        ('c', 'd', 7),
        ('b', 'd', 10),
        ('c', 'b', 14),
        ('b', 'f', 28),
        ('d', 'f', 36)
    ]
    G.add_weighted_edges_from(edges)
    return G
def dijkstra_steps(G, source):
    dist = {node: float('inf') for node in G.nodes()}
    dist[source] = 0
    visited = set()
    steps = []
    while len(visited) < len(G.nodes()):
        u = None
        min_dist = float('inf')
        for node in G.nodes():
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                u = node
        if u is None:
            break
        visited.add(u)
        changed_edges = []
        for v in G.neighbors(u):
            w = G[u][v]['weight']
            if v not in visited:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed_edges.append((u, v))
        steps.append((visited.copy(), dist.copy(), u, changed_edges))
    return steps
def draw_step(ax, G, pos, visited, dist, current, changed_edges, step):
    nx.draw_networkx_edges(G, pos, edge_color="gray", ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=changed_edges, edge_color="red", width=2, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=800, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=list(visited), node_color="orange", ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=[current], node_color="blue", ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
    for node, (x, y) in pos.items():
        val = "∞" if dist[node] == float('inf') else str(dist[node])
        ax.text(x, y + 0.25, val, ha='center', color="green")
    ax.set_title("Step " + str(step) + " (Selected: " + str(current) + ")")
    ax.axis("off")
def show_steps(G, steps):
    pos = {
        's': (0, 3),
        'c': (-1.5, 1.5),
        'a': (1.5, 1.5),
        'd': (-1.5, -1.5),
        'b': (1.5, -1.5),
        'f': (0, -3)
    }
    total = len(steps)
    cols = math.ceil(math.sqrt(total))
    rows = math.ceil(total / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
    if total == 1:
        axes = [axes]
    elif hasattr(axes, "flat"):
        axes = list(axes.flat)
    for i in range(total):
        visited, dist, current, changed_edges = steps[i]
        draw_step(axes[i], G, pos, visited, dist, current, changed_edges, i + 1)
    for i in range(total, len(axes)):
        axes[i].remove()
    plt.tight_layout()
    plt.show()
G = create_graph()
steps = dijkstra_steps(G, 's')
show_steps(G, steps)