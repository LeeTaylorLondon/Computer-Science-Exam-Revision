from random import randint
from typing import List
from hashing.linearprobe import *


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
    elif not(duplicates):
        if not((m := 1 + _max - _min) >= size):
            raise TypeError('Size {size} too big for {m} unique values! Change _min, _max parameters!')
        rv = {}
        while (len(rv) != size): rv.update({randint(_min,_max): 0})
        return list(rv.keys())


def tests():
    # What would the LinearProbe look like after inserting the following:
    elements = [24, 5, 21, 46, 15, 43, 35]
    lp = LinearProbe()
    for elm in elements:
        lp.insert(elm)
    print(f"{lp}")
    print(f"Possible answer to future exercise.\n")

    # Create LinearProbe then insert two values and search for two values
    lp2 = LinearProbe()
    lp2[0], lp2[3], lp2[5], lp2[6], lp2[7], lp2[9] = 33, 3, 5, 17, 40, 31
    print(lp2)
    # Insertion
    lp2.insert(24), lp2.insert(74)
    print(f"Inserting 24 then 74.\n")
    # Searching
    print(lp2)
    print(f"Searching for 17, 37: {lp2.search(17), lp2.search(37)}")

    # Demonstrating deletion from a LinearProbe
    lp3 = LinearProbe()
    lp3[0], lp3[3], lp3[7], lp3[9] = 22, 3, 40, 31
    print(f"\n{lp3}\nInserting 36 then 58.")
    # Insertion
    lp3.insert(36), lp3.insert(58)
    print(f"\n{lp3}\nDeleting 36. See -> Class LinearProbe method delete(...)")
    # Deletion
    lp3.delete(36)
    print(f"\n{lp3}")

def main():
    pass


if __name__ == '__main__':
    # main()
    tests()