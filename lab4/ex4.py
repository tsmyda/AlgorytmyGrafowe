import os
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

def vertex_cover(file_path):
    V, L = loadWeightedGraph(file_path)
    G = [None] + [Node(i) for i in range(1, V + 1)]
    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    visited = lex_BFS(G)
    I = set()
    for v in visited:
        N = I & G[v].out
        if I & N == set():
            I.add(v)
    result = {v for v in range(1, len(G))}
    return len(result - I)


run_tests(vertex_cover, 'graphs-lab4/vcover')
        
