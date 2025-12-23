"""
Test selection sort following the spec EXACTLY with no optimizations.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def selection_sort_exact_spec(initial_values):
    """
    Follows the spec in replication_summary.md exactly, with NO optimizations.
    """
    n = len(initial_values)

    class SimpleCell:
        def __init__(self, value):
            self.value = value
            self.algotype = "selection"
            self.frozen_type = "active"

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

            # NO SKIP CHECK - follow spec exactly
            target = ideal_positions[idx]
            target = max(0, min(n - 1, target))
            neighbor = cells[target]

            steps.comparisons += 1
            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells and ideal_positions
                cells[idx], cells[target] = cells[target], cells[idx]
                ideal_positions[idx], ideal_positions[target] = (
                    ideal_positions[target],
                    ideal_positions[idx]
                )
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # Increment ideal_position
                ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)

        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("TESTING EXACT SPEC IMPLEMENTATION (NO OPTIMIZATIONS)")
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
    result, steps, history = selection_sort_exact_spec(test_array.copy())
    correct = result == expected

    print(f"\nArray:    {test_array}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")
    print(f"Correct:  {correct}")
    print(f"Steps:    {steps.total} (comparisons: {steps.comparisons}, swaps: {steps.swaps})")

    if not correct:
        print(f"ERROR: Algorithm failed!")
