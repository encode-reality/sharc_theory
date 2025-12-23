"""
Selection Sort with Group-Based Reset Mechanism

Based on insights from reference implementation:
- Each cell starts in its own group (boundaries = [i, i])
- When a group is sorted, cells' ideal_position resets
- Adjacent sorted groups merge, expanding boundaries
- Reset allows cells to find their position in the expanded region

This mimics the reference implementation's group merging without full threading.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


def is_region_sorted(cells, left, right):
    """Check if cells in range [left, right] are sorted."""
    for i in range(left, right):
        if cells[i].value > cells[i + 1].value:
            return False
    return True


def selection_sort_with_groups(initial_values):
    """
    Selection sort with group-based reset mechanism.

    Key behaviors from reference implementation:
    1. Each cell has ideal_position (search position)
    2. ideal_position increments when cell.value >= target.value
    3. Swap occurs when cell.value < target.value
    4. When a group becomes sorted, update() resets ideal_position
    5. Adjacent sorted groups merge
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

    # Track groups: each cell starts in its own group
    # groups[i] = (left_boundary, right_boundary) for cell i
    groups = {i: (i, i) for i in range(n)}

    steps = StepCounter()
    history = []

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

            # Get cell's group boundaries
            left_boundary, right_boundary = groups[idx]

            # Clamp ideal_position to boundaries
            target = max(left_boundary, min(right_boundary, ideal_positions[idx]))

            # Skip if target is self
            if target == idx:
                ideal_positions[idx] = min(right_boundary, ideal_positions[idx] + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            # Reference implementation logic: swap if value < target.value
            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells
                cells[idx], cells[target] = cells[target], cells[idx]
                # Swap ideal_positions too (cells carry their state)
                ideal_positions[idx], ideal_positions[target] = (
                    ideal_positions[target],
                    ideal_positions[idx]
                )
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # value >= target.value, increment ideal_position
                ideal_positions[idx] = min(right_boundary, ideal_positions[idx] + 1)

        # After each timestep, check for sorted groups and merge them
        # This mimics the group merging behavior in the reference implementation
        merged_any = False

        # Find all sorted groups and try to merge adjacent ones
        sorted_groups = []
        i = 0
        while i < n:
            left = i
            # Find extent of sorted region starting at i
            while i < n - 1 and cells[i].value <= cells[i + 1].value:
                i += 1
            right = i
            sorted_groups.append((left, right))
            i += 1

        # Merge adjacent groups and reset ideal_positions (mimics update())
        for left, right in sorted_groups:
            if right - left > 0:  # Group has more than one element
                # This group is sorted - reset all cells' ideal_positions
                # This is equivalent to calling update() in the reference implementation
                for i in range(left, right + 1):
                    # Update group boundaries for all cells in the merged region
                    groups[i] = (left, right)
                    # Reset ideal_position to left boundary (mimics update())
                    ideal_positions[i] = left
                    merged_any = True

        # Termination: no swaps and no merges (fully sorted)
        if not swapped_any and not merged_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("TESTING: SELECTION SORT WITH GROUP-BASED RESET")
print("=" * 70)
print("\nBased on reference implementation insight:")
print("- Groups start as single cells")
print("- Sorted groups detected and cells' ideal_position reset")
print("- Adjacent sorted groups merge, expanding boundaries")
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
    result, steps, history = selection_sort_with_groups(test_array.copy())
    correct = result == expected

    print(f"Array:    {test_array}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")
    print(f"Correct:  {correct}")
    print(f"Steps:    {steps.total} (comparisons: {steps.comparisons}, swaps: {steps.swaps})")

    if correct:
        print("  ✓ SUCCESS!")
    else:
        print("  ✗ FAILED")
    print()

print("=" * 70)
