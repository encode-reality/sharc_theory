"""Detailed side-by-side comparison of implementations."""

# Read working version
with open('test_selection_full_groups.py', 'r') as f:
    test_lines = f.readlines()

# Read module version
with open('modules/cell_view_sorts.py', 'r') as f:
    module_lines = f.readlines()

# Find SelectionCell in test file
print("=" * 70)
print("WORKING SelectionCell (test_selection_full_groups.py):")
print("=" * 70)
in_class = False
for i, line in enumerate(test_lines, 1):
    if 'class SelectionCell:' in line:
        in_class = True
    if in_class:
        print(f"{i:3}: {line}", end='')
        if line.strip() and not line.strip().startswith('#') and in_class and i > 56:
            if 'def can_be_moved' in line:
                # Print next few lines
                for j in range(4):
                    if i + j < len(test_lines):
                        print(f"{i+j+1:3}: {test_lines[i+j]}", end='')
                break

print("\n" + "=" * 70)
print("MODULE SelectionCell (modules/cell_view_sorts.py):")
print("=" * 70)
in_class = False
for i, line in enumerate(module_lines, 1):
    if 'class SelectionCell:' in line and 'def selection_sort' in ''.join(module_lines[max(0,i-5):i]):
        in_class = True
        start = i
    if in_class:
        print(f"{i:3}: {line}", end='')
        if 'def can_be_moved' in line:
            # Print next few lines
            for j in range(1, 5):
                if i + j - 1 < len(module_lines):
                    print(f"{i+j:3}: {module_lines[i+j-1]}", end='')
            break

print("\n" + "=" * 70)
print("KEY ALGORITHM DIFFERENCES:")
print("=" * 70)

# Check for specific critical lines
print("\n1. Checking 'continue' after merge in working version:")
test_str = ''.join(test_lines)
if 'merged_any = True' in test_str:
    idx = test_str.find('merged_any = True')
    snippet = test_str[idx-200:idx+300]
    print("Working version around 'merged_any = True':")
    lines = snippet.split('\n')
    for line in lines[-5:]:
        print(f"   {line}")

print("\n2. Checking 'continue' after merge in module version:")
module_str = ''.join(module_lines)
if 'merged_any = True' in module_str:
    # Find the one in selection_sort
    idx = module_str.rfind('merged_any = True')  # Use rfind to get the one in selection_sort
    snippet = module_str[idx-200:idx+300]
    print("Module version around 'merged_any = True':")
    lines = snippet.split('\n')
    for line in lines[-5:]:
        print(f"   {line}")

