"""Tests for the sovereign-securities and rollover model — written test-first.

The model shows how maturity structure and refinancing pressure change
fiscal dynamics even when the headline debt/GDP ratio is the same.
Short-maturity debt creates rollover risk that long-maturity debt does not.

Key distinction: debt stock vs refinancing flow.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.sovereign_securities import (
    RolloverParams,
    run_rollover_model,
)


# ===================================================================
# Structural tests
# ===================================================================

class TestStructure:
    """Model produces valid, well-formed output."""

    def test_returns_expected_keys(self):
        r = run_rollover_model()
        for key in ("output", "debt_total", "debt_short", "debt_long",
                     "rollover_need", "effective_rate", "interest_expense",
                     "inflation", "spending"):
            assert key in r, f"Missing key: {key}"

    def test_all_arrays_same_length(self):
        p = RolloverParams(periods=40)
        r = run_rollover_model(p)
        lengths = {k: len(v) for k, v in r.items() if isinstance(v, list)}
        assert len(set(lengths.values())) == 1
        assert list(lengths.values())[0] == 40

    def test_debt_stock_equals_short_plus_long(self):
        """Total debt = short + long at every period."""
        r = run_rollover_model()
        for t in range(len(r["debt_total"])):
            total = r["debt_short"][t] + r["debt_long"][t]
            assert total == pytest.approx(r["debt_total"][t], abs=0.1), (
                f"Period {t}: short+long={total:.2f} != total={r['debt_total'][t]:.2f}"
            )


# ===================================================================
# Maturity structure matters
# ===================================================================

class TestMaturityStructure:
    """Same debt/GDP, different maturity → different dynamics."""

    def test_short_maturity_higher_rollover(self):
        """Short-weighted debt creates larger rollover needs."""
        p_short = RolloverParams(short_share=0.80, periods=50)
        p_long = RolloverParams(short_share=0.20, periods=50)

        r_short = run_rollover_model(p_short)
        r_long = run_rollover_model(p_long)

        avg_roll_short = np.mean(r_short["rollover_need"][10:40])
        avg_roll_long = np.mean(r_long["rollover_need"][10:40])
        assert avg_roll_short > avg_roll_long, (
            f"Short-maturity rollover {avg_roll_short:.2f} should exceed "
            f"long-maturity {avg_roll_long:.2f}"
        )

    def test_short_maturity_higher_rate_for_user(self):
        """Currency user with short maturity faces higher effective rate
        because rollover pressure adds to the spread."""
        p_short = RolloverParams(
            regime="USER", short_share=0.80, periods=50,
            rollover_phi=0.10,
        )
        p_long = RolloverParams(
            regime="USER", short_share=0.20, periods=50,
            rollover_phi=0.10,
        )

        r_short = run_rollover_model(p_short)
        r_long = run_rollover_model(p_long)

        avg_rate_short = np.mean(r_short["effective_rate"][20:40])
        avg_rate_long = np.mean(r_long["effective_rate"][20:40])
        assert avg_rate_short > avg_rate_long, (
            f"Short-maturity rate {avg_rate_short:.4f} should exceed "
            f"long-maturity {avg_rate_long:.4f}"
        )

    def test_same_debt_ratio_different_outcomes(self):
        """Two USER economies with the same initial debt/GDP but different
        maturity structures produce different rate paths."""
        common = dict(
            regime="USER", periods=80, initial_debt=60.0, base_G=55.0,
            rollover_phi=0.12, spread_phi=0.08,
        )
        r_short = run_rollover_model(RolloverParams(short_share=0.80, **common))
        r_long = run_rollover_model(RolloverParams(short_share=0.20, **common))

        # Rate paths should diverge (short maturity → higher rollover spread)
        rate_short = np.mean(r_short["effective_rate"][20:50])
        rate_long = np.mean(r_long["effective_rate"][20:50])
        assert rate_short > rate_long, (
            f"Short-maturity rate {rate_short:.4f} should exceed "
            f"long-maturity rate {rate_long:.4f}"
        )


# ===================================================================
# Issuer vs user
# ===================================================================

class TestIssuerVsUser:
    """Sovereign issuer faces no rollover pressure; user does."""

    def test_issuer_rate_independent_of_maturity(self):
        """Issuer sets its own rate — maturity structure doesn't add spread."""
        p_short = RolloverParams(regime="ISSUER", short_share=0.80, periods=40)
        p_long = RolloverParams(regime="ISSUER", short_share=0.20, periods=40)

        r_short = run_rollover_model(p_short)
        r_long = run_rollover_model(p_long)

        for t in range(len(r_short["effective_rate"])):
            assert r_short["effective_rate"][t] == pytest.approx(
                r_long["effective_rate"][t], abs=0.001
            )

    def test_issuer_no_forced_consolidation(self):
        """Issuer never faces forced consolidation regardless of rollover."""
        p = RolloverParams(
            regime="ISSUER", short_share=0.90,
            initial_debt=80.0, periods=50,
        )
        r = run_rollover_model(p)
        target = p.base_G
        for t in range(len(r["spending"])):
            assert r["spending"][t] == pytest.approx(target, abs=0.1), (
                f"Issuer spending should stay at target, got {r['spending'][t]:.2f}"
            )

    def test_user_may_face_consolidation(self):
        """User with high rollover pressure may face forced spending cuts."""
        p = RolloverParams(
            regime="USER", short_share=0.90,
            initial_debt=80.0, base_G=35.0, periods=80,
            rollover_phi=0.15, spread_phi=0.12,
            market_access_spread=0.06,
        )
        r = run_rollover_model(p)
        target = p.base_G
        has_cut = any(s < target - 0.1 for s in r["spending"])
        assert has_cut, "User with high rollover should face consolidation"


# ===================================================================
# Boundary / adversarial tests
# ===================================================================

class TestBoundaryAndAdversarial:
    """Edge cases and conditions where the story weakens."""

    def test_zero_debt_no_rollover(self):
        """With no initial debt, rollover need is just the primary deficit."""
        p = RolloverParams(initial_debt=0.0, periods=20)
        r = run_rollover_model(p)
        # First period: rollover_need should just be the deficit (spending - revenue)
        assert r["rollover_need"][0] >= 0

    def test_all_long_maturity_minimal_rollover(self):
        """100% long-maturity debt has near-zero rollover in early periods."""
        p = RolloverParams(short_share=0.0, long_maturity=20, periods=15)
        r = run_rollover_model(p)
        # In early periods (before any long debt matures), rollover is just deficit
        early_rollover = r["rollover_need"][1]
        assert early_rollover < p.base_G * 2, (
            "All-long debt should have minimal rollover early on"
        )

    def test_user_with_no_spread_matches_issuer(self):
        """USER with spread_phi=0 and rollover_phi=0 behaves like ISSUER
        (same base rate, no market pressure)."""
        p_user = RolloverParams(
            regime="USER", spread_phi=0.0, rollover_phi=0.0,
            r_base=0.02, periods=30,
        )
        p_issuer = RolloverParams(
            regime="ISSUER", r_policy=0.02, periods=30,
        )
        r_user = run_rollover_model(p_user)
        r_issuer = run_rollover_model(p_issuer)

        for t in range(len(r_user["spending"])):
            assert r_user["spending"][t] == pytest.approx(
                r_issuer["spending"][t], rel=0.02
            )

    def test_issuer_debt_still_accumulates(self):
        """Even issuers accumulate debt when running a deficit — the
        model does not claim debt is irrelevant, only that refinancing
        pressure differs."""
        p = RolloverParams(regime="ISSUER", periods=60)
        r = run_rollover_model(p)
        assert r["debt_total"][-1] > r["debt_total"][5], (
            "Issuer running a deficit should see debt grow"
        )

    def test_no_explosive_output(self):
        """No configuration should produce explosive output growth."""
        for regime in ("ISSUER", "USER"):
            p = RolloverParams(regime=regime, periods=80)
            r = run_rollover_model(p)
            ratio = max(r["output"]) / max(r["output"][0], 1.0)
            assert ratio < 10.0, (
                f"{regime} output ratio {ratio:.1f}x looks explosive"
            )
