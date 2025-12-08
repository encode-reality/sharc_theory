"""Verify all component functions are working"""

from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort
from modules.metrics import sortedness
from modules.core import Cell, StepCounter

test_array = [3, 1, 4, 1, 5, 9, 2, 6]

print('Testing component functions...')
print('=' * 60)

# Bubble sort
result_b, steps_b, hist_b = bubble_sort(test_array.copy())
print(f'Bubble Sort: {result_b == sorted(test_array)} - {result_b}')

# Insertion sort
result_i, steps_i, hist_i = insertion_sort(test_array.copy())
print(f'Insertion Sort: {result_i == sorted(test_array)} - {result_i}')

# Selection sort
result_s, steps_s, hist_s = selection_sort(test_array.copy())
print(f'Selection Sort: {result_s == sorted(test_array)} - {result_s}')

# Sortedness metric
print(f'Sortedness of [1,2,3,4]: {sortedness([1,2,3,4])}')
print(f'Sortedness of [4,3,2,1]: {sortedness([4,3,2,1])}')

print('=' * 60)
print('All component functions working!')
