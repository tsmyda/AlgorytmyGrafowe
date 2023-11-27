from dimacs import *
from queue import *
from tests import *
from copy import deepcopy

def DWGraph2Matrix(V, E):
    '''
    Convert directed and weighted graph to adjacency matrix
    where G[u][v] is the weight/maxflow of edge from vertex u to vertex v
    0 meaning no edge between vertices exists or maxflow of edge is 0
    '''
    G = [[0 for _ in range(V)] for _ in range(V)]
    for u, v, w in E:
        G[u-1][v-1] = w
    return G
    
def WGraph2Matrix(V, E):
    '''
    Convert weighted graph to adjacency matrix
    where G[u][v] is the weight/maxflow of edge from vertex u to vertex v
    0 meaning no edge between vertices exists or maxflow of edge is 0
    '''
    G = [[0 for _ in range(V)] for _ in range(V)]
    for u, v, w in E:
        G[u-1][v-1] = w
        G[v-1][u-1] = w
    return G
    
def DWGraph2List(V, E):
    '''
    Convert directed and weighted graph to adjacency list
    where G[u] is the list of tuples (v, w), where v is the number of vertex connected with u, and w is weight of the edge
    '''
    G = [[] for _ in range(V)]
    for u, v, w in E:
        G[u-1].append((v-1, w))
    return G

def readGraph(graphdir):
    V, E = loadWeightedGraph(graphdir)
    G = WGraph2Matrix(V, E)
    return G


def readDirectedGraph(graphdir):
    V, E = loadDirectedWeightedGraph(graphdir)
    G = DWGraph2Matrix(V, E)
    return G


def FordFulkerson(G, s, t):
    '''
    G is matrix representation of weighted and directed graph, s and t are source and sink vertices
    '''
    n = len(G)
    inf = float('inf')
    max_flow = 0
    
    flow = [[0 for _ in range(n)] for _ in range(n)]
    visited = [False for _ in range(n)]
        
    def DFS(u, bottleneck):
        visited[u] = True
        if u==t: return bottleneck
        for v in range(1, n):
            remaining = G[u][v] - flow[u][v]
            if not visited[v] and remaining>0:
                new_bottleneck = DFS(v, min(remaining, bottleneck))
                if new_bottleneck>0:
                    flow[u][v] += new_bottleneck
                    flow[v][u] -= new_bottleneck
                    return new_bottleneck
        return 0
    
    while True:
        increment = DFS(s, inf)
        if not increment: break
        max_flow += increment
        visited = [False for _ in range(n)]
    return max_flow

def EdmondsKarp(G, s, t):
    '''
    G is matrix representation of weighted and directed graph, s and t are source and sink vertices
    '''
    n = len(G)
    inf = float('inf')
    max_flow = 0
    parent = [None for _ in range(n)]
    
    def BFS(G, s, t, parent):
        n = len(G)
        queue = Queue()
        visited = [False for _ in range(n)]
        visited[s] = True
        queue.put(s)
        while not queue.empty():
            u = queue.get()
            for v in range(n):
                if G[u][v]!=0 and not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    queue.put(v)
                    if visited[t]: return True
        return visited[t]

    while BFS(G, s, t, parent):
        current_flow = inf
        current = t
        #path = []
        while current != s:
            #path.append(current)
            current_flow = min(current_flow, G[parent[current]][current])
            current = parent[current]
        #path.append(s)
        #path.reverse()
        max_flow += current_flow
        v = t
        while v!=s:
            u = parent[v]
            G[u][v] -= current_flow
            G[v][u] += current_flow
            v = parent[v]
        #print(path)
    return max_flow
    
def zad1(graphdir):
    G = readDirectedGraph(graphdir)
    return FordFulkerson(G, 0, len(G)-1)
    
def zad2(graphdir):
    G = readDirectedGraph(graphdir)
    return EdmondsKarp(G, 0, len(G)-1)
    
def zad3(graphdir):
    G = readGraph(graphdir)
    n = len(G)
    res = float('inf')
    for t in range(1, n):
        #print('-----------------')
        G1 = deepcopy(G) 
        res = min(res, EdmondsKarp(G1, 0, t))
    return res



#print(zad3('../lab3/graphs-lab3/geo20_2b'))
      
to_skip = ['grid100x100']       
run_tests(zad1, './graphs-lab2/flow', to_skip)
run_tests(zad2, './graphs-lab2/flow', to_skip)
run_tests(zad3, './graphs-lab2/connectivity', to_skip)
run_tests(zad3, '../lab3/graphs-lab3', to_skip)
 


