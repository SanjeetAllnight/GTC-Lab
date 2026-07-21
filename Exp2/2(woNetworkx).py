import matplotlib.pyplot as plt
from itertools import permutations, combinations
from collections import deque, Counter
edges1 = [
(0,1),(1,2),(2,3),(3,4),(4,0),
(5,6),(6,7),(7,8),(8,9),(9,5),
(0,5),(1,6),(2,7),(3,8),(4,9)
]
edges2 = [
(0,1),(1,2),(2,3),(3,4),(4,0),
(0,5),(1,6),(2,7),(3,9),(4,8),
(5,6),(6,9),(9,8),(8,7),(7,5)
]
nodes = list(range(10))
p1 = {
0:(-2.8,2.8),1:(2.8,2.8),2:(4.2,0),3:(0,-3.2),4:(-4.2,0),
5:(-1.8,1.4),6:(1.8,1.4),7:(2.2,-0.6),8:(0,-1.8),9:(-2.2,-0.6)
}
p2 = {
0:(-2.8,2.8),1:(2.8,2.8),2:(4.2,0),3:(0,-3.2),4:(-4.2,0),
5:(-1.8,1.4),6:(1.5,1.4),7:(2.2,-0.2),8:(-1.8,-0.2),9:(0,-2.0)
}
def build_adj(edges):
    adj={n:set() for n in nodes}
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj
G1=build_adj(edges1)
G2=build_adj(edges2)
def bfs(adj,start):
    dist={start:0}
    q=deque([start])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1
                q.append(v)
    return dist
def path_hist(adj):
    c=Counter()
    for n in adj:
        d=bfs(adj,n)
        for v in d.values():
            c[v]+=1
    return dict(sorted(c.items()))
def count_k_cycles(edges,k):
    count=0
    edge_set=set(tuple(sorted(e)) for e in edges)
    for comb in combinations(nodes,k):
        e=0
        for u,v in combinations(comb,2):
            if tuple(sorted((u,v))) in edge_set:
                e+=1
        if e==k:
            count+=1
    return count
def isomorphic(e1,e2):
    e2_set=set(tuple(sorted(e)) for e in e2)
    for p in permutations(nodes):
        m=dict(zip(nodes,p))
        mapped=set(tuple(sorted((m[u],m[v]))) for u,v in e1)
        if mapped==e2_set:
            return True,m
    return False,{}
L1=path_hist(G1)
L2=path_hist(G2)
c41=count_k_cycles(edges1,4)
c42=count_k_cycles(edges2,4)
c51=count_k_cycles(edges1,5)
c52=count_k_cycles(edges2,5)
iso,map=isomorphic(edges1,edges2)
result="ISOMORPHIC" if iso else "NOT ISOMORPHIC"
def draw_graph(edges,pos,ax,title):
    for u,v in edges:
        x=[pos[u][0],pos[v][0]]
        y=[pos[u][1],pos[v][1]]
        ax.plot(x,y,color="black")
    for n in pos:
        ax.scatter(pos[n][0],pos[n][1],color="pink")
        ax.text(pos[n][0],pos[n][1],str(n),ha="center",va="center")
    ax.set_title(title)
    ax.axis("off")
fig,axs=plt.subplots(2,2,figsize=(10,8))
draw_graph(edges1,p1,axs[0,0],"Graph 1")
draw_graph(edges2,p2,axs[0,1],"Graph 2")
axs[1,0].axis("off")
axs[1,1].axis("off")
def format_table(title, rows):
    lines = []
    lines.append(title)
    lines.append(f"{'Metric':<12}{'Graph1':>8}{'Graph2':>8}")
    lines.append("-"*28)
    for label,g1,g2 in rows:
        lines.append(f"{label:<12}{g1:>8}{g2:>8}")
    return "\n".join(lines)
length_rows = []
for k in sorted(set(L1) | set(L2)):
    length_rows.append((f"Len {k}", L1.get(k,0), L2.get(k,0)))
cycle_rows = [
    ("4-cycles", c41, c42),
    ("5-cycles", c51, c52)
]
length_text = format_table("Shortest Path Length Counts", length_rows)
cycle_text = format_table("Cycle Counts", cycle_rows)
axs[1,0].text(
    0.05,0.85,length_text,
    family="monospace",
    fontsize=11,
    verticalalignment="top"
)
axs[1,1].text(
    0.05,0.85,
    cycle_text + "\n\nMapping: " + str(map),
    family="monospace",
    fontsize=11,
    verticalalignment="top"
)
fig.suptitle(result)
plt.show()