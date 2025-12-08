"""
Traditional (top-down) sorting algorithms.

These are the classic implementations where a single controller
has complete visibility and control over the entire array.

Each function returns:
    - sorted array
    - StepCounter (tracking comparisons and swaps)
    - sortedness history (list of sortedness values after each swap)
"""

from typing import List, Tuple
from .core import StepCounter
from .metrics import sortedness


def bubble_sort(arr: List[int]) -> Tuple[List[int], StepCounter, List[float]]:
    """
    Traditional bubble sort with top-down control.

    Algorithm:
    1. Start at beginning of array
    2. Compare adjacent elements, swap if out of order
    3. Repeat until no swaps needed

    Args:
        arr: List of integers to sort

    Returns:
        (sorted_array, step_counter, sortedness_history)
    """
    a = arr[:]  # Create a copy
    steps = StepCounter()
    sortedness_history = []

    n = len(a)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            steps.comparisons += 1
            if a[i] > a[i + 1]:
                # Swap
                a[i], a[i + 1] = a[i + 1], a[i]
                steps.swaps += 1
                swapped = True
                # Record sortedness after this swap
                sortedness_history.append(sortedness(a))

    return a, steps, sortedness_history


def insertion_sort(arr: List[int]) -> Tuple[List[int], StepCounter, List[float]]:
    """
    Traditional insertion sort with top-down control.

    Algorithm:
    1. Maintain sorted and unsorted portions
    2. Take first element from unsorted portion
    3. Insert it into correct position in sorted portion
    4. Repeat until all elements sorted

    Args:
        arr: List of integers to sort

    Returns:
        (sorted_array, step_counter, sortedness_history)
    """
    a = arr[:]  # Create a copy
    steps = StepCounter()
    sortedness_history = []

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0:
            steps.comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                steps.swaps += 1
                sortedness_history.append(sortedness(a))
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, steps, sortedness_history


def selection_sort(arr: List[int]) -> Tuple[List[int], StepCounter, List[float]]:
    """
    Traditional selection sort with top-down control.

    Algorithm:
    1. Find smallest element in unsorted portion
    2. Swap it with first element of unsorted portion
    3. Move boundary between sorted/unsorted one step right
    4. Repeat until all elements sorted

    Args:
        arr: List of integers to sort

    Returns:
        (sorted_array, step_counter, sortedness_history)
    """
    a = arr[:]  # Create a copy
    steps = StepCounter()
    sortedness_history = []

    n = len(a)

    for i in range(n):
        # Find minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            steps.comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j

        # Swap found minimum with first element of unsorted portion
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            steps.swaps += 1
            sortedness_history.append(sortedness(a))

    return a, steps, sortedness_history
