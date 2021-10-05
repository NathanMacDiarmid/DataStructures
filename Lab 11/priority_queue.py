class PriorityQueue:
    """An implementation of ADT PriorityQueue, using a max-heap.
    """

    def __init__(self) -> None:
        """Initialize the empty priority queue.
        """
        self._heap = []

    def is_empty(self) -> bool:
        """Return True if this priority queue is empty; otherwise False.
        """
        return not bool(self._heap)

    def __len__(self) -> int:
        """Return the number of items in this priority queue.
        """
        return len(self._heap)

    def __str__(self) -> str:
        """Return a string representation of this priority queue.
        """
        return str(self._heap)

    def insert(self, priority: int, item: str) -> None:
        """Insert item with the specified priority in this priority queue.
        """
        thing = (item, priority)
        self._heap.append(thing)
        self._perc_up(len(self._heap) - 1)

    def get_highest(self) -> str:
        """Return the item with the highest priority in this priority queue.

        Raise IndexError if the priority queue is empty.
        """
        if (self.is_empty()):
            raise IndexError("Queue is empty.")

        return self._heap[0][0]

    def remove_highest(self) -> str:
        """Return the item with the highest priority in this priority queue and
        remove it from the queue.

        Raise IndexError if the priority queue is empty.
        """
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def _perc_up(self, cur_idx: int) -> None:
        """Percolate the most-recently added item (at position
        cur_idx in _heap) up the tree until it reaches the position
        where the heap property is restored.
        """
        cur_idx,
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx][1] > self._heap[parent_idx][1]:
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
            if self._heap[cur_idx][1] < self._heap[max_child_idx][1]:
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
        if self._heap[2 * parent_idx + 1][1] > self._heap[2 * parent_idx + 2][1]:
            return 2 * parent_idx + 1
        return 2 * parent_idx + 2
