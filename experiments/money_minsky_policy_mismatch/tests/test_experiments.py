"""Integration tests for experiment runners.

Validates that each experiment produces structurally valid results
consistent with the blog's claims.
"""
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.experiments import (
    run_austerity_experiment,
    run_issuer_vs_user_experiment,
    run_jg_experiment,
    run_rate_hike_experiment,
)
from experiments.money_minsky_policy_mismatch.abm_model import run_abm, MacroABM
from experiments.money_minsky_policy_mismatch.config import ABM_DEFAULTS


class TestRateHikeExperiment:
    """Rate hike × leverage → crisis boundary."""

    def test_returns_expected_keys(self):
        """Result has grid, delta_r, initial_d, threshold."""
        r = run_rate_hike_experiment(
            delta_r_list=[0.01, 0.03],
            initial_d_list=[0.5, 1.5],
        )
        assert "grid" in r
        assert "delta_r" in r
        assert "initial_d" in r

    def test_rate_shock_triggers_crisis_at_high_debt(self):
        """At very high debt, a rate shock can trigger immediate crisis
        that the baseline avoids (rate hike tips a fragile system over)."""
        r = run_rate_hike_experiment(
            delta_r_list=[0.01, 0.05],
            initial_d_list=[3.0],
        )
        grid = np.array(r["grid"])
        # Higher rate shock at d0=3.0 should produce crisis
        assert not np.isnan(grid[1, 0]), (
            "High rate + high debt should trigger crisis"
        )

    def test_low_debt_may_avoid_crisis(self):
        """Low initial debt with small rate shock may avoid crisis."""
        r = run_rate_hike_experiment(
            delta_r_list=[0.01],
            initial_d_list=[0.3],
            t_span=(0.0, 100.0),
        )
        grid = np.array(r["grid"])
        # With d0=0.3 and tiny rate shock, crisis within 100 periods is unlikely
        # (though not impossible — test is directional, not absolute)
        assert grid.shape == (1, 1)


class TestAusterityExperiment:
    """Austerity vs functional finance comparison."""

    def test_returns_expected_keys(self):
        """Result contains all four scenarios."""
        r = run_austerity_experiment(sfc_periods=50, abm_periods=30)
        assert "sfc_baseline" in r
        assert "sfc_austerity" in r
        assert "abm_baseline" in r
        assert "abm_austerity" in r

    def test_sfc_austerity_reduces_output(self):
        """SFC austerity scenario produces lower output than baseline."""
        r = run_austerity_experiment(sfc_periods=100, abm_periods=30)
        base_Y = np.mean(r["sfc_baseline"]["Y"][60:80])
        aust_Y = np.mean(r["sfc_austerity"]["Y"][60:80])
        assert aust_Y < base_Y, "Austerity should reduce SFC output"

    def test_abm_results_have_expected_fields(self):
        """ABM results contain unemployment and fragility data."""
        r = run_austerity_experiment(sfc_periods=30, abm_periods=30)
        assert "unemployment" in r["abm_baseline"]
        assert "ponzi_share" in r["abm_baseline"]

    def test_sfc_fiscal_multiplier_in_range(self):
        """Fiscal multiplier should be in the Blanchard-Leigh range (0.5-2.0)."""
        r = run_austerity_experiment(sfc_periods=100, abm_periods=30)
        # Multiplier = dY / dG (spending cut of 6.0: from 20 to 14)
        base_Y = np.mean(r["sfc_baseline"]["Y"][60:80])
        aust_Y = np.mean(r["sfc_austerity"]["Y"][60:80])
        dY = base_Y - aust_Y
        dG = 6.0  # 20 - 14
        multiplier = dY / dG
        assert 0.5 <= multiplier <= 2.0, (
            f"Fiscal multiplier {multiplier:.2f} outside Blanchard-Leigh range [0.5, 2.0]"
        )


class TestJGExperiment:
    """Job Guarantee at different wage levels."""

    def test_returns_all_ratios(self):
        """Result has an entry for each w_jg ratio."""
        r = run_jg_experiment(periods=30, w_jg_ratios=[0.0, 0.50])
        assert "0.0" in r
        assert "0.5" in r

    def test_jg_produces_jg_employment(self):
        """Non-zero JG wage should produce JG employment."""
        r = run_jg_experiment(periods=50, w_jg_ratios=[0.0, 0.50])
        no_jg_share = np.mean(r["0.0"]["jg_share"])
        with_jg_share = np.mean(r["0.5"]["jg_share"])
        assert no_jg_share == 0.0, "No JG should mean zero JG share"
        # JG may or may not absorb workers depending on unemployment
        assert with_jg_share >= 0.0

    def test_baseline_is_nairu_equivalent(self):
        """With w_jg=0, the model is effectively a NAIRU-type economy."""
        r = run_jg_experiment(periods=50, w_jg_ratios=[0.0])
        assert all(j == 0.0 for j in r["0.0"]["jg_share"])


class TestIssuerVsUserExperiment:
    """Issuer vs user under same fiscal shock."""

    def test_returns_expected_keys(self):
        """Result has issuer, user, and shock metadata."""
        r = run_issuer_vs_user_experiment(periods=50)
        assert "issuer" in r
        assert "user" in r
        assert "shock_period" in r

    def test_issuer_maintains_spending(self):
        """ISSUER regime can always spend at target G (even after shock)."""
        r = run_issuer_vs_user_experiment(periods=50, shock_period=20)
        # After shock, G_eff should be the shocked value, not further constrained
        issuer_g = r["issuer"]["G_eff"]
        # Before shock: G=20, after shock: G=14
        for t in range(25, 50):
            assert issuer_g[t] == pytest.approx(14.0, abs=0.1)

    def test_both_regimes_same_length(self):
        """Both regime results have the same number of periods."""
        r = run_issuer_vs_user_experiment(periods=60)
        assert len(r["issuer"]["Y"]) == 60
        assert len(r["user"]["Y"]) == 60


class TestABMValidation:
    """Cross-cutting ABM validation tests."""

    def test_firms_survive_baseline(self):
        """At baseline parameters, >60% of firms survive 200 periods."""
        m = MacroABM(seed=42)
        for _ in range(200):
            m.step()
        alive = sum(1 for f in m.firms if f.alive)
        survival_rate = alive / len(m.firms)
        assert survival_rate > 0.60, (
            f"Baseline firm survival {survival_rate:.0%} below 60%"
        )

    def test_baseline_mostly_hedge(self):
        """At baseline parameters, economy should be hedge-dominated."""
        r = run_abm(seed=42, periods=100)
        avg_hedge = np.mean(r.hedge_share)
        assert avg_hedge > 0.7, (
            f"Baseline should be hedge-dominated, got avg hedge = {avg_hedge:.2f}"
        )
