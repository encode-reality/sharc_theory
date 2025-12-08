"""Debug Selection Sort to understand behavior"""

import random
from modules.core import StepCounter, MAX_STEPS

def selection_sort_debug(initial_values, max_timesteps=50):
    n = len(initial_values)

    class SelectionCell:
        def __init__(self, value, initial_idx):
            self.value = value
            self.ideal_position = 0
            self.initial_idx = initial_idx  # For tracking

        def __repr__(self):
            return f"Cell(v={self.value}, ip={self.ideal_position})"

    cells = [SelectionCell(v, i) for i, v in enumerate(initial_values)]
    steps = StepCounter()

    print(f"Initial: {[c.value for c in cells]}")
    print(f"Ideal positions: {[c.ideal_position for c in cells]}\n")

    for timestep in range(min(max_timesteps, MAX_STEPS)):
        idx_order = list(range(n))
        random.seed(42 + timestep)
        random.shuffle(idx_order)

        print(f"--- Timestep {timestep}, order: {idx_order} ---")
        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]
            target = max(0, min(n - 1, cell.ideal_position))

            if target == idx:
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)
                print(f"  Cell at {idx} (v={cell.value}): target==idx, increment ip to {cell.ideal_position}")
                continue

            neighbor = cells[target]
            steps.comparisons += 1

            if cell.value < neighbor.value:
                print(f"  Cell at {idx} (v={cell.value}, ip={cell.ideal_position}) SWAPS with {target} (v={neighbor.value}, ip={neighbor.ideal_position})")
                cells[idx], cells[target] = cells[target], cells[idx]
                steps.swaps += 1
                swapped_any = True
            else:
                print(f"  Cell at {idx} (v={cell.value}, ip={cell.ideal_position}) >= neighbor at {target} (v={neighbor.value}), increment ip")
                cell.ideal_position = min(n - 1, cell.ideal_position + 1)

        print(f"After timestep: {[c.value for c in cells]}")
        print(f"Ideal positions: {[c.ideal_position for c in cells]}")
        print(f"Swapped: {swapped_any}\n")

        if timestep >= 10:
            break

    return [c.value for c in cells], steps

# Test simple case
result, steps = selection_sort_debug([2, 1])
print(f"\nFinal result: {result}")
print(f"Total swaps: {steps.swaps}")
