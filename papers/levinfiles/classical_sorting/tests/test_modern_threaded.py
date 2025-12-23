"""
Test the modern multithreaded selection sort implementation.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.multithreaded_selection import selection_sort_threaded
from modules.metrics import sortedness


def test_size(n: int, description: str = ""):
    """Test selection sort with array of size n."""
    print(f"\n{'='*70}")
    print(f"Testing N={n}: {description}")
    print(f"{'='*70}")

    # Create reverse-sorted array
    test_array = list(range(n, 0, -1))
    expected = sorted(test_array)

    print(f"Initial: {test_array[:10]}{'...' if n > 10 else ''}")
    print(f"Expected: {expected[:10]}{'...' if n > 10 else ''}")
    print()

    # Run threaded selection sort
    result, steps, history = selection_sort_threaded(test_array, max_time=30.0)

    print(f"Result: {result[:10]}{'...' if n > 10 else ''}")
    print(f"Swaps: {steps.swaps}")
    print(f"Comparisons: {steps.comparisons}")
    print(f"Sortedness: {sortedness(result):.1f}%")
    print(f"Correct: {result == expected}")

    # Show history
    if history:
        print(f"History samples: {len(history)} measurements")
        print(f"  Initial: {history[0]:.1f}%")
        if len(history) > 1:
            print(f"  Mid: {history[len(history)//2]:.1f}%")
        print(f"  Final: {history[-1]:.1f}%")

    # Traditional selection sort comparison
    traditional_swaps = n * (n - 1) // 2  # Worst case
    if traditional_swaps > 0:
        ratio = steps.swaps / traditional_swaps
        print(f"Ratio to traditional: {ratio:.1f}x")

    return result == expected


if __name__ == "__main__":
    print("Modern Multithreaded Selection Sort - Validation")
    print("="*70)

    results = []

    # Test N=10 (known failure point for sequential)
    results.append(("N=10", test_size(10, "Reverse sorted")))

    # Test N=20
    results.append(("N=20", test_size(20, "Reverse sorted")))

    # Test N=50
    results.append(("N=50", test_size(50, "Reverse sorted")))

    # Optional: Test N=100 if previous tests pass
    if all(r[1] for r in results):
        results.append(("N=100", test_size(100, "Reverse sorted - Full scale")))

    # Summary
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    for test_name, passed in results:
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} {test_name}")

    all_passed = all(r[1] for r in results)
    print(f"\nOverall: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
