from graph.graphunweighted import *
from graph.graphweighted import *
from random import randint
from typing import List


def list_to_string(a: List[int], pivot=None, si:int=None, ei:int=None, trace:List[str]=None) -> str:
    """
    Returns string of all elements in list a if pivot, si, & ei = None

    Quicksort partitions a list. Passing the index of the pivot. The beginning
    of the partition (starting index -> si). The ending of the partition (ending
    index -> ei). Then a string of that partition along with the pivot highlighted
    is returned.

    :param: si -- starting index of partition : int
    :param: ei -- ending index of partition   : int
    :param: pivot -- index of pivot           : int
    :param: trace -- appends the current state of the list, a,
                     as a str to trace - used in question
                     trace : List[str]
    """
    rv = ''
    if (pivot != None):
        for i,v in enumerate(a):
            if (i != pivot) and (si <= i <= ei): rv = rv + ' ' + str(v)
            elif (i == pivot): rv = rv + f" [{a[pivot]}]"
    else:
        for elm in a: rv = rv + ' ' + str(elm)
    if (trace != None): trace.append(rv[1:])
    return rv[1:]

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

def return_rugraph() -> Graph:
    """ Returns Random Unweighted graph (rugraph) """
    # Init. possible node names, & integer array to chose nodes
    node_names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                  "L", "M"]
    int_arr = [x for x in range(randint(6, len(node_names) - 1))]
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
    # Create graph by passing str of vertices, & list of links as strings
    return Graph(names_str, list(links.keys()))

def return_rcity(_min:int=1, _max:int=100):
    """ Returns a graph where every node is connected to every other node """
    letters = ["A", "B", "C", "D", "E"]
    cities = randint(4, 5)
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

def return_rwgraph(_min:int=1, _max:int=100):
    """ Returns a graph where every node is connected to every other node """
    # Define possible node names
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    # Determine number of nodes to use
    cities = randint(6, 10)
    # Max links represent range of random links to be made
    max_links = 0
    # Max links is equal to i=0Σcities(cities - (i + 1))
    for i in range(cities):
        max_links += cities - (i + 1)
    # Determine random number of links to be made
    links_int = randint(cities, 15)
    # Init. graph data
    v = ''.join(letters[:cities])
    e = ["A" + v[randint(1, len(v)-1)]]  # No link from A causes infinite loop
    # Create links without weights first
    while (len(e) != links_int):
        s = v[randint(0, len(v) -1)] + v[randint(0, len(v) - 1)]
        # If it does not link to itself, and does not already exist
        if not(s[0] == s[1]) and (s[::-1] not in e) and (s not in e):
            # Then add it to edges
            e.append(s)
    # Delete any unused nodes
    temp_str = ''.join(e)
    v2 = ''
    for char in v:
        if (char in temp_str):
            v2 = v2 + char
    v = v2
    # Append weights to those links in e
    for i,s in enumerate(e):
        e[i] = s + str(randint(_min, _max))
    return WeightedGraph(v, e)

def trace_breadth() -> NoReturn:
    """
    User is presented with a random set of vertices and edges
    user must sketch out graph (on paper) & provide breadth trace
    """
    # Init. random graph & breadth trace
    rugraph = return_rugraph()
    breadth = list_to_string(rugraph.breadth())
    # Question
    text = f"\n\nGiven a graph made up of: {rugraph.v()}\nand {rugraph.e()}" + \
           f"\nProvide the order of nodes breadth first search would traverse."
    print(text)
    # Take user input
    user_inp = str(input("\nInput answer: "))
    # Mark answers
    if (user_inp == breadth):
        print("Correct!")
    else:
        print(f"Incorrect -_- Correct answer: {breadth}")

def trace_depth() -> NoReturn:
    """
    User is presented with a random set of vertices and edges
    user must sketch out graph (on paper) & provide depth trace
    """
    # Init. random graph & depth trace
    rugraph = return_rugraph()
    depth = list_to_string(rugraph.depth())
    # Question
    text = f"\n\nGiven a graph made up of: {rugraph.v()}\nand {rugraph.e()}" + \
           f"\nProvide the order of nodes depth first search would traverse."
    print(text)
    # Take user input
    user_inp = str(input("\nInput answer: "))
    # Mark answers
    if (user_inp == depth):
        print("Correct!")
    else:
        print(f"Incorrect -_- Correct answer: {depth}")

def trace_best() -> NoReturn:
    """
    User is presented with a random set of vertices, edges, and a random vertex.
    User must input which traversal algorithm will reach the random vertex first.
    """
    # Init. indexes of target
    d, b, = 0, 0
    # Init random graph
    rugraph = None
    # While loop ensures either depth or breadth will be better
    while (d == b):
        # Init. random graph
        rugraph = return_rugraph()
        rugraph_vertices = list(rugraph.vertices)
        # Init. sorted vertices of graph
        rugraph_vertices.sort()
        # Select random vertex to get to
        target = rugraph_vertices[randint(4, len(rugraph_vertices) - 1)]
        # Trace depth and breadth
        depth = list_to_string(rugraph.depth())
        breadth = list_to_string(rugraph.breadth())
        # Acquire index
        d = depth.find(target)
        b = breadth.find(target)
    # Calculate ans
    if (d > b):
        ans = "breadth"
    else:
        ans = "depth"
    # Question
    text = f"\n\nGiven a graph made up of: {rugraph.v()}\nand {rugraph.e()}" + \
           f"\nWhich search would traverse vertex {target} faster?"
    print(text)
    # Take user input
    user_inp = str(input("\nEnter answer: "))
    # Mark user answer
    if (user_inp == ans):
        print("Correct!")
    else:
        print(f"Incorrect -_- Correct answer: {ans}")
        print(f"Breadth = {breadth}\nDepth = {depth}")

def trace_mst(inp:bool=True):
    # Init. graph & ans
    g = return_rwgraph()
    ans = ' '.join(g.mst())
    # Question
    print(f"\n\nGiven the graph made up of the following sets: \n{g}\nProvide the minimal spanning tree."
          f" In the format <vertex name><cost><space>")
    # User input
    user_inp = ''
    if (inp):
        user_inp = str(input("\nInput answer: "))
    # Mark user ans
    if (user_inp == ans):
        print('\nCorrect!')
    else:
        print(f"\nIncorrect -_- Correct answer: {ans}")

def trace_tsp(debug:bool=False):
    # Init. graph & ans
    g = return_rcity()
    path, weights, _sum = g.tsp()
    # Convert path to string of nodes
    path = ''.join(path)
    # Convert list of ints to list of strings for .join()
    for i,v in enumerate(weights):
        weights[i] = str(v)
    # Create sum ans
    sum_ans = '+'.join(weights) + '=' + str(_sum)
    # Question
    print(f"\n\nGiven the graph made up of the following sets: \n{g}\nProvide the route taken by the nearest "
          f"neighbour algorithm.")
    # Debug
    if (debug):
        print(f"\nDebug ans:\n    {path}\n    {'+'.join(weights)}={_sum}")
    # User input
    path_inp = str(input("\nInput path: "))
    print("Sum format: x+y+z=sum")
    sum_inp = str(input("Input sum: "))
    # Mark user ans
    if (path_inp == path) and (sum_inp == sum_ans):
        print('\nCorrect!')
    else:
        print(f"\nIncorrect -_- Correct answer: {path}\n{'+'.join(weights)}={_sum}")


if __name__ == '__main__':
    # trace_mst()
    for calls in range(100):
        trace_tsp(True)
    # trace_depth()
    # trace_breadth()
    # trace_best()
