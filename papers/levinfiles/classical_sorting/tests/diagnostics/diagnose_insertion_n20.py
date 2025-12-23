import sys
from pathlib import Path
# Add grandparent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
"""Diagnose Insertion Sort issue with N=20 and frozen cells."""

import numpy as np
from modules.cell_view_sorts import insertion_sort
from modules.metrics import sortedness
import time

# Parameters matching Experiment 6 with N=20
array_size = 20
frozen_pct = 10
num_frozen = int(array_size * frozen_pct / 100)

# Create worst-case test array (reverse sorted)
test_array = list(range(array_size, 0, -1))

# Randomly select cells to freeze
np.random.seed(42)  # Same seed as notebook
frozen_positions = np.random.choice(array_size, size=num_frozen, replace=False)
frozen_indices = {int(pos): 'immovable' for pos in frozen_positions}

print("Diagnostic Test: Insertion Sort with N=20")
print("=" * 70)
print(f"Array size: {array_size}")
print(f"Frozen cells: {frozen_pct}% ({num_frozen} cells)")
print(f"Initial array: {test_array}")
print(f"Frozen positions: {sorted(frozen_indices.keys())}")
print()

print("Running Insertion Sort (timeout: 30 seconds)...")
start_time = time.time()

try:
    result, steps, history = insertion_sort(test_array.copy(), frozen_indices=frozen_indices)
    elapsed = time.time() - start_time

    print(f"✓ Completed in {elapsed:.2f} seconds")
    print()
    print(f"Final sortedness: {sortedness(result):.1f}%")
    print(f"Swaps: {steps.swaps:,}")
    print(f"Comparisons: {steps.comparisons:,}")
    print(f"History points: {len(history)}")
    print(f"Final array: {result}")

    if len(history) == 0:
        print()
        print("WARNING: No swaps occurred!")
        print("This suggests the algorithm couldn't make any progress.")
        print()
        print("Analyzing why:")
        print("- Initial sortedness:", sortedness(test_array), "%")
        print("- With immovable frozen cells, insertion sort may be blocked")
        print("- Check if frozen cells prevent left side from being sorted")

except Exception as e:
    elapsed = time.time() - start_time
    print(f"✗ Error after {elapsed:.2f} seconds: {e}")
    import traceback
    traceback.print_exc()
