"""
Morphogenesis Sorting Algorithms Package

This package implements experiments from:
Zhang, T., Goldstein, A., Levin, M. (2024)
"Classical Sorting Algorithms as a Model of Morphogenesis"

Modules:
    core: Data structures (Cell, StepCounter, Probe)
    metrics: Measurement functions (sortedness, DG, aggregation)
    traditional_sorts: Top-down sorting algorithms
    cell_view_sorts: Distributed, agent-based sorting
    experiments: Experiment harness and runners
    visualization: Plotting functions
    statistical: Statistical analysis tools
"""

__version__ = "1.0.0"
__author__ = "Based on Zhang, Goldstein & Levin (2024)"

# Import key components for easier access
from .core import Cell, StepCounter, Probe, Algotype, FrozenType, set_experiment_seed
from .metrics import sortedness, monotonicity_error, compute_delayed_gratification, aggregation_value
from .experiments import (
    run_trajectories_experiment,
    run_efficiency_comparison,
    run_frozen_cell_experiments,
    run_delayed_gratification_experiment,
    run_mixed_algotypes_experiment,
    run_all_experiments
)
from .visualization import (
    plot_trajectories,
    plot_trajectories_comparison,
    plot_efficiency_comparison,
    plot_error_tolerance,
    plot_delayed_gratification,
    plot_aggregation
)
from .statistical import z_test, t_test, compare_algorithms, print_comparison

__all__ = [
    # Core
    'Cell', 'StepCounter', 'Probe', 'Algotype', 'FrozenType', 'set_experiment_seed',
    # Metrics
    'sortedness', 'monotonicity_error', 'compute_delayed_gratification', 'aggregation_value',
    # Experiments
    'run_trajectories_experiment', 'run_efficiency_comparison',
    'run_frozen_cell_experiments', 'run_delayed_gratification_experiment',
    'run_mixed_algotypes_experiment', 'run_all_experiments',
    # Visualization
    'plot_trajectories', 'plot_trajectories_comparison', 'plot_efficiency_comparison',
    'plot_error_tolerance', 'plot_delayed_gratification', 'plot_aggregation',
    # Statistical
    'z_test', 't_test', 'compare_algorithms', 'print_comparison'
]
