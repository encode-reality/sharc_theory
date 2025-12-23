"""
Detailed group debugging - see why groups won't merge.
"""

import sys
from pathlib import Path
# Add grandparent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from modules.cell_view_sorts import selection_sort
from modules.core import StepCounter, MAX_STEPS
from modules.metrics import sortedness
import modules.cell_view_sorts as cvs
import random

def debug_groups(initial_values):
    frozen_indices = {}
    n = len(initial_values)
    
    class SelectionCell:
        def __init__(self, value, cell_id, initial_position, frozen_type="active"):
            self.value = value
            self.cell_id = cell_id
            self.group = None
            self.left_boundary = initial_position
            self.right_boundary = initial_position
            self.ideal_position = initial_position
            self.frozen_type = frozen_type

        def update(self):
            self.ideal_position = self.left_boundary

        def can_initiate_move(self):
            return True

        def can_be_moved(self):
            return True
    
    cells = [SelectionCell(v, i, i) for i, v in enumerate(initial_values)]
    groups = [cvs._SelectionGroup(i, i, i) for i in range(n)]
    
    for i in range(n):
        cells[i].group = groups[i]
        groups[i].cells.append(cells[i])
    
    steps = StepCounter()
    
    for timestep in range(200):  # Limited run
        # Phase 1: Cell movements
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
            
            target = max(cell.left_boundary, min(cell.right_boundary, cell.ideal_position))
            if target == idx:
                cell.ideal_position = min(cell.right_boundary, cell.ideal_position + 1)
                continue
            
            neighbor = cells[target]
            steps.comparisons += 1
            
            if cell.value < neighbor.value and neighbor.can_be_moved():
                cells[idx], cells[target] = cells[target], cells[idx]
                cells_that_acted.add(neighbor.cell_id)
                steps.swaps += 1
                swapped_any = True
                break
            else:
                cell.ideal_position = min(cell.right_boundary, cell.ideal_position + 1)
        
        # Phase 2: Merge groups
        merged_any = False
        i = 0
        active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
        
        # DETAILED LOGGING
        if len(active_groups) <= 3 and timestep % 10 == 0:
            print(f"\nStep {timestep}: {len(active_groups)} groups")
            current_vals = [c.value for c in cells]
            print(f"  Array: {current_vals}")
            for g in active_groups:
                group_vals = current_vals[g.left_boundary:g.right_boundary+1]
                is_sorted = g.is_sorted(cells)
                print(f"  Group [{g.left_boundary}-{g.right_boundary}]: {group_vals} - sorted={is_sorted}")
        
        while i < len(active_groups) - 1:
            current_group = active_groups[i]
            next_group = active_groups[i + 1]
            
            # Check adjacency
            adjacent = (current_group.right_boundary + 1 == next_group.left_boundary)
            
            if adjacent:
                curr_sorted = current_group.is_sorted(cells)
                next_sorted = next_group.is_sorted(cells)
                
                if curr_sorted and next_sorted:
                    if len(active_groups) <= 3:
                        print(f"  MERGING groups {i} and {i+1} at step {timestep}")
                    current_group.merge_with(next_group, cells)
                    groups.remove(next_group)
                    active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
                    merged_any = True
                    continue
                elif len(active_groups) <= 3 and timestep % 10 == 0:
                    print(f"  Can't merge: curr_sorted={curr_sorted}, next_sorted={next_sorted}")
            
            i += 1
        
        # Check termination
        if len(active_groups) == 1 and active_groups[0].left_boundary == 0 and active_groups[0].right_boundary == n - 1:
            if active_groups[0].is_sorted(cells):
                print(f"\nCONVERGED at step {timestep}!")
                break
        
        if not swapped_any and not merged_any:
            is_sorted_array = all(cells[i].value <= cells[i + 1].value for i in range(n - 1))
            if is_sorted_array:
                print(f"\nSORTED at step {timestep}!")
                break
            
            all_at_boundary = all(cell.ideal_position >= cell.right_boundary for cell in cells)
            if all_at_boundary:
                if len(active_groups) <= 3 and timestep % 10 == 0:
                    print(f"  RESET at step {timestep}")
                for cell in cells:
                    cell.ideal_position = cell.left_boundary
    
    final_values = [c.value for c in cells]
    return final_values, steps

# Test with N=10
test = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Testing with N=10 (reverse sorted)")
print("=" * 70)
result, steps = debug_groups(test)
print("\n" + "=" * 70)
print(f"Final: {result}")
print(f"Expected: {sorted(test)}")
print(f"Swaps: {steps.swaps}")
