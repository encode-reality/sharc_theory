"""Check notebook cell structure."""
import json

with open('morphogenesis_experiments.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print('Notebook Cell Structure:')
print('='*70)
for i, cell in enumerate(nb['cells']):
    cell_type = cell['cell_type']
    if cell_type == 'markdown':
        # Get first line as title
        source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        first_line = source.split('\n')[0][:70]
        print(f'{i:2d}. [MD]   {first_line}')
    else:
        source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        first_line = source.split('\n')[0][:70]
        print(f'{i:2d}. [CODE] {first_line}')
