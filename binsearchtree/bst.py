from typing import NoReturn, List, Optional
from random import randint

class Node:
    """
    Class definition of Node

    :attr value:  Integer value of node                : int
    :attr right:  Right child pointer to node obj      : Node
    :attr left:   Left child pointer to node obj       : Node
    :attr side:   Indicates which side this node is on : str
    :attr parent: Ptr to parent node                   : Node
    """
    def __init__(self, v) -> NoReturn:
        # Standard Node attributes
        self.value = v
        self.left  = None
        self.right = None
        # Ptr to parent, & str of side
        self.side   = None
        self.parent = None

    def __repr__(self) -> str:
        return f"<Node v={self.value}, l={self.left}, r={self.right}>"

    def get_depth(self) -> int:
        rv = 0
        n = self
        while (n.parent != None):
            n = n.parent
            rv += 1
        return rv

class BinarySearchTree:
    """
    Class definition of Binary Search Tree


    * Attribute
    -------------------------------
    :attr root:
        pointer to root node of BST


    * Methods
    -------------------------------
    :method __init__:
        Optional to pass List[int]. Converts each int to Node
        and inserts them in the order they appear

    :method insert:
        Adds element passed into BST

    :method search:
        Returns (T|F) if an element exists within BST

    :method delete:
        Removes specified Node from BST

    :method inorder:
        Appends inorder traversal to passed List[str]

    :method bfs:
        Returns list of BFS result

    :method get_depth:
        Returns depth of a Node as int

    :method bfs_matrix:
        Returns matrix where each vector is a depth of Node(s)

    :method __repr__:
        Returns string representation of BST

    """
    def __init__(self, arr=None):
        self.root = None
        # Allows user to pass list of integers to BST construct
        if (arr != None):
            for elm in arr: self.insert(Node(elm))

    def insert(self, n) -> NoReturn:
        """ Insert node, n, into binary search tree """
        # If user inserts integer transmute integer to node object
        if (type(n) == int):
            n = Node(n)
        # If user insert non-integer, non-node then raise error
        if (type(n) != Node):
            raise TypeError(f"Data to insert must be of type 'Node', not {type(n)}!")
        # Assign root node if none
        if (self.root == None):
            self.root = n
            return
        # Performs comparisons - locates position to insert
        check = self.root
        while (True):
            if (n.value >= check.value):
                if (check.right == None):
                    check.right = n
                    check.right.parent = check
                    n.side = 'right'
                    return
                check = check.right
            else:
                if (check.left == None):
                    check.left = n
                    check.left.parent = check
                    n.side = 'left'
                    return
                check = check.left

    def search(self, key) -> Optional[Node]:
        """ Search for key in binary search tree """
        # If user searches by node key is transmuted into integer
        if (type(key) == Node):
            key = key.value
        # If user searches for non-integer, non-node then raise error
        if (type(key) != int):
            raise TypeError(f"Key must be of type 'int', not {type(key)}!")
        # Perform comparisons to locate key
        current_node = self.root
        while (current_node != None):
            if (key < current_node.value):
                current_node = current_node.left
            elif (key > current_node.value):
                current_node = current_node.right
            elif (key == current_node.value):
                return current_node
        return None

    def delete(self, key) -> NoReturn:
        # If key is non-integer non-node then raise error
        if (type(key) != int) and (type(key) != Node):
            raise TypeError(f"Key must be of type int or Node, not {type(key)}!")
        # x : Node -> points to node to delete
        if (type(key) != Node):
            x = self.search(key)
        else: x = key
        if (x == None): return
        # 0 Children case
        if (x.left == None) and (x.right == None):
            if (x.side == 'left'):
                x.parent.left = None
                return
            elif (x.side == 'right'):
                x.parent.right = None
                return
        # 1 Child case (left)
        elif (x.left != None) and (x.right == None):
            if (x.side == 'left'):
                x.parent.left = x.left
                return
            elif (x.side == 'right'):
                x.parent.right = x.left
                return
        # 1 Child case (right)
        elif (x.left == None) and (x.right != None):
            if (x.side == 'left'):
                x.parent.left = x.right
                return
            elif (x.side == 'right'):
                x.parent.right = x.right
                return
        # 2 Children case
        elif (x.left != None) and (x.right != None):
            # Traverse one right & left until null
            replacement = x.right
            while (replacement.left != None):
                replacement = replacement.left
            # Perform replacement & deletion
            x.value = replacement.value
            self.delete(replacement)

    def inorder(self, c, rv) -> NoReturn:
        """ Appends BST elements in ascending order to list """
        if (c != None):
            self.inorder(c.left, rv)
            rv.append(str(c.value))
            self.inorder(c.right, rv)

    def bfs(self) -> List[Node]:
        """ Breadth-first-search :returns ordered List[Node] """
        c = 0
        q = [self.root]
        while (c != len(q)):
            if (q[c].left != None) : q.append(q[c].left)
            if (q[c].right != None): q.append(q[c].right)
            c += 1
        return q

    def get_depth(self, n) -> int:
        """ Return integer value depth of a passed Node """
        # Type check
        if (type(n) != Node):
            raise TypeError(f"Type of n must be Node, not {type(n)}!")
        # Determines depth
        depth = 0
        while (n != self.root):
            n = n.parent
            depth += 1
        return depth

    def bfs_matrix(self) -> List[List[Node]]:
        """ Return matrix of vectors representing each depth/level """
        # Init list of nodes as q, & init matrix
        q = self.bfs()
        matrix = [[q[0]]]
        # Iterate over q
        for node in q:
            # Skip null
            if (node == None): continue
            # Left child if null
            if (node.left == None):
                try:
                    matrix[self.get_depth(node) + 1].append(None)
                except IndexError:
                    matrix.append([])
                    matrix[self.get_depth(node) + 1].append(None)
            # Left child if not null
            else:
                try:
                    matrix[self.get_depth(node.left)].append(node.left)
                except IndexError:
                    matrix.append([])
                    matrix[self.get_depth(node.left)].append(node.left)
            # Right child if null
            if (node.right == None):
                try:
                    matrix[self.get_depth(node) + 1].append(None)
                except IndexError:
                    matrix.append([])
                    matrix[self.get_depth(node) + 1].append(None)
            # Right child if not null
            else:
                try:
                    matrix[self.get_depth(node.right)].append(node.right)
                except IndexError:
                    matrix.append([])
                    matrix[self.get_depth(node.right)].append(node.right)
        # Debug display matrix
        # for vec in matrix:
        #     line = ''
        #     for node in vec:
        #         if (node != None):
        #             line = line + ' ' + str(node.value)
        #         else:
        #             line = line + ' none'
        #     print(line[1:])
        return matrix

    def __repr__(self) -> str:
        """ :returns: String representation of BST """
        return f"<BinarySearchTree r={self.root}>"


def nodes_to_ints(vec: List[Node]) -> NoReturn:
    """ Passed a list of nodes each element becomes an int """
    for i,elm in enumerate(vec):
        if (elm != None): vec[i] = elm.value

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

def list_to_string(a: List[int], pivot:int=None, si:int=None, ei:int=None, trace:List[str]=None) -> str:
    """
    Returns string of all elements in list a if pivot, si, & ei = None

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

def test_bst() -> NoReturn:
    # Init. BST.
    bst = BinarySearchTree()

    # Init. nodes
    n1 = Node(4)
    n2 = Node(5)
    n3 = Node(3)
    n4 = Node(100)

    # Insert nodes into BST.
    bst.insert(n1)
    bst.insert(n2)
    bst.insert(n3)
    bst.insert(n4)

    # Display BST
    print(bst)

    # BST Search
    print(f"bst.search(100) -> {bst.search(100)}")
    # print(f"bst.search(100) -> {bst.search(n1)}")  # Raises error as expected

def test_inorder() -> NoReturn:
    """ Jason Steggles' tutorial video example """
    # Init. BST, & array of integers used in example video
    bst = BinarySearchTree()
    arr = [9, 4, 2, 7, 12, 10]

    # Insert each integer as a node into the example BST
    for elm in arr: bst.insert(Node(elm))

    # Display the BST
    print(bst)

    # Display result from inorder traversal
    rv = []
    bst.inorder(bst.root, rv)
    print(list_to_string(rv))

def test_delete():
    # Init. node values, BST
    arr = [5, 3, 1, 4, 8, 10, 6, 7]
    bst = BinarySearchTree()
    for n in arr: bst.insert(Node(n))

    print(bst)

    bst.delete(5)

    print(bst)
    print(bst.root.left)
    print(bst.root.right)
    print(bst.root.right.left)


if __name__ == '__main__':
    """ Pre-written tests """
    # test_bst()
    # test_inorder()

    arr = [5, 3, 1, 4, 8, 10, 6, 7]
    bst = BinarySearchTree(arr)
    matrix1 = bst.bfs_matrix()

    arr2 = [1, 2, 3]
    bst2 = BinarySearchTree(arr2)
    matrix2 = bst2.bfs_matrix()

    # for vec in matrix1: print(vec)
    # print()
    # for vec in matrix2: print(vec)

    # Depth test
    print(f"val={bst2.root.right.right}, depth={bst2.get_depth(bst2.root.right.right)}")
    print(f"val={bst2.root.right.right}, depth={bst2.root.right.right.get_depth()}")