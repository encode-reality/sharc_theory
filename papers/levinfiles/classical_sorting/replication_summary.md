> Zhang, T., Goldstein, A., Levin, M. (2024). *Classical Sorting Algorithms as a Model of Morphogenesis: self-sorting arrays reveal unexpected competencies in a minimal model of basal intelligence* 

---

# Notebook: Reproducing “Classical Sorting Algorithms as a Model of Morphogenesis”

## 0. Goals

Implement and compare:

1. **Traditional** Bubble / Insertion / Selection sort
2. **Cell-view** (distributed / agent-based) versions of those sorts
3. Metrics:

   * Sortedness, Monotonicity Error
   * Efficiency (steps: comparisons + swaps)
   * Delayed Gratification (DG)
   * Aggregation for mixed Algotypes
4. Experiments corresponding to Figures 3–9:

   * Sorting trajectories
   * Efficiency comparison
   * Frozen / damaged cells
   * DG vs number of Frozen Cells
   * Mixed Algotypes with/without duplicates
   * Mixed Algotypes with opposite sorting goals

The notebook should be **self-contained** (no external repo required), but may optionally verify against the GitHub repo mentioned in the paper.

---

## 1. Environment & Global Configuration

### 1.1. Imports

Create a cell with imports:

```python
import numpy as np
import random
import math
import itertools
from dataclasses import dataclass
from typing import List, Callable, Literal, Dict, Tuple
import matplotlib.pyplot as plt
```

### 1.2. Global Settings

Create a cell with:

```python
# Reproducibility
GLOBAL_SEED = 42
random.seed(GLOBAL_SEED)
np.random.seed(GLOBAL_SEED)

# Default experiment parameters (based on paper)
N_CELLS = 100            # array length
N_REPEATS = 100          # repetitions per configuration
MAX_STEPS = 100000       # hard safety cap if needed

# Utility to enforce reproducible RNG per experiment
def set_experiment_seed(base_seed: int, experiment_idx: int):
    seed = base_seed + experiment_idx
    random.seed(seed)
    np.random.seed(seed)
```

---

## 2. Core Data Structures

### 2.1. Cell & Algotype

Define a `Cell` dataclass to encapsulate properties:

```python
Algotype = Literal["bubble", "insertion", "selection"]

FrozenType = Literal["active", "movable", "immovable"]
# active      = normal cell
# movable     = frozen cell that cannot initiate moves, but can be moved by others
# immovable   = completely fixed: cannot move or be moved

@dataclass
class Cell:
    value: int
    algotype: Algotype
    frozen_type: FrozenType = "active"
```

Array state: a simple `List[Cell]` in 1D.

---

## 3. Metrics Implementations

### 3.1. Sortedness & Monotonicity Error

Implement functions to compute:

* **Monotonicity error** (number of violations in increasing order)
* **Sortedness** = percentage of cells that obey order

Use definition from the paper (increasing order). 

```python
def monotonicity_error(values: List[int]) -> int:
    """Return number of violations of non-decreasing order."""
    errors = 0
    for i in range(len(values) - 1):
        if values[i] > values[i+1]:
            errors += 1
    return errors

def sortedness(values: List[int]) -> float:
    """
    Sortedness Value: percentage of cells that follow the designated order.
    Here we use: 100 * (number_of_pairs_in_correct_order / total_pairs).
    """
    if len(values) < 2:
        return 100.0
    correct_pairs = 0
    total_pairs = len(values) - 1
    for i in range(len(values) - 1):
        if values[i] <= values[i+1]:
            correct_pairs += 1
    return 100.0 * correct_pairs / total_pairs
```

You can later create a variant `sortedness_decreasing` if needed for “opposite goal” experiments.

### 3.2. Step Accounting

We need to track:

* `comparison_steps`: number of comparisons / reads
* `swap_steps`: number of swaps / writes
* `total_steps`: `comparison_steps + swap_steps`

Define a small helper:

```python
@dataclass
class StepCounter:
    comparisons: int = 0
    swaps: int = 0

    @property
    def total(self) -> int:
        return self.comparisons + self.swaps
```

---

## 4. Traditional Sorting Algorithms

Implement classic top-down versions for each sort.
Each function must:

* Take a list of integers
* Sort **in place**
* Return:

  * sorted list
  * `StepCounter`
  * history of `sortedness` over **swap steps** (for Figures 3 & 6)

### 4.1. Traditional Bubble Sort

```python
def traditional_bubble_sort(arr: List[int]) -> Tuple[List[int], StepCounter, List[float]]:
    a = arr[:]
    steps = StepCounter()
    sortedness_history = []

    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            steps.comparisons += 1
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                steps.swaps += 1
                swapped = True
                sortedness_history.append(sortedness(a))
    return a, steps, sortedness_history
```

### 4.2. Traditional Insertion Sort

```python
def traditional_insertion_sort(arr: List[int]) -> Tuple[List[int], StepCounter, List[float]]:
    a = arr[:]
    steps = StepCounter()
    sortedness_history = []

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            steps.comparisons += 1
            if a[j] > key:
                a[j+1] = a[j]
                steps.swaps += 1
                sortedness_history.append(sortedness(a))
                j -= 1
            else:
                break
        a[j+1] = key
    return a, steps, sortedness_history
```

### 4.3. Traditional Selection Sort

```python
def traditional_selection_sort(arr: List[int]) -> Tuple[List[int], StepCounter, List[float]]:
    a = arr[:]
    steps = StepCounter()
    sortedness_history = []

    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            steps.comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            steps.swaps += 1
            sortedness_history.append(sortedness(a))
    return a, steps, sortedness_history
```

---

## 5. Cell-View Sorting Algorithms

We simulate the “multi-threaded, parallel” behavior with **discrete time steps**:

* At each timestep:

  * Traverse cells in **random order**
  * For each cell, apply its cell-view rule
  * Respect Frozen types (movable vs immovable)
  * Count comparisons + swaps
* Stop when:

  * A full timestep results in **no swaps**, or
  * `MAX_STEPS` reached

Always record `sortedness` **after each swap** (for trajectory plots).

### 5.1. Helpers: “Move Permission” with Frozen Cells

```python
def can_initiate_move(cell: Cell) -> bool:
    return cell.frozen_type == "active"

def can_be_moved(cell: Cell) -> bool:
    # movable frozen cells can be moved by others
    return cell.frozen_type in ("active", "movable")
```

### 5.2. Cell-view Bubble Sort

Rules (increasing order) from the paper: 

* Each cell may look at **left** and **right** neighbor.
* If value < left neighbor → wants to move left (swap)
* If value > right neighbor → wants to move right (swap)

Implementation outline:

```python
def cell_view_bubble_step(cells: List[Cell], steps: StepCounter) -> Tuple[bool, List[float]]:
    """
    Perform one parallel-like timestep:
    - iterate cells in random order
    - apply bubble rules
    Returns (swapped_any, list_of_sortedness_after_each_swap).
    """
    n = len(cells)
    idx_order = list(range(n))
    random.shuffle(idx_order)

    swapped_any = False
    sortedness_traces = []

    for idx in idx_order:
        cell = cells[idx]
        if not can_initiate_move(cell):
            continue

        # Try move left
        if idx > 0:
            neighbor_left = cells[idx - 1]
            steps.comparisons += 1
            if cell.value < neighbor_left.value and can_be_moved(neighbor_left):
                cells[idx], cells[idx-1] = neighbor_left, cell
                steps.swaps += 1
                swapped_any = True
                sortedness_traces.append(sortedness([c.value for c in cells]))
                continue

        # Try move right
        if idx < n - 1:
            neighbor_right = cells[idx + 1]
            steps.comparisons += 1
            if cell.value > neighbor_right.value and can_be_moved(neighbor_right):
                cells[idx], cells[idx+1] = neighbor_right, cell
                steps.swaps += 1
                swapped_any = True
                sortedness_traces.append(sortedness([c.value for c in cells]))
    return swapped_any, sortedness_traces
```

Wrapper to sort:

```python
def cell_view_bubble_sort(
    initial_values: List[int],
    frozen_indices: Dict[int, FrozenType] | None = None
) -> Tuple[List[int], StepCounter, List[float]]:
    frozen_indices = frozen_indices or {}
    cells = [
        Cell(value=v, algotype="bubble", frozen_type=frozen_indices.get(i, "active"))
        for i, v in enumerate(initial_values)
    ]
    steps = StepCounter()
    history = []

    for t in range(MAX_STEPS):
        swapped, traces = cell_view_bubble_step(cells, steps)
        history.extend(traces)
        if not swapped:
            break

    return [c.value for c in cells], steps, history
```

### 5.3. Cell-view Insertion Sort

Rules: 

1. Each cell can **view all cells to its left**.
2. Can swap **only with left neighbor**.
3. A cell moves left if:

   * Cells to the left are already sorted
   * Its value is smaller than left neighbor.

Implement `cell_view_insertion_step` similarly:

```python
def cell_view_insertion_step(cells: List[Cell], steps: StepCounter) -> Tuple[bool, List[float]]:
    n = len(cells)
    idx_order = list(range(n))
    random.shuffle(idx_order)

    swapped_any = False
    traces = []

    values = [c.value for c in cells]

    for idx in idx_order:
        if idx == 0:
            continue

        cell = cells[idx]
        if not can_initiate_move(cell):
            continue

        # Check left side sorted
        left_values = [c.value for c in cells[:idx]]
        left_sorted = all(left_values[i] <= left_values[i+1] for i in range(len(left_values)-1))
        if not left_sorted:
            continue

        neighbor_left = cells[idx-1]
        steps.comparisons += 1
        if cell.value < neighbor_left.value and can_be_moved(neighbor_left):
            cells[idx], cells[idx-1] = neighbor_left, cell
            steps.swaps += 1
            swapped_any = True
            traces.append(sortedness([c.value for c in cells]))

    return swapped_any, traces
```

And the wrapper `cell_view_insertion_sort` analogous to `cell_view_bubble_sort`.

### 5.4. Cell-view Selection Sort

Rules: 

1. Each cell has an **ideal target position** (initially 0 for all).
2. Each cell can view and swap with the cell **at its ideal position**.
3. If a cell’s value is smaller than that occupying its ideal position, it swaps; otherwise it shifts its ideal position one step to the right.

Implementation hints:

* Track an array `ideal_positions: List[int]` parallel to cells list.
* At each timestep, for each index in random order:

  * Let `target = ideal_positions[idx]`
  * Clamp target to `[0, n-1]`
  * Compare `cells[idx]` with `cells[target]`
  * Apply swap + possible target shift.

Write:

```python
def cell_view_selection_sort(
    initial_values: List[int],
    frozen_indices: Dict[int, FrozenType] | None = None
) -> Tuple[List[int], StepCounter, List[float]]:
    frozen_indices = frozen_indices or {}
    cells = [
        Cell(value=v, algotype="selection", frozen_type=frozen_indices.get(i, "active"))
        for i, v in enumerate(initial_values)
    ]
    steps = StepCounter()
    history = []

    n = len(cells)
    ideal_positions = [0 for _ in range(n)]

    for t in range(MAX_STEPS):
        swapped_any = False
        idx_order = list(range(n))
        random.shuffle(idx_order)

        for idx in idx_order:
            cell = cells[idx]
            if not can_initiate_move(cell):
                continue

            target = ideal_positions[idx]
            target = max(0, min(n-1, target))
            neighbor = cells[target]

            steps.comparisons += 1
            if cell.value < neighbor.value and can_be_moved(neighbor):
                # swap with target
                cells[idx], cells[target] = neighbor, cell
                # also swap their ideal positions
                ideal_positions[idx], ideal_positions[target] = (
                    ideal_positions[target],
                    ideal_positions[idx],
                )
                steps.swaps += 1
                swapped_any = True
                history.append(sortedness([c.value for c in cells]))
            else:
                # shift ideal position right
                ideal_positions[idx] = min(n-1, ideal_positions[idx] + 1)

        if not swapped_any:
            break

    return [c.value for c in cells], steps, history
```

---

## 6. Experiment Harness

Create a general function to run many repetitions of an algorithm and collect statistics.

### 6.1. Experiment Runner

```python
def run_experiments(
    algo_name: str,
    variant: Literal["traditional", "cell_view"],
    n_cells: int = N_CELLS,
    n_repeats: int = N_REPEATS,
    frozen_config_factory=None,
    allow_duplicates: bool = False,
    sort_direction: Literal["increasing", "decreasing"] = "increasing",
) -> Dict:
    """
    Run n_repeats experiments and collect:
    - step counts
    - final monotonicity error
    - full histories of sortedness vs swap steps
    """
    results = {
        "comparison_steps": [],
        "swap_steps": [],
        "total_steps": [],
        "monotonicity_error": [],
        "sortedness_history": [],  # list of lists
    }

    for rep in range(n_repeats):
        set_experiment_seed(GLOBAL_SEED, rep)

        if allow_duplicates:
            # 100 cells, values 1..10 each repeated 10x
            base_vals = np.repeat(np.arange(1, 11), n_cells // 10)
            np.random.shuffle(base_vals)
            values = base_vals.tolist()
        else:
            values = list(range(1, n_cells + 1))
            random.shuffle(values)

        if sort_direction == "decreasing":
            # internally sort increasing by negating values or by reversing comparison later
            values = values  # for now keep same and adjust metric later if desired

        frozen_indices = frozen_config_factory(rep) if frozen_config_factory else {}

        if variant == "traditional":
            if algo_name == "bubble":
                final_vals, steps, history = traditional_bubble_sort(values)
            elif algo_name == "insertion":
                final_vals, steps, history = traditional_insertion_sort(values)
            else:
                final_vals, steps, history = traditional_selection_sort(values)
        else:
            if algo_name == "bubble":
                final_vals, steps, history = cell_view_bubble_sort(values, frozen_indices)
            elif algo_name == "insertion":
                final_vals, steps, history = cell_view_insertion_sort(values, frozen_indices)
            else:
                final_vals, steps, history = cell_view_selection_sort(values, frozen_indices)

        results["comparison_steps"].append(steps.comparisons)
        results["swap_steps"].append(steps.swaps)
        results["total_steps"].append(steps.total)
        results["monotonicity_error"].append(monotonicity_error(final_vals))
        results["sortedness_history"].append(history)

    return results
```

---

## 7. Experiments by Figure

Below: which functions to call and what plots to produce.

### 7.1. Figure 3 – Sorting Trajectories (State Space Paths)

For each algorithm:

* Run **traditional** and **cell-view** versions with:

  * `n_cells=100`
  * `n_repeats=100`
  * `no frozen cells`
  * `no duplicates`
* For each repetition, plot `sortedness_history` vs **swap index**.

Implementation outline:

```python
# Example for bubble sort
bubble_traditional = run_experiments("bubble", "traditional")
bubble_cellview   = run_experiments("bubble", "cell_view")

def plot_trajectories(results, title):
    plt.figure(figsize=(6,4))
    for history in results["sortedness_history"]:
        plt.plot(range(len(history)), history, alpha=0.2)
    plt.xlabel("swap steps")
    plt.ylabel("Sortedness (%)")
    plt.title(title)
    plt.ylim(0, 105)
    plt.grid(True)

plot_trajectories(bubble_traditional, "Traditional Bubble Sort")
plot_trajectories(bubble_cellview, "Cell-view Bubble Sort")
```

Repeat for Insertion and Selection.

---

### 7.2. Figure 4 – Efficiency Comparison

For each algorithm:

1. Use results from Section 7.1 where **no frozen cells**.
2. Compute:

   * Mean & std of `swap_steps`
   * Mean & std of `total_steps`
3. Plot grouped bar charts, similar to Fig 4A and 4B:

   * A: “swap steps only”
   * B: “comparisons + swaps”

Use `plt.bar` with error bars (std).

---

### 7.3. Figure 5 – Error Tolerance with Frozen Cells

You need two frozen models:

* **Movable Frozen Cells**: type `"movable"`
* **Immovable Frozen Cells**: type `"immovable"`

Implement a factory that randomly chooses which indices are frozen:

```python
def make_frozen_factory(n_frozen: int, frozen_type: FrozenType):
    def factory(rep: int) -> Dict[int, FrozenType]:
        set_experiment_seed(GLOBAL_SEED + 1000 * n_frozen, rep)
        indices = random.sample(range(N_CELLS), n_frozen)
        return {i: frozen_type for i in indices}
    return factory
```

Run experiments for `n_frozen in {0, 1, 2, 3}` and for each algorithm & variant:

```python
frozen_counts = [0, 1, 2, 3]
results_movable = {}
results_immovable = {}

for algo in ["bubble", "insertion", "selection"]:
    results_movable[algo] = {}
    results_immovable[algo] = {}
    for f in frozen_counts:
        factory_mov = make_frozen_factory(f, "movable") if f > 0 else None
        factory_imm = make_frozen_factory(f, "immovable") if f > 0 else None

        results_movable[algo][f] = {
            "traditional": run_experiments(algo, "traditional", frozen_config_factory=factory_mov),
            "cell_view": run_experiments(algo, "cell_view", frozen_config_factory=factory_mov),
        }
        results_immovable[algo][f] = {
            "traditional": run_experiments(algo, "traditional", frozen_config_factory=factory_imm),
            "cell_view": run_experiments(algo, "cell_view", frozen_config_factory=factory_imm),
        }
```

For each, compute mean **monotonicity error** and plot bar charts mimicking Figure 5.

---

### 7.4. Figures 6–7 – Delayed Gratification (DG)

#### 7.4.1. DG Metric

Define DG as in Fig 6D: 

* Find **local drops** in Sortedness over swap steps, followed by a rise.
* For each drop–rise episode:

  * `x = total consecutive increase after the minimum`
  * `y = total consecutive decrease before the increase`
  * DG contribution = `x / y`, aggregated across episodes.

Implement:

```python
def compute_delayed_gratification(sortedness_series: List[float]) -> float:
    """
    Given a per-swap sortedness series, calculate DG according to:
    DG = sum(x_i / y_i) over all episodes
    where y_i is a net drop and x_i the subsequent net gain.
    Return total DG for this run.
    """
    if len(sortedness_series) < 3:
        return 0.0

    dg_total = 0.0
    i = 0
    while i < len(sortedness_series) - 1:
        # find start of downward segment
        if sortedness_series[i+1] < sortedness_series[i]:
            start = i
            # move until we stop decreasing
            j = i + 1
            while j < len(sortedness_series) and sortedness_series[j] <= sortedness_series[j-1]:
                j += 1
            bottom = j - 1
            y = sortedness_series[start] - sortedness_series[bottom]
            # now we expect increase
            k = bottom + 1
            while k < len(sortedness_series) and sortedness_series[k] >= sortedness_series[k-1]:
                k += 1
            peak = k - 1
            x = sortedness_series[peak] - sortedness_series[bottom]
            if y > 0 and x > 0:
                dg_total += x / y
            i = peak
        else:
            i += 1
    return dg_total
```

#### 7.4.2. DG vs Frozen Cells

For each algorithm & variant & frozen count (0–3):

* Compute DG for each run and take the mean.
* Plot bars like Fig 7 A–C.

```python
def summarize_dg(results_dict):
    dg_values = []
    for history in results_dict["sortedness_history"]:
        dg_values.append(compute_delayed_gratification(history))
    return np.mean(dg_values), np.std(dg_values)
```

Then produce DG plots.

---

### 7.5. Figure 8 – Mixed Algotypes (Chimeric Arrays)

We now assign **different Algotypes** to cells in the same array.

#### 7.5.1. Aggregation Metric

Aggregation Value = fraction of cells whose immediate neighbors share the same Algotype (1D). 

Define:

```python
def aggregation_value(algotypes: List[Algotype]) -> float:
    n = len(algotypes)
    same_neighbor_count = 0
    total_neighbors = 0

    for i in range(n):
        neighbors = []
        if i > 0:
            neighbors.append(algotypes[i-1])
        if i < n-1:
            neighbors.append(algotypes[i+1])
        if not neighbors:
            continue
        total_neighbors += 1
        if all(nei == algotypes[i] for nei in neighbors):
            same_neighbor_count += 1

    return same_neighbor_count / total_neighbors if total_neighbors > 0 else 0.0
```

#### 7.5.2. Mixed Cell-View Sort (Two Algotypes)

Create a function that:

* Randomly assigns 2 Algotypes across cells with equal probability (or 3 in “all mixed” condition).
* Uses **cell-view rules according to each cell’s Algotype**.
* Records:

  * Sortedness trajectory
  * Aggregation trajectory

For each timestep:

* Capture `Sortedness` after each swap or at fixed intervals.
* After each full timestep, compute `AggregationValue` from Algotype distribution.

You can reuse previous cell-view step functions; you just have to **select behavior by cell.algotype**:

```python
def cell_view_mixed_step(
    cells: List[Cell],
    steps: StepCounter
) -> Tuple[bool, List[float]]:
    """
    One timestep where each cell applies its own algotype rules.
    Returns (swapped_any, sortedness_after_each_swap).
    """
    n = len(cells)
    idx_order = list(range(n))
    random.shuffle(idx_order)

    swapped_any = False
    traces = []

    for idx in idx_order:
        algo = cells[idx].algotype
        if algo == "bubble":
            swapped, local_traces = cell_view_bubble_step_for_single_index(cells, idx, steps)
        elif algo == "insertion":
            swapped, local_traces = cell_view_insertion_step_for_single_index(cells, idx, steps)
        else:
            swapped, local_traces = cell_view_selection_step_for_single_index(cells, idx, steps)
        if swapped:
            swapped_any = True
            traces.extend(local_traces)

    return swapped_any, traces
```

> **Note:** For simplicity, you can refactor earlier cell-view step functions into per-cell versions (`*_for_single_index`) rather than reusing the full step.

Wrapper:

```python
def run_mixed_algotype_experiment(
    algotypes: List[Algotype],
    allow_duplicates: bool = False,
    n_repeats: int = N_REPEATS
) -> Dict:
    """
    For a fixed multiset of algotypes (e.g. ["bubble", "selection"]),
    run n_repeats experiments where cells are randomly assigned among these algotypes.
    """
    results = {
        "sortedness_history": [],
        "aggregation_history": [],
        "swap_steps": [],
    }

    for rep in range(n_repeats):
        set_experiment_seed(GLOBAL_SEED + 2000, rep)

        if allow_duplicates:
            base_vals = np.repeat(np.arange(1, 11), N_CELLS // 10)
            np.random.shuffle(base_vals)
            values = base_vals.tolist()
        else:
            values = list(range(1, N_CELLS + 1))
            random.shuffle(values)

        # assign algotypes randomly from provided list
        cell_algotypes = [random.choice(algotypes) for _ in range(N_CELLS)]
        cells = [Cell(value=v, algotype=a) for v, a in zip(values, cell_algotypes)]
        steps = StepCounter()

        sortedness_trace = []
        aggregation_trace = []

        for t in range(MAX_STEPS):
            swapped, s_traces = cell_view_mixed_step(cells, steps)
            sortedness_trace.extend(s_traces)
            aggregation_trace.append(aggregation_value([c.algotype for c in cells]))
            if not swapped:
                break

        results["sortedness_history"].append(sortedness_trace)
        results["aggregation_history"].append(aggregation_trace)
        results["swap_steps"].append(steps.swaps)

    return results
```

Run for combinations:

* ["bubble", "insertion"]
* ["bubble", "selection"]
* ["insertion", "selection"]
* ["bubble", "insertion", "selection"]

Plot:

* Sortedness vs swap steps (blue).
* Aggregation Value vs normalized progress (red).

For duplicate vs non-duplicate value experiments:

* Call `run_mixed_algotype_experiment(algotypes, allow_duplicates=True/False)`
* Compare final and max Aggregation Values as in the paper.

---

### 7.6. Figure 9 – Opposite Sorting Goals

Here we mix **two Algotypes** with conflicting goals:

* Example: Bubble sorting **increasingly** vs Selection sorting **decreasingly**. 

One pragmatic way:

* Add a `direction` attribute on `Cell`: `"inc"` or `"dec"`.
* For `"dec"` cells:

  * In comparisons, **flip the inequality** (e.g., > becomes <).
  * Or equivalently, treat their `effective_value = -value`.

Implement:

```python
@dataclass
class Cell:
    value: int
    algotype: Algotype
    frozen_type: FrozenType = "active"
    direction: Literal["inc", "dec"] = "inc"
```

Update your per-cell rules to interpret:

```python
def compare(a: Cell, b: Cell) -> int:
    """
    Compare a and b according to each cell's direction.
    For simplicity, use plain values and flip logic per direction in rules.
    """
    # For increasing: want smaller values left
    # For decreasing: want larger values left
    # Implement directly in each rule function.
    ...
```

For each mixed combination:

* Initialize arrays where half of the cells are `direction="inc"` and half `"dec"`, and Algotypes assigned accordingly.
* Run cell-view mixed step as in 7.5.
* Track Sortedness as defined for **increasing order** (to match paper’s Y-axis).
* Plot Sortedness vs time (swap steps or timesteps) and Aggregation Values until equilibrium (when metrics stop changing).

---

## 8. Statistical Analysis

The paper reports **Z-tests / T-tests** for various comparisons. 

Implement simple helpers using `scipy.stats` (optional but recommended):

```python
from scipy import stats

def z_test_equal_means(sample1, sample2):
    mean1, mean2 = np.mean(sample1), np.mean(sample2)
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)
    n1, n2 = len(sample1), len(sample2)
    se = math.sqrt(var1/n1 + var2/n2)
    z = (mean1 - mean2) / se
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p
```

Use this to:

* Compare traditional vs cell-view step counts
* Compare DG values etc.

---

## 9. Notebook Organization

Have the notebook organized with top-level markdown headings like:

1. **Introduction & Goals** (brief summary of paper + what you reproduce)
2. **Environment Setup**
3. **Core Data Structures & Metrics**
4. **Traditional Algorithms**
5. **Cell-view Algorithms**
6. **Experiment Harness**
7. **Experiments**

   * 7.1 Sorting trajectories (Fig 3)
   * 7.2 Efficiency (Fig 4)
   * 7.3 Frozen cells & error tolerance (Fig 5)
   * 7.4 Delayed Gratification (Figs 6–7)
   * 7.5 Mixed Algotypes & Aggregation (Fig 8)
   * 7.6 Opposing Goals (Fig 9)
8. **Discussion & Comparison to Reported Results**

Each experiment section should:

* Run the relevant `run_experiments` calls.
* Plot equivalent figures.
* Print mean/STD and, optionally, Z-test results.

