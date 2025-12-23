"""Test frozen cell sortedness dynamics over time."""

import numpy as np
import matplotlib.pyplot as plt
from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort
from modules.metrics import sortedness

def test_frozen_dynamics():
    """Test how sortedness changes over time with frozen cells."""

    # Parameters
import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
    array_size = 10  # Small array for testing
    frozen_pct = 10
    num_frozen = max(1, int(array_size * frozen_pct / 100))  # Ensure at least 1 frozen

    # Create test array
    test_array = list(range(array_size, 0, -1))  # Reverse sorted (worst case)

    print("Testing Frozen Cell Dynamics (10% frozen)")
    print("="*70)
    print(f"Array size: {array_size}")
    print(f"Frozen cells: {frozen_pct}% ({num_frozen} cells)")
    print(f"Initial array: {test_array[:5]}...{test_array[-5:]}")
    print()

    # Randomly select cells to freeze
    np.random.seed(42)  # For reproducibility
    frozen_positions = np.random.choice(array_size, size=num_frozen, replace=False)
    frozen_indices = {int(pos): 'immovable' for pos in frozen_positions}  # Fixed: use valid FrozenType

    print(f"Frozen positions: {sorted(frozen_indices.keys())}")
    print()

    # Test each algorithm
    algorithms = [
        ('Bubble Sort', bubble_sort),
        ('Insertion Sort', insertion_sort),
        ('Selection Sort', selection_sort)
    ]

    results = {}

    for name, algo_func in algorithms:
        print(f"Testing {name}...")
        result, steps, history = algo_func(test_array.copy(), frozen_indices=frozen_indices)

        final_sortedness = sortedness(result)

        results[name] = {
            'history': history,
            'final_sortedness': final_sortedness,
            'swaps': steps.swaps,
            'comparisons': steps.comparisons
        }

        print(f"  Final sortedness: {final_sortedness:.1f}%")
        print(f"  Swaps: {steps.swaps:,}")
        print(f"  Comparisons: {steps.comparisons:,}")
        print(f"  History points: {len(history)}")
        print()

    # Visualize the dynamics
    print("Creating visualization...")
    fig, ax = plt.subplots(figsize=(12, 6))

    colors = {'Bubble Sort': '#1f77b4', 'Insertion Sort': '#ff7f0e', 'Selection Sort': '#2ca02c'}

    for name, data in results.items():
        history = data['history']
        if len(history) > 0:
            # Plot sortedness vs swap number
            ax.plot(range(len(history)), history,
                   label=name, linewidth=2, color=colors[name], alpha=0.8)

    ax.set_xlabel('Swap Number', fontsize=12)
    ax.set_ylabel('Sortedness (%)', fontsize=12)
    ax.set_title(f'Sortedness Dynamics with {frozen_pct}% Frozen Cells',
                fontsize=13, fontweight='bold')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 105)

    # Add horizontal line at 100%
    ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5, label='Perfect Sort')

    plt.tight_layout()
    plt.savefig('figures/frozen_dynamics_test.png', dpi=150, bbox_inches='tight')
    plt.close()  # Close the figure to free memory
    print("Figure saved: figures/frozen_dynamics_test.png")

    print()
    print("="*70)
    print("Summary of Dynamics:")
    print("="*70)

    for name, data in results.items():
        history = data['history']
        if len(history) > 0:
            print(f"\n{name}:")
            print(f"  Starting sortedness: {history[0]:.1f}%")
            print(f"  Final sortedness: {history[-1]:.1f}%")
            print(f"  Improvement: {history[-1] - history[0]:.1f}%")
            print(f"  Steps to converge: {len(history)}")

            # Find when it reaches 90% (if it does)
            reached_90 = None
            for i, s in enumerate(history):
                if s >= 90.0:
                    reached_90 = i
                    break

            if reached_90 is not None:
                print(f"  Reached 90% at swap: {reached_90}")
            else:
                print(f"  Did not reach 90%")

    print("\n" + "="*70)
    print("PASS: Frozen dynamics test complete")
    return True

if __name__ == "__main__":
    test_frozen_dynamics()
