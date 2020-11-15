from bigo.expression import *

ORDER = '1,log n,n,n log n,n^2,n^3,2^n,n!'.split(',')

def return_rterm(_min=1, _max=5) -> object:
    """ Return a single random term """
    return TYPES.get(randint(_min, _max))()

def equality() -> NoReturn:
    """ User evaluates if the two algorithmic runtime's have the same Big O """
    a1, a2 = randint(0, 3), randint(0, 3)
    # Init algorithm 1
    if (a1 == 0): a1 = Expression(terms=3)
    else: a1 = return_rterm()
    # Init algorithm 2
    if (a2 == 0): a2 = Expression(terms=3)
    else: a2 = return_rterm()
    # Init answer
    if (a1.bigo() == a2.bigo()): ans = 'true'
    else: ans = 'false'
    # Question user
    print(f"\nIs the Big O of these two algorithms equal or not:\n    ({a1}) ({a2})")
    user_inp = str(input("\nInput answer (true/false): ")).lower()
    if (user_inp == ans): print(f"Correct!")
    else: print(f"Incorrect ._. -- Correct Answer: {ans}")

def worse() -> NoReturn:
    """
    User evaluates whether O(a1) is worse than O(a2).
    Where a1 & a2 are random expressions.
    """
    a1, a2 = randint(0, 3), randint(0, 3)
    # Init algorithm 1
    if (a1 == 0): a1 = Expression(terms=3)
    else: a1 = return_rterm()
    # Init algorithm 2
    if (a2 == 0): a2 = Expression(terms=3)
    else: a2 = return_rterm()
    # Init answer
    if (type(a1) == Expression) and (type(a2) == Expression):
        if (max(a1.terms) > max(a2.terms)): ans = 'true'
        else: ans = 'false'
    elif (type(a1) == Expression) and (type(a2) != Expression):
        if (max(a1.terms) > a2): ans = 'true'
        else: ans = 'false'
    elif (type(a1) != Expression) and (type(a2) == Expression):
        if (a1 > max(a2.terms)): ans = 'true'
        else: ans = 'false'
    else:
        if (a1 > a2): ans = 'true'
        else: ans = 'false'
    # Question user
    print(f"\nIs the Big O of {a1} considered worst than {a2}?")
    user_inp = str(input("\nInput answer (true/false): ")).lower()
    if (user_inp == ans): print(f"Correct!")
    else: print(f"Incorrect ._. -- Correct Answer: {ans}")

def bigo():
    """ User inputs corresponding Big O of randomly generated expression """
    # Init algorithm 1
    a1 = randint(0, 2)
    if (a1 == 0): a1 = Expression(terms=3)
    else        : a1 = return_rterm()
    # Question user
    print(f"\nGive the corresponding Big O of {a1}.")
    user_inp = str(input("\nInput answer: ")).lower()
    if (user_inp == a1.bigo().lower()): print(f"Correct!")
    else: print(f"Incorrect ._. -> Correct Answer: {a1.bigo().lower()}")

def order(reverse=None) -> NoReturn:
    """ User must input each classification of Big O in valid order """
    if (reverse == None):
        reverse = randint(0,1)
        if (reverse):
            ORDER.reverse()
            print("\nInput Big O classifications in descending order.")
        else:
            print("\nInput Big O classifications in ascending order.")
    for elm in ORDER:
        user_inp = str(input("Enter answer: ")).strip()
        if (user_inp.lower().strip() != elm):
            print(f"\nIncorrect ._. -- Correct order:\n{ORDER}")
            return
    print(f'\n<All correct!>')

if __name__ == '__main__':
    questions = {1: equality,
                 2: worse,
                 3: bigo,
                 4: order}
    while (True):
        x = randint(1, 3)
        q = questions.get(x)()
        del x  # Delete x to generate new random integer
