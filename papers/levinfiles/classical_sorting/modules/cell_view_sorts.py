"""
Cell-view (distributed, agent-based) sorting algorithms.

In these implementations, each cell is an autonomous agent that
makes decisions based on local information. This models biological
morphogenesis where cells collectively organize without a central controller.

Key differences from traditional sorts:
1. Parallel execution (simulated via random cell ordering each timestep)
2. Local decision-making (cells only see neighbors)
3. Support for frozen (damaged) cells
4. Emergent collective behavior
"""

import random
from typing import List, Tuple, Dict, Optional
from .core import Cell, StepCounter, FrozenType, Algotype, MAX_STEPS
from .metrics import sortedness


def bubble_sort(
    initial_values: List[int],
    frozen_indices: Optional[Dict[int, FrozenType]] = None,
    algotype: Algotype = "bubble"
) -> Tuple[List[int], StepCounter, List[float]]:
    """
    Cell-view bubble sort: each cell looks at neighbors and swaps accordingly.

    Rules for each cell:
    - If my value < left neighbor's value → swap left
    - Else if my value > right neighbor's value → swap right

    Args:
        initial_values: Starting array values
        frozen_indices: Dict mapping indices to FrozenType for damaged cells
        algotype: Algorithm type identifier

    Returns:
        (final_values, step_counter, sortedness_history)
    """
    frozen_indices = frozen_indices or {}

    # Create cells
    cells = [
        Cell(
            value=v,
            algotype=algotype,
            frozen_type=frozen_indices.get(i, "active")
        )
        for i, v in enumerate(initial_values)
    ]

    steps = StepCounter()
    history = []
    n = len(cells)

    # Main sorting loop
    for timestep in range(MAX_STEPS):
        # Random order of cell activation (simulates parallelism)
        idx_order = list(range(n))
        random.shuffle(idx_order)

        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]

            # Skip if cell cannot initiate movement
            if not cell.can_initiate_move():
                continue

            # Try to move left
            if idx > 0:
                neighbor_left = cells[idx - 1]
                steps.comparisons += 1

                if cell.value < neighbor_left.value and neighbor_left.can_be_moved():
                    # Swap with left neighbor
                    cells[idx], cells[idx - 1] = cells[idx - 1], cells[idx]
                    steps.swaps += 1
                    swapped_any = True
                    history.append(sortedness([c.value for c in cells]))
                    continue  # Don't check right if we swapped left

            # Try to move right
            if idx < n - 1:
                neighbor_right = cells[idx + 1]
                steps.comparisons += 1

                if cell.value > neighbor_right.value and neighbor_right.can_be_moved():
                    # Swap with right neighbor
                    cells[idx], cells[idx + 1] = cells[idx + 1], cells[idx]
                    steps.swaps += 1
                    swapped_any = True
                    history.append(sortedness([c.value for c in cells]))

        # Stop if no swaps occurred in this timestep
        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, history


def insertion_sort(
    initial_values: List[int],
    frozen_indices: Optional[Dict[int, FrozenType]] = None,
    algotype: Algotype = "insertion"
) -> Tuple[List[int], StepCounter, List[float]]:
    """
    Cell-view insertion sort: cells move left if left side is sorted and they're smaller.

    Rules for each cell:
    - Can view all cells to the left
    - Can only swap with immediate left neighbor
    - Moves left if: (1) left side is sorted AND (2) I'm smaller than left neighbor

    Args:
        initial_values: Starting array values
        frozen_indices: Dict mapping indices to FrozenType for damaged cells
        algotype: Algorithm type identifier

    Returns:
        (final_values, step_counter, sortedness_history)
    """
    frozen_indices = frozen_indices or {}

    # Create cells
    cells = [
        Cell(
            value=v,
            algotype=algotype,
            frozen_type=frozen_indices.get(i, "active")
        )
        for i, v in enumerate(initial_values)
    ]

    steps = StepCounter()
    history = []
    n = len(cells)

    # Main sorting loop
    for timestep in range(MAX_STEPS):
        # Random order of cell activation
        idx_order = list(range(n))
        random.shuffle(idx_order)

        swapped_any = False

        for idx in idx_order:
            if idx == 0:  # First cell can't move left
                continue

            cell = cells[idx]

            # Skip if cell cannot initiate movement
            if not cell.can_initiate_move():
                continue

            # Check if left side is sorted
            left_values = [c.value for c in cells[:idx]]
            left_sorted = all(
                left_values[i] <= left_values[i + 1]
                for i in range(len(left_values) - 1)
            ) if len(left_values) > 1 else True

            if not left_sorted:
                continue

            # Check if should swap with left neighbor
            neighbor_left = cells[idx - 1]
            steps.comparisons += 1

            if cell.value < neighbor_left.value and neighbor_left.can_be_moved():
                # Swap with left neighbor
                cells[idx], cells[idx - 1] = cells[idx - 1], cells[idx]
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))

        # Stop if no swaps occurred
        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, history


class _SelectionGroup:
    """
    Internal class for group merging in selection sort.
    Mimics CellGroup from reference implementation.
    """
    def __init__(self, group_id: int, left_boundary: int, right_boundary: int):
        self.group_id = group_id
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary

    def is_sorted(self, cells: List[Cell]) -> bool:
        """Check if all cells in this group are in sorted order."""
        for i in range(self.left_boundary, self.right_boundary):
            if cells[i].value > cells[i + 1].value:
                return False
        return True

    def merge_with(self, other_group: '_SelectionGroup', cells: List[Cell],
                   cell_boundaries: List[Tuple[int, int]],
                   ideal_positions: List[int]) -> None:
        """
        Merge this group with another group.
        Updates boundaries and resets ideal_positions.
        """
        self.right_boundary = other_group.right_boundary

        # Update all cells in the merged region
        for i in range(self.left_boundary, self.right_boundary + 1):
            cell_boundaries[i] = (self.left_boundary, self.right_boundary)
            ideal_positions[i] = self.left_boundary  # Reset to left boundary


def selection_sort(
    initial_values: List[int],
    frozen_indices: Optional[Dict[int, FrozenType]] = None,
    algotype: Algotype = "selection"
) -> Tuple[List[int], StepCounter, List[float]]:
    """
    Cell-view selection sort with group merging system.

    This implements the full group merging mechanism from the reference implementation:
    1. Each cell starts in its own group (trivially sorted)
    2. Groups detect when they're sorted
    3. Adjacent sorted groups merge
    4. Merging resets ideal_position to left boundary
    5. Process repeats until single group remains

    Rules for each cell:
    - Each cell has an "ideal_position" (starts at own position)
    - Cell can only move within its group boundaries
    - If cell.value < target.value → swap
    - Otherwise → increment ideal_position
    - When groups merge, ideal_position resets to group's left boundary

    Args:
        initial_values: Starting array values
        frozen_indices: Dict mapping indices to FrozenType for damaged cells
        algotype: Algorithm type identifier

    Returns:
        (final_values, step_counter, sortedness_history)
    """
    frozen_indices = frozen_indices or {}
    n = len(initial_values)

    # Create cells
    cells = [
        Cell(
            value=v,
            algotype=algotype,
            frozen_type=frozen_indices.get(i, "active")
        )
        for i, v in enumerate(initial_values)
    ]

    # Create initial groups (one per cell)
    groups = [_SelectionGroup(i, i, i) for i in range(n)]

    # Track cell boundaries and ideal positions
    cell_boundaries = [(i, i) for i in range(n)]  # (left, right) for each cell
    ideal_positions = list(range(n))  # Each starts at own position

    # Track which cell is which (for identity tracking)
    cell_ids = list(range(n))

    steps = StepCounter()
    history = []

    for timestep in range(MAX_STEPS):
        # Phase 1: Cells attempt moves
        idx_order = list(range(n))
        random.seed(42 + timestep)  # Consistent randomization
        random.shuffle(idx_order)

        cells_that_acted = set()
        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]
            cell_id = cell_ids[idx]

            # Skip if this cell already acted
            if cell_id in cells_that_acted:
                continue
            cells_that_acted.add(cell_id)

            if not cell.can_initiate_move():
                continue

            # Clamp ideal_position to cell's group boundaries
            left_bound, right_bound = cell_boundaries[idx]
            target = max(left_bound, min(right_bound, ideal_positions[idx]))

            if target == idx:
                # At ideal position, try next
                ideal_positions[idx] = min(right_bound, ideal_positions[idx] + 1)
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            # Swap if value < target
            if cell.value < neighbor.value and neighbor.can_be_moved():
                # Swap cells
                cells[idx], cells[target] = cells[target], cells[idx]
                # Swap cell IDs
                cell_ids[idx], cell_ids[target] = cell_ids[target], cell_ids[idx]
                # Swap boundaries
                cell_boundaries[idx], cell_boundaries[target] = (
                    cell_boundaries[target], cell_boundaries[idx]
                )
                # Swap ideal positions
                ideal_positions[idx], ideal_positions[target] = (
                    ideal_positions[target], ideal_positions[idx]
                )

                cells_that_acted.add(cell_ids[target])
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
                # Only one swap per timestep to avoid cycles
                break
            else:
                # Increment ideal_position
                ideal_positions[idx] = min(right_bound, ideal_positions[idx] + 1)

        # Phase 2: Merge adjacent sorted groups
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
                    current_group.merge_with(next_group, cells,
                                            cell_boundaries, ideal_positions)
                    groups.remove(next_group)
                    active_groups = [g for g in groups
                                   if g.left_boundary <= g.right_boundary]
                    merged_any = True
                    continue

            i += 1

        # Termination: fully sorted (single group)
        if (len(active_groups) == 1 and
            active_groups[0].left_boundary == 0 and
            active_groups[0].right_boundary == n - 1):
            if active_groups[0].is_sorted(cells):
                break

        # Safety: reset if all cells stuck at boundary
        if not swapped_any and not merged_any:
            is_sorted = all(cells[i].value <= cells[i + 1].value
                          for i in range(n - 1))
            if is_sorted:
                break

            # Check if all cells are stuck at right boundary
            all_at_boundary = all(
                ideal_positions[i] >= cell_boundaries[i][1]
                for i in range(n)
            )
            if all_at_boundary:
                # Reset ideal_positions to left boundaries
                for i in range(n):
                    ideal_positions[i] = cell_boundaries[i][0]

    final_values = [c.value for c in cells]
    return final_values, steps, history


def mixed_algotype_sort(
    initial_values: List[int],
    algotype_assignments: List[Algotype],
    frozen_indices: Optional[Dict[int, FrozenType]] = None,
    allow_duplicates: bool = False
) -> Tuple[List[int], StepCounter, List[float], List[List[Algotype]]]:
    """
    Chimeric array: cells follow different algorithms.

    This models biological chimeras where cells from different species
    or with different genetic programs must work together.

    Args:
        initial_values: Starting array values
        algotype_assignments: List specifying which algorithm each cell follows
        frozen_indices: Dict mapping indices to FrozenType
        allow_duplicates: Whether values can repeat

    Returns:
        (final_values, step_counter, sortedness_history, algotype_history)
    """
    frozen_indices = frozen_indices or {}
    n = len(initial_values)

    # Create cells with assigned algotypes
    cells = [
        Cell(
            value=initial_values[i],
            algotype=algotype_assignments[i],
            frozen_type=frozen_indices.get(i, "active")
        )
        for i in range(n)
    ]

    steps = StepCounter()
    sortedness_history = []
    algotype_history = []  # Track algotype positions over time

    # Selection sort cells need ideal positions
    ideal_positions = [0 for _ in range(n)]

    # Main sorting loop
    for timestep in range(MAX_STEPS):
        # Record current algotype configuration
        algotype_history.append([c.algotype for c in cells])

        # Random order of cell activation
        idx_order = list(range(n))
        random.shuffle(idx_order)

        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]

            if not cell.can_initiate_move():
                continue

            # Apply rules based on this cell's algotype
            if cell.algotype == "bubble":
                # Bubble sort rules
                moved = False

                # Try left
                if idx > 0:
                    neighbor_left = cells[idx - 1]
                    steps.comparisons += 1
                    if cell.value < neighbor_left.value and neighbor_left.can_be_moved():
                        cells[idx], cells[idx - 1] = cells[idx - 1], cells[idx]
                        ideal_positions[idx], ideal_positions[idx - 1] = ideal_positions[idx - 1], ideal_positions[idx]
                        steps.swaps += 1
                        swapped_any = True
                        moved = True

                # Try right if didn't move left
                if not moved and idx < n - 1:
                    neighbor_right = cells[idx + 1]
                    steps.comparisons += 1
                    if cell.value > neighbor_right.value and neighbor_right.can_be_moved():
                        cells[idx], cells[idx + 1] = cells[idx + 1], cells[idx]
                        ideal_positions[idx], ideal_positions[idx + 1] = ideal_positions[idx + 1], ideal_positions[idx]
                        steps.swaps += 1
                        swapped_any = True

            elif cell.algotype == "insertion":
                # Insertion sort rules
                if idx > 0:
                    left_values = [c.value for c in cells[:idx]]
                    left_sorted = all(
                        left_values[i] <= left_values[i + 1]
                        for i in range(len(left_values) - 1)
                    ) if len(left_values) > 1 else True

                    if left_sorted:
                        neighbor_left = cells[idx - 1]
                        steps.comparisons += 1
                        if cell.value < neighbor_left.value and neighbor_left.can_be_moved():
                            cells[idx], cells[idx - 1] = cells[idx - 1], cells[idx]
                            ideal_positions[idx], ideal_positions[idx - 1] = ideal_positions[idx - 1], ideal_positions[idx]
                            steps.swaps += 1
                            swapped_any = True

            elif cell.algotype == "selection":
                # Selection sort rules
                target = max(0, min(n - 1, ideal_positions[idx]))

                # Skip if target is self
                if target == idx:
                    ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)
                    continue

                neighbor = cells[target]
                steps.comparisons += 1

                if cell.value < neighbor.value and neighbor.can_be_moved():
                    cells[idx], cells[target] = cells[target], cells[idx]
                    ideal_positions[idx], ideal_positions[target] = ideal_positions[target], ideal_positions[idx]
                    steps.swaps += 1
                    swapped_any = True
                else:
                    ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)

        # Record sortedness after this timestep
        if swapped_any:
            sortedness_history.append(sortedness([c.value for c in cells]))

        # Stop if no swaps occurred
        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, sortedness_history, algotype_history
