"""Tests for the holder-composition model — written test-first.

Shows that *who holds public liabilities* matters: the same nominal debt
produces different recirculation, leakage, and distribution effects
depending on the holder mix.

This is intentionally stylized.  The test suite reflects what the
mechanism does and does not establish.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.holder_composition import (
    HolderParams,
    HolderShares,
    run_holder_model,
)


# ===================================================================
# Structure
# ===================================================================

class TestStructure:

    def test_returns_expected_keys(self):
        r = run_holder_model()
        for key in (
            "output", "domestic_recirculation", "foreign_leakage",
            "cb_remittance", "net_interest_cost", "hh_wealth",
            "asset_wealth", "wealth_concentration",
        ):
            assert key in r, f"Missing key: {key}"

    def test_all_arrays_same_length(self):
        p = HolderParams(periods=40)
        r = run_holder_model(p)
        lengths = {k: len(v) for k, v in r.items() if isinstance(v, list)}
        assert len(set(lengths.values())) == 1
        assert list(lengths.values())[0] == 40

    def test_holder_shares_sum_to_one(self):
        """Constructor should accept shares that sum to ~1.0."""
        # Valid shares
        shares = HolderShares(household=0.4, asset=0.3, foreign=0.2, central_bank=0.1)
        total = shares.household + shares.asset + shares.foreign + shares.central_bank
        assert total == pytest.approx(1.0)

    def test_invalid_shares_rejected(self):
        """Shares that don't sum to 1.0 should raise."""
        with pytest.raises(ValueError):
            HolderShares(household=0.5, asset=0.3, foreign=0.5, central_bank=0.0)


# ===================================================================
# Holder mechanism
# ===================================================================

class TestHolderMechanism:
    """Different holders create different recirculation."""

    def test_high_mpc_holder_higher_recirculation(self):
        """When debt is held mostly by high-MPC households, more interest
        income recirculates as domestic demand."""
        p_hh = HolderParams(
            shares=HolderShares(household=0.90, asset=0.10, foreign=0.0, central_bank=0.0),
            periods=30,
        )
        p_asset = HolderParams(
            shares=HolderShares(household=0.10, asset=0.90, foreign=0.0, central_bank=0.0),
            periods=30,
        )
        r_hh = run_holder_model(p_hh)
        r_asset = run_holder_model(p_asset)

        avg_recirc_hh = np.mean(r_hh["domestic_recirculation"][5:25])
        avg_recirc_asset = np.mean(r_asset["domestic_recirculation"][5:25])
        assert avg_recirc_hh > avg_recirc_asset, (
            f"HH-held recirculation {avg_recirc_hh:.2f} should exceed "
            f"asset-held {avg_recirc_asset:.2f}"
        )

    def test_foreign_holdings_create_leakage(self):
        """Foreign-held debt creates real foreign leakage; domestic-held
        debt does not."""
        p_dom = HolderParams(
            shares=HolderShares(household=1.0, asset=0.0, foreign=0.0, central_bank=0.0),
            periods=20,
        )
        p_for = HolderParams(
            shares=HolderShares(household=0.30, asset=0.0, foreign=0.70, central_bank=0.0),
            periods=20,
        )
        r_dom = run_holder_model(p_dom)
        r_for = run_holder_model(p_for)

        leakage_dom = np.mean(r_dom["foreign_leakage"][5:18])
        leakage_for = np.mean(r_for["foreign_leakage"][5:18])
        assert leakage_for > leakage_dom, (
            f"Foreign-held leakage {leakage_for:.2f} should exceed "
            f"domestic-held {leakage_dom:.2f}"
        )

    def test_central_bank_holdings_remit_back(self):
        """Central-bank-held debt: interest is remitted back to treasury,
        reducing the net interest cost."""
        p_market = HolderParams(
            shares=HolderShares(household=0.50, asset=0.50, foreign=0.0, central_bank=0.0),
            periods=20,
        )
        p_cb = HolderParams(
            shares=HolderShares(household=0.25, asset=0.25, foreign=0.0, central_bank=0.50),
            periods=20,
        )
        r_market = run_holder_model(p_market)
        r_cb = run_holder_model(p_cb)

        net_market = np.mean(r_market["net_interest_cost"][5:18])
        net_cb = np.mean(r_cb["net_interest_cost"][5:18])
        assert net_cb < net_market, (
            f"CB-holding net cost {net_cb:.2f} should be lower than "
            f"market-only {net_market:.2f}"
        )

    def test_high_recirculation_higher_output(self):
        """When more interest recirculates, output should be higher."""
        p_hh = HolderParams(
            shares=HolderShares(household=0.90, asset=0.10, foreign=0.0, central_bank=0.0),
            debt_stock=200.0, periods=30,
        )
        p_asset = HolderParams(
            shares=HolderShares(household=0.10, asset=0.90, foreign=0.0, central_bank=0.0),
            debt_stock=200.0, periods=30,
        )
        r_hh = run_holder_model(p_hh)
        r_asset = run_holder_model(p_asset)

        y_hh = np.mean(r_hh["output"][5:25])
        y_asset = np.mean(r_asset["output"][5:25])
        assert y_hh > y_asset, (
            f"Output under HH-held {y_hh:.2f} should exceed asset-held {y_asset:.2f}"
        )


# ===================================================================
# Distribution effects
# ===================================================================

class TestDistributionEffects:

    def test_asset_held_concentrates_wealth(self):
        """When asset holders dominate, wealth concentration grows."""
        p_asset = HolderParams(
            shares=HolderShares(household=0.20, asset=0.80, foreign=0.0, central_bank=0.0),
            debt_stock=200.0, periods=60,
        )
        p_hh = HolderParams(
            shares=HolderShares(household=0.80, asset=0.20, foreign=0.0, central_bank=0.0),
            debt_stock=200.0, periods=60,
        )
        r_asset = run_holder_model(p_asset)
        r_hh = run_holder_model(p_hh)

        late_conc_asset = r_asset["wealth_concentration"][-1]
        late_conc_hh = r_hh["wealth_concentration"][-1]
        assert late_conc_asset > late_conc_hh, (
            f"Asset-held concentration {late_conc_asset:.3f} should exceed "
            f"HH-held {late_conc_hh:.3f}"
        )

    def test_wealth_concentration_in_unit_range(self):
        """Concentration index stays in [0, 1]."""
        r = run_holder_model()
        for c in r["wealth_concentration"]:
            assert 0.0 <= c <= 1.0


# ===================================================================
# Boundary / adversarial
# ===================================================================

class TestBoundaryAndAdversarial:

    def test_zero_debt_no_holder_effect(self):
        """With no debt stock, holder composition doesn't matter."""
        p_hh = HolderParams(
            shares=HolderShares(household=1.0, asset=0.0, foreign=0.0, central_bank=0.0),
            debt_stock=0.0, periods=20,
        )
        p_asset = HolderParams(
            shares=HolderShares(household=0.0, asset=1.0, foreign=0.0, central_bank=0.0),
            debt_stock=0.0, periods=20,
        )
        r_hh = run_holder_model(p_hh)
        r_asset = run_holder_model(p_asset)
        for t in range(20):
            assert r_hh["output"][t] == pytest.approx(r_asset["output"][t], abs=0.1)

    def test_central_bank_full_holdings_zero_net_cost(self):
        """If the central bank holds 100% of debt, net interest cost is ~zero."""
        p = HolderParams(
            shares=HolderShares(household=0.0, asset=0.0, foreign=0.0, central_bank=1.0),
            periods=20,
        )
        r = run_holder_model(p)
        for cost in r["net_interest_cost"]:
            assert cost == pytest.approx(0.0, abs=0.001)

    def test_small_holder_changes_small_output_differences(self):
        """Tiny changes in holder mix produce tiny outcome changes."""
        p1 = HolderParams(
            shares=HolderShares(household=0.50, asset=0.50, foreign=0.0, central_bank=0.0),
            periods=30,
        )
        p2 = HolderParams(
            shares=HolderShares(household=0.51, asset=0.49, foreign=0.0, central_bank=0.0),
            periods=30,
        )
        r1 = run_holder_model(p1)
        r2 = run_holder_model(p2)

        gap = abs(np.mean(r1["output"][5:25]) - np.mean(r2["output"][5:25]))
        baseline = np.mean(r1["output"][5:25])
        assert gap / max(baseline, 1.0) < 0.05, (
            "Tiny holder differences should produce tiny output differences"
        )

    def test_does_not_overclaim_political_economy(self):
        """The model is stylized: it produces directional differences but
        the absolute magnitudes should not be treated as empirical
        calibration. This test just checks the model runs and reports
        reasonable bounded quantities."""
        r = run_holder_model()
        assert all(np.isfinite(y) for y in r["output"])
        assert all(np.isfinite(c) for c in r["wealth_concentration"])
