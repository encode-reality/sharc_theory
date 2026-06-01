"""Tests for the IMF-backed austerity counterfactual module."""

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch import austerity_counterfactual
from experiments.money_minsky_policy_mismatch.austerity_counterfactual import (
    CounterfactualCalibration,
    build_country_episode,
    build_delayed_consolidation_path,
    run_imf_counterfactual_experiment,
    simulate_counterfactual,
)


class TestAusterityCounterfactual:
    """Counterfactuals should be explicit, state-dependent, and reproducible."""

    def test_delayed_path_zeroes_first_two_years(self):
        observed = [1.655, 1.542, 3.167, 3.001, 1.666]
        delayed = build_delayed_consolidation_path(observed)
        assert delayed[:2] == [0.0, 0.0]
        assert delayed[-1] == observed[-1] * 0.7

    def test_simulation_returns_expected_series(self):
        calibration = CounterfactualCalibration()
        case = austerity_counterfactual.DEFAULT_COUNTERFACTUAL_CASES["ESP"]
        result = simulate_counterfactual(
            actions=[1.0, 1.0, 2.0, 2.0, 1.0],
            initial_debt_ratio=50.0,
            initial_unemployment=20.0,
            calibration=calibration,
            case_params=case,
        )
        assert len(result["gdp_index"]) == 5
        assert len(result["debt_ratio"]) == 5
        assert result["gdp_index"][-1] < 100.0

    def test_run_experiment_uses_public_episode_data(self, monkeypatch):
        imf_df = pd.DataFrame(
            [
                {"sample": "oecd_advanced", "country": "ESP", "year": 2010, "total": 1.0, "tax": 0.3, "spend": 0.7},
                {"sample": "oecd_advanced", "country": "ESP", "year": 2011, "total": 1.0, "tax": 0.3, "spend": 0.7},
                {"sample": "oecd_advanced", "country": "ESP", "year": 2012, "total": 2.0, "tax": 1.0, "spend": 1.0},
                {"sample": "oecd_advanced", "country": "ESP", "year": 2013, "total": 2.0, "tax": 1.0, "spend": 1.0},
                {"sample": "oecd_advanced", "country": "ESP", "year": 2014, "total": 1.0, "tax": 0.4, "spend": 0.6},
                {"sample": "oecd_advanced", "country": "GBR", "year": 2010, "total": 0.4, "tax": 0.1, "spend": 0.3},
                {"sample": "oecd_advanced", "country": "GBR", "year": 2011, "total": 0.8, "tax": 0.4, "spend": 0.4},
                {"sample": "oecd_advanced", "country": "GBR", "year": 2012, "total": 0.8, "tax": 0.3, "spend": 0.5},
                {"sample": "oecd_advanced", "country": "GBR", "year": 2013, "total": 1.0, "tax": 0.2, "spend": 0.8},
                {"sample": "oecd_advanced", "country": "GBR", "year": 2014, "total": 0.9, "tax": 0.2, "spend": 0.7},
            ]
        )
        wb_df = pd.DataFrame(
            [
                {"country": "ESP", "country_name": "Spain", "year": 2010, "unemployment_rate": 20.0, "central_government_debt_ratio": 50.0},
                {"country": "ESP", "country_name": "Spain", "year": 2011, "unemployment_rate": 21.0, "central_government_debt_ratio": 60.0},
                {"country": "ESP", "country_name": "Spain", "year": 2012, "unemployment_rate": 23.0, "central_government_debt_ratio": 75.0},
                {"country": "ESP", "country_name": "Spain", "year": 2013, "unemployment_rate": 25.0, "central_government_debt_ratio": 90.0},
                {"country": "ESP", "country_name": "Spain", "year": 2014, "unemployment_rate": 24.0, "central_government_debt_ratio": 105.0},
                {"country": "GBR", "country_name": "United Kingdom", "year": 2010, "unemployment_rate": 8.0, "central_government_debt_ratio": 130.0},
                {"country": "GBR", "country_name": "United Kingdom", "year": 2011, "unemployment_rate": 8.2, "central_government_debt_ratio": 143.0},
                {"country": "GBR", "country_name": "United Kingdom", "year": 2012, "unemployment_rate": 8.3, "central_government_debt_ratio": 146.0},
                {"country": "GBR", "country_name": "United Kingdom", "year": 2013, "unemployment_rate": 7.8, "central_government_debt_ratio": 141.0},
                {"country": "GBR", "country_name": "United Kingdom", "year": 2014, "unemployment_rate": 6.4, "central_government_debt_ratio": 149.0},
            ]
        )

        monkeypatch.setattr(
            austerity_counterfactual,
            "load_imf_action_based_dataset",
            lambda refresh=False: imf_df,
        )
        monkeypatch.setattr(
            austerity_counterfactual,
            "load_country_context",
            lambda country, years, refresh=False: wb_df[wb_df["country"] == country],
        )

        episode = build_country_episode("ESP", 2010, 2014)
        assert episode["observed_actions"][0] == 1.0
        assert episode["delayed_actions"][:2] == [0.0, 0.0]

        result = run_imf_counterfactual_experiment(refresh_data=False)
        assert "ESP" in result["cases"]
        assert result["cases"]["ESP"]["summary"]["final_gdp_gain"] > 0
        assert result["boundary_case"]["summary"]["final_debt_ratio_difference"] > 0
