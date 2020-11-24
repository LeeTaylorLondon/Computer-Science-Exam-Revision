# Author: Lee Taylor
# hashing.questions.py
from hashing.linearprobe import *
from random import randint
from typing import List, NoReturn


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

def rswap(a) -> NoReturn:
    """ Perform random swap of two elements in list a """
    # Init. min, max, & ptrs
    _min, _max = 0, len(a)-1
    i = i2 = randint(_min, _max)
    while (i == i2):
        i2 = randint(_min, _max)
    # Perform swap
    temp = a[i]
    a[i] = a[i2]
    a[i2] = temp

def produced() -> NoReturn:
    """
    Given a LinearProbe's values the user must indicate which array
    of random values produced the LinearProbe
    """
    # Init. question variables
    _min, _max, size, lp_size, swap_iters, valid_answers = 11, 64, 6, 8, 12, 0
    # Tries arrays of random integers until only 1 valid answer is possible
    valid = 1
    while (valid_answers != valid):
        vector = return_rarray(_min, _max, size)
        matrix = []
        # Same vector copied 5 times
        for i in range(6):
            matrix.append(vector.copy())
        # Each vector randomized by swapping
        for vector in matrix:
            for swaps in range(swap_iters):
                rswap(vector)
        # Init. Linear Probe
        ans = randint(0, len(matrix)-1)
        lp = LinearProbe(lp_size, matrix[ans])
        # Evaluate random arrays
        valid_answers = 0
        for vector in matrix:
            temp_lp = LinearProbe(lp_size, vector)
            if (f"{temp_lp}" == f"{lp}"):
                valid_answers += 1
    # Question text
    pretext = f"Suppose you have an array of size {size} and have been given\n" \
              "the following simple hash function"
    hashfnc = f"       H(k) = k mod {lp_size}"
    midtext = "Consider the following array produced using hashing with\n" \
              "linear probing:"
    lpvalues = f"       {lp}"
    question = "Inserting which of the following sequences of numbers in\n" \
               "the order given could have produced the above array?"
    arrays = ''
    for i,arr in enumerate(matrix):
        arrays = arrays + f"{i+1}) " + list_to_string(arr) + '\n'
    # Ask question
    print(f"\n\n{pretext}\n{hashfnc}\n{midtext}\n{lpvalues}\n{question}\n{arrays}")
    # Receive user input
    user_inp = str(input("Enter choice (1-5): "))
    # Evaluate user input
    if (user_inp == str(ans + 1)): print(f"Correct!")
    else: print(f"Incorrect ._. Correct answer: {ans+1}")

def result() -> NoReturn:
    """ Given an array of random integers input resultant LinearProbe """
    # Question variables
    lp_size, rsize = randint(8, 12), randint(7, 9)
    rarray = return_rarray(_max=53, size=rsize)
    lp = LinearProbe(lp_size, rarray)
    # Question text
    pretext = f"Suppose you have an array of size {rsize} and have been given\n" \
              "the following simple hash function"
    hashfunc = f"      H(k) = k mod {lp_size}"
    midtext = "Then draw the array that would result from adding following\n" \
              "values in the order they are given using linear probing:"
    array = list_to_string(rarray)
    notetext = "Note you can use a dash '-' to represent an empty array\n" \
               "location."
    # Ask question
    print(f"\n\n{pretext}\n{hashfunc}\n{midtext}\n      {array}\n{notetext}\n")
    # Take user input
    user_inp = str(input("Input answer: ")).strip()
    if (user_inp == f"{lp}"): print('Correct!')
    else: print(f"Incorrect ._. Correct answer: {lp}")

def search() -> NoReturn:
    # Question variables
    lp_size, arr = randint(9, 13), return_rarray(_max=53, size=randint(6, 8))
    lp = LinearProbe(lp_size, arr)
    targets = return_rarray(_max=50, size=2)
    # Pick two findable values in LP.values
    i = i2 = randint(0, len(arr) - 1)
    # Make the pointers unique
    while (i == i2):
        i2 = randint(0, len(arr) - 1)
    # Append the new values to find into targets
    targets.append(arr[i])
    targets.append(arr[i2])
    # Swap random values in targets array
    for swaps in range(6):
        rswap(targets)
    # Question text
    lpinfo = f"Consider the hash function H(k) = k mod {lp_size} and the following hash array\n" \
             f"produced using the above hash function with linear probing:"
    pretext = f"* Search for: {list_to_string(targets)}"
    note = f"Write down the answers on a piece of paper in\n" \
           f"Jason Steggles format shown in his videos. Then\n" \
           f"Compare your answers to the calculated answers!" \
    # Ask question
    print(f"\n\n{lpinfo}\n{pretext}\n     {lp}\n{note}")
    user_inp = str(input("\nPress ENTER to reveal answers!"))
    # Print answers
    for target in targets:
        trace, i = lp.search_traced(target)
        print()
        for line in trace:
            print(line)

def deletion() -> NoReturn:
    """
    User is presented with the values of a Linear Probe (LP) & a value, x, to delete
    the user must input the state of values after deletion of x from LP

    A 'simple' deletion of a value from a Linear Probe can be described as deleting a
    value in which no other values share the same hash. No shifting of values occurs.

    A 'complex' deletion of a value from a Linear Probe can be described as deleting a
    value in which other value(s) share the same hash. As shifting particular values is
    required.

    There is a 15% chance the user is required to answer a simple deletion and 85%
    chance the user will answer a complex deletion.
    """
    shift, delrv = True, None
    if (randint(1, 100) > 85): shift = False
    while (delrv != shift):
        # Init. LinearProbe (LP), & array of random integers
        lp_size, arr = randint(9, 13), return_rarray(_max=64, size=randint(8, 9))
        lp = LinearProbe(lp_size, arr)
        # Randomly pick value to delete
        delval = arr[randint(0, len(arr)-1)]
        # Record state of LP before deletion
        lp_before = f"{lp}"
        # Perform deletion & record whether a shift occurred
        delrv = lp.delete(delval)
    # Record state of LP after deletion
    lp_after = f"{lp}"
    # Question text
    pretext = f"Consider the hash function H(k) = k mod {lp_size} and the following hash array\n" \
              f"produced using the above hash function with linear probing:"
    midtext = f"Show how the key {delval} will be deleted in the above array using the remove and reinsert\n" \
              f"approach for deletion."
    # Ask question
    print(f"\n\n{pretext}\n     {lp_before}\n{midtext}\n")
    # print(f"{lp_before}\n{lp_after}\n{shift}")  # Debug information
    # User input
    user_inp = str(input("Enter LP values after deletion: ")).strip()
    # Mark user answer
    if (user_inp == lp_after): print(f"Correct!")
    else: print(f"Incorrect ._. Correct answer: {lp_after}")

def test_deletion() -> NoReturn:
    """
    Testing LinearProbe.delete(key) to show that it handles special
    or slightly more complex cases of values.

    This test is two special case deletions such that the value deleted
    in each case causes certain values to move around in a particular
    manner that must be maintained in all similar cases.

    Linear Probe 1:
        Given a Linear Probe (LP) where H(k) = int(k) mod 11
            - 12 - - 26 27 59 40 30 19 41
        30, 19, & 41 share the same hash of 8. The special case is as follows:
        deletion of 19 firstly should remove 19, secondly move 41 one left, & lastly
        not move 30 as that is in index 8. Expected result below:
            - 12 - - 26 27 59 40 30 41 -

    Linear Probe 2:
        Given a LP where H(k) = int(k) mod 11
            41 52 63 74 85 96 - - 8 19 30
        Notice that every element in the LP has the same calculated hash value.
        For all k ∈ LP.values, H(k) = 8 is true. Deletion of 19 expected result:
            52 63 74 85 96 - - - 8 30 41
        Note values sharing the same hash as the deletion value must be moved in
        particular manner.
    """
    # Init. Linear Probe (LP) & view state before deletion
    lp = LinearProbe(11, [12, 26, 27, 59, 40, 30, 19, 41])
    print(lp, '(Before deleting 19)')
    # Perform deletion & view state of LP
    lp.delete(19)
    print(lp, '(After deleting 19)', '\n')

    # Init. second LP & view state before deletion
    lp2 = LinearProbe(11, [8, 19, 30, 41, 52, 63, 74, 85, 96])
    print(lp2, '(Before deleting 19)')
    # Perform deletion & view state of LP
    lp2.delete(19)
    print(lp2, '(After deleting 19)')


if __name__ == '__main__':
    # test_deletion()
    questions = {1: produced, 2: result, 3: search, 4: deletion}
    # Infinite loop of randomly picked randomized questions
    while True:
        q = randint(1, 4)
        questions.get(q)()
        del q  # Garbage collect q to prevent a case of being stuck on a single question
