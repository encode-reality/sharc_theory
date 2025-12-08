"""
Selection Sort with Full Group Merging System

Implements the complete group merging mechanism from the reference implementation:
1. Each cell starts in its own group (trivially sorted)
2. Groups detect when they're sorted
3. Adjacent sorted groups merge
4. Merging triggers update() which resets ideal_position
5. Process repeats until single group remains
"""

import random
from modules.core import Cell, StepCounter, MAX_STEPS
from modules.metrics import sortedness


class Group:
    """
    Represents a group of cells with shared boundaries.
    Mimics CellGroup from reference implementation.
    """
    def __init__(self, group_id, left_boundary, right_boundary):
        self.group_id = group_id
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.cells = []  # Will be populated with cell references

    def is_sorted(self, cells_array):
        """Check if all cells in this group are in sorted order."""
        for i in range(self.left_boundary, self.right_boundary):
            if cells_array[i].value > cells_array[i + 1].value:
                return False
        return True

    def merge_with(self, other_group, cells_array):
        """
        Merge this group with another group.
        Updates boundaries and calls update() on all cells.

        Mimics CellGroup.merge_with_group() from reference.
        """
        # Expand boundaries to encompass both groups
        self.right_boundary = other_group.right_boundary

        # Update all cells in the merged region
        for i in range(self.left_boundary, self.right_boundary + 1):
            cell = cells_array[i]
            cell.group = self
            cell.left_boundary = self.left_boundary
            cell.right_boundary = self.right_boundary
            cell.update()  # Key: reset ideal_position!

        return self


class SelectionCell:
    """
    Cell with ideal_position that resets when groups merge.
    Mimics SelectionSortCell from reference implementation.
    """
    def __init__(self, value, cell_id, initial_position):
        self.value = value
        self.cell_id = cell_id
        self.group = None  # Will be set to a Group
        self.left_boundary = initial_position
        self.right_boundary = initial_position
        self.ideal_position = initial_position  # Start at own position

    def update(self):
        """
        Reset ideal_position to left_boundary.
        Called when groups merge (mimics SelectionSortCell.update()).
        """
        self.ideal_position = self.left_boundary

    def can_initiate_move(self):
        return True

    def can_be_moved(self):
        return True


def selection_sort_with_groups(initial_values):
    """
    Complete selection sort with group merging system.
    """
    n = len(initial_values)

    # Create cells
    cells = [SelectionCell(v, i, i) for i, v in enumerate(initial_values)]

    # Create initial groups (one per cell)
    groups = [Group(i, i, i) for i in range(n)]

    # Assign each cell to its group
    for i in range(n):
        cells[i].group = groups[i]
        groups[i].cells.append(cells[i])

    steps = StepCounter()
    history = []

    for timestep in range(MAX_STEPS):
        # Phase 1: Cells attempt moves
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

            if not cell.can_initiate_move():
                continue

            # Clamp ideal_position to cell's group boundaries
            target = max(cell.left_boundary,
                        min(cell.right_boundary, cell.ideal_position))

            if target == idx:
                # At ideal position, try next
                cell.ideal_position = min(cell.right_boundary,
                                         cell.ideal_position + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            # Reference logic: swap if value < target
            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells
                cells[idx], cells[target] = cells[target], cells[idx]
                cells_that_acted.add(neighbor.cell_id)
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
                # Only one swap per timestep to avoid cycles
                break
            else:
                # value >= target, increment ideal_position
                cell.ideal_position = min(cell.right_boundary,
                                         cell.ideal_position + 1)

        # Phase 2: Merge adjacent sorted groups
        # Check all groups from left to right
        merged_any = False
        i = 0
        active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]

        while i < len(active_groups) - 1:
            current_group = active_groups[i]
            next_group = active_groups[i + 1]

            # Check if groups are adjacent
            if current_group.right_boundary + 1 == next_group.left_boundary:
                # Check if both are sorted
                if current_group.is_sorted(cells) and next_group.is_sorted(cells):
                    # Merge them!
                    current_group.merge_with(next_group, cells)

                    # Remove the merged group from active list
                    groups.remove(next_group)
                    active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]

                    merged_any = True
                    # Don't increment i, check if newly merged group can merge with next
                    continue

            i += 1

        # Termination: fully sorted (single group)
        if len(active_groups) == 1 and active_groups[0].left_boundary == 0 and active_groups[0].right_boundary == n - 1:
            if active_groups[0].is_sorted(cells):
                break

        # Safety: no progress for multiple timesteps
        if not swapped_any and not merged_any:
            # Check if fully sorted
            is_sorted = all(cells[i].value <= cells[i + 1].value for i in range(n - 1))
            if is_sorted:
                break

            # Check if all cells are stuck at right boundary
            # If so, reset them to left boundary (simulates new merge cycle)
            all_at_boundary = all(
                cell.ideal_position >= cell.right_boundary for cell in cells
            )
            if all_at_boundary:
                for cell in cells:
                    cell.ideal_position = cell.left_boundary

    final_values = [c.value for c in cells]
    return final_values, steps, history


# Test
print("=" * 70)
print("SELECTION SORT - FULL GROUP MERGING SYSTEM")
print("=" * 70)
print("\nImplements complete group merging from reference:")
print("- Each cell starts in own group")
print("- Sorted groups merge with adjacent sorted groups")
print("- Merging calls update() to reset ideal_position")
print()

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
    result, steps, history = selection_sort_with_groups(test_array.copy())
    correct = result == expected

    print(f"Array:    {test_array}")
    print(f"Result:   {result}")
    print(f"Expected: {expected}")
    print(f"Correct:  {'YES' if correct else 'NO'}")
    print(f"Steps:    {steps.total} (comparisons: {steps.comparisons}, swaps: {steps.swaps})")

    if not correct:
        all_success = False
    print()

print("=" * 70)
if all_success:
    print("ALL TESTS PASSED!")
    print("Selection Sort with group merging is working!")
else:
    print("Some tests failed - debugging needed")
print("=" * 70)
