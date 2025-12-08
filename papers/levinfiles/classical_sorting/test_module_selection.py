"""Test the updated selection_sort module"""

from modules.cell_view_sorts import selection_sort

test_arrays = [
    [2, 1],
    [3, 2, 1],
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 2, 8, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
]

print('Testing updated selection_sort module:')
print('=' * 60)

all_pass = True
for arr in test_arrays:
    result, steps, history = selection_sort(arr.copy())
    expected = sorted(arr)
    passed = result == expected
    all_pass = all_pass and passed
    
    print(f'Array: {arr}')
    print(f'Result: {result}')
    print(f'Expected: {expected}')
    print(f'Status: {"PASS" if passed else "FAIL"}')
    print(f'Swaps: {steps.swaps}')
    print()

print('=' * 60)
print(f'Overall: {"ALL TESTS PASSED!" if all_pass else "SOME TESTS FAILED"}')
