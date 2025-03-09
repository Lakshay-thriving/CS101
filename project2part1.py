import random
import csv
import networkx as nx
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


def random_walk_pagerank(G, num_steps, teleport=0.85):
    visits = {node: 0 for node in G.nodes()}
    current_node = random.choice(list(G.nodes()))
    for _ in range(num_steps):
        if random.random() < teleport and list(G.neighbors(current_node)):
            current_node = random.choice(list(G.neighbors(current_node)))
        else:
            current_node = random.choice(list(G.nodes()))
        visits[current_node] += 1

    pagerank = {node: visits[node] / num_steps for node in G.nodes()}
    return pagerank

num_steps = 10000000
pagerank = random_walk_pagerank(G, num_steps)
sorted_pagerank = dict(sorted(pagerank.items(), key=lambda item: item[1], reverse=True))
sorted_pagerank_list=[x for x in sorted_pagerank.keys()]
print(sorted_pagerank_list[0],'is the leader')

