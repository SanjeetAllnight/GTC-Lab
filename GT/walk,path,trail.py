import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ('A','B'), ('A','C'), ('B','C'),
    ('B','D'), ('C','F'), ('D','F'),
    ('D','G'), ('F','G'),
    ('B','E'), ('C','E'), ('D','E'), ('E','F')
]

G.add_edges_from(edges)

pos = {
    'A':(0,3),
    'B':(-2,2), 'C':(2,2),
    'E':(0,1),
    'D':(-2,0), 'F':(2,0),
    'G':(0,-2)
}


# 1. Closed Walk
closed_walk = nx.find_cycle(G)


# 2. Path of length 5
path = None

for source in G.nodes():
    for target in G.nodes():

        for p in nx.all_simple_paths(G, source, target, cutoff=5):

            if len(p) - 1 == 5:
                path = p
                break

        if path:
            break

    if path:
        break

path_edges = list(zip(path, path[1:]))


# 3. Find Longest Trail
longest_trail = []

def find_trail(node, trail, used_edges):
    global longest_trail

    if len(trail) > len(longest_trail):
        longest_trail = trail.copy()

    for neighbor in G.neighbors(node):

        edge = frozenset((node, neighbor))

        if edge not in used_edges:

            used_edges.add(edge)
            trail.append((node, neighbor))

            find_trail(neighbor, trail, used_edges)

            trail.pop()
            used_edges.remove(edge)


for node in G.nodes():
    find_trail(node, [], set())


# Plot
plt.figure(figsize=(12,10))

# Original
plt.subplot(2,2,1)
nx.draw(G, pos, with_labels=True)
plt.title("Original Graph")


# Closed Walk
plt.subplot(2,2,2)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(
    G, pos,
    edgelist=closed_walk,
    edge_color="red",
    width=3
)
plt.title(f"Closed Walk\n{closed_walk}")


# Path
plt.subplot(2,2,3)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(
    G, pos,
    edgelist=path_edges,
    edge_color="red",
    width=3
)
plt.title(f"Path of Length 5\n{path}")


# Longest Trail
plt.subplot(2,2,4)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(
    G, pos,
    edgelist=longest_trail,
    edge_color="red",
    width=3
)
plt.title(f"Longest Trail\nLength = {len(longest_trail)}")


plt.tight_layout()
plt.show()