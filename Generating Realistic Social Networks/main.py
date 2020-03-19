# generate a realistic social network graph
import networkx as nx
import matplotlib.pyplot as plt
import random

def degree_distribute(g):
	distribute = {}
	for i in g.nodes():
		d = g.degree(i)
		if d not in distribute:
			distribute[d] = 1
		else:
			distribute[d] += 1
	
	x = []
	y = []
	for k in sorted(distribute.iterkeys()):
		x.append(k)
		y.append(distribute[k])

	return (x, y)

"""generate graph--"""
'''
N: nodes
K: lattice ring neighbors
rewriteP: rewriting probability
'''
N = 100
K = 6
rewriteP = 0.5


erG = nx.erdos_renyi_graph(100, 0.15)
myGraph = nx.watts_strogatz_graph(N ,K, 0)
wsG = nx.watts_strogatz_graph(N ,K, rewriteP)
baG = nx.barabasi_albert_graph(N, 5)

total_deg = 0
for n in myGraph.nodes():
	total_deg += myGraph.degree(n)

print(total_deg)

del_count = 0
add_count = 0
print("edge:")
# for e in myGraph.edges():
# 	print(e)

print("nodes")

for n in myGraph.nodes():
	# print("start from n")
	# print(myGraph.edges(n))
	

	for e in myGraph.edges(n):
		target = e[1]
		# print(n, target)
		choise = myGraph.nodes()

		# the choise exclude the node with the origin edge(-2) and mulitple edge
		choise.remove(n)
		choise.remove(target)
		# print(myGraph.neighbors(n))

		for neighbor in myGraph.neighbors(n):
			if neighbor in choise:
				choise.remove(neighbor)

		# print(choise)

		r = random.uniform(0, 1)
		# print(r)

		if r <= rewriteP:
			# rewriting
			print("rewrting", [n, target])
			del_count += 1
			rewrite_attaching = {}
			myGraph.remove_edge(n, target)

			# compute probability base on node's deg
			total_deg = 0
			for c in choise:
				total_deg += myGraph.degree(c)
			# print("total_deg:", total_deg)

			for c in choise:
				rewrite_attaching[c] = myGraph.degree(c)/float(total_deg)
			# print(rewrite_attaching)

			# choose a node to attach
			rand_Newedge_target = random.random()
			sum = 0

			for node in rewrite_attaching.keys():
				# print(node)

				sum += rewrite_attaching[node]
				if rand_Newedge_target < sum:
					myGraph.add_edge(n, node)
					add_count += 1
					break




print("#del = %d\n#add = %d" %(del_count, add_count))

"""table or plot(analyze)"""

# cluster coefficient
print("cluster coefficient")
avgCC = nx.average_clustering(myGraph)
print(avgCC)
avgCC = nx.average_clustering(wsG)
print(avgCC)

# power-law
print("power law distribution?")
(x, y) = degree_distribute(myGraph)
print(x, y)
plt.plot(x, y, 'o-')
plt.xlabel('degrees')
plt.ylabel('nodes')
plt.show()

(x, y) = degree_distribute(wsG)
print(x, y)
plt.plot(x, y, 'o-')
plt.show()


(x, y) = degree_distribute(baG)
print(x, y)
plt.plot(x, y, 'o-')
plt.show()

# average path length
print("average path length")
# APL = nx.average_shortest_path_length(myGraph)
# print(APL)
# APL = nx.average_shortest_path_length(wsG)
# print(APL)
# APL = nx.average_shortest_path_length(baG)
# print(APL)

"""visualization"""
nx.draw(myGraph)
plt.show()

nx.draw(wsG)
plt.show()

nx.draw(baG)
plt.show()