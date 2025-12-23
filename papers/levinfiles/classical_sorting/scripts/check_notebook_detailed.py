"""Check notebook cell structure in detail."""
import json

with open('morphogenesis_experiments.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print('Notebook Cell Structure (Detailed):')
print('='*80)
for i, cell in enumerate(nb['cells']):
    cell_type = cell['cell_type']
    source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    lines = source.split('\n')

    # Find header line
    header = ""
    for line in lines[:5]:  # Check first 5 lines
        if line.startswith('##'):
            header = line
            break

    if not header and lines:
        header = lines[0][:80]

    print(f'\nCell {i:2d} [{cell_type:8s}]: {header}')
    if i in [8, 9, 10, 11, 12, 13]:  # Show more detail for problem cells
        print(f'  First 3 lines:')
        for j, line in enumerate(lines[:3]):
            if line.strip():
                print(f'    {line[:76]}')
