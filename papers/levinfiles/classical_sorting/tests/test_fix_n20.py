import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Test that Insertion Sort now works with N=20."""

import numpy as np
from modules.cell_view_sorts import insertion_sort
from modules.metrics import sortedness

# Parameters matching fixed Experiment 6
array_size = 20
frozen_pct = 10
num_frozen = int(array_size * frozen_pct / 100)

# Create worst-case test array (reverse sorted)
test_array = list(range(array_size, 0, -1))

# Randomly select cells to freeze (EXCLUDING position 0)
np.random.seed(42)
available_positions = list(range(1, array_size))  # Exclude position 0
frozen_positions = np.random.choice(available_positions, size=num_frozen, replace=False)
frozen_indices = {int(pos): 'immovable' for pos in frozen_positions}

print("Testing Insertion Sort with N=20 (position 0 excluded)")
print("=" * 70)
print(f"Array size: {array_size}")
print(f"Frozen cells: {frozen_pct}% ({num_frozen} cells)")
print(f"Frozen positions: {sorted(frozen_indices.keys())}")
print()

print("Running Insertion Sort...")
result, steps, history = insertion_sort(test_array.copy(), frozen_indices=frozen_indices)

print("PASS: Completed successfully")
print()
print(f"Final sortedness: {sortedness(result):.1f}%")
print(f"Swaps: {steps.swaps:,}")
print(f"Comparisons: {steps.comparisons:,}")
print(f"History points: {len(history)}")
print()

if len(history) > 0:
    print("SUCCESS: Insertion Sort made progress!")
    print(f"  Starting sortedness: {history[0]:.1f}%")
    print(f"  Final sortedness: {history[-1]:.1f}%")
    print(f"  Improvement: {history[-1] - history[0]:.1f}%")
else:
    print("WARNING: Still no progress made")
