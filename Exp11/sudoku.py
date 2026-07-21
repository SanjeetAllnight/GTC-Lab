import networkx as nx
import matplotlib.pyplot as plt
sudoku = [
    [0,4,0,0],
    [0,0,0,0],
    [0,0,4,0],
    [4,0,0,0]
]
size = 4
box = 2
G = nx.Graph()
for r in range(size):
    for c in range(size):
        node = r*size + c
        G.add_node(node)
for r1 in range(size):
    for c1 in range(size):
        n1 = r1*size+c1
        for r2 in range(size):
            for c2 in range(size):
                n2 = r2*size+c2
                if n1!=n2:
                    same_row=(r1==r2)
                    same_col=(c1==c2)
                    same_box=(
                        r1//box==r2//box and
                        c1//box==c2//box
                    )
                    if same_row or same_col or same_box:
                        G.add_edge(n1,n2)
fixed = {}
for r in range(size):
    for c in range(size):
        if sudoku[r][c]!=0:
            node=r*size+c
            fixed[node]=sudoku[r][c]-1
coloring=nx.coloring.greedy_color(
    G,
    strategy="DSATUR"
)
for node,value in fixed.items():
    coloring[node]=value
for node in G.nodes():
    if node not in fixed:
        used=set()
        for nbr in G.neighbors(node):
            if nbr in coloring:
                used.add(coloring[nbr])
        for color in range(4):
            if color not in used:
                coloring[node]=color
                break
solution=[]
for r in range(size):
    row=[]
    for c in range(size):
        node=r*size+c
        row.append(coloring[node]+1)
    solution.append(row)
print("\nSolved Sudoku:\n")
for i,row in enumerate(solution):
    print(
        row[0],
        row[1],
        "|",
        row[2],
        row[3]
    )
    if i==1:
        print("-"*15)
positions={}
for r in range(size):
    for c in range(size):
        node=r*size+c
        positions[node]=(c,-r)
rgb={
0:"red",
1:"green",
2:"blue",
3:"yellow"
}
node_colors=[]
for node in G.nodes():
    node_colors.append(
        rgb[coloring[node]]
    )
labels={}
for r in range(size):
    for c in range(size):
        node=r*size+c
        labels[node]=str(
            solution[r][c]
        )
plt.figure(figsize=(10,8))
nx.draw_networkx_nodes(
    G,
    positions,
    node_color=node_colors,
    node_size=1000,
    edgecolors="black"
)
nx.draw_networkx_edges(
    G,
    positions,
    alpha=0.25
)
nx.draw_networkx_labels(
    G,
    positions,
    labels,
    font_size=12,
    font_weight='bold'
)
plt.title(
"4x4 Sudoku using NetworkX Greedy Vertex Colouring (DSATUR)"
)
plt.axis("off")
plt.show()