"""Experiment runners for Money-Minsky-Policy-Mismatch simulations.

The package now has two layers:

- rebuilt core experiments used by the blog
- legacy exploratory experiments retained for comparison
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from typing import Dict, List, Optional

import numpy as np

from experiments.money_minsky_policy_mismatch.config import (
    ABM_DEFAULTS,
    AUSTERITY_SWEEP,
    DEFAULT_SEED,
    JG_SWEEP,
    KEEN_CRISIS_THRESHOLD,
    KEEN_ODE_DEFAULTS,
    KEEN_ODE_INITIAL,
    RATE_HIKE_SWEEP,
    SFC_DEFAULTS,
    SFC_INITIAL,
)
from experiments.money_minsky_policy_mismatch.keen_ode import (
    detect_crisis,
    solve_keen,
    KeenResult,
)
from experiments.money_minsky_policy_mismatch.policy_sectoral_model import (
    run_policy_sectoral_experiment,
)
from experiments.money_minsky_policy_mismatch.austerity_counterfactual import (
    run_imf_counterfactual_experiment,
)
from experiments.money_minsky_policy_mismatch.fragility_regimes import (
    run_fragility_regime_experiment,
)
from experiments.money_minsky_policy_mismatch.sfc_model import (
    SFCParams,
    run_sfc,
)
from experiments.money_minsky_policy_mismatch.abm_model import run_abm
from experiments.money_minsky_policy_mismatch.comparative_constraints import (
    ConstraintParams,
    run_comparative,
)
from experiments.money_minsky_policy_mismatch.policy_controllers import (
    AusterityController,
    FunctionalFinanceController,
    PassiveController,
    run_policy_lab,
)
from experiments.money_minsky_policy_mismatch.capacity_constraint import (
    CapacityParams,
    run_capacity_model,
)
from experiments.money_minsky_policy_mismatch.sovereign_securities import (
    RolloverParams,
    run_rollover_model,
)
from experiments.money_minsky_policy_mismatch.external_constraint import (
    ExternalParams,
    run_external_model,
)
from experiments.money_minsky_policy_mismatch.holder_composition import (
    HolderParams,
    HolderShares,
    run_holder_model,
)


# ---------------------------------------------------------------------------
# Visualization helper: stable vs crisis Keen ODE trajectories
# ---------------------------------------------------------------------------

def run_keen_stable_vs_crisis(
    seed: int = DEFAULT_SEED,
    t_span: tuple = (0.0, 300.0),
) -> dict:
    """Generate two Keen ODE trajectories for visualization.

    Stable: low initial debt (d0=0.3) — produces bounded limit cycle.
    Crisis: high initial debt (d0=2.0) — debt eventually explodes.

    Returns:
        Dict with 'stable' and 'crisis' keys, each a KeenResult.to_dict().
    """
    params = dict(KEEN_ODE_DEFAULTS)
    y0_stable = [KEEN_ODE_INITIAL[0], KEEN_ODE_INITIAL[1], 0.3]
    y0_crisis = [KEEN_ODE_INITIAL[0], KEEN_ODE_INITIAL[1], 2.0]

    r_stable = solve_keen(params, y0_stable, t_span)
    r_crisis = solve_keen(params, y0_crisis, t_span)

    return {
        "stable": r_stable.to_dict(),
        "crisis": r_crisis.to_dict(),
    }


def run_argument_rebuild_experiments(
    seed: int = DEFAULT_SEED,
    refresh_data: bool = False,
) -> dict:
    """Run the three rebuilt experiment families used by the article.

    1. Sectoral accounting + policy response
    2. Public-data-backed austerity counterfactuals
    3. Fragility regime comparison for monetary tightening
    """
    del seed  # kept for symmetry with other experiment runners
    return {
        "policy_sectoral": run_policy_sectoral_experiment(),
        "imf_counterfactual": run_imf_counterfactual_experiment(refresh_data=refresh_data),
        "fragility_regimes": run_fragility_regime_experiment(),
    }


# ---------------------------------------------------------------------------
# Experiment 1: Rate hike under leverage (Keen ODE)
# ---------------------------------------------------------------------------

def run_rate_hike_experiment(
    seed: int = DEFAULT_SEED,
    delta_r_list: Optional[List[float]] = None,
    initial_d_list: Optional[List[float]] = None,
    t_span: tuple = (0.0, 200.0),
) -> dict:
    """Sweep interest rate shocks across initial debt levels.

    Tests the Minsky mechanism: rate hikes under high leverage trigger crisis,
    while the same hike under low leverage does not.

    Returns:
        Dict with keys: 'grid' (rate x debt matrix of crisis times),
        'delta_r', 'initial_d', 'threshold'.
    """
    if delta_r_list is None:
        delta_r_list = RATE_HIKE_SWEEP["delta_r"]
    if initial_d_list is None:
        initial_d_list = RATE_HIKE_SWEEP["initial_d"]

    crisis_grid = np.full((len(delta_r_list), len(initial_d_list)), np.nan)

    for i, dr in enumerate(delta_r_list):
        for j, d0 in enumerate(initial_d_list):
            params = dict(KEEN_ODE_DEFAULTS)
            params["r"] = params["r"] + dr
            y0 = [KEEN_ODE_INITIAL[0], KEEN_ODE_INITIAL[1], d0]

            result = solve_keen(params, y0, t_span)
            crisis_idx = detect_crisis(result, KEEN_CRISIS_THRESHOLD)
            if crisis_idx is not None:
                crisis_grid[i, j] = result.t[crisis_idx]

    return {
        "grid": crisis_grid.tolist(),
        "delta_r": delta_r_list,
        "initial_d": initial_d_list,
        "threshold": KEEN_CRISIS_THRESHOLD,
    }


# ---------------------------------------------------------------------------
# Experiment 2: Austerity vs functional finance (SFC + ABM)
# ---------------------------------------------------------------------------

def run_austerity_experiment(
    seed: int = DEFAULT_SEED,
    sfc_periods: int = 150,
    abm_periods: int = 100,
) -> dict:
    """Compare austerity vs functional finance policy responses.

    SFC: government cuts spending at period 50 (austerity) vs maintains (FF).
    ABM: austerity_phi > 0 vs austerity_phi = 0.

    Returns:
        Dict with 'sfc_baseline', 'sfc_austerity', 'abm_baseline', 'abm_austerity'.
    """
    # SFC: baseline (functional finance)
    sfc_base = run_sfc(periods=sfc_periods)

    # SFC: austerity shock at period 50
    sfc_aust = run_sfc(
        periods=sfc_periods,
        shocks={50: {"G": 14.0}},  # 30% spending cut
    )

    # ABM: elevated rate so fragility actually appears, JG on so austerity
    # has a real channel (cutting the safety net).
    abm_params_base = dict(ABM_DEFAULTS, policy_rate=0.06, w_jg=1.0,
                            austerity_phi=0.0)
    abm_base = run_abm(params=abm_params_base, periods=abm_periods, seed=seed)

    # ABM: same stressed economy but with austerity cutting JG spending
    abm_params_aust = dict(ABM_DEFAULTS, policy_rate=0.06, w_jg=1.0,
                            austerity_phi=0.5)
    abm_aust = run_abm(params=abm_params_aust, periods=abm_periods, seed=seed)

    return {
        "sfc_baseline": sfc_base.to_dict(),
        "sfc_austerity": sfc_aust.to_dict(),
        "abm_baseline": abm_base.to_dict(),
        "abm_austerity": abm_aust.to_dict(),
    }


# ---------------------------------------------------------------------------
# Experiment 3: Job Guarantee vs NAIRU (ABM)
# ---------------------------------------------------------------------------

def run_jg_experiment(
    seed: int = DEFAULT_SEED,
    periods: int = 100,
    w_jg_ratios: Optional[List[float]] = None,
) -> dict:
    """Compare JG at different wage levels vs no JG (NAIRU baseline).

    Returns:
        Dict mapping w_jg_ratio -> ABMResult.to_dict().
    """
    if w_jg_ratios is None:
        w_jg_ratios = JG_SWEEP["w_jg_ratio"]

    # Elevated rate generates meaningful unemployment for JG to absorb
    base_wage = ABM_DEFAULTS["base_productivity"] * (1.0 + ABM_DEFAULTS["firm_markup"]) * 0.5
    results = {}

    for ratio in w_jg_ratios:
        w_jg = ratio * base_wage
        params = dict(ABM_DEFAULTS, policy_rate=0.06, w_jg=w_jg)
        r = run_abm(params=params, periods=periods, seed=seed)
        results[str(ratio)] = r.to_dict()

    return results


# ---------------------------------------------------------------------------
# Experiment 4: Issuer vs User under shock (SFC)
# ---------------------------------------------------------------------------

def run_issuer_vs_user_experiment(
    seed: int = DEFAULT_SEED,
    periods: int = 100,
    shock_period: int = 30,
    shock_G: float = 14.0,
) -> dict:
    """Same negative fiscal shock under ISSUER vs USER regimes.

    Returns:
        Dict with 'issuer' and 'user' SFCHistory.to_dict().
    """
    user_params = SFCParams(spread_phi=0.02)
    shock = {shock_period: {"G": shock_G}}

    h_issuer = run_sfc(
        periods=periods,
        regime="ISSUER",
        shocks=shock,
    )
    h_user = run_sfc(
        params=user_params,
        periods=periods,
        regime="USER",
        shocks=shock,
    )

    return {
        "issuer": h_issuer.to_dict(),
        "user": h_user.to_dict(),
        "shock_period": shock_period,
        "shock_G": shock_G,
    }


# ---------------------------------------------------------------------------
# Experiment 5: Comparative constraint — household vs user vs issuer
# ---------------------------------------------------------------------------

def run_comparative_constraint_experiment(
    params: Optional[ConstraintParams] = None,
) -> dict:
    """Compare spending, output, and debt paths across three entity types
    facing the same private-demand shock.

    The three entities differ only in their financing constraint:
      HOUSEHOLD        — hard budget constraint, endogenous borrowing rate
      CURRENCY_USER    — market-access constraint, endogenous sovereign spread
      SOVEREIGN_ISSUER — no financing constraint, policy-set rate

    Returns:
        Dict with keys ``"household"``, ``"currency_user"``,
        ``"sovereign_issuer"`` (each an EntityHistory.to_dict()), plus
        ``"shock_period"`` and ``"demand_shock"`` metadata.
    """
    if params is None:
        params = ConstraintParams()

    histories = run_comparative(params)

    return {
        "household": histories["household"].to_dict(),
        "currency_user": histories["currency_user"].to_dict(),
        "sovereign_issuer": histories["sovereign_issuer"].to_dict(),
        "shock_period": params.shock_period,
        "demand_shock": params.demand_shock,
    }


# ---------------------------------------------------------------------------
# Experiment 6: ABM policy lab — austerity vs functional finance
# ---------------------------------------------------------------------------

def run_policy_lab_experiment(
    seed: int = DEFAULT_SEED,
    periods: int = 150,
) -> dict:
    """Compare austerity vs functional-finance policy controllers
    under stressed ABM conditions.

    Stressed conditions: elevated policy rate (0.07) + JG active + fiscal
    transfers — enough to generate unemployment and deficits for the
    controllers to react to.

    Returns:
        Dict with keys ``"austerity"``, ``"functional_finance"``,
        ``"passive"`` (each ABMResult.to_dict()), plus metadata.
    """
    stressed = dict(
        ABM_DEFAULTS,
        policy_rate=0.07,
        w_jg=1.0,
        fiscal_transfer=0.40,
        demand_sensitivity=0.5,
    )
    base_w_jg = 1.0
    base_tau = stressed["tau"]
    base_transfer = 0.40

    r_aust = run_policy_lab(
        controller=AusterityController(
            base_w_jg=base_w_jg, base_tau=base_tau,
            base_transfer=base_transfer, deficit_target=0.03,
        ),
        params=stressed, seed=seed, periods=periods,
    )
    r_ff = run_policy_lab(
        controller=FunctionalFinanceController(
            base_w_jg=base_w_jg, base_tau=base_tau,
            base_transfer=base_transfer, unemployment_target=0.05,
        ),
        params=stressed, seed=seed, periods=periods,
    )
    r_passive = run_policy_lab(
        controller=PassiveController(
            base_w_jg=base_w_jg, base_tau=base_tau,
            base_transfer=base_transfer,
        ),
        params=stressed, seed=seed, periods=periods,
    )

    return {
        "austerity": r_aust.to_dict(),
        "functional_finance": r_ff.to_dict(),
        "passive": r_passive.to_dict(),
        "policy_rate": stressed["policy_rate"],
        "periods": periods,
    }


# ---------------------------------------------------------------------------
# Experiment 7: Real-capacity constraint boundary
# ---------------------------------------------------------------------------

def run_capacity_constraint_experiment() -> dict:
    """Compare the effect of government spending under slack vs tight
    capacity conditions.

    Under slack: extra G creates real output without inflation.
    At capacity: extra G creates inflation, not output.

    Returns:
        Dict with ``"slack"`` and ``"tight"`` results, plus
        ``"spending_ramp"`` showing the transition.
    """
    slack = run_capacity_model(CapacityParams(
        capacity=200.0, base_private_demand=60.0, base_G=30.0, periods=40,
    ))
    tight = run_capacity_model(CapacityParams(
        capacity=100.0, base_private_demand=60.0, base_G=60.0, periods=40,
    ))
    ramp = run_capacity_model(
        CapacityParams(capacity=100.0, base_private_demand=50.0, periods=60),
        spending_path={t: 20.0 + t for t in range(60)},
    )

    return {
        "slack": slack,
        "tight": tight,
        "spending_ramp": ramp,
    }


# ---------------------------------------------------------------------------
# Experiment 8: Sovereign securities — rollover and maturity structure
# ---------------------------------------------------------------------------

def run_rollover_experiment() -> dict:
    """Compare fiscal dynamics under different maturity structures and
    regime types.

    Shows that the same debt/GDP ratio produces different outcomes
    depending on maturity structure and whether the entity is a
    sovereign issuer or currency user.

    Returns:
        Dict with ``"issuer_short"``, ``"issuer_long"``,
        ``"user_short"``, ``"user_long"`` rollover results.
    """
    common = dict(initial_debt=50.0, periods=60)

    return {
        "issuer_short": run_rollover_model(RolloverParams(
            regime="ISSUER", short_share=0.80, **common,
        )),
        "issuer_long": run_rollover_model(RolloverParams(
            regime="ISSUER", short_share=0.20, **common,
        )),
        "user_short": run_rollover_model(RolloverParams(
            regime="USER", short_share=0.80,
            rollover_phi=0.10, spread_phi=0.08, **common,
        )),
        "user_long": run_rollover_model(RolloverParams(
            regime="USER", short_share=0.20,
            rollover_phi=0.10, spread_phi=0.08, **common,
        )),
    }


# ---------------------------------------------------------------------------
# Experiment 9: External constraint — import dependence and FX stress
# ---------------------------------------------------------------------------

def run_external_constraint_experiment() -> dict:
    """Compare fiscal space under low vs high import dependence.

    Shows that domestic monetary space works under low external
    dependence but faces real limits when import dependence is high.

    Returns:
        Dict with ``"low_dependence"`` and ``"high_dependence"`` results.
    """
    return {
        "low_dependence": run_external_model(ExternalParams(
            import_share=0.05, export_earnings=20.0,
            base_G=35.0, periods=50,
        )),
        "high_dependence": run_external_model(ExternalParams(
            import_share=0.40, export_earnings=15.0,
            base_G=35.0, periods=50,
        )),
    }


# ---------------------------------------------------------------------------
# Experiment 10: Holder composition — who holds the debt
# ---------------------------------------------------------------------------

def run_holder_composition_experiment() -> dict:
    """Compare macro and distributional effects under different holder mixes.

    Same nominal debt and rate; the only thing that changes is *who*
    holds the bonds.

    Returns:
        Dict with ``"household_heavy"``, ``"asset_heavy"``,
        ``"foreign_heavy"``, ``"cb_heavy"`` results.
    """
    common = dict(debt_stock=200.0, periods=60)

    return {
        "household_heavy": run_holder_model(HolderParams(
            shares=HolderShares(household=0.80, asset=0.10,
                                foreign=0.05, central_bank=0.05),
            **common,
        )),
        "asset_heavy": run_holder_model(HolderParams(
            shares=HolderShares(household=0.10, asset=0.80,
                                foreign=0.05, central_bank=0.05),
            **common,
        )),
        "foreign_heavy": run_holder_model(HolderParams(
            shares=HolderShares(household=0.10, asset=0.10,
                                foreign=0.70, central_bank=0.10),
            **common,
        )),
        "cb_heavy": run_holder_model(HolderParams(
            shares=HolderShares(household=0.20, asset=0.20,
                                foreign=0.10, central_bank=0.50),
            **common,
        )),
    }
