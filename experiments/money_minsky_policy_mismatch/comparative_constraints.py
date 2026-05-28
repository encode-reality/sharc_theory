"""Comparative constraint simulation: household vs currency-user vs sovereign-issuer.

Three entity types face the same private-demand shock.  The simulation shows
how the *binding constraint* on spending differs by monetary position:

  HOUSEHOLD        — hard budget constraint, endogenous borrowing rate,
                     no macro feedback from own spending
  CURRENCY_USER    — market-access constraint, endogenous sovereign spread,
                     spending feeds back to revenue via fiscal multiplier
  SOVEREIGN_ISSUER — no financing constraint, policy-set rate,
                     spending feeds back to revenue via fiscal multiplier

Differences in outcomes emerge from the structural rules, not from any
imposed narrative.  If the contrast is weaker than expected under certain
parameters, that is itself informative — the model documents what it finds.

Accounting:
  For government entities (CURRENCY_USER, SOVEREIGN_ISSUER):
    deficit  = spending + interest_expense − revenue
    debt(t)  = debt(t−1) + deficit(t)
    revenue  = tax_rate × output
    output   = (autonomous_demand + spending) / (1 − mpc × (1 − tax_rate))

  For HOUSEHOLD:
    net_income = income − interest − principal_repayment
    spending   = min(target, net_income + new_borrowing)
    debt(t)    = debt(t−1) − repayment + new_borrowing
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


# ---------------------------------------------------------------------------
# Entity type
# ---------------------------------------------------------------------------

class EntityType(Enum):
    HOUSEHOLD = "HOUSEHOLD"
    CURRENCY_USER = "CURRENCY_USER"
    SOVEREIGN_ISSUER = "SOVEREIGN_ISSUER"


# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ConstraintParams:
    """Parameters for the comparative constraint model.

    Simulation:
        periods:          Number of periods.
        shock_period:     Period at which autonomous demand drops.
        demand_shock:     Fractional drop in autonomous demand (negative).
        recovery_rate:    Fractional recovery of autonomous demand per period.
        base_autonomous:  Pre-shock autonomous demand.
        spending_target:  Desired spending level (common starting point).
        initial_debt:     Starting debt for all entities.

    Household:
        hh_income_share:       Fraction of autonomous demand → household income.
        hh_r_base:             Base borrowing rate.
        hh_leverage_phi:       Spread sensitivity to debt/income.
        hh_leverage_threshold: Debt/income where spread activates.
        hh_max_debt_ratio:     Hard borrowing ceiling (debt/income).
        hh_repayment_rate:     Fraction of principal repaid per period.

    Currency user:
        cu_r_base:              Base sovereign borrowing rate.
        cu_spread_phi:          Spread sensitivity to debt/GDP.
        cu_spread_threshold:    Debt/GDP where spread activates.
        cu_market_access_spread: Spread that triggers forced consolidation.
        cu_max_cut:             Maximum forced spending cut (fraction of target).
        cu_max_rate:            Interest rate ceiling (market lockout above this).
        cu_tax_rate:            Tax rate on output.
        cu_mpc:                 Marginal propensity to consume (multiplier).

    Sovereign issuer:
        si_r_policy:  Policy-set interest rate (fixed).
        si_tax_rate:  Tax rate on output.
        si_mpc:       Marginal propensity to consume (multiplier).
    """
    # Simulation
    periods: int = 120
    shock_period: int = 30
    demand_shock: float = -0.20
    recovery_rate: float = 0.02
    base_autonomous: float = 50.0
    spending_target: float = 48.0
    initial_debt: float = 0.0

    # Household
    hh_income_share: float = 1.0
    hh_r_base: float = 0.03
    hh_leverage_phi: float = 0.05
    hh_leverage_threshold: float = 1.5
    hh_max_debt_ratio: float = 4.0
    hh_repayment_rate: float = 0.04

    # Currency user
    cu_r_base: float = 0.03
    cu_spread_phi: float = 0.10
    cu_spread_threshold: float = 0.60
    cu_market_access_spread: float = 0.10
    cu_max_cut: float = 0.40
    cu_max_rate: float = 0.25
    cu_tax_rate: float = 0.25
    cu_mpc: float = 0.65

    # Sovereign issuer
    si_r_policy: float = 0.02
    si_tax_rate: float = 0.25
    si_mpc: float = 0.65


# ---------------------------------------------------------------------------
# Per-period state
# ---------------------------------------------------------------------------

@dataclass
class EntityState:
    """State of a single entity at one point in time."""
    revenue: float = 0.0
    spending: float = 0.0
    debt: float = 0.0
    interest_rate: float = 0.0
    interest_expense: float = 0.0
    output: float = 0.0
    debt_ratio: float = 0.0
    constraint_binding: bool = False
    spending_gap: float = 0.0


# ---------------------------------------------------------------------------
# Time-series container
# ---------------------------------------------------------------------------

@dataclass
class EntityHistory:
    """Time series for one entity."""
    entity_type: str
    revenue: List[float] = field(default_factory=list)
    spending: List[float] = field(default_factory=list)
    debt: List[float] = field(default_factory=list)
    interest_rate: List[float] = field(default_factory=list)
    interest_expense: List[float] = field(default_factory=list)
    output: List[float] = field(default_factory=list)
    debt_ratio: List[float] = field(default_factory=list)
    constraint_binding: List[bool] = field(default_factory=list)
    spending_gap: List[float] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "entity_type": self.entity_type,
            "revenue": self.revenue[:],
            "spending": self.spending[:],
            "debt": self.debt[:],
            "interest_rate": self.interest_rate[:],
            "interest_expense": self.interest_expense[:],
            "output": self.output[:],
            "debt_ratio": self.debt_ratio[:],
            "constraint_binding": self.constraint_binding[:],
            "spending_gap": self.spending_gap[:],
        }


# ---------------------------------------------------------------------------
# Autonomous demand path (common shock)
# ---------------------------------------------------------------------------

def _autonomous_demand(t: int, params: ConstraintParams) -> float:
    """Autonomous private demand at period *t*.

    Flat before the shock, drops by ``demand_shock`` at ``shock_period``,
    then recovers linearly at ``recovery_rate`` per period (capped at
    full recovery).
    """
    if t < params.shock_period:
        return params.base_autonomous
    periods_since = t - params.shock_period
    shock = params.demand_shock  # negative
    recovery = min(params.recovery_rate * periods_since, -shock)
    return params.base_autonomous * (1.0 + shock + recovery)


# ---------------------------------------------------------------------------
# Entity step functions
# ---------------------------------------------------------------------------

def _step_household(
    prev_debt: float,
    income: float,
    params: ConstraintParams,
) -> EntityState:
    """One-period update for a budget-constrained household.

    - Income is exogenous (no macro feedback from own spending).
    - Borrowing rate rises with leverage (endogenous spread).
    - Hard ceiling on debt/income.
    - When borrowing room exhausted, spending is forced below target.
    """
    safe_income = max(income, 1.0)

    # Interest rate: base + leverage spread
    leverage = prev_debt / safe_income
    spread = params.hh_leverage_phi * max(leverage - params.hh_leverage_threshold, 0.0)
    r = params.hh_r_base + spread
    interest = r * prev_debt

    # Debt service
    repayment = params.hh_repayment_rate * prev_debt
    after_service = income - interest - repayment

    # Borrowing room
    max_debt = params.hh_max_debt_ratio * safe_income
    borrow_room = max(max_debt - prev_debt + repayment, 0.0)

    # Spending decision
    target = params.spending_target
    if after_service >= target:
        spending = target
        new_borrow = 0.0
        surplus = after_service - target
        new_debt = prev_debt - repayment - surplus
    else:
        gap = target - after_service
        actual_borrow = min(gap, borrow_room)
        spending = max(after_service + actual_borrow, 0.0)
        new_borrow = actual_borrow
        new_debt = prev_debt - repayment + new_borrow

    new_debt = max(new_debt, 0.0)
    constrained = spending < target - 0.01

    return EntityState(
        revenue=income,
        spending=spending,
        debt=new_debt,
        interest_rate=r,
        interest_expense=interest,
        output=spending,
        debt_ratio=new_debt / safe_income,
        constraint_binding=constrained,
        spending_gap=max(target - spending, 0.0),
    )


def _step_currency_user(
    prev_debt: float,
    prev_output: float,
    autonomous: float,
    params: ConstraintParams,
) -> EntityState:
    """One-period update for a currency-user / quasi-sovereign.

    - Revenue = tax_rate × output (endogenous via multiplier).
    - Borrowing rate rises with debt/GDP (endogenous spread).
    - When spread exceeds market-access threshold → forced consolidation.
    """
    target = params.spending_target
    safe_output = max(prev_output, 1.0)

    # Sovereign spread (capped: beyond cu_max_rate, markets lock out entirely)
    debt_gdp = prev_debt / safe_output
    spread = params.cu_spread_phi * max(debt_gdp - params.cu_spread_threshold, 0.0)
    r = min(params.cu_r_base + spread, params.cu_max_rate)
    interest = r * prev_debt

    # Market-access constraint
    constrained = spread > params.cu_market_access_spread
    if constrained:
        excess = spread - params.cu_market_access_spread
        cut_frac = min(
            params.cu_max_cut,
            excess / max(params.cu_market_access_spread, 0.01) * params.cu_max_cut,
        )
        spending = target * (1.0 - cut_frac)
    else:
        spending = target

    # Output via fiscal multiplier
    denom = 1.0 - params.cu_mpc * (1.0 - params.cu_tax_rate)
    output = (autonomous + spending) / denom

    # Revenue and deficit
    revenue = params.cu_tax_rate * output
    deficit = spending + interest - revenue
    new_debt = prev_debt + deficit

    return EntityState(
        revenue=revenue,
        spending=spending,
        debt=max(new_debt, 0.0),
        interest_rate=r,
        interest_expense=interest,
        output=output,
        debt_ratio=max(new_debt, 0.0) / max(output, 1.0),
        constraint_binding=constrained,
        spending_gap=max(target - spending, 0.0),
    )


def _step_sovereign_issuer(
    prev_debt: float,
    prev_output: float,
    autonomous: float,
    params: ConstraintParams,
) -> EntityState:
    """One-period update for a sovereign currency issuer.

    - Revenue = tax_rate × output (endogenous via multiplier).
    - Interest rate is policy-set (fixed, low).
    - No financing constraint: spending always equals target.
    - Debt accumulates but never forces a spending cut.
    """
    target = params.spending_target
    spending = target  # never constrained

    r = params.si_r_policy
    interest = r * prev_debt

    # Output via fiscal multiplier (same structure as currency user)
    denom = 1.0 - params.si_mpc * (1.0 - params.si_tax_rate)
    output = (autonomous + spending) / denom

    # Revenue and deficit
    revenue = params.si_tax_rate * output
    deficit = spending + interest - revenue
    new_debt = prev_debt + deficit

    return EntityState(
        revenue=revenue,
        spending=spending,
        debt=new_debt,
        interest_rate=r,
        interest_expense=interest,
        output=output,
        debt_ratio=new_debt / max(output, 1.0),
        constraint_binding=False,
        spending_gap=0.0,
    )


# ---------------------------------------------------------------------------
# Recording helper
# ---------------------------------------------------------------------------

def _record(history: EntityHistory, state: EntityState) -> None:
    history.revenue.append(state.revenue)
    history.spending.append(state.spending)
    history.debt.append(state.debt)
    history.interest_rate.append(state.interest_rate)
    history.interest_expense.append(state.interest_expense)
    history.output.append(state.output)
    history.debt_ratio.append(state.debt_ratio)
    history.constraint_binding.append(state.constraint_binding)
    history.spending_gap.append(state.spending_gap)


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def run_comparative(
    params: Optional[ConstraintParams] = None,
) -> Dict[str, EntityHistory]:
    """Run all three entity types under the same demand shock.

    Returns:
        Dict with keys ``"household"``, ``"currency_user"``,
        ``"sovereign_issuer"``, each an :class:`EntityHistory`.
    """
    if params is None:
        params = ConstraintParams()

    histories: Dict[str, EntityHistory] = {
        "household": EntityHistory(entity_type="HOUSEHOLD"),
        "currency_user": EntityHistory(entity_type="CURRENCY_USER"),
        "sovereign_issuer": EntityHistory(entity_type="SOVEREIGN_ISSUER"),
    }

    # --- initial conditions ---
    hh_debt = params.initial_debt
    cu_debt = params.initial_debt
    si_debt = params.initial_debt

    # Initial output for government entities (pre-shock equilibrium)
    cu_denom = 1.0 - params.cu_mpc * (1.0 - params.cu_tax_rate)
    si_denom = 1.0 - params.si_mpc * (1.0 - params.si_tax_rate)
    cu_output = (params.base_autonomous + params.spending_target) / cu_denom
    si_output = (params.base_autonomous + params.spending_target) / si_denom

    for t in range(params.periods):
        autonomous = _autonomous_demand(t, params)

        # Household income: fraction of autonomous demand (exogenous)
        hh_income = params.hh_income_share * autonomous

        # Step each entity
        hh = _step_household(hh_debt, hh_income, params)
        cu = _step_currency_user(cu_debt, cu_output, autonomous, params)
        si = _step_sovereign_issuer(si_debt, si_output, autonomous, params)

        # Carry forward state
        hh_debt = hh.debt
        cu_debt = cu.debt
        cu_output = cu.output
        si_debt = si.debt
        si_output = si.output

        _record(histories["household"], hh)
        _record(histories["currency_user"], cu)
        _record(histories["sovereign_issuer"], si)

    return histories
