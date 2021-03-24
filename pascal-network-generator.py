import math
import numpy
import networkx as nx
%matplotlib inline
import matplotlib.pyplot as plt


order = int(raw_input("enter order of graph: "))
PM = numpy.zeros((order,order),dtype= int)

#Generate Pascal matrix
for i in range(order-1):
    for j in range(i+1 ):
        PM[i+1][j] = ((math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))%2) #jCr mod 2
        PM[j][i+1] = PM[i+1][j]

PG = nx.Graph()		#Pascal graph

for i in range(1,order+1):
    PG.add_node(i)		#Add nodes to the graph
for i in range(order):
    for j in range(order):
        if (PM[i][j] == 1):
            PG.add_edge(i+1,j+1)		#Add edges to the graph according to the matrix


print PM
nx.draw_networkx(PG,node_color='green',node_size=700)

