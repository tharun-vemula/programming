from graph import Graph, Vertex


def DFS(g: Graph, u: Vertex, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)
