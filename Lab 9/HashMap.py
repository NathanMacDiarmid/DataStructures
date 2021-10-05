# SYSC 2100 Winter 2021 Lab 9 / Assignment 2
# Last edited: Mar. 15, 2021

# An implementation of ADT Map that uses a hash table as the
# underlying data structure.

from typing import Any


def _to_str(val: Any) -> str:
    """If val is a string, return val enclosed in single-quotes;
    otherwise return str(val).

    >>> _to_str(5)
    '5'
    >>> _to_str('Hello')
    "'Hello'"
    >>> _to_str("Hello")
    "'Hello'"

    # Create s string of the form '(value)', where value is enclosed in
    # single quotes if it's a string.
    >>> value = 42
    >>> "(" + _to_str(value) + ")"   # or, "({0})".format(_to_str(value))
    '(42)'
    >>> value = 'word'
    >>> "(" + _to_str(value) + ")"   # or, "({0})".format(_to_str(value))
    "('word')"

    """
    if isinstance(val, str):
        return "'{0}'".format(val)
    return str(val)


class Entry:
    """An entry in a chain in a hash table."""

    def __init__(self, key: Any, value: Any) -> None:
        """Initialize this Entry with key and the associated value.
        The entry's link is initialized with the end-of-list marker (None).
        """
        self._key = key
        self._value = value
        self._next = None

    def get_key(self) -> Any:
        """Return this entry's key."""
        return self._key

    def set_key(self, key: Any) -> None:
        """Replace this entry's key with key."""
        self._key = value

    key = property(get_key, set_key)

    def get_value(self) -> Any:
        """Return the value part of this entry."""
        return self._value

    def set_value(self, value: Any) -> None:
        """Replace the value part of this entry with value."""
        self._value = value

    value = property(get_value, set_value)

    # Using 'Entry' as a type annotation is the PEP 484 hack for handling
    # forward references. Starting with Python 3.10, we should be able to
    # use Entry as a type annotation within the class.

    def get_next(self) -> 'Entry':
        """Return the reference (pointer) to the entry that follows this entry,
        or None if this entry is at the end of a chain.
        """
        return self._next

    def set_next(self, next_entry: 'Entry') -> None:
        """Append next_entry to this entry."""
        self._next = next_entry

    next = property(get_next, set_next)

    def __str__(self) -> str:
        """Return a string representation of the (key, value) pair stored
        in this entry, in the form "(key, value)".
        """
        return "(" + _to_str(self.key) + ", " + _to_str(self.value) + ")"

    def __repr__(self) -> str:
        """Return a string representation of the (key, value) pair stored
        in this entry, in the form "Entry(key, value)".
        """
        return 'Entry' + str(self)


TABLE_SIZE = 11  # of slots in the hash table

class HashMap:

    def __init__(self, iterable=None) -> None:
        """Initialize this HashMap with the contents of iterable
        (a sequence of (key, value) pairs).

        If iterable isn't provided, the new map is empty.

        >>> map = HashMap()
        >>> map
        {}

        >>> supplies = HashMap([('pencils', 1), ('erasers', 2), ('pens', 5)])
        >>> supplies
        {'erasers': 2, 'pens': 5, 'pencils': 1}
        """
        self._slots = [None] * TABLE_SIZE
        self._size = 0
        if iterable is not None:
            for key, value in iterable:
                self.put(key, value)  # put will increment _size

    def __str__(self) -> str:
        """Return a string representation of this map, in the format:
        "{key_1: value_1, key_2: value_2, ...}"

        >>> map = HashMap()
        >>> str(map)
        '{}'

        >>> supplies = HashMap()
        >>> supplies.put('pencils', 1)
        >>> supplies.put('erasers', 2)
        >>> supplies.put('pens', 5)
        >>> str(supplies)
        "{'erasers': 2, 'pens': 5, 'pencils': 1}"
        """
        if self._size == 0:
            return '{}'

        # Traverse the hash table's chains from head to tail, collecting the
        # (key, value) pairs as a list of strings.
        items = []
        for i in range(len(self._slots)):
            if self._slots[i] is not None:
                entry = self._slots[i]
                while entry is not None:
                    # Represent the entry as: 'key: value'.
                    items.append(_to_str(entry.key) + ": " + _to_str(entry.value))
                    entry = entry.next

        return '{' + ', '.join(items) + '}'

    def __repr__(self) -> str:
        """Return a string representation of this map, in the format:
        "{key_1: value_1, key_2: value_2, ...}"

        >>> map = HashMap()
        >>> str(map)
        '{}'

        >>> supplies = HashMap()
        >>> supplies.put('pencils', 1)
        >>> supplies.put('erasers', 2)
        >>> supplies.put('pens', 5)
        >>> supplies
        {'erasers': 2, 'pens': 5, 'pencils': 1}
        """
        return str(self)

    def _hash_function(self, key: Any, size: int) -> int:
        """Hash key into a slot (an index in the hash table) in the
        range 0..size - 1, and return that slot.

        Precondition: key must be hashable.
        Precondition: size > 0.

        >>> map = HashMap()
        >>> map._hash_function(42, 11)
        9
        >>> map._hash_function(-42, 11)
        9
        >>> map._hash_function('pencil', 11)
        10
        """
        return abs(hash(key)) % size

    def put(self, key: Any, value: Any) -> None:
        """Insert key and the associated value in this map.

        If key is already in the map, replace the old value with value.

        Precondition: key is hashable.

        >>> supplies = HashMap()
        >>> supplies.put('pencils', 1)
        >>> supplies.put('erasers', 2)
        >>> supplies.put('pencils', 7)
        >>> str(supplies)
        "{'erasers': 2, 'pencils': 7}"
        """
        entry = Entry(key, value)
        hash_value = self._hash_function(key, len(self._slots))

        if (self._slots[hash_value] is None):
            self._slots[hash_value] = entry
            self._size += 1

        else:
            if (self._slots[hash_value].get_key() == key):
                if (self._slots[hash_value].get_value() < value):
                    self._slots[hash_value] = entry

            else:
                new_hash_value = self._hash_function(hash_value + 1, len(self._slots))
                count = 0

                while (self._slots[new_hash_value] is not None):

                    if (count > TABLE_SIZE):
                        break
                    if (self._slots[new_hash_value].get_key() == key):
                        if (self._slots[new_hash_value].get_value() < value):
                            self._slots[new_hash_value] = entry
                            break
                    new_hash_value = self._hash_function(new_hash_value + 1, len(self._slots))
                    count += 1

                if (self._slots[new_hash_value] is None):
                    self._slots[new_hash_value] = entry
                    self._size += 1

                elif (self._slots[new_hash_value].get_key() != key):
                    old_entry = self._slots[new_hash_value]
                    self._slots[new_hash_value] = entry
                    entry.next = old_entry
                    self._size += 1

    def get(self, key: Any, default=None) -> Any:
        """If key is in the map, return the value associated with key;
        otherwise return default. If key is not in the map and default is
        not given, return None.

        Precondition: key is hashable.

        >>> supplies = HashMap()
        >>> supplies.put('pencils', 1)
        >>> supplies.put('erasers', 2)
        >>> supplies.put('pens', 5)
        >>> supplies.get('pencils')
        1
        >>> supplies.get('rulers', 0)
        0
        >>> print(supplies.get('rulers'))
        None
        """
        for i in self._slots:
            test = i
            while (test is not None):
                if (test.get_key() == key):
                    return test.get_value()
                test = test.next

        if (default != None):
            return default
        else:
            return print(None)

    def __len__(self) -> int:
        """Return the number of (key, value) pairs in this map.

        >>> map = HashMap()
        >>> len(map)
        0

        >>> supplies = HashMap()
        >>> supplies.put('pencils', 1)
        >>> supplies.put('erasers', 2)
        >>> supplies.put('pens', 5)
        >>> len(supplies)
        3
        """
        return self._size

    def __contains__(self, key: Any) -> bool:
        """Return True if key is in the HashMap; otherwise False

        Precondition: key must be hashable.

        >>> map = HashMap()
        >>> 5 in map
        False

        >>> supplies = HashMap()
        >>> supplies.put('pencils', 1)
        >>> supplies.put('erasers', 2)
        >>> supplies.put('pens', 5)
        >>> 'pencils' in supplies
        True
        >>> 'rulers' in supplies
        False
        """
        for i in self._slots:
            test = i
            while (test is not None):
                if (test.get_key() == key):
                    return True
                test = test.next
        return False

    def pop(self, key: Any, default: Any = None) -> Any:
        """If key is in the map, remove it and return the value associated
        with the key; otherwise return default. If key is not in the map
        and default is not given, raise a KeyError with the message,
        "Key key not found"

        Precondition: key is hashable.

        >>> supplies = HashMap()
        >>> supplies.put('pencils', 1)
        >>> supplies.put('erasers', 2)
        >>> supplies.put('pens', 5)

        >>> supplies.pop('erasers')
        2
        >>> supplies
        {'pens': 5, 'pencils': 1}

        >>> supplies.pop('rulers', 0)
        0
        >>> supplies
        {'pens': 5, 'pencils': 1}

        >>> supplies.pop('rulers')
        builtins.KeyError: 'Key rulers not found'
        >>> supplies
        {'pens': 5, 'pencils': 1}
        """
        index = 0
        for i in self._slots:
            test = i
            while (test is not None):
                if (test.get_key() == key):
                    if (test.next is None):
                        value = test.get_value()
                        self._slots[index] = None
                        self._size -= 1
                        return value
                    else:
                        value = test.get_value()
                        self._slots[index] = self._slots[index].next
                        self._size -= 1
                        return value
                test = test.next
            index += 1

        if (default is not None):
            return default
        else:
            raise KeyError("Key not found.")
