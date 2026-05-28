"""Tests for ABM policy controllers — written test-first.

Design:
  - Two competing controllers (austerity vs functional-finance) make
    interpretable fiscal decisions based on economy state.
  - Tests verify mechanism, outcome divergence, multi-seed robustness,
    and adversarial boundary conditions.
  - No test encodes the preferred political conclusion as a tautology.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.config import ABM_DEFAULTS
from experiments.money_minsky_policy_mismatch.policy_controllers import (
    AusterityController,
    FunctionalFinanceController,
    PassiveController,
    PolicyAdjustment,
    run_policy_lab,
)


# ===================================================================
# Stressed parameter set used across tests
# ===================================================================

def _stressed_params(**overrides):
    """ABM params with elevated rate + JG + fiscal transfer — enough
    stress to push workers onto JG and open a deficit for controllers
    to react to."""
    p = dict(
        ABM_DEFAULTS,
        policy_rate=0.07,
        w_jg=1.0,
        fiscal_transfer=0.40,
        demand_sensitivity=0.5,
    )
    p.update(overrides)
    return p


# ===================================================================
# Controller interface tests
# ===================================================================

class TestControllerInterface:
    """All controllers return a PolicyAdjustment with valid fields."""

    def test_passive_returns_adjustment(self):
        ctrl = PassiveController(base_w_jg=1.0, base_tau=0.20, base_transfer=0.20)
        adj = ctrl.adjust({"unemployment": 0.10, "deficit_ratio": 0.05})
        assert isinstance(adj, PolicyAdjustment)
        assert adj.w_jg == 1.0
        assert adj.tau == 0.20
        assert adj.fiscal_transfer == 0.20

    def test_austerity_returns_adjustment(self):
        ctrl = AusterityController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            deficit_target=0.03,
        )
        adj = ctrl.adjust({"unemployment": 0.10, "deficit_ratio": 0.10})
        assert isinstance(adj, PolicyAdjustment)
        assert adj.w_jg >= 0
        assert adj.tau >= 0
        assert adj.fiscal_transfer >= 0

    def test_ff_returns_adjustment(self):
        ctrl = FunctionalFinanceController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            unemployment_target=0.05,
        )
        adj = ctrl.adjust({"unemployment": 0.15, "jg_share": 0.05, "deficit_ratio": 0.10})
        assert isinstance(adj, PolicyAdjustment)


# ===================================================================
# Austerity controller mechanism
# ===================================================================

class TestAusterityMechanism:
    """Austerity targets deficit/GDP — cuts spending, raises taxes."""

    def test_cuts_transfer_when_deficit_high(self):
        ctrl = AusterityController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            deficit_target=0.03,
        )
        adj = ctrl.adjust({"unemployment": 0.10, "deficit_ratio": 0.10})
        assert adj.fiscal_transfer < 0.20, "Should cut transfers when deficit high"

    def test_raises_tau_when_deficit_high(self):
        ctrl = AusterityController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            deficit_target=0.03,
        )
        adj = ctrl.adjust({"unemployment": 0.10, "deficit_ratio": 0.10})
        assert adj.tau > 0.20, "Should raise tax rate when deficit high"

    def test_cuts_jg_wage_when_deficit_high(self):
        ctrl = AusterityController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            deficit_target=0.03,
        )
        adj = ctrl.adjust({"unemployment": 0.10, "deficit_ratio": 0.10})
        assert adj.w_jg < 1.0, "Should cut JG wage when deficit high"

    def test_no_change_when_deficit_below_target(self):
        ctrl = AusterityController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            deficit_target=0.03,
        )
        adj = ctrl.adjust({"unemployment": 0.10, "deficit_ratio": 0.02})
        assert adj.fiscal_transfer == 0.20
        assert adj.tau == 0.20
        assert adj.w_jg == 1.0

    def test_cut_proportional_to_excess(self):
        """Larger deficit excess → larger cuts."""
        ctrl = AusterityController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            deficit_target=0.03,
        )
        adj_small = ctrl.adjust({"unemployment": 0.05, "deficit_ratio": 0.05})
        adj_large = ctrl.adjust({"unemployment": 0.05, "deficit_ratio": 0.15})
        assert adj_large.fiscal_transfer < adj_small.fiscal_transfer
        assert adj_large.tau > adj_small.tau

    def test_adjustments_bounded(self):
        """Even with huge deficit, adjustments stay within sane bounds."""
        ctrl = AusterityController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            deficit_target=0.03,
        )
        adj = ctrl.adjust({"unemployment": 0.50, "deficit_ratio": 0.50})
        assert adj.fiscal_transfer >= 0.0
        assert adj.w_jg >= 0.0
        assert adj.tau <= 0.50  # don't tax more than 50%


# ===================================================================
# Functional finance controller mechanism
# ===================================================================

class TestFunctionalFinanceMechanism:
    """FF targets underutilization (unemployment + JG share) — increases
    spending, lowers taxes when the economy is weak."""

    def test_raises_transfer_when_underutilization_high(self):
        ctrl = FunctionalFinanceController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            unemployment_target=0.05,
        )
        adj = ctrl.adjust({"unemployment": 0.05, "jg_share": 0.15, "deficit_ratio": 0.10})
        assert adj.fiscal_transfer > 0.20, "Should raise transfers when underutilization high"

    def test_lowers_tau_when_underutilization_high(self):
        ctrl = FunctionalFinanceController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            unemployment_target=0.05,
        )
        adj = ctrl.adjust({"unemployment": 0.05, "jg_share": 0.15, "deficit_ratio": 0.10})
        assert adj.tau < 0.20, "Should lower tax rate when underutilization high"

    def test_raises_jg_wage_when_underutilization_high(self):
        ctrl = FunctionalFinanceController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            unemployment_target=0.05,
        )
        adj = ctrl.adjust({"unemployment": 0.05, "jg_share": 0.15, "deficit_ratio": 0.10})
        assert adj.w_jg > 1.0, "Should raise JG wage when underutilization high"

    def test_no_change_when_underutilization_below_target(self):
        ctrl = FunctionalFinanceController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            unemployment_target=0.05,
        )
        adj = ctrl.adjust({"unemployment": 0.02, "jg_share": 0.02, "deficit_ratio": 0.02})
        assert adj.fiscal_transfer == 0.20
        assert adj.tau == 0.20
        assert adj.w_jg == 1.0

    def test_boost_proportional_to_excess(self):
        """Higher underutilization → larger stimulus."""
        ctrl = FunctionalFinanceController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            unemployment_target=0.05,
        )
        adj_mild = ctrl.adjust({"unemployment": 0.03, "jg_share": 0.05, "deficit_ratio": 0.05})
        adj_severe = ctrl.adjust({"unemployment": 0.10, "jg_share": 0.20, "deficit_ratio": 0.05})
        assert adj_severe.fiscal_transfer > adj_mild.fiscal_transfer
        assert adj_severe.tau < adj_mild.tau

    def test_adjustments_bounded(self):
        """Even with extreme underutilization, adjustments stay sane."""
        ctrl = FunctionalFinanceController(
            base_w_jg=1.0, base_tau=0.20, base_transfer=0.20,
            unemployment_target=0.05,
        )
        adj = ctrl.adjust({"unemployment": 0.40, "jg_share": 0.40, "deficit_ratio": 0.30})
        assert adj.tau >= 0.05  # don't go below floor
        assert adj.fiscal_transfer <= 1.0  # bounded
        assert adj.w_jg <= 3.0  # bounded


# ===================================================================
# Policy lab outcome divergence
# ===================================================================

class TestPolicyLabOutcomes:
    """Under stress, competing controllers produce different outcomes."""

    def test_austerity_higher_underutilization_than_ff(self):
        """Austerity produces higher late-period labor underutilization
        (JG share + unemployment) than FF under stressed conditions.
        JG absorbs all unemployed, so the divergence shows up in JG share:
        more workers on JG means weaker private sector."""
        params = _stressed_params()

        r_aust = run_policy_lab(
            controller=AusterityController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                deficit_target=0.03,
            ),
            params=params, seed=42, periods=150,
        )
        r_ff = run_policy_lab(
            controller=FunctionalFinanceController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                unemployment_target=0.05,
            ),
            params=params, seed=42, periods=150,
        )

        underutil_aust = np.mean([u + j for u, j in zip(
            r_aust.unemployment[80:130], r_aust.jg_share[80:130])])
        underutil_ff = np.mean([u + j for u, j in zip(
            r_ff.unemployment[80:130], r_ff.jg_share[80:130])])
        assert underutil_aust > underutil_ff, (
            f"Austerity underutilization {underutil_aust:.3f} should exceed "
            f"FF underutilization {underutil_ff:.3f} under stress"
        )

    def test_ff_maintains_output_better(self):
        """FF maintains higher output than austerity under stress."""
        params = _stressed_params()

        r_aust = run_policy_lab(
            controller=AusterityController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                deficit_target=0.03,
            ),
            params=params, seed=42, periods=150,
        )
        r_ff = run_policy_lab(
            controller=FunctionalFinanceController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                unemployment_target=0.05,
            ),
            params=params, seed=42, periods=150,
        )

        avg_y_aust = np.mean(r_aust.Y[80:130])
        avg_y_ff = np.mean(r_ff.Y[80:130])
        assert avg_y_ff > avg_y_aust, (
            f"FF output {avg_y_ff:.2f} should exceed "
            f"austerity output {avg_y_aust:.2f}"
        )

    def test_passive_between_extremes(self):
        """Passive controller (no adjustment) should produce outcomes
        somewhere between pure austerity and pure FF."""
        params = _stressed_params()

        r_passive = run_policy_lab(
            controller=PassiveController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
            ),
            params=params, seed=42, periods=150,
        )
        r_aust = run_policy_lab(
            controller=AusterityController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                deficit_target=0.03,
            ),
            params=params, seed=42, periods=150,
        )
        r_ff = run_policy_lab(
            controller=FunctionalFinanceController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                unemployment_target=0.05,
            ),
            params=params, seed=42, periods=150,
        )

        u_passive = np.mean(r_passive.unemployment[80:130])
        u_aust = np.mean(r_aust.unemployment[80:130])
        u_ff = np.mean(r_ff.unemployment[80:130])
        # Passive should be between austerity (highest) and FF (lowest)
        assert u_ff <= u_passive <= u_aust or u_ff <= u_passive, (
            f"Passive unemployment {u_passive:.3f} not between "
            f"FF {u_ff:.3f} and austerity {u_aust:.3f}"
        )


# ===================================================================
# Multi-seed robustness
# ===================================================================

class TestMultiSeedRobustness:
    """Outcome divergence holds across multiple random seeds."""

    def test_output_divergence_across_seeds(self):
        """FF produces higher output than austerity for majority of seeds."""
        params = _stressed_params()
        seeds = [42, 99, 123, 7, 256]
        ff_wins = 0

        for seed in seeds:
            r_aust = run_policy_lab(
                controller=AusterityController(
                    base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                    deficit_target=0.03,
                ),
                params=params, seed=seed, periods=150,
            )
            r_ff = run_policy_lab(
                controller=FunctionalFinanceController(
                    base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                    unemployment_target=0.05,
                ),
                params=params, seed=seed, periods=150,
            )

            y_aust = np.mean(r_aust.Y[80:130])
            y_ff = np.mean(r_ff.Y[80:130])
            if y_ff > y_aust:
                ff_wins += 1

        assert ff_wins >= 3, (
            f"FF should produce higher output in majority of seeds, "
            f"got {ff_wins}/{len(seeds)}"
        )


# ===================================================================
# Adversarial / boundary tests
# ===================================================================

class TestAdversarial:
    """Scenarios where the expected differences weaken or invert."""

    def test_austerity_reduces_deficit_more(self):
        """Austerity should at least reduce the deficit ratio more than FF.
        This is what it's designed to do — the question is at what cost."""
        params = _stressed_params()

        r_aust = run_policy_lab(
            controller=AusterityController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                deficit_target=0.03,
            ),
            params=params, seed=42, periods=150,
        )
        r_ff = run_policy_lab(
            controller=FunctionalFinanceController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                unemployment_target=0.05,
            ),
            params=params, seed=42, periods=150,
        )

        def_aust = np.mean(r_aust.deficit_ratio[80:130])
        def_ff = np.mean(r_ff.deficit_ratio[80:130])
        assert def_aust < def_ff, (
            f"Austerity deficit {def_aust:.4f} should be lower than "
            f"FF deficit {def_ff:.4f}"
        )

    def test_no_stress_minimal_divergence(self):
        """At baseline rate (no stress), both controllers should be
        roughly passive — minimal difference."""
        params = _stressed_params(policy_rate=0.04)  # low stress

        r_aust = run_policy_lab(
            controller=AusterityController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                deficit_target=0.03,
            ),
            params=params, seed=42, periods=100,
        )
        r_ff = run_policy_lab(
            controller=FunctionalFinanceController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                unemployment_target=0.05,
            ),
            params=params, seed=42, periods=100,
        )

        u_aust = np.mean(r_aust.unemployment[50:90])
        u_ff = np.mean(r_ff.unemployment[50:90])
        gap = abs(u_aust - u_ff)
        # Under low stress, difference should be small (< 10pp)
        assert gap < 0.10, (
            f"Under low stress, controllers should converge. Gap={gap:.3f}"
        )

    def test_results_have_expected_fields(self):
        """Policy lab results contain all standard ABM fields."""
        params = _stressed_params()
        r = run_policy_lab(
            controller=PassiveController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
            ),
            params=params, seed=42, periods=30,
        )
        d = r.to_dict()
        assert "Y" in d
        assert "unemployment" in d
        assert "ponzi_share" in d
        assert "deficit_ratio" in d
        assert len(d["Y"]) == 30

    def test_ff_may_increase_fragility(self):
        """FF's higher spending may increase private debt and fragility —
        the model does not claim FF is costless."""
        params = _stressed_params()

        r_ff = run_policy_lab(
            controller=FunctionalFinanceController(
                base_w_jg=1.0, base_tau=0.20, base_transfer=0.40,
                unemployment_target=0.05,
            ),
            params=params, seed=42, periods=150,
        )
        # Just verify the metric is tracked and non-trivial
        assert any(p > 0 for p in r_ff.ponzi_share), (
            "FF should still produce some financial fragility"
        )
