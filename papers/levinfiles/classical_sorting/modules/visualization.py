"""
Visualization functions for sorting algorithm experiments.

This module provides plotting functions for all figures in the paper.
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List
from .metrics import compute_delayed_gratification


def plot_trajectories(results: Dict, title: str, color: str = 'blue', alpha: float = 0.2):
    """
    Plot sortedness trajectories (Figure 3 style).

    Shows multiple runs as semi-transparent lines showing the path
    through "sortedness space" over the course of the sorting process.

    Args:
        results: Dictionary with 'sortedness_history' key
        title: Plot title
        color: Line color
        alpha: Transparency level
    """
    plt.figure(figsize=(8, 5))

    for history in results["sortedness_history"]:
        if len(history) > 0:
            plt.plot(range(len(history)), history, color=color, alpha=alpha, linewidth=0.5)

    plt.xlabel("Swap Steps", fontsize=12)
    plt.ylabel("Sortedness (%)", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_trajectories_comparison(results_dict: Dict, algorithm_name: str):
    """
    Plot traditional vs cell-view trajectories side by side.

    Args:
        results_dict: Dictionary with 'traditional' and 'cell_view' keys
        algorithm_name: Name of algorithm for title
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Traditional
    for history in results_dict["traditional"]["sortedness_history"]:
        if len(history) > 0:
            ax1.plot(range(len(history)), history, color='steelblue', alpha=0.2, linewidth=0.5)

    ax1.set_xlabel("Swap Steps", fontsize=11)
    ax1.set_ylabel("Sortedness (%)", fontsize=11)
    ax1.set_title(f"Traditional {algorithm_name.capitalize()} Sort", fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 105)
    ax1.grid(True, alpha=0.3)

    # Cell-view
    for history in results_dict["cell_view"]["sortedness_history"]:
        if len(history) > 0:
            ax2.plot(range(len(history)), history, color='coral', alpha=0.2, linewidth=0.5)

    ax2.set_xlabel("Swap Steps", fontsize=11)
    ax2.set_ylabel("Sortedness (%)", fontsize=11)
    ax2.set_title(f"Cell-View {algorithm_name.capitalize()} Sort", fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 105)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def plot_efficiency_comparison(results: Dict):
    """
    Plot efficiency comparison bar charts (Figure 4 style).

    Shows swap steps and total steps for traditional vs cell-view.

    Args:
        results: Dictionary with algorithm results
    """
    algorithms = ["bubble", "insertion", "selection"]

    # Calculate statistics
    swap_trad = [np.mean(results[algo]["traditional"]["swap_steps"]) for algo in algorithms]
    swap_cell = [np.mean(results[algo]["cell_view"]["swap_steps"]) for algo in algorithms]
    swap_trad_std = [np.std(results[algo]["traditional"]["swap_steps"]) for algo in algorithms]
    swap_cell_std = [np.std(results[algo]["cell_view"]["swap_steps"]) for algo in algorithms]

    total_trad = [np.mean(results[algo]["traditional"]["total_steps"]) for algo in algorithms]
    total_cell = [np.mean(results[algo]["cell_view"]["total_steps"]) for algo in algorithms]
    total_trad_std = [np.std(results[algo]["traditional"]["total_steps"]) for algo in algorithms]
    total_cell_std = [np.std(results[algo]["cell_view"]["total_steps"]) for algo in algorithms]

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    x = np.arange(len(algorithms))
    width = 0.35

    # Swap steps only
    ax1.bar(x - width/2, swap_trad, width, label='Traditional', color='steelblue', yerr=swap_trad_std, capsize=5)
    ax1.bar(x + width/2, swap_cell, width, label='Cell-View', color='coral', yerr=swap_cell_std, capsize=5)
    ax1.set_ylabel('Swapping Steps', fontsize=11)
    ax1.set_title('Efficiency Comparison (A): Swap Steps Only', fontsize=12, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels([a.capitalize() for a in algorithms])
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')

    # Total steps
    ax2.bar(x - width/2, total_trad, width, label='Traditional', color='steelblue', yerr=total_trad_std, capsize=5)
    ax2.bar(x + width/2, total_cell, width, label='Cell-View', color='coral', yerr=total_cell_std, capsize=5)
    ax2.set_ylabel('Total Steps (Comparisons + Swaps)', fontsize=11)
    ax2.set_title('Efficiency Comparison (B): Total Steps', fontsize=12, fontweight='bold')
    ax2.set_xticks(x)
    ax2.set_xticklabels([a.capitalize() for a in algorithms])
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.show()


def plot_error_tolerance(results: Dict, frozen_type: str = "movable"):
    """
    Plot error tolerance with frozen cells (Figure 5 style).

    Args:
        results: Dictionary with frozen cell experiment results
        frozen_type: "movable" or "immovable"
    """
    algorithms = ["bubble", "insertion", "selection"]
    frozen_counts = [0, 1, 2, 3]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for idx, algo in enumerate(algorithms):
        ax = axes[idx]

        trad_errors = []
        cell_errors = []
        trad_stds = []
        cell_stds = []

        for f in frozen_counts:
            trad_err = results[frozen_type][algo][f]["traditional"]["monotonicity_error"]
            cell_err = results[frozen_type][algo][f]["cell_view"]["monotonicity_error"]

            trad_errors.append(np.mean(trad_err))
            cell_errors.append(np.mean(cell_err))
            trad_stds.append(np.std(trad_err))
            cell_stds.append(np.std(cell_err))

        x = np.arange(len(frozen_counts))
        width = 0.35

        ax.bar(x - width/2, trad_errors, width, label='Traditional', color='steelblue', yerr=trad_stds, capsize=5)
        ax.bar(x + width/2, cell_errors, width, label='Cell-View', color='coral', yerr=cell_stds, capsize=5)

        ax.set_xlabel('Number of Frozen Cells', fontsize=10)
        ax.set_ylabel('Monotonicity Error', fontsize=10)
        ax.set_title(f'{algo.capitalize()} Sort', fontsize=11, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(frozen_counts)
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')

    fig.suptitle(f'Error Tolerance with {frozen_type.capitalize()} Frozen Cells', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_delayed_gratification(results: Dict, frozen_type: str = "movable"):
    """
    Plot delayed gratification vs frozen cell count (Figure 7 style).

    Args:
        results: Dictionary with frozen cell experiment results
        frozen_type: "movable" or "immovable"
    """
    algorithms = ["bubble", "insertion", "selection"]
    frozen_counts = [0, 1, 2, 3]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for idx, algo in enumerate(algorithms):
        ax = axes[idx]

        trad_dgs = []
        cell_dgs = []
        trad_stds = []
        cell_stds = []

        for f in frozen_counts:
            # Calculate DG for traditional
            trad_histories = results[frozen_type][algo][f]["traditional"]["sortedness_history"]
            trad_dg_vals = [compute_delayed_gratification(h) for h in trad_histories if len(h) > 0]

            # Calculate DG for cell-view
            cell_histories = results[frozen_type][algo][f]["cell_view"]["sortedness_history"]
            cell_dg_vals = [compute_delayed_gratification(h) for h in cell_histories if len(h) > 0]

            trad_dgs.append(np.mean(trad_dg_vals) if trad_dg_vals else 0)
            cell_dgs.append(np.mean(cell_dg_vals) if cell_dg_vals else 0)
            trad_stds.append(np.std(trad_dg_vals) if trad_dg_vals else 0)
            cell_stds.append(np.std(cell_dg_vals) if cell_dg_vals else 0)

        x = np.arange(len(frozen_counts))
        width = 0.35

        ax.bar(x - width/2, trad_dgs, width, label='Traditional', color='steelblue', yerr=trad_stds, capsize=5)
        ax.bar(x + width/2, cell_dgs, width, label='Cell-View', color='coral', yerr=cell_stds, capsize=5)

        ax.set_xlabel('Number of Frozen Cells', fontsize=10)
        ax.set_ylabel('Delayed Gratification', fontsize=10)
        ax.set_title(f'{algo.capitalize()} Sort', fontsize=11, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(frozen_counts)
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')

    fig.suptitle('Delayed Gratification vs Frozen Cell Count', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_aggregation(results: Dict, pair_key: str):
    """
    Plot aggregation and sortedness for mixed algotypes (Figure 8 style).

    Args:
        results: Mixed algotype experiment results
        pair_key: Key for the algotype pair (e.g., "bubble_selection")
    """
    data = results[pair_key]

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot sortedness histories
    for sort_hist in data["sortedness_histories"]:
        if len(sort_hist) > 0:
            # Normalize x-axis to percentage of completion
            x_norm = np.linspace(0, 100, len(sort_hist))
            ax1.plot(x_norm, sort_hist, color='steelblue', alpha=0.1, linewidth=0.5)

    ax1.set_xlabel('Sorting Progress (%)', fontsize=12)
    ax1.set_ylabel('Sortedness (%)', fontsize=12, color='steelblue')
    ax1.tick_params(axis='y', labelcolor='steelblue')
    ax1.set_ylim(0, 105)

    # Plot aggregation histories on secondary axis
    ax2 = ax1.twinx()

    for agg_hist in data["aggregation_histories"]:
        if len(agg_hist) > 0:
            x_norm = np.linspace(0, 100, len(agg_hist))
            ax2.plot(x_norm, agg_hist, color='coral', alpha=0.1, linewidth=0.5)

    ax2.set_ylabel('Aggregation Value (%)', fontsize=12, color='coral')
    ax2.tick_params(axis='y', labelcolor='coral')
    ax2.set_ylim(0, 105)

    # Calculate and plot mean aggregation
    max_len = max(len(h) for h in data["aggregation_histories"])
    mean_agg = []
    for i in range(max_len):
        vals = [h[i] for h in data["aggregation_histories"] if i < len(h)]
        mean_agg.append(np.mean(vals))

    x_norm_mean = np.linspace(0, 100, len(mean_agg))
    ax2.plot(x_norm_mean, mean_agg, color='darkred', linewidth=2.5, label='Mean Aggregation')
    ax2.legend(loc='upper right')

    plt.title(f'Mixed Algotypes: {pair_key.replace("_", " + ").title()}', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


def plot_summary_statistics(results: Dict):
    """
    Create a comprehensive summary figure with key statistics.

    Args:
        results: All experiment results
    """
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3)

    # This would create a comprehensive dashboard
    # For brevity, showing structure only
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.text(0.5, 0.5, 'Efficiency Summary', ha='center', va='center', fontsize=14)
    ax1.axis('off')

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.text(0.5, 0.5, 'Error Tolerance Summary', ha='center', va='center', fontsize=14)
    ax2.axis('off')

    ax3 = fig.add_subplot(gs[0, 2])
    ax3.text(0.5, 0.5, 'Delayed Gratification Summary', ha='center', va='center', fontsize=14)
    ax3.axis('off')

    ax4 = fig.add_subplot(gs[1, :])
    ax4.text(0.5, 0.5, 'Overall Competency Scores', ha='center', va='center', fontsize=14)
    ax4.axis('off')

    plt.suptitle('Experiment Summary Dashboard', fontsize=16, fontweight='bold')
    plt.show()


def plot_sorting_progress(algorithm_name: str, initial_values: List[int],
                         final_values: List[int], steps_taken: int,
                         history: List[float] = None):
    """
    Simple plot showing sorting progress for a single algorithm run.

    Args:
        algorithm_name: Name of the algorithm
        initial_values: Starting array
        final_values: Final sorted array
        steps_taken: Number of steps taken
        history: Optional sortedness history
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    # Show initial vs final
    ax1.bar(range(len(initial_values)), initial_values, color='coral', alpha=0.7)
    ax1.set_title(f'Initial Array', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Position')
    ax1.set_ylabel('Value')
    ax1.grid(True, alpha=0.3, axis='y')

    ax2.bar(range(len(final_values)), final_values, color='steelblue', alpha=0.7)
    ax2.set_title(f'Final Array (after {steps_taken} steps)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Position')
    ax2.set_ylabel('Value')
    ax2.grid(True, alpha=0.3, axis='y')

    fig.suptitle(f'{algorithm_name.capitalize()} Sort', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

    # Plot sortedness history if available
    if history and len(history) > 0:
        plt.figure(figsize=(10, 4))
        plt.plot(history, color='green', linewidth=2)
        plt.xlabel('Swap Steps', fontsize=11)
        plt.ylabel('Sortedness (%)', fontsize=11)
        plt.title(f'{algorithm_name.capitalize()} Sort - Sortedness Progress',
                 fontsize=12, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.ylim(0, 105)
        plt.tight_layout()
        plt.show()


def plot_sortedness_comparison(results: Dict, title: str = "Algorithm Comparison"):
    """
    Compare sortedness progression for multiple algorithms.

    Args:
        results: Dict with algorithm names as keys, each containing 'history' list
        title: Plot title
    """
    plt.figure(figsize=(12, 6))

    colors = {'bubble': 'coral', 'insertion': 'steelblue', 'selection': 'green'}

    for algo_name, data in results.items():
        if isinstance(data, dict) and 'history' in data:
            history = data['history']
        elif isinstance(data, list):
            history = data
        else:
            continue

        if len(history) > 0:
            color = colors.get(algo_name, 'gray')
            plt.plot(history, label=algo_name.capitalize(),
                    color=color, linewidth=2, alpha=0.8)

    plt.xlabel('Swap Steps', fontsize=12)
    plt.ylabel('Sortedness (%)', fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 105)
    plt.tight_layout()
    plt.show()
