"""CLI runner for Money-Minsky-Policy-Mismatch experiments."""

import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from experiments.money_minsky_policy_mismatch.config import DEFAULT_SEED
from experiments.money_minsky_policy_mismatch.experiments import (
    run_argument_rebuild_experiments,
    run_austerity_experiment,
    run_capacity_constraint_experiment,
    run_comparative_constraint_experiment,
    run_external_constraint_experiment,
    run_holder_composition_experiment,
    run_issuer_vs_user_experiment,
    run_jg_experiment,
    run_keen_stable_vs_crisis,
    run_policy_lab_experiment,
    run_rate_hike_experiment,
    run_rollover_experiment,
)
from experiments.money_minsky_policy_mismatch.policy_sectoral_model import (
    run_policy_sectoral_experiment,
)
from experiments.money_minsky_policy_mismatch.austerity_counterfactual import (
    run_imf_counterfactual_experiment,
)
from experiments.money_minsky_policy_mismatch.fragility_regimes import (
    run_fragility_regime_experiment,
)
from experiments.money_minsky_policy_mismatch.plotting import save_all_plots
from experiments.money_minsky_policy_mismatch.cache import save_cache, load_results


def run_experiment(seed=DEFAULT_SEED, experiment="all", output_dir="./results",
                   plot_only=False, refresh_data=False):
    """Run experiments and generate outputs."""
    print("=" * 60)
    print("  Money, Minsky, and Policy Mismatch — Experiments")
    print("=" * 60)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    plot_dir = Path(__file__).parent.parent.parent / "static" / "images" / "money_minsky_policy_mismatch"

    if plot_only:
        print("  --plot-only: loading from cache, skipping simulation")
        results = load_results(output_dir)
        save_all_plots(results, str(plot_dir))
        return results

    print(f"  seed={seed}")
    results = {}

    if experiment in ("all", "core", "fragility", "legacy_rate_hike", "legacy_all"):
        print("\n  [0] Keen stable vs crisis visualization...")
        results["keen_stable_vs_crisis"] = run_keen_stable_vs_crisis(seed=seed)
        print("      Done.")

    if experiment in ("all", "core", "new"):
        print("\n  [1] Core argument rebuild...")
        results.update(
            run_argument_rebuild_experiments(seed=seed, refresh_data=refresh_data)
        )
        print("      Done.")

    if experiment in ("all", "new"):
        print("\n  [N1] Comparative constraints (household/user/issuer)...")
        results["comparative_constraints"] = run_comparative_constraint_experiment()
        print("       Done.")

        print("\n  [N2] Policy lab (austerity vs functional finance)...")
        results["policy_lab"] = run_policy_lab_experiment(seed=seed)
        print("       Done.")

        print("\n  [N3] Capacity constraint (slack vs tight)...")
        results["capacity_constraint"] = run_capacity_constraint_experiment()
        print("       Done.")

        print("\n  [N4] Rollover / maturity structure...")
        results["rollover"] = run_rollover_experiment()
        print("       Done.")

        print("\n  [N5] External constraint (import dependence)...")
        results["external_constraint"] = run_external_constraint_experiment()
        print("       Done.")

        print("\n  [N6] Holder composition (who holds the debt)...")
        results["holder_composition"] = run_holder_composition_experiment()
        print("       Done.")

    if experiment == "policy_sectoral":
        print("\n  [1] Policy sectoral experiment...")
        results["policy_sectoral"] = run_policy_sectoral_experiment()
        print("      Done.")

    if experiment == "imf_counterfactual":
        print("\n  [1] IMF counterfactual experiment...")
        results["imf_counterfactual"] = run_imf_counterfactual_experiment(
            refresh_data=refresh_data
        )
        print("      Done.")

    if experiment == "fragility":
        print("\n  [1] Fragility regime experiment...")
        results["fragility_regimes"] = run_fragility_regime_experiment(seed=seed)
        print("      Done.")

    if experiment in ("legacy_rate_hike", "legacy_all"):
        print("\n  [L1] Legacy rate-hike experiment...")
        results["rate_hike"] = run_rate_hike_experiment(seed=seed)
        print("       Done.")

    if experiment in ("legacy_austerity", "legacy_all"):
        print("\n  [L2] Legacy austerity experiment...")
        results["austerity"] = run_austerity_experiment(seed=seed)
        print("       Done.")

    if experiment in ("legacy_jg", "legacy_all"):
        print("\n  [L3] Legacy Job Guarantee experiment...")
        results["jg"] = run_jg_experiment(seed=seed)
        print("       Done.")

    if experiment in ("legacy_issuer_user", "legacy_all"):
        print("\n  [L4] Legacy issuer vs user experiment...")
        results["issuer_user"] = run_issuer_vs_user_experiment(seed=seed)
        print("       Done.")

    # Save cache
    save_cache(str(output_path), results)

    # Generate plots
    print("\n  Generating plots...")
    save_all_plots(results, str(plot_dir))

    print("\n" + "=" * 60)
    print("  All experiments complete.")
    print("=" * 60)

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Run Money-Minsky-Policy-Mismatch experiments"
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED,
                        help=f"Random seed (default: {DEFAULT_SEED})")
    parser.add_argument("--experiment", type=str, default="all",
                        choices=[
                            "all",
                            "core",
                            "new",
                            "policy_sectoral",
                            "imf_counterfactual",
                            "fragility",
                            "legacy_all",
                            "legacy_rate_hike",
                            "legacy_austerity",
                            "legacy_jg",
                            "legacy_issuer_user",
                        ],
                        help="Which experiment to run (default: all)")
    parser.add_argument("--output-dir", type=str, default="./results",
                        help="Output directory for cache (default: ./results)")
    parser.add_argument("--plot-only", action="store_true",
                        help="Skip simulation, regenerate plots from cache")
    parser.add_argument("--refresh-data", action="store_true",
                        help="Refresh public data caches before running")
    args = parser.parse_args()

    run_experiment(
        seed=args.seed,
        experiment=args.experiment,
        output_dir=args.output_dir,
        plot_only=args.plot_only,
        refresh_data=args.refresh_data,
    )


if __name__ == "__main__":
    main()
