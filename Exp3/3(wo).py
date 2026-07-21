import matplotlib.pyplot as plt

nodes = ["A","B","C","D","E","F","G","H","I"]

edges = [
("A","B"),("A","C"),("A","D"),
("B","F"),("B","H"),
("C","D"),("C","G"),("C","I"),
("D","E"),("D","G"),
("E","F"),("E","G"),
("F","H"),
("G","I"),
("H","I")
]

pos = {
"A": (0.0,4.4),
"B": (5.3,3.2),
"C": (-3.2,0.8),
"D": (-0.6,1.8),
"E": (1.0,0.7),
"F": (3.8,0.7),
"G": (-0.6,-0.2),
"H": (5.3,-2.8),
"I": (-0.7,-3.6)
}

spanning_edges = [
("A","B"),("A","C"),("A","D"),
("D","E"),("E","F"),
("F","H"),("H","I"),("I","G")
]

induced_nodes = ["C","D","E","G","I"]

edge_induced_edges = [
("A","D"),("C","D"),
("D","E"),("E","F"),
("F","H"),("G","I")
]

def draw_graph(edges, pos, nodes, ax, title, node_color, edge_color):

    for u,v in edges:
        x=[pos[u][0],pos[v][0]]
        y=[pos[u][1],pos[v][1]]
        ax.plot(x,y,color=edge_color,linewidth=1.5)

    for n in nodes:
        ax.scatter(pos[n][0],pos[n][1],color=node_color)
        ax.text(pos[n][0],pos[n][1],n,ha="center",va="center")

    ax.set_title(title)
    ax.axis("off")
induced_edges=[]
for u,v in edges:
    if u in induced_nodes and v in induced_nodes:
        induced_edges.append((u,v))
fig, ax = plt.subplots(2,2, figsize=(13,10))
draw_graph(edges,pos,nodes,ax[0,0],"Original graph","#a7b8c9","#5a5a5a")
draw_graph(spanning_edges,pos,nodes,ax[0,1],"Spanning subgraph","#b8d8b8","#2f6f2f")
draw_graph(induced_edges,pos,induced_nodes,ax[1,0],"Induced subgraph","#d7c9a2","#6f5a2f")
edge_nodes=set()
for u,v in edge_induced_edges:
    edge_nodes.add(u)
    edge_nodes.add(v)
draw_graph(edge_induced_edges,pos,list(edge_nodes),ax[1,1],"Edge-induced subgraph","#d1b5d8","#5b2f6f")
plt.tight_layout()
plt.show()