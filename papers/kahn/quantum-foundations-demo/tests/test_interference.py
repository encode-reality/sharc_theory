"""Tests for quantum interference demonstrations."""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'src'))

import numpy as np
import pytest
from quantum_demo.linalg import ket
from quantum_demo.gates import H, Z
from quantum_demo.interference import (
    hadamard_interference_demo,
    path_amplitude_sum,
    compare_probability_vs_amplitude_combination,
)


# ── hadamard_interference_demo ────────────────────────────────────


def test_hadamard_demo_returns_dict_with_expected_keys():
    result = hadamard_interference_demo()
    expected_keys = {
        'ket0', 'H_ket0', 'H_ket0_probs',
        'HH_ket0', 'HH_ket0_probs',
        'Z_H_ket0', 'Z_H_ket0_probs',
        'HZH_ket0', 'HZH_ket0_probs',
    }
    assert isinstance(result, dict)
    assert set(result.keys()) == expected_keys


def test_hadamard_demo_h_ket0_equal_superposition():
    """H|0> should give equal superposition (1/sqrt(2), 1/sqrt(2))."""
    result = hadamard_interference_demo()
    ket0 = ket(0, 2)
    ket1 = ket(1, 2)
    expected = (ket0 + ket1) / np.sqrt(2)
    np.testing.assert_allclose(result['H_ket0'], expected, atol=1e-12)


def test_hadamard_demo_hh_ket0_constructive_interference():
    """HH|0> should return to |0> via constructive interference."""
    result = hadamard_interference_demo()
    ket0 = ket(0, 2)
    np.testing.assert_allclose(result['HH_ket0'], ket0, atol=1e-12)
    # Probabilities: 100% on |0>, 0% on |1>
    np.testing.assert_allclose(result['HH_ket0_probs'], [1.0, 0.0], atol=1e-12)


def test_hadamard_demo_hzh_ket0_destructive_interference():
    """HZH|0> should give |1> via destructive interference on |0>."""
    result = hadamard_interference_demo()
    ket1 = ket(1, 2)
    np.testing.assert_allclose(result['HZH_ket0'], ket1, atol=1e-12)
    # Probabilities: 0% on |0>, 100% on |1>
    np.testing.assert_allclose(result['HZH_ket0_probs'], [0.0, 1.0], atol=1e-12)


# ── path_amplitude_sum ────────────────────────────────────────────


def test_path_amplitude_sum_constructive():
    """Two positive amplitudes [1/2, 1/2] sum to 1.0 with probability 1.0."""
    amp, prob = path_amplitude_sum([0.5, 0.5])
    assert amp == pytest.approx(1.0)
    assert prob == pytest.approx(1.0)


def test_path_amplitude_sum_destructive():
    """Opposite amplitudes [1/2, -1/2] cancel to 0.0 with probability 0.0."""
    amp, prob = path_amplitude_sum([0.5, -0.5])
    assert amp == pytest.approx(0.0)
    assert prob == pytest.approx(0.0)


def test_path_amplitude_sum_complex():
    """Complex amplitudes [1/2, 1j/2] should give correct result."""
    amp, prob = path_amplitude_sum([0.5, 0.5j])
    expected_amp = 0.5 + 0.5j
    expected_prob = abs(expected_amp) ** 2  # 0.5
    assert amp == pytest.approx(expected_amp)
    assert prob == pytest.approx(expected_prob)


# ── compare_probability_vs_amplitude_combination ─────────────────


def test_compare_returns_dict_with_expected_structure():
    result = compare_probability_vs_amplitude_combination()
    assert isinstance(result, dict)
    expected_keys = {
        'classical_probs',
        'quantum_constructive',
        'quantum_destructive',
        'explanation',
    }
    assert set(result.keys()) == expected_keys


def test_compare_classical_probs():
    result = compare_probability_vs_amplitude_combination()
    classical = result['classical_probs']
    assert classical['paths'] == pytest.approx([0.25, 0.25])
    assert classical['total'] == pytest.approx(0.5)


def test_compare_quantum_constructive():
    result = compare_probability_vs_amplitude_combination()
    qc = result['quantum_constructive']
    assert qc['amplitudes'] == pytest.approx([0.5, 0.5])
    assert qc['probability'] == pytest.approx(1.0)


def test_compare_quantum_destructive():
    result = compare_probability_vs_amplitude_combination()
    qd = result['quantum_destructive']
    assert qd['amplitudes'] == pytest.approx([0.5, -0.5])
    assert qd['probability'] == pytest.approx(0.0)


def test_compare_explanation_is_string():
    result = compare_probability_vs_amplitude_combination()
    assert isinstance(result['explanation'], str)
    assert len(result['explanation']) > 0
