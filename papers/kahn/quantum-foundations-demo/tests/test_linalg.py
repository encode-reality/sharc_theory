"""Tests for quantum_demo.linalg — linear algebra utilities."""

import numpy as np
import pytest

from quantum_demo.linalg import (
    dagger,
    is_normalized,
    is_unitary,
    ket,
    normalize,
    projectors_from_basis,
)


# ── normalize ────────────────────────────────────────────────────────────────

class TestNormalize:
    def test_real_vector(self):
        v = np.array([3.0, 4.0])
        result = normalize(v)
        assert np.linalg.norm(result) == pytest.approx(1.0)
        # direction preserved
        assert result[0] / result[1] == pytest.approx(3.0 / 4.0)

    def test_complex_vector(self):
        v = np.array([1 + 1j, 1 - 1j])
        result = normalize(v)
        assert np.linalg.norm(result) == pytest.approx(1.0)

    def test_already_normalized(self):
        v = np.array([1.0, 0.0])
        result = normalize(v)
        np.testing.assert_allclose(result, v)

    def test_higher_dimension(self):
        v = np.array([1, 2, 3, 4, 5], dtype=np.complex128)
        result = normalize(v)
        assert np.linalg.norm(result) == pytest.approx(1.0)

    def test_zero_vector_raises(self):
        v = np.array([0.0, 0.0, 0.0])
        with pytest.raises((ValueError, ZeroDivisionError, FloatingPointError)):
            normalize(v)

    def test_single_element(self):
        v = np.array([5.0 + 0j])
        result = normalize(v)
        assert np.linalg.norm(result) == pytest.approx(1.0)


# ── is_normalized ────────────────────────────────────────────────────────────

class TestIsNormalized:
    def test_unit_vector_true(self):
        v = np.array([1.0, 0.0, 0.0])
        assert is_normalized(v) is True

    def test_non_unit_vector_false(self):
        v = np.array([1.0, 1.0])
        assert is_normalized(v) is False

    def test_complex_unit_vector(self):
        v = np.array([1 / np.sqrt(2), 1j / np.sqrt(2)])
        assert is_normalized(v) is True

    def test_tolerance(self):
        v = np.array([1.0 + 1e-10, 0.0])
        assert is_normalized(v, atol=1e-9) is True

    def test_tight_tolerance_false(self):
        v = np.array([1.0 + 1e-5, 0.0])
        assert is_normalized(v, atol=1e-9) is False

    def test_zero_vector(self):
        v = np.array([0.0, 0.0])
        assert is_normalized(v) is False


# ── ket ──────────────────────────────────────────────────────────────────────

class TestKet:
    def test_ket_0_dim_2(self):
        result = ket(0, 2)
        expected = np.array([1, 0], dtype=np.complex128)
        np.testing.assert_array_equal(result, expected)

    def test_ket_1_dim_2(self):
        result = ket(1, 2)
        expected = np.array([0, 1], dtype=np.complex128)
        np.testing.assert_array_equal(result, expected)

    def test_ket_dim_4(self):
        result = ket(2, 4)
        expected = np.zeros(4, dtype=np.complex128)
        expected[2] = 1.0
        np.testing.assert_array_equal(result, expected)

    def test_ket_dtype(self):
        result = ket(0, 3)
        assert result.dtype == np.complex128

    def test_ket_custom_dtype(self):
        result = ket(0, 3, dtype=np.float64)
        assert result.dtype == np.float64

    def test_ket_is_normalized(self):
        for dim in [2, 3, 5]:
            for idx in range(dim):
                assert is_normalized(ket(idx, dim)) is True

    def test_ket_invalid_index_raises(self):
        with pytest.raises((IndexError, ValueError)):
            ket(3, 2)

    def test_ket_negative_index_raises(self):
        with pytest.raises((IndexError, ValueError)):
            ket(-1, 2)


# ── projectors_from_basis ────────────────────────────────────────────────────

class TestProjectorsFromBasis:
    def test_dim_2(self):
        projs = projectors_from_basis(2)
        assert len(projs) == 2
        # |0><0|
        np.testing.assert_allclose(projs[0], np.array([[1, 0], [0, 0]], dtype=np.complex128))
        # |1><1|
        np.testing.assert_allclose(projs[1], np.array([[0, 0], [0, 1]], dtype=np.complex128))

    def test_projectors_are_idempotent(self):
        """P^2 = P for each projector."""
        for dim in [2, 3, 4]:
            projs = projectors_from_basis(dim)
            for P in projs:
                np.testing.assert_allclose(P @ P, P, atol=1e-12)

    def test_projectors_are_hermitian(self):
        projs = projectors_from_basis(3)
        for P in projs:
            np.testing.assert_allclose(P, dagger(P), atol=1e-12)

    def test_projectors_sum_to_identity(self):
        """Completeness: sum_i |i><i| = I."""
        for dim in [2, 3, 5]:
            projs = projectors_from_basis(dim)
            total = sum(projs)
            np.testing.assert_allclose(total, np.eye(dim, dtype=np.complex128), atol=1e-12)

    def test_projectors_shape(self):
        projs = projectors_from_basis(4)
        for P in projs:
            assert P.shape == (4, 4)

    def test_projectors_orthogonal(self):
        """P_i P_j = 0 for i != j."""
        projs = projectors_from_basis(3)
        for i in range(3):
            for j in range(3):
                if i != j:
                    np.testing.assert_allclose(projs[i] @ projs[j],
                                               np.zeros((3, 3)), atol=1e-12)


# ── dagger ───────────────────────────────────────────────────────────────────

class TestDagger:
    def test_real_matrix(self):
        m = np.array([[1, 2], [3, 4]], dtype=np.float64)
        np.testing.assert_array_equal(dagger(m), m.T)

    def test_complex_matrix(self):
        m = np.array([[1 + 1j, 2], [3, 4 - 2j]])
        expected = np.array([[1 - 1j, 3], [2, 4 + 2j]])
        np.testing.assert_array_equal(dagger(m), expected)

    def test_vector(self):
        # 1-D array dagger should still conjugate (transpose is no-op for 1-D)
        v = np.array([1 + 1j, 2 - 1j])
        expected = np.array([1 - 1j, 2 + 1j])
        np.testing.assert_array_equal(dagger(v), expected)

    def test_identity_is_hermitian(self):
        I = np.eye(3, dtype=np.complex128)
        np.testing.assert_array_equal(dagger(I), I)

    def test_dagger_involutory(self):
        """(A^dagger)^dagger = A."""
        m = np.array([[1 + 2j, 3 - 4j], [5j, 6]])
        np.testing.assert_allclose(dagger(dagger(m)), m)

    def test_non_square(self):
        m = np.array([[1 + 1j, 2, 3j], [4, 5 - 1j, 6]])
        result = dagger(m)
        assert result.shape == (3, 2)
        np.testing.assert_array_equal(result, m.conj().T)


# ── is_unitary ───────────────────────────────────────────────────────────────

class TestIsUnitary:
    def test_identity_is_unitary(self):
        assert is_unitary(np.eye(3, dtype=np.complex128)) is True

    def test_pauli_x_is_unitary(self):
        X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
        assert is_unitary(X) is True

    def test_pauli_y_is_unitary(self):
        Y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
        assert is_unitary(Y) is True

    def test_pauli_z_is_unitary(self):
        Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)
        assert is_unitary(Z) is True

    def test_hadamard_is_unitary(self):
        H = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=np.complex128)
        assert is_unitary(H) is True

    def test_non_unitary_false(self):
        m = np.array([[1, 1], [0, 1]], dtype=np.complex128)  # upper triangular
        assert is_unitary(m) is False

    def test_zero_matrix_not_unitary(self):
        assert is_unitary(np.zeros((2, 2))) is False

    def test_random_unitary(self):
        """A matrix from QR decomposition of a random matrix is unitary."""
        rng = np.random.default_rng(42)
        A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
        Q, _ = np.linalg.qr(A)
        assert is_unitary(Q) is True

    def test_tolerance(self):
        I = np.eye(2, dtype=np.complex128)
        # Add small perturbation within default tolerance
        perturbed = I + 1e-11 * np.ones((2, 2))
        assert is_unitary(perturbed, atol=1e-9) is True

    def test_non_square_false(self):
        m = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.complex128)
        assert is_unitary(m) is False
