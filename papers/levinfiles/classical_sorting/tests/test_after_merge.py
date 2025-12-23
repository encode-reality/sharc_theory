"""
Debug what happens after all groups merge.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.multithreaded_selection import (
    SelectionCell, SelectionGroup, GroupStatus
)
import threading
import time


def test_after_merge():
    """Test and monitor after groups merge."""
    print("After-merge test: N=3, array=[3,2,1]")
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
            phase_period=20
        )
        cells[i].group = group
        groups.append(group)

    # Start threads
    for cell in cells:
        cell.start()
    for group in groups:
        group.start()

    # Wait for groups to merge
    time.sleep(0.5)

    # Check state every 0.5 seconds
    for t in range(8):
        time.sleep(0.5)

        with lock:
            active_groups = [g for g in groups if g.status != GroupStatus.MERGED]
            values = [cells[i].value for i in range(n)]
            swaps = swaps_counter[0]

            print(f"\nt={t*0.5:.1f}s: {values}, swaps={swaps}, groups={len(active_groups)}")

            # If all in one group, show cell details
            if len(active_groups) == 1:
                for i in range(n):
                    cell = cells[i]
                    print(f"  pos{i}: Cell{cell.cell_id} (val={cell.value}, ideal={cell.ideal_position}, "
                          f"bounds=[{cell.left_boundary},{cell.right_boundary}], cooldown={cell._swap_cooldown})")

    # Stop threads
    for cell in cells:
        cell.stop()
    for group in groups:
        group.stop()

    for cell in cells:
        cell.join(timeout=1.0)
    for group in groups:
        group.join(timeout=1.0)

    with lock:
        final_values = [cells[i].value for i in range(n)]

    print(f"\nFinal: {final_values}")
    print(f"Expected: {sorted(initial_values)}")
    print(f"Swaps: {swaps_counter[0]}")


if __name__ == "__main__":
    test_after_merge()
