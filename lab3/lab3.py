from dimacs import *
from queue import PriorityQueue


class Node:
    
    def __init__(self):
        self.edges = {}
        self.active = True
    
    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight
    
    def delEdge(self, to):
        del self.edges[to]
        
def mergeVertices(G, x, y):
    for i in G[y].edges:
        if i != x: 
            G[x].addEdge(i ,G[y].edges[i])
    to_remove = [i for i in G[y].edges]
    for i in to_remove:
        G[y].delEdge(i)
    G[y].active = False
    
    
(V,L) = loadWeightedGraph( "./graphs-lab3/clique5" )
for (x,y,c) in L:
    print( "krawedz miedzy", x-1, "i", y-1,"o wadze", c )
  
G = [Node() for i in range(V)]
for (x, y, c) in L:
    G[x-1].addEdge(y-1, c)
    G[y-1].addEdge(x-1, c)

for i in G[1].edges:
    print(f"Krawedz z wierzcholka 1 do wierzcholka {i} o wadze {G[1].edges[i]}")

for i in G[2].edges:
    print(f"Krawedz z wierzcholka 2 do wierzcholka {i} o wadze {G[2].edges[i]}")
    
mergeVertices(G, 1, 2)

print('------------------------')

for i in G[1].edges:
    print(f"Krawedz z wierzcholka 1 do wierzcholka {i} o wadze {G[1].edges[i]}")

for i in G[2].edges:
    print(f"Krawedz z wierzcholka 2 do wierzcholka {i} o wadze {G[2].edges[i]}")
    
print(G[1].edges[0])   
    
S = {1, 2, 3, 4, 5}
print(S)
S.add(6)
print(S)

def minimumCutPhase(G):
    a = 0
    S = [a]
    while len(S)<len(G):
        pass
        