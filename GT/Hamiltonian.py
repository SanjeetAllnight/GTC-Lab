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
# Find Hamiltonian circuits using backtracking
circuits = []
start = 'A'
def hamiltonian(path):
    # All vertices visited
    if len(path) == len(G):
        # Check if last vertex connects back to start
        if G.has_edge(path[-1], start):
            circuits.append(path + [start])
        return
    # Try every neighbor
    for neighbor in G.neighbors(path[-1]):
        if neighbor not in path:
            path.append(neighbor)
            hamiltonian(path)
            path.pop()
        if len(circuits) >= 7:
            return
hamiltonian([start])
# Plot original graph
plt.figure(figsize=(15, 10))
plt.subplot(2, 4, 1)
nx.draw(G, pos, with_labels=True)
plt.title("Original Graph")
# Plot up to 7 Hamiltonian circuits
for i, circuit in enumerate(circuits[:7]):
    plt.subplot(2, 4, i + 2)
    nx.draw(G, pos, with_labels=True)
    circuit_edges = list(zip(
        circuit,
        circuit[1:]
    ))
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=circuit_edges,
        edge_color="red",
        width=3
    )
    plt.title(f"Circuit {i+1}\n{circuit}")

plt.tight_layout()
plt.show()