from typing import List, NoReturn

"""
NOTE: below extract of pseudo code found in
Jason Steggles' lecture/module notes. Link
to Jason Steggles can be found in README.md.
----------------------------------------------
<Partitioning the Array: Pseudo Code>
----------------------------------------------
Algorithm Partition
Inputs    A : Array of Integers, L, R: Integer
Returns   pL: Integer
Variables pL,pR,v : Integer
Begin
    v := A[R]
    pL := L; pR := R
    while (pL < pR) do
        while (A[pL] < v) do pL:=pL+1
        while (A[pR]>= v and pR > L) do pR:=pR=1
        if (pL < pR) then swap(A,pL,pR)
    swap(A,pL,R)
    return pL
-------------------------------------------
<Quicksort Algorithm: Pseudo Code>
-------------------------------------------
Algorithm quickSort
Inputs    A: Array of Integers; L,R:Integer
Variables p: Integer
Begin 
    if (R > L) then
        p := partition(A,L,R)
        quickSort(A,L,p-1)
        quickSort(A,p+1,R)
End

"""


def swap(a: List[int], i: int, i2: int) -> NoReturn:
    """ Swaps two elements given indexes, i & i2, in given list, a. """
    temp  = a[i]
    a[i]  = a[i2]
    a[i2] = temp


def quicksort(a: List[int], pl: int, pr: int) -> NoReturn:
    # Start with quicksort(A, 0, N-1) | where N = len(A)
    if (pr > pl):
        p = partition(a, pl, pr)
        quicksort(a, pl, p-1)
        quicksort(a, p+1, pr)


def partition(a: List[int], l: int, r: int) -> NoReturn:
    pl, pr = l, r
    v = a[pr]  # Init. pivot value
    while (pl < pr):
        while (a[pl] < v): pl += 1
        while (a[pr] >= v) and (pr > l): pr -= 1
        if (pl < pr): swap(a, pl, pr)
    swap(a, pl, r)
    return pl


def main():
    e = [7, 2, 8, 3, 10, 6, 4, 9, 5]
    print(e)
    quicksort(e, 0, len(e)-1)
    print(e)

if __name__ == '__main__':
    main()
