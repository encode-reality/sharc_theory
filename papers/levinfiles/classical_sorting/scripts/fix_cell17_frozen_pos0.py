"""Fix Cell 17 to prevent freezing position 0 (breaks Insertion Sort)."""

import json

# Read notebook
with open('morphogenesis_experiments.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Get Cell 17
cell17 = nb['cells'][17]
source = ''.join(cell17['source']) if isinstance(cell17['source'], list) else cell17['source']

# Find and replace the frozen cell selection code
old_code = """# Randomly select cells to freeze
np.random.seed(42)  # For reproducibility
frozen_positions = np.random.choice(array_size, size=num_frozen, replace=False)
frozen_indices_dynamics = {int(pos): 'immovable' for pos in frozen_positions}"""

new_code = """# Randomly select cells to freeze (excluding position 0 for Insertion Sort compatibility)
np.random.seed(42)  # For reproducibility
available_positions = list(range(1, array_size))  # Exclude position 0
frozen_positions = np.random.choice(available_positions, size=num_frozen, replace=False)
frozen_indices_dynamics = {int(pos): 'immovable' for pos in frozen_positions}"""

if old_code in source:
    updated_source = source.replace(old_code, new_code)
    cell17['source'] = updated_source

    # Write back
    with open('morphogenesis_experiments.ipynb', 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print("SUCCESS: Fixed Cell 17 frozen cell selection")
    print("Position 0 is now excluded from freezing")
    print("This prevents Insertion Sort from getting stuck")
else:
    print("ERROR: Could not find code to replace")
    print("Cell 17 may have been modified")
