"""Research-aligned austerity counterfactuals built from public data.

The point of this module is not to reconstruct a full DSGE system. It builds a
transparent reduced-form counterfactual around:

- IMF action-based fiscal consolidation episodes
- World Bank unemployment and debt-ratio context

This lets the repo show, in code, how the same consolidation schedule can look
very different once state-dependent multipliers, automatic stabilizers, and
monetary architecture are allowed to matter.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, List

from experiments.money_minsky_policy_mismatch.research_data import (
    load_country_context,
    load_imf_action_based_dataset,
)

DEFAULT_COUNTERFACTUAL_CASES = {
    "ESP": {
        "label": "Spain",
        "architecture": "quasi_sovereign",
        "base_rate": 0.03,
        "spread_phi": 0.035,
        "spread_threshold": 0.70,
        "structural_primary_deficit": 0.015,
        "stabilizer_slope": 0.55,
    },
    "GBR": {
        "label": "United Kingdom",
        "architecture": "sovereign_issuer",
        "base_rate": 0.02,
        "spread_phi": 0.0,
        "spread_threshold": 1.20,
        "structural_primary_deficit": 0.012,
        "stabilizer_slope": 0.45,
    },
}


@dataclass(frozen=True)
class CounterfactualCalibration:
    """Parameters for the reduced-form counterfactual model."""

    trend_growth: float = 0.018
    high_slack_multiplier: float = 1.4
    low_slack_multiplier: float = 0.6
    hysteresis: float = 0.18
    okun_beta: float = 0.35
    consolidation_passthrough: float = 0.85
    slack_unemployment_threshold: float = 8.0

    @classmethod
    def boundary_case(cls) -> "CounterfactualCalibration":
        """A lower-multiplier calibration that weakens the anti-austerity result."""
        return cls(
            high_slack_multiplier=0.3,
            low_slack_multiplier=0.2,
            hysteresis=0.05,
            okun_beta=0.15,
            consolidation_passthrough=0.90,
        )


def run_imf_counterfactual_experiment(
    countries: tuple[str, ...] = ("ESP", "GBR"),
    start_year: int = 2010,
    end_year: int = 2014,
    refresh_data: bool = False,
    calibration: CounterfactualCalibration | None = None,
) -> Dict[str, object]:
    """Run the public-data-backed austerity counterfactual experiment."""
    if calibration is None:
        calibration = CounterfactualCalibration()

    cases = {}
    for country in countries:
        episode = build_country_episode(
            country=country,
            start_year=start_year,
            end_year=end_year,
            refresh_data=refresh_data,
        )
        country_params = DEFAULT_COUNTERFACTUAL_CASES[country]

        observed = simulate_counterfactual(
            actions=episode["observed_actions"],
            initial_debt_ratio=episode["initial_debt_ratio"],
            initial_unemployment=episode["initial_unemployment"],
            calibration=calibration,
            case_params=country_params,
        )
        delayed = simulate_counterfactual(
            actions=episode["delayed_actions"],
            initial_debt_ratio=episode["initial_debt_ratio"],
            initial_unemployment=episode["initial_unemployment"],
            calibration=calibration,
            case_params=country_params,
        )

        cases[country] = {
            **episode,
            "observed": observed,
            "delayed": delayed,
            "summary": summarize_comparison(observed, delayed),
        }

    boundary_country = countries[0]
    boundary_episode = cases[boundary_country]
    boundary_calibration = CounterfactualCalibration.boundary_case()
    boundary_observed = simulate_counterfactual(
        actions=boundary_episode["observed_actions"],
        initial_debt_ratio=boundary_episode["initial_debt_ratio"],
        initial_unemployment=boundary_episode["initial_unemployment"],
        calibration=boundary_calibration,
        case_params=DEFAULT_COUNTERFACTUAL_CASES[boundary_country],
    )
    boundary_delayed = simulate_counterfactual(
        actions=boundary_episode["delayed_actions"],
        initial_debt_ratio=boundary_episode["initial_debt_ratio"],
        initial_unemployment=boundary_episode["initial_unemployment"],
        calibration=boundary_calibration,
        case_params=DEFAULT_COUNTERFACTUAL_CASES[boundary_country],
    )

    return {
        "calibration": asdict(calibration),
        "cases": cases,
        "boundary_case": {
            "country": boundary_country,
            "calibration": asdict(boundary_calibration),
            "observed": boundary_observed,
            "delayed": boundary_delayed,
            "summary": summarize_comparison(boundary_observed, boundary_delayed),
        },
    }


def build_country_episode(
    country: str,
    start_year: int,
    end_year: int,
    refresh_data: bool = False,
) -> Dict[str, object]:
    """Join IMF consolidation actions with World Bank context for one country."""
    years = list(range(start_year, end_year + 1))
    imf_df = load_imf_action_based_dataset(refresh=refresh_data)
    imf_episode = (
        imf_df[(imf_df["country"] == country) & (imf_df["year"].between(start_year, end_year))]
        .sort_values("year")
        .reset_index(drop=True)
    )
    if imf_episode.empty:
        raise ValueError(f"No IMF consolidation episode found for {country} in {start_year}-{end_year}.")

    wb_context = load_country_context(country=country, years=years, refresh=refresh_data)
    if wb_context.empty:
        raise ValueError(f"No World Bank context found for {country}.")

    unemployment_map = dict(zip(wb_context["year"], wb_context["unemployment_rate"]))
    debt_map = dict(zip(wb_context["year"], wb_context["central_government_debt_ratio"]))

    return {
        "country": country,
        "country_name": DEFAULT_COUNTERFACTUAL_CASES[country]["label"],
        "architecture": DEFAULT_COUNTERFACTUAL_CASES[country]["architecture"],
        "years": years,
        "observed_actions": [
            float(imf_episode.loc[imf_episode["year"] == year, "total"].iloc[0])
            for year in years
        ],
        "observed_tax_actions": [
            float(imf_episode.loc[imf_episode["year"] == year, "tax"].iloc[0])
            for year in years
        ],
        "observed_spending_actions": [
            float(imf_episode.loc[imf_episode["year"] == year, "spend"].iloc[0])
            for year in years
        ],
        "delayed_actions": build_delayed_consolidation_path(
            [
                float(imf_episode.loc[imf_episode["year"] == year, "total"].iloc[0])
                for year in years
            ]
        ),
        "actual_unemployment": [float(unemployment_map.get(year)) for year in years],
        "actual_debt_ratio": [
            float(debt_map.get(year)) if debt_map.get(year) is not None else None
            for year in years
        ],
        "initial_unemployment": float(unemployment_map[start_year]),
        "initial_debt_ratio": float(debt_map[start_year]),
    }


def build_delayed_consolidation_path(observed_actions: List[float]) -> List[float]:
    """Shift early consolidation out of the slump and soften the tail.

    This is intentionally explicit rather than optimized: the article can show
    the path in code and say exactly what the counterfactual means.
    """
    n = len(observed_actions)
    if n == 0:
        return []
    if n == 1:
        return [0.7 * observed_actions[0]]
    if n == 2:
        return [0.0, 0.7 * sum(observed_actions) / 2.0]

    delayed = [0.0, 0.0]
    for idx in range(2, n - 1):
        delayed.append(0.5 * observed_actions[idx - 2] + 0.5 * observed_actions[idx])
    delayed.append(0.7 * observed_actions[-1])
    return delayed


def simulate_counterfactual(
    actions: List[float],
    initial_debt_ratio: float,
    initial_unemployment: float,
    calibration: CounterfactualCalibration,
    case_params: Dict[str, float | str],
) -> Dict[str, List[float]]:
    """Simulate a reduced-form policy path from a consolidation schedule."""
    gdp = 100.0
    trend = 100.0
    debt_ratio = initial_debt_ratio / 100.0
    unemployment = initial_unemployment

    gdp_series = []
    trend_series = []
    gap_series = []
    debt_series = []
    unemployment_series = []
    growth_series = []
    primary_deficit_series = []
    rate_series = []
    multiplier_series = []

    for action in actions:
        slack = unemployment > calibration.slack_unemployment_threshold or gdp < trend
        multiplier = (
            calibration.high_slack_multiplier if slack else calibration.low_slack_multiplier
        )
        effective_rate = float(case_params["base_rate"]) + float(case_params["spread_phi"]) * max(
            debt_ratio - float(case_params["spread_threshold"]),
            0.0,
        )

        growth = (
            calibration.trend_growth
            - multiplier * (action / 100.0)
            - calibration.hysteresis * max((trend - gdp) / trend, 0.0)
        )
        gdp *= 1.0 + growth
        trend *= 1.0 + calibration.trend_growth
        output_gap = gdp / trend - 1.0

        unemployment = max(
            3.5,
            unemployment - calibration.okun_beta * (growth - calibration.trend_growth) * 100.0,
        )
        primary_deficit = (
            float(case_params["structural_primary_deficit"])
            + float(case_params["stabilizer_slope"]) * max(-output_gap, 0.0)
            - calibration.consolidation_passthrough * (action / 100.0)
        )
        debt_ratio = (debt_ratio * (1.0 + effective_rate)) / (1.0 + growth) + primary_deficit

        gdp_series.append(gdp)
        trend_series.append(trend)
        gap_series.append(output_gap)
        debt_series.append(debt_ratio * 100.0)
        unemployment_series.append(unemployment)
        growth_series.append(growth * 100.0)
        primary_deficit_series.append(primary_deficit * 100.0)
        rate_series.append(effective_rate * 100.0)
        multiplier_series.append(multiplier)

    return {
        "actions": actions[:],
        "gdp_index": gdp_series,
        "trend_index": trend_series,
        "output_gap": gap_series,
        "debt_ratio": debt_series,
        "unemployment_rate": unemployment_series,
        "growth_rate": growth_series,
        "primary_deficit_ratio": primary_deficit_series,
        "effective_rate": rate_series,
        "multiplier": multiplier_series,
    }


def summarize_comparison(observed: Dict[str, List[float]], delayed: Dict[str, List[float]]) -> Dict[str, float]:
    """Summarize how the delayed path differs from the observed one."""
    return {
        "final_gdp_gain": delayed["gdp_index"][-1] - observed["gdp_index"][-1],
        "final_debt_ratio_difference": delayed["debt_ratio"][-1] - observed["debt_ratio"][-1],
        "final_unemployment_difference": (
            delayed["unemployment_rate"][-1] - observed["unemployment_rate"][-1]
        ),
        "cumulative_action_reduction": sum(observed["actions"]) - sum(delayed["actions"]),
    }
