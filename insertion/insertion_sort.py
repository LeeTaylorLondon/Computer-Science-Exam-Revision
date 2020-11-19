# Author: Lee Taylor

from random import randint
from typing import List, NoReturn


def swap(a: List[int], i: int, i2: int) -> NoReturn:
    '''
    Swaps two elements in a list
    :param: a  -- reference to the list of integers
    :param: i  -- pointer to the element to be swapped
    :param: i2 -- pointer to the element to be swapped
    '''
    temp  = a[i]
    a[i]  = a[i2]
    a[i2] = temp

"""
Reference -- https://www.youtube.com/watch?v=JU767SDMDvA
Insertion Sort Pseudo Code: 

for i : 1 to length(A)-1
    j = i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j = j - 1
"""
def insertion_sort(a: List[int]) -> NoReturn:
    for i in range(1, len(a)):  # range is executed up until upper_limit-1
        j = i
        while (j > 0) and (a[j-1] > a[j]):
            swap(a, j, j-1)
            j = j - 1


## Functions below used for testing the user.


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

def list_to_string(a: List[int]) -> str:
    """ Returns string of all elements in list a """
    rv = ''
    for elm in a: rv = rv + ' ' + str(elm)
    return rv[1:]

def insertion_sort_test(a: List[int]) -> NoReturn:
    """
    Insertion sort with each outer iteration trace stored
    and returned. Used to recreate questions from worksheet.
    """

    traces = []                       # init traces
    traces.append(list_to_string(a))  # append first trace
    for i in range(1, len(a)):
        j = i
        while (j > 0) and (a[j-1] > a[j]):
            swap(a, j, j-1)
            j = j - 1
        traces.append(list_to_string(a))  # append each outter for loop trace
    return traces

def recognition(traces:int=4) -> NoReturn:
    """
    Based on ~ CSC2032: Tutorial 1.4.1/2.1.1 ~ Question 1

    Generates a matrix of traces in which only one corresponds
    to the insertion sort -- the user must label the correct
    trace block.

    """

    # Init. answers, obstacles, and pointers for randomization
    a = return_rarray(size=5)
    actual_traces, random_traces = insertion_sort_test(a), []
    i, i2 = 0, 0
    # Populate random_traces matrix
    for i in range(traces):
        # while-loop prevents identical pointers causing no swap
        while(i == i2): i, i2 = randint(0, len(a)-1), randint(0, len(a)-1)
        a_copy   = a.copy()
        swap(a_copy, i, i2)
        trace    = insertion_sort_test(a_copy)
        trace[0] = actual_traces[0]  # Adds more confusion
        random_traces.append(trace)
        i, i2 = 0, 0
    ow_ptr = randint(0,traces-1)  # 'ow' -> points to element to 'overwrite'
    random_traces[ow_ptr] = actual_traces
    random_traces[randint(0,traces-1)][1] = actual_traces[1]
    # Print statements ripped from question-1
    print('Consider the following array traces which may or may not have been ')
    print('produced by different sorting algorithms when applied to the array of values:')
    print(f"{actual_traces[0]}\n")
    # Displays contents of random traces
    for i,vec in enumerate(random_traces):
        print(f"Trace [{i+1}]")
        for s in vec:
            print(s)
        print()
    # User input | answer = ow_ptr + 1
    print('Which trace above corresponds to insertion sort?')
    try:
        ua = int(input("Enter number of trace: "))
    except ValueError:
        print('\n<Invalid input - question exited>\n')
        return
    if (ua == ow_ptr + 1): print('<Answer: Correct!>\n')
    else:
        print('<Answer: Incorrect ._. >\n')
        print(f"The right answer was: {int(ow_ptr)+1}\n")

def traces(size:int=7) -> int:
    """
    Based on ~ CSC2032: Tutorial 1.4.1/2.1.1 ~ Question 2

    The user is presented with an array of integers. User
    must enter each outer iteration trace.
    User input format (i.e): 1 2 3 4 5 6 7

    Note: the array of integers are random unique
    values which can be customized see 'return_rarray()'
    for more details.

    """

    # init actual-traces and user-input storage
    a = return_rarray(size=size)
    actual_traces = insertion_sort_test(a)
    user_inp      = []
    user_inp.append(actual_traces[0])
    # Create 'Step) i=<int>: Insert A[i]=x'
    states = []
    for i in range(len(a)):
        states.append(f"i={i} A[i]={actual_traces[0].split(' ')[i]}")
    ans = []
    ans.append(actual_traces[0])
    for trace,state in zip(actual_traces[1:], states[1:]):
        # ans.append(state)
        ans.append(trace)
    # First trace is always the original list
    # print('\nGive a high-level trace of applying insertion sort to the array given below.\n'
    #       "    Format = (Jason Steggles' Format with Example Below):\n        i=1 A[i]=3 <Input Iteration, "
    #       "& element. Press Enter>\n"
    #       "        3 4 1 3 0 <Input list sorted up to point i. Press Enter & Repeat>\n")
    print(f"Give a high-level trace of applying insertion sort to the array given below.")
    print("Array to be sorted: ", actual_traces[0])
    # Take user input for each trace
    for p in range(1, len(ans)):
        user_inp.append(str(input(f"Input line : ")).strip())
    # Calculate and print score for matching traces
    correct = 0
    for a, ua in zip(ans, user_inp):
        if (a.lower() == ua.lower()): correct += 1
    print(f"<You scored [{correct-1}/{len(ans)-1}]!>\n")
    # Print answers & user input only if they got something wrong
    if (correct != len(ans)):
        for a, ua in zip(ans, user_inp):
            print(f"Your answer: {ua} | Actual: {a}")
        print()
    return correct

def iteration_recognition(iteration=3, lists=5) -> NoReturn:
    """
    Based on ~ CSC2032: Tutorial 1.4.1/2.1.1 ~ Question 3

    Displays an array partially sorted by insertion sort.
    The original array is display with others that are not
    the original array. The user must pick out the correct
    array.

    """

    # Init. obstacles, copy of list, and partial sorted version of list
    p_answers = []  # p_answers -> possible answers
    a = return_rarray(size=7)
    og_list = a.copy()
    partially_sorted_array = insertion_sort_test(a)[iteration]
    # Populate p_answers with non-answers and answer
    i, i2 = 0, 0  # while-loop prevents equal ptrs causing no swap
    while (i == i2): i, i2 = randint(0, len(a) - 1), randint(0, len(a) - 1)
    # Swap elements in the original array and display to confuse user
    for i in range(lists):
        temp_list = og_list.copy()
        swap(temp_list, i, i2)
        p_answers.append(temp_list)
    # Change a value in each possible answer list to be sorted
    for pa in p_answers:
        if (randint(0,1)): pa[randint(1,len(pa)-1)] = randint(0, max(pa)+2)
    # Sets at least one vector in p_answers to the actual answer
    p_answers[randint(0, lists - 1)] = og_list
    # Display question information to user
    print(f'\nSuppose after {int(iteration)} outer iterations of insertion')
    print('sort we have the following array:')
    print(f'{partially_sorted_array}\n')  # Display actual trace
    print('Then which of the following arrays could have been the initial')
    print('array insertion sort was applied to.\n')
    for i, vec in enumerate(p_answers): print(f"{i + 1}) {list_to_string(vec)}")
    # User input is taken and evaluated
    try:
        user_inp = int(input('\nEnter the number of any correct array: '))
        if not(0 < user_inp <= len(p_answers)):
            print('\n<Invalid input - question exited>\n')
            return
    except ValueError:
        print('\n<Invalid input - question exited>\n')
        return
    try:
        user_list = insertion_sort_test(p_answers[user_inp-1])[iteration]
        if (user_list == partially_sorted_array):
            print('<Answer: Correct!>\n')
        else:
            print('<Answer: Incorrect ._. >\n')
            acceptable = []
            for i,arr in enumerate(p_answers):
                if (insertion_sort_test(arr)[iteration] == partially_sorted_array):
                    acceptable.append(i+1)
            print(f"Acceptable Answer(s): {list_to_string(acceptable)}")
    except IndexError:
        print('<Answer: Incorrect ._. >\n')
        s = 'Acceptable answers:'
        for i, pa in enumerate(p_answers):
            if (pa == og_list): s = s + ' ' + f"[{str(i)}]"
        print(s)

def explain_stability(*args):
    """
    Based on ~ CSC2032: Tutorial 1.4.1/2.1.1 ~ Question 4

    The user must type the definition below -- of course as
    a user you may change the definition typed out. By changing
    the string below.

    """

    a = "If an input list contains two equal elements in positions \
    i and j where i < j then in the sorted list they have to be in positions \
    i' and j'"
    q = 'Enter a short definition for sorting stability below.'

    def mark_continuous(user: List[str], actual: List[str]) -> int:
        '''
        :return: mark int, counted for each matching word
                 where exact order matters
        :param:  user   -- the user's answer
        :param:  actual -- the actual answer
        '''
        mark = 0
        for words in zip(user, actual):
            if (words[0].lower() != words[1]): return mark
            mark += 1
        return mark

    def mark_matches(user: List[str], actual: List[str]) -> int:
        """
        :return: mark counted for each matching word
        :param:  user   -- the user's answer
        :param:  actual -- the actual answer
        """
        mark = 0
        for words in zip(user, actual):
            if (words[0] == words[1]): mark += 1
        return mark

    answer = [word.lower() for word in a.split()]
    print('\nQuestion: ' + q)  # Print question
    user_inp = str(input("Answer  : ")).split()
    # Marking occurs
    print(f"<Mark_C = {mark_continuous(user_inp, answer)}/{len(answer)}>")
    print(f"<Mark_M = {mark_matches(user_inp, answer)}/{len(answer)}>")
    print(f"<Answer = {a}>\n")

def main():
    ''' Examples '''
    #reference_example = [2, 8, 5, 3, 9, 4]
    ''' >>> <example_1 = [2, 8, 5, 3, 9, 4] (Before i.sort)> '''
    #insertion_sort(reference_example)
    ''' >>> <example_1 = [2, 3, 4, 5, 8, 9] (After i.sort)> '''

    ''' Testing '''
    questions = {1: recognition,
                 2: traces,
                 3: iteration_recognition,
                 4: explain_stability}
    while True:
        q = randint(1, 4)
        questions.get(q)()

def test_q3():
    iteration_recognition()

def test_q2():
    traces()

if __name__ == '__main__':
    # main()
    while True:
        # test_q3()
        test_q2()