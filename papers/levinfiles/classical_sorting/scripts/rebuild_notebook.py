"""Rebuild notebook with correct cell structure."""
import json
import shutil
from datetime import datetime

# Backup original
backup_name = f'morphogenesis_experiments_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.ipynb'
shutil.copy('morphogenesis_experiments.ipynb', backup_name)
print(f"Created backup: {backup_name}")

# Read current notebook
with open('morphogenesis_experiments.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Extract cells we need
cells = nb['cells']

# Build correct structure
new_cells = []

# Keep cells 0-2 (intro, imports, strategies)
new_cells.extend(cells[0:3])

# Keep cells 3-4 (Experiment 1)
new_cells.extend(cells[3:5])

# Keep cells 5-6 (Experiment 2 header + visualization code)
new_cells.extend(cells[5:7])

# Add implications AFTER visualization (currently cell 8, but should be after cell 6)
new_cells.append(cells[8])  # The implications cell

# Now Experiment 3
new_cells.append(cells[7])  # Experiment 3 header

# ADD MISSING Experiment 3 CODE
exp3_code = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Test different array sizes\n",
        "array_sizes = [5, 10, 15, 20]\n",
        "num_trials = 10  # Multiple trials for averaging\n",
        "\n",
        "comparison_results = {\n",
        "    'Bubble': {'sizes': [], 'avg_swaps': [], 'avg_comparisons': []},\n",
        "    'Insertion': {'sizes': [], 'avg_swaps': [], 'avg_comparisons': []},\n",
        "    'Selection': {'sizes': [], 'avg_swaps': [], 'avg_comparisons': []}\n",
        "}\n",
        "\n",
        "print(\"Running comparison across array sizes...\")\n",
        "print(\"=\" * 70)\n",
        "\n",
        "for size in array_sizes:\n",
        "    print(f\"\\nArray size: {size}\")\n",
        "    \n",
        "    # Run multiple trials\n",
        "    trial_results = {'Bubble': [], 'Insertion': [], 'Selection': []}\n",
        "    \n",
        "    for trial in range(num_trials):\n",
        "        # Generate random array\n",
        "        test_arr = list(np.random.randint(1, 100, size=size))\n",
        "        \n",
        "        # Test each algorithm\n",
        "        _, steps_b, _ = bubble_sort(test_arr.copy())\n",
        "        _, steps_i, _ = insertion_sort(test_arr.copy())\n",
        "        _, steps_s, _ = selection_sort(test_arr.copy())\n",
        "        \n",
        "        trial_results['Bubble'].append(steps_b)\n",
        "        trial_results['Insertion'].append(steps_i)\n",
        "        trial_results['Selection'].append(steps_s)\n",
        "    \n",
        "    # Calculate averages\n",
        "    for algo_name, algo_key in [('Bubble Sort', 'Bubble'), \n",
        "                                  ('Insertion Sort', 'Insertion'),\n",
        "                                  ('Selection Sort', 'Selection')]:\n",
        "        avg_swaps = np.mean([s.swaps for s in trial_results[algo_key]])\n",
        "        avg_comps = np.mean([s.comparisons for s in trial_results[algo_key]])\n",
        "        \n",
        "        comparison_results[algo_key]['sizes'].append(size)\n",
        "        comparison_results[algo_key]['avg_swaps'].append(avg_swaps)\n",
        "        comparison_results[algo_key]['avg_comparisons'].append(avg_comps)\n",
        "        \n",
        "        print(f\"  {algo_name:15s} - Avg swaps: {avg_swaps:7.1f}, Avg comparisons: {avg_comps:7.1f}\")\n",
        "\n",
        "print(\"\\n\" + \"=\" * 70)\n",
        "print(\"✓ Comparison complete\")"
    ]
}
new_cells.append(exp3_code)

# Add Experiment 3 plotting (currently cell 10)
new_cells.append(cells[10])

# Now Experiment 4 - use cell 9 (the one WITH motivation, not cell 11 duplicate)
new_cells.append(cells[9])

# Add Experiment 4 code and plotting (cells 13, 14)
new_cells.extend(cells[13:15])

# Add Experiment 4 implications (need to create this)
# For now, skip - we can add later

# Add Experiment 5 (cells 12, 17, 18 - header, code, plotting)
new_cells.append(cells[12])  # Experiment 5 header with motivation
new_cells.extend(cells[17:19])  # Code and plotting

# Add Experiment 5 implications (would be a new cell - skip for now)

# Add Summary & Synthesis (cell 15)
new_cells.append(cells[15])

# Add References (cell 16)
new_cells.append(cells[16])

# Update notebook
nb['cells'] = new_cells

# Write new notebook
with open('morphogenesis_experiments.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"\nPASS: Notebook rebuilt with {len(new_cells)} cells (was {len(cells)} cells)")
print("PASS: Fixed cell ordering")
print("PASS: Added missing Experiment 3 code")
print("PASS: Removed duplicate headers")
print("\nNext steps:")
print("1. Open notebook in VSCode/Jupyter")
print("2. Kernel → Restart & Clear Output")
print("3. Run All Cells")
print("4. Verify Selection Sort shows 100% sortedness")
