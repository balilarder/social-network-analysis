'''
hw3: maximize influence
goal: choose 30 nodes as seed, try to infect more nodes
intuition: between+
'''

import networkx as nx
import json
import operator
def DEG_BETWEENESS(graph, weight):
    # input a graph, compute score by degree and between 
    # score = weight*degree + (1-weight)*betweeness

    # degree part
    size = graph.size()
    for n in graph.nodes():
        graph.node[n]['degree'] = graph.degree(n)
        # graph.node[n]['degree'] = (graph.degree(n))/float(size)
    # test
    print(type(graph.node), graph.node['8828'])

    # between part
    with open('betweeness.json') as data_file:    
        betweeness = json.load(data_file)
        # print(betweeness['163'])
        for key in betweeness:
            graph.node[key]['betweeness'] = betweeness[key]
    # test
    print(type(graph.node), graph.node['8828'])

    # combine the degree and betweeness = score
    score_rank = {}
    for n in graph.node:
        graph.node[n]['score'] = weight*graph.node[n]['degree'] + \
            (1-weight)*graph.node[n]['betweeness']
        score_rank[n] = graph.node[n]['score']
    # test
    print(type(graph.node), graph.node['8828'])

    # score rank
    score_rank = sorted(score_rank.items(), key=operator.itemgetter(1), reverse = True)
    with open('seed.txt', 'w') as f:
        # for rank in score_rank:
        for rank in score_rank[:30]:

            print(rank)

            # f.write(rank[0]+' '+str(rank[1])+'\n')
            f.write(rank[0]+'\n')
def spread(graph):
    pass


def main():
    # form a graph
    G = nx.Graph()

    # G.add_edge(1, 3)

    # print(G.edges())
    # print(G.size())
    # print(G.nodes())
    # print(G.order())

    file = open('networkdata.txt', 'r')
    edges = file.readlines()
    print(len(edges))

    for edge in edges:
        edge = edge.split()
        # print(edge)

        G.add_edge(edge[0], edge[1], probability = 0.05)

    for n in G.nodes():
        G.node[n]['seed'] = 0
        G.node[n]['score'] = 0
        G.node[n]['active'] = 0
        G.node[n]['degree'] = 0
        G.node[n]['betweeness'] = 0
        # if (edge[0], edge[1]) in G.edges() or \
        #     (edge[1], edge[0]) in G.edges():
        #     print("gan")

    # print(G.edges())
    # print(G.size())
    # print(G.nodes())
    # print(G.order(), len(G.nodes()))
    # print(G.nodes(data = True))
    DEG_BETWEENESS(G, 0.5)


    '''
    '''
    # F = nx.Graph()
    # F.add_edge('A', 'B')
    # F.add_edge('B', 'C')
    # F.add_edge('C', 'E')
    # F.add_edge('E', 'D')
    # F.add_edge('D', 'B')
    # res = nx.betweenness_centrality(F)
    # print(res)

if __name__ == '__main__':
    main()