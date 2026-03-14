"""Quantum gate constants and utility functions for pedagogical demos."""

import numpy as np
from quantum_demo.linalg import ket

# ── Single-qubit gate constants (2x2, complex128) ─────────────────

I2 = np.eye(2, dtype=np.complex128)

X = np.array([[0, 1],
              [1, 0]], dtype=np.complex128)

Y = np.array([[0, -1j],
              [1j,  0]], dtype=np.complex128)

Z = np.array([[1,  0],
              [0, -1]], dtype=np.complex128)

H = np.array([[1,  1],
              [1, -1]], dtype=np.complex128) / np.sqrt(2)

S = np.array([[1, 0],
              [0, 1j]], dtype=np.complex128)

T = np.array([[1, 0],
              [0, np.exp(1j * np.pi / 4)]], dtype=np.complex128)

# ── Two-qubit gate constants (4x4, complex128) ────────────────────

CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]], dtype=np.complex128)


# ── Utility functions ─────────────────────────────────────────────

def apply_gate(state: np.ndarray, gate: np.ndarray) -> np.ndarray:
    """Apply unitary gate to state vector: gate @ state."""
    return gate @ state


def phase_oracle(target_index: int, dim: int) -> np.ndarray:
    """Diagonal oracle that flips sign of target basis amplitude only.

    Returns diagonal matrix with -1 at target_index, +1 elsewhere.
    """
    diag = np.ones(dim, dtype=np.complex128)
    diag[target_index] = -1.0
    return np.diag(diag)


def diffusion_operator(dim: int) -> np.ndarray:
    """Grover diffusion operator: 2|s><s| - I where |s> is equal superposition."""
    s = np.ones(dim, dtype=np.complex128) / np.sqrt(dim)
    return 2.0 * np.outer(s, s) - np.eye(dim, dtype=np.complex128)
