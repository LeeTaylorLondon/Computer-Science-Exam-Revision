from typing import List, NoReturn
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


""" Swaps two elements given indexes, i & i2, in given list, a. """
def swap_traced(a: List[int], i: int, i2: int, llt, p:int=None, si:int=None, ei:int=None, w=True) -> NoReturn:
    """
    Swaps two elements in a list. If & only if this function is passed
    more than 3 parameters then this will swap items & append the swap to
    param llt. If recorded the pivot can also be highlighted.
    :param: a   -- Reference to the array to perform swap on : List[int]
    :param: i   -- Reference to one of the elements to swap  : int
    :param: i2  -- Reference to one of the elements to swap  : int
    :param: llt -- A swap is recorded and appended to this array : List[str]
    :param: p   -- If swap is recorded this points to the element to highlight.
                   Used to highlight the pivot in question-function -> wrong()
                   : int
    :param: si  -- Starting index. Where to start recording from in the list : int
    :param: ei  -- Ending index. Where to end recording in the list          : int
    :param: w   -- Used in question-function -> wrong() to sabotage the
                   trace only once. Also to tell which line is sabotaged     : bool
    """
    if (w == False) and (llt != None): llt.append(f"*Swap values {a[i]} and {a[i2]}")
    elif (w) and (llt != None): llt.append(f"Swap values {a[i]} and {a[i2]}")
    temp  = a[i]
    a[i]  = a[i2]
    a[i2] = temp
    if (llt != None): llt.append(f"             {list_to_string(a, p, si, ei)}")


def quicksort_traced(a: List[int], pl: int, pr: int, llt, trace:List[str]=None, w=False) -> NoReturn:
    """
    A variation of quicksort in which low level or high level traces can be recorded.
    Note: There is a much simpler solution however I just want something to revise from
          now!
    :param: a     -- array to be sorted : List[int]
    :param: pl    -- left pointer      : int
    :param: pr    -- right pointer     : int
    :param: llt   -- reference to an array of low level traces to be recorded
                     used in question -> wrong() : List[str]
    :param: trace -- reference to an array of high level traces to be recorded
                     used in question -> trace() : List[str]
    :param: w     -- used for question -> wrong() used to ensure only a single
                     llt is sabotaged : List[str]
    """
    if (w):
        ans = partition_traced(a, pl, pr, llt, trace, w)
        return ans
    if (pr > pl):
        p = partition_traced(a, pl, pr, llt, trace, False)
        quicksort_traced(a, pl, p-1, llt, trace)
        quicksort_traced(a, p+1, pr, llt, trace)


def partition_traced(a: List[int], l: int, r: int, llt, trace:List[str], w=False) -> NoReturn:
    # list_to_string used for question-function -> trace(...)
    # if (trace != None): trace.append(f"L={l} R={r} Pivot={a[r]}")
    list_to_string(a, pivot=r, si=l, ei=r, trace=trace)
    pl, pr = l, r
    v = a[pr]
    while (pl < pr):
        while (a[pl] < v): pl += 1
        while (a[pr] >= v) and (pr > l): pr -= 1
        if (pl < pr):
            if (w) and (randint(0,1)):
                pl = randint(pl+1, len(a)-1)
                w = False
            swap_traced(a, pl, pr, llt, r, l, r, w)
    swap_traced(a, pl, r, llt, pl, l, r)
    # list_to_string used for question-function -> trace(...)
    list_to_string(a, pivot=pl, si=l, ei=r, trace=trace)
    return pl


""" 
Questions presented to the user - as functions
    trace -- user inputs high-level traces for array of randint's 
"""
def trace(array: List[int]=[]) -> int:
    """
    User is presented with an array of random integers, the user must
    provide a high level trace of quick-sort applied to the array.

    NOTE -- Variable: 'traces' a List containing each trace as a string.
    To append each trace, the reference to this list has to be passed
    through out the functions used in quicksort:
        quicksort_traced(...), partition_traced(...), & list_to_string(...)

    """

    # Init. traces, user_inp
    traces, user_inp = [], []
    # Init. rarray -> if no array is passed an array of random integers is traced
    if (array == []): rarray = return_rarray(size=9)
    else            : rarray = array
    # quicksort_traced(...) appends each trace to passed list 'traces'
    traces.append(list_to_string(rarray))
    quicksort_traced(rarray, 0, len(rarray)-1, llt=None, trace=traces)
    user_inp.append(traces[0])
    # Prompt user with question
    print(f'\nProvide a high level trace of quick sort applied to the array below.\n    {traces[0]}'
          # f"\n    Format = (Jason Steggles' Format with Example Below):"
          # f"\n        L=0, R=4: Pivot is 5 <Input left & right pointer values, & pivot value. Press Enter>"
          # f"\n        1 2 3 4 [5] <Input array from pl to pr with pivot in square brackets. Press Enter>"
          # f"\n        1 2 3 4 [5] <Input array after partition algorithm has run with pivot highlighted. Press Enter"
          # f" & Repeat>\n"
          )
    # User inputs each trace
    for inp in range(1, len(traces)):
        user_inp.append(str(input(f"Enter line: ")).strip())
    # Mark answers provided by user
    correct = 0
    for a, ua in zip(traces, user_inp):
        if (a.lower() == ua.lower()): correct += 1
    # Display user's mark
    if (correct != len(traces)): print(f"<You scored [{correct-1}/"
                                       f"{len(traces)-1}] ._. >\n")
    else: print(f"<You scored [{correct-1}/{len(traces)-1}]!>\n")
    # If the user did not achieve full marks then display the answers
    if (correct != len(traces)):
        for a, ua in zip(traces, user_inp):
            print(f"Your answer: {ua}\nReal Answer: {a}")
        print()
    return correct


def spot_wrong():
    """
    User is presented with low level traces of quicksort.
    One of the lines may be wrong the user must respond with the line or 'none'.
    """
    # llt -> low-level-traces
    llt = []
    # Generates traces based off of random arrays
    # Only present random combinations that results in many traces
    while (len(llt) < 10):
        rarray = return_rarray(size=8)
        llt.append(f"Select Pivot = {rarray[-1]}")
        llt.append(f"             {list_to_string(rarray, len(rarray)-1, 0, len(rarray))}")
        # Call Qsort_traced passing 'llt' and True to only initiate a single partition run
        quicksort_traced(rarray, 0, 7, llt, w=True)
        # If the random combination return too few traces this store is wiped
        if (len(llt) < 10): llt = []
    # Calculates the answer based off of the traces
    # To calculate which line is wrong the first char contains '*'
    ans = -1
    for i,line in enumerate(llt):
        # The '*' is found and removed - var ans is set to the current index
        if (line.__contains__("*")) and (ans <= -1):
            ans = i
            llt[i] = line[1:]
        # Subsequent lines containing '*' are changed not to have that char
        elif (line.__contains__("*")): llt[i] = line[1:]
    # Map answer & convert to string
    answer_map = {2: '2', 4: '3', 6: '4', -1: 'none'}
    ans = answer_map.get(ans)
    # Ask question
    print("\nIdentify what is wrong with the following high-level traces for the partition"
          " algorithm.\nIf you think nothing is wrong type 'none' otherwise type the step number. \n")
    for i,line in enumerate(llt):
        if (i % 2 == 0): print(f"Step {int(i/2)+1}) {line}")
        else: print(line)
    # User input
    user_inp = str(input("Enter answer: "))
    if (user_inp != ans): print(f"<Incorrect ._. Correct answer: {ans}>")
    else: print(f"<Correct!>")


def test_trace():
    for calls in range(4): print(), trace()


if __name__ == '__main__':
    while True:
        test_trace()
        spot_wrong()