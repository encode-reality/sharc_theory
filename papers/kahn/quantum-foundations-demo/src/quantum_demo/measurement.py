"""Quantum measurement simulation for pedagogical quantum mechanics."""

import numpy as np
from quantum_demo.states import amplitudes_to_probabilities
from quantum_demo.linalg import ket


def measure_state(
    state: np.ndarray,
    rng: np.random.Generator | None = None,
) -> tuple[int, np.ndarray, np.ndarray]:
    """
    Sample one computational basis outcome.

    Return (observed_index, collapsed_state, probabilities).

    collapsed_state is the basis vector |observed_index>.
    probabilities is the Born probability vector before measurement.

    Parameters
    ----------
    state : np.ndarray
        Quantum state vector (1-D, normalized).
    rng : np.random.Generator or None
        Random number generator.  If ``None`` a fresh default generator
        is created (non-reproducible).
    """
    if rng is None:
        rng = np.random.default_rng()

    probabilities = amplitudes_to_probabilities(state)
    dim = len(state)
    observed_index = int(rng.choice(dim, p=probabilities))
    collapsed_state = ket(observed_index, dim)

    return observed_index, collapsed_state, probabilities


def repeated_measurements(
    state: np.ndarray,
    shots: int,
    rng: np.random.Generator | None = None,
) -> dict[int, int]:
    """Empirical measurement histogram.

    Each shot is an independent measurement of the ORIGINAL state
    (not collapsed -- each measurement is fresh from the same state).

    Parameters
    ----------
    state : np.ndarray
        Quantum state vector (1-D, normalized).
    shots : int
        Number of independent measurement samples.
    rng : np.random.Generator or None
        Random number generator.  If ``None`` a fresh default generator
        is created (non-reproducible).

    Returns
    -------
    dict[int, int]
        Mapping ``{outcome_index: count}`` for each observed outcome.
    """
    if rng is None:
        rng = np.random.default_rng()

    probabilities = amplitudes_to_probabilities(state)
    dim = len(state)
    samples = rng.choice(dim, size=shots, p=probabilities)

    counts: dict[int, int] = {}
    for outcome in samples:
        key = int(outcome)
        counts[key] = counts.get(key, 0) + 1

    return counts
