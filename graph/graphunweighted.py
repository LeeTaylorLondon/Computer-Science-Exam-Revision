from typing import NoReturn, List

class Graph:
    def __init__(self, v, e):
        # Set self.v (vertices) -> Can pass 'v' or 'vertices' as a str
        if (type(v) == str):
            st = set()
            for elm in v:
                st.update(elm.upper())
            self.vertices = st
        else:
            self.vertices = v
        # Set self.e (edges) -> Can pass 'e' or 'edges' as a list of strings
        if (type(e) == list):
            sete = set()
            for elm in e:
                if (len(elm) != 2) or (type(elm) != str):
                    raise TypeError(f"Elements of e must be type 'str' and of length 2.")
                temp_fset = frozenset({elm[0].upper(), elm[1].upper()})
                sete.add(temp_fset)
            self.edges = sete
        else:
            self.edges = e
        # Init. visited to None
        self.visited = None

    def __repr__(self) -> str:
        return f"{self.v()}\n{self.e()}"

    def init_visited(self) -> NoReturn:
        """ Sets self.visited to Dict[str, bool] where all values are False """
        visited = {}
        vertices_arr = list(self.vertices)
        vertices_arr.sort()
        for elm in vertices_arr:
            visited.update({elm: False})
        self.visited = visited

    def set_visited(self, v:str) -> NoReturn:
        """ Remove node with name v from self.visited """
        if (type(v) != str):
            raise TypeError(f"Expected type 'str', got '{type(v)}'")
        del self.visited[v]

    def v(self) -> str:
        """ Return string of vertices """
        return f"Vertices ({len(self.vertices)}): " + ','.join(self.vertices)

    def e(self) -> str:
        """ Return string of edges """
        rv = f'Edges ({len(self.edges)}): '
        for edge in self.edges:
            rv = rv + '' + str(edge)[-9] + '-' + str(edge)[-4] + '|'
        return rv[:-1]

    def get_neighbours(self, v) -> List[str]:
        """ Returns neighbours of a given node """
        # Get string of frozen set containing path
        rv = []
        for path in self.edges:
            if (v in path):
                rv.append(str(path))
        # Perform string manipulation get names only
        for i,s in enumerate(rv):
            chars = [s[-9], s[-4]]
            if (chars[0] == v): del chars[0]
            else: del chars[1]
            rv[i] = chars[0]
        rv.sort()
        return rv

    def breadth(self) -> List[str]:
        """ Performs breadth-first search """
        # Init. queues, & trace
        trace, q1, q2 = [], [], []
        # Set all vertices to not visited
        self.init_visited()
        # While not all nodes have been visited
        while (self.all_visited() != True):
            # If there is nothing in q2 ...
            if (q2 == []):
                # Pick the next minimum node in the whole graph
                q1 = [min(self.get_unvisited())]
            # Otherwise overwrite q1 with q2 then clear q2
            else:
                q2.sort()  # Enables traversing in alphabetical order
                q1 = q2.copy()
                q2 = []
            # Explore all nodes in q1
            while (q1 != []):
                vertex_name = q1[0]
                # Add all unvisited neighbours to second queue ...
                # That are not already in second queue.
                for neighbour_name in self.get_neighbours(vertex_name):
                    if (self.visited.get(neighbour_name) == False) and \
                            (neighbour_name not in q2) and (neighbour_name not in q1):
                        q2.append(neighbour_name)
                # Current node is visited, appended to trace, & removed from queue
                self.visited.update({q1[0]: True})
                trace.append(q1[0])
                del q1[0]
        return trace

    def get_unvisited(self) -> List[str]:
        """ Returns unvisited vertices as a list of names """
        rv = []
        for k,v in self.visited.items():  # items or items() ??? Unpack to two items ???
            if (v == False):
                rv.append(k)
        return rv

    def all_visited(self) -> bool:
        """ Returns false if any node is unvisited otherwise True """
        for v in list(self.visited.values()):
            if (v == False):
                return False
        return True

    def depth(self):
        """ Performs depth-first search """
        # Init. unvisited nodes, & starting node
        self.init_visited()
        trace = []
        for node in self.visited.keys():
            if (self.visited.get(node) == False):
                self.depthTrav(node, trace)
        return trace

    def depthTrav(self, v=None, trace=None):
        """ Performs depth-first search """
        trace.append(v)
        self.visited.update({v: True})
        for node in self.get_neighbours(v):
            if (self.visited.get(node) == False):
                self.depthTrav(node, trace)


if __name__ == '__main__':
    # Graph data (Vertices, & edges)
    v = {"A", "B", "C", "D", "E"}
    e = {frozenset({"A", "B"}), frozenset({"B", "D"}), frozenset({"A", "E"}),
         frozenset({"E", "C"}), frozenset({"B", "C"})}

    # Init graph
    graph = Graph(v, e)

    # Display edges, & vertices
    print(graph.e())
    print(graph.v())

    # Display visited nodes in graph
    print(graph.visited)  # Expected None
    graph.init_visited()  # Initialize visited
    print(graph.visited)  # Expected Dict[str, bool]

    # Display the next unvisited node
    print(min(graph.visited))

    # Get neighbours array of chars
    print(graph.get_neighbours('A'))
    print(graph.get_neighbours('B'))

    # Test Breadth
    graph.breadth()