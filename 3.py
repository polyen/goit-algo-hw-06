import networkx as nx
from matplotlib import pyplot as plt
from search.dijkstra import dijkstra


def get_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 16))
    for i in range(1, 16):
        G.nodes[i]['ip'] = '192.168.1.' + str(i)

    G.add_weighted_edges_from([(1, 2, 2), (1, 3, 3), (1, 4, 5), (1, 5, 1), (1, 6, 1)])
    G.add_weighted_edges_from([(2, 7, 4), (2, 8, 7), (2, 9, 3)])
    G.add_weighted_edges_from([(3, 10, 5), (3, 11, 1)])
    G.add_weighted_edges_from([(4, 12, 4)])
    G.add_weighted_edges_from([(5, 13, 8)])
    G.add_weighted_edges_from([(6, 14, 2), (6, 15, 5)])

    # Додамо кілька ребер для більшої складності
    G.add_weighted_edges_from([(1, 7, 3), (1, 8, 1), (1, 9, 7)])
    G.add_weighted_edges_from([(2, 10, 6), (2, 11, 6)])
    G.add_weighted_edges_from([(3, 12, 2)])
    G.add_weighted_edges_from([(4, 13, 4)])

    pos = nx.fruchterman_reingold_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

    return G


if __name__ == '__main__':
    graph = get_graph()
    dijkstra(graph, 1)
