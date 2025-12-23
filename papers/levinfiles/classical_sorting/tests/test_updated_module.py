"""Test the updated selection_sort in cell_view_sorts.py"""

from modules.cell_view_sorts import selection_sort
from modules.metrics import sortedness


def test_sizes():
    """Test multiple array sizes."""
import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
    sizes = [3, 5, 10, 20]

    for n in sizes:
        test_array = list(range(n, 0, -1))
        print(f"\n{'='*70}")
        print(f"Testing N={n}: {test_array[:5]}{'...' if n > 5 else ''}")

        result, steps, history = selection_sort(test_array)

        expected = sorted(test_array)
        correct = result == expected
        sort_pct = sortedness(result)

        print(f"Result: {result[:5]}{'...' if n > 5 else ''}")
        print(f"Sortedness: {sort_pct:.1f}%")
        print(f"Swaps: {steps.swaps}")
        print(f"Comparisons: {steps.comparisons}")
        print(f"Correct: {'PASS' if correct else 'FAIL'}")

        if not correct:
            print(f"ERROR: Expected {expected[:5]}{'...' if n > 5 else ''}")
            return False

    print(f"\n{'='*70}")
    print("ALL TESTS PASSED")
    return True


if __name__ == "__main__":
    test_sizes()
