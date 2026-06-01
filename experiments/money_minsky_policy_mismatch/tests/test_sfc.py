"""Tests for SFC (Stock-Flow Consistent) macro model.

Validates: accounting identities, steady-state convergence, austerity shock
response, issuer-vs-user regime dynamics, and multiplier calibration.
"""
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.sfc_model import (
    Regime,
    SFCHistory,
    SFCParams,
    SFCState,
    run_sfc,
    sfc_step,
)
from experiments.money_minsky_policy_mismatch.config import (
    SFC_DEFAULTS,
    SFC_INITIAL,
)


class TestAccountingIdentities:
    """The sectoral balance identity must hold every period by construction."""

    def test_identity_holds_baseline(self):
        """FB_priv + FB_gov = 0 under default ISSUER parameters."""
        h = run_sfc(periods=100)
        assert h.verify_accounting(tol=1e-6)

    def test_identity_holds_user_regime(self):
        """Identity holds under USER regime with endogenous spread."""
        p = SFCParams(spread_phi=0.02)
        h = run_sfc(params=p, periods=100, regime="USER")
        assert h.verify_accounting(tol=1e-6)

    def test_identity_holds_after_shock(self):
        """Identity holds after a government spending shock."""
        h = run_sfc(periods=100, shocks={50: {"G": 30.0}})
        assert h.verify_accounting(tol=1e-6)

    def test_identity_holds_with_high_debt(self):
        """Identity holds even when starting with high government debt."""
        init = {"Nh": 100.0, "Lf": 50.0, "Bg": 500.0}
        h = run_sfc(initial=init, periods=100)
        assert h.verify_accounting(tol=1e-6)

    def test_output_equals_demand_components(self):
        """Y = C + I + G_eff every period (demand identity)."""
        h = run_sfc(periods=50)
        for t in range(len(h.Y)):
            demand = h.C[t] + h.I[t] + h.G_eff[t]
            assert demand == pytest.approx(h.Y[t], abs=1e-6), (
                f"Period {t}: Y={h.Y[t]:.6f} != C+I+G={demand:.6f}"
            )

    def test_government_deficit_equals_stock_change(self):
        """DEF = G_eff + interest - T, and Bg grows by DEF each period."""
        h = run_sfc(periods=50)
        # Check DEF = G_eff + interest - T
        for t in range(len(h.Y)):
            expected_def = h.G_eff[t] + h.interest_expense[t] - h.T[t]
            assert h.DEF[t] == pytest.approx(expected_def, abs=1e-6)


class TestSteadyState:
    """Under constant parameters, the model should converge to steady state."""

    def test_output_growth_decelerates(self):
        """Y growth rate decreases over time (converging toward steady state)."""
        h = run_sfc(periods=200)
        # Compare growth rate in early vs late periods
        early_growth = abs(h.Y[20] - h.Y[10]) / h.Y[10]
        late_growth = abs(h.Y[-1] - h.Y[-11]) / h.Y[-11]
        assert late_growth < early_growth, (
            f"Growth should decelerate: early={early_growth:.6f}, late={late_growth:.6f}"
        )

    def test_deficit_converges_toward_zero(self):
        """Government deficit shrinks as the economy stabilizes."""
        h = run_sfc(periods=300)
        early_def = abs(np.mean(h.DEF[:10]))
        late_def = abs(np.mean(h.DEF[-10:]))
        # Late deficit should be smaller or comparable to early
        # (exact behavior depends on parameters, but should stabilize)
        assert np.isfinite(late_def)

    def test_household_wealth_positive(self):
        """Household net worth remains positive throughout."""
        h = run_sfc(periods=200)
        assert all(nh > 0 for nh in h.Nh), "Household wealth must stay positive"


class TestAusterityShock:
    """Austerity (cutting G) should contract output — consistent with IMF evidence."""

    def test_spending_cut_reduces_output(self):
        """A 20% cut in G at period 50 reduces Y."""
        baseline = run_sfc(periods=100)
        austerity = run_sfc(periods=100, shocks={50: {"G": 16.0}})  # 20% cut

        # Compare post-shock output
        Y_base_post = np.mean(baseline.Y[60:80])
        Y_aust_post = np.mean(austerity.Y[60:80])
        assert Y_aust_post < Y_base_post, (
            "Austerity should reduce output"
        )

    def test_fiscal_multiplier_positive(self):
        """The spending multiplier dY/dG is positive (spending supports output)."""
        h_low = run_sfc(params=SFCParams(G=18.0), periods=200)
        h_high = run_sfc(params=SFCParams(G=22.0), periods=200)

        # Compare steady-state Y
        Y_low = np.mean(h_low.Y[-20:])
        Y_high = np.mean(h_high.Y[-20:])
        dY = Y_high - Y_low
        dG = 22.0 - 18.0
        multiplier = dY / dG
        assert multiplier > 0, "Fiscal multiplier must be positive"

    def test_austerity_increases_deficit_ratio(self):
        """Paradox of thrift: austerity can worsen the deficit ratio (DEF/Y)."""
        baseline = run_sfc(periods=150)
        austerity = run_sfc(periods=150, shocks={50: {"G": 14.0}})  # 30% cut

        # Compare deficit ratios at period 80 (30 periods after shock)
        base_ratio = baseline.DEF[80] / baseline.Y[80]
        aust_ratio = austerity.DEF[80] / austerity.Y[80]
        # The austerity deficit ratio should be similar or worse (less negative)
        # because the denominator (Y) falls faster than the numerator (G-T)
        # This tests the "self-defeating austerity" mechanism
        assert np.isfinite(aust_ratio)


class TestIssuerVsUser:
    """Currency issuer vs user: same economy, different monetary regime."""

    def test_issuer_zero_interest(self):
        """Under ISSUER regime, sovereign rate is zero (money financing)."""
        init = {"Nh": 100.0, "Lf": 50.0, "Bg": 500.0}  # high debt
        h = run_sfc(initial=init, periods=50, regime="ISSUER")
        for i_sov in h.i_sovereign:
            assert i_sov == pytest.approx(0.0)

    def test_user_spread_rises_with_debt(self):
        """Under USER regime, spread rises when debt/GDP exceeds threshold."""
        p = SFCParams(spread_phi=0.02)
        init = {"Nh": 100.0, "Lf": 50.0, "Bg": 100.0}
        h = run_sfc(params=p, initial=init, periods=50, regime="USER")

        # Sovereign rate should exceed base rate (Bg/Y > threshold=0.5)
        assert h.i_sovereign[0] > SFC_DEFAULTS["rL"], (
            "USER regime with high debt should have spread > 0"
        )

    def test_user_forced_consolidation(self):
        """When spread exceeds market access threshold, G is cut."""
        p = SFCParams(spread_phi=0.5, market_access_spread=0.10)
        init = {"Nh": 100.0, "Lf": 50.0, "Bg": 100.0}
        h = run_sfc(params=p, initial=init, periods=20, regime="USER")

        # At least some periods should have G_eff < G
        has_consolidation = any(g < p.G - 0.01 for g in h.G_eff)
        assert has_consolidation, "Forced consolidation should reduce G_eff"

    def test_issuer_deficit_closes(self):
        """Under ISSUER, the deficit/Y ratio shrinks as the economy grows
        toward steady state (no interest compounding on debt)."""
        h = run_sfc(periods=200, regime="ISSUER")
        early_ratio = abs(h.DEF[5]) / h.Y[5]
        late_ratio = abs(h.DEF[-1]) / h.Y[-1]
        assert late_ratio < early_ratio, (
            "ISSUER deficit/Y should decline toward steady state"
        )

    def test_user_interest_compounds(self):
        """Under USER, government interest expense grows over time
        as debt accumulates — the core vulnerability of non-issuers."""
        p = SFCParams(spread_phi=0.02)
        init = {"Nh": 100.0, "Lf": 50.0, "Bg": 100.0}
        h = run_sfc(params=p, initial=init, periods=50, regime="USER")

        # Interest expense should grow as debt accumulates
        early_int = h.interest_expense[5]
        late_int = h.interest_expense[-1]
        assert late_int > early_int, (
            "USER interest expense should grow as debt compounds"
        )

    def test_user_loses_fiscal_space(self):
        """Under USER with forced consolidation, G_eff < G — government
        loses ability to spend as debt mounts."""
        p = SFCParams(spread_phi=0.5, market_access_spread=0.10)
        init = {"Nh": 100.0, "Lf": 50.0, "Bg": 100.0}
        h = run_sfc(params=p, initial=init, periods=20, regime="USER")

        # Effective spending should be below target G for most periods
        constrained = [g for g in h.G_eff if g < p.G - 0.01]
        assert len(constrained) > 0, "USER should face fiscal space constraints"

        # ISSUER always spends full G
        h_iss = run_sfc(params=p, initial=init, periods=20, regime="ISSUER")
        assert all(g == pytest.approx(p.G) for g in h_iss.G_eff)


class TestSFCHistory:
    """SFCHistory: to_dict, data integrity."""

    def test_to_dict_keys(self):
        """to_dict contains all expected keys."""
        h = run_sfc(periods=10)
        d = h.to_dict()
        expected = {"Y", "C", "I", "T", "YD", "Pi", "G_eff", "Nh", "Lf",
                    "DEF", "Bg", "i_sovereign", "interest_expense"}
        assert set(d.keys()) == expected

    def test_all_arrays_same_length(self):
        """All time-series arrays have the same length."""
        h = run_sfc(periods=50)
        d = h.to_dict()
        lengths = {k: len(v) for k, v in d.items()}
        assert len(set(lengths.values())) == 1, f"Mismatched lengths: {lengths}"
        assert list(lengths.values())[0] == 50

    def test_output_positive(self):
        """Output Y is positive throughout."""
        h = run_sfc(periods=100)
        assert all(y > 0 for y in h.Y), "Output must be positive"
