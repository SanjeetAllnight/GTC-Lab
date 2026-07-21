import networkx as nx
import matplotlib.pyplot as plt
import math
plt.figure()
g1 = nx.Graph()
nodes = list(range(6))
g1.add_nodes_from(nodes)
for i in nodes:
    for j in nodes:
        if i < j:
            g1.add_edge(i, j)
plt.subplot(2,3,1)
nx.draw(g1, nx.circular_layout(g1), with_labels=True, node_color="pink")
plt.title("Complete Graph")
g2 = nx.Graph()
nodes = list(range(8))
g2.add_nodes_from(nodes)
for i in range(8):
    g2.add_edge(i, (i+1) % 8)
plt.subplot(2,3,2)
nx.draw(g2, nx.circular_layout(g2), with_labels=True, node_color="pink")
plt.title("Cycle Graph")
g3 = nx.Graph()
left = [0,1,2]
right = [3,4,5,6]
g3.add_nodes_from(left + right)
for u in left:
    for v in right:
        g3.add_edge(u, v)
plt.subplot(2,3,3)
nx.draw(g3, nx.bipartite_layout(g3, left), with_labels=True, node_color="pink")
plt.title("Complete Bipartite")
g4 = nx.Graph()
g4.add_nodes_from(range(6))
for i in range(1,6):
    g4.add_edge(0, i)
for i in range(1,6):
    g4.add_edge(i, (i % 5) + 1)
rim_nodes = list(range(1,6))
pos4 = {0:(0,0)}
for i,node in enumerate(rim_nodes):
    theta = 2*math.pi*i/len(rim_nodes)
    pos4[node] = (math.cos(theta), math.sin(theta))
plt.subplot(2,3,4)
nx.draw(g4, pos4, with_labels=True, node_color="pink")
plt.title("Wheel Graph")
g5 = nx.Graph()
nodes = list(range(5))
g5.add_nodes_from(nodes)
for i in range(4):
    g5.add_edge(i, i+1)
pos5 = {i:(i,0) for i in range(5)}
plt.subplot(2,3,5)
nx.draw(g5, pos5, with_labels=True, node_color="pink")
plt.title("Path Graph")
g6 = nx.Graph()
g6.add_nodes_from(range(5))
pos6 = {i:(i,0) for i in range(5)}
plt.subplot(2,3,6)
nx.draw(g6, pos6, with_labels=True, node_color="pink")
plt.title("Null Graph")
plt.show()