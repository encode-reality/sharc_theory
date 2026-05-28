"""Tests for the fragility-regime comparison wrapper."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.fragility_regimes import (
    run_fragility_regime_experiment,
)


class TestFragilityRegimes:
    """Rate hikes should be more survivable in the resilient calibration."""

    def test_returns_expected_top_level_keys(self):
        result = run_fragility_regime_experiment()
        assert set(result.keys()) == {
            "delta_r",
            "initial_d",
            "threshold",
            "fragile",
            "resilient",
        }

    def test_resilient_calibration_has_more_safe_cells(self):
        result = run_fragility_regime_experiment()
        assert result["resilient"]["safe_share"] > result["fragile"]["safe_share"]

    def test_peak_debt_grid_matches_grid_shape(self):
        result = run_fragility_regime_experiment()
        fragile_grid = np.array(result["fragile"]["grid"])
        fragile_peak = np.array(result["fragile"]["peak_debt"])
        assert fragile_grid.shape == fragile_peak.shape
