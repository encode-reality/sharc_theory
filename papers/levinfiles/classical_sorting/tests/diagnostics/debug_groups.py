import sys
from pathlib import Path
# Add grandparent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
"""Debug group merging to understand behavior"""

import random
from modules.core import StepCounter

class Group:
    def __init__(self, group_id, left_boundary, right_boundary):
        self.group_id = group_id
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary

    def is_sorted(self, cells_array):
        for i in range(self.left_boundary, self.right_boundary):
            if cells_array[i].value > cells_array[i + 1].value:
                return False
        return True

    def merge_with(self, other_group, cells_array):
        self.right_boundary = other_group.right_boundary
        for i in range(self.left_boundary, self.right_boundary + 1):
            cell = cells_array[i]
            cell.group = self
            cell.left_boundary = self.left_boundary
            cell.right_boundary = self.right_boundary
            cell.update()
        return self


class SelectionCell:
    def __init__(self, value, cell_id, initial_position):
        self.value = value
        self.cell_id = cell_id
        self.group = None
        self.left_boundary = initial_position
        self.right_boundary = initial_position
        self.ideal_position = initial_position

    def update(self):
        self.ideal_position = self.left_boundary

    def can_initiate_move(self):
        return True

    def can_be_moved(self):
        return True


def debug_groups(initial_values, max_timesteps=10):
    n = len(initial_values)
    cells = [SelectionCell(v, i, i) for i, v in enumerate(initial_values)]
    groups = [Group(i, i, i) for i in range(n)]
    
    for i in range(n):
        cells[i].group = groups[i]

    print(f"Initial: {[c.value for c in cells]}")
    print(f"Groups: {[(g.group_id, g.left_boundary, g.right_boundary) for g in groups]}\n")

    for timestep in range(max_timesteps):
        print(f"--- Timestep {timestep} ---")
        
        # Phase 1: Try moves
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
            
            target = max(cell.left_boundary, min(cell.right_boundary, cell.ideal_position))
            
            if target == idx:
                cell.ideal_position = min(cell.right_boundary, cell.ideal_position + 1)
                continue
            
            neighbor = cells[target]
            
            if cell.value < neighbor.value:
                print(f"  Swap: pos {idx} (v={cell.value}) <-> pos {target} (v={neighbor.value})")
                cells[idx], cells[target] = cells[target], cells[idx]
                cells_that_acted.add(neighbor.cell_id)
                swapped_any = True
            else:
                cell.ideal_position = min(cell.right_boundary, cell.ideal_position + 1)
        
        print(f"  After moves: {[c.value for c in cells]}")
        
        # Phase 2: Try merges
        merged_any = False
        i = 0
        active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
        
        print(f"  Active groups: {[(g.group_id, g.left_boundary, g.right_boundary) for g in active_groups]}")
        
        while i < len(active_groups) - 1:
            current_group = active_groups[i]
            next_group = active_groups[i + 1]
            
            print(f"  Checking merge: Group {current_group.group_id} [{current_group.left_boundary}-{current_group.right_boundary}] with Group {next_group.group_id} [{next_group.left_boundary}-{next_group.right_boundary}]")
            
            if current_group.right_boundary + 1 == next_group.left_boundary:
                is_current_sorted = current_group.is_sorted(cells)
                is_next_sorted = next_group.is_sorted(cells)
                print(f"    Adjacent! Current sorted: {is_current_sorted}, Next sorted: {is_next_sorted}")
                
                if is_current_sorted and is_next_sorted:
                    print(f"    MERGING!")
                    current_group.merge_with(next_group, cells)
                    groups.remove(next_group)
                    active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
                    merged_any = True
                    continue
            
            i += 1
        
        print(f"  Swapped: {swapped_any}, Merged: {merged_any}")
        print(f"  Final groups: {[(g.group_id, g.left_boundary, g.right_boundary) for g in groups]}")
        print()

# Test
debug_groups([3, 2, 1])
