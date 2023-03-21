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
L = nx.read_edgelist(fh)
G = nx.nx_agraph.pygraphviz_layout(L) #always stays as test.edgelist because thats what the code above writes into4
Y = nx.from_dict_of_lists(G)
pos = {n: (n,n) for n in G}
nx.write_latex(L, "Figure_latex.tex",pos = pos, as_document=True)
print(G)
'''nx.draw(L)
plt.show()
#print(num)'''
fh.close()
f.close()

'''P = nx.all_shortest_paths(Y, source=1,target=26)
length = dict(nx.all_pairs_shortest_path_length(G))
path = dict(nx.all_pairs_shortest_path(G)) prob use this one because I can use cutoff length for each one'''
