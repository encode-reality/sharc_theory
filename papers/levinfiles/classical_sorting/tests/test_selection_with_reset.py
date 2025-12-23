"""
Selection Sort with Reset Mechanism

Based on reference implementation insights:
- ideal_position starts at 0 (left boundary)
- Increments when cell.value >= target.value
- Resets to left boundary when local region becomes sorted
- This mimics the update() call in the reference implementation

Simplified from full group merging - just detect sorted regions and reset.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_with_reset(initial_values):
    """
    Selection sort with automatic reset when no progress is made.

    Key insight from reference implementation:
    - update() resets ideal_position to left_boundary
    - This happens when groups merge (i.e., when sorted regions are recognized)
    - For our timestep model: detect when no swaps occur, reset all ideal_positions
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
    ideal_positions = [0 for _ in range(n)]  # Start at left boundary (0)

    steps = StepCounter()
    history = []

    consecutive_no_swap_passes = 0
    max_no_swap_passes = 2  # Reset after 2 passes without swaps

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

            target = ideal_positions[idx]

            # Clamp target to valid range
            target = max(0, min(n - 1, target))

            # Skip if target is self
            if target == idx:
                ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            # Reference implementation line 59: if value >= target, increment ideal_position
            # Only swap if value < target
            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells
                cells[idx], cells[target] = cells[target], cells[idx]
                # Swap ideal_positions (cells carry their state)
                ideal_positions[idx], ideal_positions[target] = (
                    ideal_positions[target],
                    ideal_positions[idx]
                )
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # value >= target.value, increment ideal_position
                ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)

        # Check if we made progress
        if not swapped_any:
            consecutive_no_swap_passes += 1

            # After N passes with no swaps, reset all ideal_positions
            # This mimics the update() call in the reference implementation
            if consecutive_no_swap_passes >= max_no_swap_passes:
                # Check if fully sorted
                is_sorted = all(
                    cells[i].value <= cells[i + 1].value for i in range(n - 1)
                )
                if is_sorted:
                    break

                # Reset all ideal_positions to 0 (left boundary)
                # This is equivalent to calling update() on all cells
                ideal_positions = [0 for _ in range(n)]
                consecutive_no_swap_passes = 0
        else:
            consecutive_no_swap_passes = 0

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("TESTING: SELECTION SORT WITH RESET MECHANISM")
print("=" * 70)
print("\nBased on reference implementation:")
print("- ideal_position increments when value >= target")
print("- Resets to 0 when no progress is made")
print("- Mimics the update() call from CellGroup.merge_with_group()")
print()

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
    result, steps, history = selection_sort_with_reset(test_array.copy())
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
