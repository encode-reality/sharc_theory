"""Research data loaders for austerity-policy experiments.

This module pulls two public datasets into small local CSV caches:

- IMF action-based fiscal consolidation episodes
- World Bank macro context series used for counterfactual initialization

The fetchers are written to be transparent and deterministic so the blog can
show the data pipeline directly in code rather than relying on hand-copied
numbers.
"""

from __future__ import annotations

import http.client
import io
import json
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from typing import Iterable

import pandas as pd

PACKAGE_DIR = Path(__file__).parent
REPO_ROOT = PACKAGE_DIR.parent.parent
DATA_DIR = REPO_ROOT / "results" / "money_minsky_policy_mismatch_data"
IMF_ACTIONS_CSV = DATA_DIR / "imf_action_based_consolidations.csv"
WORLD_BANK_CONTEXT_CSV = DATA_DIR / "world_bank_policy_context.csv"

IMF_ACTIONS_URL = (
    "https://www.imf.org/-/media/files/publications/wp/2024/datasets/wp24210.zip"
)

WORLD_BANK_INDICATORS = {
    "SL.UEM.TOTL.ZS": "unemployment_rate",
    "GC.DOD.TOTL.GD.ZS": "central_government_debt_ratio",
}


def refresh_research_data(
    data_dir: Path | None = None,
    start_year: int = 2000,
    end_year: int = 2024,
) -> dict[str, Path]:
    """Refresh the local CSV caches from IMF and World Bank sources."""
    if data_dir is None:
        data_dir = DATA_DIR
    data_dir.mkdir(parents=True, exist_ok=True)

    imf_path = data_dir / IMF_ACTIONS_CSV.name
    imf_df = _refresh_or_load_cached(
        fetch_fn=_fetch_imf_action_based_dataset,
        cache_path=imf_path,
        label="IMF action-based dataset",
    )

    country_codes = sorted(imf_df["country"].dropna().unique().tolist())
    wb_path = data_dir / WORLD_BANK_CONTEXT_CSV.name
    wb_df = _refresh_or_load_cached(
        fetch_fn=lambda: _fetch_world_bank_context(country_codes, start_year, end_year),
        cache_path=wb_path,
        label="World Bank policy context",
    )

    return {"imf_actions": imf_path, "world_bank_context": wb_path}


def load_imf_action_based_dataset(
    data_dir: Path | None = None,
    refresh: bool = False,
) -> pd.DataFrame:
    """Load the IMF action-based dataset from cache or source."""
    if data_dir is None:
        data_dir = DATA_DIR
    path = data_dir / IMF_ACTIONS_CSV.name
    if refresh or not path.exists():
        refresh_research_data(data_dir=data_dir)
    return pd.read_csv(path)


def load_world_bank_context(
    data_dir: Path | None = None,
    refresh: bool = False,
) -> pd.DataFrame:
    """Load World Bank context data from cache or source."""
    if data_dir is None:
        data_dir = DATA_DIR
    path = data_dir / WORLD_BANK_CONTEXT_CSV.name
    if refresh or not path.exists():
        refresh_research_data(data_dir=data_dir)
    return pd.read_csv(path)


def load_country_context(
    country: str,
    years: Iterable[int],
    data_dir: Path | None = None,
    refresh: bool = False,
) -> pd.DataFrame:
    """Return one country's World Bank context over a chosen year range."""
    wb_df = load_world_bank_context(data_dir=data_dir, refresh=refresh)
    years = set(int(year) for year in years)
    result = wb_df[(wb_df["country"] == country) & (wb_df["year"].isin(years))].copy()
    return result.sort_values("year").reset_index(drop=True)


def _fetch_imf_action_based_dataset() -> pd.DataFrame:
    """Download and tidy the IMF consolidation workbook."""
    payload = _read_url_bytes(IMF_ACTIONS_URL)

    with zipfile.ZipFile(io.BytesIO(payload)) as zf:
        workbook_name = zf.namelist()[0]
        with zf.open(workbook_name) as workbook_file:
            table_a1 = pd.read_excel(workbook_file, sheet_name="Table_A1", header=None)

        with zf.open(workbook_name) as workbook_file:
            table_a2 = pd.read_excel(workbook_file, sheet_name="Table_A2", header=None)

    oecd = _extract_block_table(
        table_a1,
        starts=[1, 7, 13, 19, 26, 32],
        data_row_start=5,
        sample="oecd_advanced",
    )
    lac = _extract_block_table(
        table_a2,
        starts=[1, 7],
        data_row_start=3,
        sample="latin_america_caribbean",
    )

    df = pd.concat([oecd, lac], ignore_index=True)
    df["country"] = df["country"].astype(str).str.strip()
    df["year"] = df["year"].astype(int)
    for column in ("total", "tax", "spend"):
        df[column] = pd.to_numeric(df[column], errors="coerce")
    return df.sort_values(["sample", "country", "year"]).reset_index(drop=True)


def _extract_block_table(
    raw: pd.DataFrame,
    starts: list[int],
    data_row_start: int,
    sample: str,
) -> pd.DataFrame:
    """Convert a repeated 5-column block table into a long dataframe."""
    blocks = []
    for start in starts:
        block = raw.iloc[data_row_start:, start:start + 5].copy()
        block.columns = ["country", "year", "total", "tax", "spend"]
        block = block.dropna(subset=["country", "year"])
        block["sample"] = sample
        blocks.append(block)
    return pd.concat(blocks, ignore_index=True)


def _fetch_world_bank_context(
    country_codes: list[str],
    start_year: int,
    end_year: int,
) -> pd.DataFrame:
    """Fetch unemployment and debt-ratio context from the World Bank API."""
    frames = []
    for indicator_code, column_name in WORLD_BANK_INDICATORS.items():
        frames.append(
            _fetch_world_bank_indicator(
                country_codes=country_codes,
                indicator_code=indicator_code,
                column_name=column_name,
                start_year=start_year,
                end_year=end_year,
            )
        )

    merged = None
    for frame in frames:
        if merged is None:
            merged = frame
        else:
            merged = merged.merge(frame, how="outer", on=["country", "country_name", "year"])

    if merged is None:
        raise RuntimeError("Failed to fetch World Bank context data.")
    return merged.sort_values(["country", "year"]).reset_index(drop=True)


def _fetch_world_bank_indicator(
    country_codes: list[str],
    indicator_code: str,
    column_name: str,
    start_year: int,
    end_year: int,
) -> pd.DataFrame:
    """Fetch one indicator in chunks to avoid oversized URLs."""
    rows: list[dict[str, object]] = []
    for chunk in _chunked(country_codes, chunk_size=8):
        try:
            items = _request_world_bank_series(";".join(chunk), indicator_code)
        except (urllib.error.HTTPError, urllib.error.URLError):
            items = []
            for country_code in chunk:
                items.extend(
                    _request_world_bank_series(country_code, indicator_code)
                )

        for item in items:
            year = int(item["date"])
            if year < start_year or year > end_year:
                continue
            rows.append(
                {
                    "country": item["countryiso3code"],
                    "country_name": item["country"]["value"],
                    "year": year,
                    column_name: item["value"],
                }
            )

    if not rows:
        return pd.DataFrame(columns=["country", "country_name", "year", column_name])
    return pd.DataFrame(rows)


def _request_world_bank_series(
    country_selector: str,
    indicator_code: str,
) -> list[dict[str, object]]:
    """Fetch one World Bank indicator payload for one or more countries."""
    url = (
        "https://api.worldbank.org/v2/country/"
        f"{country_selector}/indicator/{indicator_code}?format=json&per_page=20000"
    )
    payload = json.loads(_read_url_bytes(url).decode("utf-8"))

    if not isinstance(payload, list) or len(payload) < 2 or payload[1] is None:
        return []
    return payload[1]


def _chunked(items: list[str], chunk_size: int) -> Iterable[list[str]]:
    """Yield fixed-size chunks from a list."""
    for start in range(0, len(items), chunk_size):
        yield items[start:start + chunk_size]


def _read_url_bytes(url: str, timeout: int = 60, retries: int = 3) -> bytes:
    """Read bytes from a URL with limited retries for transient failures."""
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            if 400 <= exc.code < 500 and exc.code != 429:
                raise
            last_error = exc
        except (
            TimeoutError,
            urllib.error.URLError,
            http.client.RemoteDisconnected,
            ConnectionResetError,
        ) as exc:
            last_error = exc

        if attempt < retries:
            time.sleep(min(2 ** (attempt - 1), 5))

    if last_error is None:
        raise RuntimeError(f"Failed to fetch {url}")
    raise last_error


def _refresh_or_load_cached(fetch_fn, cache_path: Path, label: str) -> pd.DataFrame:
    """Refresh a dataset, or fall back to the on-disk cache if the source fails."""
    try:
        df = fetch_fn()
        df.to_csv(cache_path, index=False)
        return df
    except Exception as exc:
        if cache_path.exists():
            print(
                f"  Warning: {label} refresh failed ({exc}). "
                f"Using cached data at {cache_path}."
            )
            return pd.read_csv(cache_path)
        raise
