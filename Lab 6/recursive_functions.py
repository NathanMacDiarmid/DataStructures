# SYSC 2100 Winter 2021 Lab 6
# Last edited: Feb. 21, 2021
# v2: Changed header for function last.

class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        return self._data

    def set_data(self, node_data):
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        return self._next

    def set_next(self, node_next):
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)


def to_string(head: Node) -> str:
    """Return a string representation of the linked list referred to by head.

    >>> head = build_linked_list([31, 77, 17, 93, 26, 54])
    >>> to_string(head)
    '31 -> 77 -> 17 -> 93 -> 26 -> 54'

    >>> head = build_linked_list([])
    >>> to_string(head)
    'None'
    """
    if head is None:
        return 'None'

    node = head
    # Traverse the list from head to tail, collecting the data
    # in the nodes as a list of strings.
    items = []
    while node is not None:
        items.append(str(node.data))
        node = node.next

    # Concatenate the strings in items, with each pair separated by " -> "
    return " -> ".join(items)

def build_linked_list(lst: list) -> Node:
    """Build a linked list containing the data in lst and return a
    reference to the first node.

    >>> head = build_linked_list([1, 2, 3, 4])
    >>> to_string(head)
    '1 -> 2 -> 3 -> 4'
    """
    head = None # Empty list has no nodes
    i = len(lst) - 1 # Traverse lst back to
                     # front
    while i >= 0:
        # insert a node (3-step link-in)
        node = Node(lst[i])
        node.next = head
        head = node
        i -= 1
    return head

#--------------------------------
# Exercise 1

def power(x: float, n: int) -> float:
    """Return x raised to the power n.

    Precondition: n >= 0.

    >>> power(3.5, 0)
    1.0
    >>> power(3.5, 1)
    3.5
    >>> power(3.5, 2)
    12.25
    """
    if (n <= 0):
        return 1
    return x * power(x, (n - 1))

#--------------------------------
# Exercise 2

def num_digits(n: int) -> int:
    """Return the number of digits in n.

    Precondition: n >= 0.

    >>> num_digits(492)
    3
    >>> num_digits(63)
    2
    >>> num_digits(7)
    1
    """
    count = 1
    if (n < 10):
        return 1
    return count + num_digits(n // 10)

#--------------------------------
# Exercise 3

def count(head: Node, value: int) -> int:
    """Return the number of integers equal to value in the linked list of
    integers referred to by head.

    >>> head = None
    >>> count(head, 5)
    0
    >>> head = build_linked_list([10, 20, 10, 30, 20, 10])
    >>> to_string(head)
    '10 -> 20 -> 10 -> 30 -> 20 -> 10'
    >>> count(head, 10)
    3
    >>> count(head, 30)
    1
    """
    current = head
    if (current == None):
        return 0
    if (current.data == value):
        return 1 + count(current.next, value)
    return count(current.next, value)
    

#--------------------------------
# Exercise 4

def last(head: Node) -> int:
    """Return the last integer in the linked list of integers
    referred to by head.

    Precondition: head is not None (the linked list is not empty).

    >>> head = build_linked_list([1, 2, 4, 4, 6, 5])
    >>> to_string(head)
    '1 -> 2 -> 3 -> 4 -> 5'
    >>> last(head)
    5
    >>> head = build_linked_list([10])
    >>> to_string(head)
    '10'
    >>> last(head)
    10
    """
    current = head
    if (current.next == None):
        return current.data
    return last(current.next)

#--------------------------------
# Exercise 5

def copy(head: Node) -> Node:
    """Make a copy of the linked list referred to by head (duplicate
    all the nodes in the original list) and return a reference to the
    first node in the new linked list.

    >>> head = build_linked_list([1, 2, 4, 4, 6, 5])
    >>> to_string(head)
    '1 -> 2 -> 3 -> 4 -> 5'
    >>> copied = copy(head)
    >>> to_string(copied)
    '1 -> 2 -> 3 -> 4 -> 5'
    """
    current = head
    if (current == None):
        return None
    new_node = Node(current.data)
    new_node.next = copy(current.next)
    return new_node
    
