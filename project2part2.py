
import random
import csv
import networkx as nx
import numpy as np
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
node_indices = {node: i for i, node in enumerate(G.nodes())}
def replace_zero(adj_matrix, row, col):
    A1 = np.copy(adj_matrix)
    A1 = np.delete(A1, (row, col), axis=0)
    A1 = np.delete(A1, (row, col), axis=1)

    A = np.delete(adj_matrix[row], col)
    A = np.delete(A, row)
    A = A.reshape(-1, 1)  # Reshape A to a column vector
    B = np.delete(adj_matrix[col], row)
    B = np.delete(B, col)
    B = B.reshape(-1, 1)  # Reshape B to a column vector

    return A1, A, B

def solve_equation_least_squares(A1, A):
    X, _, _, _ = np.linalg.lstsq(A1, A, rcond=None)
    return X

def find_Xtranspose_B(X, B):
    X_transpose = np.transpose(X)
    X_transpose_B = np.dot(X_transpose, B)
    return X_transpose_B


num_nodes = len(G.nodes())

adj_matrix = np.zeros((num_nodes, num_nodes))

for edge in G.edges():
    node1, node2 = edge
    index1, index2 = node_indices[node1], node_indices[node2]
    adj_matrix[index1][index2] = 1
print(adj_matrix)
t=input('Want to check for edges between nodes')
while t.lower()=='yes':
    node1 = input("Enter the label for node 1: ").upper()
    node2 = input("Enter the label for node 2: ").upper()
    
    if node1 in G.nodes() and node2 in G.nodes() and node1!=node2:
        index1, index2 = node_indices[node1], node_indices[node2]
        if adj_matrix[index1][index2] == 1 and adj_matrix[index2][index1] == 1:
            print("Bidirectional edge exists between", node1, "and", node2)
        elif adj_matrix[index1][index2]==1 and adj_matrix[index2][index1]==0:
            A1, A, B = replace_zero(adj_matrix,index2,index1)
            X = solve_equation_least_squares(A1, A)
            X_transpose_B = find_Xtranspose_B(X, B)
            if X_transpose_B>=0:
                print("Bidirectional edge exists between", node1, "and", node2) 
            else:
                print(node1,'points to',node2)
        
        elif adj_matrix[index1][index2]==0 and adj_matrix[index2][index1]==1:
            A1, A, B = replace_zero(adj_matrix,index1,index2)
            X = solve_equation_least_squares(A1, A)
            X_transpose_B = find_Xtranspose_B(X, B)
            if X_transpose_B>=0:
                print("Bidirectional edge exists between", node1, "and", node2) 
            else:
                print(node2,'points to',node1)
        else:
            
            A1, A, B = replace_zero(adj_matrix,index1,index2)
            X = solve_equation_least_squares(A1, A)
            X_transpose_B = find_Xtranspose_B(X, B)
            p1=1 if X_transpose_B>=0 else 0
            
            A1, A, B = replace_zero(adj_matrix,index2,index1)
            X = solve_equation_least_squares(A1, A)
            X_transpose_B = find_Xtranspose_B(X, B)
            p2=1 if X_transpose_B>=0 else 0
            if p1==1 and p2==1:
                print('Bidirectional edge exits between', node1 ,'and', node2)
            elif p1==1 and p2==0:
                print(node1,'points to',node2)
            elif p1==0 and p2==1:
                print(node2,'points to', node1)
            else:
                print('No edge possible between the two nodes',node1,'and',node2)
    else:
        if node1 in G.nodes() and node2 in G.nodes() and node1==node2:
            print('Both nodes are same')
        else:
            print("One or both of the entered nodes do not exist in the graph.")
    t=input('Want to check again?')
    if t.lower()=='no':
        break
