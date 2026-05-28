"""State-dependent fragility experiments built on the Keen-style ODE."""

from __future__ import annotations

from typing import Dict, List, Optional

import numpy as np

from experiments.money_minsky_policy_mismatch.config import (
    DEFAULT_SEED,
    KEEN_CRISIS_THRESHOLD,
    KEEN_ODE_DEFAULTS,
    KEEN_ODE_INITIAL,
    RATE_HIKE_SWEEP,
)
from experiments.money_minsky_policy_mismatch.keen_ode import detect_crisis, solve_keen


def run_fragility_regime_experiment(
    seed: int = DEFAULT_SEED,
    delta_r_list: Optional[List[float]] = None,
    initial_d_list: Optional[List[float]] = None,
    t_span: tuple[float, float] = (0.0, 200.0),
) -> Dict[str, object]:
    """Compare rate-hike vulnerability under fragile and resilient calibrations."""
    del seed  # deterministic model; kept for a consistent experiment interface
    if delta_r_list is None:
        delta_r_list = RATE_HIKE_SWEEP["delta_r"]
    if initial_d_list is None:
        initial_d_list = RATE_HIKE_SWEEP["initial_d"]

    fragile_params = dict(KEEN_ODE_DEFAULTS)
    resilient_params = dict(KEEN_ODE_DEFAULTS, k2=0.20, r=0.03)

    fragile = _build_crisis_grid(
        params=fragile_params,
        delta_r_list=delta_r_list,
        initial_d_list=initial_d_list,
        t_span=t_span,
    )
    resilient = _build_crisis_grid(
        params=resilient_params,
        delta_r_list=delta_r_list,
        initial_d_list=initial_d_list,
        t_span=t_span,
    )

    return {
        "delta_r": delta_r_list,
        "initial_d": initial_d_list,
        "threshold": KEEN_CRISIS_THRESHOLD,
        "fragile": fragile,
        "resilient": resilient,
    }


def _build_crisis_grid(
    params: dict,
    delta_r_list: List[float],
    initial_d_list: List[float],
    t_span: tuple[float, float],
) -> Dict[str, object]:
    """Evaluate time-to-crisis across a rate/debt grid."""
    crisis_grid = np.full((len(delta_r_list), len(initial_d_list)), np.nan)
    peak_debt_grid = np.full((len(delta_r_list), len(initial_d_list)), np.nan)

    for i, delta_r in enumerate(delta_r_list):
        for j, initial_d in enumerate(initial_d_list):
            shocked = dict(params)
            shocked["r"] = shocked["r"] + delta_r
            y0 = [KEEN_ODE_INITIAL[0], KEEN_ODE_INITIAL[1], initial_d]
            result = solve_keen(shocked, y0, t_span)
            crisis_idx = detect_crisis(result, KEEN_CRISIS_THRESHOLD)
            if crisis_idx is not None:
                crisis_grid[i, j] = result.t[crisis_idx]
            peak_debt_grid[i, j] = float(np.max(result.d))

    return {
        "grid": crisis_grid.tolist(),
        "peak_debt": peak_debt_grid.tolist(),
        "safe_share": float(np.isnan(crisis_grid).mean()),
    }
