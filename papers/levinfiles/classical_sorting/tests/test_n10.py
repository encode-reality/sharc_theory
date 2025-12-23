"""Test just N=10."""

from modules.multithreaded_selection import selection_sort_threaded
from modules.metrics import sortedness


def test_n10():
    """Test with N=10."""
import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
    test_array = list(range(10, 0, -1))
    print(f"Testing N=10: {test_array}")

    result, steps, history = selection_sort_threaded(test_array, max_time=10.0)

    print(f"Result: {result}")
    print(f"Expected: {sorted(test_array)}")
    print(f"Correct: {result == sorted(test_array)}")
    print(f"Sortedness: {sortedness(result):.1f}%")
    print(f"Swaps: {steps.swaps}")
    print(f"Comparisons: {steps.comparisons}")


if __name__ == "__main__":
    test_n10()
