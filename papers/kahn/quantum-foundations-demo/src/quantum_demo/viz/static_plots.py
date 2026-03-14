"""Static plotting utilities for quantum demos.

All functions return matplotlib Figure objects and support export to PNG/SVG.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def plot_probabilities(
    probabilities: np.ndarray,
    labels: list[str] | None = None,
    title: str = "",
    ax: plt.Axes | None = None,
) -> Figure:
    """Bar chart of a probability distribution.

    Parameters
    ----------
    probabilities : array of non-negative reals summing to 1
    labels : optional tick labels for each bar
    title : plot title
    ax : optional existing axes to draw on
    """
    dim = len(probabilities)
    if labels is None:
        labels = [str(i) for i in range(dim)]

    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(max(4, dim * 0.8), 3))
    else:
        fig = ax.get_figure()

    colors = ["#4C72B0"] * dim
    ax.bar(labels, probabilities, color=colors, edgecolor="black", linewidth=0.5)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Probability")
    ax.set_title(title)
    ax.axhline(y=0, color="black", linewidth=0.5)
    fig.tight_layout()
    return fig


def plot_real_amplitudes(
    state: np.ndarray,
    labels: list[str] | None = None,
    title: str = "",
    ax: plt.Axes | None = None,
) -> Figure:
    """Signed bar chart for real-valued amplitude vectors.

    Bars extend above/below zero to make sign structure visible.
    """
    dim = len(state)
    if labels is None:
        labels = [str(i) for i in range(dim)]

    values = np.real(state)

    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(max(4, dim * 0.8), 3))
    else:
        fig = ax.get_figure()

    colors = ["#55A868" if v >= 0 else "#C44E52" for v in values]
    ax.bar(labels, values, color=colors, edgecolor="black", linewidth=0.5)
    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.set_ylabel("Amplitude (real)")
    ax.set_title(title)
    y_max = max(abs(values.min()), abs(values.max()), 0.1) * 1.2
    ax.set_ylim(-y_max, y_max)
    fig.tight_layout()
    return fig


def plot_complex_amplitudes(
    state: np.ndarray,
    labels: list[str] | None = None,
    title: str = "",
) -> Figure:
    """Three-panel plot: real part, imaginary part, and |amplitude|^2.

    For complex state vectors where both parts matter.
    """
    dim = len(state)
    if labels is None:
        labels = [str(i) for i in range(dim)]

    real_parts = np.real(state)
    imag_parts = np.imag(state)
    probs = np.abs(state) ** 2

    fig, axes = plt.subplots(1, 3, figsize=(max(10, dim * 2), 3))

    # Real part
    colors_r = ["#55A868" if v >= 0 else "#C44E52" for v in real_parts]
    axes[0].bar(labels, real_parts, color=colors_r, edgecolor="black", linewidth=0.5)
    axes[0].axhline(y=0, color="black", linewidth=0.8)
    axes[0].set_ylabel("Re(amplitude)")
    axes[0].set_title("Real Part")

    # Imaginary part
    colors_i = ["#5599CC" if v >= 0 else "#CC8855" for v in imag_parts]
    axes[1].bar(labels, imag_parts, color=colors_i, edgecolor="black", linewidth=0.5)
    axes[1].axhline(y=0, color="black", linewidth=0.8)
    axes[1].set_ylabel("Im(amplitude)")
    axes[1].set_title("Imaginary Part")

    # Probabilities
    axes[2].bar(labels, probs, color="#4C72B0", edgecolor="black", linewidth=0.5)
    axes[2].set_ylim(0, 1.05)
    axes[2].set_ylabel("Probability")
    axes[2].set_title("|amplitude|²")

    fig.suptitle(title, fontsize=12, y=1.02)
    fig.tight_layout()
    return fig


def plot_qubit_state_2d(
    state: np.ndarray,
    title: str = "",
    ax: plt.Axes | None = None,
) -> Figure:
    """Unit-circle plot for a real-valued single-qubit state.

    Shows the state vector on the unit circle with projections
    onto |0> and |1> axes, overlaying the corresponding probabilities.
    """
    alpha = float(np.real(state[0]))
    beta = float(np.real(state[1]))

    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(5, 5))
    else:
        fig = ax.get_figure()

    # Unit circle
    theta = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(theta), np.sin(theta), "k-", linewidth=0.5, alpha=0.3)

    # Axes
    ax.axhline(0, color="gray", linewidth=0.3)
    ax.axvline(0, color="gray", linewidth=0.3)

    # State vector
    ax.annotate(
        "",
        xy=(alpha, beta),
        xytext=(0, 0),
        arrowprops=dict(arrowstyle="->", color="#C44E52", lw=2),
    )

    # Projections
    ax.plot([alpha, alpha], [0, beta], "k--", linewidth=0.8, alpha=0.5)
    ax.plot([0, alpha], [beta, beta], "k--", linewidth=0.8, alpha=0.5)

    # Labels
    ax.text(1.08, 0, "|0⟩", fontsize=12, ha="left", va="center")
    ax.text(0, 1.08, "|1⟩", fontsize=12, ha="center", va="bottom")

    # Probability annotations
    p0 = alpha**2
    p1 = beta**2
    ax.text(
        0.6, -0.15,
        f"P(0) = {p0:.3f}",
        fontsize=9, ha="center", color="#4C72B0",
    )
    ax.text(
        -0.15, 0.6,
        f"P(1) = {p1:.3f}",
        fontsize=9, ha="center", va="center", rotation=90, color="#4C72B0",
    )

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect("equal")
    ax.set_title(title)
    fig.tight_layout()
    return fig


def plot_classical_vs_quantum_panel(
    classical_probs: np.ndarray,
    quantum_state: np.ndarray,
    labels: list[str] | None = None,
    title: str = "",
) -> Figure:
    """Side-by-side comparison: classical probabilities vs quantum amplitudes + probabilities.

    Left panel: classical probability bars.
    Middle panel: quantum amplitude bars (signed).
    Right panel: quantum measurement probabilities (Born rule).
    """
    dim = len(classical_probs)
    if labels is None:
        labels = [str(i) for i in range(dim)]

    quantum_probs = np.abs(quantum_state) ** 2
    amplitudes = np.real(quantum_state)

    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))

    # Classical
    axes[0].bar(labels, classical_probs, color="#4C72B0", edgecolor="black", linewidth=0.5)
    axes[0].set_ylim(0, 1.05)
    axes[0].set_ylabel("Probability")
    axes[0].set_title("Classical Distribution")

    # Quantum amplitudes
    colors = ["#55A868" if v >= 0 else "#C44E52" for v in amplitudes]
    axes[1].bar(labels, amplitudes, color=colors, edgecolor="black", linewidth=0.5)
    axes[1].axhline(y=0, color="black", linewidth=0.8)
    axes[1].set_ylabel("Amplitude")
    axes[1].set_title("Quantum Amplitudes")
    y_max = max(abs(amplitudes.min()), abs(amplitudes.max()), 0.1) * 1.2
    axes[1].set_ylim(-y_max, y_max)

    # Quantum probabilities
    axes[2].bar(labels, quantum_probs, color="#8172B2", edgecolor="black", linewidth=0.5)
    axes[2].set_ylim(0, 1.05)
    axes[2].set_ylabel("Probability")
    axes[2].set_title("Quantum Probabilities (Born)")

    fig.suptitle(title, fontsize=12, y=1.02)
    fig.tight_layout()
    return fig
