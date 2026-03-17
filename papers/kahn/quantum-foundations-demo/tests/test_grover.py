"""Tests for Grover's search algorithm module."""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'src'))

import numpy as np
import pytest
from quantum_demo.linalg import is_normalized
from quantum_demo.states import equal_superposition, amplitudes_to_probabilities
from quantum_demo.grover import (
    grover_iteration,
    grover_run,
    grover_optimal_iterations,
    target_probability_trajectory,
    reduced_grover_plane_coordinates,
)


# ── grover_iteration ─────────────────────────────────────────────

def test_grover_iteration_increases_target_probability():
    """One Grover iteration should boost the target amplitude."""
    dim = 8
    target = 3
    state = equal_superposition(dim)
    initial_prob = amplitudes_to_probabilities(state)[target]

    new_state = grover_iteration(state, target)
    new_prob = amplitudes_to_probabilities(new_state)[target]

    assert new_prob > initial_prob, (
        f"Target probability did not increase: {initial_prob} -> {new_prob}"
    )


# ── grover_run ────────────────────────────────────────────────────

def test_grover_run_returns_correct_length():
    """Returned list has iterations+1 entries (initial + each iteration)."""
    dim = 4
    iterations = 3
    states = grover_run(dim, target_index=0, iterations=iterations)
    assert len(states) == iterations + 1


def test_grover_run_first_state_is_equal_superposition():
    """The first state in the trajectory should be the equal superposition."""
    dim = 8
    states = grover_run(dim, target_index=2, iterations=2)
    expected = equal_superposition(dim)
    np.testing.assert_allclose(states[0], expected, atol=1e-12)


# ── grover_optimal_iterations ────────────────────────────────────

@pytest.mark.parametrize("dim,expected", [
    (4, 2),
    (8, 2),
    (256, 13),
])
def test_grover_optimal_iterations(dim, expected):
    result = grover_optimal_iterations(dim)
    assert result == expected, (
        f"grover_optimal_iterations({dim}) = {result}, expected {expected}"
    )


# ── target_probability_trajectory ────────────────────────────────

def test_target_probability_trajectory_increases_early():
    """For the first couple of iterations the target probability should grow."""
    dim = 8
    target = 0
    iterations = 2
    probs = target_probability_trajectory(dim, target, iterations)
    # probability should increase at each of the first 2 steps
    for i in range(len(probs) - 1):
        assert probs[i + 1] > probs[i], (
            f"Probability did not increase at step {i}: {probs[i]} -> {probs[i + 1]}"
        )


def test_target_probability_trajectory_length():
    dim = 4
    iterations = 5
    probs = target_probability_trajectory(dim, target_index=1, iterations=iterations)
    assert len(probs) == iterations + 1


# ── reduced_grover_plane_coordinates ─────────────────────────────

def test_reduced_grover_plane_coordinates_returns_float_tuple():
    dim = 4
    state = equal_superposition(dim)
    coords = reduced_grover_plane_coordinates(state, target_index=0)
    assert isinstance(coords, tuple) and len(coords) == 2
    assert isinstance(coords[0], float)
    assert isinstance(coords[1], float)


def test_reduced_grover_plane_coordinates_for_equal_superposition():
    """For equal superposition of dim states, x = 1/sqrt(dim) and
    y = sqrt((dim-1)/dim), giving angle arcsin(1/sqrt(dim))."""
    dim = 8
    target = 0
    state = equal_superposition(dim)
    x, y = reduced_grover_plane_coordinates(state, target)
    expected_x = 1.0 / np.sqrt(dim)
    expected_y = np.sqrt((dim - 1) / dim)
    np.testing.assert_allclose(x, expected_x, atol=1e-12)
    np.testing.assert_allclose(y, expected_y, atol=1e-12)


# ── normalization throughout iterations ──────────────────────────

def test_states_remain_normalized_throughout_grover_run():
    dim = 8
    target = 5
    iterations = 5
    states = grover_run(dim, target, iterations)
    for i, state in enumerate(states):
        assert is_normalized(state), (
            f"State at step {i} is not normalized (norm = {np.linalg.norm(state)})"
        )
