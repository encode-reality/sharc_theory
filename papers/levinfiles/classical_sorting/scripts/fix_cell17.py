"""Fix Cell 17 colors dictionary issue."""

import json

# Read notebook
with open('morphogenesis_experiments.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Get Cell 17 source
cell17 = nb['cells'][17]
source = ''.join(cell17['source']) if isinstance(cell17['source'], list) else cell17['source']

# Replace the plotting section to define colors locally
old_plot_code = """# Visualize the dynamics
print("Creating visualization...")
fig, ax = plt.subplots(figsize=(12, 6))

for name, data in dynamics_results.items():
    history = data['history']
    if len(history) > 0:
        ax.plot(range(len(history)), history,
               label=name, linewidth=2, color=colors[name], alpha=0.8)"""

new_plot_code = """# Visualize the dynamics
print("Creating visualization...")
fig, ax = plt.subplots(figsize=(12, 6))

# Define colors for this experiment
dynamics_colors = {
    'Bubble Sort': '#1f77b4',
    'Insertion Sort': '#ff7f0e',
    'Selection Sort': '#2ca02c'
}

for name, data in dynamics_results.items():
    history = data['history']
    if len(history) > 0:
        ax.plot(range(len(history)), history,
               label=name, linewidth=2, color=dynamics_colors[name], alpha=0.8)"""

# Replace in source
updated_source = source.replace(old_plot_code, new_plot_code)

# Update cell
cell17['source'] = updated_source

# Write back
with open('morphogenesis_experiments.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("SUCCESS: Fixed Cell 17 colors dictionary")
print("Added local 'dynamics_colors' dictionary with full algorithm names")
