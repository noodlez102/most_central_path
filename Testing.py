import networkx as nx
import numpy as np
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
f = open("bus_1138.txt", "r") # will change this later to as for user input or something of the like change it to get code
fh = open("test.edgelist", "w+")
lines = f.readlines()
lines = [s.strip('\n') for s in lines]
lines = [s.strip('e') for s in lines]
#print(lines)
y = len(lines)
num = []
l = 0
for i in lines: #this code needs to be fixed so that it can chose between tabs and spaces
    temp = lines[l].split("\t", 2)
    num.append(temp.split(" ", 2))
    if len(num[l]) != 2:
        num[l].pop(0)
    fh.write(num[l][0])
    fh.write(" ")
    fh.write(num[l][1])
    fh.write("\n")
    l = l+1

array = np.array(num)
content = str(array)
fh.close()
fh = open("test.edgelist", "r")
G = nx.read_edgelist("test.edgelist",create_using = nx.Graph() ,nodetype=int ) #always stays as test.edgelist because thats what the code above writes into
nx.draw(G)
plt.show()
#print(num)
fh.close()
f.close()