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
