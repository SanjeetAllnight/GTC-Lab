import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# -----------------------------
# Initial Sudoku puzzle
# -----------------------------

sudoku_board = [
    [1,0,0,4],
    [0,4,1,0],
    [2,0,0,3],
    [0,3,2,0]
]

# -----------------------------
# Create graph
# -----------------------------

G = nx.Graph()

for v in range(1,17):
    G.add_node(v)

def vertex(row,col):
    return row*4 + col + 1


# Row constraints
for row in range(4):
    for c1 in range(4):
        for c2 in range(c1+1,4):
            G.add_edge(vertex(row,c1),
                       vertex(row,c2))

# Column constraints
for col in range(4):
    for r1 in range(4):
        for r2 in range(r1+1,4):
            G.add_edge(vertex(r1,col),
                       vertex(r2,col))

# Box constraints
for br in range(2):
    for bc in range(2):

        cells=[]

        for r in range(br*2,br*2+2):
            for c in range(bc*2,bc*2+2):
                cells.append(vertex(r,c))

        for i in range(len(cells)):
            for j in range(i+1,len(cells)):
                G.add_edge(cells[i],cells[j])

# -----------------------------
# Fixed values
# -----------------------------

fixed={}

for r in range(4):
    for c in range(4):

        value=sudoku_board[r][c]

        if value!=0:
            fixed[vertex(r,c)] = value-1


# -----------------------------
# DSATUR colouring
# -----------------------------

coloring=dict(fixed)

uncolored=set(G.nodes())-set(fixed.keys())

while uncolored:

    node=max(
        uncolored,
        key=lambda n:(
            len(
                set(
                    coloring[nb]
                    for nb in G.neighbors(n)
                    if nb in coloring
                )
            ),
            G.degree(n)
        )
    )

    neighbor_colors=set(
        coloring[nb]
        for nb in G.neighbors(node)
        if nb in coloring
    )

    color=0

    while color in neighbor_colors:
        color+=1

    coloring[node]=color
    uncolored.remove(node)


# -----------------------------
# Create solved board
# -----------------------------

solved=[]

for r in range(4):

    row=[]

    for c in range(4):

        node=vertex(r,c)

        row.append(
            coloring[node]+1
        )

    solved.append(row)


# -----------------------------
# Print solution
# -----------------------------

print("\nSolved Sudoku\n")

for i,row in enumerate(solved):

    if i==2:
        print("------|------")

    line=""

    for j,val in enumerate(row):

        if j==2:
            line+="| "

        line+=str(val)+" "

    print(line)


# -----------------------------
# Visualization
# -----------------------------

color_map={
0:"#D94F4F",
1:"#4DB86B",
2:"#4A90D9",
3:"#E6C13D"
}

node_colors=[
color_map[coloring[n]]
for n in G.nodes()
]

labels={}

for n in G.nodes():

    r=(n-1)//4
    c=(n-1)%4

    labels[n]=str(
        solved[r][c]
    )

# Better spacing
pos={}

spacing=5

for r in range(4):
    for c in range(4):

        pos[
        vertex(r,c)
        ]=(

        c*spacing,
        (3-r)*spacing
        )


plt.figure(
figsize=(14,10)
)

nx.draw_networkx_nodes(
G,
pos,
node_color=node_colors,
node_size=1800,
edgecolors='black'
)

nx.draw_networkx_edges(
G,
pos,
alpha=.3,
width=1
)

nx.draw_networkx_labels(
G,
pos,
labels,
font_color='white',
font_weight='bold',
font_size=14
)

plt.title(
"4×4 Sudoku using DSATUR Graph Colouring",
fontsize=16,
fontweight='bold'
)

legend=[

mpatches.Patch(
color="#D94F4F",
label="1"
),

mpatches.Patch(
color="#4DB86B",
label="2"
),

mpatches.Patch(
color="#4A90D9",
label="3"
),

mpatches.Patch(
color="#E6C13D",
label="4"
)
]

plt.legend(
handles=legend,
loc='lower center',
ncol=4
)

plt.axis("off")

plt.tight_layout()

plt.show()