"""State-specific visualization utilities."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def plot_state_comparison(
    states: list[np.ndarray],
    state_labels: list[str],
    basis_labels: list[str] | None = None,
    title: str = "",
) -> Figure:
    """Compare multiple quantum states side by side.

    Each state gets two sub-plots: amplitudes and probabilities.
    Useful for Demo A (same probabilities, different states).
    """
    n_states = len(states)
    dim = len(states[0])
    if basis_labels is None:
        basis_labels = [str(i) for i in range(dim)]

    fig, axes = plt.subplots(2, n_states, figsize=(4 * n_states, 6))
    if n_states == 1:
        axes = axes.reshape(-1, 1)

    for col, (state, label) in enumerate(zip(states, state_labels)):
        amps = np.real(state)
        probs = np.abs(state) ** 2

        # Amplitude row
        colors = ["#55A868" if v >= 0 else "#C44E52" for v in amps]
        axes[0, col].bar(basis_labels, amps, color=colors, edgecolor="black", linewidth=0.5)
        axes[0, col].axhline(0, color="black", linewidth=0.8)
        axes[0, col].set_title(f"{label}\n(amplitudes)")
        axes[0, col].set_ylim(-1.1, 1.1)

        # Probability row
        axes[1, col].bar(basis_labels, probs, color="#4C72B0", edgecolor="black", linewidth=0.5)
        axes[1, col].set_ylim(0, 1.05)
        axes[1, col].set_title(f"{label}\n(probabilities)")

    fig.suptitle(title, fontsize=13, y=1.02)
    fig.tight_layout()
    return fig


def plot_oracle_phase_demo(
    before_oracle: np.ndarray,
    after_oracle: np.ndarray,
    after_diffusion: np.ndarray,
    target_index: int,
    labels: list[str] | None = None,
    title: str = "Oracle Phase Flip Is Invisible — Until Diffusion",
) -> Figure:
    """Demo C visualization: oracle phase flip doesn't change probabilities,
    but after diffusion the target probability increases.

    Shows 3 columns x 2 rows (amplitudes + probabilities).
    """
    dim = len(before_oracle)
    if labels is None:
        labels = [str(i) for i in range(dim)]

    stages = [before_oracle, after_oracle, after_diffusion]
    stage_names = ["Before Oracle", "After Oracle", "After Diffusion"]

    fig, axes = plt.subplots(2, 3, figsize=(12, 5))

    for col, (state, name) in enumerate(zip(stages, stage_names)):
        amps = np.real(state)
        probs = np.abs(state) ** 2

        # Amplitudes
        colors = ["#55A868" if v >= 0 else "#C44E52" for v in amps]
        colors[target_index] = "#DD8800"  # highlight target
        axes[0, col].bar(labels, amps, color=colors, edgecolor="black", linewidth=0.5)
        axes[0, col].axhline(0, color="black", linewidth=0.8)
        axes[0, col].set_title(f"{name}\n(amplitudes)")
        y_max = max(abs(amps.min()), abs(amps.max()), 0.1) * 1.3
        axes[0, col].set_ylim(-y_max, y_max)

        # Probabilities
        bar_colors = ["#4C72B0"] * dim
        bar_colors[target_index] = "#DD8800"
        axes[1, col].bar(labels, probs, color=bar_colors, edgecolor="black", linewidth=0.5)
        axes[1, col].set_ylim(0, max(probs) * 1.3)
        axes[1, col].set_title(f"{name}\n(probabilities)")

    fig.suptitle(title, fontsize=13, y=1.02)
    fig.tight_layout()
    return fig
