import sys
from pathlib import Path
# Add grandparent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
"""Analyze why algorithms stop at different points in Experiment 6."""

import numpy as np
from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort
from modules.metrics import sortedness

# Set up test matching Experiment 6 with N=20, seed 123
array_size = 20
frozen_pct = 10
num_frozen = int(array_size * frozen_pct / 100)

test_array = list(range(array_size, 0, -1))

np.random.seed(123)
frozen_positions = np.random.choice(array_size, size=num_frozen, replace=False)
frozen_indices = {int(pos): 'immovable' for pos in frozen_positions}

print("Analyzing Why Algorithms Stop at Different Points")
print("=" * 70)
print(f"Initial array: {test_array}")
print(f"Frozen positions: {sorted(frozen_indices.keys())}")
print(f"  Position {sorted(frozen_indices.keys())[0]}: value {test_array[sorted(frozen_indices.keys())[0]]}")
print(f"  Position {sorted(frozen_indices.keys())[1]}: value {test_array[sorted(frozen_indices.keys())[1]]}")
print()

algorithms = [
    ('Bubble Sort', bubble_sort),
    ('Insertion Sort', insertion_sort),
    ('Selection Sort', selection_sort)
]

results = {}

for name, algo_func in algorithms:
    result, steps, history = algo_func(test_array.copy(), frozen_indices=frozen_indices)
    results[name] = {
        'result': result,
        'steps': steps,
        'history': history,
        'sortedness': sortedness(result)
    }

print("=" * 70)
print("RESULTS:")
print("=" * 70)

for name, data in results.items():
    print(f"\n{name}:")
    print(f"  Swaps: {data['steps'].swaps}")
    print(f"  Final sortedness: {data['sortedness']:.1f}%")
    print(f"  Final array: {data['result']}")

    # Identify where frozen cells ended up
    frozen_final_positions = []
    for i, val in enumerate(data['result']):
        # Check if this is one of the originally frozen values
        original_frozen_vals = [test_array[pos] for pos in frozen_indices.keys()]
        if val in original_frozen_vals and i in frozen_indices.keys():
            frozen_final_positions.append((i, val))

    print(f"  Frozen cells still at original positions: {frozen_final_positions}")

    # Analyze sortedness around frozen cells
    for frozen_pos in sorted(frozen_indices.keys()):
        if frozen_pos > 0 and frozen_pos < len(data['result']) - 1:
            left_val = data['result'][frozen_pos - 1]
            frozen_val = data['result'][frozen_pos]
            right_val = data['result'][frozen_pos + 1]
            print(f"    Around position {frozen_pos}: [{left_val}] <{frozen_val}> [{right_val}]")

print()
print("=" * 70)
print("ANALYSIS: Why Each Algorithm Stops")
print("=" * 70)

print("\nBubble Sort:")
print("  - Can swap both LEFT and RIGHT")
print("  - Continues until NO adjacent pairs are out of order")
print("  - Most persistent algorithm")
print("  - Only stops when truly stuck (no more swaps possible)")

print("\nInsertion Sort:")
print("  - Can ONLY move LEFT")
print("  - Requires LEFT SIDE to be sorted before moving")
print("  - Stops when:")
print("    1. Left side not sorted (due to frozen barriers), OR")
print("    2. Can't move past immovable frozen cells")
print("  - Gets blocked earlier by frozen cells in critical positions")

print("\nSelection Sort:")
print("  - Works with GROUPS and IDEAL POSITIONS")
print("  - Can only move LEFT to reach ideal position")
print("  - Stops when:")
print("    1. All cells are at ideal position within their group, OR")
print("    2. Groups can't merge due to frozen cells")
print("  - More progress than Insertion but less than Bubble")

print()
print("=" * 70)
print("KEY INSIGHT:")
print("=" * 70)
print("The stopping point depends on the algorithm's MOVEMENT CONSTRAINTS:")
print("  - Bidirectional movement (Bubble) → Most progress")
print("  - Unidirectional + sorted requirement (Insertion) → Least progress")
print("  - Unidirectional + group-based (Selection) → Medium progress")
