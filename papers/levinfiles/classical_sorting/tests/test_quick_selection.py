import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.cell_view_sorts import selection_sort
import signal
import sys

def timeout_handler(signum, frame):
    print("TIMEOUT - infinite loop detected!")
    sys.exit(1)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(3)  # 3 second timeout

try:
    test_array = [2, 1]
    print(f"Testing: {test_array}")
    result, steps, history = selection_sort(test_array)
    print(f"Result: {result}")
    print(f"Success: {result == [1, 2]}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
finally:
    signal.alarm(0)
