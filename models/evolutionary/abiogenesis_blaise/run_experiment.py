#!/usr/bin/env python3
"""
BFF Abiogenesis Experiment - Command Line Runner

Run the 2 million interaction experiment from the command line.
Saves results and creates basic visualizations.

Usage:
    python run_experiment.py
    python run_experiment.py --interactions 100000 --seed 42
"""

import sys
from pathlib import Path
import argparse
import time
import json
from collections import Counter
import numpy as np

# Add core to path
sys.path.insert(0, str(Path(__file__).parent))

from core.soup import Soup


def run_experiment(
    total_interactions: int = 2_000_000,
    soup_size: int = 1024,
    tape_length: int = 64,
    mutation_rate: float = 0.0,
    seed: int = 42,
    batch_size: int = 1000,
    sample_interval: int = 1000
):
    """Run the BFF experiment with specified parameters."""

    print("="*70)
    print("BFF ABIOGENESIS EXPERIMENT")
    print("="*70)
    print(f"\nConfiguration:")
    print(f"  Soup size: {soup_size} tapes")
    print(f"  Tape length: {tape_length} bytes")
    print(f"  Total interactions: {total_interactions:,}")
    print(f"  Mutation rate: {mutation_rate}")
    print(f"  Random seed: {seed}")
    print(f"  Zero mutation evolution: {mutation_rate == 0.0}")

    # Initialize soup
    print(f"\nInitializing primordial soup...")
    soup = Soup(
        size=soup_size,
        tape_length=tape_length,
        mutation_rate=mutation_rate,
        seed=seed
    )
    print(f"  Initial diversity: {soup.get_diversity():.4f}")
    print(f"  Initial unique tapes: {soup.count_unique_tapes()}/{soup_size}")

    # Prepare tracking
    num_batches = total_interactions // batch_size
    sampled_interactions = []
    sampled_ops_mean = []
    sampled_ops_max = []
    sampled_diversity = []

    transition_detected = False
    transition_point = None

    # Run simulation
    print(f"\nRunning simulation ({num_batches:,} batches of {batch_size})...")
    print("Progress: ", end='', flush=True)

    start_time = time.time()
    last_progress_time = start_time

    for batch_num in range(num_batches):
        # Run batch
        results = soup.run(num_interactions=batch_size, max_ops=10000)

        # Sample metrics
        if soup.interaction_count % sample_interval == 0:
            batch_ops = [r.operations for r in results]
            sampled_interactions.append(soup.interaction_count)
            sampled_ops_mean.append(np.mean(batch_ops))
            sampled_ops_max.append(np.max(batch_ops))
            sampled_diversity.append(soup.get_diversity())

        # Check for phase transition
        if not transition_detected and soup.interaction_count % 10000 == 0:
            if len(sampled_ops_mean) > 10:
                recent_mean = np.mean(sampled_ops_mean[-10:])
                if recent_mean > 500:
                    transition_detected = True
                    transition_point = soup.interaction_count
                    print(f"\n🎉 PHASE TRANSITION at {transition_point:,}! ", end='', flush=True)

        # Progress indicator
        if batch_num % (num_batches // 20) == 0:
            print("█", end='', flush=True)

        # Status updates
        if soup.interaction_count % 200000 == 0:
            elapsed = time.time() - last_progress_time
            rate = 200000 / elapsed
            last_progress_time = time.time()
            print(f"\n[{soup.interaction_count:,}] {rate:.0f} int/sec, ops={sampled_ops_mean[-1]:.1f}, div={soup.get_diversity():.3f} ", end='', flush=True)

    total_time = time.time() - start_time

    print("\n\n" + "="*70)
    print("SIMULATION COMPLETE")
    print("="*70)

    # Final statistics
    print(f"\nPerformance:")
    print(f"  Total time: {total_time/60:.1f} minutes ({total_time:.1f} seconds)")
    print(f"  Average speed: {total_interactions/total_time:.1f} interactions/second")

    print(f"\nFinal state:")
    print(f"  Diversity: {soup.get_diversity():.4f}")
    print(f"  Unique tapes: {soup.count_unique_tapes()}/{soup_size}")

    if transition_detected:
        print(f"\n✅ Phase transition detected at interaction {transition_point:,}")
        print(f"   Final mean operations: {sampled_ops_mean[-1]:.1f}")
    else:
        print(f"\n⚠️  No clear phase transition detected")
        print(f"   Maximum mean operations: {max(sampled_ops_mean):.1f}")

    # Analyze population
    tape_hashes = soup.get_tape_hashes()
    hash_counts = Counter(tape_hashes)

    print(f"\nPopulation analysis:")
    print(f"  Unique tapes: {len(hash_counts)}")

    if len(hash_counts) > 0:
        top1_count = hash_counts.most_common(1)[0][1]
        top1_frac = top1_count / soup_size
        print(f"  Dominant replicator: {top1_count} copies ({100*top1_frac:.1f}%)")

        print(f"\n  Top 10 replicators:")
        for rank, (hash_val, count) in enumerate(hash_counts.most_common(10), 1):
            pct = 100 * count / soup_size
            print(f"    #{rank}: {count:4d} copies ({pct:5.1f}%) - {hash_val[:16]}...")

    # Save results
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    results_dir = Path(__file__).parent / "experiments"
    results_dir.mkdir(exist_ok=True)

    # Save metrics
    metrics_path = results_dir / f"run_{timestamp}_metrics.json"
    metrics = {
        'config': {
            'soup_size': soup_size,
            'tape_length': tape_length,
            'mutation_rate': mutation_rate,
            'seed': seed,
            'total_interactions': total_interactions
        },
        'results': {
            'runtime_seconds': total_time,
            'transition_detected': transition_detected,
            'transition_point': transition_point,
            'final_diversity': soup.get_diversity(),
            'final_unique_count': soup.count_unique_tapes(),
        },
        'time_series': {
            'sampled_interactions': sampled_interactions,
            'sampled_ops_mean': sampled_ops_mean,
            'sampled_ops_max': sampled_ops_max,
            'sampled_diversity': sampled_diversity,
        }
    }

    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)

    print(f"\n📊 Metrics saved to: {metrics_path}")

    # Save final state
    checkpoint_dir = results_dir / "checkpoints"
    checkpoint_dir.mkdir(exist_ok=True)

    state_path = checkpoint_dir / f"run_{timestamp}_final.json"
    with open(state_path, 'w') as f:
        json.dump(soup.get_state(), f)

    print(f"💾 Final state saved to: {state_path}")
    print(f"   Size: {state_path.stat().st_size / 1024:.1f} KB")

    print("\n✅ Experiment complete!")
    print("\nTo visualize results, open notebooks/02_long_run_2M.ipynb")
    print("and load the saved checkpoint.")

    return metrics


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Run BFF abiogenesis experiment",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '--interactions', '-n', type=int, default=2_000_000,
        help='Total number of interactions to run'
    )
    parser.add_argument(
        '--soup-size', '-s', type=int, default=1024,
        help='Number of tapes in the soup'
    )
    parser.add_argument(
        '--tape-length', '-l', type=int, default=64,
        help='Length of each tape in bytes'
    )
    parser.add_argument(
        '--mutation-rate', '-m', type=float, default=0.0,
        help='Mutation rate (0.0 = zero mutation evolution)'
    )
    parser.add_argument(
        '--seed', type=int, default=42,
        help='Random seed for reproducibility'
    )
    parser.add_argument(
        '--batch-size', '-b', type=int, default=1000,
        help='Interactions per batch'
    )

    args = parser.parse_args()

    # Run experiment
    run_experiment(
        total_interactions=args.interactions,
        soup_size=args.soup_size,
        tape_length=args.tape_length,
        mutation_rate=args.mutation_rate,
        seed=args.seed,
        batch_size=args.batch_size
    )


if __name__ == '__main__':
    main()
