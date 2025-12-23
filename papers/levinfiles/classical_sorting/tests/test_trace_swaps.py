"""
Trace swap attempts in detail.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.multithreaded_selection import (
    SelectionCell, SelectionGroup, CellStatus, GroupStatus
)
import threading
import time


# Monkey-patch to add logging
original_swap = SelectionCell.swap

def logged_swap(self, target_pos):
    print(f"  [SWAP ATTEMPT] Cell {self.cell_id} (value={self.value}, pos={self.current_position[0]}) "
          f"-> target_pos={target_pos}")
    result = original_swap(self, target_pos)
    print(f"  [SWAP RESULT] Cell {self.cell_id} now at pos={self.current_position[0]}")
    return result

SelectionCell.swap = logged_swap

original_should_move = SelectionCell.should_move_to

def logged_should_move(self, target_pos):
    result = original_should_move(self, target_pos)
    if result:
        print(f"  [SHOULD_MOVE] Cell {self.cell_id} (value={self.value}, pos={self.current_position[0]}, "
              f"ideal={self.ideal_position}) should move to {target_pos}")
    return result

SelectionCell.should_move_to = logged_should_move


def test_trace():
    """Test with tracing."""
    print("Trace test: N=3, array=[3,2,1]")
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

    print("Starting threads...")
    for cell in cells:
        cell.start()
    for group in groups:
        group.start()

    # Run for 2 seconds
    time.sleep(2.0)

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
    print(f"Swaps: {swaps_counter[0]}, Comparisons: {comparisons_counter[0]}")


if __name__ == "__main__":
    test_trace()
