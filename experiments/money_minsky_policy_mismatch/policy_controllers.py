"""Fiscal policy controllers for the ABM policy lab.

Two competing controllers represent alternative policy frameworks:

  AusterityController         — targets deficit/GDP; cuts spending and raises
                                taxes when the deficit exceeds target.
  FunctionalFinanceController — targets unemployment; raises spending and
                                lowers taxes when unemployment exceeds target.

A PassiveController (fixed policy) provides the baseline.

Each controller observes the economy state each period and returns a
:class:`PolicyAdjustment` that sets ``w_jg``, ``tau``, and
``fiscal_transfer`` for the next ABM step.  The ABM itself is unchanged —
controllers adjust its parameters externally.
"""

from __future__ import annotations

import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np

from experiments.money_minsky_policy_mismatch.abm_model import (
    ABMResult,
    MacroABM,
)
from experiments.money_minsky_policy_mismatch.config import ABM_DEFAULTS


# ---------------------------------------------------------------------------
# Adjustment dataclass
# ---------------------------------------------------------------------------

@dataclass
class PolicyAdjustment:
    """Policy parameters for the next ABM step."""
    w_jg: float
    tau: float
    fiscal_transfer: float


# ---------------------------------------------------------------------------
# Controllers
# ---------------------------------------------------------------------------

class PassiveController:
    """Fixed policy — no adjustment regardless of economy state."""

    def __init__(self, base_w_jg: float, base_tau: float, base_transfer: float):
        self.base_w_jg = base_w_jg
        self.base_tau = base_tau
        self.base_transfer = base_transfer

    def adjust(self, state: dict) -> PolicyAdjustment:
        return PolicyAdjustment(
            w_jg=self.base_w_jg,
            tau=self.base_tau,
            fiscal_transfer=self.base_transfer,
        )


class AusterityController:
    """Targets deficit/GDP ratio.  Cuts spending and raises taxes when
    the deficit exceeds ``deficit_target``.

    Mechanism:
      excess = max(deficit_ratio - deficit_target, 0)
      fiscal_transfer = base × (1 - speed × excess)     [clamped ≥ 0]
      w_jg             = base × (1 - speed × excess / 2) [clamped ≥ 0]
      tau              = base + speed × excess / 2        [clamped ≤ 0.50]

    When deficit is at or below target, policy stays at baseline.
    """

    def __init__(
        self,
        base_w_jg: float,
        base_tau: float,
        base_transfer: float,
        deficit_target: float = 0.03,
        adjustment_speed: float = 3.0,
    ):
        self.base_w_jg = base_w_jg
        self.base_tau = base_tau
        self.base_transfer = base_transfer
        self.deficit_target = deficit_target
        self.speed = adjustment_speed

    def adjust(self, state: dict) -> PolicyAdjustment:
        deficit_ratio = state.get("deficit_ratio", 0.0)
        excess = max(deficit_ratio - self.deficit_target, 0.0)

        if excess <= 0:
            return PolicyAdjustment(
                w_jg=self.base_w_jg,
                tau=self.base_tau,
                fiscal_transfer=self.base_transfer,
            )

        cut = self.speed * excess
        return PolicyAdjustment(
            w_jg=max(self.base_w_jg * (1.0 - cut * 0.5), 0.0),
            tau=min(self.base_tau + cut * 0.5 * self.base_tau, 0.50),
            fiscal_transfer=max(self.base_transfer * (1.0 - cut), 0.0),
        )


class FunctionalFinanceController:
    """Targets labor underutilization (unemployment + JG share).  Raises
    spending and lowers taxes when underutilization exceeds target.

    The metric is unemployment + jg_share because a high JG share signals
    that the private sector is weak — JG is a buffer, not a solution.

    Mechanism:
      underutilization = unemployment + jg_share
      excess = max(underutilization - target, 0)
      fiscal_transfer = base × (1 + speed × excess)      [clamped ≤ 1.0]
      w_jg             = base × (1 + speed × excess / 2)  [clamped ≤ 3.0]
      tau              = base × (1 - speed × excess / 2)  [clamped ≥ 0.05]

    When underutilization is at or below target, policy stays at baseline.
    """

    def __init__(
        self,
        base_w_jg: float,
        base_tau: float,
        base_transfer: float,
        unemployment_target: float = 0.05,
        adjustment_speed: float = 3.0,
    ):
        self.base_w_jg = base_w_jg
        self.base_tau = base_tau
        self.base_transfer = base_transfer
        self.unemployment_target = unemployment_target
        self.speed = adjustment_speed

    def adjust(self, state: dict) -> PolicyAdjustment:
        underutilization = (
            state.get("unemployment", 0.0) + state.get("jg_share", 0.0)
        )
        excess = max(underutilization - self.unemployment_target, 0.0)

        if excess <= 0:
            return PolicyAdjustment(
                w_jg=self.base_w_jg,
                tau=self.base_tau,
                fiscal_transfer=self.base_transfer,
            )

        boost = self.speed * excess
        return PolicyAdjustment(
            w_jg=min(self.base_w_jg * (1.0 + boost * 0.5), 3.0),
            tau=max(self.base_tau * (1.0 - boost * 0.5), 0.05),
            fiscal_transfer=min(self.base_transfer * (1.0 + boost), 1.0),
        )


# ---------------------------------------------------------------------------
# Policy lab runner
# ---------------------------------------------------------------------------

def run_policy_lab(
    controller,
    params: Optional[dict] = None,
    seed: int = 42,
    periods: int = 150,
) -> ABMResult:
    """Run the ABM under a given policy controller.

    Each period:
      1. Controller observes economy state.
      2. Controller returns policy adjustments (w_jg, tau, fiscal_transfer).
      3. ABM parameters are updated.
      4. ABM advances one step.
      5. Metrics are recorded.

    Args:
        controller: A policy controller with an ``adjust(state)`` method.
        params:     Base ABM parameter dict.
        seed:       Random seed.
        periods:    Number of periods.

    Returns:
        ABMResult with time-series data.
    """
    if params is None:
        params = dict(ABM_DEFAULTS)

    model = MacroABM(params=dict(params), seed=seed)
    result = ABMResult(periods=periods)

    for _ in range(periods):
        # 1. Observe
        state = {
            "unemployment": model.compute_unemployment(),
            "jg_share": model.compute_jg_share(),
            "output": model.compute_output(),
            "deficit_ratio": model.compute_deficit_ratio(),
            "ponzi_share": model.compute_ponzi_share(),
            "hedge_share": model.compute_hedge_share(),
        }

        # 2. Adjust
        adj = controller.adjust(state)
        model.p["w_jg"] = adj.w_jg
        model.p["tau"] = adj.tau
        model.p["fiscal_transfer"] = adj.fiscal_transfer

        # 3. Step
        model.step()

        # 4. Record
        result.Y.append(model.compute_output())
        result.unemployment.append(model.compute_unemployment())
        result.jg_share.append(model.compute_jg_share())
        result.debt_ratio.append(model.compute_private_debt_ratio())
        result.ponzi_share.append(model.compute_ponzi_share())
        result.speculative_share.append(model.compute_speculative_share())
        result.hedge_share.append(model.compute_hedge_share())
        result.deficit_ratio.append(model.compute_deficit_ratio())
        result.total_deposits.append(model.compute_total_deposits())
        result.total_loans.append(model.compute_total_loans())

    return result
