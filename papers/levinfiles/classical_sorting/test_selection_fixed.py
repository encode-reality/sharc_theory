"""
Selection Sort - Correct Implementation

Based on reference implementation:
- ideal_position is a property of the CELL, not the position
- When cells swap, they carry their ideal_position with them
- ideal_position increments when value >= target.value
- Resets to 0 when no progress detected
"""

import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_fixed(initial_values):
    """
    Selection sort with ideal_position as cell property.
    """
    n = len(initial_values)

    class SelectionCell:
        def __init__(self, value):
            self.value = value
            self.ideal_position = 0  # Each cell tracks its own ideal_position

        def can_initiate_move(self):
            return True

        def can_be_moved(self):
            return True

    cells = [SelectionCell(v) for v in initial_values]

    steps = StepCounter()
    history = []

    consecutive_no_swap_passes = 0
    max_no_swap_passes = 2

    for timestep in range(MAX_STEPS):
        idx_order = list(range(n))
        random.seed(42 + timestep)
        random.shuffle(idx_order)

        swapped_any = False

        # Process each cell
        for idx in idx_order:
            cell = cells[idx]
            if not cell.can_initiate_move():
                continue

            target = cell.ideal_position  # Cell's property, not array index!

            # Clamp target to valid range
            target = max(0, min(n - 1, target))

            # Skip if target is self
            if target == idx:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            # Reference: swap if value < target, else increment ideal_position
            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells - they carry their ideal_position with them
                cells[idx], cells[target] = cells[target], cells[idx]
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # value >= target.value, increment ideal_position
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        # Reset mechanism
        if not swapped_any:
            consecutive_no_swap_passes += 1

            if consecutive_no_swap_passes >= max_no_swap_passes:
                # Check if sorted
                is_sorted = all(
                    cells[i].value <= cells[i + 1].value for i in range(n - 1)
                )
                if is_sorted:
                    break

                # Reset all cells' ideal_position (mimics update())
                for cell in cells:
                    cell.ideal_position = 0
                consecutive_no_swap_passes = 0
        else:
            consecutive_no_swap_passes = 0

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("SELECTION SORT - FIXED IMPLEMENTATION")
print("=" * 70)
print("\nKey insight: ideal_position is a CELL property, not position property")
print("Cells carry their ideal_position when they swap positions\n")

test_arrays = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 2, 8, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [4, 2, 7, 1, 9, 3],
    [1, 1, 1, 1],
    [2, 1],
]

for test_array in test_arrays:
    expected = sorted(test_array)
    result, steps, history = selection_sort_fixed(test_array.copy())
    correct = result == expected

    print(f"Array:    {test_array}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")
    print(f"Correct:  {correct}")
    print(f"Steps:    {steps.total} (comparisons: {steps.comparisons}, swaps: {steps.swaps})")

    if correct:
        print("  >>> SUCCESS!")
    else:
        print("  >>> FAILED")
    print()

print("=" * 70)
