# Missing Experiments & Metrics - YouTube Analysis

## Summary

Based on the author's YouTube transcript (Lex Fridman show), we are missing **3 key experiments/metrics** that reveal critical "unexpected competencies" of the sorting algorithms.

---

## What We Currently Have ✓

| Experiment | Status | Description |
|------------|--------|-------------|
| **Basic Sorting** | ✓ Complete | All three algorithms work correctly |
| **Dynamics Visualization** | ✓ Complete | Sortedness progression over time |
| **Array Size Comparison** | ✓ Complete | Efficiency across different sizes |
| **Frozen Cell Robustness** | ✓ Complete | Damage resilience (0-50% frozen) |
| **Chimeric Arrays** | ✓ Complete | Mixed algorithm types |
| **Frozen Cell Dynamics** | ✓ Complete | Recovery trajectories with 10% frozen |
| **Distributed Agents** | ✓ Implicit | Our implementation is cell-autonomous |

---

## What We're Missing ❌

### 🔴 **MISSING 1: Delayed Gratification Analysis**

**From YouTube (Experiment 1):**
> "Sortedness temporarily decreases at specific points when the algorithm hits an immovable element. The algorithm must make the array *less sorted* to work around the obstacle. This resembles delayed gratification—temporarily moving against instantaneous reward to achieve global reward."

**What We Have:**
- We track sortedness over time (Experiment 6)
- We measure final sortedness with frozen cells (Experiment 4)

**What We're Missing:**
- ❌ **Explicit identification of sortedness "dips"**
- ❌ **Visualization highlighting delayed gratification**
- ❌ **Metric quantifying temporary regression**
- ❌ **Analysis of when/why sortedness decreases**

**Scientific Significance:**
This demonstrates **instrumental problem-solving**: the system temporarily acts against its immediate goal (increasing sortedness) to achieve the ultimate goal (full sorting). This is analogous to biological organisms taking detours around obstacles.

---

### 🔴 **MISSING 2: Algo-Type Clustering Metric** ⚠️ **CRITICAL**

**From YouTube (Experiment 3):**
> "Algo types self-organize into local homogeneous neighborhoods temporarily, even though there is no variable representing algo type, agents cannot detect their neighbors' algorithm, and no rule encourages clustering. The clustering behavior is emergent and 'free'—it cost zero extra computational steps."

**What We Have:**
- Chimeric arrays with mixed algorithms (Experiment 5)
- Final sortedness measurement
- Swap counts

**What We're Missing:**
- ❌ **Clustering metric** (probability neighbors share same algo type)
- ❌ **Clustering over time** (should peak in middle, then return to baseline)
- ❌ **Visualization of clustering dynamics**
- ❌ **Analysis of emergent spatial organization**

**Implementation:**
```python
def algo_type_clustering(algotype_assignments):
    """
    Measure probability that adjacent cells have same algorithm type.

    Returns:
        float: Clustering coefficient (0.0 = no clustering, 1.0 = perfect clustering)
    """
    matches = sum(
        algotype_assignments[i] == algotype_assignments[i+1]
        for i in range(len(algotype_assignments)-1)
    )
    return matches / (len(algotype_assignments) - 1)
```

**Expected Curve:**
```
Clustering %
    60% ┤     ╭──╮
    55% ┤    ╱    ╲
    50% ┼───╯      ╰────
        └─────────────────> Sorting Progress (0% → 100%)
         Start   Mid    End
```

**Scientific Significance:**
This is the **KEY "unexpected competency"** that reveals emergent cultural/behavioral organization. The system exhibits spontaneous spatial clustering *without* any mechanism designed to produce it. This parallels biological pattern formation (e.g., somitogenesis).

---

### 🔴 **MISSING 3: Relaxed Constraints (Repeated Digits)**

**From YouTube (Experiment 4):**
> "Allow repeated digits in the array. Clustering increases beyond the previous maximum. Interpretation: Sorting is the externally imposed goal. Clustering is the intrinsic motivation of the system. Reducing the pressure of the imposed goal allows intrinsic behavior to flourish."

**What We Have:**
- Tests with unique values only
- Chimeric arrays

**What We're Missing:**
- ❌ **Experiments with repeated/duplicate values**
- ❌ **Clustering measurement with duplicates**
- ❌ **Comparison: clustering with unique vs. duplicate values**
- ❌ **Analysis of "intrinsic motivation" vs. "imposed goal"**

**Implementation:**
```python
# Test array with duplicates
test_array = [5, 3, 5, 2, 3, 5, 1, 3, 2, 5]  # Multiple repeated values

# Assign mixed algotypes
algotypes = ['bubble', 'insertion', 'selection'] * (len(test_array) // 3)

# Track clustering throughout sorting
```

**Expected Observation:**
- **With unique values:** Clustering peaks ~55-60%, then returns to baseline
- **With duplicates:** Clustering peaks higher (~70-80%+) and sustains longer
- Duplicates reduce sorting constraint, allowing algo-type clustering to dominate

**Scientific Significance:**
This reveals the **competition between imposed goals and intrinsic dynamics**. When external constraints are relaxed, the system's "natural" organizational tendencies emerge. This parallels biological development where reducing selective pressure reveals latent phenotypic variation.

---

## Proposed New Experiments

### **Experiment 7: Delayed Gratification Visualization**

**Purpose:** Demonstrate that sorting algorithms exhibit instrumental problem-solving

**Procedure:**
1. Use reverse-sorted array with 1-2 immovable frozen cells
2. Track sortedness after every swap
3. Identify points where sortedness decreases
4. Visualize with annotations

**Metrics:**
- `dips_count`: Number of times sortedness decreases
- `max_regression`: Maximum temporary decrease in sortedness
- `dip_positions`: Array indices where dips occur

**Visualization:**
```
Sortedness %
   100% ┤                    ╭─────
    80% ┤              ╭────╯
    60% ┤         ╭───╯
    40% ┤    ╭───╯↓ Dip (routing around frozen cell)
    20% ┼───╯
        └──────────────────────────> Swap Number
```

**Code Outline:**
```python
# Track sortedness and identify dips
for i in range(1, len(history)):
    if history[i] < history[i-1]:
        dips.append((i, history[i-1] - history[i]))

# Visualize with annotations
plt.plot(history, linewidth=2)
for dip_idx, magnitude in dips:
    plt.annotate('Delayed gratification',
                 xy=(dip_idx, history[dip_idx]),
                 xytext=(dip_idx+5, history[dip_idx]-10),
                 arrowprops=dict(arrowstyle='->'))
```

---

### **Experiment 8: Algo-Type Clustering Dynamics** ⚠️ **HIGH PRIORITY**

**Purpose:** Reveal emergent spatial organization without designed mechanism

**Procedure:**
1. Create chimeric array with mixed algotypes
2. Track clustering coefficient after every swap
3. Normalize by sorting progress (0-100%)
4. Compare to random baseline (50%)

**Metrics:**
- `clustering_coefficient(t)`: Algo-type clustering over time
- `peak_clustering`: Maximum clustering achieved
- `peak_time`: When maximum clustering occurs (should be ~50% sorted)

**Visualization:**
```
Clustering
    70% ┤          Bubble-rich    Insertion-rich
    60% ┤    Peak  ┌─────┐        ┌─────┐
    50% ┼────╯     │     │        │     │
    40% ┤          └─────┘        └─────┘
        └───────────────────────────────────> Sorting Progress
         0%         25%    75%     100%
```

**Code Outline:**
```python
def track_clustering_during_sort(initial_values, algotype_assignments):
    history_clustering = []
    history_sortedness = []

    # Run mixed sort while tracking both metrics
    for step in sorting_process:
        clustering = algo_type_clustering(current_algotypes)
        sortedness_val = sortedness(current_values)

        history_clustering.append(clustering)
        history_sortedness.append(sortedness_val)

    return history_clustering, history_sortedness

# Normalize clustering by sorting progress
normalized_clustering = interpolate(history_clustering,
                                   history_sortedness,
                                   x_points=[0, 25, 50, 75, 100])
```

**Statistical Test:**
```python
# Compare to random baseline
random_clustering = 0.5  # Expected for random mixing
peak_clustering = max(history_clustering)
significance = (peak_clustering - random_clustering) / std(bootstrap_samples)

print(f"Peak clustering: {peak_clustering:.2%}")
print(f"Above baseline: {peak_clustering - 0.5:.2%}")
print(f"Statistical significance: {significance:.2f} σ")
```

---

### **Experiment 9: Intrinsic Motivation (Duplicate Values)**

**Purpose:** Show that relaxing constraints reveals intrinsic system dynamics

**Procedure:**
1. Run Experiment 8 with **unique values**
2. Run Experiment 8 with **50% duplicate values**
3. Run Experiment 8 with **75% duplicate values**
4. Compare clustering peaks

**Metrics:**
- `peak_clustering_unique`: Max clustering with unique values
- `peak_clustering_duplicates`: Max clustering with duplicates
- `clustering_ratio = peak_duplicates / peak_unique`

**Expected Results:**
```
Peak Clustering vs. Duplicate Percentage

Clustering
    85% ┤                          ╱─────
    75% ┤                    ╱────╯
    65% ┤              ╱────╯
    55% ┼────────────╯
        └────────────────────────────────> Duplicate %
         0%    25%    50%    75%   100%
```

**Code Outline:**
```python
def create_array_with_duplicates(size, duplicate_pct):
    unique_count = int(size * (1 - duplicate_pct/100))
    unique_values = list(range(1, unique_count + 1))

    # Add duplicates to reach desired size
    while len(unique_values) < size:
        unique_values.append(random.choice(unique_values[:unique_count]))

    random.shuffle(unique_values)
    return unique_values

# Test different duplicate levels
for dup_pct in [0, 25, 50, 75]:
    test_array = create_array_with_duplicates(20, dup_pct)
    algotypes = random_algotype_assignment(20)

    clustering_history = track_clustering(test_array, algotypes)
    peak = max(clustering_history)

    results[dup_pct] = peak
```

**Interpretation:**
- **Low duplicates:** Sorting dominates, clustering is weak
- **High duplicates:** Sorting constraint relaxed, clustering strengthens
- Demonstrates "intrinsic motivation" (clustering) vs "imposed goal" (sorting)

---

## Implementation Priority

### 🔴 **Critical (Must Have)**
1. **Experiment 8: Algo-Type Clustering** - This is THE key finding from the paper
   - Implement clustering metric
   - Track clustering over sorting progress
   - Visualize clustering dynamics

### 🟡 **High Priority**
2. **Experiment 7: Delayed Gratification** - Demonstrates instrumental reasoning
   - Identify sortedness dips
   - Annotate delayed gratification points

### 🟢 **Important (Should Have)**
3. **Experiment 9: Duplicate Values** - Tests intrinsic vs. imposed dynamics
   - Arrays with duplicates
   - Clustering comparison across duplicate levels

---

## Code Requirements

### New Metrics Module Functions

```python
# In modules/metrics.py

def algo_type_clustering(algotype_assignments: List[str]) -> float:
    """
    Calculate algo-type clustering coefficient.

    Measures probability that adjacent elements have same algorithm type.

    Args:
        algotype_assignments: List of algorithm types ['bubble', 'insertion', 'selection']

    Returns:
        float: Clustering coefficient (0.0 to 1.0)
               0.5 = random baseline
               > 0.5 = clustering present
    """
    if len(algotype_assignments) < 2:
        return 0.0

    matches = sum(
        algotype_assignments[i] == algotype_assignments[i+1]
        for i in range(len(algotype_assignments)-1)
    )
    return matches / (len(algotype_assignments) - 1)


def identify_sortedness_dips(history: List[float]) -> List[Tuple[int, float]]:
    """
    Identify points where sortedness temporarily decreases.

    Args:
        history: Sortedness values over time

    Returns:
        List of (index, magnitude) tuples for each dip
    """
    dips = []
    for i in range(1, len(history)):
        if history[i] < history[i-1]:
            magnitude = history[i-1] - history[i]
            dips.append((i, magnitude))
    return dips


def normalize_by_sorting_progress(values: List[float],
                                  sortedness_history: List[float],
                                  progress_points: List[int] = [0, 25, 50, 75, 100]) -> Dict[int, float]:
    """
    Normalize a metric by sorting progress instead of time.

    Args:
        values: Metric values over time
        sortedness_history: Sortedness over same time points
        progress_points: Progress percentages to sample at

    Returns:
        Dict mapping progress percentage to metric value
    """
    from scipy.interpolate import interp1d

    # Create interpolation function
    f = interp1d(sortedness_history, values, kind='linear', fill_value='extrapolate')

    # Sample at desired progress points
    return {p: float(f(p)) for p in progress_points}
```

### New Experiments Module Functions

```python
# In modules/experiments.py

def clustering_experiment(initial_values: List[int],
                         algotype_assignments: List[str],
                         track_interval: int = 1) -> Dict:
    """
    Track algo-type clustering throughout sorting process.

    Returns:
        Dict with:
            - clustering_history: Clustering over time
            - sortedness_history: Sortedness over time
            - peak_clustering: Maximum clustering
            - peak_time: When peak occurred
    """
    # Implementation
    pass


def delayed_gratification_experiment(initial_values: List[int],
                                     frozen_indices: Dict[int, str]) -> Dict:
    """
    Identify and analyze sortedness dips (delayed gratification).

    Returns:
        Dict with:
            - history: Sortedness over time
            - dips: List of (index, magnitude) tuples
            - max_regression: Largest temporary decrease
    """
    # Implementation
    pass
```

---

## Visualization Requirements

### Clustering Dynamics Plot

```python
def plot_clustering_dynamics(clustering_history, sortedness_history):
    """
    Plot clustering coefficient vs. sorting progress.

    Shows emergent spatial organization over time.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Top: Sortedness progression
    ax1.plot(sortedness_history, linewidth=2, color='steelblue')
    ax1.set_ylabel('Sortedness (%)')
    ax1.set_title('Sorting Progress')

    # Bottom: Clustering with baseline
    ax2.plot(clustering_history, linewidth=2, color='coral', label='Observed')
    ax2.axhline(y=0.5, color='gray', linestyle='--', label='Random Baseline')
    ax2.set_xlabel('Swap Number')
    ax2.set_ylabel('Clustering Coefficient')
    ax2.set_title('Emergent Algo-Type Clustering')
    ax2.legend()

    # Highlight peak clustering
    peak_idx = clustering_history.index(max(clustering_history))
    ax2.annotate('Peak Clustering\n(Emergent Organization)',
                xy=(peak_idx, clustering_history[peak_idx]),
                xytext=(peak_idx+10, clustering_history[peak_idx]+0.05),
                arrowprops=dict(arrowstyle='->', color='red'))
```

### Delayed Gratification Plot

```python
def plot_delayed_gratification(history, dips):
    """
    Plot sortedness with annotated dips showing delayed gratification.
    """
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(history, linewidth=2, color='steelblue')

    # Annotate each dip
    for i, (dip_idx, magnitude) in enumerate(dips):
        ax.annotate(f'Delayed Gratification\n(-{magnitude:.1f}%)',
                   xy=(dip_idx, history[dip_idx]),
                   xytext=(dip_idx+5, history[dip_idx]-10),
                   arrowprops=dict(arrowstyle='->', color='red', lw=2),
                   bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

    ax.set_xlabel('Swap Number')
    ax.set_ylabel('Sortedness (%)')
    ax.set_title('Delayed Gratification: Temporary Regression to Route Around Obstacles')
```

---

## Expected Outcomes

### Clustering Dynamics (Experiment 8)

**Hypothesis:** Clustering will peak at ~50% sorting progress

**Expected Numbers:**
- Start: ~50% clustering (random baseline)
- Peak: ~55-65% clustering (emergent organization)
- End: ~50% clustering (sorting dominates)

**Significance:**
- Peak > baseline by 5-15 percentage points
- Occurs without any mechanism designed to produce clustering
- "Free" emergent behavior

### Delayed Gratification (Experiment 7)

**Hypothesis:** Sortedness will temporarily decrease when encountering frozen cells

**Expected Numbers:**
- Dips: 1-5 per frozen cell (depending on position)
- Magnitude: 5-20% temporary decrease
- Recovery: Sortedness increases again after routing around

**Significance:**
- Demonstrates instrumental problem-solving
- System acts against immediate goal to achieve ultimate goal

### Duplicate Values (Experiment 9)

**Hypothesis:** Clustering increases with duplicate percentage

**Expected Numbers:**
- 0% duplicates: Peak ~60% clustering
- 50% duplicates: Peak ~70% clustering
- 75% duplicates: Peak ~80% clustering

**Significance:**
- Reveals competition between imposed goal (sorting) and intrinsic dynamics (clustering)
- "Intrinsic motivation" emerges when external pressure is reduced

---

## Summary Table

| Experiment | Status | Priority | Metric Missing | Complexity |
|------------|--------|----------|----------------|------------|
| **Delayed Gratification** | ❌ Missing | High | Dip identification | Low |
| **Clustering Dynamics** | ❌ Missing | **CRITICAL** | Clustering coefficient | Medium |
| **Duplicate Values** | ❌ Missing | Medium | Clustering with duplicates | Medium |

---

## Next Steps

1. **Implement clustering metric** (`algo_type_clustering()`)
2. **Modify mixed_algotype_sort** to track algotype assignments throughout
3. **Create Experiment 8** (clustering dynamics)
4. **Create Experiment 7** (delayed gratification)
5. **Create Experiment 9** (duplicate values)
6. **Add visualizations** to notebook
7. **Document findings** in notebook markdown cells

---

## References

- **Source:** YouTube transcript summary (Lex Fridman show)
- **Paper:** Zhang, T., Goldstein, A., & Levin, M. (2024)
- **Key Concept:** "Unexpected competencies" = emergent behaviors not explicitly programmed

---

**Author Note:** The clustering experiment is the **most important missing piece**. This is the core "unexpected competency" that demonstrates emergent spatial organization without any designed mechanism. It should be highest priority for implementation.
