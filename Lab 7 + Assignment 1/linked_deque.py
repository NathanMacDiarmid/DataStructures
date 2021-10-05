# SYSC 2100 ADT Deque (Implementation using a singly-linked list.)

# Last edited: Feb. 27, 2021, D.L. Bailey, SCE, Carleton University

from typing import Any


class Node:
    """A node in singly-linked list"""

    def __init__(self, node_data: Any) -> None:
        """Initialize this node with "payload" node_data.
        The node's link is initialized with the end-of-list marker (None).
        """
        self._data = node_data
        self._next = None

    def get_data(self) -> Any:
        """Return this node's payload."""
        return self._data

    def set_data(self, node_data: Any) -> None:
        """Replace this node's payload with node_data."""
        self._data = node_data

    data = property(get_data, set_data)

    # Using 'Node' as a type annotation is the PEP 484 hack for handling
    # forward references. Starting with Python 3.10, we should be able to
    # use Node as a type annotation within the class.

    def get_next(self) -> 'Node':
        """Return the reference (pointer) to the node that follows this node,
        or None if this node is at the end of a list.
        """
        return self._next

    def set_next(self, node_next: 'Node') -> None:
        """Append the node referred (pointed) to by node_next to this node."""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self) -> str:
        """Return a string representation of this node's payload."""
        return str(self._data)


class LinkedDeque:
    """An implementation of a deque (double-ended queue).

    The methods for adding items to the front or rear of a deque are O(1).
    The method for removing an item from the front of a deque is O(1).
    Unlike the deque class in the Python standard library, the method
    for removing an item from the rear of a deque is O(n).
    """
    # The data structure underlying this implementation of ADT Deque is a
    # circular singly-linked list.
    #
    # A LinkedDeque object has two instance variables:
    #
    #    _rear refers to the node at the rear of the deque;
    #    i.e., the last (tail) node in the linked list.
    #
    #    _size is the the number of items in the deque;
    #    i.e., the number of nodes in the linked list.

    def __init__(self, iterable=None) -> None:
        """Initialize this LinkedDeque with the contents of iterable.

        Items are added to the rear of the deque in the order they are returned
        by the iterable. If iterable isn't provided, the new deque is empty.

        >>> dq = LinkedDeque()
        >>> str(dq)
        'None'

        >>> dq = LinkedDeque([10, 20, 30])
        >>> str(dq)
        '10 -> 20 -> 30'

        >>> dq = LinkedDeque()  # Another way to create the same deque.
        >>> dq.add_rear(10)
        >>> dq.add_rear(20)
        >>> dq.add_rear(30)
        >>> str(dq)
        '10 -> 20 -> 30'
        """
        self._rear = None
        self._size = 0
        if iterable is not None:
            for elem in iterable:
                # add_rear will update _rear, increment _size
                self.add_rear(elem)

    def __str__(self) -> str:
        """Return a string representation of this deque, in the format:
        'value_1 -> value_2 -> value_3 ... -> value_n'

        value_1 is the value at the FRONT of the deque.
        value_n is the value at the REAR of the deque.

        >>> dq = LinkedDeque([10, 20, 30])
        >>> str(dq)
        '10 -> 20 -> 30'

        >>> dq = LinkedDeque()
        >>> str(dq)
        'None'

        >>> dq.add_rear(10)
        >>> str(dq)
        '10'
        >>> dq.add_rear(20)
        >>> str(dq)
        '10 -> 20'
        >>> dq.add_rear(30)
        >>> str(dq)
        '10 -> 20 -> 30'
        """
        if self._rear is None:
            return 'None'

        # Grab the reference to the front node.
        node = self._rear.next

        # Traverse the deque from the front node to the node immediately before
        # the rear node, collecting the data in the nodes as a list of strings.
        items = []
        while node is not self._rear:
            items.append(str(node.data))
            node = node.next

        # Now get the data from the node at the rear of the deque.
        items.append(str(node.data))

        # Concatenate the strings in items, with each pair separated by " -> "
        return " -> ".join(items)

    def __repr__(self) -> str:
        """Return a string representation of this deque.

        >>> dq = LinkedDeque([10, 20, 30])
        >>> repr(dq)
        'LinkedDeque([10, 20, 30])'
        >>> dq
        LinkedDeque([10, 20, 30])

        >>> dq = LinkedDeque()  # or, dq = LinkedDeque([])
        >>> dq
        LinkedDeque([])
        """
        if self._rear is None:
            return "LinkedDeque([])"

        node = self._rear.next
        items = []
        while node is not self._rear:
            items.append(node.data)
            node = node.next

        items.append(node.data)

        return "LinkedDeque({0})".format(items)

    def __len__(self) -> int:
        """Return the number of items in this deque.

        >>> dq = LinkedDeque([10, 20, 30])
        >>> len(dq)
        3
        """
        return self._size

    def add_rear(self, item: Any) -> None:
        """Add item at the rear of this deque.

        If the deque is used as a queue, add_rear enqueues item at the
        rear of the queue.

        >>> dq = LinkedDeque()
        >>> dq.add_rear(10)
        >>> dq.add_rear(20)
        >>> dq.add_rear(30)
        >>> str(dq)
        '10 -> 20 -> 30'
        # 10 (the first item added) is at the front of the deque,
        # 30 (the most recent item added) is at the rear.
        """
        newNode = Node(item)
        if self._rear is None:
            self._rear = newNode
            newNode.next = newNode
        else:
            newNode.next = self._rear.next
            self._rear.next = newNode
            self._rear = newNode
        self._size += 1

    def add_front(self, item: Any) -> None:
        """Add item to the front of this deque.

        If the deque is used as a stack, add_front pushes an item on the top
        of the stack.

        >>> dq = LinkedDeque()
        >>> dq.add_front(10)
        >>> dq.add_front(20)
        >>> dq.add_front(30)
        >>> str(dq)
        '30 -> 20 -> 10'
        # 30 (the most recently-added item) is at the front of the deque,
        # 10 (the first item added) is at the rear.
        """
        newNode = Node(item)
        if self._rear is None:
            self._rear = newNode
            newNode.next = newNode

        else:
            newNode.next = self._rear.next
            self._rear.next = newNode
        self._size += 1

    def remove_front(self) -> Any:
        """Remove and return (dequeue) the item at the front of this deque.

        Raise IndexError with the message, "remove_front: empty deque"
        if the deque is empty.

        If the deque is used as a queue, remove_front dequeues an item from
        the front of the queue.
        If the deque is used as a stack, remove_front pops an item from the
        top of the stack.

        >>> dq = LinkedDeque([10, 20, 30])
        >>> dq.remove_front()
        10
        >>> dq.remove_front()
        20
        >>> dq.remove_front()
        30
        """
        if self._rear is None:
            raise IndexError("remove_front: empty deque")

        removed = self._rear.next.data
        delete = self._rear.next
        self._rear.next = self._rear.next.next
        delete.next = None
        delete = None
        self._size -= 1
        return removed

    def remove_rear(self) -> Any:
        """Remove and return the item at the rear of this deque.

        Raise IndexError with the message, "remove_rear: empty deque"
        if the deque is empty.

        >>> dq = LinkedDeque([10, 20, 30])
        >>> dq.remove_rear()
        30
        >>> dq.remove_rear()
        20
        >>> dq.remove_rear()
        10
        """
        if self._rear is None:
            raise IndexError("remove_rear:empty deque")

        node = self._rear.next
        while node.next != self._rear:
            node = node.next

        removed = node.next.data
        delete = node.next
        self._rear = node
        self._rear.next = delete.next
        delete.next = None
        delete = None
        self._size -= 1
        return removed

    def peek_front(self) -> Any:
        """Return (but don't remove) the item at the front of this deque.

        Raise IndexError with the message, "peek_front: empty deque"
        if the deque is empty.

        >>> dq = LinkedDeque([10, 20, 30])
        >>> dq.peek_front()
        10
        """
        if self._rear is None:
            raise IndexError("peek_front: empty deque")

        return self._rear.next.data

    def peek_rear(self) -> Any:
        """Return (but don't remove) the item at the rear of this deque.

        Raise IndexError with the message, "peek_rear: empty deque"
        if the deque is empty.

        >>> dq = LinkedDeque([10, 20, 30])
        >>> dq.peek_rear()
        30
        """
        if self._rear is None:
            raise IndexError("peek_rear: empty deque")

        return self._rear.data
