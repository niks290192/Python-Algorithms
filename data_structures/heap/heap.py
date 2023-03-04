from __future__ import annotations

from collections.abc import Iterable

class Heap:
    """A Max heap implementation

    >>> unsorted = [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
    >>> h = Heap()
    >>> h.build_max_heap(unsorted)
    >>> h
    [209, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]
    >>>
    >>> h.extract_max()
    209
    >>> h
    [201, 107, 25, 103, 11, 15, 1, 9, 7, 5]
    >>>
    >>> h.insert(100)
    >>> h
    [201, 107, 25, 103, 15, 1, 9, 7, 5, 11]
    >>>
    >>> h.heap_sort()
    >>> h
    [1, 5, 7, 9, 11, 15, 25, 100, 103, 107, 201]
    """

    def __init__(self) -> None:
        self.h: list[float] = []
        self.heap_size: int = 0

    def __repr__(self) -> str:
        return str(self.h)

    def parent_index(self, child_idx: int) -> int | None:
        """return the parent index of given child"""
        if child_idx > 0:
            return (child_idx - 1) // 2
        return None

    def left_child_idx(self, parent_idx: int) -> int | None:
        """
        :return the left child index if the left child exists.
        if not, return None.
        """
        left_child_index = 2 * parent_idx + 1
        if left_child_index < self.heap_size:
            return left_child_index
        return None

    def right_child_idx(self, parent_idx: int) -> int | None:
        """
        :return the right child index if the right child exists.
        if not, return None.
        """
        right_child_index = 2 * parent_idx + 2
        if right_child_index < self.heap_size:
            return right_child_index
        return None

    def max_heapify(self, index: int) -> None:
        """
        correct a single violation of the heap property in a subtree's root.
        """
        if index < self.heap_size:
            violation: int = index
