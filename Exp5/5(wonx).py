import matplotlib.pyplot as plt
import math
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)
edges = []
for i in range(n):
    for j in range(i+1,n):
        if A[i][j] == 1:
            edges.append((i,j))
line_nodes = list(range(len(edges)))
line_edges = []
for i in range(len(edges)):
    for j in range(i+1,len(edges)):
        e1 = edges[i]
        e2 = edges[j]

        if (e1[0] in e2) or (e1[1] in e2):
            line_edges.append((i,j))
pos1 = {}
for i in range(n):
    angle = 2*math.pi*i/n
    pos1[i] = (math.cos(angle), math.sin(angle))
pos2 = {}
m = len(edges)
for i in range(m):
    angle = 2*math.pi*i/m
    pos2[i] = (math.cos(angle), math.sin(angle))
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
for i in range(n):
    for j in range(i+1,n):
        if A[i][j] == 1:
            x=[pos1[i][0],pos1[j][0]]
            y=[pos1[i][1],pos1[j][1]]
            plt.plot(x,y,color="black")
for i in pos1:
    plt.scatter(pos1[i][0],pos1[i][1],color="pink")
    plt.text(pos1[i][0],pos1[i][1],str(i),ha="center",va="center")
plt.title("Original Graph")
plt.axis("off")
plt.subplot(1,2,2)
for u,v in line_edges:
    x=[pos2[u][0],pos2[v][0]]
    y=[pos2[u][1],pos2[v][1]]
    plt.plot(x,y,color="black")
for i in pos2:
    plt.scatter(pos2[i][0],pos2[i][1],color="pink")
    plt.text(pos2[i][0],pos2[i][1],str(i),ha="center",va="center")
plt.title("Line Graph")
plt.axis("off")
plt.show()