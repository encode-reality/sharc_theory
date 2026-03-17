"""Tensor product utilities for multi-qubit quantum systems."""

import numpy as np
from quantum_demo.linalg import ket


def tensor(*arrays: np.ndarray) -> np.ndarray:
    """Kronecker product of arbitrary number of arrays.

    Uses ``np.kron`` repeatedly (left fold).

    Parameters
    ----------
    *arrays : np.ndarray
        Two or more arrays (vectors or matrices) to combine.

    Returns
    -------
    np.ndarray
        The Kronecker product of all inputs.
    """
    result = arrays[0]
    for arr in arrays[1:]:
        result = np.kron(result, arr)
    return result


def basis_state_bits(bits: str) -> np.ndarray:
    """Return computational basis state corresponding to a bitstring.

    Parameters
    ----------
    bits : str
        A string of '0' and '1' characters, e.g. ``'101'``.
        Each character specifies one qubit (left = most significant).

    Returns
    -------
    np.ndarray
        The tensor product of single-qubit basis states,
        e.g. ``basis_state_bits('10')`` returns |1> ⊗ |0>.
    """
    qubit_kets = [ket(int(b), 2) for b in bits]
    return tensor(*qubit_kets)


def expand_single_qubit_gate(gate: np.ndarray, target: int, num_qubits: int) -> np.ndarray:
    """Lift a single-qubit gate to the full multi-qubit Hilbert space.

    Places *gate* on the *target* qubit and identity on all other qubits,
    then takes the tensor (Kronecker) product.

    Parameters
    ----------
    gate : np.ndarray
        A 2x2 unitary matrix representing a single-qubit gate.
    target : int
        Index of the qubit the gate acts on.
        ``target=0`` is the leftmost (most significant) qubit.
    num_qubits : int
        Total number of qubits in the system.

    Returns
    -------
    np.ndarray
        A (2^n x 2^n) matrix representing the gate in the full space.
    """
    I = np.eye(2, dtype=np.complex128)
    factors = [I] * num_qubits
    factors[target] = gate
    return tensor(*factors)
