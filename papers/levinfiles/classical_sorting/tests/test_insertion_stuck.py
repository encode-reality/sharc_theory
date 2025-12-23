import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Test if Insertion Sort gets stuck with frozen position 0."""

import numpy as np
from modules.cell_view_sorts import insertion_sort
from modules.metrics import sortedness
from modules.core import MAX_STEPS

# Small test to show the issue
test_array = [5, 4, 3, 2, 1]
frozen_indices = {0: 'immovable'}  # Position 0 frozen with value 5

print("Testing Insertion Sort with frozen position 0")
print("Array:", test_array)
print("Frozen:", frozen_indices)
print()

result, steps, history = insertion_sort(test_array.copy(), frozen_indices=frozen_indices)

print("Result:", result)
print("Swaps:", steps.swaps)
print("Comparisons:", steps.comparisons)
print("History length:", len(history))
print("Hit MAX_STEPS?", steps.comparisons > 0 and steps.swaps == 0)
print()

if len(history) == 0:
    print("DIAGNOSIS: Insertion Sort made 0 swaps!")
    print("Reason: Position 0 is frozen with value 5 (max value)")
    print("        The left side can never be sorted")
    print("        Algorithm requirement: left_sorted must be True")
    print("        But [5] followed by [4,3,2,1] is never sorted")
    print()
    print("SOLUTION: Use different random seed or exclude position 0 from freezing")
