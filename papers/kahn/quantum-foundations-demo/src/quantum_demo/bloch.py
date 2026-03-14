"""Bloch sphere coordinate mapping for single-qubit states."""

import numpy as np


def bloch_coordinates(state: np.ndarray) -> tuple[float, float, float]:
    """Map normalized 1-qubit state to Bloch coordinates (x, y, z).

    For state alpha|0> + beta|1>:
        x = 2*Re(alpha* beta)
        y = 2*Im(alpha* beta)
        z = |alpha|^2 - |beta|^2

    Parameters
    ----------
    state : np.ndarray
        A length-2 complex array representing a normalized qubit state
        [alpha, beta].

    Returns
    -------
    tuple[float, float, float]
        Bloch sphere coordinates (x, y, z).
    """
    alpha = state[0]
    beta = state[1]

    x = 2.0 * np.real(np.conj(alpha) * beta)
    y = 2.0 * np.imag(np.conj(alpha) * beta)
    z = float(np.abs(alpha) ** 2 - np.abs(beta) ** 2)

    return (float(x), float(y), float(z))
