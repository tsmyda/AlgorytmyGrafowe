from dimacs import *
from tests import run_tests
from lexBFS import *

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()
        self.RN = set()
        self.parent = None

    def connect_to(self, v):
        self.out.add(v)
        
def max_clique(file_path):
    V, L = loadWeightedGraph(file_path)
    G = [None] + [Node(i) for i in range(1, V + 1)]
    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    visited = lex_BFS(G)
    result = 0
    for v in visited:
        result = max(result, len(G[v].RN) + 1)
    return result


run_tests(max_clique, 'graphs-lab4/maxclique')