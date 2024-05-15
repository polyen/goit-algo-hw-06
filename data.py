import networkx as nx


def get_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 16))
    for i in range(1, 16):
        G.nodes[i]['ip'] = '192.168.1.' + str(i)

    G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6)])
    G.add_edges_from([(2, 7), (2, 8), (2, 9)])
    G.add_edges_from([(3, 10), (3, 11)])
    G.add_edges_from([(4, 12)])
    G.add_edges_from([(5, 13)])
    G.add_edges_from([(6, 14), (6, 15)])

    return G
