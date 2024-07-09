import networkx as nx
import random
import numpy as np

def add_edges(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r=random.random()
                if r<=p:
                    G.add_edge(i,j)
                else:
                    continue
    return G
 
def initialize_points(G):
    points=[100 for i in range(G.number_of_nodes())]
    return points

def distribute_points(G,points):
    prev_points=points
    new_points=[0 for i in range(G.number_of_nodes())]

    for i in G.nodes():
        out=G.out_edges(i)
        if len(out)==0:
            new_points[i]+=prev_points[i]
        else:
            share = (float)(prev_points[i])/len(out)
            for each in out:
                new_points[each[1]]+=share

    return G, new_points

def keep_distributing_points(G,points):
    prev_points=points
    print ('Enter # to stop')
    while(1):
        G,new_points=distribute_points(G,prev_points)
        print (new_points)

        char = input()
        if char=='#':
            break
        prev_points = new_points

    return G,new_points

def get_nodes_sorted_by_points(points):
    points_array=np.array(points)
    nodes_sorted_by_points = np.argsort(-points_array)
    return nodes_sorted_by_points

def main():
    # Create/take a directed graph with 'n' nodes.
    G=nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G=add_edges(G,0.3)

    # Assign 100 points to each node.
    points=initialize_points(G)
    print (points)

    # Keep distributing points until convergence
    G,points=keep_distributing_points(G,points)

    # # Get nodes ranking as per the points accumulated
    nodes_sorted_by_points = get_nodes_sorted_by_points(points)
    print(f"nodes_sorted_by_points {nodes_sorted_by_points}")

    # Compare the ranks thus obained with the ranks obtained from the inbuilt Page Rank Method
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(),key=lambda x:x[1],reverse=True)
    for i in pr_sorted:
        print(i[0], end=" " )



main()