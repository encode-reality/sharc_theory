"""Stock-Flow Consistent (SFC) macro model — minimal 3-sector economy.

Implements a demand-determined, stock-flow consistent model with three
consolidated sectors:
  Households + Banks (consume, save, earn wages + bank profits + bond interest)
  Firms (produce, invest, borrow from banks)
  Government (spends, taxes, issues bonds)

Banks are consolidated with households: loan interest received by banks flows
through to households (as bank equity owners / depositors). This means the only
interest flows crossing sector boundaries are:
  - Firm loans: rL * Lf (internal to private sector, redistributes HH<->Firm)
  - Government bonds: i_sov * Bg (government -> households)

The sectoral balance identity holds every period by construction:
  FB_priv + FB_gov = 0    (closed economy, no foreign sector)
where:
  FB_priv = (YD - C) + (Pi - I)    [household saving + firm net cash flow]
  FB_gov  = T - G_eff - interest    [government surplus]

Two monetary regimes:
  ISSUER — sovereign currency issuer (fixed rate, no endogenous spread)
  USER   — currency user / constrained sovereign (endogenous spread on
           government borrowing, forced fiscal consolidation when spread
           exceeds market-access threshold)

References:
  - Godley & Lavoie (2007), "Monetary Economics"
  - Minsky (1992), "The Financial Instability Hypothesis"
  - Mitchell, Wray & Watts (2019), "Macroeconomics"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

import numpy as np

from experiments.money_minsky_policy_mismatch.config import SFC_DEFAULTS, SFC_INITIAL


# ---------------------------------------------------------------------------
# Regime enum
# ---------------------------------------------------------------------------

class Regime(Enum):
    """Monetary regime: determines sovereign borrowing dynamics."""
    ISSUER = "ISSUER"
    USER = "USER"


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class SFCParams:
    """Parameters for the SFC model.

    Fiscal / monetary:
        G:     Government spending (exogenous baseline).
        tau:   Income tax rate (applied to all output).
        rL:    Interest rate on firm loans (also base sovereign rate).

    Behavioral:
        c1:    Marginal propensity to consume out of disposable income.
        c2:    Marginal propensity to consume out of wealth (net worth).
        kappa0: Autonomous investment.
        kappa1: Investment sensitivity to firm profits.
        kappa2: Investment sensitivity to firm leverage (debt drag).
        W:     Aggregate wage bill (simplified exogenous).

    Issuer-vs-user spread parameters:
        spread_phi:           Sensitivity of sovereign spread to debt/GDP.
        spread_threshold:     Debt/GDP ratio above which spread activates.
        market_access_spread: Spread level that triggers forced consolidation.

    Interest-income channel:
        mpc_interest:       Marginal propensity to consume out of sovereign
                            interest income.  Bondholders typically save more
                            than wage earners, so this is lower than c1.
        max_sovereign_rate: Interest rate ceiling for USER regime.  Beyond
                            this rate the market locks out entirely — the
                            government cannot borrow at any price.  Prevents
                            the endogenous spread from driving superexponential
                            debt/output dynamics.
    """
    G: float = SFC_DEFAULTS["G"]
    tau: float = SFC_DEFAULTS["tau"]
    rL: float = SFC_DEFAULTS["rL"]
    c1: float = SFC_DEFAULTS["c1"]
    c2: float = SFC_DEFAULTS["c2"]
    kappa0: float = SFC_DEFAULTS["kappa0"]
    kappa1: float = SFC_DEFAULTS["kappa1"]
    kappa2: float = SFC_DEFAULTS["kappa2"]
    W: float = SFC_DEFAULTS["W"]
    spread_phi: float = SFC_DEFAULTS["spread_phi"]
    spread_threshold: float = SFC_DEFAULTS["spread_threshold"]
    market_access_spread: float = SFC_DEFAULTS["market_access_spread"]
    mpc_interest: float = SFC_DEFAULTS["mpc_interest"]
    max_sovereign_rate: float = SFC_DEFAULTS["max_sovereign_rate"]


@dataclass
class SFCState:
    """State of the SFC economy at a single point in time.

    Flow variables:
        Y:      Aggregate output (GDP).
        C:      Household consumption.
        I:      Firm investment.
        T:      Tax revenue (= tau * Y).
        YD:     Household disposable income.
        Pi:     Firm after-tax profit.
        G_eff:  Effective government spending (may differ from G under USER).
        DEF:    Government deficit (G_eff + interest - T).
        interest_expense: Government interest payment on bonds.

    Stock variables:
        Nh:  Household net worth.
        Lf:  Firm loans outstanding.
        Bg:  Government debt stock.

    Price / rate:
        i_sovereign: Sovereign borrowing rate.
    """
    Y: float = 0.0
    C: float = 0.0
    I: float = 0.0
    T: float = 0.0
    YD: float = 0.0
    Pi: float = 0.0
    G_eff: float = 0.0
    Nh: float = 0.0
    Lf: float = 0.0
    DEF: float = 0.0
    Bg: float = 0.0
    i_sovereign: float = 0.0
    interest_expense: float = 0.0


@dataclass
class SFCHistory:
    """Time-series container for SFC model results."""
    Y: List[float] = field(default_factory=list)
    C: List[float] = field(default_factory=list)
    I: List[float] = field(default_factory=list)
    T: List[float] = field(default_factory=list)
    YD: List[float] = field(default_factory=list)
    Pi: List[float] = field(default_factory=list)
    G_eff: List[float] = field(default_factory=list)
    Nh: List[float] = field(default_factory=list)
    Lf: List[float] = field(default_factory=list)
    DEF: List[float] = field(default_factory=list)
    Bg: List[float] = field(default_factory=list)
    i_sovereign: List[float] = field(default_factory=list)
    interest_expense: List[float] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "Y": self.Y[:], "C": self.C[:], "I": self.I[:],
            "T": self.T[:], "YD": self.YD[:], "Pi": self.Pi[:],
            "G_eff": self.G_eff[:], "Nh": self.Nh[:], "Lf": self.Lf[:],
            "DEF": self.DEF[:], "Bg": self.Bg[:],
            "i_sovereign": self.i_sovereign[:],
            "interest_expense": self.interest_expense[:],
        }

    def verify_accounting(self, tol: float = 1e-6) -> bool:
        """Check the sectoral balance identity holds every period.

        The identity for a closed economy:
          FB_priv + FB_gov = 0
        where:
          FB_priv = (YD - C) + (Pi - I)  [household saving + firm net cash flow]
          FB_gov  = T - G_eff - interest  [government surplus]

        The proof:
          FB_priv = (1-tau)*Y + i_sov*Bg - C - I
          FB_gov  = tau*Y - G_eff - i_sov*Bg
          Sum     = Y - C - I - G_eff = 0  (since Y = C + I + G_eff)
        """
        n = len(self.Y)
        for t in range(n):
            hh_saving = self.YD[t] - self.C[t]
            firm_ncf = self.Pi[t] - self.I[t]
            fb_priv = hh_saving + firm_ncf
            fb_gov = self.T[t] - self.G_eff[t] - self.interest_expense[t]
            residual = fb_priv + fb_gov
            if abs(residual) > tol:
                raise AssertionError(
                    f"Sectoral balance violated at period {t}: "
                    f"FB_priv={fb_priv:.8f}, FB_gov={fb_gov:.8f}, "
                    f"residual={residual:.8e}"
                )
        return True


# ---------------------------------------------------------------------------
# One-period update
# ---------------------------------------------------------------------------

def sfc_step(state: SFCState, params: SFCParams, regime: Regime,
             max_iter: int = 50, tol: float = 1e-8) -> SFCState:
    """Advance the SFC model by one period.

    Income distribution (banks consolidated with households):
      - Household+bank income: (1-tau) * (W + rL*Lf) + i_sov*Bg
        = after-tax wages + after-tax bank profits + government bond interest
      - Firm after-tax profit: (1-tau) * (Y - W - rL*Lf)
      - Total: (1-tau)*Y + i_sov*Bg = Y - T + i_sov*Bg

    This ensures YD + Pi = Y - T + i_sov*Bg, so the sectoral balance
    identity holds by construction.
    """
    # Previous-period stocks
    Nh_prev = state.Nh
    Lf_prev = state.Lf
    Bg_prev = state.Bg
    Y_prev = max(state.Y, 1.0)

    # --- Sovereign rate and effective G ---
    # ISSUER: sovereign money financing — no interest on government liabilities.
    # USER: bond financing at market rate with endogenous spread.
    G_eff = params.G
    if regime == Regime.USER:
        debt_ratio = Bg_prev / max(Y_prev, 1.0)
        spread = params.spread_phi * max(debt_ratio - params.spread_threshold, 0.0)
        # Cap rate at max_sovereign_rate (market lockout beyond this)
        i_sov = min(params.rL + spread, params.max_sovereign_rate)
        interest_exp = i_sov * Bg_prev
        if spread > params.market_access_spread:
            cut_factor = max(1.0 - (spread - params.market_access_spread), 0.3)
            G_eff = params.G * cut_factor
    else:
        # Sovereign issuer: finances deficits through money creation.
        # Government liabilities are non-interest-bearing reserves.
        i_sov = 0.0
        interest_exp = 0.0

    # --- Predetermined variables ---
    # Household disposable income: after-tax (wages + bank profit) + bond interest
    # Banks consolidated with HH: bank income = rL*Lf (loan interest received)
    # HH+bank gross income = W + rL*Lf_prev
    # After tax: (1-tau)*(W + rL*Lf_prev)
    # Plus bond interest (not taxed, it's a government transfer): i_sov*Bg_prev
    YD_earned = (1.0 - params.tau) * (params.W + params.rL * Lf_prev)
    YD = YD_earned + interest_exp
    # Consumption: earned income at c1, interest income at mpc_interest.
    # Bondholders save more than wage earners — this prevents the USER regime
    # from generating explosive output through interest-transfer feedback.
    C = params.c1 * YD_earned + params.mpc_interest * interest_exp + params.c2 * Nh_prev

    # --- Solve Y = C + I(Y) + G_eff by iteration ---
    # Only I depends on Y (through firm profit Pi)
    Y_guess = Y_prev
    for _ in range(max_iter):
        Pi = (1.0 - params.tau) * (Y_guess - params.W - params.rL * Lf_prev)
        I_val = max(
            params.kappa0 + params.kappa1 * Pi
            - params.kappa2 * (Lf_prev / max(Y_guess, 1.0)),
            0.0,
        )
        Y_new = C + I_val + G_eff
        if abs(Y_new - Y_guess) < tol:
            Y_guess = Y_new
            break
        Y_guess = Y_new

    # Final values with converged Y
    Y = Y_guess
    T = params.tau * Y
    Pi = (1.0 - params.tau) * (Y - params.W - params.rL * Lf_prev)
    I_val = max(
        params.kappa0 + params.kappa1 * Pi
        - params.kappa2 * (Lf_prev / max(Y, 1.0)),
        0.0,
    )

    # --- Stock updates ---
    saving = YD - C
    Nh = Nh_prev + saving
    Lf = max(Lf_prev + I_val - Pi, 0.0)
    DEF = G_eff + interest_exp - T
    Bg = Bg_prev + DEF

    return SFCState(
        Y=Y, C=C, I=I_val, T=T, YD=YD, Pi=Pi, G_eff=G_eff,
        Nh=Nh, Lf=Lf, DEF=DEF, Bg=Bg,
        i_sovereign=i_sov, interest_expense=interest_exp,
    )


# ---------------------------------------------------------------------------
# Multi-period runner
# ---------------------------------------------------------------------------

def run_sfc(
    params: Optional[SFCParams] = None,
    initial: Optional[Dict[str, float]] = None,
    periods: int = 100,
    regime: str = "ISSUER",
    shocks: Optional[Dict[int, Dict[str, float]]] = None,
) -> SFCHistory:
    """Run the SFC model for multiple periods.

    Args:
        params:   SFCParams instance (defaults to SFCParams()).
        initial:  Dict of initial stock values (keys: Nh, Lf, Bg).
                  Defaults to SFC_INITIAL from config.
        periods:  Number of periods to simulate.
        regime:   'ISSUER' or 'USER' (string, converted to Regime enum).
        shocks:   Dict mapping period number to parameter overrides, e.g.
                  {50: {'G': 16.0}} means set G=16 starting at period 50.

    Returns:
        SFCHistory with time-series arrays for all variables.
    """
    if params is None:
        params = SFCParams()
    if initial is None:
        initial = dict(SFC_INITIAL)
    if shocks is None:
        shocks = {}

    regime_enum = Regime(regime)

    # Initial state — estimate starting Y from simple multiplier
    Y_init = params.G / (1.0 - params.c1 * (1.0 - params.tau))
    i_init = params.rL if regime_enum == Regime.USER else 0.0
    state = SFCState(
        Y=Y_init,
        Nh=initial.get("Nh", 100.0),
        Lf=initial.get("Lf", 50.0),
        Bg=initial.get("Bg", 60.0),
        i_sovereign=i_init,
    )

    history = SFCHistory()

    # Working copy of params that we can mutate for shocks
    working_params = SFCParams(
        G=params.G, tau=params.tau, rL=params.rL,
        c1=params.c1, c2=params.c2, kappa0=params.kappa0,
        kappa1=params.kappa1, kappa2=params.kappa2, W=params.W,
        spread_phi=params.spread_phi, spread_threshold=params.spread_threshold,
        market_access_spread=params.market_access_spread,
        mpc_interest=params.mpc_interest,
        max_sovereign_rate=params.max_sovereign_rate,
    )

    for t in range(periods):
        if t in shocks:
            for key, val in shocks[t].items():
                if hasattr(working_params, key):
                    setattr(working_params, key, val)

        state = sfc_step(state, working_params, regime_enum)

        # Record
        history.Y.append(state.Y)
        history.C.append(state.C)
        history.I.append(state.I)
        history.T.append(state.T)
        history.YD.append(state.YD)
        history.Pi.append(state.Pi)
        history.G_eff.append(state.G_eff)
        history.Nh.append(state.Nh)
        history.Lf.append(state.Lf)
        history.DEF.append(state.DEF)
        history.Bg.append(state.Bg)
        history.i_sovereign.append(state.i_sovereign)
        history.interest_expense.append(state.interest_expense)

    return history
