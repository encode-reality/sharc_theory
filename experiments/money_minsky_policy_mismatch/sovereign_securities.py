"""Toy sovereign-securities and rollover model.

Shows how maturity structure and refinancing pressure change fiscal
dynamics even when the headline debt/GDP ratio is the same.

Key distinction: **debt stock** vs **refinancing flow**.

A government with 60% debt/GDP in 30-year bonds faces very different
pressure from one with 60% debt/GDP in 1-year bills that must be rolled
over annually.  This model makes that distinction explicit.

Two regimes:
  ISSUER — sets its own rate, no rollover spread, no forced consolidation.
  USER   — market-determined rate with spread sensitive to both debt/GDP
           AND rollover-need/GDP.  Forced consolidation when spread
           exceeds market-access threshold.

The model is intentionally minimal.  It does not attempt to model a
yield curve, dealer behavior, or auction mechanics.  Its purpose is to
show that debt composition matters for fiscal dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class RolloverParams:
    """Parameters for the sovereign-securities model.

    Regime:
        regime: 'ISSUER' or 'USER'.

    Fiscal:
        base_G:              Government spending target.
        tax_rate:            Tax rate on output.
        base_private_demand: Autonomous private demand.
        mpc:                 Marginal propensity to consume (for multiplier).

    Debt structure:
        initial_debt:   Starting total debt stock.
        short_share:    Fraction of new issuance that is short-term.
        short_maturity: Periods until short debt matures (default 1).
        long_maturity:  Periods until long debt matures.

    Issuer-specific:
        r_policy: Policy-set interest rate (fixed).

    User-specific:
        r_base:               Base market rate.
        spread_phi:           Spread sensitivity to debt/GDP.
        rollover_phi:         Spread sensitivity to rollover-need/GDP.
        spread_threshold:     Debt/GDP above which spread activates.
        rollover_threshold:   Rollover/GDP above which rollover spread activates.
        market_access_spread: Spread that triggers forced consolidation.
        max_rate:             Interest rate ceiling.
        max_cut:              Maximum forced spending cut (fraction of base_G).

    Simulation:
        periods: Number of periods.
    """
    regime: str = "ISSUER"
    periods: int = 60

    # Fiscal
    base_G: float = 48.0
    tax_rate: float = 0.25
    base_private_demand: float = 50.0
    mpc: float = 0.65

    # Debt structure
    initial_debt: float = 40.0
    short_share: float = 0.50
    short_maturity: int = 1
    long_maturity: int = 10

    # Issuer
    r_policy: float = 0.02

    # User
    r_base: float = 0.03
    spread_phi: float = 0.05
    rollover_phi: float = 0.08
    spread_threshold: float = 0.50
    rollover_threshold: float = 0.10
    market_access_spread: float = 0.12
    max_rate: float = 0.20
    max_cut: float = 0.40


def run_rollover_model(
    params: Optional[RolloverParams] = None,
) -> Dict[str, List[float]]:
    """Run the sovereign-securities rollover model.

    Returns dict with time-series lists for: output, debt_total,
    debt_short, debt_long, rollover_need, effective_rate,
    interest_expense, inflation, spending.
    """
    if params is None:
        params = RolloverParams()

    denom = 1.0 - params.mpc * (1.0 - params.tax_rate)
    is_issuer = params.regime == "ISSUER"

    # Initialize debt stocks
    debt_short = params.initial_debt * params.short_share
    debt_long = params.initial_debt * (1.0 - params.short_share)

    # Maturity queues: track when each tranche matures
    # Short debt matures every short_maturity periods
    # Long debt matures every long_maturity periods
    # Simple approach: spread existing long debt evenly across maturity buckets
    long_buckets = [0.0] * params.long_maturity
    if params.long_maturity > 0 and debt_long > 0:
        per_bucket = debt_long / params.long_maturity
        for i in range(params.long_maturity):
            long_buckets[i] = per_bucket

    prev_output = (params.base_private_demand + params.base_G) / denom

    history: Dict[str, List[float]] = {
        "output": [],
        "debt_total": [],
        "debt_short": [],
        "debt_long": [],
        "rollover_need": [],
        "effective_rate": [],
        "interest_expense": [],
        "inflation": [],
        "spending": [],
    }

    for t in range(params.periods):
        debt_total = debt_short + debt_long

        # --- Maturing debt this period ---
        # All short debt matures every period (maturity=1)
        maturing_short = debt_short
        # Long debt: oldest bucket matures
        maturing_long = long_buckets[0] if long_buckets else 0.0
        maturing = maturing_short + maturing_long

        # --- Rate determination ---
        safe_output = max(prev_output, 1.0)
        debt_ratio = debt_total / safe_output
        rollover_ratio = maturing / safe_output

        if is_issuer:
            effective_rate = params.r_policy
            spending = params.base_G
        else:
            # Spread from debt level + rollover pressure
            debt_spread = params.spread_phi * max(
                debt_ratio - params.spread_threshold, 0.0
            )
            rollover_spread = params.rollover_phi * max(
                rollover_ratio - params.rollover_threshold, 0.0
            )
            total_spread = debt_spread + rollover_spread
            effective_rate = min(
                params.r_base + total_spread, params.max_rate
            )

            # Forced consolidation
            if total_spread > params.market_access_spread:
                excess = total_spread - params.market_access_spread
                cut_frac = min(
                    params.max_cut,
                    excess / max(params.market_access_spread, 0.01) * params.max_cut,
                )
                spending = params.base_G * (1.0 - cut_frac)
            else:
                spending = params.base_G

        # --- Output and revenue ---
        output = (params.base_private_demand + spending) / denom
        revenue = params.tax_rate * output
        interest_expense = effective_rate * debt_total

        # --- Primary deficit and rollover need ---
        primary_deficit = spending - revenue
        net_borrowing_need = primary_deficit + interest_expense

        if net_borrowing_need >= 0:
            # Deficit: issue new debt + refinance all maturing
            rollover_need = net_borrowing_need + maturing
            new_issuance = net_borrowing_need
            refinance_short = maturing_short
            refinance_long = maturing_long
        else:
            # Surplus: use surplus to pay down maturing debt
            surplus = -net_borrowing_need
            refinance = max(maturing - surplus, 0.0)
            rollover_need = refinance
            new_issuance = 0.0
            refinance_short = refinance * params.short_share
            refinance_long = refinance * (1.0 - params.short_share)

        new_short = new_issuance * params.short_share + refinance_short
        new_long_issuance = new_issuance * (1.0 - params.short_share) + refinance_long

        # Update debt stocks
        debt_short = new_short
        # Shift long buckets: remove matured, add new at end
        long_buckets = long_buckets[1:] + [new_long_issuance]
        debt_long = sum(long_buckets)

        # Simple inflation proxy (demand pressure)
        capacity = safe_output * 1.05  # modest capacity headroom
        inflation = max((output / capacity) - 1.0, 0.0) * 0.3

        prev_output = output

        # Record
        history["output"].append(output)
        history["debt_total"].append(debt_short + debt_long)
        history["debt_short"].append(debt_short)
        history["debt_long"].append(debt_long)
        history["rollover_need"].append(rollover_need)
        history["effective_rate"].append(effective_rate)
        history["interest_expense"].append(interest_expense)
        history["inflation"].append(inflation)
        history["spending"].append(spending)

    return history
