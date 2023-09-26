class Vertex:
    """Lighweight vertex structure for a graph"""
    __slots__ = '_element'
    
    def __init__(self, x):
        """Should not call the constructor directly, instead we should use the insert_vertex(x) method
        to create the vertex object"""
        self._element = x 

    def element(self):
        """return element associated with thi vertex"""
        return self._element
    
    def __hash__(self): # will allow vertex to be a map/set key
        return hash(id(self)) 
    
class Edge:
    """Lighweight edge structure for a graph"""

    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        """Should not call constructor directly use, insert_edge(u , v ,x) method from graph class to create 
        edge object"""
        self._origin = u
        self._destination = v
        self._element = x

    def element(self):
        """return element associated with the edge"""
        return self._element
    
    def endpoints(self):
        """return the vertices (U,V) that are endpoints for this edge in a tuple form """
        return (self._origin, self._destination)
    
    def opposite(self, v):
        """Return the vertex opposite to v in this edge """

        if v is self._origin:
            return self._destination
        else:
            return self._origin
        
    def __hash__(self): # will allow wdge to be a map/set key
        return hash((self._origin, self._destination))
    
class Graph:
    """Representation of a simple grahph using an adjacency map """

    def __init__(self, directed=False):
        """Create an empty graph, which is undirected by default
        
        Graph is directed if we parameter driected is set to True in constructor call"""

        self._outgoing = {} # map that will contain incident edges of vertex v 
        # if map is directed we need an extra *in incident* map 
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return true if the graph is a directed grph False otherwise
        
        Property based on the original declaration of the graph, not its contents"""
        return self._incoming is not self._outgoing 
    
    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._outgoing) 
    
    def vertices(self):
        #return an iteration of vertices in the graph which are the keys to the incident map of outgoing endpoints
        return self._outgoing.keys() 
    
    def edge_count(self):
        """Return the number of edges in the graph"""
        total = sum(len(self._outgoing[v]) for v in self._outgoing) # len of values for each key in incident map
        # for undirected graphs, do not double-count the edges 
        return total if self.is_directed else total // 2
    
    def edges(self):
        """return a set of all edges of the graph"""
        result = set() # to avoid double-reporting edges of undirected graphs
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values) #Update a set with the union of itself and others.
        
        return result
    
    def get_edge(self, u, v):
        """return the edge from u to v, or None if not adjacent"""
        return self._outgoing[u].get(v) #return None if v not adjacent 
    
    def degree(self, v, outgoing=True):
        """Return the number of (outgoing) edges incident to vertex v in the graph
        
        If graph is directed optional parameter used to count incoming edges """

        adj = self._outgoing if outgoing else self._incoming 

        return len(adj[v]) 

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph
        
        If graph is directed, optional parameter used to request incoming edges"""

        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge 

    def insert_vertex(self, x = None):
        """Insert and return a new Vertex with element x"""

        vertex = self.Vertex(x)
        self._outgoing[vertex] = {} # new vertex will contain empty map of icidency
        if self.is_directed():
            self._incoming[vertex] = {} # if directed graph 2 incidency maps are needed.

        return vertex 
    
    def insert_edge(self, u, v, x = None):
        """Inser and return a new Edge from u to v with auxiliary element x"""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self.incident_edges[v][u] = e 