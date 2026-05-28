"""Agent-Based Model with Minsky financial fragility classifier.

A minimal ABM with three agent types (firms, households, banks) that
endogenously generates Minsky cycles: hedge -> speculative -> Ponzi
financing regimes emerge from interaction of credit creation, investment
decisions, and profit dynamics.

Key mechanisms:
  - Endogenous money: every loan creates an equal deposit (ΔL = ΔD)
  - Minsky classifier: firms classified as hedge/speculative/Ponzi based
    on cash-flow coverage of debt obligations
  - Job Guarantee (optional): government hires unemployed at w_jg,
    creating a buffer stock of employment

No external framework (Mesa etc.) — pure Python + numpy for consistency
with the project's established patterns.

References:
  - Minsky (1992), "The Financial Instability Hypothesis"
  - Keen (1995), "Finance and Economic Breakdown"
  - Mitchell, Wray & Watts (2019), "Macroeconomics"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np

from experiments.money_minsky_policy_mismatch.config import ABM_DEFAULTS, DEFAULT_SEED


# ---------------------------------------------------------------------------
# Agent dataclasses
# ---------------------------------------------------------------------------

@dataclass
class Firm:
    """A firm that produces, invests, borrows, and services debt."""
    firm_id: int
    deposits: float = 0.0
    debt: float = 0.0
    output: float = 0.0
    employment: int = 0
    cash_flow: float = 0.0
    interest_due: float = 0.0
    principal_due: float = 0.0
    minsky_state: str = "hedge"
    productivity: float = 2.0
    markup: float = 0.10
    alive: bool = True


@dataclass
class Household:
    """A household that works, consumes, and saves."""
    hh_id: int
    deposits: float = 0.0
    wage: float = 0.0
    employed_by: int = -1  # firm_id, -2 = JG, -1 = unemployed
    consumption: float = 0.0


@dataclass
class Bank:
    """A bank that creates loans (endogenous money) and collects interest."""
    bank_id: int
    loans: float = 0.0
    deposits: float = 0.0
    equity: float = 0.0
    capital_ratio: float = 0.10


# ---------------------------------------------------------------------------
# Minsky classifier
# ---------------------------------------------------------------------------

def classify_minsky(firm: Firm) -> str:
    """Classify firm's financial position per Minsky's taxonomy.

    - hedge: cash flow covers both interest and principal
    - speculative: cash flow covers interest but not principal
    - ponzi: cash flow insufficient even for interest
    """
    if firm.cash_flow >= firm.interest_due + firm.principal_due:
        return "hedge"
    if firm.cash_flow >= firm.interest_due:
        return "speculative"
    return "ponzi"


# ---------------------------------------------------------------------------
# ABM Result container
# ---------------------------------------------------------------------------

@dataclass
class ABMResult:
    """Time-series output from the ABM simulation."""
    periods: int = 0
    Y: List[float] = field(default_factory=list)
    unemployment: List[float] = field(default_factory=list)
    jg_share: List[float] = field(default_factory=list)
    debt_ratio: List[float] = field(default_factory=list)
    ponzi_share: List[float] = field(default_factory=list)
    speculative_share: List[float] = field(default_factory=list)
    hedge_share: List[float] = field(default_factory=list)
    deficit_ratio: List[float] = field(default_factory=list)
    total_deposits: List[float] = field(default_factory=list)
    total_loans: List[float] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "periods": self.periods,
            "Y": self.Y[:], "unemployment": self.unemployment[:],
            "jg_share": self.jg_share[:],
            "debt_ratio": self.debt_ratio[:],
            "ponzi_share": self.ponzi_share[:],
            "speculative_share": self.speculative_share[:],
            "hedge_share": self.hedge_share[:],
            "deficit_ratio": self.deficit_ratio[:],
            "total_deposits": self.total_deposits[:],
            "total_loans": self.total_loans[:],
        }


# ---------------------------------------------------------------------------
# ABM Model
# ---------------------------------------------------------------------------

class MacroABM:
    """Minimal agent-based macro model with Minsky fragility dynamics.

    Args:
        n_firms:    Number of firms.
        n_households: Number of households.
        n_banks:    Number of banks.
        params:     Parameter dictionary (see ABM_DEFAULTS).
        seed:       Random seed for reproducibility.
    """

    def __init__(self, params: Optional[dict] = None, seed: int = DEFAULT_SEED):
        if params is None:
            params = dict(ABM_DEFAULTS)
        self.p = params
        self.rng = np.random.default_rng(seed)
        self.t = 0

        n_firms = params["n_firms"]
        n_households = params["n_households"]
        n_banks = params["n_banks"]

        # Initialize agents with heterogeneous parameters for gradual
        # Minsky transitions (not all firms flip state simultaneously).
        base_markup = params["firm_markup"]
        base_prod = params["base_productivity"]
        self.firms = [
            Firm(
                firm_id=i,
                deposits=self.rng.uniform(30.0, 70.0),
                debt=self.rng.uniform(5, 35),
                productivity=base_prod * self.rng.uniform(0.85, 1.15),
                markup=base_markup + self.rng.uniform(-0.04, 0.04),
            )
            for i in range(n_firms)
        ]
        # Per-firm investment propensity (some are aggressive borrowers)
        self._firm_invest_share = self.rng.uniform(0.08, 0.25, size=n_firms)

        self.households = [
            Household(hh_id=i, deposits=5.0)
            for i in range(n_households)
        ]

        self.banks = [
            Bank(bank_id=i, equity=50.0)
            for i in range(n_banks)
        ]

        # Assign initial employment (distribute HH across firms)
        for i, hh in enumerate(self.households):
            firm_idx = i % n_firms
            hh.employed_by = firm_idx
            self.firms[firm_idx].employment += 1

        # Government state
        self.gov_spending = 0.0
        self.gov_revenue = 0.0

        # Animal spirits: accumulated confidence drives investment boom/bust.
        # During good times confidence grows → more borrowing → debt rises.
        # This is the core Minsky mechanism: stability breeds instability.
        self._confidence = 0.0

        # Track endogenous money creation
        self._loan_deposit_log: List[tuple] = []

    def _base_wage(self) -> float:
        """Base wage per worker.

        Wage is 70% of revenue per unit of output, leaving a 30% gross margin.
        A thinner margin means debt obligations can realistically exceed cash
        flow, which is necessary for Minsky dynamics to emerge.
        """
        return self.p["base_productivity"] * (1.0 + self.p["firm_markup"]) * 0.7

    def _effective_rate(self, firm: Firm) -> float:
        """Interest rate for a firm, with spread based on leverage."""
        leverage = firm.debt / max(firm.deposits + 1.0, 1.0)
        spread = self.p["bank_spread_phi"] * max(leverage - 1.0, 0.0)
        return self.p["policy_rate"] + spread

    def _create_loan(self, firm: Firm, bank: Bank, amount: float):
        """Endogenous money creation: loan creates equal deposit."""
        firm.debt += amount
        firm.deposits += amount
        bank.loans += amount
        bank.deposits += amount
        self._loan_deposit_log.append((amount, amount))

    def _step_production(self):
        """Firms produce based on employment."""
        for firm in self.firms:
            if not firm.alive:
                continue
            firm.output = firm.employment * firm.productivity

    def _step_income(self):
        """Pay wages, compute cash flow with demand feedback.

        Revenue is cost-plus modulated by a demand factor reflecting
        unemployment, firm survival, and (optionally) lagged household
        consumption.  The consumption channel allows fiscal policy to
        affect firm revenue: higher transfers → more consumption →
        higher firm revenue → less fragility.
        """
        base_w = self._base_wage()
        unemp = self.compute_unemployment()
        alive_share = sum(1 for f in self.firms if f.alive) / max(len(self.firms), 1)
        demand_factor = max(alive_share * (1.0 - 0.15 * unemp), 0.3)

        # Modulate demand by lagged aggregate consumption
        sensitivity = self.p.get("demand_sensitivity", 0.0)
        lagged = getattr(self, "_agg_consumption", None)
        if sensitivity > 0 and lagged is not None and lagged > 0:
            n_active = max(sum(
                1 for hh in self.households
                if hh.employed_by >= 0 or hh.employed_by == -2
            ), 1)
            expected = n_active * base_w * self.p["consumption_propensity"]
            if expected > 0:
                ratio = lagged / expected
                demand_factor *= max(1.0 + sensitivity * (ratio - 1.0), 0.5)

        total_cf = 0.0
        for firm in self.firms:
            if not firm.alive:
                continue
            revenue = firm.output * (1.0 + firm.markup) * demand_factor
            wage_bill = firm.employment * base_w
            firm.cash_flow = revenue - wage_bill

            # Balance sheet: revenue in, wages out
            firm.deposits += revenue
            firm.deposits -= wage_bill
            if firm.cash_flow > 0:
                total_cf += firm.cash_flow

            # Pay wages to employed households
            for hh in self.households:
                if hh.employed_by == firm.firm_id:
                    hh.wage = base_w

        # Update animal spirits: profitability builds confidence over time
        n_alive = max(sum(1 for f in self.firms if f.alive), 1)
        avg_cf = total_cf / n_alive
        self._confidence = 0.9 * self._confidence + 0.1 * max(avg_cf, 0.0)

        # JG wages
        w_jg = self.p.get("w_jg", 0.0)
        if w_jg > 0:
            for hh in self.households:
                if hh.employed_by == -2:  # JG employed
                    hh.wage = w_jg

    def _step_debt_service(self):
        """Firms service their debt: interest + principal.

        Interest payments flow to banks as income, building bank equity
        over time.  This allows banks to support growing loan books during
        expansions (and constrains them after losses from defaults).
        """
        for firm in self.firms:
            if not firm.alive:
                continue
            r = self._effective_rate(firm)
            firm.interest_due = r * firm.debt
            loan_dur = max(self.p["loan_duration"], 1)
            firm.principal_due = firm.debt / loan_dur

            # Pay what they can — cap deposit draw to 15% to preserve working capital
            total_due = firm.interest_due + firm.principal_due
            max_from_deposits = firm.deposits * 0.15
            payment = min(total_due, max(firm.cash_flow, 0.0) + max_from_deposits)
            interest_paid = min(firm.interest_due, payment)
            firm.deposits -= min(payment, firm.deposits)
            principal_paid = min(firm.principal_due, max(payment - firm.interest_due, 0.0))
            firm.debt = max(firm.debt - principal_paid, 0.0)

            # Bank earns interest income → builds equity (retained earnings)
            bank = self.banks[firm.firm_id % len(self.banks)]
            bank.equity += interest_paid * 0.5  # 50% retention ratio

    def _step_classify(self):
        """Classify each firm's Minsky state."""
        for firm in self.firms:
            if not firm.alive:
                continue
            firm.minsky_state = classify_minsky(firm)

    def _step_investment(self):
        """Firms invest: animal spirits amplify borrowing during good times.

        The confidence multiplier is the Minsky mechanism: prolonged
        profitability builds confidence, boosting investment and debt
        accumulation beyond what cash flow alone would justify.
        """
        inv_share = self.p.get("invest_share", 0.15)
        conf_sens = self.p.get("confidence_sensitivity", 0.2)
        confidence_mult = 1.0 + conf_sens * self._confidence
        for firm in self.firms:
            if not firm.alive:
                continue

            # Investment desire based on profitability, amplified by confidence
            profit_rate = firm.cash_flow / max(firm.output, 1.0)
            if profit_rate > 0.05 and firm.minsky_state != "ponzi":
                # Per-firm investment propensity + animal spirits
                fi = self._firm_invest_share[firm.firm_id]
                invest_amount = firm.cash_flow * fi * confidence_mult
                bank = self.banks[firm.firm_id % len(self.banks)]

                # Bank lending: check capital ratio
                if bank.equity / max(bank.loans + 1.0, 1.0) > self.p["bank_capital_ratio_min"]:
                    self._create_loan(firm, bank, invest_amount)

    def _step_consumption(self):
        """Households consume based on income, transfers, and wealth."""
        c_prop = self.p["consumption_propensity"]
        tau = self.p["tau"]
        transfer = self.p.get("fiscal_transfer", 0.0)
        self.gov_revenue = 0.0

        for hh in self.households:
            # Tax
            tax = tau * hh.wage
            self.gov_revenue += tax
            disposable = hh.wage - tax + transfer

            # Track transfer spending
            self.gov_spending += transfer

            # Consume
            hh.consumption = c_prop * disposable + 0.01 * hh.deposits
            hh.deposits += disposable - hh.consumption

        # Track aggregate consumption for demand feedback
        self._agg_consumption = sum(hh.consumption for hh in self.households)

    def _step_jg(self):
        """Job Guarantee: hire unemployed at w_jg."""
        w_jg = self.p.get("w_jg", 0.0)
        if w_jg <= 0:
            return

        self.gov_spending = 0.0
        for hh in self.households:
            if hh.employed_by == -1:  # unemployed
                hh.employed_by = -2   # JG
                self.gov_spending += w_jg

    def _step_labor_market(self):
        """Labor market: firms hire/fire based on financial health.

        Firms in distress cut employment to reduce costs — Ponzi firms shed
        aggressively, speculative firms trim modestly.  This creates
        unemployment that feeds back into lower demand.
        """
        for firm in self.firms:
            if not firm.alive:
                continue

            # Base desired employment from output capacity
            base_desired = max(int(firm.output / max(firm.productivity, 0.1)), 1)

            # Financial distress reduces desired workforce
            if firm.minsky_state == "ponzi":
                desired = max(int(base_desired * 0.7), 1)
            elif firm.minsky_state == "speculative":
                desired = max(int(base_desired * 0.9), 1)
            else:
                desired = base_desired

            current = firm.employment
            if current < desired:
                # Hire from unemployed or JG pool
                for hh in self.households:
                    if hh.employed_by in (-1, -2) and current < desired:
                        hh.employed_by = firm.firm_id
                        current += 1
            elif current > desired:
                # Lay off excess workers
                fired = 0
                target_fire = current - desired
                for hh in self.households:
                    if hh.employed_by == firm.firm_id and fired < target_fire:
                        hh.employed_by = -1
                        hh.wage = 0.0
                        fired += 1

            firm.employment = sum(
                1 for hh in self.households if hh.employed_by == firm.firm_id
            )

    def _step_defaults(self):
        """Handle firm defaults: Ponzi firms with depleted deposits fail."""
        for firm in self.firms:
            if not firm.alive:
                continue
            if firm.minsky_state == "ponzi" and firm.deposits < 0.1 and firm.debt > 0:
                firm.alive = False
                # Fire all workers
                for hh in self.households:
                    if hh.employed_by == firm.firm_id:
                        hh.employed_by = -1
                        hh.wage = 0.0
                # Write down bank loan
                bank = self.banks[firm.firm_id % len(self.banks)]
                bank.equity -= min(firm.debt, bank.equity * 0.5)
                bank.loans = max(bank.loans - firm.debt, 0.0)

    def _step_austerity(self):
        """Austerity rule: cut JG spending and fire JG workers if deficit too high.

        When the deficit-to-output ratio exceeds the target, austerity fires
        JG workers proportionally.  This creates the policy feedback loop the
        blog describes: austerity → unemployment ↑ → demand ↓ → fragility ↑.
        """
        phi = self.p.get("austerity_phi", 0.0)
        if phi <= 0:
            return
        Y = self.compute_output()
        if Y <= 0:
            return
        deficit_ratio = (self.gov_spending - self.gov_revenue) / Y
        target = self.p.get("target_deficit", 0.03)
        if deficit_ratio > target:
            excess = deficit_ratio - target
            cut_fraction = min(phi * excess, 1.0)
            # Fire JG workers proportionally — this is the real austerity bite
            jg_workers = [hh for hh in self.households if hh.employed_by == -2]
            n_to_fire = int(len(jg_workers) * cut_fraction)
            for hh in jg_workers[:n_to_fire]:
                hh.employed_by = -1
                hh.wage = 0.0
            self.gov_spending *= (1.0 - cut_fraction)

    def step(self):
        """Advance the model by one period."""
        self.t += 1
        self._loan_deposit_log.clear()

        self._step_production()
        self._step_income()
        self._step_debt_service()
        self._step_classify()
        self._step_investment()
        self._step_labor_market()
        self._step_jg()
        self._step_consumption()
        self._step_austerity()
        self._step_defaults()

    # --- Aggregate computations ---

    def compute_output(self) -> float:
        return sum(f.output for f in self.firms if f.alive)

    def compute_unemployment(self) -> float:
        n = len(self.households)
        unemployed = sum(1 for hh in self.households if hh.employed_by == -1)
        return unemployed / n if n > 0 else 0.0

    def compute_jg_share(self) -> float:
        n = len(self.households)
        jg = sum(1 for hh in self.households if hh.employed_by == -2)
        return jg / n if n > 0 else 0.0

    def compute_private_debt_ratio(self) -> float:
        Y = self.compute_output()
        total_debt = sum(f.debt for f in self.firms)
        return total_debt / max(Y, 1.0)

    def compute_ponzi_share(self) -> float:
        alive = [f for f in self.firms if f.alive]
        if not alive:
            return 0.0
        return sum(1 for f in alive if f.minsky_state == "ponzi") / len(alive)

    def compute_speculative_share(self) -> float:
        alive = [f for f in self.firms if f.alive]
        if not alive:
            return 0.0
        return sum(1 for f in alive if f.minsky_state == "speculative") / len(alive)

    def compute_hedge_share(self) -> float:
        alive = [f for f in self.firms if f.alive]
        if not alive:
            return 0.0
        return sum(1 for f in alive if f.minsky_state == "hedge") / len(alive)

    def compute_deficit_ratio(self) -> float:
        Y = self.compute_output()
        if Y <= 0:
            return 0.0
        return (self.gov_spending - self.gov_revenue) / Y

    def compute_total_deposits(self) -> float:
        return sum(hh.deposits for hh in self.households) + sum(f.deposits for f in self.firms)

    def compute_total_loans(self) -> float:
        return sum(f.debt for f in self.firms)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_abm(
    params: Optional[dict] = None,
    periods: Optional[int] = None,
    seed: int = DEFAULT_SEED,
) -> ABMResult:
    """Run the ABM for a given number of periods.

    Args:
        params:  Parameter dictionary (defaults to ABM_DEFAULTS).
        periods: Number of periods to simulate (defaults to params["periods"]).
        seed:    Random seed.

    Returns:
        ABMResult with time-series data.
    """
    if params is None:
        params = dict(ABM_DEFAULTS)
    if periods is None:
        periods = params.get("periods", 200)

    model = MacroABM(params=params, seed=seed)
    result = ABMResult(periods=periods)

    for _ in range(periods):
        model.step()
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
