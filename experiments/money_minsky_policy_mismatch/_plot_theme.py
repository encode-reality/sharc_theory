"""Polished plotting theme — editorial-quality dark figures via seaborn + matplotlib.

Centralizes:
  - Color palette (consistent across all figures)
  - Theme application (fonts, gridlines, axis spines, legend frame)
  - Annotation helpers (shock markers, callouts, shaded regions)
  - Standard figure sizes and DPI

Inspired by Financial Times / Economist editorial graphics conventions:
  • One-line subtitle inside the figure beneath the bold title
  • Sparing gridlines, hairline spines
  • Annotations point at the moment the headline happens
  • Color used for meaning, not decoration
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# ---------------------------------------------------------------------------
# Palette (semantic, not decorative)
# ---------------------------------------------------------------------------

PALETTE = {
    # Entity-type colors (used across comparative + policy plots)
    "household":          "#ff6b6b",  # warm red
    "currency_user":      "#ffa94d",  # amber
    "sovereign_issuer":   "#51cf66",  # bright green
    # Policy controllers
    "austerity":          "#ff6b6b",
    "functional_finance": "#51cf66",
    "passive":            "#adb5bd",  # neutral grey
    # Capacity / external
    "slack":              "#51cf66",
    "tight":              "#ff6b6b",
    "capacity_line":      "#868e96",
    "inflation":          "#ff8787",
    "output":             "#74c0fc",
    # Holder types
    "holder_household":   "#51cf66",
    "holder_asset":       "#ff6b6b",
    "holder_foreign":     "#ffa94d",
    "holder_cb":          "#74c0fc",
    # Annotations
    "shock":              "#ffd43b",
    "annotation":         "#e9ecef",
    "muted":              "#868e96",
}

# Background colors for editorial dark theme
BG_FIGURE = "#1a1d23"
BG_AXES   = "#22262e"
FG_TEXT   = "#e9ecef"
FG_MUTED  = "#adb5bd"
FG_GRID   = "#2e333c"
FG_SPINE  = "#3d434d"

# Standard figure dimensions
FIG_WIDTH  = 14
FIG_HEIGHT = 5
FIG_DPI    = 160


# ---------------------------------------------------------------------------
# Theme application
# ---------------------------------------------------------------------------

def apply_theme():
    """Apply the polished dark theme globally for the current process."""
    sns.set_theme(context="paper", style="darkgrid")

    mpl.rcParams.update({
        # Figure / axes background
        "figure.facecolor":   BG_FIGURE,
        "axes.facecolor":     BG_AXES,
        "savefig.facecolor":  BG_FIGURE,
        "savefig.edgecolor":  BG_FIGURE,

        # Spines
        "axes.edgecolor":     FG_SPINE,
        "axes.linewidth":     0.8,
        "axes.spines.top":    False,
        "axes.spines.right":  False,

        # Gridlines — sparing
        "axes.grid":          True,
        "axes.grid.axis":     "y",
        "grid.color":         FG_GRID,
        "grid.linewidth":     0.6,
        "grid.alpha":         0.7,

        # Text
        "text.color":         FG_TEXT,
        "axes.labelcolor":    FG_TEXT,
        "axes.titlecolor":    FG_TEXT,
        "xtick.color":        FG_MUTED,
        "ytick.color":        FG_MUTED,
        "xtick.labelsize":    9,
        "ytick.labelsize":    9,
        "axes.labelsize":     10,
        "axes.titlesize":     12,
        "axes.titleweight":   "bold",
        "axes.titlepad":      10,

        # Font
        "font.family":        "sans-serif",
        "font.sans-serif":    ["Inter", "Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size":          10,

        # Ticks
        "xtick.major.size":   3,
        "ytick.major.size":   3,
        "xtick.major.width":  0.8,
        "ytick.major.width":  0.8,
        "xtick.direction":    "out",
        "ytick.direction":    "out",

        # Legend
        "legend.frameon":     True,
        "legend.facecolor":   BG_FIGURE,
        "legend.edgecolor":   FG_SPINE,
        "legend.framealpha":  0.85,
        "legend.fontsize":    9,

        # Lines
        "lines.linewidth":    2.0,
        "lines.solid_capstyle": "round",

        # Saved figure
        "savefig.dpi":        FIG_DPI,
        "savefig.bbox":       "tight",
        "savefig.pad_inches": 0.25,
    })


# ---------------------------------------------------------------------------
# Figure / layout helpers
# ---------------------------------------------------------------------------

def make_figure(
    n_panels: int = 3,
    figsize: Optional[Tuple[float, float]] = None,
    title: str = "",
    subtitle: str = "",
):
    """Create a standardized multi-panel figure with title + subtitle.

    Returns (fig, axes).  axes is always a 1D array even if n_panels=1.
    """
    if figsize is None:
        figsize = (FIG_WIDTH, FIG_HEIGHT)

    fig, axes = plt.subplots(1, n_panels, figsize=figsize, dpi=FIG_DPI)
    if n_panels == 1:
        axes = [axes]

    # Title + subtitle (editorial style)
    if title:
        fig.suptitle(title, fontsize=15, fontweight="bold",
                      color=FG_TEXT, y=1.04, x=0.05, ha="left")
    if subtitle:
        fig.text(0.05, 0.98, subtitle, fontsize=10.5, color=FG_MUTED,
                  style="italic", ha="left", va="top")

    return fig, axes


def style_panel(ax, title: str = "", xlabel: str = "Period", ylabel: str = ""):
    """Apply per-panel polish: title left-aligned, labels in muted color."""
    if title:
        ax.set_title(title, loc="left", fontsize=11, fontweight="bold",
                     color=FG_TEXT, pad=8)
    if xlabel:
        ax.set_xlabel(xlabel, color=FG_MUTED, fontsize=9.5)
    if ylabel:
        ax.set_ylabel(ylabel, color=FG_MUTED, fontsize=9.5)
    ax.tick_params(colors=FG_MUTED)
    for spine in ax.spines.values():
        spine.set_color(FG_SPINE)


# ---------------------------------------------------------------------------
# Annotation helpers
# ---------------------------------------------------------------------------

def add_shock_marker(ax, period: float, label: str = "shock",
                     color: Optional[str] = None, top_label: bool = True):
    """Vertical dashed line marking a shock or regime change."""
    if color is None:
        color = PALETTE["shock"]
    ax.axvline(period, color=color, linestyle="--", linewidth=1.0,
               alpha=0.7, zorder=1)
    if label:
        ymin, ymax = ax.get_ylim()
        y_pos = ymax - (ymax - ymin) * 0.04 if top_label else ymin + (ymax - ymin) * 0.04
        ax.text(period, y_pos, f" {label}", color=color, fontsize=8.5,
                ha="left", va="top" if top_label else "bottom",
                fontweight="bold", alpha=0.9)


def add_callout(ax, x: float, y: float, text: str,
                xytext: Optional[Tuple[float, float]] = None,
                color: Optional[str] = None):
    """Add a labeled callout pointing at (x, y)."""
    if color is None:
        color = PALETTE["annotation"]
    if xytext is None:
        xytext = (10, 10)

    ax.annotate(
        text,
        xy=(x, y),
        xytext=xytext,
        textcoords="offset points",
        fontsize=8.5,
        color=color,
        ha="left",
        va="bottom",
        arrowprops=dict(
            arrowstyle="->",
            color=color,
            lw=0.8,
            alpha=0.7,
        ),
        bbox=dict(boxstyle="round,pad=0.3", facecolor=BG_FIGURE,
                  edgecolor=FG_SPINE, alpha=0.85),
    )


def add_band(ax, period_start: float, period_end: float,
             color: Optional[str] = None, alpha: float = 0.1, label: str = ""):
    """Shade a horizontal time region."""
    if color is None:
        color = PALETTE["shock"]
    ax.axvspan(period_start, period_end, color=color, alpha=alpha,
               zorder=0, label=label if label else None)


def add_horizontal_threshold(ax, y: float, label: str = "",
                              color: Optional[str] = None):
    """Horizontal dashed reference line (e.g., capacity, rate cap)."""
    if color is None:
        color = PALETTE["muted"]
    ax.axhline(y, color=color, linestyle=":", linewidth=1.0,
               alpha=0.8, zorder=1)
    if label:
        xmin, xmax = ax.get_xlim()
        ax.text(xmax * 0.98, y, f" {label} ", color=color, fontsize=8.5,
                ha="right", va="bottom", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", facecolor=BG_AXES,
                          edgecolor="none", alpha=0.85))


def polish_legend(ax, loc: str = "best", title: Optional[str] = None):
    """Apply consistent legend styling."""
    leg = ax.legend(loc=loc, title=title, frameon=True,
                    facecolor=BG_FIGURE, edgecolor=FG_SPINE,
                    framealpha=0.9, fontsize=9)
    if leg is not None:
        for text in leg.get_texts():
            text.set_color(FG_TEXT)
        if leg.get_title() is not None:
            leg.get_title().set_color(FG_TEXT)
            leg.get_title().set_fontsize(9)
            leg.get_title().set_fontweight("bold")


@contextmanager
def themed():
    """Context manager: apply theme, restore previous rcParams on exit."""
    saved = mpl.rcParams.copy()
    try:
        apply_theme()
        yield
    finally:
        mpl.rcParams.update(saved)
