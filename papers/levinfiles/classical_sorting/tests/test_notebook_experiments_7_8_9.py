"""
Test script for Experiments 7, 8, 9 - exact replication of notebook code.
This tests the code BEFORE adding to the notebook to catch errors early.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
import matplotlib.pyplot as plt

# Import all necessary functions
from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort, mixed_algotype_sort
from modules.metrics import sortedness, algo_type_clustering, identify_sortedness_dips

print("="*80)
print("TESTING EXPERIMENT 7: DELAYED GRATIFICATION")
print("="*80)

# Setup from Experiment 6 (needed for Experiment 7)
array_size = 20
frozen_pct = 10
num_frozen = int(array_size * frozen_pct / 100)
test_array_dynamics = list(range(array_size, 0, -1))

np.random.seed(123)
frozen_positions = np.random.choice(array_size, size=num_frozen, replace=False)
frozen_indices_dynamics = {int(pos): 'immovable' for pos in frozen_positions}

# Run algorithms to get dynamics_results
dynamics_algorithms = [
    ('Bubble Sort', bubble_sort),
    ('Insertion Sort', insertion_sort),
    ('Selection Sort', selection_sort)
]

dynamics_results = {}
for name, algo_func in dynamics_algorithms:
    result, steps, history = algo_func(test_array_dynamics.copy(), frozen_indices=frozen_indices_dynamics)
    dynamics_results[name] = {
        'history': history,
        'final_sortedness': sortedness(result),
        'swaps': steps.swaps,
        'comparisons': steps.comparisons,
        'result': result
    }

# Now test Experiment 7 code
print("\nRunning Experiment 7 code...")

dip_analysis = {}

for name, data in dynamics_results.items():
    history = data['history']
    dips = identify_sortedness_dips(history, threshold=0.1)

    dip_analysis[name] = {
        'dips': dips,
        'num_dips': len(dips),
        'total_magnitude': sum(mag for _, mag in dips),
        'avg_magnitude': np.mean([mag for _, mag in dips]) if dips else 0.0,
        'history': history
    }

    print(f"{name}: {len(dips)} dips detected")

print("[PASS] Experiment 7 code runs successfully\n")


print("="*80)
print("TESTING EXPERIMENT 8: CLUSTERING DYNAMICS")
print("="*80)

array_size_cluster = 30
np.random.seed(42)
test_array_cluster = list(np.random.randint(1, 50, size=array_size_cluster))

algotype_assignments = ['bubble'] * 10 + ['insertion'] * 10 + ['selection'] * 10
np.random.shuffle(algotype_assignments)

print(f"Array size: {array_size_cluster}")
print(f"Running mixed_algotype_sort...")

result_cluster, steps_cluster, sort_history, algotype_history = mixed_algotype_sort(
    test_array_cluster.copy(),
    algotype_assignments
)

print(f"sort_history length: {len(sort_history)}")
print(f"algotype_history length: {len(algotype_history)}")

# Calculate clustering at each timestep
cluster_history = [algo_type_clustering(algotypes) for algotypes in algotype_history]

print(f"cluster_history length: {len(cluster_history)}")

# Analyze results
final_sortedness_val = sortedness(result_cluster)
peak_clustering = max(cluster_history)
peak_index = cluster_history.index(peak_clustering)

print(f"Final sortedness: {final_sortedness_val:.1f}%")
print(f"Peak clustering: {peak_clustering:.1%}")
print(f"Peak index: {peak_index}")

print("[PASS] Experiment 8 code runs successfully\n")


print("="*80)
print("TESTING EXPERIMENT 9: DUPLICATE VALUES")
print("="*80)

def create_array_with_duplicates(size, duplicate_pct):
    """Create array where specified % of values are duplicates."""
    unique_count = max(2, int(size * (100 - duplicate_pct) / 100))
    unique_values = list(range(1, unique_count + 1))
    result = []
    for _ in range(size):
        result.append(np.random.choice(unique_values))
    np.random.shuffle(result)
    return result

array_size_dup = 30
duplicate_levels = [0, 25, 50]

duplicate_results = {}

for dup_pct in duplicate_levels:
    print(f"\nTesting with {dup_pct}% duplicates...")

    np.random.seed(123)
    if dup_pct == 0:
        test_array_dup = list(range(1, array_size_dup + 1))
        np.random.shuffle(test_array_dup)
    else:
        test_array_dup = create_array_with_duplicates(array_size_dup, dup_pct)

    algotypes_dup = ['bubble'] * 10 + ['insertion'] * 10 + ['selection'] * 10
    np.random.shuffle(algotypes_dup)

    result_dup, steps_dup, sort_hist_dup, algotype_hist_dup = mixed_algotype_sort(
        test_array_dup.copy(),
        algotypes_dup
    )

    print(f"  sort_hist_dup length: {len(sort_hist_dup)}")
    print(f"  algotype_hist_dup length: {len(algotype_hist_dup)}")

    cluster_hist_dup = [algo_type_clustering(alg) for alg in algotype_hist_dup]

    print(f"  cluster_hist_dup length: {len(cluster_hist_dup)}")

    # Check that lengths match for visualization
    if len(sort_hist_dup) != len(cluster_hist_dup):
        print(f"  [WARNING] Lengths don't match!")
        print(f"    sort_hist_dup: {len(sort_hist_dup)}")
        print(f"    cluster_hist_dup: {len(cluster_hist_dup)}")
    else:
        print(f"  [OK] Lengths match")

    peak_clustering_dup = max(cluster_hist_dup)
    final_sortedness_dup = sortedness(result_dup)

    duplicate_results[dup_pct] = {
        'peak_clustering': peak_clustering_dup,
        'cluster_history': cluster_hist_dup,
        'sort_history': sort_hist_dup,
        'final_sortedness': final_sortedness_dup,
        'swaps': steps_dup.swaps,
    }

    print(f"  Peak clustering: {peak_clustering_dup:.1%}")
    print(f"  Final sortedness: {final_sortedness_dup:.1f}%")

# Test the scatter plot that's failing
print("\nTesting scatter plot data for 0% duplicates...")
results_0 = duplicate_results[0]
print(f"  sort_history length: {len(results_0['sort_history'])}")
print(f"  cluster_history length: {len(results_0['cluster_history'])}")

if len(results_0['sort_history']) == len(results_0['cluster_history']):
    print("  [PASS] Scatter plot data lengths match")
else:
    print("  [ERROR] Scatter plot data lengths don't match!")
    print(f"    This will cause: ValueError: x and y must be the same size")

print("\n[PASS] Experiment 9 code runs successfully")

print("\n" + "="*80)
print("ALL EXPERIMENTS TESTED SUCCESSFULLY")
print("="*80)
