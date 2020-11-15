from binsearchtree.bst import *

def insert():
    """
    User is presented with BST user must input
    state of the BST after inserting a random number of
    random integers
    """
    pass

def strip_list(a: List[int]):
    n = len(a) - 1
    for elm in a[::-1]:
        if (elm == None):
            n -= 1
        else:
            break
    return a[0:n]

def bst():
    """ User must input BST given an empty BST & list of random ints """
    _min, _max = 1, 15
    min_size, max_size = 8, 12
    vec = return_rarray(_min, _max, randint(min_size, max_size))
    bst = BinarySearchTree(vec)
    bst_matrix = bst.bfs_matrix()
    print(vec)
    for vec in bst_matrix:
        nodes_to_ints(vec)
        print(vec)

def search():
    """ User must input traces for searching for a key in BST (Jason Steggles' format) """
    pass

def truth():
    """ User is presented with a BST user must determine whether or not it is valid """
    # Is this really possible given the limited functionality of bst.bfs_matrix(...) ??
    # ----------------------------------------------------------------------------------
    # Update: Modified bst.bfs_matrix(...) to include null pointers so now this question
    #          is possible! =)
    pass

def depth():
    """ User inputs depth of a Node """
    pass

def inorder():
    """ User inputs ??? """
    pass


if __name__ == '__main__':
    bst()