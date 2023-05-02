with open("table.txt", encoding='utf8') as f:
    p = f.read().strip()

dic = {}
for i, value in enumerate(p):
    if value == ':':
        dic[p[i - 1]] = p[i + 1]


k, value, path_ = '1', dic['1'], '1'

while k != '0':
    path_ += dic[k]
    k = path_[-1]

print(', '.join(path_[::-1]))



'''319. CRITICAL PATH

Difficulty: 5 out of 10

The structure below is called a directed graph, and it consists of a set of nodes: 0, A, N, and so on, as well as links between them. So nodes N and Z are connected, and at the same time, Z is a child of node N, and N is an ancestor (parent) of node Z:
In the table below, the top row lists all nodes in the graph, and the bottom row lists their ancestors. So, for example, node Z has node A as its ancestor. Note that node Z has two ancestors on the graph: A and N, but the table always shows one:

Particular attention in the graph is occupied by nodes 0 and 1 - these are the initial and final nodes. Your task, using the table, is to build a path from 0 to 1. In the example above, the path will be: 0, A, Z, B, M, 1
In Python code, such a table is best stored as a dictionary, where the key is the node of the graph, and its value is the parent:

table = {"0": None, "A": 0, ...}
Algorithmically, the task is reduced to traversing such a dictionary with the subsequent construction of a path.
A complete table with nodes and their ancestors is stored in the table.txt file next to the program. The file has the following format: N1:,N2:P2,N3:P3, where N is the next node. A node is followed by a colon, followed by the node's parent. N1 has no ancestor, so there is a space after the colon, N2 has a P2 ancestor, and so on. All nodes and ancestors are separated by commas. A complete example of such a file for the table above looks like this:

0:,A:0,N:A,T:N,Z:A,B:Z,M:B,X:A,1:M

Write a program that reads the table.txt file and then outputs a path from 0 to 1. The nodes in the path must be separated by a comma and a space:

Usage example (based on the data in the task text):
> pythonpath.py
> 0, A, Z, B, M, 1

This task is one of the elements of a more complex algorithm for constructing a critical path in graph theory. Critical paths are often used in design activities to find bottlenecks in the design of large projects. This allows for better control and planning of complex tasks.

'''
