"""Quantum state construction utilities for pedagogical quantum mechanics."""

import numpy as np
from quantum_demo.linalg import normalize, ket


def basis_state(index: int, dim: int) -> np.ndarray:
    """Alias for computational basis state |index> in C^dim."""
    return ket(index, dim)


def qubit_state(alpha: complex, beta: complex) -> np.ndarray:
    """Create normalized 1-qubit state alpha|0> + beta|1>."""
    vec = np.array([alpha, beta], dtype=np.complex128)
    return normalize(vec)


def equal_superposition(dim: int) -> np.ndarray:
    """Uniform amplitude state over computational basis: (1/sqrt(dim)) * sum of all basis states."""
    return np.ones(dim, dtype=np.complex128) / np.sqrt(dim)


def amplitudes_to_probabilities(state: np.ndarray) -> np.ndarray:
    """Born probabilities from amplitude vector: |psi_i|^2."""
    return (np.abs(state) ** 2).astype(np.float64)


def pretty_basis_labels(num_qubits: int) -> list[str]:
    """Return ['00', '01', '10', '11'] labels for computational basis of num_qubits."""
    dim = 2 ** num_qubits
    return [format(i, f'0{num_qubits}b') for i in range(dim)]
