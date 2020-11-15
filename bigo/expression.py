from typing import List
from bigo.types_ import *


TYPES = { 1: Integer,
          2: LogN,
          3: NLogN,
          4: Exponential,
          5: Polynomial }


class Expression:
    """
    Expression class designed to hold objects of types defined in types_.py
    Objects from types_.py are modeled after Big O classifications.
    """

    def __init__(self, terms=7):
        self.terms = self.init_terms(terms)

    def __repr__(self):
        rv = ''
        for t in self.terms: rv = rv + ' + ' + str(t)
        return rv[3:]

    def init_terms(self, terms: int) -> List[object]:
        """ Return list of objects of types defined in TYPES """
        rv = []
        for x in range(terms):
            rv.append(TYPES.get(randint(1, 5))())
        for elm in rv:
            if (type(elm) == Polynomial):
                poly_type = randint(1, 3)
                if (poly_type == 1): elm.linearfy()
                if (poly_type == 2): elm.quadraticfy()
                if (poly_type == 3): elm.factorialfy()
        return rv

    def bigo(self):
        return max(self.terms).bigo()


def test():
    while (True):
        terms = randint(2, 6)
        tempE = Expression(terms=terms)
        print(f"\nWhat is the Big-O of:\n     {tempE}")
        user_inp = str(input("\nEnter answer: "))
        print("Correct!") if (user_inp.lower() == tempE.bigo().lower())\
    else print(f"Incorrect ._. \nCorrect Answer:{tempE.bigo()}")


if __name__ == '__main__':
    test()