import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Find the exact array size where selection_sort starts failing."""

from modules.cell_view_sorts import selection_sort

print("Testing Selection Sort at different array sizes...")
print("=" * 70)

test_sizes = [2, 3, 4, 5, 6, 7, 8, 10, 15, 20]

for n in test_sizes:
    # Create test array
    test_array = list(range(n, 0, -1))  # Reverse sorted (worst case)
    
    print(f"\nN={n}: Testing {test_array[:5]}{'...' if n > 5 else ''}")
    
    try:
        result, steps, history = selection_sort(test_array)
        expected = sorted(test_array)
        
        is_correct = (result == expected)
        final_sortedness = history[-1] if history else 0
        
        status = "[PASS]" if is_correct else "[FAIL]"
        print(f"  {status} Sortedness: {final_sortedness:.1f}%, Swaps: {steps.swaps}, Correct: {is_correct}")
        
        if not is_correct:
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            print(f"  FAILURE THRESHOLD FOUND!")
            break
            
    except KeyboardInterrupt:
        print(f"  [TIMEOUT] Interrupted at N={n}")
        print(f"  FAILURE THRESHOLD: N={n}")
        break
    except Exception as e:
        print(f"  [ERROR] {e}")
        break

print("\n" + "=" * 70)
