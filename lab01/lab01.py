from dimacs import *

(V, L) = loadWeightedGraph("g1")
for (x,y,c) in L:
    print("Krawedz miedzy", x, "i", y, "o wadze", c)
    
print(L)
    
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
    
vert = [make_set(i) for i in range(V+1)]
E = MergeSortDesc(L)
print(E)
print(V)
i = 0
while not connected(vert[1], vert[2]):
    u, v, w = E[i]
    if not connected(vert[u], vert[v]):
        union(vert[u], vert[v])
    i+=1
print(w)

#print(MergeSortDesc(T))