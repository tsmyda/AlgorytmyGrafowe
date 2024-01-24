from dimacs import *
from tests import *
from lexBFS import *

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()
        self.RN = set()
        self.parent = None

    def connect_to(self, v):
        self.out.add(v)

def check_lex_BFS(G, visited):
    for v in visited[1:]:
        if not G[v].RN - {G[v].parent} <= G[G[v].parent].RN:
            return False
    return True


def perfect_elimination_order(file_path):
    V, L = loadWeightedGraph(file_path)
    G = [None] + [Node(i) for i in range(1, V + 1)]
    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    visited = lex_BFS(G)
    return check_lex_BFS(G, visited)


run_tests(perfect_elimination_order, 'graphs-lab4/chordal')
