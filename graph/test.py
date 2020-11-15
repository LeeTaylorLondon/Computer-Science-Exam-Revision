from graph.graphunweighted import *
from graphunweighted import *
from random import randint


""" ### Graph 1 ### """

# Graph data (Vertices, & edges)
v = {"A", "B", "C", "D", "E"}
e = {frozenset({"A", "B"}), frozenset({"B", "D"}), frozenset({"A", "E"}),
     frozenset({"E", "C"}), frozenset({"B", "C"})}

# Init graph
graph = Graph(v, e)

# Display edges, & vertices
print(f"\n{graph}")

# Test Breadth & Depth
print(f"Breadth: {graph.breadth()}")
print(f"Breadth: {graph.breadth()}")
print(f"Depth: {graph.depth()}")


""" ### Graph 2 ### """

# Test 'polymorphism' *After-test: IT WORKS! =)
v = "ABCDEFG"
e = ["AB", "BD", "AE", "EC", "BC", "FG"]
graph2 = Graph(v, e)

# Display edges, & vertices
print(f"\n{graph2}")

# Test Breadth
print(f"Breadth: {graph2.breadth()}")
print(f"Breadth: {graph2.breadth()}")
print(f"Depth: {graph2.depth()}")


""" ### Graph 3 ### """

# Graph data (Vertices, & edges)
v = "FABDCEGHI"
e = ["FA", "AB", "AD", "DC", "BC", "DB",
     "BE", "EH", "EG", "GI"]

# Init graph, & display
graph3 = Graph(v, e)
print(f"\n{graph3}")

# Test Breadth
print(f"Breadth: {graph3.breadth()}")
print(f"Breadth: {graph3.breadth()}")
print(f"Depth: {graph3.depth()}")


def return_rarray(_min=1, _max=10, size=5, duplicates=False) -> List[int]:
    """
    Returns array of random elements [x0, x1, ..., xn]
    for each element in the range (_min >= x >= _max).
    Where the number of elements equals parameter -> size.

    :param: _min -- int
        the smallest possible integer that could be randomly generated
    :param: _max -- int
        the largest possible integer that could be randomly generated
    :param: size -- int
        the number of elements appended to the array
    :param: duplicates -- boolean
        if True, elements of equal value may be generated otherwise
        all elements are unique

    """

    if (duplicates):
        rv = []
        for i in range(size): rv.append(randint(_min, _max))
        return rv
    elif not (duplicates):
        if not ((m := 1 + _max - _min) >= size):
            raise TypeError('Size {size} too big for {m} unique values! Change _min, _max parameters!')
        rv = {}
        while (len(rv) != size): rv.update({randint(_min, _max): 0})
        return list(rv.keys())

def return_rugraph():
    """ Returns Random Unweighted graph (rugraph) """
    # Init. possible node names, & integer array to chose nodes
    node_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    int_arr = [x for x in range(randint(4, 10))]
    # Create str of random node names
    names_str = ''
    for n in int_arr:
        names_str = names_str + node_names[n]
    # Create links
    links = {}
    loops = randint(len(int_arr) - 1, len(int_arr) + 2)
    while (len(links) != loops):
        char_sta = names_str[randint(0, len(names_str) - 1)]
        char_end = names_str[randint(0, len(names_str) - 1)]
        if (char_sta == char_end):
             continue
        if (char_sta + char_end not in links) and (char_end + char_sta not in links):
            links.update({char_sta + char_end: char_sta + char_end})
    # Crete graph by passing str of vertices, & list of links as strings
    return Graph(names_str, list(links.keys()))


""" ### Test Function -> Return Random Unweighted Graph ### """
print(f"\nRandom Graph: ")
rugraph = return_rugraph()
print(rugraph)
print(f"Breadth: {rugraph.breadth()}")
print(f"Depth: {rugraph.depth()}")


""" ### Graph 4 (From return_rugraph(...)) ### """
v = "ABCDEFG"
e = ["FA", "EG", "DE", "EF", "FB",
     "GC", "EA", "AG", "DG"]
graph4 = Graph(v, e)

print()
print(graph4)
print(f"Breadth: {graph4.breadth()}")
print(f"Breadth: {graph4.breadth()}")