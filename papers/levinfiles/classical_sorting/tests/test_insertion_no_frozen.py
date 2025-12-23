import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Test Insertion Sort with N=20, NO frozen cells."""

from modules.cell_view_sorts import insertion_sort
from modules.metrics import sortedness

# Test with reverse sorted array, NO frozen cells
test_array = list(range(20, 0, -1))

print("Testing Insertion Sort with N=20, NO frozen cells")
print("Array:", test_array)
print()

result, steps, history = insertion_sort(test_array.copy(), frozen_indices={})

print("Result:", result)
print(f"Swaps: {steps.swaps:,}")
print(f"Comparisons: {steps.comparisons:,}")
print(f"History points: {len(history)}")
print(f"Final sortedness: {sortedness(result):.1f}%")
print()

if steps.swaps > 0:
    print("SUCCESS: Insertion Sort works without frozen cells")
else:
    print("PROBLEM: Insertion Sort not working even without frozen cells!")
    print("This suggests a deeper issue with the algorithm")
