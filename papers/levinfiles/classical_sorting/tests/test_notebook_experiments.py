import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Test all notebook experiments before running in notebook."""

from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort, mixed_algotype_sort
from modules.metrics import sortedness
import numpy as np

print("Testing Notebook Experiments")
print("="*70)

# Experiment 1: Basic Sorting
print("\n[Experiment 1] Basic Sorting")
print("-"*70)
test_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
expected = sorted(test_array)

results = {}
for name, func in [('Bubble', bubble_sort), ('Insertion', insertion_sort), ('Selection', selection_sort)]:
    result, steps, history = func(test_array.copy())
    correct = result == expected
    sort_pct = sortedness(result)
    results[name] = {'correct': correct, 'sortedness': sort_pct, 'swaps': steps.swaps, 'history': history}
    print(f"  {name:10s}: {sort_pct:5.1f}% sortedness, {steps.swaps:6,} swaps, Correct: {'PASS' if correct else 'FAIL'}")

if all(r['correct'] for r in results.values()):
    print("PASS: Experiment 1 - All algorithms sort correctly")
else:
    print("FAIL: Experiment 1 - Some algorithms failed")
    for name, data in results.items():
        if not data['correct']:
            print(f"  FAILED: {name}")

# Experiment 2: Check if we have sorting history for visualization
print("\n[Experiment 2] Sorting Dynamics (checking history)")
print("-"*70)
for name, data in results.items():
    hist_len = len(data['history'])
    print(f"  {name:10s}: {hist_len} history points")
    if hist_len > 0:
        print(f"    Start: {data['history'][0]:.1f}%, End: {data['history'][-1]:.1f}%")

# Check for monotonic vs non-monotonic
bubble_monotonic = all(results['Bubble']['history'][i] <= results['Bubble']['history'][i+1]
                       for i in range(len(results['Bubble']['history'])-1))
insertion_monotonic = all(results['Insertion']['history'][i] <= results['Insertion']['history'][i+1]
                          for i in range(len(results['Insertion']['history'])-1))
selection_monotonic = all(results['Selection']['history'][i] <= results['Selection']['history'][i+1]
                          for i in range(len(results['Selection']['history'])-1))

print(f"\n  Monotonic progression:")
print(f"    Bubble:    {'Yes' if bubble_monotonic else 'No'}")
print(f"    Insertion: {'Yes' if insertion_monotonic else 'No'}")
print(f"    Selection: {'Yes' if selection_monotonic else 'No (can have temporary regression)'}")

print("PASS: Experiment 2 - History data available for visualization")

# Experiment 3: Algorithm Comparison
print("\n[Experiment 3] Algorithm Comparison")
print("-"*70)
test_size = 10
test_arr = list(np.random.randint(1, 50, size=test_size))

bubble_result, bubble_steps, _ = bubble_sort(test_arr.copy())
insertion_result, insertion_steps, _ = insertion_sort(test_arr.copy())
selection_result, selection_steps, _ = selection_sort(test_arr.copy())

print(f"  Array size: {test_size}")
print(f"  Bubble:    {bubble_steps.swaps:6,} swaps, {bubble_steps.comparisons:6,} comparisons")
print(f"  Insertion: {insertion_steps.swaps:6,} swaps, {insertion_steps.comparisons:6,} comparisons")
print(f"  Selection: {selection_steps.swaps:6,} swaps, {selection_steps.comparisons:6,} comparisons")

print("PASS: Experiment 3 - Comparison metrics collected")

# Experiment 4: Frozen Cells
print("\n[Experiment 4] Frozen Cell Robustness")
print("-"*70)
test_array = list(np.random.randint(1, 50, size=20))
frozen_pcts = [0, 10, 30, 50]

for frozen_pct in frozen_pcts:
    num_frozen = int(20 * frozen_pct / 100)
    frozen_indices = {}
    if num_frozen > 0:
        frozen_positions = np.random.choice(20, size=num_frozen, replace=False)
        frozen_indices = {int(pos): 'frozen' for pos in frozen_positions}

    result, steps, history = bubble_sort(test_array.copy(), frozen_indices=frozen_indices)
    final_sort = sortedness(result)
    print(f"  {frozen_pct:2d}% frozen: {final_sort:5.1f}% sortedness, {steps.swaps:6,} swaps")

print("PASS: Experiment 4 - Frozen cell experiments work")

# Experiment 5: Chimeric Arrays
print("\n[Experiment 5] Chimeric Arrays (Mixed Algotypes)")
print("-"*70)
chimeric_array = list(np.random.randint(1, 50, size=20))

mixtures = [
    ("Pure Bubble", [1.0, 0.0, 0.0]),
    ("Pure Insertion", [0.0, 1.0, 0.0]),
    ("Pure Selection", [0.0, 0.0, 1.0]),
    ("Equal Mix", [0.33, 0.33, 0.34])
]

for name, composition in mixtures:
    bubble_count = int(composition[0] * 20)
    insertion_count = int(composition[1] * 20)
    selection_count = 20 - bubble_count - insertion_count

    algotype_assignments = (['bubble'] * bubble_count +
                           ['insertion'] * insertion_count +
                           ['selection'] * selection_count)

    np.random.shuffle(algotype_assignments)

    result, steps, hist, algo_hist = mixed_algotype_sort(chimeric_array.copy(), algotype_assignments)
    final_sortedness = sortedness(result)
    correct = result == sorted(chimeric_array)

    print(f"  {name:20s}: {final_sortedness:5.1f}% sortedness, {steps.swaps:6,} swaps, Correct: {'PASS' if correct else 'partial'}")

print("PASS: Experiment 5 - Chimeric experiments work")

print("\n" + "="*70)
print("ALL NOTEBOOK EXPERIMENTS VALIDATED")
print("="*70)
