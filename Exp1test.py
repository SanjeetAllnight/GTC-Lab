import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.Graph()
nodes1=[1,2,3,4,5,6,7,8,9,10]
G1.add_nodes_from(nodes1)
edges1 = [
    (1,2),(1,5),(1,7),
    (2,8),(2,3),
    (3,4),(3,9),
    (4,5),(4,10),
    (5,6),
    (6,7),(6,10),
    (7,8),
    (8,9),
    (9,10)
]
G1.add_edges_from(edges1)

pos1={
    1:(-2,2),
    2:(2,2),
    3:(4,0),
    4:(0,-4),
    5:(-4,0),
    6:(-2,0),
    7:(-1,1),
    8:(1,1),
    9:(2,0),
    10:(0,-2)
}

G2 = nx.Graph()
nodes2 = ["a","b","c","d","e","f","g","h","i","j"]
G2.add_nodes_from(nodes2)
edges2=[
    ("a","b"),("a","g"),("a","e"),
    ("b","c"),("b","h"),
    ("c","d"),("c","i"),
    ("d","e"),("d","j"),
    ("e","f"),
    ("f","i"),("f","j"),
    ("g","h"),("g","i"),
    ("h","j"),
]
G2.add_edges_from(edges2)
pos2={
    "a":(-2,2),
    "b":(2,2),
    "c":(4,0),
    "d":(0,-4),
    "e":(-4,0),
    "f":(-2,0),
    "g":(-1,1),
    "h":(1,1),
    "i":(2,0),
    "j":(0,-2)
}

iso=nx.is_isomorphic(G1,G2)

n1=G1.number_of_nodes()
n2=G2.number_of_nodes()

e1=G1.number_of_edges()
e2=G2.number_of_edges()

deg1=[d for n, d in G1.degree()]
deg2=[d for n, d in G2.degree()]

cycle1=list(nx.simple_cycles(G1))
cycle2=list(nx.simple_cycles(G2))

connected1 = nx.is_connected(G1)
connected2 = nx.is_connected(G2)

plt.figure(figsize=(14,10))

plt.subplot(2,2,1)
nx.draw(G1,pos1,with_labels=True)
plt.title("Graph1: ")

plt.subplot(2,2,2)
nx.draw(G2,pos2,with_labels=True)
plt.title("Graph2: ")

plt.subplot(2,1,2)
plt.axis("off")
tabledata = [
    ["Number of vertices:",n1,n2],
    ["Number of edges: ",e1,e2],
    ["Degree sequence:",deg1,deg2],
    ["Connected: ",connected1,connected2],
    ["number of cycles: ",len(cycle1),len(cycle2)]
]
table=plt.table(cellText=tabledata,colLabels=["Properties","Graph1","Graph2"])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1,2)

if iso:
    res= "Isomorphic!"
else:
    res= "Not Isomorphic!"
plt.title(res)

plt.tight_layout()
plt.show()