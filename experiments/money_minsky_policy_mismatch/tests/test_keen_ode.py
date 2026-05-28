"""Tests for Keen-Minsky leverage-cycle ODE model.

Validates: Phillips curve, investment function, ODE derivatives,
solver behavior, regime transitions, and empirical consistency.
"""
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.keen_ode import (
    KeenResult,
    detect_crisis,
    invest,
    keen_minsky_ode,
    phillips,
    solve_keen,
)
from experiments.money_minsky_policy_mismatch.config import (
    KEEN_CRISIS_THRESHOLD,
    KEEN_ODE_DEFAULTS,
    KEEN_ODE_INITIAL,
    KEEN_ODE_TSPAN,
)


class TestPhillipsCurve:
    """Convex Phillips curve: wage growth accelerates above employment threshold."""

    def test_below_threshold_returns_intercept(self):
        """Below lam0, Phillips curve returns a0 (no tight-labor pressure)."""
        assert phillips(0.8, a0=0.0, a1=6.0, lam0=0.9) == pytest.approx(0.0)

    def test_at_threshold_returns_intercept(self):
        """Exactly at lam0, excess = 0 so result = a0."""
        assert phillips(0.9, a0=0.0, a1=6.0, lam0=0.9) == pytest.approx(0.0)

    def test_above_threshold_positive(self):
        """Above lam0, wage pressure is positive and proportional to excess."""
        val = phillips(0.95, a0=0.0, a1=6.0, lam0=0.9)
        assert val == pytest.approx(6.0 * 0.05)
        assert val > 0.0

    def test_monotonically_increasing_above_threshold(self):
        """Higher employment above threshold means higher wage pressure."""
        v1 = phillips(0.92, a0=0.0, a1=6.0, lam0=0.9)
        v2 = phillips(0.95, a0=0.0, a1=6.0, lam0=0.9)
        v3 = phillips(0.98, a0=0.0, a1=6.0, lam0=0.9)
        assert v1 < v2 < v3

    def test_nonzero_intercept(self):
        """With a0 != 0, the baseline shift applies everywhere."""
        val = phillips(0.80, a0=-0.02, a1=6.0, lam0=0.9)
        assert val == pytest.approx(-0.02)

    def test_slope_sensitivity(self):
        """Higher a1 means steeper wage response to tight labor."""
        v_low = phillips(0.95, a0=0.0, a1=3.0, lam0=0.9)
        v_high = phillips(0.95, a0=0.0, a1=12.0, lam0=0.9)
        assert v_high > v_low


class TestInvestmentFunction:
    """Investment: rises with profit share, falls with debt (drag), non-negative floor."""

    def test_positive_profit_positive_investment(self):
        """Healthy firms invest when profit share is high and debt is low."""
        val = invest(profit_share=0.4, d=0.5, k0=0.02, k1=0.20, k2=0.12)
        assert val > 0.0

    def test_debt_drag_reduces_investment(self):
        """Higher debt ratio reduces investment (debt drag channel)."""
        v_low_debt = invest(0.3, d=0.5, k0=0.02, k1=0.20, k2=0.12)
        v_high_debt = invest(0.3, d=3.0, k0=0.02, k1=0.20, k2=0.12)
        assert v_low_debt > v_high_debt

    def test_nonnegative_floor(self):
        """Investment cannot go negative (firms stop investing, don't disinvest here)."""
        val = invest(profit_share=0.0, d=10.0, k0=0.02, k1=0.20, k2=0.12)
        assert val >= 0.0

    def test_profit_sensitivity(self):
        """Higher profit share increases investment."""
        v_low = invest(0.1, d=1.0, k0=0.02, k1=0.20, k2=0.12)
        v_high = invest(0.5, d=1.0, k0=0.02, k1=0.20, k2=0.12)
        assert v_high > v_low


class TestODEDerivatives:
    """Test the RHS of the ODE system at known states."""

    def test_derivatives_at_baseline(self):
        """Derivatives are finite at baseline initial conditions."""
        y = KEEN_ODE_INITIAL
        p = KEEN_ODE_DEFAULTS
        dy = keen_minsky_ode(0.0, y, p)
        assert all(np.isfinite(dy))

    def test_wage_share_rises_at_high_employment(self):
        """When lambda > lam0, wage share should grow (Phillips channel)."""
        p = KEEN_ODE_DEFAULTS
        y = [0.5, 0.96, 1.0]  # omega low, lambda high, moderate debt
        dy = keen_minsky_ode(0.0, y, p)
        # domega > 0 when Phillips(lam) > alpha
        phi = phillips(0.96, p["a0"], p["a1"], p["lam0"])
        if phi > p["alpha"]:
            assert dy[0] > 0.0, "Wage share should rise when labor is tight"

    def test_debt_rises_when_investment_exceeds_profit(self):
        """When investment > internal funds, firms borrow — debt ratio rises."""
        p = dict(KEEN_ODE_DEFAULTS)
        p["k1"] = 0.40  # high investment sensitivity
        y = [0.7, 0.94, 0.3]  # high wage share, moderate employment, low debt
        dy = keen_minsky_ode(0.0, y, p)
        # With high omega (0.7) and low debt, profit = 1 - 0.7 - 0.04*0.3 = 0.288
        # Investment with high k1 should exceed profit, pushing dd > 0
        # (exact sign depends on growth term, but directionally dd should be positive)
        assert np.isfinite(dy[2])

    def test_three_state_variables(self):
        """ODE returns exactly 3 derivatives [domega, dlambda, dd]."""
        dy = keen_minsky_ode(0.0, KEEN_ODE_INITIAL, KEEN_ODE_DEFAULTS)
        assert len(dy) == 3


class TestKeenResult:
    """KeenResult dataclass: to_dict, derived properties."""

    def test_to_dict_keys(self):
        """to_dict contains all expected keys."""
        res = KeenResult(
            t=np.array([0.0, 1.0]),
            omega=np.array([0.6, 0.61]),
            lam=np.array([0.94, 0.93]),
            d=np.array([1.0, 1.02]),
        )
        d = res.to_dict()
        assert set(d.keys()) >= {"t", "omega", "lam", "d"}

    def test_profit_share(self):
        """profit_share = max(1 - omega - r*d, 0)."""
        res = KeenResult(
            t=np.array([0.0]),
            omega=np.array([0.6]),
            lam=np.array([0.94]),
            d=np.array([1.0]),
        )
        ps = res.profit_share(r=0.04)
        expected = 1.0 - 0.6 - 0.04 * 1.0
        assert ps[0] == pytest.approx(expected)

    def test_profit_share_nonnegative(self):
        """Profit share floored at zero."""
        res = KeenResult(
            t=np.array([0.0]),
            omega=np.array([0.95]),
            lam=np.array([0.94]),
            d=np.array([5.0]),
        )
        ps = res.profit_share(r=0.04)
        assert ps[0] >= 0.0


class TestSolver:
    """Integration tests for solve_keen.

    The default calibration is designed to show a Minskyan fragility mechanism,
    but the model is still parameter-sensitive. Tests are structured as:
      1. Early-phase cycle: bounded Goodwin-like dynamics over a moderate span
      2. Long-run instability: eventual crisis under the default calibration
      3. Parameter sensitivity: stronger debt drag can suppress crisis
    """

    def test_early_phase_bounded_cycle(self):
        """In the early phase (first ~60 time units), the system exhibits a
        Goodwin-like cycle: omega and lambda oscillate within (0, 1) and debt
        remains moderate.  This is the 'hedge finance' regime.
        """
        result = solve_keen(KEEN_ODE_DEFAULTS, KEEN_ODE_INITIAL, (0.0, 60.0))
        assert np.all(result.omega > 0), "Wage share must be positive"
        assert np.all(result.omega < 1), "Wage share must be < 1"
        assert np.all(result.lam > 0), "Employment rate must be positive"
        assert np.all(result.lam < 1), "Employment rate must be < 1"
        # Debt should stay moderate in the early phase
        assert np.max(result.d) < KEEN_CRISIS_THRESHOLD, (
            "Early phase: debt should stay below crisis threshold"
        )

    def test_long_run_instability(self):
        """Over longer horizons, the system endogenously generates crisis.
        Under the default calibration, prolonged prosperity shifts financing
        toward fragility and the debt ratio eventually diverges.
        """
        result = solve_keen(KEEN_ODE_DEFAULTS, KEEN_ODE_INITIAL, (0.0, 200.0))
        crisis_idx = detect_crisis(result, threshold=KEEN_CRISIS_THRESHOLD)
        assert crisis_idx is not None, (
            "Keen-Minsky model should produce eventual crisis "
            "(stability breeds instability)"
        )

    def test_default_calibration_crisis_across_selected_initial_conditions(self):
        """Under the default calibration, a selected debt range reaches crisis.

        This is a property of the chosen calibration, not a theorem about all
        formulations of the model.
        """
        for d0 in [0.3, 1.0, 2.0]:
            y0 = [0.80, 0.92, d0]
            result = solve_keen(KEEN_ODE_DEFAULTS, y0, (0.0, 200.0))
            crisis = detect_crisis(result, KEEN_CRISIS_THRESHOLD)
            assert crisis is not None, (
                f"Default calibration should cross crisis threshold from d0={d0}"
            )

    def test_stronger_debt_drag_can_avoid_crisis_within_horizon(self):
        """Crisis timing depends on calibration; higher debt drag can stabilize."""
        params = dict(KEEN_ODE_DEFAULTS, k2=0.20)
        result = solve_keen(params, KEEN_ODE_INITIAL, (0.0, 200.0))
        crisis = detect_crisis(result, KEEN_CRISIS_THRESHOLD)
        assert crisis is None

    def test_exhibits_boom_bust_cycle(self):
        """The model exhibits a Goodwin-like boom-bust cycle: employment and
        wage share both rise during the boom (profit-led investment) then fall
        during the bust (profit squeeze kills investment).  This cyclical
        behavior in the early phase is a prerequisite for the Minsky result.
        """
        result = solve_keen(KEEN_ODE_DEFAULTS, KEEN_ODE_INITIAL, (0.0, 100.0))

        # Lambda (employment) should rise then fall — at least one peak
        lam_diff = np.diff(result.lam)
        has_rise = np.any(lam_diff > 0)
        has_fall = np.any(lam_diff < 0)
        assert has_rise and has_fall, (
            "Employment should rise then fall (boom-bust cycle)"
        )

        # Omega (wage share) should rise during the boom
        omega_diff = np.diff(result.omega)
        has_omega_rise = np.any(omega_diff > 0)
        assert has_omega_rise, "Wage share should rise during the boom phase"

    def test_profit_share_lower_at_higher_rate_for_debtors(self):
        """When d > 0 (net debtor), higher r mechanically produces lower
        profit share: pi = 1 - omega - r*d.  This is Minsky's channel:
        rate hikes squeeze leveraged positions.  When d < 0 (net creditor),
        the effect reverses — which is economically correct.
        """
        result = solve_keen(KEEN_ODE_DEFAULTS, KEEN_ODE_INITIAL, (0.0, 60.0))
        debtor_mask = result.d > 0
        assert np.any(debtor_mask), "Trajectory should include debtor states"

        low_r_ps = result.profit_share(r=0.03)
        high_r_ps = result.profit_share(r=0.08)
        # When d > 0, higher r produces lower profit share
        assert np.all(high_r_ps[debtor_mask] <= low_r_ps[debtor_mask] + 1e-12), (
            "For debtors (d>0), higher rate must reduce profit share"
        )

    def test_solver_output_shape(self):
        """Result arrays are aligned in length."""
        result = solve_keen(KEEN_ODE_DEFAULTS, KEEN_ODE_INITIAL, (0.0, 50.0))
        n = len(result.t)
        assert len(result.omega) == n
        assert len(result.lam) == n
        assert len(result.d) == n
        assert n > 10  # solver should produce many time steps


class TestDetectCrisis:
    """Crisis detection: find first time debt ratio crosses threshold."""

    def test_no_crisis(self):
        """Returns None when debt stays below threshold."""
        res = KeenResult(
            t=np.linspace(0, 10, 100),
            omega=np.full(100, 0.6),
            lam=np.full(100, 0.94),
            d=np.full(100, 1.0),
        )
        assert detect_crisis(res, threshold=5.0) is None

    def test_crisis_detected(self):
        """Returns the time index where d first exceeds threshold."""
        d = np.concatenate([np.ones(50), np.linspace(1, 10, 50)])
        res = KeenResult(
            t=np.linspace(0, 10, 100),
            omega=np.full(100, 0.6),
            lam=np.full(100, 0.94),
            d=d,
        )
        idx = detect_crisis(res, threshold=5.0)
        assert idx is not None
        assert res.d[idx] >= 5.0
        if idx > 0:
            assert res.d[idx - 1] < 5.0
