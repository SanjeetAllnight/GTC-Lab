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
# Check for Eulerian Circuit
is_eulerian = nx.is_eulerian(G)
table_data = []
if is_eulerian:
    circuit = list(nx.eulerian_circuit(G))
    for i, edge in enumerate(circuit):
        table_data.append([
            i + 1,
            f"{edge[0]} -> {edge[1]}"
        ])
    result = "Eulerian Circuit Exists"
else:
    odd_vertices = [
        node for node, degree in G.degree()
        if degree % 2 != 0
    ]
    reason = f"Odd degree vertices: {odd_vertices}"
    table_data.append([
        "No Circuit",
        reason
    ])
    result = "No Eulerian Circuit"
# Plot Original Graph
plt.subplot(2,1,1)
nx.draw(G,pos,)
plt.title(result)
# Display Steps / Reason
plt.subplot(2,1,2)
plt.axis("off")
plt.table(cellText=table_data,colLabels=["Step", "Edge / Reason"])
plt.tight_layout()
plt.show()