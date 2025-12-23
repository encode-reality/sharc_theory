import sys
from pathlib import Path
# Add grandparent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from modules.core import Cell, StepCounter, MAX_STEPS, FrozenType
from modules.metrics import sortedness
import random

# Simple test
initial_values = [5, 2, 8, 1]
n = len(initial_values)

cells = [Cell(value=v, algotype="selection", frozen_type="active") for v in initial_values]
ideal_positions = [0 for _ in range(n)]

print(f"Initial: {[c.value for c in cells]}")
print(f"Ideal positions: {ideal_positions}\n")

steps = StepCounter()
history = []

# Run a few timesteps manually
for timestep in range(5):
    print(f"=== Timestep {timestep} ===")
    print(f"Array: {[c.value for c in cells]}")
    print(f"Ideal positions: {ideal_positions}")

    idx_order = list(range(n))
    random.seed(42 + timestep)
    random.shuffle(idx_order)
    print(f"Cell order: {idx_order}")

    swapped_any = False

    for idx in idx_order:
        cell = cells[idx]
        target = max(0, min(n - 1, ideal_positions[idx]))

        print(f"  Cell {idx} (value={cell.value}), ideal_pos={ideal_positions[idx]}, target={target}", end="")

        if target == idx:
            print(f" -> SKIP (self), increment ideal_pos")
            ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)
            continue

        neighbor = cells[target]
        print(f", neighbor value={neighbor.value}", end="")

        if cell.value < neighbor.value:
            print(f" -> SWAP ({cell.value} < {neighbor.value})")
            cells[idx], cells[target] = cells[target], cells[idx]
            ideal_positions[idx], ideal_positions[target] = ideal_positions[target], ideal_positions[idx]
            swapped_any = True
            print(f"     After swap: {[c.value for c in cells]}")
            print(f"     Ideal positions: {ideal_positions}")
        else:
            print(f" -> NO SWAP ({cell.value} >= {neighbor.value}), increment ideal_pos")
            ideal_positions[idx] = min(n - 1, ideal_positions[idx] + 1)

    print()
    if not swapped_any:
        print("No swaps this timestep - DONE")
        break

print(f"\nFinal: {[c.value for c in cells]}")
print(f"Expected: {sorted(initial_values)}")
