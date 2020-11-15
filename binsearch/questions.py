from binsearch.binsearch import *
from binsearch import *


def trace(debug:bool=False):
    """
    Question description:
        User must provide high-level trace of binary search applied to
        randomly sized array containing random integers
    """
    # Init. empty answers array + range for random ints + array of random ints + key
    answers = []
    _min, _max = 1, 30
    rarray = return_rarray(_max=_max, size=randint(9, 16))
    rarray.sort()
    key = randint(_min, _max)
    # Run binary search traced
    binsearch_traced_simple(rarray, key, 0, len(rarray)-1, answers)
    # Question
    print(f"\n\n* Search for {key} in the array:\n    {list_to_string(rarray)}")
    print(f"Input each state of the variables as: l=? r=? m=?\n")
    # User input
    user_inp = []
    for i,line in enumerate(answers):
        user_inp.append(str(input("Enter trace-line: ")))
        # Debug option - See answers & exit function
        if (user_inp[i] == 'odin') and (debug == True):
            for line in answers:
                print(line)
            return
        # Debug option - See answers & do not exit function
        elif (user_inp[i] == 'ymir') and (debug == True):
            for line in answers:
                print(line)
    # Mark answers
    correct = 0
    for ans, actual_ans in zip(user_inp, answers):
        if (ans == actual_ans):
            correct += 1
    if (correct == len(answers)):
        print('Correct!')
    else:
        print(f"Incorrect -_- Correct answer: ")
        for line in answers:
            print(line)


def recursive_calls(_max: int=18):
    """
    Question description:
        User deduces the number of recursive calls to bin-search occurred
    """
    # Init. question text, & powers of 2 (question variable)
    text = "Suppose you have a sorted array of size N and you apply binary\n" \
           " search to it. How many recursive calls would have occurred if\n" \
           " you artificially stopped the algorithm and observed that the\n" \
           " array has size approximately N/"
    pwrs = [2**x for x in range(_max)]
    # Init. index (index = answer) & power
    i = randint(3, _max-1)
    pwr = pwrs[i]
    # Ask question
    print(f"\n\n{text+str(pwr)}?")
    # Take user input
    user_inp = str(input("\nEnter answer: "))
    # Mark answer
    if (user_inp == str(i)):
        print('\nCorrect!')
    else:
        print(f'\nIncorrect -_- Correct answer: {i}')
