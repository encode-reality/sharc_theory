"""Save and load experiment results to/from compressed numpy cache.

Usage
-----
Save after a run::

    from experiments.money_minsky_policy_mismatch.cache import save_cache
    save_cache(output_dir, results)

Load for re-plotting::

    from experiments.money_minsky_policy_mismatch.cache import load_cache
    data = load_cache(output_dir)
"""

import json
from pathlib import Path

import numpy as np

CACHE_FILE = "experiment_cache.npz"
META_FILE = "experiment_meta.json"


def save_cache(output_dir: str, results: dict) -> Path:
    """Save experiment results to .npz (arrays) + .json (metadata).

    Results dict maps experiment name -> dict of arrays/scalars.
    Arrays are stored in the .npz; non-array metadata in .json.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    arrays = {}
    meta = {}

    for exp_name, exp_data in results.items():
        if exp_data is None:
            continue
        _flatten_to_arrays(arrays, meta, prefix=exp_name, data=exp_data)

    np.savez_compressed(output_path / CACHE_FILE, **arrays)
    with open(output_path / META_FILE, "w") as f:
        json.dump(meta, f, indent=2)

    print(f"  Cache saved: {output_path / CACHE_FILE}")
    return output_path / CACHE_FILE


def load_cache(output_dir: str) -> dict:
    """Load experiment results from cache."""
    output_path = Path(output_dir)
    npz_path = output_path / CACHE_FILE
    meta_path = output_path / META_FILE

    if not npz_path.exists():
        raise FileNotFoundError(
            f"No cache found at {npz_path}. Run without --plot-only first.")

    arrays = np.load(npz_path, allow_pickle=False)
    meta = {}
    if meta_path.exists():
        with open(meta_path) as f:
            meta = json.load(f)

    print(f"  Cache loaded: {npz_path}")
    return {"arrays": dict(arrays), "meta": meta}


def load_results(output_dir: str) -> dict:
    """Load and reconstruct nested experiment results from cache files."""
    cache = load_cache(output_dir)
    results = {}

    for key, value in cache["meta"].items():
        _assign_nested(results, key.split("__"), value)

    for key, value in cache["arrays"].items():
        _assign_nested(results, key.split("__"), value.tolist())

    return results


def _flatten_to_arrays(arrays: dict, meta: dict, prefix: str, data: dict):
    """Recursively flatten a nested dict into namespaced arrays and metadata."""
    for key, val in data.items():
        full_key = f"{prefix}__{key}"
        if isinstance(val, (list, np.ndarray)):
            try:
                arrays[full_key] = np.array(val, dtype=float)
            except (ValueError, TypeError):
                # Non-numeric list — store as JSON metadata
                meta[full_key] = val
        elif isinstance(val, dict):
            _flatten_to_arrays(arrays, meta, full_key, val)
        elif isinstance(val, (int, float, str, bool)):
            meta[full_key] = val
        else:
            meta[full_key] = str(val)


def _assign_nested(target: dict, path: list[str], value):
    """Assign a value into a nested dict given a split cache key."""
    current = target
    for key in path[:-1]:
        current = current.setdefault(key, {})
    current[path[-1]] = value
