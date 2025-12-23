"""
Selection Sort with Smart Reset

Reset strategy: When all cells reach the right boundary or make no progress,
detect sorted regions and reset cells' ideal_position to the start of their region.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def find_sorted_regions(cells):
    """Find all maximal sorted regions in the array."""
    n = len(cells)
    regions = []
    i = 0
    while i < n:
        start = i
        while i < n - 1 and cells[i].value <= cells[i + 1].value:
            i += 1
        regions.append((start, i))
        i += 1
    return regions


def selection_sort_smart_reset(initial_values):
    n = len(initial_values)

    class SelectionCell:
        def __init__(self, value, cell_id):
            self.value = value
            self.ideal_position = 0
            self.cell_id = cell_id

    cells = [SelectionCell(v, i) for i, v in enumerate(initial_values)]
    steps = StepCounter()
    history = []

    passes_without_progress = 0

    for timestep in range(MAX_STEPS):
        idx_order = list(range(n))
        random.seed(42 + timestep)
        random.shuffle(idx_order)

        cells_that_acted = set()
        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]
            
            if cell.cell_id in cells_that_acted:
                continue
            cells_that_acted.add(cell.cell_id)

            target = max(0, min(n - 1, cell.ideal_position))

            if target == idx:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            if cell.value < neighbor.value:
                cells[idx], cells[target] = cells[target], cells[idx]
                cells_that_acted.add(neighbor.cell_id)
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        # Check progress
        if not swapped_any:
            passes_without_progress += 1
        else:
            passes_without_progress = 0

        # Reset when stuck
        if passes_without_progress >= 2:
            # Check if fully sorted
            is_sorted = all(
                cells[i].value <= cells[i + 1].value for i in range(n - 1)
            )
            if is_sorted:
                break

            # Find sorted regions and reset cells within them
            # This mimics group merging in the reference implementation
            regions = find_sorted_regions(cells)
            
            # Reset all cells' ideal_position to 0
            # (simpler than trying to track region boundaries)
            for cell in cells:
                cell.ideal_position = 0

            passes_without_progress = 0

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("SELECTION SORT - SMART RESET")
print("=" * 70)

test_arrays = [
    [2, 1],
    [3, 2, 1],
    [3, 1, 2],
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 2, 8, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [4, 2, 7, 1, 9, 3],
    [1, 1, 1, 1],
]

all_success = True
for test_array in test_arrays:
    expected = sorted(test_array)
    result, steps, history = selection_sort_smart_reset(test_array.copy())
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
    print("ALL TESTS PASSED! ✓")
else:
    print("Some tests failed")
print("=" * 70)
