import networkx as nx
import json

G = nx.Graph()

file = open('networkdata.txt', 'r')
edges = file.readlines()


for edge in edges:
    edge = edge.split()
    G.add_edge(edge[0], edge[1], probability = 0.05)

res = nx.betweenness_centrality(G)
with open('betweeness.json', 'w') as fp:
	json.dump(res, fp)