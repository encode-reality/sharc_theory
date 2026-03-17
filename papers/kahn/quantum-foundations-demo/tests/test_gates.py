"""Tests for quantum gate constants and utility functions."""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'src'))

import numpy as np
import pytest
from quantum_demo.linalg import ket, is_unitary
from quantum_demo.gates import (
    I2, X, Y, Z, H, S, T, CNOT,
    apply_gate, phase_oracle, diffusion_operator,
)


# ── Gate unitarity ──────────────────────────────────────────────────

@pytest.mark.parametrize("gate,name", [
    (I2, "I2"), (X, "X"), (Y, "Y"), (Z, "Z"),
    (H, "H"), (S, "S"), (T, "T"), (CNOT, "CNOT"),
])
def test_all_gates_are_unitary(gate, name):
    assert is_unitary(gate), f"{name} gate is not unitary"


# ── X gate (bit flip) ──────────────────────────────────────────────

def test_x_flips_zero_to_one():
    ket0 = ket(0, 2)
    ket1 = ket(1, 2)
    result = X @ ket0
    np.testing.assert_allclose(result, ket1)


def test_x_flips_one_to_zero():
    ket0 = ket(0, 2)
    ket1 = ket(1, 2)
    result = X @ ket1
    np.testing.assert_allclose(result, ket0)


# ── Z gate (phase flip) ───────────────────────────────────────────

def test_z_leaves_zero_unchanged():
    ket0 = ket(0, 2)
    result = Z @ ket0
    np.testing.assert_allclose(result, ket0)


def test_z_flips_phase_of_one():
    ket1 = ket(1, 2)
    result = Z @ ket1
    np.testing.assert_allclose(result, -ket1)


# ── H gate (Hadamard) ─────────────────────────────────────────────

def test_h_creates_equal_superposition():
    ket0 = ket(0, 2)
    ket1 = ket(1, 2)
    expected = (ket0 + ket1) / np.sqrt(2)
    result = H @ ket0
    np.testing.assert_allclose(result, expected)


def test_h_is_own_inverse():
    result = H @ H
    np.testing.assert_allclose(result, I2, atol=1e-12)


# ── CNOT gate ──────────────────────────────────────────────────────

def test_cnot_is_4x4():
    assert CNOT.shape == (4, 4)


def test_cnot_computational_basis():
    # |00> -> |00>
    ket00 = np.kron(ket(0, 2), ket(0, 2))
    np.testing.assert_allclose(CNOT @ ket00, ket00)
    # |01> -> |01>
    ket01 = np.kron(ket(0, 2), ket(1, 2))
    np.testing.assert_allclose(CNOT @ ket01, ket01)
    # |10> -> |11>
    ket10 = np.kron(ket(1, 2), ket(0, 2))
    ket11 = np.kron(ket(1, 2), ket(1, 2))
    np.testing.assert_allclose(CNOT @ ket10, ket11)
    # |11> -> |10>
    np.testing.assert_allclose(CNOT @ ket11, ket10)


# ── apply_gate ─────────────────────────────────────────────────────

def test_apply_gate_multiplies_correctly():
    ket0 = ket(0, 2)
    result = apply_gate(ket0, X)
    np.testing.assert_allclose(result, ket(1, 2))


# ── phase_oracle ───────────────────────────────────────────────────

def test_phase_oracle_flips_target_only():
    dim = 4
    oracle = phase_oracle(2, dim)
    state = np.ones(dim, dtype=np.complex128) / 2.0  # equal superposition
    result = oracle @ state
    expected = state.copy()
    expected[2] = -expected[2]
    np.testing.assert_allclose(result, expected)


def test_phase_oracle_is_diagonal():
    dim = 4
    oracle = phase_oracle(1, dim)
    # Off-diagonal elements should be zero
    assert oracle.shape == (dim, dim)
    for i in range(dim):
        for j in range(dim):
            if i != j:
                assert oracle[i, j] == 0.0


def test_phase_oracle_diagonal_values():
    dim = 8
    target = 3
    oracle = phase_oracle(target, dim)
    for i in range(dim):
        if i == target:
            assert oracle[i, i] == -1.0
        else:
            assert oracle[i, i] == 1.0


# ── diffusion_operator ────────────────────────────────────────────

def test_diffusion_operator_formula():
    dim = 4
    D = diffusion_operator(dim)
    # |s> = equal superposition
    s = np.ones(dim, dtype=np.complex128) / np.sqrt(dim)
    expected = 2.0 * np.outer(s, s) - np.eye(dim, dtype=np.complex128)
    np.testing.assert_allclose(D, expected, atol=1e-12)


def test_diffusion_operator_is_unitary():
    D = diffusion_operator(4)
    assert is_unitary(D)


def test_diffusion_operator_shape():
    D = diffusion_operator(8)
    assert D.shape == (8, 8)
