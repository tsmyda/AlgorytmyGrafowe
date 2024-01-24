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


def color_graph(file_path):
    V, L = loadWeightedGraph(file_path)
    G = [None] + [Node(i) for i in range(1, V + 1)]
    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    visited = lex_BFS(G)
    color = [0] * len(G)
    for v in visited:
        used = {color[u] for u in G[v].out}
        j = 1
        while j in used:
            j += 1
        color[v] = j
    return max(color)
     
run_tests(color_graph, 'graphs-lab4/coloring')
