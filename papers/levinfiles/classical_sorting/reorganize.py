"""Reorganize the classical_sorting folder structure."""

import os
import shutil
from pathlib import Path

# Define the reorganization plan
REORGANIZATION = {
    'tests/': [
        # Core test files
        'test_implementation.py',
        'test_notebook_experiments.py',
        'test_frozen_dynamics.py',
        'test_mixed_fixed.py',
        'test_updated_module.py',
        'test_working_version.py',
        'test_n10.py',

        # Selection sort tests
        'test_selection_approaches.py',
        'test_selection_continuous.py',
        'test_selection_correct.py',
        'test_selection_directional.py',
        'test_selection_exact_spec.py',
        'test_selection_final.py',
        'test_selection_find_slot.py',
        'test_selection_fixed.py',
        'test_selection_full_groups.py',
        'test_selection_inverted.py',
        'test_selection_no_reset.py',
        'test_selection_own_position.py',
        'test_selection_persistent.py',
        'test_selection_reset_both.py',
        'test_selection_reset_displaced.py',
        'test_selection_smart_reset.py',
        'test_selection_threshold.py',
        'test_selection_with_groups.py',
        'test_selection_with_reset.py',

        # Threading tests
        'test_modern_threaded.py',
        'test_simple_thread.py',
        'test_debug_thread.py',
        'test_trace_swaps.py',

        # Other tests
        'test_after_merge.py',
        'test_array_state.py',
        'test_debug_groups.py',
        'test_debug_selection.py',
        'test_direct_import.py',
        'test_module_selection.py',
        'test_quick_selection.py',

        # Insertion sort diagnostics
        'test_insertion_frozen_positions.py',
        'test_insertion_no_frozen.py',
        'test_insertion_stuck.py',
        'test_fix_n20.py',

        # Validation
        'validate_experiments.py',
    ],

    'tests/diagnostics/': [
        'debug_312.py',
        'debug_groups.py',
        'debug_groups_detailed.py',
        'debug_selection.py',
        'debug_selection_verbose.py',
        'diagnose_insertion_n20.py',
        'analyze_stopping_points.py',
        'compare_implementations.py',
        'detailed_comparison.py',
        'trace_selection_manual.py',
    ],

    'scripts/': [
        'add_experiment6.py',
        'create_clean_notebook.py',
        'rebuild_notebook.py',
        'fix_cell17.py',
        'fix_cell17_frozen_pos0.py',
        'fix_cell17_seed.py',
        'check_imports.py',
        'check_imports_simple.py',
        'check_notebook_detailed.py',
        'check_notebook_structure.py',
        'verify_components.py',
        'verify_notebook.py',
        'verify_notebook_imports.py',
        'verify_seed123.py',
    ],

    'docs/': [
        'AUTHOR_INQUIRY_SELECTION_SORT.md',
        'EXPERIMENT_PLAN.md',
        'EXPERIMENT6_ADDED.md',
        'REFERENCE_README.md',
        'replication_summary.md',
        '2401.05375v1.pdf',
        'INSERTION_SORT_FIX.md',
    ],
}

# Files to keep in root (in addition to directories)
KEEP_IN_ROOT = [
    'morphogenesis_experiments.ipynb',
    'morphogenesis_experiment.ipynb',  # Old version
    'validation_results.json',
    'validation_output.log',
]

def reorganize():
    """Perform the reorganization."""
    base_dir = Path('.')

    print("Classical Sorting Folder Reorganization")
    print("=" * 70)

    # Create new directories
    new_dirs = ['tests', 'tests/diagnostics', 'scripts', 'docs']
    for dir_name in new_dirs:
        dir_path = base_dir / dir_name
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
            print(f"Created directory: {dir_name}/")

    print()

    # Move files
    moved_count = 0
    for target_dir, files in REORGANIZATION.items():
        target_path = base_dir / target_dir
        print(f"\nMoving files to {target_dir}:")

        for filename in files:
            source = base_dir / filename
            if source.exists():
                destination = target_path / filename
                shutil.move(str(source), str(destination))
                print(f"  {filename}")
                moved_count += 1
            else:
                print(f"  SKIP (not found): {filename}")

    print()
    print("=" * 70)
    print(f"Reorganization complete: {moved_count} files moved")
    print()

    # Show new structure
    print("New structure:")
    print("=" * 70)

    for item in sorted(base_dir.iterdir()):
        if item.is_dir() and item.name not in ['.git', '__pycache__', '.ipynb_checkpoints']:
            print(f"  {item.name}/")
            # Count files in directory
            files = list(item.rglob('*'))
            file_count = sum(1 for f in files if f.is_file())
            print(f"    ({file_count} files)")

    print()
    print("Root files:")
    for item in sorted(base_dir.iterdir()):
        if item.is_file():
            print(f"  {item.name}")

    print()
    print("=" * 70)
    print("DONE")

if __name__ == "__main__":
    reorganize()
