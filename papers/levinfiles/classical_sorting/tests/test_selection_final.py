"""
Selection Sort - Final Correct Implementation

Key insight: Each cell acts ONCE per timestep based on its position at START of timestep
- Use cell identity tracking to ensure cells don't act twice
- Cells carry their ideal_position when they swap positions
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_final(initial_values):
    """
    Selection sort with proper cell identity tracking.
    """
    n = len(initial_values)

    class SelectionCell:
        def __init__(self, value, cell_id):
            self.value = value
            self.ideal_position = 0
            self.cell_id = cell_id  # Unique identifier

        def can_initiate_move(self):
            return True

        def can_be_moved(self):
            return True

    cells = [SelectionCell(v, i) for i, v in enumerate(initial_values)]
    steps = StepCounter()
    history = []

    consecutive_no_swap_passes = 0
    max_no_swap_passes = 2

    for timestep in range(MAX_STEPS):
        idx_order = list(range(n))
        random.seed(42 + timestep)
        random.shuffle(idx_order)

        # Track which cells have acted this timestep
        cells_that_acted = set()
        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]
            
            # Skip if this cell already acted this timestep
            if cell.cell_id in cells_that_acted:
                continue
                
            cells_that_acted.add(cell.cell_id)

            if not cell.can_initiate_move():
                continue

            target = max(0, min(n - 1, cell.ideal_position))

            if target == idx:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells
                cells[idx], cells[target] = cells[target], cells[idx]
                # Mark both cells as having acted
                cells_that_acted.add(neighbor.cell_id)
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        # Reset mechanism
        if not swapped_any:
            consecutive_no_swap_passes += 1

            if consecutive_no_swap_passes >= max_no_swap_passes:
                is_sorted = all(
                    cells[i].value <= cells[i + 1].value for i in range(n - 1)
                )
                if is_sorted:
                    break

                # Reset all ideal_positions (mimics update())
                for cell in cells:
                    cell.ideal_position = 0
                consecutive_no_swap_passes = 0
        else:
            consecutive_no_swap_passes = 0

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("SELECTION SORT - FINAL CORRECT IMPLEMENTATION")
print("=" * 70)
print("\nKey fix: Track cell identity to ensure each cell acts once per timestep\n")

test_arrays = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 2, 8, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [4, 2, 7, 1, 9, 3],
    [1, 1, 1, 1],
    [2, 1],
]

all_success = True
for test_array in test_arrays:
    expected = sorted(test_array)
    result, steps, history = selection_sort_final(test_array.copy())
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
        all_success = False
    print()

print("=" * 70)
if all_success:
    print("ALL TESTS PASSED!")
else:
    print("Some tests failed")
print("=" * 70)
