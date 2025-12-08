"""
Selection Sort - Correct Implementation (Two-Phase)

Key fix: Separate decision phase from execution phase
- Phase 1: Each cell decides what it wants to do based on current state
- Phase 2: Execute all decisions
- This avoids race conditions where cells process after being moved
"""

import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_correct(initial_values):
    """
    Selection sort with two-phase execution to avoid race conditions.
    """
    n = len(initial_values)

    class SelectionCell:
        def __init__(self, value):
            self.value = value
            self.ideal_position = 0

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

        # PHASE 1: Decide actions based on current state
        swaps_to_execute = []  # List of (idx, target) tuples

        for idx in idx_order:
            cell = cells[idx]
            if not cell.can_initiate_move():
                continue

            target = max(0, min(n - 1, cell.ideal_position))

            if target == idx:
                # Cell is at its ideal position, try next
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            # Decide: swap or increment?
            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Schedule swap
                swaps_to_execute.append((idx, target))
            else:
                # Increment ideal_position
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        # PHASE 2: Execute swaps
        # Only execute first swap to maintain simplicity
        # (cells can only perform one action per timestep)
        if swaps_to_execute:
            idx, target = swaps_to_execute[0]
            cells[idx], cells[target] = cells[target], cells[idx]
            steps.swaps += 1
            history.append(sortedness([c.value for c in cells]))

        swapped_any = len(swaps_to_execute) > 0

        # Reset mechanism
        if not swapped_any:
            consecutive_no_swap_passes += 1

            if consecutive_no_swap_passes >= max_no_swap_passes:
                is_sorted = all(
                    cells[i].value <= cells[i + 1].value for i in range(n - 1)
                )
                if is_sorted:
                    break

                # Reset all ideal_positions
                for cell in cells:
                    cell.ideal_position = 0
                consecutive_no_swap_passes = 0
        else:
            consecutive_no_swap_passes = 0

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("SELECTION SORT - CORRECT IMPLEMENTATION (TWO-PHASE)")
print("=" * 70)
print("\nFix: Separate decision and execution phases")
print("Prevents cells from being processed after they've just moved\n")

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
    result, steps, history = selection_sort_correct(test_array.copy())
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
