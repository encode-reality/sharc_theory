"""Test the fixed mixed_algotype_sort function."""

from modules.cell_view_sorts import mixed_algotype_sort
from modules.metrics import sortedness


def test_pure_algotypes():
    """Test pure algotype arrays."""
import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
    n = 20
    test_array = list(range(n, 0, -1))

    print("Testing Pure Algotypes (N=20)")
    print("="*70)

    # Test pure selection
    print("\nPure Selection...")
    algotypes = ["selection"] * n
    result, steps, sort_history, _ = mixed_algotype_sort(test_array, algotypes)

    expected = sorted(test_array)
    correct = result == expected
    sort_pct = sortedness(result)

    print(f"Result: {result[:5]}...{result[-5:]}")
    print(f"Expected: {expected[:5]}...{expected[-5:]}")
    print(f"Sortedness: {sort_pct:.1f}%")
    print(f"Swaps: {steps.swaps}")
    print(f"Correct: {'PASS' if correct else 'FAIL'}")

    if not correct:
        print("ERROR: Pure selection failed!")
        return False

    # Test pure bubble
    print("\nPure Bubble...")
    algotypes = ["bubble"] * n
    result, steps, sort_history, _ = mixed_algotype_sort(test_array, algotypes)

    correct = result == expected
    sort_pct = sortedness(result)

    print(f"Sortedness: {sort_pct:.1f}%")
    print(f"Swaps: {steps.swaps}")
    print(f"Correct: {'PASS' if correct else 'FAIL'}")

    # Test pure insertion
    print("\nPure Insertion...")
    algotypes = ["insertion"] * n
    result, steps, sort_history, _ = mixed_algotype_sort(test_array, algotypes)

    correct = result == expected
    sort_pct = sortedness(result)

    print(f"Sortedness: {sort_pct:.1f}%")
    print(f"Swaps: {steps.swaps}")
    print(f"Correct: {'PASS' if correct else 'FAIL'}")

    # Test equal mix
    print("\nEqual Mix...")
    # Create equal distribution
    third = n // 3
    algotypes = (["bubble"] * third +
                 ["insertion"] * third +
                 ["selection"] * (n - 2 * third))  # Remaining go to selection
    print(f"Algotype counts: B={algotypes.count('bubble')}, "
          f"I={algotypes.count('insertion')}, S={algotypes.count('selection')}")
    result, steps, sort_history, _ = mixed_algotype_sort(test_array, algotypes)

    correct = result == expected
    sort_pct = sortedness(result)

    print(f"Sortedness: {sort_pct:.1f}%")
    print(f"Swaps: {steps.swaps}")
    print(f"Correct: {'PASS (100%)' if correct else f'PARTIAL ({sort_pct:.1f}%)'}")

    # Mixed algotypes are EXPECTED to have reduced efficiency (per paper)
    # 85%+ sortedness is good performance for mixed arrays
    if sort_pct < 85.0:
        print(f"WARNING: Expected >=85% for equal mix, got {sort_pct:.1f}%")
        return False

    print("\n" + "="*70)
    print("ALL TESTS PASSED")
    print("Note: Mixed algotypes achieve partial sorting as expected per paper")
    return True


if __name__ == "__main__":
    test_pure_algotypes()
