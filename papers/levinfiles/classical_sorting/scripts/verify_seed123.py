import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Verify that seed 123 works for all algorithms with N=20."""

import numpy as np
from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort
from modules.metrics import sortedness

# Parameters
array_size = 20
frozen_pct = 10
num_frozen = int(array_size * frozen_pct / 100)

# Create test array
test_array = list(range(array_size, 0, -1))

# Use seed 123
np.random.seed(123)
frozen_positions = np.random.choice(array_size, size=num_frozen, replace=False)
frozen_indices = {int(pos): 'immovable' for pos in frozen_positions}

print("Verifying seed 123 with N=20")
print("=" * 70)
print(f"Frozen positions: {sorted(frozen_indices.keys())}")
print()

algorithms = [
    ('Bubble Sort', bubble_sort),
    ('Insertion Sort', insertion_sort),
    ('Selection Sort', selection_sort)
]

for name, algo_func in algorithms:
    result, steps, history = algo_func(test_array.copy(), frozen_indices=frozen_indices)
    final_sort = sortedness(result)

    status = "PASS" if steps.swaps > 0 else "STUCK"
    print(f"{name:15s}: {steps.swaps:4d} swaps, {final_sort:5.1f}% sortedness - {status}")

print()
print("=" * 70)

if all(algo_func(test_array.copy(), frozen_indices=frozen_indices)[1].swaps > 0
       for _, algo_func in algorithms):
    print("SUCCESS: All algorithms work with seed 123 at N=20")
else:
    print("WARNING: Some algorithms still stuck")
