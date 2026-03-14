"""Tests for quantum_demo.measurement — quantum measurement simulation."""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'src'))

import numpy as np
import pytest

from quantum_demo.measurement import measure_state, repeated_measurements
from quantum_demo.states import equal_superposition, basis_state
from quantum_demo.linalg import is_normalized, ket


# -- measure_state -------------------------------------------------------------

class TestMeasureState:
    def test_returns_valid_index_within_range(self):
        """Observed index must be in [0, dim)."""
        state = equal_superposition(4)
        rng = np.random.default_rng(42)
        idx, collapsed, probs = measure_state(state, rng=rng)
        assert 0 <= idx < 4

    def test_returns_valid_index_qubit(self):
        """For a qubit the index must be 0 or 1."""
        state = equal_superposition(2)
        rng = np.random.default_rng(99)
        idx, collapsed, probs = measure_state(state, rng=rng)
        assert idx in (0, 1)

    def test_probabilities_match_born_rule(self):
        """Returned probabilities must equal |amplitude|^2."""
        state = np.array([1 / np.sqrt(3), 1j / np.sqrt(3), 1 / np.sqrt(3)],
                         dtype=np.complex128)
        rng = np.random.default_rng(0)
        _, _, probs = measure_state(state, rng=rng)
        expected = np.array([1 / 3, 1 / 3, 1 / 3])
        np.testing.assert_allclose(probs, expected, atol=1e-12)

    def test_probabilities_born_rule_unequal(self):
        """Born rule for unequal amplitudes."""
        state = np.array([np.sqrt(0.7), np.sqrt(0.3)], dtype=np.complex128)
        rng = np.random.default_rng(7)
        _, _, probs = measure_state(state, rng=rng)
        np.testing.assert_allclose(probs, [0.7, 0.3], atol=1e-12)

    def test_collapsed_state_is_basis_state(self):
        """After measurement the collapsed state must be a basis vector."""
        state = equal_superposition(4)
        rng = np.random.default_rng(12)
        idx, collapsed, _ = measure_state(state, rng=rng)
        expected_basis = ket(idx, 4)
        np.testing.assert_array_equal(collapsed, expected_basis)

    def test_collapsed_state_is_normalized(self):
        """Collapsed state should be a valid normalized state."""
        state = equal_superposition(3)
        rng = np.random.default_rng(1)
        _, collapsed, _ = measure_state(state, rng=rng)
        assert is_normalized(collapsed)

    def test_repeated_measurement_of_collapsed_state(self):
        """Measuring a collapsed (basis) state always returns the same index."""
        state = equal_superposition(4)
        rng = np.random.default_rng(55)
        idx, collapsed, _ = measure_state(state, rng=rng)
        # Measure the collapsed state many times — always same result
        for _ in range(20):
            idx2, collapsed2, probs2 = measure_state(collapsed, rng=rng)
            assert idx2 == idx
            np.testing.assert_array_equal(collapsed2, collapsed)

    def test_basis_state_always_gives_itself(self):
        """Measuring |1> in dim=2 always returns index 1."""
        state = basis_state(1, 2)
        rng = np.random.default_rng(0)
        for _ in range(10):
            idx, collapsed, probs = measure_state(state, rng=rng)
            assert idx == 1
            np.testing.assert_allclose(probs, [0.0, 1.0])


# -- repeated_measurements ----------------------------------------------------

class TestRepeatedMeasurements:
    def test_returns_dict_with_int_keys(self):
        """Keys of the histogram must be Python ints."""
        state = equal_superposition(2)
        rng = np.random.default_rng(0)
        result = repeated_measurements(state, shots=100, rng=rng)
        assert isinstance(result, dict)
        for key in result:
            assert isinstance(key, int)

    def test_counts_sum_to_shots(self):
        """Total counts must equal the number of shots."""
        state = equal_superposition(3)
        rng = np.random.default_rng(1)
        shots = 500
        result = repeated_measurements(state, shots=shots, rng=rng)
        assert sum(result.values()) == shots

    def test_counts_sum_to_shots_various(self):
        """Works for different shot counts."""
        state = equal_superposition(2)
        rng = np.random.default_rng(2)
        for shots in [1, 10, 1000]:
            result = repeated_measurements(state, shots=shots, rng=rng)
            assert sum(result.values()) == shots

    def test_seeded_rng_reproducible(self):
        """Same seed produces identical results."""
        state = equal_superposition(4)
        result1 = repeated_measurements(state, shots=200, rng=np.random.default_rng(42))
        result2 = repeated_measurements(state, shots=200, rng=np.random.default_rng(42))
        assert result1 == result2

    def test_keys_are_valid_indices(self):
        """All keys must be valid basis indices."""
        dim = 4
        state = equal_superposition(dim)
        rng = np.random.default_rng(10)
        result = repeated_measurements(state, shots=500, rng=rng)
        for key in result:
            assert 0 <= key < dim

    def test_statistical_convergence_plus_state(self):
        """|+> state should give roughly 50/50 over many shots."""
        state = equal_superposition(2)  # |+> = (|0> + |1>) / sqrt(2)
        rng = np.random.default_rng(123)
        shots = 10_000
        result = repeated_measurements(state, shots=shots, rng=rng)
        freq_0 = result.get(0, 0) / shots
        freq_1 = result.get(1, 0) / shots
        # Allow 5% tolerance for statistical fluctuation
        assert freq_0 == pytest.approx(0.5, abs=0.05)
        assert freq_1 == pytest.approx(0.5, abs=0.05)

    def test_statistical_convergence_biased(self):
        """Biased state should converge to Born-rule probabilities."""
        state = np.array([np.sqrt(0.9), np.sqrt(0.1)], dtype=np.complex128)
        rng = np.random.default_rng(77)
        shots = 10_000
        result = repeated_measurements(state, shots=shots, rng=rng)
        freq_0 = result.get(0, 0) / shots
        freq_1 = result.get(1, 0) / shots
        assert freq_0 == pytest.approx(0.9, abs=0.05)
        assert freq_1 == pytest.approx(0.1, abs=0.05)

    def test_basis_state_all_same_outcome(self):
        """Measuring a basis state should always yield the same index."""
        state = basis_state(0, 2)
        rng = np.random.default_rng(0)
        result = repeated_measurements(state, shots=100, rng=rng)
        assert result == {0: 100}
