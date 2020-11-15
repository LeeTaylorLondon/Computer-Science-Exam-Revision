# from functions.functions_ import *
from typing import List
from math import ceil
from random import randint

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

"""
Jason Steggles' binary search trace format:
    * Search for 14 in the array:
        2 3 5 6 8 10 12 14 17 18 21 23

        2 3 5 6 8 [10] 12 14 17 18 21 23
    L=0, R=12, key:=14
    m:=(0+12)/2 = 6
    (14 > 10) Right

        12 14 17 [18] 21 23
    L=7, R=12
    m:= (7+12)/2 = 9.5 = 10
    (14 < 18) Left

        12 [14] 17
    L=7, R=9
    m:=(7+9)/2 = 8
    (14 = 14) Found!
"""
def bin_search(a: List[int], key: int, l: int, r: int) -> int:
    if (r < l): return -1
    m = ceil((r + l) / 2)  # math.ceil rounds up
    if (key == a[m]): return m
    if (key > a[m]) : return bin_search(a, key, m+1, r)
    else: return bin_search(a, key, l, m-1)


def binsearch_traced(a: List[int], key: int, l: int, r: int, trace: List[str]) -> int:
    # binsearch pointer comparison
    if (r < l): return -1
    # binsearch calc midpoint
    m = ceil((r + l) / 2)
    # traces append midpoint value
    list_to_string(a, m, l, r, trace)
    # traces append left & right pointers, & possibly the key
    if (len(trace) == 1): trace.append(f"L={l}, R={r}, key:={key}")
    else: trace.append(f"L={l}, R={r}")
    # traces append calculation for m -> user must show round implemented
    if (int((r+l)/2) == (r+l)/2): trace.append(f"m:=({l}+{r})/2 = {m}")
    else: trace.append(f"m:=({l}+{r})/2 = {m-0.5} = {m}")
    # traces append key and A[m] comparison
    if (r <= l) and (key != a[m]): trace.append(f"L={l}, R={r} Not found")
    elif (key > a[m]): trace.append(f"({key} > {a[m]}) Right")
    elif (key < a[m]): trace.append(f"({key} < {a[m]}) Left")
    elif (key == a[m]): trace.append(f"({key} = {a[m]}) Found")
    # binsearch check midpoint
    if (key == a[m]): return m
    if (key > a[m]) : return binsearch_traced(a, key, m+1, r, trace)
    else: return binsearch_traced(a, key, l, m-1, trace)

def binsearch_traced_simple(a: List[int], key: int, l: int, r: int, trace: List[str]) -> int:
    # binsearch pointer comparison
    if (r < l): return -1
    # binsearch calc midpoint
    m = ceil((r + l) / 2)
    # traces append calculation for m -> user must show round implemented
    trace.append(f"l={l} r={r} m={m}")
    # binsearch check midpoint
    if (key == a[m]): return m
    if (key > a[m]) : return binsearch_traced_simple(a, key, m+1, r, trace)
    else: return binsearch_traced_simple(a, key, l, m-1, trace)




