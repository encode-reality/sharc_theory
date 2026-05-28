"""Keen-Minsky leverage-cycle ODE model.

Implements a Goodwin-Keen system with three state variables:
  omega (wage share), lambda (employment rate), d (private debt ratio).

The core mechanism: investment responds to profitability with a debt-drag
term; wages respond to labor-market tightness via a Phillips curve; debt
accumulates when investment exceeds internal funds. Under stable parameters
the system produces limit cycles; under fragile parameters (high leverage,
high rates, weak debt drag) it produces crisis-like trajectories where the
debt ratio diverges.

References:
  - Keen (1995), "Finance and Economic Breakdown"
  - Keen (2013), "A monetary Minsky model of the Great Moderation and the
    Great Recession"
  - Minsky (1992), "The Financial Instability Hypothesis"
"""

from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy.integrate import solve_ivp


def phillips(lam: float, a0: float = 0.0, a1: float = 6.0, lam0: float = 0.9) -> float:
    """Convex Phillips curve proxy: wage-growth pressure as a function of employment.

    Returns a0 when lam <= lam0 (no tight-labor pressure).
    Above lam0, pressure rises linearly with slope a1.
    """
    return a0 + a1 * max(lam - lam0, 0.0)


def invest(profit_share: float, d: float,
           k0: float = 0.02, k1: float = 0.20, k2: float = 0.12) -> float:
    """Investment-to-output ratio: rises with profits, falls with debt (drag).

    Floored at zero — firms stop investing but don't disinvest in this model.
    """
    return max(k0 + k1 * profit_share - k2 * d, 0.0)


def keen_minsky_ode(t: float, y: list, p: dict) -> list:
    """Right-hand side of the Keen-Minsky ODE system.

    State vector y = [omega, lambda, d]:
      omega  — wage share of output
      lambda — employment rate
      d      — private debt-to-output ratio

    Parameters p (dict keys):
      r      — interest rate on private debt
      delta  — depreciation rate
      alpha  — labor productivity growth rate
      n      — labor force growth rate
      a0, a1, lam0 — Phillips curve parameters
      k0, k1, k2  — investment function parameters
    """
    omega, lam, d = y

    # Clamp state variables to physical bounds for numerical stability.
    # omega (wage share) and lam (employment rate) are shares in [0, 1].
    omega_c = max(min(omega, 1.0 - 1e-10), 1e-10)
    lam_c = max(min(lam, 1.0 - 1e-10), 1e-10)
    d_c = max(d, 0.0)

    # Profit share: output minus wages minus debt service, floored at 0
    profit = max(1.0 - omega_c - p["r"] * d_c, 0.0)

    # Investment-to-output ratio
    I_over_Y = invest(profit, d_c, p["k0"], p["k1"], p["k2"])

    # Output growth proxy: investment minus depreciation
    gY = I_over_Y - p["delta"]

    # Wage share dynamics: logistic-bounded so omega stays in (0, 1).
    # The (1 - omega_c) factor prevents omega from exceeding 1 (wages
    # cannot exceed output) and provides self-dampening near the boundary.
    phi_net = phillips(lam_c, p["a0"], p["a1"], p["lam0"]) - p["alpha"]
    domega = omega_c * (1.0 - omega_c) * phi_net

    # Employment dynamics: logistic-bounded so lam stays in (0, 1).
    # Employment rate cannot exceed 100% of the labor force.
    dlam = lam_c * (1.0 - lam_c) * (gY - p["alpha"] - p["n"])

    # Debt ratio dynamics: rises when investment exceeds internal funds,
    # adjusted for output growth dilution
    dd = (I_over_Y - profit) - d_c * gY

    return [domega, dlam, dd]


@dataclass
class KeenResult:
    """Result container for a Keen ODE solve."""

    t: np.ndarray
    omega: np.ndarray
    lam: np.ndarray
    d: np.ndarray

    def to_dict(self) -> dict:
        return {
            "t": self.t.tolist(),
            "omega": self.omega.tolist(),
            "lam": self.lam.tolist(),
            "d": self.d.tolist(),
        }

    def profit_share(self, r: float = 0.04) -> np.ndarray:
        """Compute profit share at each time step: max(1 - omega - r*d, 0)."""
        return np.maximum(1.0 - self.omega - r * self.d, 0.0)

    def debt_service(self, r: float = 0.04) -> np.ndarray:
        """Debt service ratio: r * d."""
        return r * self.d


def solve_keen(params: dict, y0: list, t_span: tuple,
               max_step: float = 0.1, rtol: float = 1e-8,
               atol: float = 1e-10) -> KeenResult:
    """Solve the Keen-Minsky ODE system.

    Args:
        params: Parameter dictionary (see keen_minsky_ode).
        y0: Initial conditions [omega_0, lambda_0, d_0].
        t_span: (t_start, t_end).
        max_step: Maximum solver step size.
        rtol, atol: Solver tolerances.

    Returns:
        KeenResult with time series of all state variables.
    """
    sol = solve_ivp(
        fun=lambda t, y: keen_minsky_ode(t, y, params),
        t_span=t_span,
        y0=y0,
        method="RK45",
        max_step=max_step,
        rtol=rtol,
        atol=atol,
        dense_output=False,
    )

    if not sol.success:
        raise RuntimeError(f"ODE solver failed: {sol.message}")

    return KeenResult(
        t=sol.t,
        omega=sol.y[0],
        lam=sol.y[1],
        d=sol.y[2],
    )


def detect_crisis(result: KeenResult, threshold: float = 5.0) -> Optional[int]:
    """Find first time index where debt ratio exceeds threshold.

    Returns:
        Index into result arrays, or None if threshold never crossed.
    """
    above = np.where(result.d >= threshold)[0]
    if len(above) == 0:
        return None
    return int(above[0])
