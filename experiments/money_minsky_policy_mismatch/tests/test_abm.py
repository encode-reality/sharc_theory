"""Tests for ABM with Minsky financial fragility classifier.

Validates: Minsky classification, endogenous money, reproducibility,
aggregate consistency, Job Guarantee effects, and fragility dynamics.
"""
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.abm_model import (
    ABMResult,
    Bank,
    Firm,
    Household,
    MacroABM,
    classify_minsky,
    run_abm,
)
from experiments.money_minsky_policy_mismatch.config import ABM_DEFAULTS, DEFAULT_SEED


class TestMinskyClassifier:
    """Minsky taxonomy: hedge / speculative / Ponzi based on cash-flow coverage."""

    def test_hedge_firm(self):
        """Cash flow covers both interest and principal -> hedge."""
        f = Firm(firm_id=0, cash_flow=10.0, interest_due=3.0, principal_due=5.0)
        assert classify_minsky(f) == "hedge"

    def test_speculative_firm(self):
        """Cash flow covers interest but not principal -> speculative."""
        f = Firm(firm_id=0, cash_flow=4.0, interest_due=3.0, principal_due=5.0)
        assert classify_minsky(f) == "speculative"

    def test_ponzi_firm(self):
        """Cash flow insufficient even for interest -> Ponzi."""
        f = Firm(firm_id=0, cash_flow=1.0, interest_due=3.0, principal_due=5.0)
        assert classify_minsky(f) == "ponzi"

    def test_boundary_hedge_speculative(self):
        """Cash flow exactly covers interest + principal -> hedge."""
        f = Firm(firm_id=0, cash_flow=8.0, interest_due=3.0, principal_due=5.0)
        assert classify_minsky(f) == "hedge"

    def test_boundary_speculative_ponzi(self):
        """Cash flow exactly covers interest -> speculative."""
        f = Firm(firm_id=0, cash_flow=3.0, interest_due=3.0, principal_due=5.0)
        assert classify_minsky(f) == "speculative"

    def test_zero_debt_is_hedge(self):
        """Firm with no debt obligations is always hedge."""
        f = Firm(firm_id=0, cash_flow=5.0, interest_due=0.0, principal_due=0.0)
        assert classify_minsky(f) == "hedge"

    def test_negative_cash_flow_is_ponzi(self):
        """Negative cash flow firm is always Ponzi."""
        f = Firm(firm_id=0, cash_flow=-2.0, interest_due=1.0, principal_due=1.0)
        assert classify_minsky(f) == "ponzi"


class TestEndogenousMoney:
    """Every loan creates an equal deposit (ΔL = ΔD)."""

    def test_loan_creates_equal_deposit(self):
        """When a bank creates a loan, firm deposits increase by the same amount."""
        model = MacroABM(seed=42)
        firm = model.firms[0]
        bank = model.banks[0]

        debt_before = firm.debt
        deposits_before = firm.deposits
        bank_loans_before = bank.loans
        bank_deposits_before = bank.deposits

        amount = 100.0
        model._create_loan(firm, bank, amount)

        assert firm.debt - debt_before == pytest.approx(amount)
        assert firm.deposits - deposits_before == pytest.approx(amount)
        assert bank.loans - bank_loans_before == pytest.approx(amount)
        assert bank.deposits - bank_deposits_before == pytest.approx(amount)

    def test_loan_deposit_equality_in_simulation(self):
        """Over a full simulation, net loan creation = net deposit creation."""
        model = MacroABM(seed=42)
        for _ in range(20):
            model.step()
            # Check that each loan event has ΔL = ΔD
            for dl, dd in model._loan_deposit_log:
                assert dl == pytest.approx(dd), "Every loan must create equal deposit"


class TestReproducibility:
    """Same seed -> same trajectory."""

    def test_same_seed_same_output(self):
        """Two runs with the same seed produce identical results."""
        r1 = run_abm(seed=42, periods=50)
        r2 = run_abm(seed=42, periods=50)
        assert r1.Y == r2.Y
        assert r1.unemployment == r2.unemployment
        assert r1.ponzi_share == r2.ponzi_share

    def test_different_seed_different_output(self):
        """Different seeds produce different trajectories."""
        r1 = run_abm(seed=42, periods=50)
        r2 = run_abm(seed=99, periods=50)
        # At least some values should differ
        assert r1.Y != r2.Y


class TestAggregates:
    """Aggregate consistency checks."""

    def test_output_is_sum_of_firm_outputs(self):
        """Total output = sum of individual firm outputs."""
        model = MacroABM(seed=42)
        for _ in range(10):
            model.step()
        Y = model.compute_output()
        firm_sum = sum(f.output for f in model.firms if f.alive)
        assert Y == pytest.approx(firm_sum)

    def test_minsky_shares_sum_to_one(self):
        """Hedge + speculative + Ponzi shares sum to 1.0 (for alive firms)."""
        result = run_abm(seed=42, periods=50)
        for t in range(50):
            total = result.hedge_share[t] + result.speculative_share[t] + result.ponzi_share[t]
            # Shares should sum to ~1.0 if any firms are alive
            if result.Y[t] > 0:
                assert total == pytest.approx(1.0, abs=0.01), (
                    f"Period {t}: shares sum to {total}, expected 1.0"
                )

    def test_unemployment_in_valid_range(self):
        """Unemployment rate is between 0 and 1."""
        result = run_abm(seed=42, periods=50)
        for u in result.unemployment:
            assert 0.0 <= u <= 1.0

    def test_output_positive(self):
        """Output should be positive in early periods."""
        result = run_abm(seed=42, periods=50)
        assert result.Y[0] > 0, "Initial output should be positive"
        assert result.Y[5] > 0, "Output should be positive in early periods"


class TestABMResult:
    """ABMResult dataclass: to_dict, data integrity."""

    def test_to_dict_keys(self):
        """to_dict contains all expected keys."""
        r = run_abm(seed=42, periods=10)
        d = r.to_dict()
        expected = {"periods", "Y", "unemployment", "jg_share", "debt_ratio",
                    "ponzi_share", "speculative_share", "hedge_share",
                    "deficit_ratio", "total_deposits", "total_loans"}
        assert set(d.keys()) == expected

    def test_all_arrays_same_length(self):
        """All time-series arrays have the expected length."""
        r = run_abm(seed=42, periods=30)
        for key in ["Y", "unemployment", "ponzi_share", "debt_ratio"]:
            assert len(getattr(r, key)) == 30, f"{key} should have length 30"


class TestJobGuarantee:
    """JG reduces unemployment by absorbing unemployed into public employment."""

    def test_jg_reduces_unemployment(self):
        """With JG at elevated rate, unemployment drops and JG absorbs workers."""
        # Use elevated rate to generate unemployment that JG can absorb
        p_no_jg = dict(ABM_DEFAULTS, policy_rate=0.06, w_jg=0.0)
        p_jg = dict(ABM_DEFAULTS, policy_rate=0.06, w_jg=1.0)

        r_no_jg = run_abm(params=p_no_jg, seed=42, periods=100)
        r_jg = run_abm(params=p_jg, seed=42, periods=100)

        avg_u_no_jg = np.mean(r_no_jg.unemployment[-20:])
        avg_u_jg = np.mean(r_jg.unemployment[-20:])
        avg_jg_share = np.mean(r_jg.jg_share[-20:])

        # JG must absorb workers AND reduce unemployment
        assert avg_jg_share > 0, "JG should employ workers"
        assert avg_u_jg < avg_u_no_jg, (
            f"JG should reduce unemployment: {avg_u_jg:.3f} >= {avg_u_no_jg:.3f}"
        )

    def test_no_jg_means_zero_jg_share(self):
        """Without JG (w_jg=0), no one should be JG-employed."""
        p = dict(ABM_DEFAULTS, w_jg=0.0)
        r = run_abm(params=p, seed=42, periods=30)
        assert all(j == 0.0 for j in r.jg_share), "No JG share when JG is off"


class TestFragilityDynamics:
    """Under stress, the system should transition toward greater fragility."""

    def test_high_rate_increases_fragility(self):
        """Higher policy rate should increase peak and mean non-hedge share."""
        p_low = dict(ABM_DEFAULTS, policy_rate=0.04)
        p_high = dict(ABM_DEFAULTS, policy_rate=0.08)

        r_low = run_abm(params=p_low, seed=42, periods=200)
        r_high = run_abm(params=p_high, seed=42, periods=200)

        # Use mean fragility over the full run (not tail, since crisis may pass)
        mean_nh_low = np.mean([1 - h for h in r_low.hedge_share])
        mean_nh_high = np.mean([1 - h for h in r_high.hedge_share])
        assert mean_nh_high > mean_nh_low, (
            f"Higher rate should increase mean fragility: "
            f"low={mean_nh_low:.3f}, high={mean_nh_high:.3f}"
        )

        # Also check peak fragility
        peak_nh_low = max(1 - h for h in r_low.hedge_share)
        peak_nh_high = max(1 - h for h in r_high.hedge_share)
        assert peak_nh_high > peak_nh_low, (
            f"Higher rate should increase peak fragility: "
            f"low={peak_nh_low:.3f}, high={peak_nh_high:.3f}"
        )
