"""
Modern multithreaded Selection Sort implementation.

This is a Python 3.12 reimplementation of the authors' multithreaded approach,
using modern patterns while maintaining functional equivalence.

Key improvements over reference implementation:
- dataclasses for clean data structures
- Context managers for lock handling
- Type hints throughout
- threading.Event for signaling
- Modern thread management patterns
"""

from __future__ import annotations
from enum import Enum, auto
from typing import List, Dict, Optional, Tuple
import threading
import time
from .core import StepCounter, FrozenType


class CellStatus(Enum):
    """Status of a cell in the sorting process."""
    ACTIVE = auto()      # Cell can move
    SLEEP = auto()       # Cell is sleeping (group in SLEEP phase)
    MOVING = auto()      # Cell is currently swapping
    FREEZE = auto()      # Cell is frozen (damaged)
    INACTIVE = auto()    # Cell has stopped (sorting complete)


class GroupStatus(Enum):
    """Status of a group in the sorting process."""
    ACTIVE = auto()      # Group is actively sorting
    SLEEP = auto()       # Group is sleeping (pacing mechanism)
    MERGED = auto()      # Group has been merged into another


class SelectionCell(threading.Thread):
    """
    A cell that sorts using selection sort logic.

    Each cell runs in its own thread and continuously attempts to move
    to its ideal position within its group boundaries.
    """

    def __init__(
        self,
        value: int,
        cell_id: int,
        initial_position: int,
        cells: List['SelectionCell'],
        lock: threading.Lock,
        swaps_counter: List[int],
        comparisons_counter: List[int],
        frozen_type: FrozenType = "active"
    ):
        """Initialize cell with threading support."""
        threading.Thread.__init__(self)
        self.daemon = True  # Thread dies when main thread exits

        # Core attributes
        self.value = value
        self.cell_id = cell_id
        self.initial_position = initial_position
        self.cells = cells
        self.lock = lock
        self.swaps_counter = swaps_counter
        self.comparisons_counter = comparisons_counter
        self.frozen_type = frozen_type

        # Position tracking
        self.left_boundary = initial_position
        self.right_boundary = initial_position
        self.ideal_position = initial_position
        self.current_position = [initial_position]  # Mutable reference

        # State
        if frozen_type == "active":
            self.status = CellStatus.ACTIVE
        elif frozen_type in ("movable", "immovable"):
            self.status = CellStatus.FREEZE
        else:
            self.status = CellStatus.ACTIVE

        self.group: Optional['SelectionGroup'] = None
        self._stop_event = threading.Event()
        self._swap_cooldown = 0  # Cooldown counter after swapping

    def update(self) -> None:
        """Reset ideal_position when groups merge."""
        self.ideal_position = self.left_boundary

    def can_initiate_move(self) -> bool:
        """Check if this cell can initiate a swap."""
        return self.frozen_type == "active" and self.status != CellStatus.FREEZE

    def can_be_moved(self) -> bool:
        """Check if this cell can be moved by another cell."""
        return self.frozen_type in ("active", "movable")

    def should_move_to(self, target_pos: int) -> bool:
        """
        Check if should move to target position.

        Returns True if should swap, False if should increment ideal_position.
        """
        if not self.can_initiate_move():
            return False

        # Clamp target to boundaries
        target_pos = max(self.left_boundary, min(self.right_boundary, target_pos))

        # If target is self, increment ideal_position
        if target_pos == self.current_position[0]:
            if self.ideal_position >= self.right_boundary:
                # Reset to left to make another pass
                self.ideal_position = self.left_boundary
            else:
                self.ideal_position = min(self.right_boundary, self.ideal_position + 1)
            return False

        # Get target cell
        target_cell = self.cells[target_pos]

        # Increment comparison counter (quick operation, lock briefly)
        if self.lock.acquire(timeout=0.01):
            try:
                self.comparisons_counter[0] += 1
            finally:
                self.lock.release()

        # Check if should swap
        # Selection sort: only swap if (1) my value is smaller AND (2) swapping moves me LEFT
        if (self.value < target_cell.value and
            target_cell.can_be_moved() and
            target_pos < self.current_position[0]):  # Only move LEFT
            return True
        else:
            # Increment ideal_position, reset if at boundary
            if self.ideal_position >= self.right_boundary:
                self.ideal_position = self.left_boundary
            else:
                self.ideal_position = min(self.right_boundary, self.ideal_position + 1)
            return False

    def swap(self, target_pos: int) -> None:
        """
        Perform thread-safe swap with target position.

        This is the critical section that requires lock protection.
        """
        # Try to acquire lock with timeout
        if not self.lock.acquire(timeout=0.1):
            return

        try:
            # Check if we should still be running
            if self._stop_event.is_set():
                return

            target_cell = self.cells[target_pos]

            # Skip if cells are in wrong state
            if (self.status == CellStatus.FREEZE or
                target_cell.status == CellStatus.FREEZE or
                not target_cell.can_be_moved()):
                return

            # Set both to MOVING
            old_self_status = self.status
            old_target_status = target_cell.status
            self.status = CellStatus.MOVING
            target_cell.status = CellStatus.MOVING

            # Perform swap in cells array
            self.cells[self.current_position[0]] = target_cell
            self.cells[target_pos] = self

            # Update positions
            target_cell.current_position[0] = self.current_position[0]
            self.current_position[0] = target_pos

            # Reset ideal_position to current position to prevent immediate re-swap
            # This makes the cell start checking from its new position
            self.ideal_position = self.current_position[0]
            target_cell.ideal_position = target_cell.current_position[0]

            # Set cooldown to prevent immediate re-swapping
            self._swap_cooldown = 2
            target_cell._swap_cooldown = 2

            # Increment swap counter
            self.swaps_counter[0] += 1

            # Restore status (or set to ACTIVE if was SLEEP)
            self.status = CellStatus.ACTIVE if old_self_status == CellStatus.SLEEP else old_self_status
            target_cell.status = CellStatus.ACTIVE if old_target_status == CellStatus.SLEEP else old_target_status
        finally:
            self.lock.release()

    def move(self) -> None:
        """
        Attempt to move to ideal position.

        This is called repeatedly in the run() loop.
        """
        # Cells can move regardless of group phase
        # The SLEEP phase only affects group merging, not cell movement

        # Check cooldown - if we just swapped, wait before moving again
        if self._swap_cooldown > 0:
            self._swap_cooldown -= 1
            return

        # Check if should move
        if self.should_move_to(self.ideal_position):
            self.swap(self.ideal_position)

    def stop(self) -> None:
        """Signal the thread to stop."""
        self._stop_event.set()
        self.status = CellStatus.INACTIVE

    def run(self) -> None:
        """
        Main thread loop.

        Continuously attempts to move until stopped.
        """
        while not self._stop_event.is_set() and self.status != CellStatus.INACTIVE:
            self.move()
            time.sleep(0.001)  # Small delay to prevent CPU spinning


class SelectionGroup(threading.Thread):
    """
    A group of cells that manages merging with adjacent groups.

    Groups monitor their cells and merge with adjacent sorted groups.
    """

    def __init__(
        self,
        group_id: int,
        left_boundary: List[int],
        right_boundary: List[int],
        cells_in_group: List[SelectionCell],
        global_cells: List[SelectionCell],
        lock: threading.Lock,
        phase_period: int = 10
    ):
        """Initialize group with threading support."""
        threading.Thread.__init__(self)
        self.daemon = True

        # Core attributes
        self.group_id = group_id
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.cells_in_group = cells_in_group
        self.global_cells = global_cells
        self.lock = lock
        self.phase_period = phase_period

        # State
        self.status = GroupStatus.ACTIVE
        self.count_down = phase_period
        self._stop_event = threading.Event()

    def is_sorted(self) -> bool:
        """Check if all cells in this group are sorted."""
        left = self.left_boundary[0]
        right = self.right_boundary[0]

        if left >= right:
            return True

        prev_cell = self.global_cells[left]
        for i in range(left, right + 1):
            cell = self.global_cells[i]

            # Can't be sorted if cells are sleeping or moving
            if cell.status in (CellStatus.SLEEP, CellStatus.MOVING):
                return False

            # Check ordering
            if cell.value < prev_cell.value:
                return False

            prev_cell = cell

        return True

    def find_next_group(self) -> Optional[SelectionGroup]:
        """Find the adjacent group to the right."""
        # Look for a cell just to the right of our boundary
        next_pos = self.right_boundary[0] + 1
        if next_pos < len(self.global_cells):
            next_cell = self.global_cells[next_pos]
            return next_cell.group
        return None

    def merge_with(self, other_group: 'SelectionGroup') -> None:
        """
        Merge with another group.

        Updates boundaries and calls update() on all cells.
        """
        # Lock should already be held by caller
        # Mark other group as merged
        other_group.status = GroupStatus.MERGED
        other_group._stop_event.set()

        # Expand boundaries
        self.right_boundary[0] = other_group.right_boundary[0]

        # Add other group's cells
        self.cells_in_group.extend(other_group.cells_in_group)

        # Update all cells in merged region
        for cell in self.cells_in_group:
            cell.group = self
            cell.left_boundary = self.left_boundary[0]
            cell.right_boundary = self.right_boundary[0]
            cell.update()  # Reset ideal_position

        # Reset count_down and set to ACTIVE to give cells time to sort
        self.status = GroupStatus.ACTIVE
        self.count_down = self.phase_period

    def put_cells_to_sleep(self) -> None:
        """Put all cells in this group to sleep."""
        for cell in self.cells_in_group:
            if cell.status != CellStatus.FREEZE:
                cell.status = CellStatus.SLEEP

    def awake_cells(self) -> None:
        """Wake up all cells in this group."""
        for cell in self.cells_in_group:
            if cell.status == CellStatus.SLEEP:
                cell.status = CellStatus.ACTIVE

    def change_status(self) -> None:
        """Toggle between ACTIVE and SLEEP phases."""
        self.count_down = self.phase_period

        if self.status == GroupStatus.ACTIVE:
            self.status = GroupStatus.SLEEP
            # Cells continue to move during SLEEP
        elif self.status == GroupStatus.SLEEP:
            self.status = GroupStatus.ACTIVE

    def all_cells_inactive(self) -> bool:
        """Check if all cells are inactive."""
        return all(cell.status == CellStatus.INACTIVE for cell in self.cells_in_group)

    def stop(self) -> None:
        """Signal the thread to stop."""
        self._stop_event.set()

    def run(self) -> None:
        """
        Main thread loop.

        Monitors for merge opportunities and manages phase changes.
        """
        while not self._stop_event.is_set() and self.status != GroupStatus.MERGED:
            # Check for phase change
            if self.count_down <= 0:
                self.change_status()

            # Handle SLEEP phase
            if self.status == GroupStatus.SLEEP:
                self.put_cells_to_sleep()
                self.count_down -= 1
                time.sleep(0.05)
                continue

            # Handle ACTIVE phase - check for merges
            if self.status == GroupStatus.ACTIVE:
                # Try to acquire lock with timeout
                if self.lock.acquire(timeout=0.1):
                    try:
                        # Check if we should still be running
                        if self._stop_event.is_set():
                            break

                        if self.is_sorted():
                            next_group = self.find_next_group()
                            if (next_group and
                                next_group.status == GroupStatus.ACTIVE and
                                next_group.is_sorted()):
                                self.merge_with(next_group)
                    finally:
                        self.lock.release()

                self.count_down -= 1
                time.sleep(0.05)


def selection_sort_threaded(
    initial_values: List[int],
    frozen_indices: Optional[Dict[int, FrozenType]] = None,
    max_time: float = 30.0  # Maximum time in seconds
) -> Tuple[List[int], StepCounter, List[float]]:
    """
    Modern multithreaded selection sort.

    Args:
        initial_values: Starting array values
        frozen_indices: Dict mapping indices to FrozenType for damaged cells
        max_time: Maximum time to run in seconds

    Returns:
        (final_values, step_counter, sortedness_history)
    """
    frozen_indices = frozen_indices or {}
    n = len(initial_values)

    # Shared state
    lock = threading.Lock()
    swaps_counter = [0]
    comparisons_counter = [0]
    cells: List[SelectionCell] = []

    # Create cells
    for i, value in enumerate(initial_values):
        cell = SelectionCell(
            value=value,
            cell_id=i,
            initial_position=i,
            cells=cells,
            lock=lock,
            swaps_counter=swaps_counter,
            comparisons_counter=comparisons_counter,
            frozen_type=frozen_indices.get(i, "active")
        )
        cells.append(cell)

    # Create groups (one per cell initially)
    groups: List[SelectionGroup] = []
    for i in range(n):
        group = SelectionGroup(
            group_id=i,
            left_boundary=[i],
            right_boundary=[i],
            cells_in_group=[cells[i]],
            global_cells=cells,
            lock=lock,
            phase_period=20  # Give cells more time to sort before sleeping
        )
        cells[i].group = group
        groups.append(group)

    # Start all threads
    for cell in cells:
        cell.start()

    for group in groups:
        group.start()

    # Monitor for completion
    start_time = time.time()
    history = []

    while time.time() - start_time < max_time:
        # Check if done (single active group spanning entire array)
        active_groups = [g for g in groups if g.status != GroupStatus.MERGED]

        if len(active_groups) == 1:
            group = active_groups[0]
            if (group.left_boundary[0] == 0 and
                group.right_boundary[0] == n - 1 and
                group.is_sorted()):
                break

        # Record sortedness
        if lock.acquire(timeout=0.1):
            try:
                current_values = [cells[i].value for i in range(n)]

                # Calculate sortedness
                sorted_count = sum(1 for i in range(n-1) if current_values[i] <= current_values[i+1])
                sorted_count += 1  # Last element is always "sorted"
                sortedness_pct = (sorted_count / n) * 100
                history.append(sortedness_pct)
            finally:
                lock.release()

        time.sleep(0.1)

    # Stop all threads
    for cell in cells:
        cell.stop()

    for group in groups:
        group.stop()

    # Wait for threads to finish (with timeout)
    for cell in cells:
        cell.join(timeout=1.0)

    for group in groups:
        group.join(timeout=1.0)

    # Get final values
    if lock.acquire(timeout=1.0):
        try:
            final_values = [cells[i].value for i in range(n)]
        finally:
            lock.release()
    else:
        # If can't get lock, just read without it
        final_values = [cells[i].value for i in range(n)]

    # Create step counter
    steps = StepCounter()
    steps.swaps = swaps_counter[0]
    steps.comparisons = comparisons_counter[0]

    return final_values, steps, history
