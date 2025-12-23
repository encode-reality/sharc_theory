import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Test Insertion Sort with different frozen cell positions."""

import numpy as np
from modules.cell_view_sorts import insertion_sort
from modules.metrics import sortedness

test_array = list(range(20, 0, -1))

# Test different frozen positions
test_cases = [
    ("Frozen at [1, 6]", {1: 'immovable', 6: 'immovable'}),
    ("Frozen at [10, 15]", {10: 'immovable', 15: 'immovable'}),
    ("Frozen at [18, 19]", {18: 'immovable', 19: 'immovable'}),
]

print("Testing Insertion Sort with N=20 and different frozen positions")
print("=" * 70)

for name, frozen_indices in test_cases:
    print(f"\n{name}: {sorted(frozen_indices.keys())}")
    result, steps, history = insertion_sort(test_array.copy(), frozen_indices=frozen_indices)

    print(f"  Swaps: {steps.swaps:,}")
    print(f"  Final sortedness: {sortedness(result):.1f}%")
    print(f"  History points: {len(history)}")

    if steps.swaps == 0:
        print("  STATUS: STUCK - No progress made")
    else:
        print("  STATUS: Working")

print()
print("=" * 70)
print("CONCLUSION:")
print("Insertion Sort gets stuck when frozen cells are near the beginning")
print("of a reverse-sorted array because elements can't move past them")
print("and the 'left side sorted' requirement blocks all progress.")
