"""Debug [3, 1, 2] specifically"""
import random

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
        old_ip = self.ideal_position
        self.ideal_position = self.left_boundary
        print(f"      Cell {self.cell_id} (v={self.value}) update: ip {old_ip} -> {self.ideal_position}")

    def __repr__(self):
        return f"C{self.cell_id}(v={self.value},ip={self.ideal_position},bounds=[{self.left_boundary},{self.right_boundary}])"

def debug_312():
    initial_values = [3, 1, 2]
    n = len(initial_values)
    cells = [SelectionCell(v, i, i) for i, v in enumerate(initial_values)]
    groups = [Group(i, i, i) for i in range(n)]
    
    for i in range(n):
        cells[i].group = groups[i]

    print(f"Initial: {[c.value for c in cells]}")
    print(f"Cells: {cells}\n")

    for timestep in range(20):
        print(f"=== Timestep {timestep} ===")
        
        # Phase 1: Moves
        idx_order = list(range(n))
        random.seed(42 + timestep)
        random.shuffle(idx_order)
        
        print(f"Order: {idx_order}")
        
        cells_that_acted = set()
        swapped_any = False
        
        for idx in idx_order:
            cell = cells[idx]
            if cell.cell_id in cells_that_acted:
                print(f"  pos{idx}: Cell{cell.cell_id} already acted, skip")
                continue
            cells_that_acted.add(cell.cell_id)
            
            target = max(cell.left_boundary, min(cell.right_boundary, cell.ideal_position))
            
            if target == idx:
                cell.ideal_position = min(cell.right_boundary, cell.ideal_position + 1)
                print(f"  pos{idx}: Cell{cell.cell_id} at target, increment ip to {cell.ideal_position}")
                continue
            
            neighbor = cells[target]
            
            if cell.value < neighbor.value:
                print(f"  pos{idx}: Cell{cell.cell_id} (v={cell.value}) SWAPS with pos{target} (v={neighbor.value})")
                cells[idx], cells[target] = cells[target], cells[idx]
                cells_that_acted.add(neighbor.cell_id)
                swapped_any = True
                break  # One swap per timestep
            else:
                cell.ideal_position = min(cell.right_boundary, cell.ideal_position + 1)
                print(f"  pos{idx}: Cell{cell.cell_id} (v={cell.value}) >= neighbor (v={neighbor.value}), increment ip to {cell.ideal_position}")
        
        print(f"After moves: {[c.value for c in cells]}")
        print(f"Cells: {cells}")
        
        # Phase 2: Merges
        merged_any = False
        i = 0
        active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
        
        while i < len(active_groups) - 1:
            current_group = active_groups[i]
            next_group = active_groups[i + 1]
            
            if current_group.right_boundary + 1 == next_group.left_boundary:
                is_current_sorted = current_group.is_sorted(cells)
                is_next_sorted = next_group.is_sorted(cells)
                
                if is_current_sorted and is_next_sorted:
                    print(f"  MERGE: Group{current_group.group_id} [{current_group.left_boundary}-{current_group.right_boundary}] + Group{next_group.group_id} [{next_group.left_boundary}-{next_group.right_boundary}]")
                    current_group.merge_with(next_group, cells)
                    groups.remove(next_group)
                    active_groups = [g for g in groups if g.left_boundary <= g.right_boundary]
                    merged_any = True
                    print(f"  After merge, cells: {cells}")
                    continue
            
            i += 1
        
        print(f"Swapped: {swapped_any}, Merged: {merged_any}")
        print(f"Active groups: {[(g.group_id, g.left_boundary, g.right_boundary) for g in groups]}\n")
        
        if not swapped_any and not merged_any:
            is_sorted = all(cells[i].value <= cells[i + 1].value for i in range(n - 1))
            print(f"No progress. Sorted: {is_sorted}")
            if is_sorted:
                break
            if timestep > 15:
                print("Stuck! Breaking.")
                break

debug_312()
