"""Tests for the public-data download and cache layer."""

import sys
import urllib.error
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch import research_data


class TestResearchDataCaching:
    """Research data should be fetched via code and cached locally."""

    def test_refresh_writes_csv_caches(self, monkeypatch, tmp_path):
        imf_df = pd.DataFrame(
            [
                {
                    "sample": "oecd_advanced",
                    "country": "ESP",
                    "year": 2010,
                    "total": 1.655,
                    "tax": 0.485,
                    "spend": 1.169,
                }
            ]
        )
        wb_df = pd.DataFrame(
            [
                {
                    "country": "ESP",
                    "country_name": "Spain",
                    "year": 2010,
                    "unemployment_rate": 19.86,
                    "central_government_debt_ratio": 49.96,
                }
            ]
        )

        monkeypatch.setattr(
            research_data,
            "_fetch_imf_action_based_dataset",
            lambda: imf_df,
        )
        monkeypatch.setattr(
            research_data,
            "_fetch_world_bank_context",
            lambda country_codes, start_year, end_year: wb_df,
        )

        paths = research_data.refresh_research_data(data_dir=tmp_path)
        assert paths["imf_actions"].exists()
        assert paths["world_bank_context"].exists()

        loaded_imf = pd.read_csv(paths["imf_actions"])
        loaded_wb = pd.read_csv(paths["world_bank_context"])
        assert list(loaded_imf["country"]) == ["ESP"]
        assert list(loaded_wb["country"]) == ["ESP"]

    def test_load_country_context_filters_years(self, tmp_path):
        wb_df = pd.DataFrame(
            [
                {
                    "country": "ESP",
                    "country_name": "Spain",
                    "year": 2010,
                    "unemployment_rate": 19.86,
                    "central_government_debt_ratio": 49.96,
                },
                {
                    "country": "ESP",
                    "country_name": "Spain",
                    "year": 2011,
                    "unemployment_rate": 21.39,
                    "central_government_debt_ratio": 57.79,
                },
            ]
        )
        wb_path = tmp_path / research_data.WORLD_BANK_CONTEXT_CSV.name
        wb_df.to_csv(wb_path, index=False)

        filtered = research_data.load_country_context(
            country="ESP",
            years=[2011],
            data_dir=tmp_path,
        )
        assert list(filtered["year"]) == [2011]

    def test_world_bank_indicator_falls_back_to_single_country_requests(
        self,
        monkeypatch,
    ):
        calls = []

        def fake_request(country_selector, indicator_code):
            calls.append((country_selector, indicator_code))
            if ";" in country_selector:
                raise urllib.error.HTTPError(
                    url="https://example.test",
                    code=400,
                    msg="Bad Request",
                    hdrs=None,
                    fp=None,
                )
            country_name = {
                "ESP": "Spain",
                "GBR": "United Kingdom",
            }[country_selector]
            return [
                {
                    "countryiso3code": country_selector,
                    "country": {"value": country_name},
                    "date": "2010",
                    "value": 1.23,
                }
            ]

        monkeypatch.setattr(
            research_data,
            "_request_world_bank_series",
            fake_request,
        )

        df = research_data._fetch_world_bank_indicator(
            country_codes=["ESP", "GBR"],
            indicator_code="SL.UEM.TOTL.ZS",
            column_name="unemployment_rate",
            start_year=2009,
            end_year=2011,
        )

        assert calls[0][0] == "ESP;GBR"
        assert ("ESP", "SL.UEM.TOTL.ZS") in calls
        assert ("GBR", "SL.UEM.TOTL.ZS") in calls
        assert sorted(df["country"].tolist()) == ["ESP", "GBR"]

    def test_refresh_uses_cached_imf_when_source_is_temporarily_unavailable(
        self,
        monkeypatch,
        tmp_path,
    ):
        cached_imf = pd.DataFrame(
            [
                {
                    "sample": "oecd_advanced",
                    "country": "ESP",
                    "year": 2010,
                    "total": 1.655,
                    "tax": 0.485,
                    "spend": 1.169,
                }
            ]
        )
        cached_imf.to_csv(tmp_path / research_data.IMF_ACTIONS_CSV.name, index=False)

        wb_df = pd.DataFrame(
            [
                {
                    "country": "ESP",
                    "country_name": "Spain",
                    "year": 2010,
                    "unemployment_rate": 19.86,
                    "central_government_debt_ratio": 49.96,
                }
            ]
        )

        monkeypatch.setattr(
            research_data,
            "_fetch_imf_action_based_dataset",
            lambda: (_ for _ in ()).throw(TimeoutError("temporary outage")),
        )
        monkeypatch.setattr(
            research_data,
            "_fetch_world_bank_context",
            lambda country_codes, start_year, end_year: wb_df,
        )

        paths = research_data.refresh_research_data(data_dir=tmp_path)
        loaded_imf = pd.read_csv(paths["imf_actions"])

        assert list(loaded_imf["country"]) == ["ESP"]
