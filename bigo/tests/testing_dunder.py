from types_ import LogN, NLogN
from types_ import Integer     as Int
from types_ import Polynomial  as Pol
from types_ import Exponential as Exp
from typing import List

int   = Int()
logn  = LogN()
lin   = Pol().linearfy()
nlogn = NLogN()
poly  = Pol().quadraticfy()
expo  = Exp()
fac   = Pol().factorialfy()

VALS = [int, logn, lin, nlogn, poly, expo, fac]

# Dunder comparative methods
# == >= > <= < !=

def values():
    for v in VALS: print(f"{type(v)}\n  f(N) -> {v} -> {v.bigo()}\n")

def truth(exp) -> str:
    """ Converts return of expression from 1,0 to corresponding bool """
    return '[FALSE]' if (exp == 0) else '[TRUE]'

def test_eq(arr=None):
    """ Tests __eq__ methods : == """
    if arr is None:
        arr = VALS
    for i,v in enumerate(arr):
        print()
        for i2,v2 in enumerate(arr):
            try:
                print(f"({v} == {v2}) -> {truth(v == v2)} {v.classification(), v2.classification()} [{i}][{i2}]")
            except NameError:
                print(f"Error: {i, i2}")
                return

def test_ge(arr=None):
    """ Test __ge__ methods : >= """
    if arr is None:
        arr = VALS
    for i,v in enumerate(arr):
        print()
        for i2,v2 in enumerate(arr):
            try:
                print(f"({v} >= {v2}) -> {truth(v >= v2)} {v.classification(), v2.classification()} [{i}][{i2}]")
            except NameError:
                print(f"Error: {i, i2}")
                return

def test_gt(arr=None):
    """ Test __gt__ methods : > """
    if arr is None:
        arr = VALS
    for i,v in enumerate(arr):
        print()
        for i2,v2 in enumerate(arr):
            try:
                print(f"({v} > {v2}) -> {truth(v > v2)} {v.classification(), v2.classification()} [{i}][{i2}]")
            except NameError:
                print(f"Error: {i, i2}")
                return

def test_le(arr=None):
    """ Test __gt__ methods : > """
    if arr is None:
        arr = VALS
    for i,v in enumerate(arr):
        print()
        for i2,v2 in enumerate(arr):
            try:
                print(f"({v} <= {v2}) -> {truth(v <= v2)} {v.classification(), v2.classification()} [{i}][{i2}]")
            except NameError:
                print(f"Error: {i, i2}")
                return

def test_lt(arr=None):
    """ Test __gt__ methods : > """
    if arr is None:
        arr = VALS
    for i,v in enumerate(arr):
        print()
        for i2,v2 in enumerate(arr):
            try:
                print(f"({v} < {v2}) -> {truth(v < v2)} {v.classification(), v2.classification()} [{i}][{i2}]")
            except NameError:
                print(f"Error: {i, i2}")
                return

def test_ne(arr=None):
    """ Test __gt__ methods : > """
    if arr is None:
        arr = VALS
    for i,v in enumerate(arr):
        print()
        for i2,v2 in enumerate(arr):
            try:
                print(f"({v} != {v2}) -> {truth(v != v2)} {v.classification(), v2.classification()} [{i}][{i2}]")
            except NameError:
                print(f"Error: {i, i2}")
                return

def test_all_per_value():
    """
    Tests __eq__, __ge__, __gt__, __le__, __lt__, __ne__.
    In that order for each value against each value
    """
    for i,v in enumerate(VALS):
        print()
        for i2,v2 in enumerate(VALS):
            try:
                print(f"({v} == {v2}) -> {truth(v == v2)} <{v2.classification()}> [{i}][{i2}]")
                print(f"({v} >= {v2}) -> {truth(v >= v2)} <{v2.classification()}> [{i}][{i2}]")
                print(f"({v} >  {v2}) -> {truth(v >  v2)} <{v2.classification()}> [{i}][{i2}]")
                print(f"({v} <= {v2}) -> {truth(v <= v2)} <{v2.classification()}> [{i}][{i2}]")
                print(f"({v} <  {v2}) -> {truth(v <  v2)} <{v2.classification()}> [{i}][{i2}]")
                print(f"({v} != {v2}) -> {truth(v != v2)} <{v2.classification()}> [{i}][{i2}]")
            except NameError:
                print(f"Error: {i, i2}")
                return

def polynomial_tests():
    """ Test groups of random Linear, Quadratic, & Factorial values against each other """
    def init_values(_max=5):
        values = [[Pol().linearfy()    for x in range(_max)],
                  [Pol().quadraticfy() for x in range(_max)],
                  [Pol().factorialfy() for x in range(_max)]]
        return values

    values = init_values()

    for arr in values[2:]:
        # test_eq(arr)
        test_ge(arr)
        test_gt(arr)
        # test_le(arr)
        # test_lt(arr)
        # test_ne(arr)

values()
test_eq()
test_ge()
test_gt()
test_le()
test_lt()
test_ne()
test_all_per_value()
polynomial_tests()