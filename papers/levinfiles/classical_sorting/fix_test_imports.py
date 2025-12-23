"""Fix imports in all test files after reorganization."""

import os
from pathlib import Path

# Import fix to add at the top of files
IMPORT_FIX = """import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

"""

IMPORT_FIX_DIAGNOSTICS = """import sys
from pathlib import Path
# Add grandparent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

"""

IMPORT_FIX_SCRIPTS = """import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

"""

def fix_file_imports(file_path, import_fix):
    """Add import fix to a file if not already present."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already has the fix
    if 'sys.path.insert(0' in content or '__file__).parent.parent' in content:
        return False

    # Check if it imports from modules
    if 'from modules' not in content and 'import modules' not in content:
        return False

    # Find where to insert (after docstring/comments, before first import)
    lines = content.split('\n')
    insert_pos = 0

    # Skip docstring if present
    in_docstring = False
    for i, line in enumerate(lines):
        stripped = line.strip()

        # Track docstrings
        if stripped.startswith('"""') or stripped.startswith("'''"):
            if in_docstring:
                in_docstring = False
                insert_pos = i + 1
            else:
                in_docstring = True
            continue

        if in_docstring:
            continue

        # Skip comments
        if stripped.startswith('#'):
            insert_pos = i + 1
            continue

        # Stop at first import or code
        if stripped.startswith('import ') or stripped.startswith('from '):
            insert_pos = i
            break
        elif stripped and not stripped.startswith('#'):
            insert_pos = i
            break

    # Insert the fix
    lines.insert(insert_pos, import_fix.rstrip())
    new_content = '\n'.join(lines)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    """Fix imports in all relevant files."""
    base = Path('.')

    fixed_count = 0

    # Fix test files
    tests_dir = base / 'tests'
    if tests_dir.exists():
        print("Fixing test files...")
        for file_path in tests_dir.glob('*.py'):
            if file_path.name == '__init__.py':
                continue
            if fix_file_imports(file_path, IMPORT_FIX):
                print(f"  Fixed: {file_path.name}")
                fixed_count += 1

    # Fix diagnostic files
    diag_dir = base / 'tests' / 'diagnostics'
    if diag_dir.exists():
        print("\nFixing diagnostic files...")
        for file_path in diag_dir.glob('*.py'):
            if file_path.name == '__init__.py':
                continue
            if fix_file_imports(file_path, IMPORT_FIX_DIAGNOSTICS):
                print(f"  Fixed: {file_path.name}")
                fixed_count += 1

    # Fix script files
    scripts_dir = base / 'scripts'
    if scripts_dir.exists():
        print("\nFixing script files...")
        for file_path in scripts_dir.glob('*.py'):
            if file_path.name == '__init__.py':
                continue
            if fix_file_imports(file_path, IMPORT_FIX_SCRIPTS):
                print(f"  Fixed: {file_path.name}")
                fixed_count += 1

    print()
    print("=" * 70)
    print(f"Fixed {fixed_count} files")

if __name__ == "__main__":
    main()
