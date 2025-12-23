"""
Compare the working test implementation with the module implementation.
"""

print("Reading test_selection_full_groups.py (WORKING)...")
print("=" * 70)

with open('test_selection_full_groups.py', 'r') as f:
    test_content = f.read()

# Extract the key function
import re
match = re.search(r'def selection_sort_with_groups\(initial_values\):.*?return final_values, steps, history', test_content, re.DOTALL)
if match:
    working_impl = match.group(0)
    print("Working implementation:")
    print("-" * 70)
    # Count lines
    lines = working_impl.split('\n')
    print(f"Lines: {len(lines)}")
    print()
    
print("\nReading modules/cell_view_sorts.py (BROKEN)...")
print("=" * 70)

with open('modules/cell_view_sorts.py', 'r') as f:
    module_content = f.read()

match = re.search(r'def selection_sort\(.*?\n    return final_values, steps, history', module_content, re.DOTALL)
if match:
    module_impl = match.group(0)
    print("Module implementation:")
    print("-" * 70)
    lines = module_impl.split('\n')
    print(f"Lines: {len(lines)}")
    print()

print("\nKey differences to investigate:")
print("=" * 70)
print("1. Check if SelectionCell class is identical")
print("2. Check if Group class is identical")
print("3. Check main algorithm loop logic")
print("4. Check group merging behavior")
print("5. Check termination conditions")
