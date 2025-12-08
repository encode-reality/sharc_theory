import sys
import os
print('Current directory:', os.getcwd())
print('Python path:', sys.path[:3])
print()

try:
    from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort, mixed_algotype_sort
    print('[OK] cell_view_sorts imports work')
except Exception as e:
    print('[FAIL] cell_view_sorts error:', e)

try:
    from modules.metrics import sortedness
    print('[OK] metrics imports work')
except Exception as e:
    print('[FAIL] metrics error:', e)

try:
    from modules.core import Cell, StepCounter
    print('[OK] core imports work')
except Exception as e:
    print('[FAIL] core error:', e)

try:
    from modules.visualization import plot_sorting_progress
    print('[OK] visualization.plot_sorting_progress exists')
except Exception as e:
    print('[FAIL] visualization missing plot_sorting_progress:', e)

try:
    from modules.visualization import plot_sortedness_comparison
    print('[OK] visualization.plot_sortedness_comparison exists')
except Exception as e:
    print('[FAIL] visualization missing plot_sortedness_comparison:', e)

try:
    from modules.experiments import compare_algorithms
    print('[OK] experiments.compare_algorithms exists')
except Exception as e:
    print('[FAIL] experiments missing compare_algorithms:', e)

try:
    from modules.experiments import frozen_cell_experiment
    print('[OK] experiments.frozen_cell_experiment exists')
except Exception as e:
    print('[FAIL] experiments missing frozen_cell_experiment:', e)

try:
    from modules.experiments import chimeric_experiment
    print('[OK] experiments.chimeric_experiment exists')
except Exception as e:
    print('[FAIL] experiments missing chimeric_experiment:', e)
