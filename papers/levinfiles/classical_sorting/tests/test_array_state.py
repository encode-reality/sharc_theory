"""
Check actual array state after swaps.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.multithreaded_selection import (
    SelectionCell, SelectionGroup
)
import threading
import time


def test_array():
    """Check array state."""
    print("Array state test: N=3, array=[3,2,1]")
    print("="*70)

    # Setup
    n = 3
    initial_values = [3, 2, 1]
    lock = threading.Lock()
    swaps_counter = [0]
    comparisons_counter = [0]
    cells = []

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
            frozen_type="active"
        )
        cells.append(cell)

    print("Initial state:")
    for i in range(n):
        cell = cells[i]
        print(f"  cells[{i}] = Cell {cell.cell_id} (value={cell.value}, pos={cell.current_position[0]})")

    # Create groups
    groups = []
    for i in range(n):
        group = SelectionGroup(
            group_id=i,
            left_boundary=[i],
            right_boundary=[i],
            cells_in_group=[cells[i]],
            global_cells=cells,
            lock=lock,
            phase_period=20
        )
        cells[i].group = group
        groups.append(group)

    # Start threads
    for cell in cells:
        cell.start()
    for group in groups:
        group.start()

    # Run for 1 second
    time.sleep(1.0)

    # Check state
    with lock:
        print(f"\nAfter 1 second (swaps={swaps_counter[0]}):")
        for i in range(n):
            cell = cells[i]
            print(f"  cells[{i}] = Cell {cell.cell_id} (value={cell.value}, pos={cell.current_position[0]}, "
                  f"ideal={cell.ideal_position}, bounds=[{cell.left_boundary},{cell.right_boundary}], "
                  f"cooldown={cell._swap_cooldown})")

        # Get values by position
        values = [cells[i].value for i in range(n)]
        print(f"\nArray by position: {values}")

    # Stop threads
    for cell in cells:
        cell.stop()
    for group in groups:
        group.stop()

    for cell in cells:
        cell.join(timeout=1.0)
    for group in groups:
        group.join(timeout=1.0)


if __name__ == "__main__":
    test_array()
