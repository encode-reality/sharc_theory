"""Deterministic sectoral-policy model for austerity counterfactuals.

This module is intentionally simple and explicit. It keeps the accounting
identities visible:

    private_balance + government_balance + foreign_balance = 0

The model is demand-led, includes an external sector, and compares policy
responses to the same private-demand shortfall:

- supportive fiscal response
- immediate austerity
- delayed fiscal repair

The goal is not to reconstruct a full national-accounting system. The goal is
to make the sectoral logic inspectable in code and to show why deficit targets
behave like outcomes of the whole system rather than independent control knobs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class SectoralPolicyParams:
    """Structural parameters for the sectoral model."""

    tau: float = 0.24
    c_y: float = 0.78
    c_w: float = 0.04
    import_propensity: float = 0.14
    investment_autonomous: float = 5.0
    accelerator: float = 0.09
    exports: float = 9.0
    base_government_spending: float = 24.0
    shock_start: int = 12
    private_demand_shock: float = -3.0
    initial_output: float = 100.0
    initial_private_wealth: float = 80.0
    initial_government_debt: float = 70.0


@dataclass
class SectoralHistory:
    """Time-series output for one policy scenario."""

    scenario: str
    Y: List[float] = field(default_factory=list)
    C: List[float] = field(default_factory=list)
    I: List[float] = field(default_factory=list)
    T: List[float] = field(default_factory=list)
    G: List[float] = field(default_factory=list)
    X: List[float] = field(default_factory=list)
    M: List[float] = field(default_factory=list)
    private_balance: List[float] = field(default_factory=list)
    government_balance: List[float] = field(default_factory=list)
    foreign_balance: List[float] = field(default_factory=list)
    private_wealth: List[float] = field(default_factory=list)
    government_debt: List[float] = field(default_factory=list)
    debt_ratio: List[float] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "scenario": self.scenario,
            "Y": self.Y[:],
            "C": self.C[:],
            "I": self.I[:],
            "T": self.T[:],
            "G": self.G[:],
            "X": self.X[:],
            "M": self.M[:],
            "private_balance": self.private_balance[:],
            "government_balance": self.government_balance[:],
            "foreign_balance": self.foreign_balance[:],
            "private_wealth": self.private_wealth[:],
            "government_debt": self.government_debt[:],
            "debt_ratio": self.debt_ratio[:],
        }

    def verify_sectoral_identity(self, tol: float = 1e-8) -> bool:
        """Check that the three-sector accounting identity holds."""
        for period, values in enumerate(
            zip(self.private_balance, self.government_balance, self.foreign_balance)
        ):
            residual = sum(values)
            if abs(residual) > tol:
                raise AssertionError(
                    f"Sectoral identity failed at period {period}: residual={residual:.8e}"
                )
        return True


def run_sectoral_scenario(
    scenario: str,
    params: SectoralPolicyParams | None = None,
    periods: int = 50,
) -> SectoralHistory:
    """Run one deterministic policy scenario."""
    if params is None:
        params = SectoralPolicyParams()

    if scenario not in {"supportive", "austerity", "delayed_repair"}:
        raise ValueError(f"Unknown scenario: {scenario}")

    history = SectoralHistory(scenario=scenario)
    wealth = params.initial_private_wealth
    debt = params.initial_government_debt
    output_prev = params.initial_output

    denominator = (
        1.0 - params.c_y * (1.0 - params.tau) + params.import_propensity
    )
    if denominator <= 0:
        raise ValueError("Model denominator must remain positive for stability.")

    for period in range(periods):
        government_spending = _scenario_government_spending(period, scenario, params)
        private_shock = params.private_demand_shock if period >= params.shock_start else 0.0
        investment = max(
            params.investment_autonomous + private_shock + params.accelerator * output_prev,
            0.0,
        )

        output = (
            params.c_w * wealth
            + investment
            + government_spending
            + params.exports
        ) / denominator

        taxes = params.tau * output
        disposable_income = output - taxes
        consumption = params.c_y * disposable_income + params.c_w * wealth
        imports = params.import_propensity * output

        private_balance = output - taxes - consumption - investment
        government_balance = taxes - government_spending
        foreign_balance = imports - params.exports

        wealth += private_balance
        debt += government_spending - taxes

        history.Y.append(output)
        history.C.append(consumption)
        history.I.append(investment)
        history.T.append(taxes)
        history.G.append(government_spending)
        history.X.append(params.exports)
        history.M.append(imports)
        history.private_balance.append(private_balance)
        history.government_balance.append(government_balance)
        history.foreign_balance.append(foreign_balance)
        history.private_wealth.append(wealth)
        history.government_debt.append(debt)
        history.debt_ratio.append(debt / max(output, 1e-9))

        output_prev = output

    return history


def run_policy_sectoral_experiment(
    params: SectoralPolicyParams | None = None,
    periods: int = 50,
) -> Dict[str, dict]:
    """Run the three policy scenarios used in the rebuilt article."""
    histories = {
        scenario: run_sectoral_scenario(scenario=scenario, params=params, periods=periods)
        for scenario in ("supportive", "austerity", "delayed_repair")
    }
    for history in histories.values():
        history.verify_sectoral_identity()

    return {
        "supportive": histories["supportive"].to_dict(),
        "austerity": histories["austerity"].to_dict(),
        "delayed_repair": histories["delayed_repair"].to_dict(),
        "shock_start": (params.shock_start if params else SectoralPolicyParams().shock_start),
    }


def _scenario_government_spending(
    period: int,
    scenario: str,
    params: SectoralPolicyParams,
) -> float:
    """Scenario-specific government spending path."""
    base = params.base_government_spending
    if period < params.shock_start:
        return base

    if scenario == "supportive":
        if period < 30:
            return base + 2.0
        return base + 0.5

    if scenario == "austerity":
        return base - 3.0

    if scenario == "delayed_repair":
        if period < 28:
            return base + 1.0
        if period < 38:
            return base - 0.5
        return base - 1.0

    raise ValueError(f"Unknown scenario: {scenario}")
