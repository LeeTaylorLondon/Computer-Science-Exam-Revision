from questions import *

""" Functions for testing other functions """

def test_trace(iter: int=1):
    """ Iteratively call question trace """
    for calls in range(iter): trace(True)

def test_recursive(iter: int=1):
    """ Iteratively call question recursive calls """
    for calls in range(iter): recursive_calls()

def test_binsearch():
    """ Normal search for plain original algorithm """
    arr = [2, 3, 5, 6, 8, 9, 10, 12, 14, 17, 18, 21, 23]
    rv = bin_search(arr, 14, 0, len(arr)-1)
    print(rv)

def test_trace_simple(iter: int=1):
    """ Iteratively call question trace """
    for calls in range(iter): trace()

if __name__ == "__main__":
    # test_binsearch()
    test_trace(5)
    test_recursive()