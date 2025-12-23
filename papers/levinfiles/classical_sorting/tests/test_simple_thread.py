"""
Simple diagnostic test for multithreaded implementation.
"""

import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.multithreaded_selection import selection_sort_threaded
import time


def test_simple():
    """Test with minimal array."""
    print("Testing N=3 with 5 second timeout...")
    test_array = [3, 2, 1]

    start = time.time()
    try:
        result, steps, history = selection_sort_threaded(test_array, max_time=5.0)
        elapsed = time.time() - start

        print(f"Completed in {elapsed:.2f} seconds")
        print(f"Result: {result}")
        print(f"Expected: {sorted(test_array)}")
        print(f"Correct: {result == sorted(test_array)}")
        print(f"Swaps: {steps.swaps}")
        print(f"History length: {len(history)}")

    except Exception as e:
        elapsed = time.time() - start
        print(f"Error after {elapsed:.2f} seconds: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_simple()
    print("\nTest complete. Exiting...")
