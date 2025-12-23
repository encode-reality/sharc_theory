"""Add Experiment 6 (Frozen Cell Dynamics) to the notebook."""

import json

# Read the current notebook
with open('morphogenesis_experiments.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Experiment 6 markdown header
exp6_header = """---

## Experiment 6: Sortedness Dynamics with Frozen Cells

### Motivation: Understanding Recovery Trajectories

In Experiment 4, we measured **final sortedness** at different damage levels. But this endpoint measurement doesn't reveal **how** the system reaches partial organization—the dynamics of the recovery process itself.

**Key Questions:**
1. **Do algorithms follow different paths** to reach similar endpoints?
2. **Is progress smooth or punctuated** by plateaus and breakthroughs?
3. **Can we observe "getting stuck"** when frozen cells block critical paths?

### The Experiment: Tracking Sortedness Over Time

We fix the frozen cell percentage at 10% and track sortedness after each swap operation:

- **Frozen cells** are randomly positioned (immovable type)
- **Three algorithms** attempt to sort the same damaged array
- **Progress is measured** continuously throughout sorting
- **Comparison reveals** which strategies better navigate obstacles

This experiment reveals:
- Whether algorithms get stuck in local minima or maintain steady progress
- How many swaps are needed to reach different sortedness thresholds
- Strategic differences in handling obstacles (route around vs. get blocked)

---

### Biological Analogy: Wound Healing Trajectories

This models **regeneration dynamics** rather than just regeneration outcomes:
- Some organisms heal wounds linearly; others show initial stagnation then rapid recovery
- Tracking cell migration paths reveals different strategies (direct vs. exploratory routes)
- "Getting stuck" models scar tissue formation blocking proper reorganization"""

exp6_code = """# Experiment parameters
array_size = 10
frozen_pct = 10
num_frozen = int(array_size * frozen_pct / 100)

# Create worst-case test array (reverse sorted)
test_array_dynamics = list(range(array_size, 0, -1))

# Randomly select cells to freeze
np.random.seed(42)  # For reproducibility
frozen_positions = np.random.choice(array_size, size=num_frozen, replace=False)
frozen_indices_dynamics = {int(pos): 'immovable' for pos in frozen_positions}

print("Testing Sortedness Dynamics with Frozen Cells")
print("=" * 70)
print(f"Array size: {array_size}")
print(f"Frozen cells: {frozen_pct}% ({num_frozen} cells)")
print(f"Initial array: {test_array_dynamics}")
print(f"Frozen positions: {sorted(frozen_indices_dynamics.keys())}")
print()

# Test each algorithm
dynamics_algorithms = [
    ('Bubble Sort', bubble_sort),
    ('Insertion Sort', insertion_sort),
    ('Selection Sort', selection_sort)
]

dynamics_results = {}

for name, algo_func in dynamics_algorithms:
    print(f"Testing {name}...")
    result, steps, history = algo_func(test_array_dynamics.copy(), frozen_indices=frozen_indices_dynamics)

    final_sortedness = sortedness(result)

    dynamics_results[name] = {
        'history': history,
        'final_sortedness': final_sortedness,
        'swaps': steps.swaps,
        'comparisons': steps.comparisons,
        'result': result
    }

    print(f"  Final sortedness: {final_sortedness:.1f}%")
    print(f"  Swaps: {steps.swaps:,}")
    print(f"  Comparisons: {steps.comparisons:,}")
    print(f"  History points: {len(history)}")
    print()

# Visualize the dynamics
print("Creating visualization...")
fig, ax = plt.subplots(figsize=(12, 6))

for name, data in dynamics_results.items():
    history = data['history']
    if len(history) > 0:
        ax.plot(range(len(history)), history,
               label=name, linewidth=2, color=colors[name], alpha=0.8)

ax.set_xlabel('Swap Number', fontsize=12)
ax.set_ylabel('Sortedness (%)', fontsize=12)
ax.set_title(f'Sortedness Dynamics with {frozen_pct}% Frozen Cells (N={array_size})',
            fontsize=13, fontweight='bold')
ax.legend(fontsize=11, loc='lower right')
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 105)

# Add horizontal reference lines
ax.axhline(y=100, color='gray', linestyle='--', alpha=0.5, linewidth=1)
ax.axhline(y=90, color='gray', linestyle=':', alpha=0.3, linewidth=1)

plt.tight_layout()
plt.savefig('figures/frozen_dynamics.png', dpi=150, bbox_inches='tight')
plt.show()

print("Figure saved: figures/frozen_dynamics.png")
print()

# Summary statistics
print("=" * 70)
print("Dynamics Summary:")
print("=" * 70)

for name, data in dynamics_results.items():
    history = data['history']
    if len(history) > 0:
        print(f"\\n{name}:")
        print(f"  Starting sortedness: {history[0]:.1f}%")
        print(f"  Final sortedness: {history[-1]:.1f}%")
        print(f"  Improvement: {history[-1] - history[0]:.1f}%")
        print(f"  Total swaps: {len(history)}")

        # Find when it reaches 90% (if it does)
        reached_90 = None
        for i, s in enumerate(history):
            if s >= 90.0:
                reached_90 = i
                break

        if reached_90 is not None:
            print(f"  Reached 90% sortedness at swap: {reached_90}")
        else:
            print(f"  Did not reach 90% sortedness")

print("\\n" + "=" * 70)
print("✓ Frozen cell dynamics experiment complete")"""

# Helper function to create notebook cells
def markdown_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source
    }

def code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source
    }

# Insert new cells between cell 15 and 16
cells = nb['cells']
new_cells = cells[:16] + [
    markdown_cell(exp6_header),
    code_cell(exp6_code)
] + cells[16:]

# Update notebook
nb['cells'] = new_cells

# Write updated notebook
with open('morphogenesis_experiments.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("SUCCESS: Added Experiment 6 to notebook")
print(f"Total cells: {len(new_cells)} (was {len(cells)})")
print("New experiment inserted between cells 15 and 16")
