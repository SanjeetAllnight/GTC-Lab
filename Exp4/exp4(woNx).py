import matplotlib.pyplot as plt
import math

deg_seq = list(map(int,input("Enter degree sequence separated by space: ").split()))

n = len(deg_seq)
nodes = list(range(n))

pairs = [[nodes[i],deg_seq[i]] for i in range(n)]

edges = []

while True:

    pairs.sort(key=lambda x:x[1], reverse=True)

    if pairs[0][1] == 0:
        break

    v = pairs[0][0]
    d = pairs[0][1]
    pairs[0][1] = 0

    for i in range(1,d+1):

        if i >= len(pairs):
            print("Degree sequence is not graphical")
            exit()

        u = pairs[i][0]
        edges.append((v,u))
        pairs[i][1] -= 1

        if pairs[i][1] < 0:
            print("Degree sequence is not graphical")
            exit()


pos = {}

for i in range(n):
    angle = 2*math.pi*i/n
    pos[i] = (math.cos(angle), math.sin(angle))


plt.figure()

for u,v in edges:
    x=[pos[u][0],pos[v][0]]
    y=[pos[u][1],pos[v][1]]
    plt.plot(x,y,color="black")

for node in pos:
    plt.scatter(pos[node][0],pos[node][1],color="pink")
    plt.text(pos[node][0],pos[node][1],str(node),ha="center",va="center")

plt.title("Graph from Degree Sequence")
plt.axis("off")
plt.show()