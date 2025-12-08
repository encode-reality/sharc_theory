# Master Plan: Morphogenesis Sorting Algorithms Experiment

**Research Paper**: Zhang, T., Goldstein, A., Levin, M. (2024). *Classical Sorting Algorithms as a Model of Morphogenesis*

**Purpose**: This document serves as the comprehensive roadmap and external memory for implementing an interactive Jupyter notebook that guides users through the experiments demonstrating emergent competencies in sorting algorithms.

---

## Core Theoretical Framework

### Main Assertions of the Paper

1. **Biological Analogy**: Morphogenesis (organs arranging along body axis) can be modeled as a sorting problem
2. **Distributed Intelligence**: Cell-view (agent-based) algorithms show competencies not explicitly programmed
3. **Error Tolerance**: Cell-view sorts handle "damaged" (frozen) cells better than traditional algorithms
4. **Delayed Gratification**: Algorithms can temporarily move away from goals to solve problems
5. **Emergent Aggregation**: Mixed algotypes spontaneously cluster despite no explicit mechanism
6. **Basal Cognition**: Simple, deterministic systems exhibit problem-solving abilities

### Key Concepts

- **Algotype**: The behavioral algorithm a cell follows (bubble, insertion, or selection)
- **Cell-View**: Distributed, agent-based implementation where each element decides its own moves
- **Frozen Cells**: Elements that cannot move (modeling damaged biological tissue)
  - **Movable**: Can be moved by others but cannot initiate moves
  - **Immovable**: Completely fixed in place
- **Sortedness**: Percentage of cell pairs in correct order
- **Delayed Gratification (DG)**: Ratio of gain after temporary setback
- **Aggregation Value**: Percentage of cells with same-algotype neighbors

---

## Module Architecture

```
modules/
├── core.py              # Cell, StepCounter, Probe data structures
├── metrics.py           # All measurement functions
├── traditional_sorts.py # Top-down sorting algorithms
├── cell_view_sorts.py   # Distributed sorting algorithms
├── experiments.py       # Experiment runners and harnesses
├── visualization.py     # All plotting functions
└── statistical.py       # Statistical analysis (Z-tests, etc.)
```

### Module Responsibilities

#### core.py
- `Cell` dataclass: value, algotype, frozen_type, direction
- `StepCounter`: comparisons, swaps, total
- `Probe`: Records experiment state at each step
- `FrozenType` literal: "active", "movable", "immovable"
- `Algotype` literal: "bubble", "insertion", "selection"

#### metrics.py
- `monotonicity_error(values)`: Count violations of order
- `sortedness(values)`: Percentage in correct order
- `compute_delayed_gratification(sortedness_series)`: DG metric
- `aggregation_value(algotypes)`: Clustering metric

#### traditional_sorts.py
- `bubble_sort(arr)`: Returns (sorted, steps, history)
- `insertion_sort(arr)`: Returns (sorted, steps, history)
- `selection_sort(arr)`: Returns (sorted, steps, history)

#### cell_view_sorts.py
- `bubble_sort(values, frozen_indices)`: Cell-view bubble
- `insertion_sort(values, frozen_indices)`: Cell-view insertion
- `selection_sort(values, frozen_indices)`: Cell-view selection
- `mixed_algotype_sort(algotypes, values, ...)`: Chimeric arrays

#### experiments.py
- `run_experiment(config)`: Generic experiment runner
- `run_efficiency_comparison()`: Fig 4
- `run_frozen_cell_experiments()`: Fig 5
- `run_delayed_gratification()`: Figs 6-7
- `run_mixed_algotypes()`: Fig 8
- `run_opposite_goals()`: Fig 9

#### visualization.py
- `plot_trajectories(results, title)`: Fig 3 style
- `plot_efficiency_bars(data)`: Fig 4 style
- `plot_error_tolerance(data)`: Fig 5 style
- `plot_dg_comparison(data)`: Fig 7 style
- `plot_aggregation(data)`: Fig 8 style

#### statistical.py
- `z_test(sample1, sample2)`: Returns z-statistic, p-value
- `t_test(sample1, sample2)`: Returns t-statistic, p-value
- `summarize_stats(data)`: Mean, std, confidence intervals

---

## Experiment Roadmap

### Experiment 1: Basic Sorting Trajectories (Figure 3)
**Goal**: Show that cell-view algorithms work and visualize their paths through "sortedness space"

**Parameters**:
- N = 100 cells
- 100 repetitions
- No frozen cells
- No duplicate values

**What to show**:
- Sortedness vs swap steps for all 100 runs
- Compare traditional vs cell-view for each algorithm type

**Key Finding**: Both work, but cell-view shows different trajectories

---

### Experiment 2: Efficiency Comparison (Figure 4)
**Goal**: Determine if cell-view algorithms are more or less efficient

**Metrics**:
- Swap steps only (Panel A)
- Total steps = comparisons + swaps (Panel B)

**Key Findings**:
- Bubble & Insertion: Cell-view MORE efficient when counting total steps
- Selection: Cell-view LESS efficient
- Reason: Cell-view stops comparing once in position

---

### Experiment 3: Error Tolerance - Frozen Cells (Figure 5)
**Goal**: Test robustness to damaged components

**Conditions**:
- Frozen cells: 0, 1, 2, 3
- Two types: movable vs immovable
- Measure final monotonicity error (lower = better tolerance)

**Key Findings**:
- Cell-view algorithms handle frozen cells better
- Movable frozen: Bubble best
- Immovable frozen: Selection best

---

### Experiment 4: Delayed Gratification (Figures 6-7)
**Goal**: Detect ability to temporarily worsen to achieve later gains

**Method**:
- Track sortedness trajectory
- Find episodes where sortedness decreases then increases
- Calculate DG = (gain after) / (loss before)
- Compare DG vs number of frozen cells

**Key Findings**:
- ALL algorithms show DG
- Bubble & Insertion: DG increases with more frozen cells (context-sensitive!)
- Selection: No clear trend
- This is emergent - not explicitly programmed

---

### Experiment 5: Mixed Algotypes - Aggregation (Figure 8)
**Goal**: Study chimeric arrays with cells following different algorithms

**Conditions**:
- Mix two algotypes 50/50
- Measure aggregation value over time
- Try with/without duplicate values

**Key Findings**:
- **Unexpected aggregation occurs** - cells cluster by algotype
- Starts at 50%, peaks at ~60-70%, returns to 50%
- With duplicates: aggregation persists to end
- No explicit mechanism for this in algorithms!

---

### Experiment 6: Opposite Goals (Figure 9)
**Goal**: What happens when cells have conflicting objectives?

**Setup**:
- Mix algotypes where one sorts increasing, other decreasing
- Track sortedness and aggregation until equilibrium

**Key Findings**:
- System reaches stable equilibrium (not perfect sort)
- Aggregation values increase (cells separate by goal)
- Bubble "wins" most strongly

---

## Notebook Structure (Section by Section)

### Section 1: The Biological Question
**Type**: Pure markdown, images

**Content**:
- What is morphogenesis?
- Image: tadpole development
- The puzzle: How do cells "know" where to go?
- Analogy: organs = numbers, body axis = sorted array
- Question: Can simple sorting rules produce "intelligent" behavior?

**No code**

---

### Section 2: Key Concepts
**Type**: Markdown + simple diagrams

**Content**:
- Traditional vs Cell-View (diagram showing difference)
- The Algotype concept
- What are "frozen cells"?
- Problem: Traditional algorithms assume reliable hardware
- Solution: Study error tolerance and emergent behaviors

**Minimal code**: Just imports

```python
import sys
sys.path.append('./modules')
from core import Cell, FrozenType, Algotype
import experiments
```

---

### Section 3: Experiment 1 - Do Cell-View Algorithms Work?
**Type**: Markdown explanation + hidden code + visualization

**Structure**:
1. **What we're testing**: Can distributed cells self-organize?
2. **Why it matters**: Biology has no central controller
3. **The experiment**: Run 100 sorts, track sortedness
4. **Code** (one line): `results = experiments.run_trajectories()`
5. **Visualization**: Trajectories plot
6. **Interpretation**: Yes, they work! Notice the different paths...

---

### Section 4: Experiment 2 - Efficiency
**Structure**:
1. **Question**: Is distributed control wasteful?
2. **Biological context**: Cells must sense AND act
3. **Code**: `results = experiments.run_efficiency_comparison()`
4. **Plots**: Bar charts with error bars
5. **Finding**: Surprisingly, cell-view can be MORE efficient!
6. **Why**: Cells stop when satisfied vs. controller scans entire array

---

### Section 5: Experiment 3 - Damaged Cells
**Structure**:
1. **Motivation**: Biology deals with damage constantly
2. **The perturbation**: Some cells can't move
3. **Two scenarios**: Movable vs immovable
4. **Code**: `results = experiments.run_frozen_cell_tests()`
5. **Plots**: Error bars for 0,1,2,3 frozen cells
6. **Finding**: Cell-view is MORE robust!
7. **Biological insight**: Distributed systems handle failure better

---

### Section 6: Experiment 4 - Problem Solving
**Structure**:
1. **Concept**: Delayed gratification (William James' magnets)
2. **Question**: Can simple algorithms "go around" obstacles?
3. **Measurement**: Sortedness decreases before increasing
4. **Code**: `results = experiments.run_delayed_gratification()`
5. **Plots**: DG value vs frozen cell count
6. **Finding**: DG INCREASES with obstacles for Bubble/Insertion!
7. **Significance**: Context-sensitive problem-solving, not random
8. **No explicit encoding**: Algorithms don't "know" about DG

---

### Section 7: Experiment 5 - Chimeric Arrays
**Structure**:
1. **Biological analog**: Mixing cells from different species
2. **Setup**: 50% bubble, 50% selection (for example)
3. **Measurement**: Do same types cluster?
4. **Prediction**: No mechanism for this, should stay random
5. **Code**: `results = experiments.run_mixed_algotypes()`
6. **Plots**: Aggregation value over time
7. **Finding**: UNEXPECTED aggregation! Peaks at 60-70%
8. **With duplicates**: Clustering persists to end
9. **Implication**: Emergent "preference" for similar neighbors

---

### Section 8: Experiment 6 - Conflicting Goals
**Structure**:
1. **Scenario**: What if cells want different morphologies?
2. **Setup**: Half sort ↑, half sort ↓
3. **Code**: `results = experiments.run_opposite_goals()`
4. **Plots**: Sortedness and aggregation vs time
5. **Finding**: Stable equilibrium (not chaos, not perfect)
6. **Biological relevance**: Chimeric organisms might reach compromise states

---

### Section 9: Synthesis - What Did We Learn?
**Type**: Pure markdown, no code

**Content**:
1. **Emergent Competencies Observed**:
   - Error tolerance
   - Delayed gratification (problem-solving)
   - Spontaneous aggregation
   - Conflict resolution

2. **None explicitly programmed**: These arose from algorithm dynamics

3. **Basal Intelligence**: Even simple, deterministic, fully-known systems surprise us

4. **Implications**:
   - For biology: Cells may have more problem-solving capacity than thought
   - For engineering: Distributed systems offer robustness
   - For AI: Agency might emerge at lower complexity than assumed

5. **The broader question**: If sorting algorithms can show "intelligence," what else might we be missing in systems we think we understand?

---

## Implementation Checklist

### Phase 1: Core Infrastructure
- [ ] Create modules directory
- [ ] Implement core.py (Cell, StepCounter, etc.)
- [ ] Implement metrics.py (all measurement functions)
- [ ] Test metrics independently

### Phase 2: Sorting Algorithms
- [ ] Implement traditional_sorts.py (3 algorithms)
- [ ] Implement cell_view_sorts.py (3 algorithms)
- [ ] Test: verify traditional sorts produce correct output
- [ ] Test: verify cell-view sorts produce correct output

### Phase 3: Experiments
- [ ] Implement experiments.py harness
- [ ] Test each experiment type individually
- [ ] Verify reproducibility with random seeds

### Phase 4: Visualization
- [ ] Implement visualization.py (all plot types)
- [ ] Test plots with sample data
- [ ] Ensure matplotlib styling is clear

### Phase 5: Statistical Analysis
- [ ] Implement statistical.py (z-test, t-test)
- [ ] Verify statistical calculations

### Phase 6: Notebook
- [ ] Create notebook structure (all sections)
- [ ] Write all markdown explanations
- [ ] Add simple function calls (hiding complexity)
- [ ] Generate all visualizations
- [ ] Add interpretive text after each result

### Phase 7: Testing & Polish
- [ ] Run all experiments end-to-end
- [ ] Verify all results match paper's findings
- [ ] Check for typos and clarity
- [ ] Add cross-references to this plan document

---

## Expected Outcomes

### Quantitative Results to Reproduce

From the paper:

**Efficiency** (Figure 4):
- Bubble: Traditional vs Cell-view swap steps: ~2450 vs ~2450 (Z=0.73, p=0.47)
- Bubble: Traditional vs Cell-view total steps: ~7500 vs ~5000 (Z=-68.96, p<<0.01)
- Selection: Cell-view takes 11x more swaps than traditional

**Error Tolerance** (Figure 5):
- With 3 movable frozen cells:
  - Cell-view Bubble: 2.64 error
  - Cell-view Selection: 13.24 error
- Cell-view always < Traditional error

**Delayed Gratification** (Figure 7):
- Bubble: DG increases from 0.24 (0 frozen) to 0.37 (3 frozen)
- Insertion: DG increases from 1.1 to 1.19
- Selection: No clear trend

**Aggregation** (Figure 8):
- Bubble-Selection mix: Peak aggregation 0.72
- Bubble-Insertion mix: Peak aggregation 0.65
- All start and end at 0.5

---

## Troubleshooting Guide

### Common Issues

**Problem**: Sortedness calculations don't match expected values
- **Check**: Are you using pairs of adjacent elements only?
- **Fix**: `correct_pairs / (n-1)` not `/ n`

**Problem**: Cell-view sorts never terminate
- **Check**: Is swap detection working correctly?
- **Fix**: Ensure `swapped` flag is properly reset each timestep

**Problem**: Frozen cells being moved when they shouldn't
- **Check**: Are you checking both `can_initiate_move` AND `can_be_moved`?
- **Fix**: Immovable cells should return False for both

**Problem**: Aggregation value not showing peak
- **Check**: Are you calculating it at every timestep, not just at swaps?
- **Fix**: Aggregation is computed per timestep, not per swap

**Problem**: Statistical tests give different p-values
- **Check**: Are random seeds set consistently?
- **Fix**: Use `set_experiment_seed(GLOBAL_SEED, rep)` at start of each repeat

---

## Quick Reference: Key Formulas

**Sortedness**:
```
S = (number of adjacent pairs in order) / (n - 1) * 100
```

**Monotonicity Error**:
```
E = count(i where arr[i] > arr[i+1])
```

**Delayed Gratification**:
```
For each drop-then-rise episode:
  DG_episode = Δsortedness_rise / Δsortedness_drop
DG_total = sum(DG_episode)
```

**Aggregation Value**:
```
A = (cells with all neighbors of same algotype) / (total cells) * 100
```

---

## Cross-References

### Paper Figures → Notebook Sections

- Figure 3 → Section 3 (Trajectories)
- Figure 4 → Section 4 (Efficiency)
- Figure 5 → Section 5 (Frozen Cells)
- Figures 6-7 → Section 6 (Delayed Gratification)
- Figure 8 → Section 7 (Mixed Algotypes)
- Figure 9 → Section 8 (Opposite Goals)

### Key Assertions → Experiments

- "Cell-view more robust" → Experiments 3, 5
- "Delayed gratification exists" → Experiment 4
- "Unexpected aggregation" → Experiment 5
- "Can handle conflict" → Experiment 6

---

**Last Updated**: Initial creation
**Status**: Ready for implementation
**Next Steps**: Begin Phase 1 - Core Infrastructure
