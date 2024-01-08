import matplotlib.pyplot as plt
import networkx as nx


def node_visualize(d: dict[int, list[int]]):
    # Create a graph
    G = nx.Graph()

    # Add edges from the dictionary
    for u, neighbors in d.items():
        for v in neighbors:
            G.add_edge(u, v)

    # Draw the graph
    plt.figure(figsize=(12, 8))
    nx.draw(G, with_labels=True, node_color='lightblue',
            node_size=2000, font_size=15, font_weight='bold')
    plt.title("Visualization of Graph with Nodes and Edges")
    plt.show()


# d = {
#     8: [3, 18, 20, 7],
#     2: [19, 15, 13, 16, 1, 4, 11],
#     9: [17, 5],
#     19: [7],
#     14: [12, 10, 6],
#     10: [15],
#     5: [12]
# }
# draw_graph(d)
