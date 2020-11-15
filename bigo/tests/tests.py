from expression import Expression
from types_     import *

""" Init. polynomials and expressions """
p1, p2 = Polynomial(), Polynomial()
p3, p3.power = Polynomial(), 1
e1, e2 = Expression(), Expression()

"""
Create specific expression with only 1 factorial to the power of 1
To test the Big-O of expression method to see if it picks out the
right polynomial
"""
pe0, pe1, pe2, pe3, pe4 = Polynomial(), Polynomial(), Polynomial(), Polynomial(), Polynomial()
pe0.factorial, pe1.factorial, pe2.factorial, pe3.factorial, pe4.factorial = 1, 0, 0, 0, 0
pe0.power, ep_terms = 1, [pe0, pe1, pe2, pe3, pe4]
ep, ep.terms = Expression(), ep_terms


def main(tests=False):
    if (tests):

        print(f"<Polynomials p1=[{p1}] p2=[{p2}]>\n")

        p1.measure_growth()
        print()

        p2.measure_growth()
        print()

        # print(p1.compare_growth(p2))
        # print()

        print(f"Polynomials reduced:\n   {p1} -> {p1.bigo()}\n   {p2} -> {p2.bigo()}")
        print()

        print(f"Variable reduced: {p3} -> {p3.bigo()}")
        print()

        print(f"Expression: {e1}\nExpression: {e2}")
        print()

if __name__ == '__main__':
    main()