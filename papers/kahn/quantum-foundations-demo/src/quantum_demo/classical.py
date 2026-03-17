"""Classical probability utilities for the quantum-foundations demo."""

from __future__ import annotations

import numpy as np


def normalize_probabilities(p: np.ndarray) -> np.ndarray:
    """Normalize a nonnegative vector to sum to 1.

    Parameters
    ----------
    p : np.ndarray
        A 1-D array of nonnegative values.

    Returns
    -------
    np.ndarray
        Probability distribution that sums to 1.

    Raises
    ------
    ValueError
        If the vector sums to zero (cannot be normalized).
    """
    total = p.sum()
    if total == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return p / total


def sample_classical(p: np.ndarray, rng: np.random.Generator | None = None) -> int:
    """Sample an index according to a classical probability distribution.

    Parameters
    ----------
    p : np.ndarray
        Probability distribution (must sum to 1).
    rng : np.random.Generator or None
        Random number generator. If None, a default one is created.

    Returns
    -------
    int
        Sampled index.
    """
    if rng is None:
        rng = np.random.default_rng()
    return int(rng.choice(len(p), p=p))


def apply_stochastic_matrix(p: np.ndarray, T: np.ndarray) -> np.ndarray:
    """Apply a stochastic transition matrix to a probability vector.

    Computes T @ p, where each column of T describes transition
    probabilities *from* the corresponding state.

    Parameters
    ----------
    p : np.ndarray
        Probability column vector (1-D, sums to 1).
    T : np.ndarray
        Stochastic matrix (columns sum to 1).

    Returns
    -------
    np.ndarray
        Resulting probability distribution.
    """
    return T @ p


def indicator_distribution(index: int, dim: int) -> np.ndarray:
    """Return a deterministic classical state concentrated at one outcome.

    Parameters
    ----------
    index : int
        The outcome that receives probability 1.
    dim : int
        Dimension of the probability vector.

    Returns
    -------
    np.ndarray
        A 1-D array of length *dim* with a 1 at *index* and 0 elsewhere.

    Raises
    ------
    ValueError
        If *index* is out of range [0, dim).
    """
    if index < 0 or index >= dim:
        raise ValueError(
            f"index {index} is out of range for dimension {dim}."
        )
    d = np.zeros(dim)
    d[index] = 1.0
    return d
