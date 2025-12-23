import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.cell_view_sorts import selection_sort

test_array = [2, 1]
print(f"Testing: {test_array}", flush=True)

# Patch the function to add debug output
import modules.cell_view_sorts as cvs
original_sort = cvs.selection_sort

def debug_selection_sort(initial_values, frozen_indices=None, algotype="selection"):
    print(f"Entering selection_sort with {initial_values}", flush=True)
    try:
        # Just call the original for now to see if it even gets called
        result = original_sort(initial_values, frozen_indices, algotype)
        print(f"selection_sort completed", flush=True)
        return result
    except Exception as e:
        print(f"Exception in selection_sort: {e}", flush=True)
        raise

cvs.selection_sort = debug_selection_sort

result, steps, history = cvs.selection_sort(test_array)
print(f"Final result: {result}")
