"""Tests for quantum_demo.states — quantum state construction utilities."""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'src'))

import numpy as np
import pytest

from quantum_demo.states import (
    amplitudes_to_probabilities,
    basis_state,
    equal_superposition,
    pretty_basis_labels,
    qubit_state,
)
from quantum_demo.linalg import is_normalized


# -- basis_state --------------------------------------------------------------

class TestBasisState:
    def test_ket_0_dim_2(self):
        result = basis_state(0, 2)
        expected = np.array([1, 0], dtype=np.complex128)
        np.testing.assert_array_equal(result, expected)

    def test_ket_1_dim_2(self):
        result = basis_state(1, 2)
        expected = np.array([0, 1], dtype=np.complex128)
        np.testing.assert_array_equal(result, expected)

    def test_ket_dim_4(self):
        result = basis_state(2, 4)
        expected = np.zeros(4, dtype=np.complex128)
        expected[2] = 1.0
        np.testing.assert_array_equal(result, expected)

    def test_basis_state_is_normalized(self):
        for dim in [2, 3, 5]:
            for idx in range(dim):
                assert is_normalized(basis_state(idx, dim)) is True

    def test_invalid_index_raises(self):
        with pytest.raises((IndexError, ValueError)):
            basis_state(3, 2)

    def test_negative_index_raises(self):
        with pytest.raises((IndexError, ValueError)):
            basis_state(-1, 2)


# -- qubit_state ---------------------------------------------------------------

class TestQubitState:
    def test_pure_zero(self):
        """alpha=1, beta=0 gives |0>."""
        result = qubit_state(1, 0)
        expected = np.array([1, 0], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_pure_one(self):
        """alpha=0, beta=1 gives |1>."""
        result = qubit_state(0, 1)
        expected = np.array([0, 1], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_equal_superposition(self):
        """alpha=1, beta=1 gives normalized (1/sqrt2)|0> + (1/sqrt2)|1>."""
        result = qubit_state(1, 1)
        assert is_normalized(result) is True
        np.testing.assert_allclose(np.abs(result[0]), np.abs(result[1]))

    def test_always_normalized(self):
        """Output is normalized even when inputs are not."""
        result = qubit_state(3, 4)
        assert is_normalized(result) is True

    def test_complex_amplitudes(self):
        result = qubit_state(1j, 1)
        assert is_normalized(result) is True
        assert result.shape == (2,)

    def test_length_is_two(self):
        result = qubit_state(0.5, 0.5)
        assert result.shape == (2,)

    def test_relative_phase_preserved(self):
        """The ratio alpha/beta should be preserved after normalization."""
        alpha, beta = 1 + 1j, 2 - 1j
        result = qubit_state(alpha, beta)
        ratio_input = alpha / beta
        ratio_output = result[0] / result[1]
        assert ratio_output == pytest.approx(ratio_input)


# -- equal_superposition -------------------------------------------------------

class TestEqualSuperposition:
    def test_dim_2(self):
        result = equal_superposition(2)
        expected = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_dim_4(self):
        result = equal_superposition(4)
        expected_amp = 1 / np.sqrt(4)
        for amp in result:
            assert abs(amp) == pytest.approx(expected_amp)

    def test_is_normalized(self):
        for dim in [2, 3, 4, 8]:
            result = equal_superposition(dim)
            assert is_normalized(result) is True

    def test_all_amplitudes_equal(self):
        result = equal_superposition(5)
        magnitudes = np.abs(result)
        np.testing.assert_allclose(magnitudes, magnitudes[0] * np.ones(5))

    def test_shape(self):
        result = equal_superposition(3)
        assert result.shape == (3,)

    def test_dim_1(self):
        result = equal_superposition(1)
        np.testing.assert_allclose(result, np.array([1.0], dtype=np.complex128))


# -- amplitudes_to_probabilities -----------------------------------------------

class TestAmplitudesToProbabilities:
    def test_basis_state(self):
        """A basis state |0> gives probability [1, 0]."""
        state = np.array([1, 0], dtype=np.complex128)
        probs = amplitudes_to_probabilities(state)
        np.testing.assert_allclose(probs, [1.0, 0.0])

    def test_equal_superposition(self):
        """Equal superposition gives equal probabilities."""
        state = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)], dtype=np.complex128)
        probs = amplitudes_to_probabilities(state)
        np.testing.assert_allclose(probs, [0.5, 0.5])

    def test_born_rule_complex(self):
        """Born rule: p_i = |psi_i|^2 for complex amplitudes."""
        state = np.array([1 / np.sqrt(2), 1j / np.sqrt(2)], dtype=np.complex128)
        probs = amplitudes_to_probabilities(state)
        np.testing.assert_allclose(probs, [0.5, 0.5])

    def test_probabilities_sum_to_one(self):
        """For a normalized state, probabilities must sum to 1."""
        state = np.array([1 / np.sqrt(3), 1j / np.sqrt(3), 1 / np.sqrt(3)],
                         dtype=np.complex128)
        probs = amplitudes_to_probabilities(state)
        assert sum(probs) == pytest.approx(1.0)

    def test_probabilities_non_negative(self):
        state = np.array([0.5 + 0.5j, -0.5 + 0.5j], dtype=np.complex128)
        probs = amplitudes_to_probabilities(state)
        assert all(p >= 0 for p in probs)

    def test_returns_real(self):
        state = np.array([1j, 0], dtype=np.complex128)
        probs = amplitudes_to_probabilities(state)
        assert np.issubdtype(probs.dtype, np.floating)

    def test_four_dimensional(self):
        state = np.array([0.5, 0.5, 0.5, 0.5], dtype=np.complex128)
        probs = amplitudes_to_probabilities(state)
        np.testing.assert_allclose(probs, [0.25, 0.25, 0.25, 0.25])


# -- pretty_basis_labels -------------------------------------------------------

class TestPrettyBasisLabels:
    def test_one_qubit(self):
        labels = pretty_basis_labels(1)
        assert labels == ['0', '1']

    def test_two_qubits(self):
        labels = pretty_basis_labels(2)
        assert labels == ['00', '01', '10', '11']

    def test_three_qubits(self):
        labels = pretty_basis_labels(3)
        assert len(labels) == 8
        assert labels[0] == '000'
        assert labels[-1] == '111'
        assert labels[5] == '101'

    def test_label_count(self):
        for n in [1, 2, 3, 4]:
            labels = pretty_basis_labels(n)
            assert len(labels) == 2 ** n

    def test_labels_are_strings(self):
        labels = pretty_basis_labels(2)
        for label in labels:
            assert isinstance(label, str)

    def test_labels_correct_width(self):
        """Each label should have exactly num_qubits characters."""
        for n in [1, 2, 3]:
            labels = pretty_basis_labels(n)
            for label in labels:
                assert len(label) == n
