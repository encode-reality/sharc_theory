#!/usr/bin/env python3
import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Direct test of selection_sort from modules"""

import sys
print("Starting test...", flush=True)

# Direct import
from modules.cell_view_sorts import selection_sort

print("Import successful", flush=True)

# Simple test
test_array = [2, 1]
print(f"Testing {test_array}...", flush=True)

result, steps, history = selection_sort(test_array)

print(f"Result: {result}")
print(f"Swaps: {steps.swaps}")
print(f"Success: {result == [1, 2]}")
