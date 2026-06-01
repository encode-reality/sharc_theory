"""Tests for the deterministic sectoral-policy model."""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from experiments.money_minsky_policy_mismatch.policy_sectoral_model import (
    run_policy_sectoral_experiment,
    run_sectoral_scenario,
)


class TestSectoralPolicyModel:
    """Policy-sectoral model should preserve accounting and show policy differences."""

    def test_identity_holds_in_each_scenario(self):
        for scenario in ("supportive", "austerity", "delayed_repair"):
            history = run_sectoral_scenario(scenario=scenario, periods=50)
            assert history.verify_sectoral_identity()

    def test_immediate_austerity_reduces_post_shock_output(self):
        results = run_policy_sectoral_experiment(periods=50)
        supportive = np.mean(results["supportive"]["Y"][20:31])
        austerity = np.mean(results["austerity"]["Y"][20:31])
        assert austerity < supportive

    def test_immediate_austerity_reduces_tax_revenue(self):
        results = run_policy_sectoral_experiment(periods=50)
        supportive = np.mean(results["supportive"]["T"][20:31])
        austerity = np.mean(results["austerity"]["T"][20:31])
        assert austerity < supportive

    def test_immediate_austerity_squeezes_private_balance(self):
        results = run_policy_sectoral_experiment(periods=50)
        supportive = np.mean(results["supportive"]["private_balance"][20:31])
        austerity = np.mean(results["austerity"]["private_balance"][20:31])
        assert austerity < supportive

    def test_delayed_repair_sits_between_supportive_and_austerity(self):
        results = run_policy_sectoral_experiment(periods=50)
        supportive = np.mean(results["supportive"]["Y"][20:31])
        delayed = np.mean(results["delayed_repair"]["Y"][20:31])
        austerity = np.mean(results["austerity"]["Y"][20:31])
        assert supportive > delayed > austerity
