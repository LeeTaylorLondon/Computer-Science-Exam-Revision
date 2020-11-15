# questions.py
# Author: Lee Taylor
import stringsearch.stringsearching as stringsearching
from stringsearch.stringsearching import *
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

def bf_comps(debug:bool=False):
    """
    User is presented with text and pattern user must provide
    number of comparisons occurred in brute force searching algorithm
    """
    alphabet = ["A", "G", "C", "T"]
    # Create text
    text_int = return_rarray(_min=0, _max=3, size=randint(8, 11), duplicates=True)
    text = ''
    for elm in text_int:
        text = text + alphabet[elm]
    # Create pattern
    pattern_int = return_rarray(_min=0, _max=3, size=randint(3, 5), duplicates=True)
    pattern = ''
    for elm in pattern_int:
        pattern = pattern + alphabet[elm]
    # 20% chance to have random pattern ~ 80% chance to have pattern from text
    nomatch = False
    if (randint(1, 5) == 1): nomatch = True
    # Act according to chance
    if (nomatch):
        i, ans = bruteforce(text, pattern)
    elif not(nomatch):
        starting_index = randint(0, len(text) - 4)
        pattern = text[starting_index: starting_index+4]
        i, ans = bruteforce(text, pattern)
    # Debug
    if (debug):
        print(text, pattern)
        print(i, ans)
    # Question, & user input
    print(f"\n\nConsider the following string searching problem:\n"
          f"      t={text}\n      p={pattern}\n"
          f"Apply the brute force string searching algorithm to the\n"
          f"Above string searching problem and calculate the number of\n"
          f"Comparisons needed.")
    user_inp = str(input("\nInput answer: "))
    # Mark answer
    if (user_inp == str(ans)): print(f"Correct!")
    else: print(f"Incorrect ._. Correct answer: {ans}")

def create_table() -> NoReturn:
    """
    User is presented with a string of random chars the user
    must input the corresponding KMP table
    """
    alphabet = ["A", "B", "C", "D"]
    # Create text
    text_int = return_rarray(_min=0, _max=3, size=randint(5, 8), duplicates=True)
    text_str = ''
    for elm in text_int:
        text_str = text_str + alphabet[elm]
    # Create table
    table = stringsearching.table(text_str)
    # Ask question, & receive user input
    print("\n\nComplete the next table required by the Knuth-Morris-Pratt\n"
            f"String searching algorithm for the pattern string: {text_str}\n"
            f"by inputting the resulting values below.")
    user_inp = str(input("\nInput Answer: "))
    # Mark user input
    if (user_inp.strip() == list_to_string(table)):
        print(f"Correct!")
    else:
        print(f"Incorrect ._. Correct answer: {list_to_string(table)}")

def create_string() -> NoReturn:
    """
    User is presented with a table user must input a string
    that creates the same table.
    """
    # Init. possible characters in T & P
    alphabet = ["A", "B", "C", "D"]
    # Create text
    text_int = return_rarray(_min=0, _max=3, size=randint(5, 8), duplicates=True)
    text_str = ''
    for elm in text_int:
        text_str = text_str + alphabet[elm]
    # Create table
    table_ans = stringsearching.table(text_str)
    # Question
    print("\n\nGive a pattern that matches the following next table:"
          f"        \n{table_ans}")
    user_inp = str(input("\nInput Answer: "))
    # Mark answer
    if (table(user_inp.strip()) == table_ans):
        print(f"Correct!")
    else:
        print(f"Incorrect ._. Possible Answer: {text_str}")

def apply_kmp() -> NoReturn:
    alphabet = ["A", "B", "C", "D"]
    # Create text
    text_int = return_rarray(_min=0, _max=3, size=randint(8, 11), duplicates=True)
    text = ''
    for elm in text_int:
        text = text + alphabet[elm]
    # Create random pattern
    pattern_int = return_rarray(_min=0, _max=3, size=randint(3, 5), duplicates=True)
    pattern = ''
    for elm in pattern_int:
        pattern = pattern + alphabet[elm]
    # 20% chance to have random pattern ~ 80% chance to have pattern from text
    randomp = False
    if (randint(1, 5) == 1): randomp = True
    # Act according to chance, & init. answers
    answers = []
    if (randomp):
        i, c, answers = kmp_search_traced(text, pattern)
    elif not (randomp):
        plen = randint(3, 5)
        starting_index = randint(0, len(text) - plen)
        pattern = text[starting_index: starting_index + plen]
        i, c, answers = kmp_search_traced(text, pattern)
    # Question
    print(f"\n\nApply the KMP search algorithm to the following string searching problem\n"
          f"keeping a note of the number of comparisons required:\n"
          f"    t='{text}', p='{pattern}'")
    user_inp = []
    # Input answer
    for lines in range(len(answers)-2):
        user_inp.append(str(input("Enter line: ")))
    # Mark answers
    matches = 0
    for inputs in range(len(answers) - 2):
        if (user_inp[i].lower() == answers[inputs+1]):
            matches += 1
    print(f"\nNumber of lines inputted matching answers: {matches}/{len(answers)-2}")
    # Show answers & input
    print(f"\nCorrect answers: ")
    for line in answers: print(line)
    print(f"\nYour answers: ")
    for line in user_inp: print(line)


if __name__ == '__main__':
    questions = {1: bf_comps,
                 2: create_table,
                 3: create_string,
                 4: apply_kmp
                 }
    while True:
        q = randint(1, len(questions))
        q = 4
        questions.get(q)()
        del q  # Prevent case of stuck on one question

