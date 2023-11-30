from dimacs import *
from queue import PriorityQueue
from tests import *

class Node:
    def __init__(self):
        self.edges = {}
        self.active = True
    
    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight
    
    def delEdge(self, to):
        del self.edges[to]
        
def mergeVertices(graph, x, y):
    y_list = list(graph[y].edges.items())
    for vertex, weight in y_list:
        if vertex != x:
            graph[x].addEdge(vertex, weight)
            graph[vertex].addEdge(x, weight)
        graph[y].delEdge(vertex)
        graph[vertex].delEdge(y)

def minimumCutPhase(G):
    n = len(G)
    a = 1
    S = []
    queue=PriorityQueue()
    queue.put((0, a))
    visited = [False for _ in range(n)]
    weights = [0 for _ in range(n)]
    while not queue.empty():
        v_weight, v = queue.get()
        if not visited[v]:
            S.append(v)
            visited[v] = True
            for u, u_weight in G[v].edges.items():
                if not visited[u]:
                    weights[u] += u_weight
                    queue.put((-weights[u], u))
    s = S[-1]
    t = S[-2]
    res = 0
    for v, weight in G[s].edges.items():
        res += weight
    mergeVertices(G, t, s)
    return res
    
def stoerWagner(graphdir):
    V, L = loadWeightedGraph(graphdir)
    G = [Node() for i in range(V)]
    for (x, y, c) in L:
        G[x-1].addEdge(y-1, c)
        G[y-1].addEdge(x-1, c)
    res = float('inf')
    while V>1:
        res = min(res, minimumCutPhase(G))
        V -= 1
    return res

to_skip = ['grid100x100'] 
run_tests(stoerWagner, './graphs-lab3/', to_skip)