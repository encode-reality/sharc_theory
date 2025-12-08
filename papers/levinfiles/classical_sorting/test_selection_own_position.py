"""
Selection Sort - Start with ideal_position = current_position

Based on reference implementation discovery:
- Reference starts each cell with ideal_position = current_position (own group)
- Groups merge when sorted, then update() resets ideal_position
- For our model: start with own position, periodically reset to 0
"""

import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_own_position(initial_values):
    n = len(initial_values)

    class SelectionCell:
        def __init__(self, value, cell_id, position):
            self.value = value
            self.ideal_position = position  # Start at own position!
            self.cell_id = cell_id

    cells = [SelectionCell(v, i, i) for i, v in enumerate(initial_values)]
    steps = StepCounter()
    history = []

    # Immediately reset all to 0 (simulating first merge)
    for cell in cells:
        cell.ideal_position = 0

    passes_without_swaps = 0

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

        if not swapped_any:
            passes_without_swaps += 1
            
            if passes_without_swaps >= 2:
                is_sorted = all(cells[i].value <= cells[i + 1].value for i in range(n - 1))
                if is_sorted:
                    break
                    
                # Reset (simulating merge/update())
                for cell in cells:
                    cell.ideal_position = 0
                passes_without_swaps = 0
        else:
            passes_without_swaps = 0

    return [c.value for c in cells], steps, history


# Test
print("=" * 70)
print("SELECTION SORT - Own Position Start")
print("=" * 70)

test_arrays = [
    [2, 1],
    [3, 2, 1],
    [3, 1, 2],
    [3, 1, 4, 1, 5, 9, 2, 6],
]

for test_array in test_arrays:
    expected = sorted(test_array)
    result, steps, history = selection_sort_own_position(test_array.copy())
    correct = result == expected

    print(f"Array:    {test_array}")
    print(f"Result:   {result}")
    print(f"Correct:  {correct}")
    print(f"Swaps:    {steps.swaps}")
    print()
