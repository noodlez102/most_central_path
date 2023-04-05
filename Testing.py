import networkx as nx
import numpy as np
import pygraphviz as pgv
import matplotlib.pyplot as plt

#Below is me testing out how to make all the different kinds of edgelists uniform and useable
'''
list = []
i = 0
f = open("cables_429.txt", "r")
with open('bus_494_586.txt') as topo_file: 
    for line in topo_file:
        list[i] = line
        i = i+1 
G = nx.read_edgelist(f)
f.close
list(G)'''

'''textline = "1 2 3"
fh = open("test.edgelist", "w")
d = fh.write(textline)
fh.close()
G = nx.read_edgelist("cables_429.txt", nodetype=int, data=(("weight", float),))
#print(list(G))
'''

f = open("example_diff_paths.txt", "r") # will change this later to as for user input or something of the like change it to get code
fh = open("test.edgelist", "w+")
lines = f.readlines()
lines = [s.strip('\n') for s in lines]
lines = [s.strip('e') for s in lines]
#print(lines)
y = len(lines)
num = []
l = 0
for i in lines: #this code needs to be fixed so that it can chose between tabs and spaces
    temp = lines[l].replace("\t", " ")
    num.append(temp.split(" ", 2))
    if len(num[l]) != 2:
        num[l].pop(0)
    fh.write(num[l][0])
    fh.write(" ")
    fh.write(num[l][1])
    fh.write("\n")
    l = l+1

fh.close()
fh = open("test.edgelist", "rb")
L = nx.read_edgelist(fh) #below has prog set as a prameter
G = nx.nx_agraph.pygraphviz_layout(L, prog="fdp") #always stays as test.edgelist because thats what the code above writes into4
#Y = nx.from_dict_of_lists(G)
#nx.write_latex(L, "Figure_latex.tex",pos = G, as_document=True)
#print(G)
#print(num)'''
fh.close()
f.close()



#P = nx.shortest_paths(L, source='1',target='26')
s= '1'
t='22'
dsq = dict(nx.all_pairs_shortest_path(L,cutoff=1))
#print("all shortest paths")
#print(dsq)
d_sq = dict(nx.shortest_path_length(L, source=s))
d_qt= dict(nx.shortest_path_length(L, source=t))
k=d_sq[t]
P = {s}
p = s
layers = {}
#print("layers given")
for i in range(1, k):
    layers[i] =set()
    for q in L.nodes:
        if d_sq[q] == i and d_qt[q] == k - i:
            layers[i].add(q)
#print(layers)
for i in range(1, k):
    P_new = set()
    for path in nx.all_shortest_paths(L, source=s, target=p):
        for q in set(L.neighbors(p)).intersection(layers[i]):
            P_new.add(tuple(path + [q]))
    
    if i>= 3:
        pruned= set()
        for path in P_new:
            last_two = tuple(path[-2:])
            if all(last_two not in P for P in pruned):
                pruned.add(tuple(path))
            elif len(set(nx.neighbors(L, path[-3])).intersection(set(path[-2:]))) > 1:
                pruned = pruned - set([P for P in pruned if last_two in P])
                pruned.add(tuple(path))
                    
        P= pruned
    else:
        P = P_new
    p = max(P, key=lambda path: len(path))[-1]

most_degree_central = max(P, key=lambda path: len(L.subgraph(path).degree(path[:-1])))+(t,)
print(most_degree_central)
edge_colors = []
for u, v in L.edges():
    if (u, v) in zip(most_degree_central, most_degree_central[1:]):
        edge_colors.append('r')  # Highlight edges in red
    else:
        edge_colors.append('k')  # Leave other edges black

#print(d_sq)
#print(dsq['1'])
#print(P)
'''length = dict(nx.all_pairs_shortest_path_length(G))
path = dict(nx.all_pairs_shortest_path(G)) prob use this one because I can use cutoff length for each one up to line 8 in pseudo code
'''
nx.draw_networkx(L, pos= G,edge_color=edge_colors)
plt.show()