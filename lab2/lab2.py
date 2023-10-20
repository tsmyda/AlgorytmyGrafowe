from dimacs import *
from queue import *


path = 'graphs-lab2/flow/simple'
sol = readSolution(path)
#print(V, E)

def DWGraph2Matrix(V, E):
    '''
    Convert directed and weighted graph to adjacency matrix
    where G[u][v] is the weight/maxflow of edge from vertex u to vertex v
    0 meaning no edge between vertices exists or maxflow of edge is 0
    '''
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for u, v, w in E:
        G[u][v] = w
    return G
    
def DWGraph2List(V, E):
    '''
    Convert directed and weighted graph to adjacency list
    where G[u] is the list of tuples (v, w), where v is the number of vertex connected with u, and w is weight of the edge
    '''
    G = [[] for _ in range(V+1)]
    for u, v, w in E:
        G[u].append((v, w))
    return G
    

def FordFulkerson(graph_dir):
    V, E = loadDirectedWeightedGraph(graph_dir)
    G = DWGraph2Matrix(V, E)
    n = len(G)
    inf = float('inf')
    max_flow = 0
    
    s, t = 1, len(G)-1
    
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
    
    pass
    
    
print(FordFulkerson(path))
print(sol)
    
