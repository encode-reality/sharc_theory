"""
Test selection sort where cells continuously search from left to right,
resetting ideal_position based on current position after moves.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_continuous_search(initial_values):
    """
    Selection sort where each cell:
    1. Starts with ideal_position at leftmost (0)
    2. Tries to swap with cell at ideal_position
    3. If swaps: reset ideal_position to search from current position
    4. If doesn't swap: increment ideal_position
    5. Keep going until can't move anymore
    """
    n = len(initial_values)

    class CellWithIdealPos:
        def __init__(self, value, pos):
            self.value = value
            self.initial_pos = pos
            self.ideal_position = 0

        def can_initiate_move(self):
            return True

        def can_be_moved(self):
            return True

    cells = [CellWithIdealPos(v, i) for i, v in enumerate(initial_values)]
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

            target = max(0, min(n - 1, cell.ideal_position))

            # Skip if target is self
            if target == idx:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells
                cells[idx], cells[target] = cells[target], cells[idx]
                # RESET ideal_position to 0 to search again from beginning
                cell.ideal_position = 0
                neighbor.ideal_position = 0
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # Increment ideal_position to try next position
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("TESTING SELECTION SORT WITH CONTINUOUS SEARCH (RESET AFTER SWAP)")
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
    result, steps, history = selection_sort_continuous_search(test_array.copy())
    correct = result == expected

    print(f"\nArray:    {test_array}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")
    print(f"Correct:  {'✓ YES!' if correct else '✗ NO'}")
    print(f"Steps:    {steps.total} (comparisons: {steps.comparisons}, swaps: {steps.swaps})")

print("\n" + "=" * 70)
