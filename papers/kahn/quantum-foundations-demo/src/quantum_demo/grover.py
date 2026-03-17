"""Grover's search algorithm for pedagogical quantum mechanics demos."""

import numpy as np
from quantum_demo.linalg import ket
from quantum_demo.states import equal_superposition, amplitudes_to_probabilities
from quantum_demo.gates import apply_gate, phase_oracle, diffusion_operator


def grover_iteration(state: np.ndarray, target_index: int) -> np.ndarray:
    """Apply one Grover iteration: oracle then diffusion.

    dim is inferred from state length.
    """
    dim = len(state)
    oracle = phase_oracle(target_index, dim)
    diffusion = diffusion_operator(dim)
    state = apply_gate(state, oracle)
    state = apply_gate(state, diffusion)
    return state


def grover_run(dim: int, target_index: int, iterations: int) -> list[np.ndarray]:
    """Return sequence of states: [initial_superposition, after_iter_1, ..., after_iter_n].

    Length is iterations + 1.
    """
    state = equal_superposition(dim)
    trajectory = [state.copy()]
    for _ in range(iterations):
        state = grover_iteration(state, target_index)
        trajectory.append(state.copy())
    return trajectory


def grover_optimal_iterations(dim: int) -> int:
    """Return nearest integer to (pi/4) * sqrt(dim)."""
    return round(np.pi / 4 * np.sqrt(dim))


def target_probability_trajectory(dim: int, target_index: int, iterations: int) -> np.ndarray:
    """Probability of marked state at each step: array of length iterations+1."""
    states = grover_run(dim, target_index, iterations)
    probs = np.array([
        amplitudes_to_probabilities(s)[target_index] for s in states
    ])
    return probs


def reduced_grover_plane_coordinates(state: np.ndarray, target_index: int) -> tuple[float, float]:
    """Project state into the 2D plane spanned by:
    - |target> (x-axis)
    - |s_perp> = equal superposition of all non-target states (y-axis)

    Return (x, y) coordinates where x = <target|state>, y = <s_perp|state>.
    """
    dim = len(state)
    # |target> basis vector
    target_ket = ket(target_index, dim)
    # |s_perp> = normalized equal superposition over non-target states
    s_perp = np.ones(dim, dtype=np.complex128)
    s_perp[target_index] = 0.0
    s_perp = s_perp / np.linalg.norm(s_perp)

    x = float(np.real(np.vdot(target_ket, state)))
    y = float(np.real(np.vdot(s_perp, state)))
    return (x, y)
