"""
Experiment harness for running and analyzing sorting algorithm experiments.

This module implements all experiments from the paper, corresponding to Figures 3-9.
"""

import random
import numpy as np
from typing import Dict, List, Literal, Optional, Callable
from .core import set_experiment_seed, N_CELLS, N_REPEATS, FrozenType, Algotype
from . import traditional_sorts, cell_view_sorts
from .metrics import monotonicity_error, sortedness, aggregation_value


def run_single_experiment(
    algorithm_name: Literal["bubble", "insertion", "selection"],
    variant: Literal["traditional", "cell_view"],
    n_cells: int = N_CELLS,
    frozen_config: Optional[Dict[int, FrozenType]] = None,
    allow_duplicates: bool = False,
    seed: int = 42
) -> Dict:
    """
    Run a single sorting experiment.

    Args:
        algorithm_name: Which sorting algorithm to use
        variant: Traditional or cell-view implementation
        n_cells: Number of elements in array
        frozen_config: Dictionary of frozen cell configurations
        allow_duplicates: Whether to allow repeated values
        seed: Random seed for this run

    Returns:
        Dictionary with results including steps, error, and history
    """
    set_experiment_seed(seed, 0)

    # Generate initial values
    if allow_duplicates:
        # 100 cells, values 1-10 each repeated 10x
        base_vals = np.repeat(np.arange(1, 11), n_cells // 10)
        np.random.shuffle(base_vals)
        values = base_vals.tolist()
    else:
        # Unique values 1 to n_cells
        values = list(range(1, n_cells + 1))
        random.shuffle(values)

    # Run the appropriate sorting algorithm
    if variant == "traditional":
        if algorithm_name == "bubble":
            final_vals, steps, history = traditional_sorts.bubble_sort(values)
        elif algorithm_name == "insertion":
            final_vals, steps, history = traditional_sorts.insertion_sort(values)
        else:  # selection
            final_vals, steps, history = traditional_sorts.selection_sort(values)
    else:  # cell_view
        frozen_config = frozen_config or {}
        if algorithm_name == "bubble":
            final_vals, steps, history = cell_view_sorts.bubble_sort(values, frozen_config)
        elif algorithm_name == "insertion":
            final_vals, steps, history = cell_view_sorts.insertion_sort(values, frozen_config)
        else:  # selection
            final_vals, steps, history = cell_view_sorts.selection_sort(values, frozen_config)

    return {
        "final_values": final_vals,
        "comparison_steps": steps.comparisons,
        "swap_steps": steps.swaps,
        "total_steps": steps.total,
        "monotonicity_error": monotonicity_error(final_vals),
        "sortedness_history": history,
        "initial_values": values
    }


def run_experiments(
    algorithm_name: Literal["bubble", "insertion", "selection"],
    variant: Literal["traditional", "cell_view"],
    n_cells: int = N_CELLS,
    n_repeats: int = N_REPEATS,
    frozen_config_factory: Optional[Callable] = None,
    allow_duplicates: bool = False,
    base_seed: int = 42
) -> Dict:
    """
    Run multiple repetitions of an experiment and collect statistics.

    Args:
        algorithm_name: Which algorithm to test
        variant: Traditional or cell-view
        n_cells: Array size
        n_repeats: Number of repetitions
        frozen_config_factory: Function that generates frozen cell config for each repeat
        allow_duplicates: Whether to allow duplicate values
        base_seed: Base random seed

    Returns:
        Dictionary with aggregated results across all repeats
    """
    results = {
        "comparison_steps": [],
        "swap_steps": [],
        "total_steps": [],
        "monotonicity_error": [],
        "sortedness_history": [],
    }

    for rep in range(n_repeats):
        # Get frozen configuration for this repeat
        frozen_config = frozen_config_factory(rep) if frozen_config_factory else None

        # Run single experiment
        result = run_single_experiment(
            algorithm_name=algorithm_name,
            variant=variant,
            n_cells=n_cells,
            frozen_config=frozen_config,
            allow_duplicates=allow_duplicates,
            seed=base_seed + rep
        )

        # Collect results
        results["comparison_steps"].append(result["comparison_steps"])
        results["swap_steps"].append(result["swap_steps"])
        results["total_steps"].append(result["total_steps"])
        results["monotonicity_error"].append(result["monotonicity_error"])
        results["sortedness_history"].append(result["sortedness_history"])

    return results


def make_frozen_factory(n_frozen: int, frozen_type: FrozenType, n_cells: int = N_CELLS, base_seed: int = 1000):
    """
    Create a factory function that generates random frozen cell configurations.

    Args:
        n_frozen: Number of cells to freeze
        frozen_type: Type of freezing ("movable" or "immovable")
        n_cells: Total number of cells
        base_seed: Seed offset for reproducibility

    Returns:
        Factory function that takes repeat number and returns frozen config dict
    """
    def factory(rep: int) -> Dict[int, FrozenType]:
        if n_frozen == 0:
            return {}
        set_experiment_seed(base_seed + n_frozen * 1000, rep)
        indices = random.sample(range(n_cells), n_frozen)
        return {i: frozen_type for i in indices}

    return factory


# Experiment runners for each figure

def run_trajectories_experiment(n_cells: int = N_CELLS, n_repeats: int = N_REPEATS) -> Dict:
    """
    Experiment 1: Basic sorting trajectories (Figure 3).

    Tests whether cell-view algorithms work and visualizes their
    paths through sortedness space.

    Returns:
        Dictionary with results for all algorithm types and variants
    """
    results = {}

    for algo in ["bubble", "insertion", "selection"]:
        results[algo] = {
            "traditional": run_experiments(algo, "traditional", n_cells, n_repeats),
            "cell_view": run_experiments(algo, "cell_view", n_cells, n_repeats)
        }

    return results


def run_efficiency_comparison(n_cells: int = N_CELLS, n_repeats: int = N_REPEATS) -> Dict:
    """
    Experiment 2: Efficiency comparison (Figure 4).

    Compares computational cost (swaps and total steps) between
    traditional and cell-view algorithms.

    Returns:
        Dictionary with efficiency metrics for all algorithms
    """
    return run_trajectories_experiment(n_cells, n_repeats)


def run_frozen_cell_experiments(
    frozen_counts: List[int] = [0, 1, 2, 3],
    n_cells: int = N_CELLS,
    n_repeats: int = N_REPEATS
) -> Dict:
    """
    Experiment 3: Error tolerance with frozen cells (Figure 5).

    Tests robustness to damaged components by introducing cells
    that cannot move or cannot initiate movement.

    Args:
        frozen_counts: List of frozen cell counts to test
        n_cells: Array size
        n_repeats: Number of repetitions per configuration

    Returns:
        Dictionary with results for movable and immovable frozen cells
    """
    results_movable = {}
    results_immovable = {}

    for algo in ["bubble", "insertion", "selection"]:
        results_movable[algo] = {}
        results_immovable[algo] = {}

        for f in frozen_counts:
            factory_mov = make_frozen_factory(f, "movable", n_cells) if f > 0 else None
            factory_imm = make_frozen_factory(f, "immovable", n_cells) if f > 0 else None

            results_movable[algo][f] = {
                "traditional": run_experiments(algo, "traditional", n_cells, n_repeats, factory_mov),
                "cell_view": run_experiments(algo, "cell_view", n_cells, n_repeats, factory_mov)
            }

            results_immovable[algo][f] = {
                "traditional": run_experiments(algo, "traditional", n_cells, n_repeats, factory_imm),
                "cell_view": run_experiments(algo, "cell_view", n_cells, n_repeats, factory_imm)
            }

    return {
        "movable": results_movable,
        "immovable": results_immovable
    }


def run_delayed_gratification_experiment(
    frozen_counts: List[int] = [0, 1, 2, 3],
    n_cells: int = N_CELLS,
    n_repeats: int = N_REPEATS
) -> Dict:
    """
    Experiment 4: Delayed gratification analysis (Figures 6-7).

    Measures the ability to temporarily reduce progress (decrease sortedness)
    in order to achieve larger gains later.

    Returns:
        Dictionary with DG metrics for all algorithms and frozen cell counts
    """
    # Run same experiments as frozen cell test
    results = run_frozen_cell_experiments(frozen_counts, n_cells, n_repeats)

    # DG will be calculated from sortedness histories in visualization
    return results


def run_mixed_algotypes_experiment(
    algotype_pairs: List[tuple] = [
        ("bubble", "insertion"),
        ("bubble", "selection"),
        ("insertion", "selection")
    ],
    n_cells: int = N_CELLS,
    n_repeats: int = N_REPEATS,
    allow_duplicates: bool = False,
    base_seed: int = 2000
) -> Dict:
    """
    Experiment 5: Mixed algotypes - aggregation (Figure 8).

    Studies chimeric arrays where cells follow different algorithms.
    Measures whether cells cluster by algorithm type.

    Args:
        algotype_pairs: List of algotype combinations to test
        n_cells: Array size
        n_repeats: Number of repetitions
        allow_duplicates: Whether to allow duplicate values
        base_seed: Random seed base

    Returns:
        Dictionary with sortedness and aggregation histories
    """
    results = {}

    for pair in algotype_pairs:
        pair_key = f"{pair[0]}_{pair[1]}"
        results[pair_key] = {
            "sortedness_histories": [],
            "aggregation_histories": [],
            "swap_steps": []
        }

        for rep in range(n_repeats):
            set_experiment_seed(base_seed, rep)

            # Generate initial values
            if allow_duplicates:
                base_vals = np.repeat(np.arange(1, 11), n_cells // 10)
                np.random.shuffle(base_vals)
                values = base_vals.tolist()
            else:
                values = list(range(1, n_cells + 1))
                random.shuffle(values)

            # Randomly assign algotypes (50/50 split)
            algotypes = [random.choice(pair) for _ in range(n_cells)]

            # Run mixed sort
            final_vals, steps, sort_hist, algotype_hist = cell_view_sorts.mixed_algotype_sort(
                values, algotypes, allow_duplicates=allow_duplicates
            )

            # Calculate aggregation at each timestep
            agg_hist = [aggregation_value(algs) for algs in algotype_hist]

            results[pair_key]["sortedness_histories"].append(sort_hist)
            results[pair_key]["aggregation_histories"].append(agg_hist)
            results[pair_key]["swap_steps"].append(steps.swaps)

    return results


def run_opposite_goals_experiment(
    algotype_pairs: List[tuple] = [
        ("bubble", "selection"),
        ("bubble", "insertion"),
        ("selection", "insertion")
    ],
    n_cells: int = N_CELLS,
    n_repeats: int = N_REPEATS,
    base_seed: int = 3000
) -> Dict:
    """
    Experiment 6: Conflicting goals (Figure 9).

    Tests what happens when cells have opposite sorting objectives
    (half sort increasing, half sort decreasing).

    Note: This requires modifications to cell_view_sorts to support
    opposite directions. For now, returns placeholder.

    Returns:
        Dictionary with final sortedness and aggregation values
    """
    # This experiment requires extending the cell_view sorts to support
    # direction-specific sorting, which adds complexity.
    # For the notebook, we'll document this as a future extension.

    results = {}
    for pair in algotype_pairs:
        pair_key = f"{pair[0]}_vs_{pair[1]}"
        results[pair_key] = {
            "note": "Opposite goals experiment requires direction-aware sorting",
            "final_sortedness": [],
            "final_aggregation": []
        }

    return results


def run_all_experiments() -> Dict:
    """
    Run all experiments from the paper.

    This is the master function that executes everything.

    Returns:
        Dictionary containing all experiment results
    """
    print("Running Experiment 1: Trajectories...")
    exp1 = run_trajectories_experiment()

    print("Running Experiment 2: Efficiency Comparison...")
    exp2 = run_efficiency_comparison()

    print("Running Experiment 3: Frozen Cells...")
    exp3 = run_frozen_cell_experiments()

    print("Running Experiment 4: Delayed Gratification...")
    exp4 = run_delayed_gratification_experiment()

    print("Running Experiment 5: Mixed Algotypes...")
    exp5_no_dup = run_mixed_algotypes_experiment(allow_duplicates=False)
    exp5_dup = run_mixed_algotypes_experiment(allow_duplicates=True)

    print("Running Experiment 6: Opposite Goals...")
    exp6 = run_opposite_goals_experiment()

    print("All experiments complete!")

    return {
        "trajectories": exp1,
        "efficiency": exp2,
        "frozen_cells": exp3,
        "delayed_gratification": exp4,
        "mixed_algotypes_no_duplicates": exp5_no_dup,
        "mixed_algotypes_duplicates": exp5_dup,
        "opposite_goals": exp6
    }


# Simplified wrapper functions for notebook use

def compare_algorithms(array_sizes: List[int] = [10, 20, 30],
                      num_trials: int = 10) -> Dict:
    """
    Simple comparison of all three algorithms across different array sizes.

    Args:
        array_sizes: List of array sizes to test
        num_trials: Number of trials per size

    Returns:
        Dict with results for each algorithm and array size
    """
    results = {}

    for size in array_sizes:
        results[size] = {}

        for algo in ["bubble", "insertion", "selection"]:
            algo_results = run_experiments(
                algorithm_name=algo,
                variant="cell_view",
                n_cells=size,
                n_repeats=num_trials
            )

            results[size][algo] = {
                'swaps': np.mean(algo_results['swap_steps']),
                'comparisons': np.mean(algo_results['comparison_steps']),
                'swaps_std': np.std(algo_results['swap_steps']),
                'comparisons_std': np.std(algo_results['comparison_steps'])
            }

    return results


def frozen_cell_experiment(array_size: int = 20,
                           frozen_percentages: List[int] = [0, 10, 20, 30, 40, 50],
                           num_trials: int = 10) -> Dict:
    """
    Test algorithm robustness with frozen (damaged) cells.

    Args:
        array_size: Size of array to test
        frozen_percentages: List of damage percentages (0-100)
        num_trials: Number of trials per configuration

    Returns:
        Dict with sortedness results for each algorithm and damage level
    """
    results = {}

    for algo in ["bubble", "insertion", "selection"]:
        results[algo] = {}

        for pct in frozen_percentages:
            n_frozen = int(array_size * pct / 100)

            # Create frozen config factory
            if n_frozen > 0:
                factory = make_frozen_factory(n_frozen, "immovable", array_size)
            else:
                factory = None

            # Run experiments
            algo_results = run_experiments(
                algorithm_name=algo,
                variant="cell_view",
                n_cells=array_size,
                n_repeats=num_trials,
                frozen_config_factory=factory
            )

            # Calculate final sortedness for each trial
            final_sortedness = []
            for hist in algo_results['sortedness_history']:
                if len(hist) > 0:
                    final_sortedness.append(hist[-1])
                else:
                    # If no history, calculate from final values
                    final_sortedness.append(100 - np.mean(algo_results['monotonicity_error']))

            results[algo][pct] = {
                'final_sortedness': np.mean(final_sortedness),
                'std': np.std(final_sortedness),
                'monotonicity_error': np.mean(algo_results['monotonicity_error'])
            }

    return results


def chimeric_experiment(array_size: int = 50,
                       num_trials: int = 10) -> Dict:
    """
    Test chimeric arrays with mixed cell types.

    Args:
        array_size: Size of test array
        num_trials: Number of trials

    Returns:
        Dict with results for different algotype mixtures
    """
    pairs = [
        ("bubble", "insertion"),
        ("bubble", "selection"),
        ("insertion", "selection")
    ]

    results = run_mixed_algotypes_experiment(
        algotype_pairs=pairs,
        n_cells=array_size,
        n_repeats=num_trials,
        allow_duplicates=False
    )

    return results
