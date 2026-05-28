"""Tests for the external-constraint model — written test-first.

Shows that even a sovereign issuer can face real limits from external
dependence: import-essential needs, FX stress, and the gap between
domestic monetary space and external purchasing power.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.external_constraint import (
    ExternalParams,
    run_external_model,
)


# ===================================================================
# Structural tests
# ===================================================================

class TestStructure:

    def test_returns_expected_keys(self):
        r = run_external_model()
        for key in ("output", "inflation", "import_bill", "export_earnings",
                     "external_gap", "fx_stress", "imported_inflation"):
            assert key in r, f"Missing key: {key}"

    def test_all_arrays_same_length(self):
        p = ExternalParams(periods=40)
        r = run_external_model(p)
        lengths = {k: len(v) for k, v in r.items() if isinstance(v, list)}
        assert len(set(lengths.values())) == 1
        assert list(lengths.values())[0] == 40

    def test_output_positive(self):
        r = run_external_model()
        assert all(y > 0 for y in r["output"])


# ===================================================================
# Low dependence — domestic monetary space works
# ===================================================================

class TestLowDependence:
    """With low import dependence, a sovereign issuer can spend freely."""

    def test_low_import_share_no_fx_stress(self):
        """Low import dependence + balanced trade → no FX stress."""
        p = ExternalParams(
            import_share=0.05, export_earnings=20.0,
            base_G=30.0, periods=40,
        )
        r = run_external_model(p)
        assert all(s < 0.01 for s in r["fx_stress"]), (
            "Low-import economy should have near-zero FX stress"
        )

    def test_low_dependence_no_imported_inflation(self):
        p = ExternalParams(
            import_share=0.05, export_earnings=20.0,
            base_G=30.0, periods=40,
        )
        r = run_external_model(p)
        assert all(inf < 0.01 for inf in r["imported_inflation"])

    def test_extra_spending_raises_output_under_low_dependence(self):
        """With low import dependence, fiscal expansion works as expected."""
        p_low_g = ExternalParams(
            import_share=0.05, export_earnings=20.0,
            base_G=20.0, periods=30,
        )
        p_high_g = ExternalParams(
            import_share=0.05, export_earnings=20.0,
            base_G=40.0, periods=30,
        )
        r_low = run_external_model(p_low_g)
        r_high = run_external_model(p_high_g)
        assert np.mean(r_high["output"][10:25]) > np.mean(r_low["output"][10:25])


# ===================================================================
# High dependence — external constraint binds
# ===================================================================

class TestHighDependence:
    """With high import dependence, domestic slack can remain but
    external pressure creates inflation and limits real output gains."""

    def test_high_import_share_creates_fx_stress(self):
        """High import dependence + deficit trade → FX stress."""
        p = ExternalParams(
            import_share=0.40, export_earnings=15.0,
            base_G=40.0, periods=40,
        )
        r = run_external_model(p)
        late_stress = np.mean(r["fx_stress"][20:35])
        assert late_stress > 0.01, (
            f"High-import economy should have FX stress, got {late_stress:.4f}"
        )

    def test_high_dependence_creates_imported_inflation(self):
        p = ExternalParams(
            import_share=0.40, export_earnings=15.0,
            base_G=40.0, periods=40,
        )
        r = run_external_model(p)
        late_inf = np.mean(r["imported_inflation"][20:35])
        assert late_inf > 0.01, (
            f"High-import economy should see imported inflation, got {late_inf:.4f}"
        )

    def test_spending_less_effective_under_high_dependence(self):
        """Fiscal multiplier is weaker when imports leak demand abroad."""
        dG = 20.0
        # Low dependence
        r_low_base = run_external_model(ExternalParams(
            import_share=0.05, export_earnings=20.0, base_G=20.0, periods=30,
        ))
        r_low_high = run_external_model(ExternalParams(
            import_share=0.05, export_earnings=20.0, base_G=40.0, periods=30,
        ))
        mult_low = (np.mean(r_low_high["output"][10:25]) -
                    np.mean(r_low_base["output"][10:25])) / dG

        # High dependence
        r_high_base = run_external_model(ExternalParams(
            import_share=0.40, export_earnings=15.0, base_G=20.0, periods=30,
        ))
        r_high_high = run_external_model(ExternalParams(
            import_share=0.40, export_earnings=15.0, base_G=40.0, periods=30,
        ))
        mult_high = (np.mean(r_high_high["output"][10:25]) -
                     np.mean(r_high_base["output"][10:25])) / dG

        assert mult_low > mult_high, (
            f"Low-dep multiplier {mult_low:.2f} should exceed "
            f"high-dep multiplier {mult_high:.2f}"
        )


# ===================================================================
# Boundary and adversarial
# ===================================================================

class TestBoundaryAndAdversarial:

    def test_zero_imports_no_external_pressure(self):
        """With zero imports, external constraint never binds."""
        p = ExternalParams(import_share=0.0, base_G=50.0, periods=30)
        r = run_external_model(p)
        assert all(s == pytest.approx(0.0, abs=0.001) for s in r["fx_stress"])

    def test_high_exports_offset_imports(self):
        """Large export earnings can offset import bill, reducing stress."""
        p = ExternalParams(
            import_share=0.30, export_earnings=60.0,
            base_G=30.0, periods=30,
        )
        r = run_external_model(p)
        # With exports >> imports, stress should be low
        assert all(s < 0.05 for s in r["fx_stress"])

    def test_model_complements_not_negates_thesis(self):
        """Under low dependence, extra spending is effective — the model
        shows external limits as a complement to, not a negation of,
        the domestic-monetary-space argument."""
        p = ExternalParams(
            import_share=0.05, export_earnings=20.0,
            base_G=40.0, capacity=200.0, periods=30,
        )
        r = run_external_model(p)
        # Should be feasible: low inflation, positive output
        assert np.mean(r["inflation"][10:25]) < 0.05
        assert np.mean(r["output"][10:25]) > 100
