# SYSC 2100 Winter 2021 Lab 5
# Last edited: Feb. 9, 2021

# An implementation of ADT Unordered List that uses a singly-linked list as the
# underlying data structure.

# Based on the classes in "Problems Solving with Algorithms and Data Structures
# Using Python, 3rd Edition", Section 4.2.1.

class Node:
    """A node in a singly-linked list"""

    def __init__(self, node_data):
        """Initialize this node with "payload" node_data.
        The node's link is initialized with the end-of-list marker (None).
        """
        self._data = node_data
        self._next = None

    def get_data(self):
        """Return this node's payload."""
        return self._data

    def set_data(self, node_data):
        """Replace this node's payload with node_data."""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Return the reference (pointer) to the node that follows this node,
        or None if this node is at the end of a list.
        """
        return self._next

    def set_next(self, node_next):
        """Append the node referred (pointed) to by next_node to this node."""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """Return a string representation of this node's payload."""
        return str(self._data)


class UnorderedList:
    """A collection of items, where each item hold a relative position
    with respect to the others.
    """

    def __init__(self, iterable=None) -> None:
        """Initialize this UnorderedList with the contents of iterable.
        If iterable isn't provided, the UnorderedList is empty.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> str(lst)
        '31 -> 77 -> 17 -> 93 -> 26 -> 54'

        >>> lst = UnorderedList()
        >>> str(lst)
        'None'
        """
        self._head = None
        self._size = 0
        if iterable is not None:
            # Add the contents of iterable to this list, one-by-one.
            for elem in iterable:
                if self._head is None:
                    # Linked list is empty. Insert the first node.
                    node = Node(elem)
                    self._head = node
                else:
                    # Append nodes containing the remaining elements
                    # provided by iterable.
                    node.next = Node(elem)
                    node = node.next
                self._size += 1

    def __str__(self) -> str:
        """Return a string representation of this list.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> str(lst)
        '31 -> 77 -> 17 -> 93 -> 26 -> 54'

        >>> lst = UnorderedList()
        >>> str(lst)
        'None'
        """
        if self._head is None:
            return 'None'

        node = self._head
        # Traverse the list from head to tail, collecting the data
        # in the nodes as a list of strings.
        items = []
        while node is not None:
            items.append(str(node.data))
            node = node.next

        # Concatenate the strings in items, with each pair separated by " -> "
        return " -> ".join(items)

    def __repr__(self) -> str:
        """Return a string representation of this list.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> lst
        UnorderedList([31, 77, 17, 93, 26, 54])
        >>> repr(lst)
        'UnorderedList([31, 77, 17, 93, 26, 54])'

        >>> lst = UnorderedList()   # or, lst = UnorderedList([])
        >>> lst
        UnorderedList([])
        """
        if self._head is None:
            return "UnorderedList([])"
        node = self._head
        items = []
        while node is not None:
            items.append(node.data)
            node = node.next
            
        return "UnorderedList({0})".format(items)

    def __iter__(self):
        """Return a new iterator object that can iterate over the items
        in this list, from head to tail.

        >>> lst = UnorderedList([31, 77, 17])
        >>> for item in lst:
                print(item)
        31
        77
        17
        """
        # generator function - returns an iterator object
        # See the tutorial and the language reference at python.org.
        node = self._head
        while node is not None:
            yield node.data
            node = node.next

    def is_empty(self) -> bool:
        """Return True if this list is empty.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> lst.is_empty()
        False

        >>> lst = UnorderedList()
        >>> lst.is_empty()
        True
        """
        return self._head == None

    def __len__(self) -> int:
        """Return the number of items in this list.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> len(lst)
        6
        """
        return self._size

    def __contains__(self, item) -> bool:
        """Return True if item is in this list.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> 93 in lst
        True
        >>> 100 in lst
        False
        """
        current = self._head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def add(self, item: int) -> None:
        """Insert item at the head of this list.

        >>> lst = UnorderedList()
        >>> lst.add(17)
        >>> lst.add(77)
        >>> lst.add(31)
        >>> str(lst)
        '31 -> 77 -> 17'
        """
        temp = Node(item)
        temp.next = self._head
        self._head = temp
        self._size += 1

    def remove(self, item: int) -> None:
        """
        Remove the first value from this list that is equal to item.

        Raises ValueError if item is not in the list.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> 93 in lst
        True
        >>> lst.remove(93)
        >>> 93 in lst
        False
        """
        current = self._head
        previous = None

        while current is not None:
            if current.data == item:
                # found the item we want to remove
                if previous is None:
                    # item is in the head node
                    self._head = current.next
                else:
                    # relink, to skip over the node containing item
                    previous.next = current.next
                self._size -= 1
                return
            previous = current
            current = current.next

        # We reached the end of the list without finding item
        raise ValueError("{0} is not in the list".format(item))

    def count(self, item: int) -> int:
        """Return the total number of occurrences of item in this list.

        >>> lst = UnorderedList([31, 77, 17, 31])
        >>> lst.count(31)
        2
        >>> lst.count(100)
        0
        """
        current = self._head
        count = 0
        while current is not None:
            if current.data == item:
                count += 1
            current = current.next
        return count

    def append(self, item: int) -> None:
        """Append item at the tail of this list.

        >>> lst = UnorderedList([31, 77, 17])
        >>> lst.append(93)
        >>> str(lst)
        '31 -> 77 -> 17 -> 93'
        """
        current = self._head
        
        while current is not None:
            if current.next is None:
                current.next = Node(item)
                current.next.next = None
                self._size += 1
                return
            current = current.next

    def index(self, item: int) -> int:
        """Return index of the first occurrence of item in this list.

        Raises ValueError if item is not in the UnorderedList.

        >>> lst = UnorderedList([31, 77, 17, 31])
        >>> lst.index(31)
        0
        >>> lst.index(17)
        2
        >>> lst.index(10)
          ...
        builtins.ValueError: 10 is not in the list
        """
        current = self._head
        count = 0
        
        while current is not None:
            if current._data == item:
                return count
            current = current.next
            count += 1
            
        raise ValueError("Number is not in list")

    def pop(self, i: int) -> int:
        """Remove and return the item at index i in this list.

        Raises IndexError if i is negative.
        Raises IndexError if i is greater than the index of the item at the
        tail of the list.

        >>> lst = UnorderedList([31, 77, 17, 93, 26, 54])
        >>> lst.pop(0)
        31
        >>> str(lst)
        '77 -> 17 -> 93 -> 26 -> 54'

        >>> lst.pop(4)
        54
        >>> str(lst)
        '77 -> 17 -> 93 -> 26'
        """
        current = self._head
        previous = None
        count = 0
        
        if i < 0:
            raise IndexError("i is negative")
        if len(self) < i:
            raise IndexError("i is out of range")
        
        while current is not None:
            if previous is None:
                if count == i:
                    value = current._data
                    self._head = self._head.next
                    self._size -= 1
                    return value                    
            elif count == i:
                value = current._data
                previous.next = current.next
                self._size -= 1
                return value
                
            previous = current
            current = current.next
            count += 1

    def insert(self, i: int, item: int) -> None:
        """Insert x into this list at the index given by i.
        Appends item if i is greater than the index of the item at the
        tail of the list.

        Raises IndexError if i is negative.

        >>> lst = UnorderedList([31, 77, 17])
        >>> lst.insert(0, 25)
        >>> str(lst)
        '25 -> 31 -> 77 -> 17'
        >>> lst.insert(10, 60)  # Note argument i.
                                # Equivalent to lst.append(60)
        >>> str(lst)
        '25 -> 31 -> 77 -> 17 -> 60'
        """
        current = self._head
        value = Node(item)
        value.next = None
        previous = None
        count = 0
        
        if i < 0:
            raise IndexError("i is negative")
        
        if i > len(self):
            while current is not None:
                if current.next is None:
                    current.next = value
                    return
                current = current.next
            
        
        else:
            while current is not None:      
                if previous is None:
                    if count == i:
                        temp = self._head
                        self._head = value
                        value.next = temp
                        self._size += 1
                        return
                        
                        
                elif count == i:
                    temp = previous.next
                    previous.next = value
                    value.next = temp
                    self._size += 1
                    return
                    
                previous = current
                current = current.next
                count += 1
