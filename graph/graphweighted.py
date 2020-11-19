from typing import List, NoReturn
from graph.graphunweighted import Graph
from math import inf
from random import randint
import re


class WeightedGraph(Graph):
    def __init__(self, v, e):
        # Init. Vertices
        if (type(v) == str):
            st = set()
            for elm in v:
                st.update(elm.upper())
            self.vertices = st
        else:
            self.vertices = v
        # Set self.e (edges) -> Can pass 'e' or 'edges' as a list of strings
        if (type(e) == list) and (type(v) == str):
            sete = set()
            for elm in e:
                # Todo -> change to allow names of up to more than a single char
                temp_fset = frozenset({elm[0].upper(), elm[1].upper()})
                sete.add(temp_fset)
            self.edges = sete
        else:
            self.edges = e
        # Init. visited to None
        self.visited = None
        # Init. Weights
        self.weights = {}
        for s in e:
            link_str = ''
            link_int = ''
            for c in s:
                if (re.search("[0-9]", c) != None):
                    link_int = link_int + c
                else:
                    link_str = link_str + c
            link_int = int(link_int)
            self.weights.update({link_str: link_int})
            self.weights.update({link_str[::-1]: link_int})

    def __repr__(self):
        return f"{self.v()}\nWeights ({int(len(self.weights)/2)}): {self.w()}"

    def w(self) -> str:
        rv = ''
        counter = 0
        for pair in self.weights.items():
            counter += 1
            if (counter % 2 == 0):
                rv = rv + f"{pair[0]}:{pair[1]} "
        return rv

    def mst(self) -> List[str]:
        """ Return the path taken by the MST algorithm """
        # Mark all as unvisited
        self.init_visited()
        # Init. current node, node names, weights, & trace
        current_node = min(self.visited)
        node_names = list(self.visited.keys())
        weights = [inf for x in range(len(node_names))]
        weights[0] = 0
        trace = [current_node + '0']
        # Outer while loop accounts for disjoint sets
        while (not self.all_visited()):
            if (current_node == None):
                nodes = []
                for node in list(self.visited.keys()):
                    if (self.visited.get(node) == False):
                        nodes.append(node)
                current_node = min(nodes)
                trace.append(current_node + '0')
            # Exploration loop
            while (not self.all_visited()):
                # Set current node visited
                self.visited.update({current_node: True})
                # Break out of this loop if current node is None
                if (current_node == None):
                    break
                # Get neighbours of current node
                neighbours = self.get_neighbours(current_node)
                # Update func-weights during exploration of current node and neighbours
                for i,v in enumerate(node_names):
                    if (v in neighbours):
                        # Replace weight val if found weight is < current weight val
                        if (self.weights.get(current_node + v) < weights[i]):
                            weights[i] = self.weights.get(current_node + v)
                    else:
                        continue
                # Find least costly route & init. index, value
                index_of_min, min_value, next_node, i = -1, inf, None, 0
                for v,w in zip(node_names, weights):
                    i += 1
                    # Replace node name and val with smallest found
                    if (self.visited.get(v) == False) and (w < min_value):
                        index_of_min = i
                        min_value = w
                        next_node = v
                # Set current node for next trace
                current_node = next_node
                # Update trace
                if (index_of_min != -1) and (min_value != inf):
                    trace.append(current_node + str(min_value))
        return trace

    def tsp(self, start:str='A'):
        """ Returns the path taken by nearest neighbour algorithm """
        start = start.upper()
        self.init_visited()
        # Init. current, sum, weights and trace
        current_node = start
        sum = 0
        sum_arr = []
        weights = []
        trace = []
        while (not self.all_visited()):
            # Mark current node as visited & update trace
            self.visited.update({current_node: True})
            trace.append(current_node)
            # Get neighbours of current node
            neighbours = self.get_neighbours(start)
            # Delete neighbour nodes that have already been visited
            for i,n in enumerate(neighbours):
                if (self.visited.get(n) == True):
                    neighbours[i] = None
            # Get costs associated with neighbours
            for n in neighbours:
                if (n != None):
                    weights.append(self.weights.get(current_node + n))
                else:
                    weights.append(None)
            # Find min val and index
            val, ind = weights[0], 0
            for i,x in enumerate(weights):
                # print(self)
                # print(f"x={x}, val={val}, w={weights}")
                if (x != None):
                    if (val == None) or (x < val):
                        val = x
                        ind = i
            if (val != None):
                sum_arr.append(str(val))
                sum += val
            # Set current node to index
            if (neighbours[ind] != None):
                current_node = neighbours[ind]
            # Clear weights and neighbours
            weights, neighbours = [], []
        # Link back to starting node
        trace.append(start)
        sum += self.weights.get(start + current_node)
        sum_arr.append(str(self.weights.get(start + current_node)))
        # Return tuple of path, weights, and sum
        return trace, sum_arr, sum

    def all_cycles(self):
        """ (self.v-1)! Runtime """
        pass

def return_rcity_dev(_min:int=1, _max:int=100):
    """ Returns a graph where every node is connected to every other node """
    letters = ["A", "B", "C", "D", "E"]
    cities = randint(3, 5)
    v = ''.join(letters[:cities])
    e = []
    # Create links with only node names i.e -> AB BC AC
    for i,c in enumerate(v):
        for i2 in range(len(v)):
            if (v[i] != v[i2]) and (v[i] + v[i2] not in e) and \
                    (v[i2] + v[i] not in e):
                e.append(c + v[i2])
    # Append weight cost to each link
    for i,link in enumerate(e):
        e[i] = link + str(randint(_min, _max))
    return WeightedGraph(v, e)

if __name__ == '__main__':
    # ''' ### Graph 1 ### '''
    #
    # # v = "NLMB"
    # # e = ["NL98", "NB206", "NM145",
    # #      "ML45", "MB86", "BL119"]
    # # g = WeightedGraph(v, e)
    # # print(g)
    # # g.tsp('N')
    #
    # # newline
    # print()
    #
    # ''' ### Graph 2 ### '''
    #
    # v2 = "ABCDEF"
    # e2 = ["AB5", "AD2", "AE6", "AC3",
    #       "BD1", "DC4", "EC5", "BE7",
    #       "DF6", "CF7"]
    # g2 = WeightedGraph(v2, e2)
    # # print(g2)
    # # print(g2.weights)
    # rv = g2.mst()
    # # print(rv)
    #
    # ''' ### Random City Graph ### '''
    #
    # g3 = return_rcity_dev()
    # # print(g3)
    #
    # mst = g3.mst()
    # print(f"\nmst={mst}\n")
    #
    # tsp = g3.tsp()
    # print(f"tsp={tsp}")
    #
    # ''' ### Graph 4 - Extract from Tutorial 4.4.2 ### '''
    #
    # v4 = "ABCDE"
    # e4 = ["AB11", "AC3", "AD15", "AE5",
    #       "BC14", "DB7", "BE10", "CD8",
    #       "CE4", "DE11"]
    # g4 = WeightedGraph(v4, e4)
    # print(f"\n{g4}")
    # print(f"\ng4.tsp()={g4.tsp()}")

    """ ### Disjointed Graph ### """

    # Create Graph
    v = "CGBHIEJAFD"
    e = ["GA46", "EG77", "BH45", "IG27",
         "CD90", "HJ8", "HE43", "GB59",
         "JF75", "EB23"]
    g = WeightedGraph(v, e)
    # Acquire Minimal Spanning Tree
    mst = g.mst()
    print(mst)