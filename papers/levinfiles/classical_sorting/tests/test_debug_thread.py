"""
Debug test to see what's happening in the threading.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.multithreaded_selection import (
    SelectionCell, SelectionGroup, CellStatus, GroupStatus
)
from modules.core import StepCounter
import threading
import time


def test_debug():
    """Debug test with detailed output."""
    print("Debug test: N=3, array=[3,2,1]")
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
            phase_period=5
        )
        cells[i].group = group
        groups.append(group)

    print("Initial state:")
    for i, cell in enumerate(cells):
        print(f"  Cell {i}: value={cell.value}, pos={cell.current_position[0]}, "
              f"ideal={cell.ideal_position}, bounds=[{cell.left_boundary},{cell.right_boundary}]")

    # Start threads
    print("\nStarting threads...")
    for cell in cells:
        cell.start()
    for group in groups:
        group.start()

    # Monitor
    for t in range(10):
        time.sleep(0.5)

        with lock:
            current_values = [cells[i].value for i in range(n)]
            print(f"\nt={t*0.5:.1f}s: {current_values}, swaps={swaps_counter[0]}, comps={comparisons_counter[0]}")

            active_groups = [g for g in groups if g.status != GroupStatus.MERGED]
            print(f"  Active groups: {len(active_groups)}")

            for i, cell in enumerate(cells):
                print(f"  Cell {i}: value={cell.value}, pos={cell.current_position[0]}, "
                      f"ideal={cell.ideal_position}, status={cell.status.name}, "
                      f"bounds=[{cell.left_boundary},{cell.right_boundary}]")

    # Stop threads
    print("\nStopping...")
    for cell in cells:
        cell.stop()
    for group in groups:
        group.stop()

    for cell in cells:
        cell.join(timeout=1.0)
    for group in groups:
        group.join(timeout=1.0)

    # Final state
    with lock:
        final_values = [cells[i].value for i in range(n)]

    print(f"\nFinal: {final_values}")
    print(f"Expected: {sorted(initial_values)}")
    print(f"Swaps: {swaps_counter[0]}, Comparisons: {comparisons_counter[0]}")


if __name__ == "__main__":
    test_debug()
