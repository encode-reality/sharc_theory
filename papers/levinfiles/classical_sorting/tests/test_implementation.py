"""
Test script to verify all modules work correctly.
This runs quick smoke tests on each component.
"""

import sys
import numpy as np
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

print("=" * 60)
print("Testing Morphogenesis Sorting Implementation")
print("=" * 60)

# Test 1: Import all modules
print("\n[Test 1] Importing modules...")
try:
    from modules import core, metrics, traditional_sorts, cell_view_sorts
    from modules import experiments, visualization, statistical
    print("[PASS] All modules imported successfully")
except ImportError as e:
    print(f"[FAIL] Import failed: {e}")
    sys.exit(1)

# Test 2: Core data structures
print("\n[Test 2] Testing core data structures...")
try:
    cell = core.Cell(value=5, algotype="bubble")
    assert cell.can_initiate_move() == True
    assert cell.can_be_moved() == True

    frozen_cell = core.Cell(value=3, algotype="insertion", frozen_type="immovable")
    assert frozen_cell.can_initiate_move() == False
    assert frozen_cell.can_be_moved() == False

    counter = core.StepCounter()
    counter.comparisons = 10
    counter.swaps = 5
    assert counter.total == 15

    print("[PASS] Core data structures work correctly")
except AssertionError as e:
    print(f"[FAIL] Core test failed: {e}")
    sys.exit(1)

# Test 3: Metrics
print("\n[Test 3] Testing metrics...")
try:
    # Test sortedness
    sorted_arr = [1, 2, 3, 4, 5]
    unsorted_arr = [5, 4, 3, 2, 1]
    partially_sorted = [1, 3, 2, 4, 5]

    assert metrics.sortedness(sorted_arr) == 100.0
    assert metrics.sortedness(unsorted_arr) == 0.0
    assert 0 < metrics.sortedness(partially_sorted) < 100

    # Test monotonicity error
    assert metrics.monotonicity_error(sorted_arr) == 0
    assert metrics.monotonicity_error(unsorted_arr) > 0

    # Test delayed gratification
    dg_series = [50, 40, 30, 50, 70, 90]  # Drop then rise
    dg = metrics.compute_delayed_gratification(dg_series)
    assert dg > 0  # Should detect the delayed gratification pattern

    # Test aggregation
    algotypes = ["bubble"] * 5 + ["insertion"] * 5
    agg = metrics.aggregation_value(algotypes)
    assert agg > 50  # Should be high since types are clustered

    print("[PASS] All metrics calculated correctly")
except (AssertionError, Exception) as e:
    print(f"[FAIL] Metrics test failed: {e}")
    sys.exit(1)

# Test 4: Traditional sorts
print("\n[Test 4] Testing traditional sorting algorithms...")
try:
    test_array = [3, 1, 4, 1, 5, 9, 2, 6]

    # Bubble sort
    sorted_arr, steps, history = traditional_sorts.bubble_sort(test_array.copy())
    assert sorted_arr == sorted(test_array)
    assert steps.total > 0
    assert len(history) > 0

    # Insertion sort
    sorted_arr, steps, history = traditional_sorts.insertion_sort(test_array.copy())
    assert sorted_arr == sorted(test_array)

    # Selection sort
    sorted_arr, steps, history = traditional_sorts.selection_sort(test_array.copy())
    assert sorted_arr == sorted(test_array)

    print("[PASS] Traditional sorting algorithms work correctly")
except (AssertionError, Exception) as e:
    print(f"[FAIL] Traditional sorts test failed: {e}")
    sys.exit(1)

# Test 5: Cell-view sorts
print("\n[Test 5] Testing cell-view sorting algorithms...")
try:
    test_array = [3, 1, 4, 1, 5, 9, 2, 6]

    # Bubble sort (cell-view)
    sorted_arr, steps, history = cell_view_sorts.bubble_sort(test_array.copy())
    assert sorted_arr == sorted(test_array), f"Bubble: got {sorted_arr}, expected {sorted(test_array)}"
    assert steps.total > 0

    # Insertion sort (cell-view)
    sorted_arr, steps, history = cell_view_sorts.insertion_sort(test_array.copy())
    assert sorted_arr == sorted(test_array), f"Insertion: got {sorted_arr}, expected {sorted(test_array)}"

    # Selection sort (cell-view)
    sorted_arr, steps, history = cell_view_sorts.selection_sort(test_array.copy())
    assert sorted_arr == sorted(test_array), f"Selection: got {sorted_arr}, expected {sorted(test_array)}"

    print("[PASS] Cell-view sorting algorithms work correctly")
except (AssertionError, Exception) as e:
    print(f"[FAIL] Cell-view sorts test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 6: Frozen cells
print("\n[Test 6] Testing frozen cell handling...")
try:
    test_array = [5, 4, 3, 2, 1]
    frozen_config = {2: "immovable"}  # Freeze middle element

    sorted_arr, steps, history = cell_view_sorts.bubble_sort(
        test_array.copy(),
        frozen_config
    )

    # Should complete but may have higher error due to frozen cell
    error = metrics.monotonicity_error(sorted_arr)
    print(f"  Monotonicity error with frozen cell: {error}")

    print("[PASS] Frozen cell handling works")
except Exception as e:
    print(f"[FAIL] Frozen cells test failed: {e}")
    sys.exit(1)

# Test 7: Mixed algotypes
print("\n[Test 7] Testing mixed algotype sorting...")
try:
    test_array = [5, 4, 3, 2, 1, 6, 7, 8]
    algotypes = ["bubble"] * 4 + ["insertion"] * 4

    sorted_arr, steps, sort_hist, algotype_hist = cell_view_sorts.mixed_algotype_sort(
        test_array.copy(),
        algotypes
    )

    # Should produce reasonable results
    final_sortedness = metrics.sortedness(sorted_arr)
    print(f"  Final sortedness: {final_sortedness:.1f}%")

    # Check aggregation tracking
    assert len(algotype_hist) > 0

    print("[PASS] Mixed algotype sorting works")
except Exception as e:
    print(f"[FAIL] Mixed algotypes test failed: {e}")
    sys.exit(1)

# Test 8: Run a small experiment
print("\n[Test 8] Testing experiment harness...")
try:
    # Run a very small experiment (fewer repeats for speed)
    results = experiments.run_experiments(
        algorithm_name="bubble",
        variant="cell_view",
        n_cells=10,
        n_repeats=3
    )

    assert "total_steps" in results
    assert "sortedness_history" in results
    assert len(results["total_steps"]) == 3

    print("[PASS] Experiment harness works correctly")
except Exception as e:
    print(f"[FAIL] Experiment test failed: {e}")
    sys.exit(1)

# Test 9: Statistical functions
print("\n[Test 9] Testing statistical analysis...")
try:
    sample1 = [10, 12, 11, 13, 12]
    sample2 = [20, 22, 21, 23, 22]

    z_stat, z_p = statistical.z_test(sample1, sample2)
    t_stat, t_p = statistical.t_test(sample1, sample2)

    assert z_p < 0.05  # Should be significantly different
    assert t_p < 0.05

    stats = statistical.summarize_statistics(sample1)
    assert "mean" in stats
    assert "std" in stats
    assert stats["n"] == 5

    print("[PASS] Statistical functions work correctly")
except (AssertionError, Exception) as e:
    print(f"[FAIL] Statistical test failed: {e}")
    sys.exit(1)

# Final summary
print("\n" + "=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)
print("\nThe implementation is ready to use.")
print("You can now run the Jupyter notebook: morphogenesis_experiment.ipynb")
print("=" * 60)
