from dimacs import *
import os
from queue import PriorityQueue
from collections import deque



def run_tests(function, graph_dir):
    print(f"Testing {function.__name__} function")
    test_counter = 0
    errors = 0
    for path in os.listdir(graph_dir):
        file_path = os.path.join(graph_dir, path)
        if os.path.isfile(file_path):
            test_counter+=1
            result = "Correct answer"
            try:
                with open(file_path, 'r') as file:
                    line = file.readline()
                    expected_answer = int(line.split()[-1])
                    answer = function(file_path)
                    if answer != expected_answer:
                        result = f"Wrong answer - expected: {expected_answer}, found: {answer}"
                        errors+=1
            except:
                result = "Execute error or no answer"
                errors+=1
            print(f"Graph {path} - {result}")
    print(f"Score: {test_counter-errors}/{test_counter}")
 
def FindUnionSolution(graph_path):
    '''
    Solution based on find/union structure
    1. Sort the edges by weight descending
    2. Union vertices in an edge if they are in separate sets
    3. If vertices s and t are in the same set, it means they are connected and since we are going in descending order the smallest edge weight is as largest as possible
    
    Time Complexity: O(ElogE+ElogV) = O(ElogV)
    
    '''
    def MergeSortDesc(T):
        if len(T) < 2:
            return T
        else:
            mid = len(T) // 2
            left = MergeSortDesc(T[:mid])
            right = MergeSortDesc(T[mid:])
            i, j = 0, 0
            A = []
            while i<len(left) and j<len(right):
                if left[i][2]>right[j][2]:
                    A.append(left[i])
                    i+=1
                else:
                    A.append(right[j])
                    j+=1
            while i<len(left):
                A.append(left[i])
                i+=1
            while j<len(right):
                A.append(right[j])
                j+=1
            return A

    class Node:
        def __init__(self, id):
            self.id = id
            self.parent = self
            self.rank = float('inf')
            
    def find(x):
        if x!=x.parent:
            x.parent = find(x.parent)
        return x.parent
        
    def union(x, y):
        x = find(x)
        y = find(y)
        x.rank = min(x.rank, y.rank)
        y.rank = min(x.rank, y.rank)
        if x==y: return
        if x.rank<y.rank:
            x.parent = y
        else:
            y.parent = x
            if x.rank == y.rank: x.rank+=1

    def connected(x, y):
        return find(x)==find(y)

    def make_set(x):
        return Node(x) 
    V, E = loadWeightedGraph(graph_path)
    s, t = 1, 2
    vert = [make_set(i) for i in range(V+1)]
    E = MergeSortDesc(E)
    i = 0
    w = -1
    while not connected(vert[s], vert[t]):
        u, v, w = E[i]
        if not connected(vert[u], vert[v]):
            union(vert[u], vert[v])
        i+=1
    return w

def DFSBinSearchSolution(graph_path):
    
    def DFS(G, minimal, s, t):
        n = len(G)
        visited = [False for _ in range(n)]
        stack = []
        stack.append(s)
        while stack:
            u = stack.pop()
            if u == t: return True
            visited[u] = True
            for v, w in G[u]:
                if w >= minimal and not visited[v]:
                    stack.append(v)
        return False
   
    def BinSearch(T, G, s, t):
        l, r = 0, len(T)-1

        while l <= r:
            mid = (l+r) // 2
            result = DFS(G, T[mid], s, t)
            if not result: r = mid - 1
            else: l = mid + 1
        if r < len(T):
            return T[r]

        return -1

    V, E = loadWeightedGraph(graph_path)
    s, t = 1, 2
    n = V+1

    G = [[] for _ in range(n)]
    e = []
    # Convert graph
    for a, b, w in E:
        G[a].append((b, w))
        G[b].append((a, w))
        e.append(w)

    e = sorted(e)

    return BinSearch(e, G, s, t)

def DijkstraSolution(graph_path):
    '''
    Solution based on Dijkstra's algorithm
    Using a max PriorityQueue so we always get the largest possible weight.
    Then we relax:
    1. Set the new weight as the minimum of existing minimum-maximum weight and the tested edge
    2. Check if the new weight is greater than the existing one, if so replace it
    
    Time complexity: O(ElogV)
    '''
    V, E = loadWeightedGraph(graph_path)
    s, t = 1, 2
    G = [[] for _ in range(V+1)]
    for u, v, w in E:
        G[u].append((v, w))
        G[v].append((u, w))
    Q = PriorityQueue()
    distance = [0 for _ in range(V+1)]
    distance[s] = float('inf')
    Q.put((-distance[s], s))
    while not Q.empty():
        _, v = Q.get()
        for u, w in G[v]:
            weight = min(w, distance[v])
            if weight > distance[u]:
                distance[u] = weight
                Q.put((-distance[u], u))
    return distance[t]



run_tests(FindUnionSolution, './graphs-lab1')
run_tests(DijkstraSolution, './graphs-lab1')
run_tests(DFSBinSearchSolution, './graphs-lab1')
          



