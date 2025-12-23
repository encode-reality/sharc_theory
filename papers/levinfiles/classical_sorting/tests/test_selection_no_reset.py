import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Test Selection Sort WITHOUT reset to see basic behavior"""

import random
from modules.core import StepCounter, MAX_STEPS


def selection_sort_no_reset(initial_values, max_steps=100):
    n = len(initial_values)

    class SelectionCell:
        def __init__(self, value, cell_id):
            self.value = value
            self.ideal_position = 0
            self.cell_id = cell_id

    cells = [SelectionCell(v, i) for i, v in enumerate(initial_values)]
    steps = StepCounter()

    for timestep in range(max_steps):
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

            else:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        if not swapped_any:
            break

    return [c.value for c in cells], steps


# Test simple cases
for test_array in [[2, 1], [3, 2, 1], [3, 1, 2]]:
    result, steps = selection_sort_no_reset(test_array.copy())
    expected = sorted(test_array)
    print(f"Array:    {test_array}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")
    print(f"Correct:  {result == expected}")
    print(f"Steps:    {steps.total} (swaps: {steps.swaps})")
    print()
