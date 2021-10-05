class BinaryHeap:
    """The implementation of a min-heap from "Problem Solving with Algorithms
    and Data Structures using Python", 3rd ed., Section 7.10.3.
    """

    def __init__(self) -> None:
        """Initialize the empty heap.
        """
        self._heap = []

    def _perc_up(self, cur_idx: int) -> None:
        """Percolate the most-recently added item (at position
        cur_idx in _heap) up the tree until it reaches the position
        where the heap property is restored.
        """
        cur_idx,
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] > self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx],
                )
            cur_idx = parent_idx

    def _perc_down(self, cur_idx: int) -> None:
        """Percolate the item at position cur_idx in _heap down the tree
        until it reaches the position where the heap property is restored.
        """
        while 2 * cur_idx + 1 < len(self._heap):
            max_child_idx = self._get_max_child(cur_idx)
            if self._heap[cur_idx] < self._heap[max_child_idx]:
                self._heap[cur_idx], self._heap[max_child_idx] = (
                    self._heap[max_child_idx],
                    self._heap[cur_idx],
                )
            else:
                return
            cur_idx = max_child_idx

    def _get_max_child(self, parent_idx: int) -> int:
        """Given the index of a parent node in _heap (parameter parent_idx),
        return the index of the child node that has the smallest value.
        """
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        if self._heap[2 * parent_idx + 1] > self._heap[2 * parent_idx + 2]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2

    def heapify(self, not_a_heap: list) -> None:
        """Replace the contents of this heap with the items in not_a_heap.

        Any items that are in the heap before this method is called
        are discarded.
        """
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1

    def get_max(self) -> int:
        """Return the largest item in this heap.

        Precondition: len(self) > 0.
        """
        return self._heap[0]

    def insert(self, item: int) -> None:
        """Insert item in this heap.
        """
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def delete(self) -> int:
        """Return the smallest item in the heap and remove it from the heap.

        Precondition: len(self) > 0.
        """
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def is_empty(self) -> bool:
        """Return True if this heap is empty; otherwise False.
        """
        return not bool(self._heap)

    def __len__(self) -> int:
        """Return the number of items in this heap.
        """
        return len(self._heap)

    def __str__(self) -> str:
        """Return a string representation of this heap.
        """
        return str(self._heap)
