import matplotlib.pyplot as plt
import networkx as nx
from data import get_graph

G = get_graph()

node_labels = nx.get_node_attributes(G, 'ip')
plt.figure(figsize=(15, 15))
nx.draw_networkx(G, with_labels=True, labels=node_labels, node_size=5000, font_size=10, font_color='white', node_color='blue', edge_color='black')

graph = nx.to_dict_of_dicts(G)

print('Граф:', graph)

print('Кількість вершин:', G.number_of_nodes())
print('Кількість ребер', G.number_of_edges())
print('Вершини:', G.nodes())
print('Ребра:', G.edges())
print('Ступінь вершин:', G.degree())
print('Середня ступінь вершин:', nx.average_degree_connectivity(G))
print('Радіус графа:', nx.radius(G))
plt.show()
