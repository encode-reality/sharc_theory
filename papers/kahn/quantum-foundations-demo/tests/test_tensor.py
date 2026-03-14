"""Tests for quantum_demo.tensor — tensor product utilities."""

import sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent.parent / 'src'))

import numpy as np
import pytest

from quantum_demo.linalg import is_normalized, ket
from quantum_demo.tensor import basis_state_bits, expand_single_qubit_gate, tensor


# ── tensor ──────────────────────────────────────────────────────────────────

class TestTensor:
    def test_two_vectors_kronecker_product(self):
        """tensor(|0>, |1>) should give |01> = [0, 1, 0, 0]."""
        v0 = ket(0, 2)
        v1 = ket(1, 2)
        result = tensor(v0, v1)
        expected = np.array([0, 1, 0, 0], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_two_vectors_general(self):
        """Kronecker product of [1, 2] and [3, 4] is [3, 4, 6, 8]."""
        a = np.array([1, 2], dtype=np.complex128)
        b = np.array([3, 4], dtype=np.complex128)
        result = tensor(a, b)
        expected = np.array([3, 4, 6, 8], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_two_matrices_gives_4x4(self):
        """Tensor of two 2x2 matrices should yield a 4x4 matrix."""
        I = np.eye(2, dtype=np.complex128)
        X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
        result = tensor(I, X)
        # I ⊗ X is block-diagonal with X blocks
        expected = np.array([
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)
        assert result.shape == (4, 4)

    def test_three_vectors(self):
        """|0> ⊗ |1> ⊗ |0> should give |010> = basis vector index 2 in dim 8."""
        v0 = ket(0, 2)
        v1 = ket(1, 2)
        result = tensor(v0, v1, v0)
        expected = ket(2, 8)  # |010> is index 2 in 8-dim space
        np.testing.assert_allclose(result, expected)

    def test_single_array_returns_itself(self):
        """Tensor of a single array is the array itself."""
        v = ket(1, 3)
        result = tensor(v)
        np.testing.assert_allclose(result, v)


# ── basis_state_bits ────────────────────────────────────────────────────────

class TestBasisStateBits:
    def test_00_gives_ket_00(self):
        """|00> = [1, 0, 0, 0]."""
        result = basis_state_bits('00')
        expected = np.array([1, 0, 0, 0], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_01_gives_ket_01(self):
        """|01> = [0, 1, 0, 0]."""
        result = basis_state_bits('01')
        expected = np.array([0, 1, 0, 0], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_10_gives_ket_10(self):
        """|10> = [0, 0, 1, 0]."""
        result = basis_state_bits('10')
        expected = np.array([0, 0, 1, 0], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_11_gives_ket_11(self):
        """|11> = [0, 0, 0, 1]."""
        result = basis_state_bits('11')
        expected = np.array([0, 0, 0, 1], dtype=np.complex128)
        np.testing.assert_allclose(result, expected)

    def test_three_qubit_101(self):
        """|101> = index 5 in dim 8."""
        result = basis_state_bits('101')
        expected = ket(5, 8)  # 101 in binary = 5
        np.testing.assert_allclose(result, expected)

    def test_results_are_normalized(self):
        """All basis states should be unit vectors."""
        for bits in ['0', '1', '00', '01', '10', '11', '000', '101', '111']:
            assert is_normalized(basis_state_bits(bits)) is True


# ── expand_single_qubit_gate ────────────────────────────────────────────────

class TestExpandSingleQubitGate:
    def test_x_on_qubit0_of_2_flips_first_qubit(self):
        """X on qubit 0 of a 2-qubit system: X ⊗ I.
        Applied to |00> should give |10>."""
        X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
        gate_full = expand_single_qubit_gate(X, target=0, num_qubits=2)
        assert gate_full.shape == (4, 4)

        ket_00 = basis_state_bits('00')
        ket_10 = basis_state_bits('10')
        result = gate_full @ ket_00
        np.testing.assert_allclose(result, ket_10)

    def test_x_on_qubit1_of_2_flips_second_qubit(self):
        """X on qubit 1 of a 2-qubit system: I ⊗ X.
        Applied to |00> should give |01>."""
        X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
        gate_full = expand_single_qubit_gate(X, target=1, num_qubits=2)

        ket_00 = basis_state_bits('00')
        ket_01 = basis_state_bits('01')
        result = gate_full @ ket_00
        np.testing.assert_allclose(result, ket_01)

    def test_h_on_qubit1_of_2_creates_superposition(self):
        """H on qubit 1 of a 2-qubit system: I ⊗ H.
        Applied to |00> should give |0>(|0>+|1>)/sqrt(2) = (|00>+|01>)/sqrt(2)."""
        H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=np.complex128)
        gate_full = expand_single_qubit_gate(H, target=1, num_qubits=2)

        ket_00 = basis_state_bits('00')
        result = gate_full @ ket_00
        expected = (1 / np.sqrt(2)) * (basis_state_bits('00') + basis_state_bits('01'))
        np.testing.assert_allclose(result, expected, atol=1e-12)

    def test_z_on_qubit0_of_3(self):
        """Z on qubit 0 of a 3-qubit system: Z ⊗ I ⊗ I.
        Applied to |100> should give -|100>."""
        Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
        gate_full = expand_single_qubit_gate(Z, target=0, num_qubits=3)
        assert gate_full.shape == (8, 8)

        ket_100 = basis_state_bits('100')
        result = gate_full @ ket_100
        np.testing.assert_allclose(result, -ket_100)

    def test_x_on_middle_qubit_of_3(self):
        """X on qubit 1 of a 3-qubit system: I ⊗ X ⊗ I.
        Applied to |000> should give |010>."""
        X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
        gate_full = expand_single_qubit_gate(X, target=1, num_qubits=3)
        assert gate_full.shape == (8, 8)

        ket_000 = basis_state_bits('000')
        ket_010 = basis_state_bits('010')
        result = gate_full @ ket_000
        np.testing.assert_allclose(result, ket_010)

    def test_single_qubit_system(self):
        """Expanding a gate in a 1-qubit system should return the gate itself."""
        H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=np.complex128)
        gate_full = expand_single_qubit_gate(H, target=0, num_qubits=1)
        np.testing.assert_allclose(gate_full, H)
