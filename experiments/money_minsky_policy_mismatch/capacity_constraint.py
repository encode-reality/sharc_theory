"""Real-capacity constraint model.

A minimal model showing what genuinely constrains government spending:
not financial bookkeeping, but real productive capacity.

Under slack (demand < capacity):
  - Extra public spending creates real output.
  - Inflation is zero.
  - The fiscal multiplier operates at full strength.

At capacity (demand >= capacity):
  - Extra public spending creates inflation, not output.
  - Real output is bounded near capacity.
  - The fiscal multiplier collapses.

The model is intentionally simple — a supply-demand boundary with a
Keynesian multiplier below capacity and a price-pressure mechanism
above it.  It does not pretend to be a full macro model.  Its purpose
is to show that the real limit on sovereign spending is productive
capacity, not a financial budget constraint.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class CapacityParams:
    """Parameters for the capacity constraint model.

    Supply side:
        capacity:            Initial productive capacity (labor × productivity).
        productivity_growth:  Per-period growth rate of capacity.

    Demand side:
        base_private_demand: Autonomous private demand (C + I baseline).
        base_G:              Government spending level.
        mpc:                 Marginal propensity to consume (for multiplier).
        tax_rate:            Tax rate (for multiplier denominator).

    Price mechanism:
        inflation_sensitivity: How fast inflation rises when demand > capacity.
        inflation_persistence: Inertia of inflation (0 = no memory, 1 = full).
        output_leakage:        Fraction of excess demand that becomes real
                               output (rest becomes inflation).  Represents
                               overtime, imports, running down inventories.

    Simulation:
        periods: Number of periods.
    """
    periods: int = 60
    capacity: float = 100.0
    productivity_growth: float = 0.005
    base_private_demand: float = 60.0
    base_G: float = 20.0
    mpc: float = 0.65
    tax_rate: float = 0.25
    inflation_sensitivity: float = 0.5
    inflation_persistence: float = 0.3
    output_leakage: float = 0.10


def run_capacity_model(
    params: Optional[CapacityParams] = None,
    spending_path: Optional[Dict[int, float]] = None,
) -> Dict[str, List[float]]:
    """Run the capacity constraint model.

    Args:
        params:        Model parameters.
        spending_path: Optional dict mapping period → G override.

    Returns:
        Dict with time-series lists: ``output``, ``inflation``,
        ``capacity``, ``demand``, ``utilization``, ``price_level``,
        ``G``.
    """
    if params is None:
        params = CapacityParams()

    # Keynesian multiplier denominator
    denom = 1.0 - params.mpc * (1.0 - params.tax_rate)

    capacity = params.capacity
    inflation = 0.0
    price_level = 1.0

    history: Dict[str, List[float]] = {
        "output": [],
        "inflation": [],
        "capacity": [],
        "demand": [],
        "utilization": [],
        "price_level": [],
        "G": [],
    }

    for t in range(params.periods):
        G = (spending_path[t] if spending_path and t in spending_path
             else params.base_G)

        # Aggregate demand via multiplier
        demand = (params.base_private_demand + G) / denom

        # Utilization
        utilization = demand / max(capacity, 1.0)

        # Output and inflation pressure
        if utilization <= 1.0:
            # Slack: all demand becomes real output, no inflation
            output = demand
            inflation_pressure = 0.0
        else:
            # Tight: capacity binds.  A small fraction of excess demand
            # leaks into real output (overtime, imports); the rest is
            # pure price pressure.
            excess = demand - capacity
            output = capacity + params.output_leakage * excess
            inflation_pressure = (
                params.inflation_sensitivity * (utilization - 1.0)
            )

        # Inflation with persistence
        inflation = (
            params.inflation_persistence * inflation + inflation_pressure
        )
        price_level *= (1.0 + inflation)

        # Record
        history["output"].append(output)
        history["inflation"].append(inflation)
        history["capacity"].append(capacity)
        history["demand"].append(demand)
        history["utilization"].append(utilization)
        history["price_level"].append(price_level)
        history["G"].append(G)

        # Capacity grows
        capacity *= (1.0 + params.productivity_growth)

    return history
