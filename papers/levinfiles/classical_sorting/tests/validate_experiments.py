#!/usr/bin/env python3
"""
Comprehensive validation script for morphogenesis sorting experiments.

This script tests all implementations against the expected results from the paper:
"Classical Sorting Algorithms as a Model of Morphogenesis" (Zhang et al., 2024)

Usage:
    poetry run python validate_experiments.py
    poetry run python validate_experiments.py --quick  # Use smaller N for faster testing
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import sys
import argparse
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple
import json

from modules.core import N_CELLS, N_REPEATS
from modules.experiments import (
    run_experiments,
    run_frozen_cell_experiments,
    run_mixed_algotypes_experiment,
)
from modules.metrics import compute_delayed_gratification


class ValidationResults:
    """Store and format validation results."""

    def __init__(self):
        self.results = {}
        self.timestamp = datetime.now().isoformat()

    def add_experiment(self, name: str, data: Dict):
        """Add results for an experiment."""
        self.results[name] = data

    def save_json(self, filepath: str):
        """Save results as JSON."""
        output = {
            'timestamp': self.timestamp,
            'results': self.results
        }
        with open(filepath, 'w') as f:
            json.dump(output, f, indent=2)

    def print_summary(self):
        """Print a summary of all results."""
        print("\n" + "="*80)
        print("VALIDATION SUMMARY")
        print("="*80)
        print(f"Timestamp: {self.timestamp}")
        print(f"Experiments completed: {len(self.results)}")
        print("="*80 + "\n")


def validate_experiment_1(n_cells: int = 20, n_repeats: int = 10) -> Dict:
    """
    Experiment 1: Basic Sorting Trajectories (Figure 3)

    Validates that all algorithms successfully sort arrays to 100% sortedness.
    """
    print("\n" + "="*80)
    print("EXPERIMENT 1: Basic Sorting Trajectories")
    print("="*80)
    print(f"Parameters: N={n_cells}, Repeats={n_repeats}")
    print()

    results = {}

    for algo in ["bubble", "insertion", "selection"]:
        print(f"Testing {algo.capitalize()} Sort...")

        # Traditional
        trad_results = run_experiments(
            algorithm_name=algo,
            variant="traditional",
            n_cells=n_cells,
            n_repeats=n_repeats
        )

        # Cell-view
        cell_results = run_experiments(
            algorithm_name=algo,
            variant="cell_view",
            n_cells=n_cells,
            n_repeats=n_repeats
        )

        # Calculate statistics
        trad_swaps_mean = np.mean(trad_results['swap_steps'])
        trad_swaps_std = np.std(trad_results['swap_steps'])
        cell_swaps_mean = np.mean(cell_results['swap_steps'])
        cell_swaps_std = np.std(cell_results['swap_steps'])

        trad_error_mean = np.mean(trad_results['monotonicity_error'])
        cell_error_mean = np.mean(cell_results['monotonicity_error'])

        # Check final sortedness
        trad_final_sortedness = []
        cell_final_sortedness = []

        for hist in trad_results['sortedness_history']:
            if len(hist) > 0:
                trad_final_sortedness.append(hist[-1])
            else:
                trad_final_sortedness.append(100.0 - trad_error_mean)

        for hist in cell_results['sortedness_history']:
            if len(hist) > 0:
                cell_final_sortedness.append(hist[-1])
            else:
                cell_final_sortedness.append(100.0 - cell_error_mean)

        trad_sort_mean = np.mean(trad_final_sortedness)
        cell_sort_mean = np.mean(cell_final_sortedness)

        results[algo] = {
            'traditional': {
                'swaps': {'mean': float(trad_swaps_mean), 'std': float(trad_swaps_std)},
                'final_sortedness': {'mean': float(trad_sort_mean), 'values': trad_final_sortedness},
                'monotonicity_error': float(trad_error_mean),
                'success': trad_sort_mean >= 99.0
            },
            'cell_view': {
                'swaps': {'mean': float(cell_swaps_mean), 'std': float(cell_swaps_std)},
                'final_sortedness': {'mean': float(cell_sort_mean), 'values': cell_final_sortedness},
                'monotonicity_error': float(cell_error_mean),
                'success': cell_sort_mean >= 99.0
            }
        }

        # Print results
        print(f"  Traditional: {trad_sort_mean:.1f}% sortedness, {trad_swaps_mean:.0f} ± {trad_swaps_std:.0f} swaps")
        print(f"  Cell-view:   {cell_sort_mean:.1f}% sortedness, {cell_swaps_mean:.0f} ± {cell_swaps_std:.0f} swaps")

        # Validation
        if trad_sort_mean >= 99.0 and cell_sort_mean >= 99.0:
            print(f"  [PASS] Both reach >99% sortedness")
        else:
            print(f"  [FAIL] Sortedness below threshold")
        print()

    return results


def validate_experiment_2(n_cells: int = 20, n_repeats: int = 10) -> Dict:
    """
    Experiment 2: Efficiency Comparison (Figure 4)

    Compares computational cost between traditional and cell-view algorithms.
    Expected: Selection sort cell-view uses ~11x more swaps than traditional.
    """
    print("\n" + "="*80)
    print("EXPERIMENT 2: Efficiency Comparison")
    print("="*80)
    print(f"Parameters: N={n_cells}, Repeats={n_repeats}")
    print()

    results = {}

    for algo in ["bubble", "insertion", "selection"]:
        print(f"Testing {algo.capitalize()} Sort...")

        # Traditional
        trad_results = run_experiments(
            algorithm_name=algo,
            variant="traditional",
            n_cells=n_cells,
            n_repeats=n_repeats
        )

        # Cell-view
        cell_results = run_experiments(
            algorithm_name=algo,
            variant="cell_view",
            n_cells=n_cells,
            n_repeats=n_repeats
        )

        # Calculate statistics
        trad_swaps = np.mean(trad_results['swap_steps'])
        trad_swaps_std = np.std(trad_results['swap_steps'])
        cell_swaps = np.mean(cell_results['swap_steps'])
        cell_swaps_std = np.std(cell_results['swap_steps'])

        trad_total = np.mean(trad_results['total_steps'])
        trad_total_std = np.std(trad_results['total_steps'])
        cell_total = np.mean(cell_results['total_steps'])
        cell_total_std = np.std(cell_results['total_steps'])

        # Calculate ratio
        swap_ratio = cell_swaps / trad_swaps if trad_swaps > 0 else 0

        results[algo] = {
            'traditional': {
                'swaps': {'mean': float(trad_swaps), 'std': float(trad_swaps_std)},
                'total': {'mean': float(trad_total), 'std': float(trad_total_std)}
            },
            'cell_view': {
                'swaps': {'mean': float(cell_swaps), 'std': float(cell_swaps_std)},
                'total': {'mean': float(cell_total), 'std': float(cell_total_std)}
            },
            'swap_ratio': float(swap_ratio)
        }

        # Print results
        print(f"  SWAPS:")
        print(f"    Traditional: {trad_swaps:.0f} ± {trad_swaps_std:.0f}")
        print(f"    Cell-view:   {cell_swaps:.0f} ± {cell_swaps_std:.0f}")
        print(f"    Ratio:       {swap_ratio:.2f}x")
        print(f"  TOTAL STEPS:")
        print(f"    Traditional: {trad_total:.0f} ± {trad_total_std:.0f}")
        print(f"    Cell-view:   {cell_total:.0f} ± {cell_total_std:.0f}")

        # Validation
        if algo == "selection":
            # Selection sort should have ~11x ratio
            if 8.0 <= swap_ratio <= 14.0:
                print(f"  [PASS] PASS: Swap ratio within expected range (10-12x)")
            else:
                print(f"  [WARN]  WARNING: Swap ratio outside expected range (expected ~11x, got {swap_ratio:.2f}x)")
        else:
            # Bubble and Insertion should be nearly equal
            if swap_ratio <= 1.5:
                print(f"  [PASS] PASS: Swap counts similar (ratio {swap_ratio:.2f}x)")
            else:
                print(f"  [WARN]  WARNING: Large swap ratio difference ({swap_ratio:.2f}x)")
        print()

    return results


def validate_experiment_3(n_cells: int = 20, n_repeats: int = 10) -> Dict:
    """
    Experiment 3: Frozen Cells - Error Tolerance (Figure 5)

    Tests robustness to damaged components.
    """
    print("\n" + "="*80)
    print("EXPERIMENT 3: Frozen Cells - Error Tolerance")
    print("="*80)
    print(f"Parameters: N={n_cells}, Repeats={n_repeats}")
    print()

    frozen_counts = [0, 1, 2, 3]

    results = run_frozen_cell_experiments(
        frozen_counts=frozen_counts,
        n_cells=n_cells,
        n_repeats=n_repeats
    )

    # Print results for immovable frozen cells
    print("IMMOVABLE FROZEN CELLS:")
    print(f"{'Algorithm':<12} " + " ".join(f"{f:>8}" for f in frozen_counts))
    print("-" * 60)

    for algo in ["bubble", "insertion", "selection"]:
        errors = []
        for f in frozen_counts:
            error = np.mean(results['immovable'][algo][f]['cell_view']['monotonicity_error'])
            errors.append(error)

        print(f"{algo.capitalize():<12} " + " ".join(f"{e:>8.2f}" for e in errors))

    print()

    # Validation
    all_pass = True
    for algo in ["bubble", "insertion", "selection"]:
        zero_frozen_error = np.mean(results['immovable'][algo][0]['cell_view']['monotonicity_error'])
        if zero_frozen_error > 1.0:
            print(f"  [FAIL] FAIL: {algo} has error > 1.0 with 0 frozen cells")
            all_pass = False

    if all_pass:
        print(f"  [PASS] PASS: All algorithms work correctly with 0 frozen cells")

    return {
        'immovable': results['immovable'],
        'movable': results['movable']
    }


def validate_experiment_4(frozen_results: Dict, n_cells: int = 20) -> Dict:
    """
    Experiment 4: Delayed Gratification (Figures 6-7)

    Measures ability to temporarily decrease sortedness.
    """
    print("\n" + "="*80)
    print("EXPERIMENT 4: Delayed Gratification")
    print("="*80)
    print(f"Parameters: N={n_cells}")
    print()

    frozen_counts = [0, 1, 2, 3]
    results = {}

    print("DELAYED GRATIFICATION (% of decreasing steps):")
    print(f"{'Algorithm':<12} " + " ".join(f"{f:>8}" for f in frozen_counts))
    print("-" * 60)

    for algo in ["bubble", "insertion", "selection"]:
        results[algo] = {}
        dg_values = []

        for f in frozen_counts:
            # Calculate DG for cell-view variant
            histories = frozen_results['immovable'][algo][f]['cell_view']['sortedness_history']
            dg_vals = [compute_delayed_gratification(h) for h in histories if len(h) > 0]

            if dg_vals:
                mean_dg = np.mean(dg_vals)
                results[algo][f] = float(mean_dg)
                dg_values.append(mean_dg * 100)  # Convert to percentage
            else:
                results[algo][f] = 0.0
                dg_values.append(0.0)

        print(f"{algo.capitalize():<12} " + " ".join(f"{dg:>7.2f}%" for dg in dg_values))

    print()

    # Validation
    bubble_dg = results['bubble'][0]
    insertion_dg = results['insertion'][0]
    selection_dg = results['selection'][0]

    if bubble_dg > 0 and insertion_dg > 0:
        print(f"  [PASS] PASS: Bubble and Insertion show delayed gratification")
    else:
        print(f"  [WARN]  WARNING: Bubble or Insertion not showing DG")

    if selection_dg < 0.05:
        print(f"  [PASS] PASS: Selection shows minimal delayed gratification")
    else:
        print(f"  [WARN]  NOTE: Selection DG higher than expected ({selection_dg*100:.2f}%)")

    return results


def validate_experiment_5(n_cells: int = 20, n_repeats: int = 10) -> Dict:
    """
    Experiment 5: Mixed Algotypes - Aggregation (Figure 8)

    Tests chimeric arrays with mixed cell types.
    """
    print("\n" + "="*80)
    print("EXPERIMENT 5: Mixed Algotypes - Aggregation")
    print("="*80)
    print(f"Parameters: N={n_cells}, Repeats={n_repeats}")
    print()

    algotype_pairs = [
        ("bubble", "insertion"),
        ("bubble", "selection"),
        ("insertion", "selection")
    ]

    results = run_mixed_algotypes_experiment(
        algotype_pairs=algotype_pairs,
        n_cells=n_cells,
        n_repeats=n_repeats,
        allow_duplicates=False
    )

    print(f"{'Pair':<25} {'Sortedness':<12} {'Init Agg':<10} {'Final Agg':<10} {'Swaps':<10}")
    print("-" * 75)

    validation_results = {}

    for pair in algotype_pairs:
        pair_key = f"{pair[0]}_{pair[1]}"
        data = results[pair_key]

        # Calculate final sortedness
        final_sortedness = []
        for hist in data['sortedness_histories']:
            if len(hist) > 0:
                final_sortedness.append(hist[-1])

        mean_sortedness = np.mean(final_sortedness) if final_sortedness else 0

        # Calculate aggregation
        initial_agg = []
        final_agg = []
        for agg_hist in data['aggregation_histories']:
            if len(agg_hist) > 0:
                initial_agg.append(agg_hist[0])
                final_agg.append(agg_hist[-1])

        mean_initial_agg = np.mean(initial_agg) if initial_agg else 0
        mean_final_agg = np.mean(final_agg) if final_agg else 0
        mean_swaps = np.mean(data['swap_steps'])

        validation_results[pair_key] = {
            'final_sortedness': float(mean_sortedness),
            'initial_aggregation': float(mean_initial_agg),
            'final_aggregation': float(mean_final_agg),
            'swaps': float(mean_swaps)
        }

        pair_name = f"{pair[0].capitalize()} + {pair[1].capitalize()}"
        print(f"{pair_name:<25} {mean_sortedness:>10.1f}% {mean_initial_agg:>9.1f}% {mean_final_agg:>9.1f}% {mean_swaps:>10.0f}")

    print()

    # Validation
    all_pass = True
    for pair_key, data in validation_results.items():
        if data['final_sortedness'] < 95.0:
            print(f"  [FAIL] FAIL: {pair_key} sortedness below 95%")
            all_pass = False
        if data['final_aggregation'] < 50.0:
            print(f"  [WARN]  WARNING: {pair_key} aggregation below 50%")

    if all_pass:
        print(f"  [PASS] PASS: All chimeric arrays successfully sort")

    return validation_results


def main():
    """Run all validation experiments."""
    parser = argparse.ArgumentParser(description='Validate morphogenesis sorting experiments')
    parser.add_argument('--quick', action='store_true',
                       help='Use smaller parameters for faster testing (N=20, R=10)')
    parser.add_argument('--full', action='store_true',
                       help='Use full paper parameters (N=100, R=100) - SLOW!')
    parser.add_argument('--output', type=str, default='validation_results.json',
                       help='Output JSON file for results')
    args = parser.parse_args()

    # Set parameters
    if args.full:
        n_cells = N_CELLS  # 100
        n_repeats = N_REPEATS  # 100
        print("Running FULL validation (N=100, R=100) - This will take a long time!")
    elif args.quick:
        n_cells = 20
        n_repeats = 10
        print("Running QUICK validation (N=20, R=10)")
    else:
        # Default: medium
        n_cells = 50
        n_repeats = 20
        print("Running STANDARD validation (N=50, R=20)")

    print(f"Results will be saved to: {args.output}")
    print("=" * 80)

    # Initialize results tracker
    tracker = ValidationResults()

    try:
        # Experiment 1: Basic trajectories
        exp1_results = validate_experiment_1(n_cells, n_repeats)
        tracker.add_experiment("experiment_1_trajectories", exp1_results)

        # Experiment 2: Efficiency comparison
        exp2_results = validate_experiment_2(n_cells, n_repeats)
        tracker.add_experiment("experiment_2_efficiency", exp2_results)

        # Experiment 3: Frozen cells
        exp3_results = validate_experiment_3(n_cells, n_repeats)
        tracker.add_experiment("experiment_3_frozen_cells", exp3_results)

        # Experiment 4: Delayed gratification (uses exp3 results)
        exp4_results = validate_experiment_4(exp3_results, n_cells)
        tracker.add_experiment("experiment_4_delayed_gratification", exp4_results)

        # Experiment 5: Mixed algotypes
        exp5_results = validate_experiment_5(n_cells, n_repeats)
        tracker.add_experiment("experiment_5_mixed_algotypes", exp5_results)

        # Save results
        tracker.save_json(args.output)
        print(f"\n[PASS] Results saved to {args.output}")

        # Print summary
        tracker.print_summary()

        print("\n" + "="*80)
        print("VALIDATION COMPLETE")
        print("="*80)
        print(f"Please check {args.output} for detailed results")
        print("Update VALIDATION_TRACKER.md with the results from this run")
        print("="*80 + "\n")

    except KeyboardInterrupt:
        print("\n\n[WARN]  Validation interrupted by user")
        print("Partial results saved to:", args.output)
        tracker.save_json(args.output)
        sys.exit(1)
    except Exception as e:
        print(f"\n\n[FAIL] ERROR during validation: {e}")
        import traceback
        traceback.print_exc()
        print("\nPartial results saved to:", args.output)
        tracker.save_json(args.output)
        sys.exit(1)


if __name__ == "__main__":
    main()
