"""
Statistical analysis functions for sorting algorithm experiments.

This module provides hypothesis testing and statistical comparison tools.
"""

import numpy as np
from scipy import stats
from typing import List, Tuple, Dict


def z_test(sample1: List[float], sample2: List[float]) -> Tuple[float, float]:
    """
    Perform two-sample Z-test for equal means.

    Used when sample sizes are large (n > 30) and we're comparing means.

    Args:
        sample1: First sample
        sample2: Second sample

    Returns:
        Tuple of (z_statistic, p_value)
    """
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    var1 = np.var(sample1, ddof=1)
    var2 = np.var(sample2, ddof=1)
    n1 = len(sample1)
    n2 = len(sample2)

    # Standard error of difference
    se = np.sqrt(var1/n1 + var2/n2)

    # Z-statistic
    z = (mean1 - mean2) / se if se > 0 else 0

    # Two-tailed p-value
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))

    return z, p_value


def t_test(sample1: List[float], sample2: List[float]) -> Tuple[float, float]:
    """
    Perform two-sample t-test for equal means.

    Args:
        sample1: First sample
        sample2: Second sample

    Returns:
        Tuple of (t_statistic, p_value)
    """
    t_stat, p_value = stats.ttest_ind(sample1, sample2)
    return t_stat, p_value


def summarize_statistics(data: List[float]) -> Dict:
    """
    Calculate summary statistics for a dataset.

    Args:
        data: List of numerical values

    Returns:
        Dictionary with mean, std, median, min, max, and confidence interval
    """
    data_array = np.array(data)

    # Calculate confidence interval (95%)
    confidence = 0.95
    n = len(data_array)
    mean = np.mean(data_array)
    std_err = stats.sem(data_array)
    ci = std_err * stats.t.ppf((1 + confidence) / 2, n - 1)

    return {
        'mean': mean,
        'std': np.std(data_array, ddof=1),
        'median': np.median(data_array),
        'min': np.min(data_array),
        'max': np.max(data_array),
        'ci_lower': mean - ci,
        'ci_upper': mean + ci,
        'n': n
    }


def compare_algorithms(results1: Dict, results2: Dict, metric: str = "total_steps") -> Dict:
    """
    Statistical comparison between two algorithm results.

    Args:
        results1: First algorithm results (e.g., traditional)
        results2: Second algorithm results (e.g., cell-view)
        metric: Which metric to compare (e.g., "total_steps", "swap_steps")

    Returns:
        Dictionary with comparison statistics
    """
    data1 = results1[metric]
    data2 = results2[metric]

    stats1 = summarize_statistics(data1)
    stats2 = summarize_statistics(data2)

    z_stat, z_p = z_test(data1, data2)
    t_stat, t_p = t_test(data1, data2)

    return {
        'algorithm1_stats': stats1,
        'algorithm2_stats': stats2,
        'z_statistic': z_stat,
        'z_p_value': z_p,
        't_statistic': t_stat,
        't_p_value': t_p,
        'significant_at_0.05': z_p < 0.05,
        'significant_at_0.01': z_p < 0.01,
        'mean_difference': stats1['mean'] - stats2['mean'],
        'percent_difference': ((stats1['mean'] - stats2['mean']) / stats1['mean'] * 100) if stats1['mean'] != 0 else 0
    }


def format_significance(p_value: float) -> str:
    """
    Format p-value with asterisks for significance level.

    Args:
        p_value: P-value from statistical test

    Returns:
        Formatted string (e.g., "p < 0.001 ***")
    """
    if p_value < 0.001:
        return "p < 0.001 ***"
    elif p_value < 0.01:
        return f"p = {p_value:.3f} **"
    elif p_value < 0.05:
        return f"p = {p_value:.3f} *"
    else:
        return f"p = {p_value:.3f} (n.s.)"


def print_comparison(comparison: Dict, name1: str = "Algorithm 1", name2: str = "Algorithm 2"):
    """
    Print formatted comparison results.

    Args:
        comparison: Dictionary from compare_algorithms()
        name1: Name of first algorithm
        name2: Name of second algorithm
    """
    print(f"\n{'='*60}")
    print(f"Statistical Comparison: {name1} vs {name2}")
    print(f"{'='*60}")

    print(f"\n{name1}:")
    print(f"  Mean: {comparison['algorithm1_stats']['mean']:.2f}")
    print(f"  Std:  {comparison['algorithm1_stats']['std']:.2f}")
    print(f"  95% CI: [{comparison['algorithm1_stats']['ci_lower']:.2f}, {comparison['algorithm1_stats']['ci_upper']:.2f}]")

    print(f"\n{name2}:")
    print(f"  Mean: {comparison['algorithm2_stats']['mean']:.2f}")
    print(f"  Std:  {comparison['algorithm2_stats']['std']:.2f}")
    print(f"  95% CI: [{comparison['algorithm2_stats']['ci_lower']:.2f}, {comparison['algorithm2_stats']['ci_upper']:.2f}]")

    print(f"\nDifference:")
    print(f"  Mean difference: {comparison['mean_difference']:.2f}")
    print(f"  Percent difference: {comparison['percent_difference']:.2f}%")

    print(f"\nStatistical Tests:")
    print(f"  Z-test: z = {comparison['z_statistic']:.2f}, {format_significance(comparison['z_p_value'])}")
    print(f"  T-test: t = {comparison['t_statistic']:.2f}, {format_significance(comparison['t_p_value'])}")

    if comparison['significant_at_0.01']:
        print(f"\n  ✓ HIGHLY SIGNIFICANT difference (p < 0.01)")
    elif comparison['significant_at_0.05']:
        print(f"\n  ✓ Significant difference (p < 0.05)")
    else:
        print(f"\n  ✗ No significant difference (p ≥ 0.05)")

    print(f"{'='*60}\n")
