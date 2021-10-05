# SYSC 2100 Winter 2021 Lab 4
# Last edited: Feb. 2, 2021

# An implementation of ADT Bag that uses Python's dict type as the
# underlying data structure.

import random

class Bag:

    def __init__(self):
        """Initialize an empty bag.

        >>> bag = Bag()
        >>> bag
        {}
        """
        self._items = {}

    def __str__(self) -> str:
        """Return a string representation of this bag.

        >>> bag = Bag()
        >>> for x in ['a', 'b', 'c', 'd', 'c', 'b', 'a']:
        ...     bag.add(x)
        ...
        >>> str(bag)
        "{'a': 2, 'b': 2, 'c': 2, 'd': 1}"

        # Note: the order in which the items are listed may be different
        # from what is shown in this example.
        """
        return str(self._items)

    def __repr__(self) -> str:
        """Return a string representation of this bag.
        This string is identical to the one returned by __str__.

        >>> bag = Bag()
        >>> for x in ['a', 'b', 'c', 'd', 'c', 'b', 'a']:
        ...     bag.add(x)
        ....
        >>> repr(bag)
        "{'a': 2, 'b': 2, 'c': 2, 'd': 1}"
        >>> bag
        {'a': 2, 'b': 2, 'c': 2, 'd': 1}

        # Note: the order in which the items are listed may be different
        # from what is shown in these examples.
        """
        return "{0}".format(self._items)

    def __iter__(self):
        """Return an iterator for this bag.

        >>> bag = Bag()
        >>> for x in ['a', 'b', 'c', 'd', 'c', 'b', 'a']:
        ...     bag.add(x)
        ...
        >>> for x in bag:
        ...     print(x)
        ...
        ('a', 2)  # bag has two a's
        ('b', 2)  # bag has two b's
        ('c', 2)  # bag has two c's
        ('d', 1)  # bag has one d
        """
        # The iterator returned by this method produces a sequence of 2-tuples.
        # The first element in each tuple is an item in the bag, and the second
        # element is the number of occurrences of that item.
        return iter(self._items.items())

    def add(self, item: str) -> None:
        """Add item to this bag.

        >>> bag = Bag()
        >>> for x in ['c', 'a', 'b', 'c', 'd']:
        ...     bag.add(x)
        ...
        >>> bag
        {'c': 2, 'a': 1, 'b': 1, 'd': 1}

        # Note: the order in which the items are listed may be different
        # from what is shown in this example.
        """
        if (self._items.get(item) != None):
            self._items[item] += 1
            
        else:
            self._items[item] = 1

    def __len__(self) -> int:
        """Return the number of items in this bag.

        >>> bag = Bag()
        >>> len(bag)
        0
        >>> for x in ['a', 'b', 'c', 'd', 'c', 'b', 'a']:
        ...     bag.add(x)
        ...
        >>> len(bag)
        7
        """   
        return sum(self._items.values())

    def __contains__(self, item: str) -> bool:
        """Return True if item is in the bag.

        >>> bag = Bag()
        >>> for x in ['a', 'b', 'c', 'd']:
        ...     bag.add(x)
        ...
        >>> 'b' in bag
        True
        >>> 'k' in bag
        False
        """
        if (self._items.get(item) != None):
            return True
        
        else:
            return False

    def count(self, item: str) -> int:
        """Return the total number of occurrences of item in this bag.

        >>> bag = Bag()
        >>> for x in ['c', 'a', 'b', 'c', 'd']:
        ...     bag.add(x)
        ...
        >>> bag
        {'c': 2, 'a': 1, 'b': 1, 'd': 1}

        >>> bag.count('c')
        2
        >>> bag.count('k')
        0
        """
        if (self._items.get(item) != None):
            return self._items.get(item)
        
        else:
            return 0

    def remove(self, item: str) -> str:
        """Remove and return one instance of item from this bag.

        Raises KeyError if the bag is empty.
        Raises ValueError if item is not in the bag.

        >>> bag = Bag()
        >>> for x in ['c', 'a', 'b', 'c', 'd']:
        ...     bag.add(x)
        ...
        >>> bag
        {'c': 2, 'a': 1, 'b': 1, 'd': 1}

        >>> bag.remove('c')
        'c'
        >>> bag
        {'c': 1, 'a': 1, 'b': 1, 'd': 1}

        >>> bag.remove('c')
        'c'
        >>> bag
        {'a': 1, 'b': 1, 'd': 1}

        # Note: the order in which the items are listed may be different
        # from what is shown in these examples.
        """
        if (self._items == {}):
            raise KeyError("bag.remove(x): remove from empty bag")
        
        elif (self._items.get(item) == None):
            raise ValueError("bag.remove(x): x not in bag")
        
        else:
            self._items[item] -= 1
            
            if (self._items.get(item) == 0):
                del self._items[item]
                
            return item
        