"""
Test selection sort where cells find their proper slot.

Hypothesis: Instead of all cells competing for position 0, each cell
should find the FIRST position where it belongs (where it's >= all cells
to the left). This is more like insertion sort logic but with selection
sort's global view.
"""

import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_find_slot(initial_values):
    """
    Each cell scans from left to right to find where it belongs.
    It tries to swap with the FIRST position where swapping would
    improve local order.
    """
    n = len(initial_values)

    class SimpleCell:
        def __init__(self, value):
            self.value = value

        def can_initiate_move(self):
            return True

        def can_be_moved(self):
            return True

    cells = [SimpleCell(v) for v in initial_values]
    ideal_positions = [0 for _ in range(n)]
    steps = StepCounter()
    history = []

    for timestep in range(MAX_STEPS):
        idx_order = list(range(n))
        random.seed(42 + timestep)
        random.shuffle(idx_order)

        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]
            if not cell.can_initiate_move():
                continue

            # Search for the first position where I should be
            # Start from ideal_position
            target = ideal_positions[idx]
            target = max(0, min(n - 1, target))

            # Skip if target is self
            if target == idx:
                # Move to next position
                ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            # Check if swapping would help
            # Swap if: moving left and I'm smaller, OR moving right and I'm larger
            should_swap = False
            if target < idx:
                # Trying to move left - swap if I'm smaller
                should_swap = cell.value < neighbor.value
            else:
                # Trying to move right - swap if I'm larger
                should_swap = cell.value > neighbor.value

            if should_swap and neighbor.can_be_moved():
                # Swap
                cells[idx], cells[target] = cells[target], cells[idx]
                ideal_positions[idx], ideal_positions[target] = (
                    ideal_positions[target],
                    ideal_positions[idx]
                )
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # Try next position
                ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)

        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("TESTING: CELLS FIND THEIR PROPER SLOT")
print("=" * 70)

test_arrays = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 2, 8, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [4, 2, 7, 1, 9, 3],
]

for test_array in test_arrays:
    expected = sorted(test_array)
    result, steps, history = selection_sort_find_slot(test_array.copy())
    correct = result == expected

    print(f"\nArray:    {test_array}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")
    print(f"Correct:  {correct}")
    print(f"Steps:    {steps.total} (comparisons: {steps.comparisons}, swaps: {steps.swaps})")

    if correct:
        print("  >>> SUCCESS! THIS WORKS!")

print("\n" + "=" * 70)
