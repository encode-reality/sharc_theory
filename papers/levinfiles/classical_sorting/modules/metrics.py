"""
Metrics for analyzing sorting algorithm behavior.

This module implements all measurement functions for quantifying
the sorting process, including sortedness, error tolerance,
delayed gratification, and aggregation.
"""

from typing import List
from .core import Algotype


def monotonicity_error(values: List[int], direction: str = "inc") -> int:
    """
    Count the number of violations of monotonic order.

    In biology, this is like counting organs that are out of place
    along the body axis.

    Args:
        values: List of integer values
        direction: "inc" for increasing order, "dec" for decreasing

    Returns:
        Number of adjacent pairs that violate the specified order
    """
    if len(values) < 2:
        return 0

    errors = 0
    for i in range(len(values) - 1):
        if direction == "inc":
            if values[i] > values[i + 1]:
                errors += 1
        else:  # decreasing
            if values[i] < values[i + 1]:
                errors += 1

    return errors


def sortedness(values: List[int], direction: str = "inc") -> float:
    """
    Calculate the percentage of cells following the designated order.

    This measures how close the array is to the target morphology.

    Formula: (correct_pairs / total_pairs) * 100

    Args:
        values: List of integer values
        direction: "inc" for increasing, "dec" for decreasing

    Returns:
        Sortedness percentage (0-100)
    """
    if len(values) < 2:
        return 100.0

    correct_pairs = 0
    total_pairs = len(values) - 1

    for i in range(len(values) - 1):
        if direction == "inc":
            if values[i] <= values[i + 1]:
                correct_pairs += 1
        else:  # decreasing
            if values[i] >= values[i + 1]:
                correct_pairs += 1

    return 100.0 * correct_pairs / total_pairs


def compute_delayed_gratification(sortedness_series: List[float]) -> float:
    """
    Calculate the Delayed Gratification (DG) index.

    DG measures the ability to temporarily move away from a goal
    (decrease sortedness) to achieve larger gains later.
    This is a key signature of problem-solving intelligence.

    The algorithm finds episodes where:
    1. Sortedness decreases (y = magnitude of decrease)
    2. Then sortedness increases (x = magnitude of increase)
    3. DG for that episode = x / y

    Total DG = sum of all episode DGs

    Args:
        sortedness_series: List of sortedness values over time

    Returns:
        Total delayed gratification value
    """
    if len(sortedness_series) < 3:
        return 0.0

    dg_total = 0.0
    i = 0

    while i < len(sortedness_series) - 1:
        # Look for start of a downward segment
        if sortedness_series[i + 1] < sortedness_series[i]:
            start = i
            start_value = sortedness_series[i]

            # Find the bottom of the decrease
            j = i + 1
            while j < len(sortedness_series) and sortedness_series[j] <= sortedness_series[j - 1]:
                j += 1

            if j >= len(sortedness_series):
                break

            bottom = j - 1
            bottom_value = sortedness_series[bottom]

            # Calculate the decrease
            y = start_value - bottom_value

            # Now find the subsequent increase
            k = bottom + 1
            while k < len(sortedness_series) and sortedness_series[k] >= sortedness_series[k - 1]:
                k += 1

            peak = k - 1
            peak_value = sortedness_series[peak]

            # Calculate the increase
            x = peak_value - bottom_value

            # Add to DG if both decrease and increase occurred
            if y > 0 and x > 0:
                dg_total += x / y

            i = peak
        else:
            i += 1

    return dg_total


def aggregation_value(algotypes: List[Algotype]) -> float:
    """
    Calculate the percentage of cells with same-type neighbors.

    In chimeric arrays (mixing different algotypes), this measures
    whether cells cluster by type - an emergent behavior not
    explicitly programmed.

    Args:
        algotypes: List of algotype identifiers for each cell

    Returns:
        Aggregation percentage (0-100)
    """
    if len(algotypes) < 2:
        return 0.0

    n = len(algotypes)
    same_neighbor_count = 0
    total_checked = 0

    for i in range(n):
        neighbors = []

        # Check left neighbor
        if i > 0:
            neighbors.append(algotypes[i - 1])

        # Check right neighbor
        if i < n - 1:
            neighbors.append(algotypes[i + 1])

        if not neighbors:
            continue

        total_checked += 1

        # Check if ALL neighbors are the same type as this cell
        if all(neighbor == algotypes[i] for neighbor in neighbors):
            same_neighbor_count += 1

    if total_checked == 0:
        return 0.0

    return 100.0 * same_neighbor_count / total_checked


def calculate_efficiency_metrics(results_dict):
    """
    Extract efficiency statistics from experiment results.

    Args:
        results_dict: Dictionary with 'comparison_steps', 'swap_steps', 'total_steps' keys

    Returns:
        Dictionary with mean and std for each metric
    """
    import numpy as np

    return {
        'swap_mean': np.mean(results_dict['swap_steps']),
        'swap_std': np.std(results_dict['swap_steps']),
        'comparison_mean': np.mean(results_dict['comparison_steps']),
        'comparison_std': np.std(results_dict['comparison_steps']),
        'total_mean': np.mean(results_dict['total_steps']),
        'total_std': np.std(results_dict['total_steps'])
    }


def calculate_error_metrics(results_dict):
    """
    Extract error tolerance statistics from experiment results.

    Args:
        results_dict: Dictionary with 'monotonicity_error' key

    Returns:
        Dictionary with mean and std error
    """
    import numpy as np

    return {
        'error_mean': np.mean(results_dict['monotonicity_error']),
        'error_std': np.std(results_dict['monotonicity_error'])
    }


def calculate_dg_metrics(results_dict):
    """
    Calculate delayed gratification for all runs in results.

    Args:
        results_dict: Dictionary with 'sortedness_history' key (list of lists)

    Returns:
        Dictionary with mean and std DG
    """
    import numpy as np

    dg_values = []
    for history in results_dict['sortedness_history']:
        if len(history) > 0:
            dg = compute_delayed_gratification(history)
            dg_values.append(dg)

    return {
        'dg_mean': np.mean(dg_values) if dg_values else 0.0,
        'dg_std': np.std(dg_values) if dg_values else 0.0,
        'dg_values': dg_values
    }


def track_aggregation_over_time(algotype_histories: List[List[Algotype]]) -> List[float]:
    """
    Calculate aggregation value at each timestep across multiple runs.

    Args:
        algotype_histories: List of algotype arrays at each timestep for each run

    Returns:
        List of average aggregation values over time
    """
    import numpy as np

    if not algotype_histories or not algotype_histories[0]:
        return []

    # Find maximum length
    max_len = max(len(history) for history in algotype_histories)

    aggregation_timeline = []

    for t in range(max_len):
        timestep_aggregations = []
        for history in algotype_histories:
            if t < len(history):
                agg = aggregation_value(history[t])
                timestep_aggregations.append(agg)

        if timestep_aggregations:
            aggregation_timeline.append(np.mean(timestep_aggregations))

    return aggregation_timeline
