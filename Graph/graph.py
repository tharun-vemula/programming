class Vertex:
    """Lightweight vertex structure for a graph"""

    __slots__ = "_element"

    def __init__(self, x):
        """Do not call constructor directly. Use Graph.insert_vertex(x)"""
        self._element = x

    def element(self):
        """Return element associated with this vertex"""
        return self._element

    def __hash__(self):
        """will allow vertex to be used a kep in a map"""
        return hash(id(self))


class Edge:
    """Lightweight structure for a graph"""

    __slots__ = "_origin", "_destination", "_element"

    def __init__(self, origin, destination, element):
        """Do not call constructor directly. Use Graph.insert_edge(u,v,x)"""
        self._element = element
        self._origin = origin
        self._destination = destination

    def endpoints(self):
        """Return (u,v) tuple for vertices u and v"""
        return (self._origin, self._destination)

    def opposite(self, v):
        """Return vertex that is opposite to v"""
        return self._origin if v is self._destination else self._destination

    def element(self):
        """Return element associated with this edge"""
        return self._element

    def __hash__(self):
        """will allow vertex to be used a kep in a map"""
        return hash((self._origin, self._destination))


class Graph:
    """Representation of a Graph using an adjacency map"""

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return True if directed"""
        return self._incoming is not self._outgoing

    def vertex_count(self):
        """Return no of vertices in the Graph"""
        return len(self._outgoing)

    def edge_count(self):
        """Return no of edges in the Graph"""
        total = sum(len(self._outgoing[v] for v in self._outgoing))
        return total if self.is_directed() else total // 2

    def vertices(self):
        """Return vertices of the Graph"""
        return self._outgoing.keys()

    def edges(self):
        """Return edges of the Graph"""
        result = set()
        for secondary_map in self._outgoing:
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Return edge from u to v"""
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """Return degree of a vertex"""
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing edges) edges incident to edge v"""
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex"""
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x):
        """Insert and return a new Edge"""
        e = Edge(u, v, x)
        self._outgoing[u][v] = x
        self._incoming[v][u] = x
