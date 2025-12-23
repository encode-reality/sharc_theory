"""
Test two different approaches to cell-view selection sort:
1. GitHub approach: ideal_position is a cell property (doesn't swap with cells)
2. Spec approach: ideal_positions is an array (swaps with cells)
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness

def selection_sort_github_approach(initial_values):
    """
    GitHub implementation approach:
    - Each cell object has its own ideal_position property
    - When cells swap, ideal_position values DON'T swap
    - ideal_position travels with the cell object
    """
    n = len(initial_values)

    # Create cells with ideal_position as a property
    class CellWithIdealPos:
        def __init__(self, value):
            self.value = value
            self.ideal_position = 0  # Starts at left boundary
            self.algotype = "selection"
            self.frozen_type = "active"

        def can_initiate_move(self):
            return True

        def can_be_moved(self):
            return True

    cells = [CellWithIdealPos(v) for v in initial_values]
    steps = StepCounter()
    history = []

    for timestep in range(MAX_STEPS):
        idx_order = list(range(n))
        random.seed(42 + timestep)  # Reproducible for comparison
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
                # SWAP CELLS BUT NOT IDEAL_POSITIONS
                cells[idx], cells[target] = cells[target], cells[idx]
                # Note: ideal_position travels with the cell object
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # Increment ideal_position
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, history


def selection_sort_spec_approach(initial_values):
    """
    Spec implementation approach:
    - ideal_positions is an array indexed by position
    - When cells swap, ideal_positions also swap
    - ideal_position is tied to the position, not the cell
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
    ideal_positions = [0 for _ in range(n)]  # Array indexed by position
    steps = StepCounter()
    history = []

    for timestep in range(MAX_STEPS):
        idx_order = list(range(n))
        random.seed(42 + timestep)  # Same seed for fair comparison
        random.shuffle(idx_order)

        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]
            if not cell.can_initiate_move():
                continue

            target = max(0, min(n - 1, ideal_positions[idx]))

            # Skip if target is self
            if target == idx:
                ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            if cell.value < neighbor.value and neighbor.can_be_moved():
                # SWAP CELLS AND IDEAL_POSITIONS
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


# Run comparison tests
print("=" * 70)
print("COMPARING TWO SELECTION SORT APPROACHES")
print("=" * 70)

test_arrays = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [5, 2, 8, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
]

for test_array in test_arrays:
    expected = sorted(test_array)

    print(f"\nTest array: {test_array}")
    print(f"Expected:   {expected}")
    print("-" * 70)

    # Test GitHub approach
    result_github, steps_github, history_github = selection_sort_github_approach(test_array.copy())
    github_correct = result_github == expected
    print(f"GitHub approach:  {result_github}")
    print(f"  Correct: {github_correct}")
    print(f"  Steps: {steps_github.total} (comparisons: {steps_github.comparisons}, swaps: {steps_github.swaps})")

    # Test Spec approach
    result_spec, steps_spec, history_spec = selection_sort_spec_approach(test_array.copy())
    spec_correct = result_spec == expected
    print(f"Spec approach:    {result_spec}")
    print(f"  Correct: {spec_correct}")
    print(f"  Steps: {steps_spec.total} (comparisons: {steps_spec.comparisons}, swaps: {steps_spec.swaps})")

    if github_correct and not spec_correct:
        print("  >>> GitHub approach WORKS, Spec approach FAILS")
    elif spec_correct and not github_correct:
        print("  >>> Spec approach WORKS, GitHub approach FAILS")
    elif not github_correct and not spec_correct:
        print("  >>> BOTH APPROACHES FAIL")
    else:
        print("  >>> Both approaches work")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
