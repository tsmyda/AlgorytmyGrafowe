def lex_BFS(G):
    visited = []
    vertices = [set(range(1, len(G)))]
    while len(visited) < len(G) - 1:
        u = vertices[-1].pop()
        visited.append(u)
        idx = 0
        while idx < len(vertices):
            i = 0
            neighbour = vertices[idx] & G[u].out
            not_neighbour = vertices[idx] - neighbour
            if len(neighbour) > 0:
                vertices.insert(idx + 1, neighbour)
                i += 1
            if len(not_neighbour) > 0:
                vertices.insert(idx + 1, not_neighbour)
                i += 1
            vertices.remove(vertices[idx])
            idx += i
        new_vertices = []
        intersection = set()
        for v in visited:
            new_vertices.append(v)
            intersection.add(v)
        G[u].RN = intersection & G[u].out
        found = False
        while len(new_vertices) > 0 and not found:
            if {new_vertices[-1]} & G[u].RN == set():
                new_vertices.pop(-1)
            else:
                found = True
        if found:
            G[u].parent = new_vertices[-1]
    return visited