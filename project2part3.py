
import random
import csv
import networkx as nx
import numpy as np
import networkx as nx

def get_branch_subgraph(G, branch_type):
    return G.subgraph([node for node in G.nodes() if node[4:7] == branch_type])

def calculate_pagerank_variance(subgraph):
    pagerank_scores = nx.pagerank(subgraph).values()
    mean_pagerank = sum(pagerank_scores) / len(pagerank_scores)
    pagerank_variance = sum((x - mean_pagerank) ** 2 for x in pagerank_scores) / len(pagerank_scores)
    return pagerank_variance

G=nx.DiGraph()
def read_csv_file():
    data = []
    with open('123.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data
data=read_csv_file()
data=data[1:]

for i in data:
    if i!='':
        if i[1][:11].upper() not in G:
            G.add_node(i[1][:11].upper())
        for j in range(2,len(i)):
            if i[j]!='':
                if i[j][-11:] not in G:
                    G.add_node(i[j][-11:])
                G.add_edge(i[1][:11].upper(),i[j][-11:])
csb1=0
mcb1=0
for i in G.nodes():
    if i[4:7].upper()=='CSB':
        csb1+=1
    else:
        mcb1+=1
p={}
for node in G:
    # Initialize counters for CSB and MCB
    csb = 0
    mcb = 0
    
    # Iterate through the neighbors of the current node
    for neighbor in G[node]:
        # Check if the neighbor's label starts with 'CSB' or 'MCB'
        if neighbor[4:7].upper() == 'CSB':
            csb += 1
        else:
            mcb += 1
    
    # Update the dictionary with the counts
    p[node] = (csb/csb1, mcb/mcb1)
csbtomnc=[]
mnctocsb=[]
for i in p.keys():
    if i[4:7]=='CSB':
        if p[i][1]>p[i][0]:
            csbtomnc.append(i)
    else:
        if p[i][0]>p[i][1]:
            mnctocsb.append(i)
print("CSB TO MNC",csbtomnc)
print("MNC TO CSB",mnctocsb)
# Calculating variance for CSB and MCB in original graph
S1=get_branch_subgraph(G,'CSB')
S2=get_branch_subgraph(G,'MCB')
import networkx as nx

def calculate_variance(graph):
    """
    Calculate the variance of PageRank scores for a graph.

    Parameters:
        graph (nx.DiGraph): The graph for which PageRank variance is to be calculated.

    Returns:
        float: Variance of PageRank scores.
    """
    pagerank_scores = nx.pagerank(graph).values()
    mean_pagerank = sum(pagerank_scores) / len(pagerank_scores)
    pagerank_variance = sum((x - mean_pagerank) ** 2 for x in pagerank_scores) / len(pagerank_scores)
    return pagerank_variance

def calculate_stability(variance_old, variance_new):
    """
    Calculate the stability by comparing the variance before and after node removal.

    Parameters:
        variance_old (float): Variance of PageRank scores before node removal.
        variance_new (float): Variance of PageRank scores after node removal.

    Returns:
        float: Stability measure (percentage change in variance).
    """
    return ((variance_new - variance_old) / variance_old) * 100

def remove_nodes_from_graph(graph, nodes_list):
    """
    Remove nodes from a graph based on a list of nodes.

    Parameters:
        graph (nx.DiGraph): The graph from which nodes are to be removed.
        nodes_list (list): List of nodes to be removed.

    Returns:
        nx.DiGraph: Graph with nodes removed.
    """
    graph_copy = graph.copy()
    graph_copy.remove_nodes_from(nodes_list)
    return graph_copy


# Remove nodes from S1 and S2
S1_updated = remove_nodes_from_graph(S1, csbtomnc)
S2_updated = remove_nodes_from_graph(S2, mnctocsb)

# Calculate variance for S1 and S2
variance_s1 = calculate_variance(S1)
variance_s2 = calculate_variance(S2)

# Calculate variance for updated S1 and S2
variance_s1_updated = calculate_variance(S1_updated)
variance_s2_updated = calculate_variance(S2_updated)

# Calculate stability for CSB and MCB branches
csb_stability = calculate_stability(variance_s1, variance_s1_updated)
mcb_stability = calculate_stability(variance_s2, variance_s2_updated)

# Print the results
print("Variance of S1:", variance_s1)
print("Variance of S2:", variance_s2)
print("\nVariance of updated S1 (after removing nodes in csbtomnc):", variance_s1_updated)
print("Variance of updated S2 (after removing nodes in mnctocsb):", variance_s2_updated)
print("\nStability for CSB (Percentage change in variance):", csb_stability, "%")
print("Stability for MCB (Percentage change in variance):", mcb_stability, "%")

