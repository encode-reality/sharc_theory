"""Tests for the real-capacity constraint model — written test-first.

The model shows what genuinely constrains government spending: not
financial bookkeeping but real productive capacity.  Under slack, extra
spending creates real output.  At capacity, extra spending creates
inflation, not output.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.capacity_constraint import (
    CapacityParams,
    run_capacity_model,
)


# ===================================================================
# Structural tests
# ===================================================================

class TestStructure:
    """Model produces valid, well-formed output."""

    def test_returns_expected_keys(self):
        r = run_capacity_model()
        assert "output" in r
        assert "inflation" in r
        assert "capacity" in r
        assert "demand" in r
        assert "utilization" in r

    def test_all_arrays_same_length(self):
        p = CapacityParams(periods=40)
        r = run_capacity_model(p)
        lengths = {k: len(v) for k, v in r.items() if isinstance(v, list)}
        assert len(set(lengths.values())) == 1
        assert list(lengths.values())[0] == 40

    def test_output_positive(self):
        r = run_capacity_model()
        assert all(y > 0 for y in r["output"])

    def test_capacity_grows(self):
        """Capacity should grow over time due to productivity growth."""
        p = CapacityParams(periods=50, productivity_growth=0.01)
        r = run_capacity_model(p)
        assert r["capacity"][-1] > r["capacity"][0]


# ===================================================================
# Slack conditions — spending creates output
# ===================================================================

class TestSlackConditions:
    """Under slack (demand < capacity), extra G creates real output."""

    def test_extra_spending_raises_output_under_slack(self):
        """When the economy has slack, higher G increases output."""
        p = CapacityParams(
            capacity=200.0,       # large capacity
            base_private_demand=60.0,
            base_G=20.0,          # total demand well below capacity
            periods=30,
        )
        r_low = run_capacity_model(p)
        r_high = run_capacity_model(CapacityParams(
            capacity=200.0, base_private_demand=60.0, base_G=40.0, periods=30,
        ))

        y_low = np.mean(r_low["output"][10:25])
        y_high = np.mean(r_high["output"][10:25])
        assert y_high > y_low, "Higher G should increase output under slack"

    def test_no_inflation_under_slack(self):
        """When demand is well below capacity, inflation should be zero."""
        p = CapacityParams(
            capacity=200.0,
            base_private_demand=60.0,
            base_G=20.0,
            periods=30,
        )
        r = run_capacity_model(p)
        assert all(inf == pytest.approx(0.0, abs=0.001) for inf in r["inflation"])

    def test_utilization_below_one(self):
        """Under slack, utilization < 1.0."""
        p = CapacityParams(
            capacity=200.0, base_private_demand=60.0, base_G=20.0, periods=30,
        )
        r = run_capacity_model(p)
        assert all(u < 1.0 for u in r["utilization"])


# ===================================================================
# Tight conditions — spending creates inflation
# ===================================================================

class TestTightConditions:
    """At capacity (demand >= capacity), extra G creates inflation."""

    def test_extra_spending_creates_inflation_at_capacity(self):
        """When demand exceeds capacity, inflation should be positive."""
        p = CapacityParams(
            capacity=100.0,
            base_private_demand=60.0,
            base_G=60.0,  # total demand > capacity
            periods=30,
        )
        r = run_capacity_model(p)
        late_inflation = np.mean(r["inflation"][10:25])
        assert late_inflation > 0.01, (
            f"Inflation {late_inflation:.4f} should be positive at capacity"
        )

    def test_output_capped_near_capacity(self):
        """When demand far exceeds capacity, output is bounded near capacity."""
        p = CapacityParams(
            capacity=100.0,
            base_private_demand=60.0,
            base_G=80.0,  # way over capacity
            periods=30,
        )
        r = run_capacity_model(p)
        for t in range(10, 30):
            # Output should be no more than ~20% above capacity
            assert r["output"][t] <= r["capacity"][t] * 1.20, (
                f"Output {r['output'][t]:.1f} too far above "
                f"capacity {r['capacity'][t]:.1f}"
            )

    def test_utilization_above_one(self):
        """When demand exceeds capacity, utilization > 1.0."""
        p = CapacityParams(
            capacity=100.0, base_private_demand=60.0, base_G=60.0, periods=30,
        )
        r = run_capacity_model(p)
        assert any(u > 1.0 for u in r["utilization"])


# ===================================================================
# Boundary — transition from slack to tight
# ===================================================================

class TestBoundary:
    """The transition between slack and tight is smooth and interpretable."""

    def test_spending_ramp_transitions_smoothly(self):
        """Gradually increasing G transitions from slack to inflation."""
        p = CapacityParams(capacity=100.0, base_private_demand=50.0, periods=60)
        # Ramp G from 20 to 80 over 60 periods
        spending_path = {t: 20.0 + t for t in range(60)}
        r = run_capacity_model(p, spending_path=spending_path)

        # Early periods: slack, low inflation
        early_inf = np.mean(r["inflation"][:15])
        # Late periods: tight, higher inflation
        late_inf = np.mean(r["inflation"][45:60])
        assert late_inf > early_inf, (
            "Inflation should rise as spending ramp exceeds capacity"
        )

    def test_multiplier_effective_under_slack_only(self):
        """The fiscal multiplier should be larger under slack than at capacity."""
        p_slack = CapacityParams(
            capacity=200.0, base_private_demand=60.0, periods=30,
        )
        p_tight = CapacityParams(
            capacity=100.0, base_private_demand=60.0, periods=30,
        )
        dG = 10.0
        # Slack: compare G=20 vs G=30
        r_low = run_capacity_model(CapacityParams(**{**p_slack.__dict__, "base_G": 20.0}))
        r_high = run_capacity_model(CapacityParams(**{**p_slack.__dict__, "base_G": 30.0}))
        mult_slack = (np.mean(r_high["output"][10:25]) - np.mean(r_low["output"][10:25])) / dG

        # Tight: compare G=50 vs G=60 (both near or above capacity)
        r_low_t = run_capacity_model(CapacityParams(**{**p_tight.__dict__, "base_G": 50.0}))
        r_high_t = run_capacity_model(CapacityParams(**{**p_tight.__dict__, "base_G": 60.0}))
        mult_tight = (np.mean(r_high_t["output"][10:25]) - np.mean(r_low_t["output"][10:25])) / dG

        assert mult_slack > mult_tight, (
            f"Slack multiplier {mult_slack:.2f} should exceed "
            f"tight multiplier {mult_tight:.2f}"
        )


# ===================================================================
# Adversarial tests
# ===================================================================

class TestAdversarial:
    """Edge cases and conditions where the story weakens."""

    def test_productivity_growth_shifts_boundary(self):
        """With faster productivity growth, the capacity constraint
        relaxes — spending that was inflationary becomes feasible."""
        p_slow = CapacityParams(
            capacity=100.0, base_private_demand=60.0, base_G=50.0,
            productivity_growth=0.001, periods=50,
        )
        p_fast = CapacityParams(
            capacity=100.0, base_private_demand=60.0, base_G=50.0,
            productivity_growth=0.02, periods=50,
        )
        r_slow = run_capacity_model(p_slow)
        r_fast = run_capacity_model(p_fast)

        late_inf_slow = np.mean(r_slow["inflation"][30:45])
        late_inf_fast = np.mean(r_fast["inflation"][30:45])
        assert late_inf_fast < late_inf_slow, (
            "Faster productivity growth should reduce inflation"
        )

    def test_zero_G_no_inflation(self):
        """With no government spending and slack, no inflation."""
        p = CapacityParams(
            capacity=150.0, base_private_demand=60.0, base_G=0.0, periods=30,
        )
        r = run_capacity_model(p)
        assert all(inf == pytest.approx(0.0, abs=0.001) for inf in r["inflation"])

    def test_model_does_not_claim_unlimited_spending(self):
        """Even with very high capacity, inflation eventually appears
        if G is absurdly large — the model does not claim spending is free."""
        p = CapacityParams(
            capacity=1000.0,  # very large capacity
            base_private_demand=60.0,
            base_G=1200.0,  # absurdly large G (exceeds capacity)
            periods=30,
        )
        r = run_capacity_model(p)
        assert any(inf > 0 for inf in r["inflation"]), (
            "Even with large capacity, absurd spending should create inflation"
        )
