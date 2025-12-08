"""
Verify all imports needed by morphogenesis_experiments.ipynb work correctly.
"""

print("Testing notebook imports...")
print("=" * 70)

# Test all imports exactly as they appear in the notebook
try:
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from typing import List, Dict
    print("[OK] Standard library imports")
except Exception as e:
    print(f"[FAIL] Standard library imports: {e}")
    exit(1)

try:
    from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort, mixed_algotype_sort
    print("[OK] Cell-view sorting algorithms")
except Exception as e:
    print(f"[FAIL] Cell-view sorts: {e}")
    exit(1)

try:
    from modules.metrics import sortedness
    print("[OK] Metrics module")
except Exception as e:
    print(f"[FAIL] Metrics: {e}")
    exit(1)

try:
    from modules.core import Cell, StepCounter
    print("[OK] Core classes")
except Exception as e:
    print(f"[FAIL] Core: {e}")
    exit(1)

try:
    from modules.visualization import plot_sorting_progress, plot_sortedness_comparison
    print("[OK] Visualization functions")
except Exception as e:
    print(f"[FAIL] Visualization: {e}")
    exit(1)

try:
    from modules.experiments import (
        compare_algorithms,
        frozen_cell_experiment,
        chimeric_experiment
    )
    print("[OK] Experiment functions")
except Exception as e:
    print(f"[FAIL] Experiments: {e}")
    exit(1)

print("=" * 70)
print("\nAll notebook imports successful!")
print("\nRunning quick functionality test...")
print("-" * 70)

# Test a simple sort to ensure everything works
test_array = [3, 1, 4, 1, 5, 9, 2, 6]
result, steps, history = bubble_sort(test_array)
expected = sorted(test_array)

if result == expected:
    print(f"[OK] Bubble sort test: {test_array} -> {result}")
    print(f"     Steps: {steps.swaps} swaps, {steps.comparisons} comparisons")
else:
    print(f"[FAIL] Bubble sort: got {result}, expected {expected}")

result, steps, history = insertion_sort(test_array)
if result == expected:
    print(f"[OK] Insertion sort test: {test_array} -> {result}")
    print(f"     Steps: {steps.swaps} swaps, {steps.comparisons} comparisons")
else:
    print(f"[FAIL] Insertion sort: got {result}, expected {expected}")

result, steps, history = selection_sort(test_array)
if result == expected:
    print(f"[OK] Selection sort test: {test_array} -> {result}")
    print(f"     Steps: {steps.swaps} swaps, {steps.comparisons} comparisons")
else:
    print(f"[FAIL] Selection sort: got {result}, expected {expected}")

print("-" * 70)
print("\nThe notebook should now run without import errors!")
print("\nNext steps:")
print("1. Open morphogenesis_experiments.ipynb in VSCode")
print("2. Select Python 3.12.10 as the kernel")
print("3. Run all cells")
print("=" * 70)
