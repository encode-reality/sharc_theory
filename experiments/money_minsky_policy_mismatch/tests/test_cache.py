"""Tests for experiment result caching and reconstruction."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.cache import load_results, save_cache


class TestCacheRoundTrip:
    """Cached experiment outputs should round-trip back into nested dicts."""

    def test_nested_results_round_trip(self, tmp_path):
        results = {
            "policy_sectoral": {
                "shock_start": 12,
                "supportive": {
                    "Y": [1.0, 2.0, 3.0],
                    "scenario": "supportive",
                },
            }
        }
        save_cache(str(tmp_path), results)
        restored = load_results(str(tmp_path))
        assert restored["policy_sectoral"]["shock_start"] == 12
        assert restored["policy_sectoral"]["supportive"]["Y"] == [1.0, 2.0, 3.0]
        assert restored["policy_sectoral"]["supportive"]["scenario"] == "supportive"
