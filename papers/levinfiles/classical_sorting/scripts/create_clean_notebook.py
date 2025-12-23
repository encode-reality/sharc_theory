import sys
from pathlib import Path
# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
"""Create clean notebook with correct structure and no outputs."""
import json

# Create clean notebook structure
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.12.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

def md_cell(source):
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

# Read content from existing cells
with open('morphogenesis_experiments_OLD.ipynb', 'r', encoding='utf-8') as f:
    old_nb = json.load(f)
    old_cells = old_nb['cells']

# Build clean notebook with correct order
cells = []

# Cell 0: Introduction
cells.append(old_cells[0])

# Cell 1: Imports
cells.append(code_cell(old_cells[1]['source']))

# Cell 2: Algorithm strategies
cells.append(old_cells[2])

# Cell 3: Experiment 1 header
cells.append(old_cells[3])

# Cell 4: Experiment 1 code
cells.append(code_cell(old_cells[4]['source']))

# Cell 5: Experiment 2 header
cells.append(old_cells[5])

# Cell 6: Experiment 2 code (visualization)
cells.append(code_cell(old_cells[6]['source']))

# Cell 7: Experiment 3 header
cells.append(old_cells[7])

# Cell 8: Experiment 3 code (array size comparison) - from cell 9
cells.append(code_cell(old_cells[9]['source']))

# Cell 9: Experiment 3 plotting - from cell 10
cells.append(code_cell(old_cells[10]['source']))

# Cell 10: Experiment 4 header - from cell 9 (the one WITH motivation)
cells.append(old_cells[13])  # This is Experiment 5 header - need to find Exp 4

# Actually let me just rebuild from scratch with correct content
# Clear and start over

cells = []

# Introduction with all the content I added
intro_md = """# Classical Sorting Algorithms as a Model of Morphogenesis

## Replication and Exploration Experiments

This notebook replicates and extends experiments from:

> Zhang, T., Goldstein, A., and Levin, M. (2024). "Classical Sorting Algorithms as a Model of Morphogenesis: self-sorting arrays reveal unexpected competencies in a minimal model of basal intelligence." *Adaptive Behavior*, DOI: 10.1177/10597123241269740

---

## Motivation: Why Study Sorting as Morphogenesis?

### The Challenge of Basal Intelligence

Traditional views assume intelligence requires complex neural architectures or sophisticated computational machinery. But biological systems—from embryonic development to wound healing—demonstrate remarkable problem-solving capabilities using simple cellular mechanisms.

**Central Question:** Can we identify minimal substrates where intelligence-like behaviors emerge without being explicitly programmed?

### Sorting as a Minimal Model

Classical sorting algorithms provide an ideal testbed because:

1. **Well-understood computational properties** - Decades of analysis provide clear baselines
2. **Simple local rules** - Each element follows basic comparison and swap operations
3. **Global emergence** - Order arises from purely local interactions
4. **Testable robustness** - We can systematically introduce failures and measure degradation

By reimagining sorting arrays as **collections of autonomous agents** (like cells in tissue), we can:
- Remove centralized control (no global coordinator)
- Test resilience to damage (frozen/dead cells)
- Explore heterogeneity (chimeric arrays with mixed strategies)
- Observe emergent problem-solving without explicit programming

---

## Key Concepts

### Basal Intelligence
Recognition that intelligence manifests in simple systems lacking explicit complex programming. These systems demonstrate:
- Memory (retaining state information)
- Decision-making (context-dependent choices)
- Problem-solving (navigating around obstacles)
- Collective computation (coordinated group behavior)

### Morphogenesis
Self-organization into ordered structures through local cell-cell interactions. In development:
- Cells don't have blueprints of final forms
- Global patterns emerge from distributed rules
- Systems self-repair after damage
- Mixed cell types cooperate toward common goals

### Cell-View Algorithms
Unlike traditional implementations with centralized loops, cell-view sorting treats each array element as an **autonomous agent**:
- Each cell makes local decisions based on neighbors
- No global controller coordinates activities
- Order emerges through distributed interactions
- Resembles biological morphogenesis more than traditional computation

---

## What We'll Explore

This notebook investigates three core questions from the paper:

1. **Can autonomous cells self-organize?** (Experiments 1-3)
   - Do pure distributed algorithms achieve sorting?
   - How do different strategies compare in efficiency?

2. **How robust are these systems?** (Experiment 4)
   - What happens when cells are "damaged" (frozen)?
   - Can the collective compensate for individual failures?

3. **Can diverse cells cooperate?** (Experiment 5)
   - Do chimeric arrays (mixed strategies) still sort?
   - What emergent behaviors arise from heterogeneity?"""

cells.append(md_cell(intro_md))

# Imports code
imports_code = """# Import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict

# Set plotting style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Import our modules
from modules.cell_view_sorts import bubble_sort, insertion_sort, selection_sort, mixed_algotype_sort
from modules.metrics import sortedness
from modules.core import Cell, StepCounter
from modules.visualization import plot_sorting_progress, plot_sortedness_comparison
from modules.experiments import (
    compare_algorithms,
    frozen_cell_experiment,
    chimeric_experiment
)

print("✓ All modules loaded successfully")"""

cells.append(code_cell(imports_code))

# Get strategies markdown from old cell 2
cells.append(old_cells[2])

# Experiment 1
cells.append(old_cells[3])  # Header
cells.append(code_cell(old_cells[4]['source']))  # Code

# Experiment 2
cells.append(old_cells[5])  # Header
cells.append(code_cell(old_cells[6]['source']))  # Visualization code

# Experiment 3
cells.append(old_cells[7])  # Header
cells.append(code_cell(old_cells[9]['source']))  # Array size comparison code
cells.append(code_cell(old_cells[10]['source']))  # Plotting code

# Experiment 4 - use the one WITH motivation
exp4_md = """---

## Experiment 4: Robustness - Frozen Cell Analysis

### Motivation: Why Test Damaged Systems?

In biological development and regeneration, **cell death and dysfunction are inevitable**:
- Random mutations cause cells to malfunction
- Environmental insults damage tissues
- Aging degrades cellular capabilities
- Injuries create regions of non-functional tissue

Yet **biological systems remain remarkably robust**. Embryos with significant cell damage often develop normally. Planaria regenerate heads even when portions of tissue are destroyed. Wound healing proceeds despite infected or dead cells at injury sites.

**Central Question:** Is this robustness a property of biology's specific mechanisms, or does it emerge more generally from **distributed computational architectures**?

### The Test: Systematic Cell Freezing

We simulate cell damage by "freezing" randomly selected cells:
- **Frozen cells** cannot initiate swaps (they can't move)
- **Frozen cells** can still be moved by neighbors (passive displacement)
- This models cells that are "damaged but not removed" from the system

By varying the percentage of frozen cells (0% to 50%), we can measure:
1. **How does sortedness degrade with increasing damage?**
2. **Do algorithms differ in their vulnerability to specific damage patterns?**
3. **Can the collective compensate for non-functional members?**

---

This models:
- **Cell death** in biological systems (permanent dysfunction)
- **Hardware failures** in distributed systems (node failures in networks)
- **Robustness** of collective intelligence (performance under partial failures)"""

cells.append(md_cell(exp4_md))
cells.append(code_cell(old_cells[14]['source']))  # Frozen cell code
cells.append(code_cell(old_cells[12]['source']))  # Plotting code

# Experiment 5
cells.append(old_cells[13])  # Header with motivation
cells.append(code_cell(old_cells[17]['source']))  # Chimeric code
cells.append(code_cell(old_cells[18]['source']))  # Plotting code

# Summary
cells.append(old_cells[15])  # Big summary

# References
cells.append(old_cells[16])

# Assign to notebook
notebook['cells'] = cells

# Write clean notebook
with open('morphogenesis_experiments.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Clean notebook created with {len(cells)} cells")
print("All outputs cleared")
print("Ready to run in VSCode/Jupyter")
