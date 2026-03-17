"""Quantum interference demonstrations for pedagogical quantum mechanics."""

import numpy as np
from quantum_demo.linalg import ket
from quantum_demo.states import amplitudes_to_probabilities
from quantum_demo.gates import H, Z, apply_gate


def hadamard_interference_demo() -> dict:
    """
    Return intermediate states showing H|0>, HZH|0>, HH|0>, etc.
    Use this to demonstrate constructive and destructive interference.

    Returns dict with keys:
    - 'ket0': initial |0> state
    - 'H_ket0': H|0> state (equal superposition)
    - 'H_ket0_probs': probabilities of H|0>
    - 'HH_ket0': HH|0> state (back to |0>)
    - 'HH_ket0_probs': probabilities of HH|0>
    - 'Z_H_ket0': ZH|0> (phase flip on superposition)
    - 'Z_H_ket0_probs': probabilities (still 50/50!)
    - 'HZH_ket0': HZH|0> (goes to |1>)
    - 'HZH_ket0_probs': probabilities of HZH|0>
    """
    ket0 = ket(0, 2)

    # Step 1: H|0> — equal superposition
    h_ket0 = apply_gate(ket0, H)
    h_ket0_probs = amplitudes_to_probabilities(h_ket0)

    # Step 2: HH|0> — constructive interference brings us back to |0>
    hh_ket0 = apply_gate(h_ket0, H)
    hh_ket0_probs = amplitudes_to_probabilities(hh_ket0)

    # Step 3: ZH|0> — phase flip on superposition (probabilities unchanged)
    z_h_ket0 = apply_gate(h_ket0, Z)
    z_h_ket0_probs = amplitudes_to_probabilities(z_h_ket0)

    # Step 4: HZH|0> — destructive interference on |0>, giving |1>
    hzh_ket0 = apply_gate(z_h_ket0, H)
    hzh_ket0_probs = amplitudes_to_probabilities(hzh_ket0)

    return {
        'ket0': ket0,
        'H_ket0': h_ket0,
        'H_ket0_probs': h_ket0_probs,
        'HH_ket0': hh_ket0,
        'HH_ket0_probs': hh_ket0_probs,
        'Z_H_ket0': z_h_ket0,
        'Z_H_ket0_probs': z_h_ket0_probs,
        'HZH_ket0': hzh_ket0,
        'HZH_ket0_probs': hzh_ket0_probs,
    }


def path_amplitude_sum(contributions: list[complex]) -> tuple[complex, float]:
    """Sum amplitudes first, then compute squared magnitude.

    This illustrates the core quantum rule: add amplitudes (which can
    cancel or reinforce), then square to get probability.

    Returns (total_amplitude, probability).
    """
    total_amplitude = sum(contributions)
    probability = float(abs(total_amplitude) ** 2)
    return total_amplitude, probability


def compare_probability_vs_amplitude_combination() -> dict:
    """
    Build a tiny example showing that classical probabilities only add,
    whereas signed/complex amplitudes can cancel or reinforce.

    Returns dict with keys:
    - 'classical_probs': two paths with probabilities [0.25, 0.25], sum = 0.5
    - 'quantum_constructive': amplitudes [0.5, 0.5], |sum|^2 = 1.0
    - 'quantum_destructive': amplitudes [0.5, -0.5], |sum|^2 = 0.0
    - 'explanation': string explaining the contrast
    """
    # Classical: probabilities simply add
    classical_paths = [0.25, 0.25]
    classical_total = sum(classical_paths)

    # Quantum constructive: same-sign amplitudes reinforce
    constructive_amps = [0.5, 0.5]
    _, constructive_prob = path_amplitude_sum(constructive_amps)

    # Quantum destructive: opposite-sign amplitudes cancel
    destructive_amps = [0.5, -0.5]
    _, destructive_prob = path_amplitude_sum(destructive_amps)

    explanation = (
        "Classical probabilities are non-negative and can only add, "
        "so two paths with probability 0.25 each always give total 0.5. "
        "Quantum amplitudes are signed (or complex) and sum before squaring: "
        "same-sign amplitudes reinforce (0.5 + 0.5 = 1.0, P = 1.0), "
        "while opposite-sign amplitudes cancel (0.5 - 0.5 = 0.0, P = 0.0). "
        "This is the essence of quantum interference."
    )

    return {
        'classical_probs': {
            'paths': classical_paths,
            'total': classical_total,
        },
        'quantum_constructive': {
            'amplitudes': constructive_amps,
            'probability': constructive_prob,
        },
        'quantum_destructive': {
            'amplitudes': destructive_amps,
            'probability': destructive_prob,
        },
        'explanation': explanation,
    }
