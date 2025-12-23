import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
import sys
import os
print('Current directory:', os.getcwd())
print('Python path:', sys.path[:3])
print()

# Try importing modules
try:
    from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort, mixed_algotype_sort
    print('✓ cell_view_sorts imports work')
except Exception as e:
    print('✗ cell_view_sorts error:', e)

try:
    from modules.metrics import sortedness
    print('✓ metrics imports work')
except Exception as e:
    print('✗ metrics error:', e)

try:
    from modules.core import Cell, StepCounter
    print('✓ core imports work')
except Exception as e:
    print('✗ core error:', e)

try:
    from modules.visualization import plot_sorting_progress
    print('✓ visualization imports work')
except Exception as e:
    print('✗ visualization error:', e)

try:
    from modules.experiments import compare_algorithms
    print('✓ experiments imports work')
except Exception as e:
    print('✗ experiments error:', e)
