from typing import NoReturn
from random import randint

"""
Big O of an algorithm drops the constants even in the case such as
n*10^6 -> O(n) [Incorporate this possible in revision]
"""
class Integer:
    def __init__(self):
        self.value   = round(randint(1, 150000), -2)
        self.power   = self.init_power()
        self.divisor = self.init_divisor()
        self.factor  = self.init_factor()

    def __repr__(self):
        rv = str(self.value)
        if (self.power > 1): rv = rv + (f"^{self.power}")
        if (self.factor[0] > 1):
            rv = rv + (f"*{self.factor[0]}")
            if (self.factor[1] > 1):
                rv = rv + (f"^{self.factor[1]}")
        if (self.divisor > 1): rv = rv + (f"/{self.divisor}")
        return rv

    def __eq__(self, o):
        return 1 if (type(o) == Integer) else 0

    def __ge__(self, o):
        return 1 if (type(o) == Integer) else 0

    def __gt__(self, o):
        return 0

    def __le__(self, o):
        return 1

    def __lt__(self, o):
        return 1 if (type(o) != Integer) else 0

    def __ne__(self, o):
        return 1 if (type(o) != Integer) else 0

    def init_power(self):
        if (randint(0, 2) > 0): return 1
        else: return randint(2, 10)

    def init_divisor(self):
        if (randint(0, 2) > 0): return 1
        else: return randint(2, 6)

    def init_factor(self):
        rv = []
        factor, fpower = randint(0, 2), randint(0, 2)
        rv.append(randint(2, 10)) if (factor > 0) else rv.append(1)
        rv.append(randint(2, 10)) if (fpower > 0) else rv.append(1)
        return rv

    def bigo(self):
        return 'O(1)'

    def classification(self):
        return f"Constant"


class LogN:
    def __init__(self):
        pass

    def __eq__(self, o):
        return 1 if (type(o) == LogN) else 0

    def __ge__(self, o):
        return 1 if (type(o) in (LogN, Integer)) else 0

    def __gt__(self, o):
        return 1 if (type(o) == Integer) else 0

    def __le__(self, o):
        return 0 if (type(o) == Integer) else 1

    def __lt__(self, o):
        return 1 if (type(o) in (Polynomial, NLogN, Exponential)) else 0

    def __ne__(self, o):
        return 1 if (type(o) != LogN) else 0

    def __repr__(self) -> str:
        return f"log n"

    def bigo(self) -> str:
        return "O(log n)"

    def classification(self) -> str:
        return f"LogN"


class Polynomial:
    def __init__(self):
        self.coeff = randint(0, 12)
        self.letter = 'n'
        self.power = randint(1, 10)
        self.divisor = randint(1, 3)
        self.factorial = self.init_factorial()

    def __repr__(self):
        """ Return string of polynomial. """
        rv = ''
        if (self.coeff > 1): rv = rv + str(self.coeff)
        rv = rv + self.letter
        if (self.power != 1): rv = rv + '^' + str(self.power)
        if (self.factorial): rv = rv + '!'
        if (self.divisor > 1): rv = rv + f"/{self.divisor}"
        return rv

    def __eq__(self, p):
        if (type(p) == Polynomial) and (p.power == self.power) and (self.factorial == p.factorial):
            return 1
        if (type(p) == Polynomial) and (p.power == self.power):
            return 1
        else: return 0

    def __ne__(self, p):
        if (type(p) != Polynomial): return 1
        if (p.factorial != self.factorial): return 1
        if (p.power != self.power): return 1
        else: return 0

    def __ge__(self, p):
        # (Linear, Quadratic, Factorial) > (Integer, LogN)
        if (type(p) in (Integer, LogN)): return 1
        # Quadratic > (Integer, LogN, NLogN)
        if (self.quadratic()) and (type(p) in (NLogN, LogN, Integer)): return 1
        # Factorial >
        if (self.factorial) and (type(p) in (Exponential, NLogN, LogN, Integer)): return 1
        # Handle cases for where both are of type <Polynomial>
        if (type(p) == Polynomial):
            # If self.Factorial & not(other.Factorial)
            if (self.factorial) and not(p.factorial): return 1
            # If self, other == Factorial
            if (self.factorial) and (p.factorial):
                return 1 if (self.power >= p.power) else 0
            # If self.quadratic & not(other.quadratic)
            if (self.quadratic() != p.quadratic()):
                if (p.factorial): return 0
                if (p.linear()): return 1
            # If self, other == Quadratic
            if (self.quadratic() == p.quadratic()):
                return 1 if (self.power >= p.power) else 0
            # If self, other == linear
            if (self.linear() and p.linear()): return 1
            # Linear < (Quadratic, Factorial)
            if (self.linear()) and not(p.linear()): return 0
        else: return 0

    def __gt__(self, p):
        # (Linear, Quadratic, Factorial) > (Integer, LogN)
        if (type(p) in (Integer, LogN)): return 1
        # Quadratic > (Integer, LogN, NLogN)
        if (self.quadratic()) and (type(p) in (NLogN, LogN, Integer)): return 1
        # Factorial > ALL (:except: <Factorial> with greater power than self)
        if (self.factorial) and (type(p) in (Exponential, NLogN, LogN, Integer)): return 1
        # Handle cases for where both are of type <Polynomial>
        if (type(p) == Polynomial):
            # If self.Factorial & not(other.Factorial)
            if (self.factorial) and not (p.factorial): return 1
            # If self, other == Factorial
            if (self.factorial) and (p.factorial):
                return 1 if (self.power > p.power) else 0
            # If self.quadratic & not(other.quadratic)
            if (self.quadratic() != p.quadratic()):
                if (p.factorial): return 0
                if (p.linear()): return 1
            # If self, other == Quadratic
            if (self.quadratic() == p.quadratic()):
                return 1 if (self.power > p.power) else 0
            # If self, other == linear
            if (self.linear() and p.linear()): return 0
            # Linear < (Quadratic, Factorial)
            if (self.linear()) and not (p.linear()): return 0
        # Not sure about bottom line... ._.
        else: return 0

    def __le__(self, p):
        # Linear > (Integer, LogN)
        if (type(p) in (Integer, LogN)): return 0
        # Self.linear() cases
        if (self.linear()):
            if (type(p) in (NLogN, Exponential)): return 1
            # Linear <= (Linear, Quadratic, Factorial)
            if (type(p) == Polynomial):
                if (p.linear())   : return 1
                if (p.quadratic()): return 1
                if (p.factorial)  : return 1
            else: return 0
        if (self.quadratic()):
            if (type(p) == Exponential): return 1
            # Quadratic <= (Quadratic, Factorial)
            if (type(p) == Polynomial):
                if (p.linear())   : return 0
                if (p.quadratic()):
                    return 1 if (self.power <= p.power) else 0
                if (p.factorial)  : return 1
            else: return 0
        if (self.factorial):
            # Linear <= (Factorial)
            if (type(p) == Polynomial):
                if (p.linear())   : return 0
                if (p.quadratic()): return 0
                if (p.factorial):
                    return 1 if (self.power <= p.power) else 0
            else: return 0

    def __lt__(self, p):
        # Linear > (Integer, LogN)
        if (type(p) in (Integer, LogN)): return 0
        # Self.linear() cases
        if (self.linear()):
            if (type(p) in (NLogN, Exponential)): return 1
            # Linear < (Linear, Quadratic, Factorial)
            if (type(p) == Polynomial):
                if (p.linear())   : return 0
                if (p.quadratic()): return 1
                if (p.factorial)  : return 1
        if (self.quadratic()):
            if (type(p) == (Exponential)): return 1
            # Quadratic < (Quadratic, Factorial)
            if (type(p) == Polynomial):
                if (p.linear())   : return 0
                if (p.quadratic()):
                    return 1 if (self.power < p.power) else 0
                if (p.factorial)  : return 1
            else: return 0
        if (self.factorial):
            # Linear <= (Factorial)
            if (type(p) == Polynomial):
                if (p.linear())   : return 0
                if (p.quadratic()): return 0
                if (p.factorial):
                    return 1 if (self.power < p.power) else 0
            else: return 0

    def linear(self) -> int:
        """ Returns 1 if self only has linear properties """
        return 1 if (self.power == 1) and (self.factorial == 0) else 0

    def quadratic(self) -> int:
        """ Returns 1 if self only has quadratic properties """
        return 1 if not(self.factorial) and (self.power > 1) else 0

    def linearfy(self) -> object:
        """ Modifies self attributes to be 'linear' in terms of Big O
            :return: copy of itself """
        self.power, self.factorial = 1, 0
        return self

    def quadraticfy(self, _max=10) -> object:
        """ Modifies self attributes to be 'quadratic' in terms of Big O
            :return: copy of itself """
        self.power, self.factorial = randint(2, _max), 0
        return self

    def factorialfy(self, power=None) -> object:
        """ Modifies self attributes to a 'factorial' in terms of Big O
            :return: copy of itself """
        if (power == None): power = randint(2, 10)
        self.factorial, self.power = 1, power
        return self

    def bigo(self):
        if (self.factorial) and (self.power == 1): return "O(n!)"
        if (self.factorial) and (self.power > 1): return f"O((n^{self.power})!)"
        if (self.power > 1):
            return f"O(n^{self.power})"
        else:
            return 'O(n)'

    def classification(self) -> str:
        if (self.factorial):   return "Factorial"
        if (self.quadratic()): return "Quadratic"
        if (self.linear()):    return "Linear"
        else: raise TypeError(f"{self} Polynomial is not linear, quadratic, nor factorial.")

    def init_factorial(self):
        return 1 if (randint(1, 100) <= 10) else 0

    def measure_growth(self, _min=1, _max=6) -> NoReturn:
        pass


class NLogN:
    def __init__(self):
        pass

    def __eq__(self, o):
        return 1 if (type(o) == NLogN) else 0

    def __ge__(self, o):
        if (type(o) in (NLogN, LogN, Integer)): return 1
        if (type(o) == Polynomial) and (o.power == 1):
            return 1
        else:
            return 0

    def __gt__(self, o):
        if (type(o) in (LogN, Integer)): return 1
        if (type(o) == Polynomial) and (o.power == 1):
            return 1
        else:
            return 0

    def __le__(self, o):
        # Polynomial cases -> Linear, Quadratic, & Factorial
        if (type(o) == Polynomial):
            if (o.linear())   : return 0
            if (o.quadratic()): return 1
            if (o.factorial)  : return 1
        # Type Check
        return 1 if (type(o) in (Exponential, NLogN)) else 0

    def __lt__(self, o):
        if (type(o) == (Exponential)): return 1
        if (type(o) == Polynomial):
            if (o.linear()): return 0
            if (o.quadratic()): return 1
            if (o.factorial): return 1
        else: return 0

    def __ne__(self, o):
        return 1 if (type(o) != NLogN) else 0

    def __repr__(self):
        return f"n log n"

    def bigo(self):
        return "O(n log n)"

    def classification(self):
        return "N Log N"


class Exponential:
    def __init__(self):
        self.const = randint(2, 9)
        self.factorial = False
        self.power = None

    def __eq__(self, o):
        return 1 if (type(o) == Exponential) and (o.const == self.const) else 0

    def __ge__(self, o):
        if (type(o) in (NLogN, LogN, Integer)): return 1
        if (type(o) == Polynomial): return 1 if not(o.factorial) else 0
        if (type(o) == Exponential) and (o.const == self.const): return 1
        else: return 0

    def __gt__(self, o):
        if (type(o) in (NLogN, LogN, Integer)): return 1
        if (type(o) == Polynomial): return 1 if not (o.factorial) else 0
        if (type(o) == Exponential) and (self.const > o.const): return 1
        else: return 0

    def __le__(self, o):
        if (type(o) == Exponential) and (self.const <= o.const): return 1
        if (type(o) == Polynomial) and (o.factorial): return 1
        else: return 0

    def __lt__(self, o):
        if (type(o) == Exponential) and (self.const < o.const): return 1
        if (type(o) == Polynomial) and (o.factorial): return 1
        else: return 0

    def __ne__(self, o):
        if (type(o) != Exponential): return 1
        return 1 if (type(o) == Exponential) and (o.const != self.const) else 0

    def __repr__(self):
        return f"{self.const}^n"

    def bigo(self):
        return f"O({self.const}^n)"

    def classification(self):
        return "Exponential"
