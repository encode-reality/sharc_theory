"""Export utilities for saving figures to disk."""

from pathlib import Path
from matplotlib.figure import Figure


def save_figure(
    fig: Figure,
    path: str | Path,
    formats: list[str] | None = None,
    dpi: int = 150,
) -> list[Path]:
    """Save a matplotlib figure in one or more formats.

    Parameters
    ----------
    fig : matplotlib Figure
    path : base path without extension (e.g., 'assets/blog/my_plot')
    formats : list of extensions like ['png', 'svg']. Defaults to ['png'].
    dpi : resolution for raster formats

    Returns
    -------
    List of paths that were written.
    """
    if formats is None:
        formats = ["png"]

    base = Path(path)
    base.parent.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    for fmt in formats:
        out_path = base.with_suffix(f".{fmt}")
        fig.savefig(str(out_path), dpi=dpi, bbox_inches="tight", format=fmt)
        written.append(out_path)

    return written
