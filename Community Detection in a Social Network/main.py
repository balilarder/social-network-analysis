"""
hw2: competition
Design a algorithm to cluster a social network graph
output: the number of detected cluster and (node, clusterID) pairs
"""
import networkx as nx
import community
import operator
import collections
from random import shuffle
import matplotlib.pyplot as plt



def mymodel(graph):
	community_num = 0
	communities = {}
	print("my model")

	print(graph.nodes())

	### base on Louvain's propagation 
	# assign every nodes its label to the community
	for node in graph.nodes():
		communities[node] = node
	Qcurrent = community.modularity(communities, graph)
	# print(res)
	order = list(graph.nodes())
	shuffle(order)
	print(order)
	
	
	iterate = 1
	for i in range(5):
		for node in order:
			neighbors_community = [communities[i] for i in graph.neighbors(node)]
			# print(node, neighbors_community)
			counter = collections.Counter(neighbors_community)
			most_frequency = counter.most_common(1)
			# print(node, most_frequency)
			origin = communities[node]
			communities[node] = most_frequency[0][0]
			q = community.modularity(communities, graph)
			if q - Qcurrent < 0:
				communities[node] = origin
			else:
				Qcurrent = q
			# print(Qcurrent)

		iterate += 1
		shuffle(order)
		print(Qcurrent)

	f = open('result.txt', 'w')
	for node in communities:
		f.write("%s\t%s\n" %(node, communities[node]))

	counter = collections.Counter(communities.values())
	print(len(counter.keys()))

	nx.draw(graph)
	plt.show()
	
	##
	return(community_num, communities)
	


def main():
	## input

	print("read txt")
	graph = {}
	G = nx.Graph()
	# print(range(1000))

	nodes = [str(i) for i in range(1, 1001)]
	G.add_nodes_from(nodes)
	with open('graph.txt', 'r') as f:
		lines = f.readlines()
		# print(len(lines))
		edges = []
		for edge in lines:
			edge = edge.rstrip().split('\t')
			edges.append((edge[0], edge[1]))

	G.add_edges_from(edges)

	mymodel(G)

if __name__ == '__main__':
	main()