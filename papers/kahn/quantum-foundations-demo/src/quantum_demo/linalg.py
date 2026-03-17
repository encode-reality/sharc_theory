"""Linear algebra utilities for pedagogical quantum mechanics."""

import numpy as np


def normalize(vec: np.ndarray) -> np.ndarray:
    """Return *vec* normalized to unit L2 norm.

    Raises
    ------
    ValueError
        If *vec* is the zero vector (norm is zero).
    """
    norm = np.linalg.norm(vec)
    if norm == 0.0:
        raise ValueError("Cannot normalize the zero vector.")
    return vec / norm


def is_normalized(vec: np.ndarray, atol: float = 1e-9) -> bool:
    """Check whether *vec* has unit L2 norm within absolute tolerance *atol*."""
    return bool(abs(np.linalg.norm(vec) - 1.0) <= atol)


def ket(index: int, dim: int, dtype=np.complex128) -> np.ndarray:
    """Return computational basis vector |index> in C^dim.

    Parameters
    ----------
    index : int
        Basis index (must satisfy 0 <= index < dim).
    dim : int
        Dimension of the Hilbert space.
    dtype : numpy dtype, optional
        Data type of the returned array (default ``np.complex128``).

    Raises
    ------
    ValueError
        If *index* is out of range [0, dim).
    """
    if index < 0 or index >= dim:
        raise ValueError(
            f"index {index} out of range for dimension {dim} "
            f"(must be 0 <= index < {dim})."
        )
    vec = np.zeros(dim, dtype=dtype)
    vec[index] = 1
    return vec


def projectors_from_basis(dim: int) -> list[np.ndarray]:
    """Return computational-basis projectors |i><i| for i in range(dim).

    Each projector is a (dim, dim) matrix of dtype ``np.complex128``.
    """
    projs: list[np.ndarray] = []
    for i in range(dim):
        basis_vec = ket(i, dim)
        projs.append(np.outer(basis_vec, basis_vec.conj()))
    return projs


def dagger(mat: np.ndarray) -> np.ndarray:
    """Return the conjugate transpose (Hermitian adjoint) of *mat*."""
    return mat.conj().T


def is_unitary(mat: np.ndarray, atol: float = 1e-9) -> bool:
    """Check whether *mat* satisfies U^dagger U = I within tolerance *atol*.

    Returns ``False`` for non-square matrices.
    """
    if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
        return False
    n = mat.shape[0]
    product = dagger(mat) @ mat
    return bool(np.allclose(product, np.eye(n), atol=atol))
