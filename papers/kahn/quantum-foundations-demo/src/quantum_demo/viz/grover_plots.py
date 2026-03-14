"""Grover-specific visualization utilities."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


def plot_grover_trajectory(
    probabilities: np.ndarray,
    title: str = "Grover: Target Probability vs Iteration",
    ax: plt.Axes | None = None,
) -> Figure:
    """Plot probability of the marked state across Grover iterations.

    Parameters
    ----------
    probabilities : 1D array, probabilities[i] = P(target) after i iterations
    """
    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 4))
    else:
        fig = ax.get_figure()

    iterations = np.arange(len(probabilities))
    ax.plot(iterations, probabilities, "o-", color="#C44E52", linewidth=2, markersize=6)
    ax.set_xlabel("Iteration")
    ax.set_ylabel("P(target)")
    ax.set_title(title)
    ax.set_ylim(-0.05, 1.05)
    ax.axhline(y=1.0, color="gray", linestyle="--", linewidth=0.5)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def plot_grover_plane(
    coords: list[tuple[float, float]],
    title: str = "Grover Geometry: State Rotation in 2D Plane",
    ax: plt.Axes | None = None,
) -> Figure:
    """Visualize Grover's algorithm as rotation in the 2D reduced plane.

    Parameters
    ----------
    coords : list of (x, y) tuples where
             x = component along |target>
             y = component along |s_perp> (non-target superposition)
    """
    fig = None
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))
    else:
        fig = ax.get_figure()

    # Unit circle (quarter arc in the first quadrant)
    theta = np.linspace(0, np.pi / 2, 100)
    ax.plot(np.cos(theta), np.sin(theta), "k-", linewidth=0.5, alpha=0.3)

    # Plot state trajectory
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]

    # Draw vectors from origin
    for i, (x, y) in enumerate(coords):
        alpha_val = 0.3 + 0.7 * (i / max(len(coords) - 1, 1))
        color = plt.cm.RdYlGn(i / max(len(coords) - 1, 1))
        ax.annotate(
            "",
            xy=(x, y),
            xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=color, lw=1.5, alpha=alpha_val),
        )
        ax.plot(x, y, "o", color=color, markersize=6, zorder=5)
        ax.annotate(f"  iter {i}", (x, y), fontsize=7, alpha=0.8)

    # Connect points
    ax.plot(xs, ys, "--", color="gray", linewidth=0.8, alpha=0.5)

    # Axis labels
    ax.set_xlabel("|target⟩ component", fontsize=11)
    ax.set_ylabel("|s⊥⟩ component", fontsize=11)
    ax.set_title(title)
    ax.set_xlim(-0.1, 1.15)
    ax.set_ylim(-0.1, 1.15)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    return fig
