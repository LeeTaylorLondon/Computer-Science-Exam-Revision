from graph.graphunweighted import *
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


if __name__ == '__main__':
    trace_depth()
    trace_breadth()
    trace_best()