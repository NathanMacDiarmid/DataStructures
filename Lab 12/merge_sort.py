def merge_sort(lst: list) -> tuple[int, int]:
    """Sort lst into ascending order using the merge sort, and return the
    number of element comparisons and swaps performed while sorting.
    """
    compare, swaps = 0, 0

    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        compare2, swaps2 = merge_sort(left_half)
        compare3, swaps3 = merge_sort(right_half)
        compare += compare2 + compare3
        swaps += swaps2 + swaps3

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            compare += 1
            if left_half[i] <= right_half[j]:
                lst[k] = left_half[i]
                swaps += 1
                i = i + 1
            else:
                lst[k] = right_half[j]
                swaps += 1
                j = j + 1
            k = k + 1

        while i < len(left_half):
            lst[k] = left_half[i]
            swaps += 1
            i = i + 1
            k = k + 1

        while j < len(right_half):
            lst[k] = right_half[j]
            swaps += 1
            j = j + 1
            k = k + 1

    return (compare, swaps)


