from bubble_sort import bubble_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from heapsort import heapsort
import random

# All sorted lists for varying sizes

sorted_list_10 = list(range(1, 11))
sorted_list_100 = list(range(1, 101))
sorted_list_500 = list(range(1, 501))
sorted_list_1000 = list(range(1, 1001))

# Reverse sorted lists in varying sizes for bubble_sort()

b_reverse_sorted_10 = list(reversed(range(1, 11)))
b_reverse_sorted_100 = list(reversed(range(1, 101)))
b_reverse_sorted_500 = list(reversed(range(1, 501)))
b_reverse_sorted_1000 = list(reversed(range(1, 1001)))

# All random lists in varying sizes for bubble_sort()

b_random_list_10 = random.sample(range(1, 11), 10)
b_random_list_100 = random.sample(range(1, 101), 100)
b_random_list_500 = random.sample(range(1, 501), 500)
b_random_list_1000 = random.sample(range(1, 1001), 1000)

# Reverse sorted lists in varying sizes for selection_sort()

s_reverse_sorted_10 = list(reversed(range(1, 11)))
s_reverse_sorted_100 = list(reversed(range(1, 101)))
s_reverse_sorted_500 = list(reversed(range(1, 501)))
s_reverse_sorted_1000 = list(reversed(range(1, 1001)))

# All random lists in varying sizes for selection_sort()

s_random_list_10 = random.sample(range(1, 11), 10)
s_random_list_100 = random.sample(range(1, 101), 100)
s_random_list_500 = random.sample(range(1, 501), 500)
s_random_list_1000 = random.sample(range(1, 1001), 1000)

# Reverse sorted lists in varying sizes for merge_sort()

m_reverse_sorted_10 = list(reversed(range(1, 11)))
m_reverse_sorted_100 = list(reversed(range(1, 101)))
m_reverse_sorted_500 = list(reversed(range(1, 501)))
m_reverse_sorted_1000 = list(reversed(range(1, 1001)))

# All random lists in varying sizes for merge_sort()

m_random_list_10 = random.sample(range(1, 11), 10)
m_random_list_100 = random.sample(range(1, 101), 100)
m_random_list_500 = random.sample(range(1, 501), 500)
m_random_list_1000 = random.sample(range(1, 1001), 1000)

# Reverse sorted lists in varying sizes for heapsort()

h_reverse_sorted_10 = list(reversed(range(1, 11)))
h_reverse_sorted_100 = list(reversed(range(1, 101)))
h_reverse_sorted_500 = list(reversed(range(1, 501)))
h_reverse_sorted_1000 = list(reversed(range(1, 1001)))

# All random lists in varying sizes for heapsort()

h_random_list_10 = random.sample(range(1, 11), 10)
h_random_list_100 = random.sample(range(1, 101), 100)
h_random_list_500 = random.sample(range(1, 501), 500)
h_random_list_1000 = random.sample(range(1, 1001), 1000)


print("\n------ BEGIN TESTS ------\n")

# Testing for bubble_sort() with sorted lists

print("\n------ TESTING SORTED LISTS WITH BUBBLE_SORT() ------\n")
print(bubble_sort(sorted_list_10))
print(bubble_sort(sorted_list_100))
print(bubble_sort(sorted_list_500))
print(bubble_sort(sorted_list_1000))

# Testing for bubble_sort() with reverse sorted lists

print("\n------ TESTING REVERSE SORTED LISTS WITH BUBBLE_SORT() ------\n")
print(bubble_sort(b_reverse_sorted_10))
print(bubble_sort(b_reverse_sorted_100))
print(bubble_sort(b_reverse_sorted_500))
print(bubble_sort(b_reverse_sorted_1000))

# Testing for bubble_sort() with unsorted lists

print("\n------ TESTING UNSORTED LISTS WITH BUBBLE_SORT() ------\n")
print(bubble_sort(b_random_list_10))
print(bubble_sort(b_random_list_100))
print(bubble_sort(b_random_list_500))
print(bubble_sort(b_random_list_1000))

# Testing for selection_sort() with sorted lists

print("\n------ TESTING SORTED LISTS WITH SELECTION_SORT() ------\n")
print(selection_sort(sorted_list_10))
print(selection_sort(sorted_list_100))
print(selection_sort(sorted_list_500))
print(selection_sort(sorted_list_1000))

# Testing for selection_sort() with reverse sorted lists

print("\n------ TESTING REVERSE SORTED LISTS WITH SELECTION_SORT() ------\n")
print(selection_sort(s_reverse_sorted_10))
print(selection_sort(s_reverse_sorted_100))
print(selection_sort(s_reverse_sorted_500))
print(selection_sort(s_reverse_sorted_1000))

# Testing for selection_sort() with unsorted lists

print("\n------ TESTING UNSORTED LISTS WITH SELECTION_SORT() ------\n")
print(selection_sort(s_random_list_10))
print(selection_sort(s_random_list_100))
print(selection_sort(s_random_list_500))
print(selection_sort(s_random_list_1000))

# Testing for merge_sort() with sorted lists

print("\n------ TESTING SORTED LISTS WITH MERGE_SORT() ------\n")
print(merge_sort(sorted_list_10))
print(merge_sort(sorted_list_100))
print(merge_sort(sorted_list_500))
print(merge_sort(sorted_list_1000))

# Testing for merge_sort() with reverse sorted lists

print("\n------ TESTING REVERSE SORTED LISTS WITH MERGE_SORT() ------\n")
print(merge_sort(m_reverse_sorted_10))
print(merge_sort(m_reverse_sorted_100))
print(merge_sort(m_reverse_sorted_500))
print(merge_sort(m_reverse_sorted_1000))

# Testing for merge_sort() with unsorted lists

print("\n------ TESTING UNSORTED LISTS WITH MERGE_SORT() ------\n")
print(merge_sort(m_random_list_10))
print(merge_sort(m_random_list_100))
print(merge_sort(m_random_list_500))
print(merge_sort(m_random_list_1000))

# Testing for heapsort() with sorted lists

print("\n------ TESTING SORTED LISTS WITH HEAPSORT() ------\n")
print(heapsort(sorted_list_10))
print(heapsort(sorted_list_100))
print(heapsort(sorted_list_500))
print(heapsort(sorted_list_1000))

# Testing for heapsort() with reverse sorted lists

print("\n------ TESTING REVERSE SORTED LISTS WITH HEAPSORT() ------\n")
print(heapsort(h_reverse_sorted_10))
print(heapsort(h_reverse_sorted_100))
print(heapsort(h_reverse_sorted_500))
print(heapsort(h_reverse_sorted_1000))

# Testing for heapsort() with unsorted lists

print("\n------ TESTING UNSORTED LISTS WITH HEAPSORT() ------\n")
print(heapsort(h_random_list_10))
print(heapsort(h_random_list_100))
print(heapsort(h_random_list_500))
print(heapsort(h_random_list_1000))

print("\n------ END TESTS ------\n")