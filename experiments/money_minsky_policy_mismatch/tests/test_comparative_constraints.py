"""Tests for the comparative constraint simulation.

Design principles:
  - Tests cover the *mechanism*, not the preferred conclusion.
  - Each headline claim gets a confirming test, a boundary test, and a
    challenging test (where the claim weakens or fails).
  - No test asserts the political interpretation — only structural and
    quantitative properties.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.comparative_constraints import (
    ConstraintParams,
    EntityHistory,
    EntityType,
    run_comparative,
    _autonomous_demand,
)
from experiments.money_minsky_policy_mismatch.experiments import (
    run_comparative_constraint_experiment,
)


# ===================================================================
# Structural / accounting tests
# ===================================================================

class TestStructure:
    """All entities start from the same shock and produce valid output."""

    def test_all_three_entities_present(self):
        r = run_comparative(ConstraintParams(periods=10))
        assert set(r.keys()) == {"household", "currency_user", "sovereign_issuer"}

    def test_all_histories_same_length(self):
        p = ConstraintParams(periods=60)
        r = run_comparative(p)
        for key, h in r.items():
            assert len(h.spending) == 60, f"{key} has wrong length"
            assert len(h.output) == 60, f"{key} has wrong length"

    def test_spending_positive(self):
        """Spending never goes negative for any entity."""
        r = run_comparative()
        for key, h in r.items():
            assert all(s >= 0 for s in h.spending), f"{key} has negative spending"

    def test_pre_shock_spending_at_target(self):
        """Before the shock, all entities should spend at or near target."""
        p = ConstraintParams(periods=40, shock_period=30)
        r = run_comparative(p)
        target = p.spending_target
        for key, h in r.items():
            # Check periods 5-25 (after initial transient, before shock)
            pre_shock = h.spending[5:25]
            avg = np.mean(pre_shock)
            assert avg == pytest.approx(target, rel=0.05), (
                f"{key} pre-shock spending {avg:.2f} deviates from target {target}"
            )

    def test_autonomous_demand_path(self):
        """Demand drops at shock_period, then recovers."""
        p = ConstraintParams(shock_period=10, demand_shock=-0.20, recovery_rate=0.01)
        pre = _autonomous_demand(5, p)
        at_shock = _autonomous_demand(10, p)
        later = _autonomous_demand(30, p)
        assert pre == pytest.approx(p.base_autonomous)
        assert at_shock == pytest.approx(p.base_autonomous * 0.80)
        assert later > at_shock  # partial recovery
        assert later <= p.base_autonomous  # not yet fully recovered at t=30

    def test_government_deficit_accounting(self):
        """For government entities: deficit = spending + interest - revenue."""
        r = run_comparative()
        for key in ("currency_user", "sovereign_issuer"):
            h = r[key]
            for t in range(1, len(h.spending)):
                deficit = h.spending[t] + h.interest_expense[t] - h.revenue[t]
                debt_change = h.debt[t] - h.debt[t - 1]
                assert debt_change == pytest.approx(deficit, abs=0.01), (
                    f"{key} period {t}: debt change {debt_change:.4f} != "
                    f"deficit {deficit:.4f}"
                )


# ===================================================================
# Mechanism tests — confirming direction
# ===================================================================

class TestMechanisms:
    """Each entity responds differently because of its constraint structure."""

    def test_household_eventually_constrained(self):
        """After a persistent revenue shock, the household hits its borrowing
        ceiling and spending falls below target."""
        p = ConstraintParams(
            periods=100, shock_period=10, demand_shock=-0.30,
            recovery_rate=0.005,  # slow recovery
        )
        r = run_comparative(p)
        hh = r["household"]
        # At some point after the shock, constraint should bind
        post_shock_constrained = any(hh.constraint_binding[20:])
        assert post_shock_constrained, (
            "Household should eventually be constrained by borrowing limit"
        )

    def test_currency_user_faces_consolidation(self):
        """Under a large shock, the currency user eventually faces forced
        spending cuts from market-access constraints."""
        p = ConstraintParams(
            periods=120, shock_period=20, demand_shock=-0.25,
            recovery_rate=0.003,
            cu_spread_phi=0.15,
            cu_market_access_spread=0.08,
        )
        r = run_comparative(p)
        cu = r["currency_user"]
        post_shock_constrained = any(cu.constraint_binding[30:])
        assert post_shock_constrained, (
            "Currency user should face market-access constraint under large shock"
        )

    def test_sovereign_issuer_never_constrained(self):
        """The sovereign issuer is structurally never constrained, regardless
        of shock size."""
        p = ConstraintParams(
            periods=100, shock_period=10, demand_shock=-0.40,
            recovery_rate=0.002,
        )
        r = run_comparative(p)
        si = r["sovereign_issuer"]
        assert not any(si.constraint_binding), (
            "Sovereign issuer must never face a financing constraint"
        )

    def test_issuer_spending_gap_always_zero(self):
        """Sovereign issuer's spending gap is always zero."""
        r = run_comparative()
        si = r["sovereign_issuer"]
        assert all(g == pytest.approx(0.0) for g in si.spending_gap)

    def test_issuer_maintains_output_better_than_user(self):
        """After the shock, the sovereign issuer's output should be at least
        as high as the currency user's, because the issuer maintains spending."""
        p = ConstraintParams(
            periods=100, shock_period=20, demand_shock=-0.25,
            recovery_rate=0.005,
            cu_spread_phi=0.12,
            cu_market_access_spread=0.08,
        )
        r = run_comparative(p)
        cu_post = np.mean(r["currency_user"].output[50:80])
        si_post = np.mean(r["sovereign_issuer"].output[50:80])
        assert si_post >= cu_post, (
            f"Issuer output {si_post:.2f} should be >= user output {cu_post:.2f}"
        )

    def test_household_no_macro_feedback(self):
        """Household output equals spending (no multiplier feedback)."""
        r = run_comparative()
        hh = r["household"]
        for t in range(len(hh.output)):
            assert hh.output[t] == pytest.approx(hh.spending[t])

    def test_user_spread_rises_with_debt(self):
        """Currency user's interest rate rises as debt/GDP ratio increases."""
        p = ConstraintParams(
            periods=80, shock_period=10, demand_shock=-0.25,
            recovery_rate=0.003,
        )
        r = run_comparative(p)
        cu = r["currency_user"]
        early_rate = cu.interest_rate[15]
        late_rate = cu.interest_rate[-1]
        assert late_rate > early_rate, (
            "Currency user rate should rise as debt accumulates"
        )


# ===================================================================
# Boundary tests
# ===================================================================

class TestBoundaries:
    """When parameters are extreme, the model should still behave sensibly."""

    def test_no_shock_all_stable(self):
        """With zero shock, all entities maintain spending at target."""
        p = ConstraintParams(periods=50, demand_shock=0.0)
        r = run_comparative(p)
        target = p.spending_target
        for key, h in r.items():
            for t in range(5, 50):
                assert h.spending[t] == pytest.approx(target, rel=0.02), (
                    f"{key} spending drifted without a shock"
                )

    def test_tiny_shock_minimal_divergence(self):
        """A tiny shock should produce only small differences between entities."""
        p = ConstraintParams(periods=60, demand_shock=-0.01, recovery_rate=0.01)
        r = run_comparative(p)
        # All entities should be within 5% of each other on spending
        for t in range(40, 60):
            values = [r[k].spending[t] for k in r]
            spread = max(values) - min(values)
            assert spread < 0.05 * p.spending_target, (
                f"Tiny shock should not cause large divergence at period {t}"
            )

    def test_household_unlimited_borrowing_matches_target(self):
        """If the household has no borrowing limit, it maintains spending."""
        p = ConstraintParams(
            periods=60, shock_period=10, demand_shock=-0.20,
            hh_max_debt_ratio=100.0,  # effectively unlimited
        )
        r = run_comparative(p)
        hh = r["household"]
        # Should maintain target throughout (unlimited borrowing)
        for t in range(len(hh.spending)):
            assert hh.spending[t] == pytest.approx(p.spending_target, rel=0.01), (
                f"Household with unlimited borrowing should maintain target"
            )

    def test_user_zero_spread_acts_like_issuer(self):
        """With cu_spread_phi=0, currency user has no market constraint and
        should behave identically to sovereign issuer (same rate aside)."""
        p = ConstraintParams(
            periods=60, shock_period=20, demand_shock=-0.15,
            cu_spread_phi=0.0,
            cu_r_base=0.02,  # match issuer rate
            si_r_policy=0.02,
        )
        r = run_comparative(p)
        cu = r["currency_user"]
        si = r["sovereign_issuer"]
        # Spending should be identical (neither is constrained)
        for t in range(len(cu.spending)):
            assert cu.spending[t] == pytest.approx(si.spending[t], abs=0.01)
        # Output should be identical (same multiplier, same spending, same A)
        for t in range(len(cu.output)):
            assert cu.output[t] == pytest.approx(si.output[t], abs=0.1)


# ===================================================================
# Adversarial / challenging tests
# ===================================================================

class TestAdversarial:
    """Scenarios where the expected contrast weakens or reverses.
    These prevent the model from being used to overclaim."""

    def test_issuer_debt_grows_without_bound_under_persistent_shock(self):
        """Even a sovereign issuer accumulates debt indefinitely if the shock
        never recovers.  The model does not claim debt is irrelevant — only
        that the *financing constraint* differs."""
        p = ConstraintParams(
            periods=200, shock_period=10, demand_shock=-0.25,
            recovery_rate=0.0,  # no recovery
        )
        r = run_comparative(p)
        si = r["sovereign_issuer"]
        assert si.debt[-1] > si.debt[20], (
            "Issuer debt should grow under permanent revenue shortfall"
        )
        # Debt/output should also rise
        assert si.debt_ratio[-1] > si.debt_ratio[20]

    def test_user_may_stabilize_under_mild_conditions(self):
        """Under a mild shock with generous market access, the currency user
        may never face forced consolidation — the difference is muted."""
        p = ConstraintParams(
            periods=80, shock_period=20, demand_shock=-0.05,
            recovery_rate=0.01,
            cu_spread_phi=0.02,  # very gentle spread
            cu_market_access_spread=0.50,  # very generous
        )
        r = run_comparative(p)
        cu = r["currency_user"]
        # Should never be constrained under these mild conditions
        assert not any(cu.constraint_binding), (
            "Under mild conditions, user should not face market constraint"
        )

    def test_household_with_no_debt_and_high_income_is_fine(self):
        """A household with no initial debt and income above spending target
        is never constrained — the constraint is structural, not universal."""
        p = ConstraintParams(
            periods=60, shock_period=20, demand_shock=-0.10,
            initial_debt=0.0,
            hh_income_share=1.2,  # income > spending target before shock
        )
        r = run_comparative(p)
        hh = r["household"]
        assert not any(hh.constraint_binding), (
            "Wealthy, high-income household should not be constrained"
        )

    def test_extreme_consolidation_contracts_user_output(self):
        """Forced consolidation reduces the currency user's output by cutting
        spending, which feeds back to lower revenue (self-defeating austerity).
        The test verifies the mechanism, not that it's bad policy."""
        p = ConstraintParams(
            periods=100, shock_period=15, demand_shock=-0.30,
            recovery_rate=0.002,
            cu_spread_phi=0.20,
            cu_market_access_spread=0.05,
        )
        r = run_comparative(p)
        cu = r["currency_user"]
        si = r["sovereign_issuer"]
        # After consolidation bites, user output should be lower than issuer
        cu_late = np.mean(cu.output[60:90])
        si_late = np.mean(si.output[60:90])
        assert cu_late < si_late, (
            "Consolidation should reduce user output below issuer output"
        )

    def test_no_explosive_output(self):
        """No entity should produce explosive output growth.  This guards
        against the interest-transfer artifact found in the earlier SFC model."""
        p = ConstraintParams(periods=150, demand_shock=-0.20, recovery_rate=0.005)
        r = run_comparative(p)
        for key, h in r.items():
            max_output = max(h.output)
            initial_output = h.output[0]
            ratio = max_output / max(initial_output, 1.0)
            assert ratio < 5.0, (
                f"{key} output ratio {ratio:.1f}x looks explosive"
            )


# ===================================================================
# Experiment runner integration test
# ===================================================================

class TestExperimentRunner:
    """The experiment runner should produce valid, serializable output."""

    def test_returns_expected_keys(self):
        r = run_comparative_constraint_experiment(
            ConstraintParams(periods=20)
        )
        assert set(r.keys()) == {
            "household", "currency_user", "sovereign_issuer",
            "shock_period", "demand_shock",
        }

    def test_results_are_serializable(self):
        """All values should be JSON-safe (no numpy arrays, no booleans-as-int)."""
        r = run_comparative_constraint_experiment(
            ConstraintParams(periods=20)
        )
        for key in ("household", "currency_user", "sovereign_issuer"):
            d = r[key]
            assert isinstance(d, dict)
            assert isinstance(d["spending"], list)
            assert isinstance(d["constraint_binding"], list)
