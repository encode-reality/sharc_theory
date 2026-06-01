"""Holder-composition and distribution channel.

Same nominal debt, different holder mix → different recirculation,
leakage, and distribution effects.

Holder types:
  HOUSEHOLD     — high-MPC domestic holder (workers, pensioners).
                  Interest income recirculates as consumption demand.
  ASSET_HOLDER  — low-MPC domestic holder (wealthy savers, financial sector).
                  Interest income mostly accumulates as wealth.
  FOREIGN       — non-domestic holder.  Interest income leaks abroad,
                  no domestic demand effect.
  CENTRAL_BANK  — central-bank holdings.  Interest is remitted back to
                  the treasury (net zero domestic cost).

The model is intentionally stylized.  It illustrates that *who* holds
public liabilities matters for macro dynamics and distribution, even
when the nominal debt stock is the same.  It does not pretend to be a
calibrated political-economy model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(frozen=True)
class HolderShares:
    """Fractions of debt held by each holder type.  Must sum to 1.0."""
    household: float = 0.40
    asset: float = 0.30
    foreign: float = 0.20
    central_bank: float = 0.10

    def __post_init__(self):
        total = self.household + self.asset + self.foreign + self.central_bank
        if abs(total - 1.0) > 1e-6:
            raise ValueError(
                f"HolderShares must sum to 1.0 (got {total:.4f})"
            )


@dataclass
class HolderParams:
    """Parameters for the holder-composition model.

    Fiscal context:
        base_G:              Government spending.
        base_private_demand: Autonomous private demand.
        mpc:                 Aggregate MPC (for multiplier).
        tax_rate:            Tax rate.

    Debt:
        debt_stock:    Constant nominal debt for stylized comparison.
        interest_rate: Coupon paid on the debt.

    Holder MPCs:
        mpc_household: Marginal propensity to consume out of interest
                       income for high-MPC households.
        mpc_asset:     Marginal propensity to consume out of interest
                       income for low-MPC asset holders.
        (Foreign MPC is effectively 0 for the domestic economy.
         Central-bank interest is remitted back, not consumed.)

    Composition:
        shares: HolderShares with the holder mix.

    Simulation:
        periods: Number of periods.
    """
    periods: int = 50

    # Fiscal context
    base_G: float = 30.0
    base_private_demand: float = 50.0
    mpc: float = 0.65
    tax_rate: float = 0.25

    # Debt
    debt_stock: float = 100.0
    interest_rate: float = 0.04

    # Holder MPCs
    mpc_household: float = 0.85
    mpc_asset: float = 0.15

    # Composition
    shares: HolderShares = field(default_factory=HolderShares)


def run_holder_model(
    params: Optional[HolderParams] = None,
) -> Dict[str, List[float]]:
    """Run the holder-composition model.

    Returns dict with time-series lists: output, domestic_recirculation,
    foreign_leakage, cb_remittance, net_interest_cost, hh_wealth,
    asset_wealth, wealth_concentration.
    """
    if params is None:
        params = HolderParams()

    denom = 1.0 - params.mpc * (1.0 - params.tax_rate)
    s = params.shares
    D = params.debt_stock
    r = params.interest_rate

    # Per-period interest flows (constant since D and r are constant)
    int_household = s.household * r * D
    int_asset = s.asset * r * D
    int_foreign = s.foreign * r * D
    int_cb = s.central_bank * r * D
    total_interest = r * D

    # After-tax interest consumed by domestic holders
    domestic_recirculation = (
        params.mpc_household * (1.0 - params.tax_rate) * int_household
        + params.mpc_asset * (1.0 - params.tax_rate) * int_asset
    )
    foreign_leakage = int_foreign  # leaves the domestic economy
    cb_remittance = int_cb         # returns to treasury
    net_interest_cost = total_interest - cb_remittance

    # Wealth accumulation: savings (1 - MPC) × interest
    hh_savings_per_period = (1.0 - params.mpc_household) * int_household
    asset_savings_per_period = (1.0 - params.mpc_asset) * int_asset

    hh_wealth = 0.0
    asset_wealth = 0.0

    history: Dict[str, List[float]] = {
        "output": [],
        "domestic_recirculation": [],
        "foreign_leakage": [],
        "cb_remittance": [],
        "net_interest_cost": [],
        "hh_wealth": [],
        "asset_wealth": [],
        "wealth_concentration": [],
    }

    for t in range(params.periods):
        # Aggregate demand: base + multiplied recirculation injection
        # Output = (A + G + recirculation) / denom
        output = (
            params.base_private_demand
            + params.base_G
            + domestic_recirculation
        ) / denom

        # Update wealth stocks
        hh_wealth += hh_savings_per_period
        asset_wealth += asset_savings_per_period

        # Wealth concentration: asset-holder share of total domestic wealth
        total_wealth = hh_wealth + asset_wealth
        if total_wealth > 0:
            concentration = asset_wealth / total_wealth
        else:
            concentration = 0.5  # neutral when no wealth has accumulated

        history["output"].append(output)
        history["domestic_recirculation"].append(domestic_recirculation)
        history["foreign_leakage"].append(foreign_leakage)
        history["cb_remittance"].append(cb_remittance)
        history["net_interest_cost"].append(net_interest_cost)
        history["hh_wealth"].append(hh_wealth)
        history["asset_wealth"].append(asset_wealth)
        history["wealth_concentration"].append(concentration)

    return history
