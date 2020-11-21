from binsearchtree.bst import *


def strip_list(a: List[int]) -> NoReturn:
    """
    Remove leading blanks:
        [1, 2, None, 3, None, None, None] -> [1, 2, None, 3]
    """
    ptr = len(a) - 1
    while (a[ptr] == None) and (len(a) > 1):
        del a[ptr]
        ptr -= 1

def format_list(a: List[int]) -> NoReturn:
    """ Replace None with '-' & convert int to str """
    for i,n in enumerate(a):
        if (n == None):
            a[i] = '-'
        else:
            a[i] = str(n)

def get_ints(a: List[Node]) -> NoReturn:
    """ Replace each Node object with it's integer value """
    for i,v in enumerate(a):
        if (v != None):
            a[i] = v.value

def format_bst_matrix(m: List[List[Node]]) -> NoReturn:
    """
    BST.bst_matrix() returns a matrix representing itself - this function
    modifies the contents of the matrix to a matrix of lists of strings.
    """
    for v in m:
        get_ints(v)
        strip_list(v)
        format_list(v)


""" Above code contains general functions - Below code are question functions """

def bst():
    """ User must input BST given an list of random ints """
    # Determine BST input parameters
    _min, _max = 11, 29
    min_size, max_size = 11, 14
    # List of random ints input into BST
    vec = return_rarray(_min, _max, randint(min_size, max_size))
    bst = BinarySearchTree(vec)
    # Acquire BST matrix
    bst_matrix = bst.bfs_matrix()
    # Format matrix of answers
    format_bst_matrix(bst_matrix)
    # Question
    print(f"\n\nGiven an array of random integers: {vec}\n"
          f"provide each line of the structure of the binary search tree. After\n"
          f"insertion of these values in the order presented.\n"
          f"A line should contain nodes for that depth, only children of visible parents\n"
          f"and no leading Nones.\n")
    # User input
    user_inp = []
    for line in bst_matrix:
        user_inp.append(str(input("Enter line: ")))
    # Mark user answers
    correct = 0
    for user_ans, actu_ans in zip(user_inp, bst_matrix):
        if (user_ans == ' '.join(actu_ans)):
            correct += 1
    if (correct == len(bst_matrix)):
        print('\nAll Correct!')
    else:
        print(f"\nIncorrect ({correct}/{len(bst_matrix)}) -_- Correct Answers: ")
        for actu_ans in bst_matrix:
            print(' '.join(actu_ans))

def insert():
    """
    User is presented with BST user must input
    state of the BST after inserting a random number
    """
    # Determine BST input parameters
    _min, _max = 11, 29
    min_size, max_size = 11, 14
    # List of random ints input into BST
    vec = return_rarray(_min, _max, randint(min_size, max_size))
    bst = BinarySearchTree(vec)
    # Acquire BST matrix before insertion
    bst_matrix_q = bst.bfs_matrix()
    # Format matrix for question display
    format_bst_matrix(bst_matrix_q)
    # Insert random int
    insertion_val = randint(_min, _max)
    bst.insert(insertion_val)
    # Acquire BST matrix after insertion
    bst_matrix_ans = bst.bfs_matrix()
    # Format matrix of answers
    format_bst_matrix(bst_matrix_ans)
    # Question
    print("\n\nGiven the following BST's structure: ")
    for arr in bst_matrix_q:
        print(f"    {' '.join(arr)}")
    print(f"Provide the BST's structure after inserting {insertion_val}.\n"
          f"A line should contain nodes for that depth, only children of visible parents\n"
          f"and no leading Nones.\n")
    # User input
    user_inp = []
    for line in bst_matrix_ans:
        user_inp.append(str(input("Input line: ")))
    # Mark answers
    correct = 0
    for user_ans, actu_ans in zip(user_inp, bst_matrix_ans):
        if (user_ans == ' '.join(actu_ans)):
            correct += 1
    # Display mark
    if (correct == len(bst_matrix_ans)):
        print("\nAll correct!")
    else:
        print(f"\nIncorrect ({correct}/{len(bst_matrix_ans)}) -_- Correct answer: ")
        for line in bst_matrix_ans:
            print(f"    {' '.join(line)}")

def search():
    """ User must input traces for searching for a key in BST (Jason Steggles' format) """
    # Determine rarray parameters
    _min, _max = 8, 28
    min_size, max_size = 18, 20
    # Create & Input random ints into BST
    vec = return_rarray(_min=_min, _max=_max, size=randint(min_size, max_size))
    bst = BinarySearchTree(vec)
    # Acquire BST structure
    bst_matrix_q = bst.bfs_matrix()
    # Format matrix for question display
    format_bst_matrix(bst_matrix_q)
    # Init. Random integer to search for
    random_vec = bst_matrix_q[randint(2, len(bst_matrix_q) - 1)]
    random_key = -1
    while (random_key == -1):
        try:
            random_key = int(random_vec[randint(0, len(random_vec) - 1)])
        except ValueError:
            random_key = -1
    # Get answers
    answers, x = bst.search_traced(random_key)
    # Question
    print("\n\nGiven the following BST's structure: ")
    for arr in bst_matrix_q:
        print(f"    {' '.join(arr)}")
    print(f"Provide the high-level traces for searching for {random_key}.")
    # User input
    user_answers = []
    for line in answers:
        user_answers.append(str(input("Input line: ")))
    # Mark user answers
    correct = 0
    for user_ans, actual_ans in zip(user_answers, answers):
        if (user_ans.strip() == actual_ans):
            correct += 1
    # Display mark
    if (correct == len(answers)):
        print("\nAll correct!")
    else:
        print(f"\nIncorrect -_- ({correct}/{len(answers)}) Correct answers: ")
        for line in answers:
            print(line)

def truth():
    """ User is presented with a BST user must determine whether or not it is valid """
    pass

def inorder():
    """ User inputs ??? """
    pass


if __name__ == '__main__':
    # Test question function 'bst()'
    # bst()
    while True:
        # bst()
        # insert()
        search()
    # # Test function strip_list & format_list
    # x = [1, 2, None, 3, None, None, None]
    # print(strip_list(x))
    # print(format_list(x))