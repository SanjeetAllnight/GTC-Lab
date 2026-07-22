import networkx as nx
import matplotlib.pyplot as plt
degree_sequence = [6, 5, 5, 4, 3, 3, 2, 2, 1, 1]
is_graphical = nx.is_graphical(degree_sequence, method="hh")
if is_graphical:
    G = nx.havel_hakimi_graph(degree_sequence)
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G,pos)
    plt.title(
        f"Degree Sequence: {degree_sequence}\n"
        f"Graphical: {is_graphical}"
    )
    plt.show()
else:
    print("The given degree sequence is not graphical")