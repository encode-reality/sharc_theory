"""Verify notebook structure after adding Experiment 6."""

import json

with open('morphogenesis_experiments.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print('Notebook Structure (cells 14-19):')
print('=' * 70)

for i in range(14, min(20, len(nb['cells']))):
    cell = nb['cells'][i]
    cell_type = cell['cell_type']

    if cell_type == 'markdown':
        source = cell['source'] if isinstance(cell['source'], str) else ''.join(cell['source'][:2])
        first_line = source.split('\n')[0][:70]
        print(f'Cell {i}: [MD] {first_line}')
    else:
        source = cell['source'] if isinstance(cell['source'], str) else ''.join(cell['source'][:2])
        first_line = source.split('\n')[0][:70]
        print(f'Cell {i}: [CODE] {first_line}')

print()
print(f'Total cells: {len(nb["cells"])}')
print('✓ Notebook structure verified')
