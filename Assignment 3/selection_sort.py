def selection_sort(lst: list) -> tuple[int, int]:
    """Sort lst into ascending order using the selection sort, and return the
    number of element comparisons and swaps performed while sorting.
    """
    compare = 0
    swaps = 0

    for i, item in enumerate(lst):
        min_idx = len(lst) - 1
        for j in range(i, len(lst)):
            compare += 1
            if lst[j] < lst[min_idx]:
                min_idx = j
        if min_idx != i:
            lst[min_idx], lst[i] = lst[i], lst[min_idx]
            swaps += 1

    return (compare, swaps)
