"""External-constraint model: import dependence and FX stress.

Shows that domestic monetary space does not erase real external limits.
A sovereign issuer that depends heavily on imported essentials can face
inflationary pressure from the external sector even when domestic
capacity has slack.

Two channels:
  1. Import leakage: higher import share weakens the domestic fiscal
     multiplier (demand leaks abroad).
  2. FX stress: when the import bill exceeds export earnings, the
     external gap creates currency pressure and imported inflation.

The model complements the domestic-capacity story (capacity_constraint.py)
by adding the external dimension.  It does not negate the thesis — under
low dependence, domestic monetary space works as described.  Under high
dependence, the external constraint binds before the domestic one.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ExternalParams:
    """Parameters for the external-constraint model.

    Domestic:
        base_private_demand: Autonomous private demand.
        base_G:              Government spending.
        mpc:                 Marginal propensity to consume.
        tax_rate:            Tax rate.
        capacity:            Productive capacity (for domestic inflation).

    External:
        import_share:     Fraction of aggregate demand satisfied by imports.
        export_earnings:  Exogenous export revenue (FX inflow).
        fx_pass_through:  How much FX stress passes into domestic prices.
        fx_persistence:   Inertia of FX stress (0–1).
        external_buffer:  FX reserves / buffer before stress activates.

    Simulation:
        periods: Number of periods.
    """
    periods: int = 60

    # Domestic
    base_private_demand: float = 50.0
    base_G: float = 30.0
    mpc: float = 0.65
    tax_rate: float = 0.25
    capacity: float = 150.0

    # External
    import_share: float = 0.20
    export_earnings: float = 20.0
    fx_pass_through: float = 0.4
    fx_persistence: float = 0.3
    external_buffer: float = 5.0


def run_external_model(
    params: Optional[ExternalParams] = None,
) -> Dict[str, List[float]]:
    """Run the external-constraint model.

    Returns dict with time-series lists: output, inflation,
    import_bill, export_earnings, external_gap, fx_stress,
    imported_inflation, domestic_inflation, spending.
    """
    if params is None:
        params = ExternalParams()

    # Multiplier denominator adjusted for import leakage
    denom = 1.0 - params.mpc * (1.0 - params.tax_rate) + params.import_share

    fx_stress = 0.0

    history: Dict[str, List[float]] = {
        "output": [],
        "inflation": [],
        "import_bill": [],
        "export_earnings": [],
        "external_gap": [],
        "fx_stress": [],
        "imported_inflation": [],
        "domestic_inflation": [],
        "spending": [],
    }

    for t in range(params.periods):
        spending = params.base_G

        # Aggregate demand via multiplier (with import leakage)
        demand = (params.base_private_demand + spending) / denom

        # Domestic output (capped by capacity)
        if demand <= params.capacity:
            output = demand
            domestic_inflation = 0.0
        else:
            output = params.capacity + 0.10 * (demand - params.capacity)
            domestic_inflation = 0.3 * max(demand / params.capacity - 1.0, 0.0)

        # Import bill: share of demand goes to imports
        import_bill = params.import_share * demand

        # External gap
        external_gap = import_bill - params.export_earnings

        # FX stress: accumulates when external gap exceeds buffer
        fx_pressure = params.fx_pass_through * max(
            external_gap - params.external_buffer, 0.0
        ) / max(params.export_earnings, 1.0)
        fx_stress = params.fx_persistence * fx_stress + fx_pressure

        # Imported inflation from FX stress
        imported_inflation = max(fx_stress, 0.0)

        # Total inflation
        inflation = domestic_inflation + imported_inflation

        history["output"].append(output)
        history["inflation"].append(inflation)
        history["import_bill"].append(import_bill)
        history["export_earnings"].append(params.export_earnings)
        history["external_gap"].append(external_gap)
        history["fx_stress"].append(fx_stress)
        history["imported_inflation"].append(imported_inflation)
        history["domestic_inflation"].append(domestic_inflation)
        history["spending"].append(spending)

    return history
