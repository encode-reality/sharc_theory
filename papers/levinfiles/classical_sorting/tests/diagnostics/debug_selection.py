"""
Debug selection sort to see where it diverges.
"""

import sys
from pathlib import Path
# Add grandparent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from modules.cell_view_sorts import selection_sort

# Test with N=10 (known to fail)
test_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Testing selection_sort with N=10...")
print(f"Initial: {test_array}")
print()

# Monkey-patch to add logging
import modules.cell_view_sorts as cvs
from modules.core import StepCounter, MAX_STEPS
from modules.metrics import sortedness
import random

def debug_selection_sort(initial_values, frozen_indices=None, algotype="selection"):
    frozen_indices = frozen_indices or {}
    n = len(initial_values)
    
    # SelectionCell class
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
            return self.frozen_type == "active"

        def can_be_moved(self):
            return self.frozen_type in ("active", "movable")
    
    cells = [SelectionCell(v, i, i, frozen_indices.get(i, "active"))
             for i, v in enumerate(initial_values)]
    
    groups = [cvs._SelectionGroup(i, i, i) for i in range(n)]
    
    for i in range(n):
        cells[i].group = groups[i]
        groups[i].cells.append(cells[i])
    
    steps = StepCounter()
    history = []
    
    timestep_limit = 1000  # Limit for debugging
    
    for timestep in range(min(MAX_STEPS, timestep_limit)):
        # Debug output every 100 steps
        if timestep % 100 == 0:
            current_sort = sortedness([c.value for c in cells])
            num_groups = len([g for g in groups if g.left_boundary <= g.right_boundary])
            print(f"Step {timestep}: {current_sort:.1f}% sorted, {num_groups} groups, {steps.swaps} swaps")
        
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
            
            target = max(cell.left_boundary,
                        min(cell.right_boundary, cell.ideal_position))
            
            if target == idx:
                cell.ideal_position = min(cell.right_boundary,
                                         cell.ideal_position + 1)
                continue
            
            neighbor = cells[target]
            steps.comparisons += 1
            
            if cell.value < neighbor.value and neighbor.can_be_moved():
                cells[idx], cells[target] = cells[target], cells[idx]
                cells_that_acted.add(neighbor.cell_id)
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
                break
            else:
                cell.ideal_position = min(cell.right_boundary,
                                         cell.ideal_position + 1)
        
        # Phase 2: Merge groups
        merged_any = False
        i = 0
        active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
        
        while i < len(active_groups) - 1:
            current_group = active_groups[i]
            next_group = active_groups[i + 1]
            
            if current_group.right_boundary + 1 == next_group.left_boundary:
                if current_group.is_sorted(cells) and next_group.is_sorted(cells):
                    current_group.merge_with(next_group, cells)
                    groups.remove(next_group)
                    active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
                    merged_any = True
                    continue
            
            i += 1
        
        # Termination
        if (len(active_groups) == 1 and
            active_groups[0].left_boundary == 0 and
            active_groups[0].right_boundary == n - 1):
            if active_groups[0].is_sorted(cells):
                print(f"Converged at step {timestep}")
                break
        
        if not swapped_any and not merged_any:
            is_sorted = all(cells[i].value <= cells[i + 1].value
                          for i in range(n - 1))
            if is_sorted:
                print(f"Sorted at step {timestep}")
                break
            
            all_at_boundary = all(
                cell.ideal_position >= cell.right_boundary
                for cell in cells
            )
            if all_at_boundary:
                print(f"Reset at step {timestep}")
                for cell in cells:
                    cell.ideal_position = cell.left_boundary
    
    final_values = [c.value for c in cells]
    return final_values, steps, history

result, steps, history = debug_selection_sort(test_array)

print()
print(f"Result: {result}")
print(f"Expected: {sorted(test_array)}")
print(f"Correct: {result == sorted(test_array)}")
print(f"Swaps: {steps.swaps}")
