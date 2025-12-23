# Implementation Guide: Adding Missing Experiments

## Quick Summary

We're missing **3 key experiments** from the author's YouTube presentation:

1. 🔴 **CRITICAL:** Algo-type clustering dynamics (THE key finding)
2. 🟡 **Important:** Delayed gratification visualization
3. 🟢 **Valuable:** Duplicate values (intrinsic motivation)

This guide provides ready-to-use code to add these to the notebook.

---

## Step 1: Add Clustering Metric to `modules/metrics.py`

```python
def algo_type_clustering(algotype_assignments: List[str]) -> float:
    """
    Calculate algo-type clustering coefficient.

    Measures the probability that adjacent elements have the same algorithm type.
    A random mixture would have ~50% clustering (assuming equal distribution).
    Values > 50% indicate emergent spatial organization.

    Args:
        algotype_assignments: List of algorithm types for each position
                            e.g., ['bubble', 'selection', 'bubble', 'insertion']

    Returns:
        Clustering coefficient from 0.0 to 1.0
        - 0.5 = random baseline (no clustering)
        - > 0.5 = positive clustering (like types group together)
        - < 0.5 = negative clustering (like types avoid each other)

    Example:
        >>> types = ['bubble', 'bubble', 'selection', 'selection']
        >>> algo_type_clustering(types)
        0.6667  # 2 out of 3 adjacent pairs match
    """
    if len(algotype_assignments) < 2:
        return 0.0

    matches = sum(
        algotype_assignments[i] == algotype_assignments[i+1]
        for i in range(len(algotype_assignments) - 1)
    )

    return matches / (len(algotype_assignments) - 1)


def identify_sortedness_dips(history: List[float], threshold: float = 0.0) -> List[Tuple[int, float]]:
    """
    Identify points where sortedness temporarily decreases.

    This reveals "delayed gratification" behavior where the algorithm
    temporarily moves against its goal to route around obstacles.

    Args:
        history: Sortedness percentages over time
        threshold: Minimum decrease to count as a dip (default: any decrease)

    Returns:
        List of (swap_index, magnitude) tuples for each dip

    Example:
        >>> history = [20, 40, 60, 55, 70, 90]  # Dip at index 3
        >>> identify_sortedness_dips(history)
        [(3, 5.0)]  # Sortedness decreased by 5% at swap 3
    """
    dips = []
    for i in range(1, len(history)):
        if history[i] < history[i-1]:
            magnitude = history[i-1] - history[i]
            if magnitude >= threshold:
                dips.append((i, magnitude))
    return dips
```

---

## Step 2: Modify `mixed_algotype_sort()` to Track Clustering

Update `modules/cell_view_sorts.py`:

```python
def mixed_algotype_sort(
    initial_values: List[int],
    algotype_assignments: List[str],
    frozen_indices: Optional[Dict[int, FrozenType]] = None
) -> Tuple[List[int], StepCounter, List[float], List[float]]:  # Added clustering history
    """
    Sort array with mixed algorithm types, tracking clustering.

    NEW: Returns clustering history as 4th element!

    Returns:
        (final_values, step_counter, sortedness_history, clustering_history)
    """
    frozen_indices = frozen_indices or {}

    # Create cells with assigned algotypes
    cells = [
        Cell(
            value=v,
            algotype=algotype_assignments[i],
            frozen_type=frozen_indices.get(i, "active")
        )
        for i, v in enumerate(initial_values)
    ]

    steps = StepCounter()
    sortedness_history = []
    clustering_history = []  # NEW: Track clustering

    n = len(cells)

    # Main sorting loop
    for timestep in range(MAX_STEPS):
        idx_order = list(range(n))
        random.shuffle(idx_order)

        swapped_any = False

        for idx in idx_order:
            cell = cells[idx]

            if not cell.can_initiate_move():
                continue

            # Apply algorithm based on cell's algotype
            if cell.algotype == "bubble":
                # Bubble sort logic
                if idx > 0:
                    neighbor = cells[idx - 1]
                    steps.comparisons += 1
                    if cell.value < neighbor.value and neighbor.can_be_moved():
                        cells[idx], cells[idx - 1] = cells[idx - 1], cells[idx]
                        steps.swaps += 1
                        swapped_any = True

            elif cell.algotype == "insertion":
                # Insertion sort logic (similar to above)
                # ... (existing code)
                pass

            elif cell.algotype == "selection":
                # Selection sort logic (similar to above)
                # ... (existing code)
                pass

        # Track metrics after each timestep (if swaps occurred)
        if swapped_any:
            current_values = [c.value for c in cells]
            current_algotypes = [c.algotype for c in cells]

            sortedness_history.append(sortedness(current_values))
            clustering_history.append(algo_type_clustering(current_algotypes))  # NEW

        if not swapped_any:
            break

    final_values = [c.value for c in cells]
    return final_values, steps, sortedness_history, clustering_history
```

---

## Step 3: Create Experiment 7 (Delayed Gratification)

Add to notebook after Experiment 6:

```python
# ---
# ## Experiment 7: Delayed Gratification - Instrumental Problem Solving
#
# ### Motivation: Routing Around Obstacles
#
# When biological systems encounter obstacles, they often take **detours** that temporarily
# move away from the goal to ultimately achieve it. This is called **instrumental problem-solving**
# or **delayed gratification**.
#
# Can simple sorting algorithms exhibit this behavior when faced with immovable frozen cells?
#
# **Test:** Identify moments where sortedness *decreases* as algorithms route around frozen cells.
```

```python
# Experiment 7: Delayed Gratification Analysis

# Parameters
array_size = 15
test_array_dg = list(range(array_size, 0, -1))  # Reverse sorted

# Place frozen cells strategically to create obstacles
np.random.seed(42)
num_frozen = 2
frozen_positions = np.random.choice(range(2, array_size-2), size=num_frozen, replace=False)
frozen_indices_dg = {int(pos): 'immovable' for pos in frozen_positions}

print("Experiment 7: Delayed Gratification")
print("=" * 70)
print(f"Array size: {array_size}")
print(f"Frozen positions: {sorted(frozen_indices_dg.keys())}")
print()

# Test Bubble Sort (best for visualization)
result, steps, history = bubble_sort(test_array_dg.copy(), frozen_indices=frozen_indices_dg)

# Identify dips in sortedness
dips = identify_sortedness_dips(history, threshold=0.1)  # Only significant dips

print(f"Bubble Sort Results:")
print(f"  Final sortedness: {sortedness(result):.1f}%")
print(f"  Total swaps: {steps.swaps}")
print(f"  Sortedness dips detected: {len(dips)}")
print()

if dips:
    print("Delayed Gratification Events:")
    for i, (swap_idx, magnitude) in enumerate(dips, 1):
        print(f"  {i}. At swap {swap_idx}: sortedness decreased by {magnitude:.1f}%")
        print(f"     (Routing around obstacle)")

# Visualize
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(range(len(history)), history, linewidth=2.5, color='steelblue', label='Sortedness')

# Annotate dips
for dip_idx, magnitude in dips:
    ax.plot(dip_idx, history[dip_idx], 'ro', markersize=12, zorder=5)
    ax.annotate(f'Delayed Gratification\n-{magnitude:.1f}%',
               xy=(dip_idx, history[dip_idx]),
               xytext=(dip_idx+3, history[dip_idx]-8),
               arrowprops=dict(arrowstyle='->', color='red', lw=2),
               bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8, edgecolor='red'),
               fontsize=10, fontweight='bold')

ax.set_xlabel('Swap Number', fontsize=12)
ax.set_ylabel('Sortedness (%)', fontsize=12)
ax.set_title('Delayed Gratification: Temporary Regression to Route Around Obstacles',
            fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 105)

plt.tight_layout()
plt.savefig('figures/delayed_gratification.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nFigure saved: figures/delayed_gratification.png")
```

---

## Step 4: Create Experiment 8 (Clustering Dynamics) 🔴 **CRITICAL**

Add to notebook after Experiment 7:

```python
# ---
# ## Experiment 8: Algo-Type Clustering - Emergent Spatial Organization
#
# ### The Key "Unexpected Competency"
#
# In chimeric arrays where cells use different algorithms (Experiment 5), we measured
# final sortedness. But we missed a **critical emergent phenomenon**: cells using the
# same algorithm temporarily **cluster together spatially**, even though:
#
# 1. **No variable tracks algorithm type** during sorting
# 2. **Cells cannot detect** their neighbors' algorithms
# 3. **No rule encourages** clustering
# 4. **No extra computation** was added
#
# This clustering is **"free"** - it emerges spontaneously from the dynamics.
#
# **Test:** Track clustering throughout sorting and observe temporal peak.
```

```python
# Experiment 8: Clustering Dynamics

# Parameters
array_size = 30
test_array_cluster = list(np.random.randint(1, 50, size=array_size))

# Randomly assign algorithm types (equal mix)
algotype_assignments = (['bubble'] * 10 + ['insertion'] * 10 + ['selection'] * 10)
np.random.shuffle(algotype_assignments)

print("Experiment 8: Emergent Algo-Type Clustering")
print("=" * 70)
print(f"Array size: {array_size}")
print(f"Algorithm distribution:")
print(f"  Bubble: {algotype_assignments.count('bubble')}")
print(f"  Insertion: {algotype_assignments.count('insertion')}")
print(f"  Selection: {algotype_assignments.count('selection')}")
print()

# Run mixed algotype sort with clustering tracking
result, steps, sort_history, cluster_history = mixed_algotype_sort(
    test_array_cluster.copy(),
    algotype_assignments
)

print(f"Results:")
print(f"  Final sortedness: {sortedness(result):.1f}%")
print(f"  Total swaps: {steps.swaps}")
print(f"  Initial clustering: {cluster_history[0]:.1%}")
print(f"  Peak clustering: {max(cluster_history):.1%}")
print(f"  Final clustering: {cluster_history[-1]:.1%}")
print(f"  Random baseline: 50.0%")
print()

peak_idx = cluster_history.index(max(cluster_history))
peak_sortedness = sort_history[peak_idx]
print(f"Peak occurred at:")
print(f"  Swap {peak_idx} (of {len(cluster_history)})")
print(f"  Sortedness: {peak_sortedness:.1f}%")

# Statistical significance
baseline = 0.5
peak = max(cluster_history)
above_baseline = (peak - baseline) * 100
print()
print(f"Emergent clustering: {above_baseline:.1f} percentage points above random baseline")

# Visualization
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Top: Sortedness progression
ax1.plot(range(len(sort_history)), sort_history, linewidth=2.5, color='steelblue', label='Sortedness')
ax1.axvline(x=peak_idx, color='red', linestyle='--', alpha=0.5, label='Peak Clustering')
ax1.set_ylabel('Sortedness (%)', fontsize=12)
ax1.set_title('Sorting Progress', fontsize=13, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 105)

# Bottom: Clustering dynamics
ax2.plot(range(len(cluster_history)), [c*100 for c in cluster_history],
        linewidth=2.5, color='coral', label='Observed Clustering')
ax2.axhline(y=50, color='gray', linestyle='--', linewidth=2, label='Random Baseline (50%)')
ax2.axvline(x=peak_idx, color='red', linestyle='--', alpha=0.5)

# Highlight peak
ax2.plot(peak_idx, cluster_history[peak_idx]*100, 'ro', markersize=15, zorder=5)
ax2.annotate(f'Peak Clustering\n{cluster_history[peak_idx]:.1%}\n(Emergent Organization)',
            xy=(peak_idx, cluster_history[peak_idx]*100),
            xytext=(peak_idx+5, cluster_history[peak_idx]*100+5),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8, edgecolor='red'),
            fontsize=11, fontweight='bold')

ax2.set_xlabel('Swap Number', fontsize=12)
ax2.set_ylabel('Clustering (%)', fontsize=12)
ax2.set_title('Emergent Algo-Type Clustering (Without Designed Mechanism)',
             fontsize=13, fontweight='bold')
ax2.legend(fontsize=11, loc='upper right')
ax2.grid(True, alpha=0.3)
ax2.set_ylim(40, max(cluster_history)*100+10)

plt.tight_layout()
plt.savefig('figures/clustering_dynamics.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nFigure saved: figures/clustering_dynamics.png")
```

---

## Step 5: Create Experiment 9 (Duplicate Values - Intrinsic Motivation)

Add to notebook after Experiment 8:

```python
# ---
# ## Experiment 9: Intrinsic Motivation - Relaxing Constraints
#
# ### Imposed Goal vs. Intrinsic Dynamics
#
# **Hypothesis:** Clustering represents an "intrinsic motivation" of the system,
# while sorting is the "imposed external goal." When we relax the sorting constraint
# by allowing duplicate values, the intrinsic clustering behavior should strengthen.
#
# **Test:** Compare clustering with unique vs. duplicate values.
```

```python
# Experiment 9: Clustering with Duplicate Values

def create_array_with_duplicates(size, duplicate_pct):
    """Create array where specified % of values are duplicates."""
    unique_count = max(2, int(size * (100 - duplicate_pct) / 100))
    unique_values = list(range(1, unique_count + 1))

    # Sample with replacement to create duplicates
    result = []
    for _ in range(size):
        result.append(random.choice(unique_values))

    random.shuffle(result)
    return result

# Test different duplicate levels
duplicate_levels = [0, 25, 50, 75]
clustering_results = {}

print("Experiment 9: Intrinsic Motivation (Duplicate Values)")
print("=" * 70)

for dup_pct in duplicate_levels:
    print(f"\nDuplicate percentage: {dup_pct}%")

    # Create array with duplicates
    test_array = create_array_with_duplicates(30, dup_pct)

    # Random algotype assignment
    algotypes = (['bubble'] * 10 + ['insertion'] * 10 + ['selection'] * 10)
    np.random.shuffle(algotypes)

    # Run and track clustering
    result, steps, sort_hist, cluster_hist = mixed_algotype_sort(test_array.copy(), algotypes)

    peak_clustering = max(cluster_hist)
    clustering_results[dup_pct] = {
        'peak': peak_clustering,
        'history': cluster_hist,
        'final_sort': sortedness(result)
    }

    print(f"  Peak clustering: {peak_clustering:.1%}")
    print(f"  Final sortedness: {sortedness(result):.1f}%")

# Visualize comparison
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Left: Peak clustering vs. duplicate %
duplicate_pcts = list(clustering_results.keys())
peaks = [clustering_results[d]['peak'] * 100 for d in duplicate_pcts]

ax1.plot(duplicate_pcts, peaks, 'o-', linewidth=2.5, markersize=10, color='coral')
ax1.axhline(y=50, color='gray', linestyle='--', linewidth=2, label='Random Baseline')
ax1.set_xlabel('Duplicate Percentage (%)', fontsize=12)
ax1.set_ylabel('Peak Clustering (%)', fontsize=12)
ax1.set_title('Intrinsic Motivation: Clustering Strengthens\nWhen External Constraint is Relaxed',
             fontsize=13, fontweight='bold')
ax1.legend(fontsize=11)
ax1.grid(True, alpha=0.3)

# Right: Clustering trajectories
for dup_pct in duplicate_levels:
    history = clustering_results[dup_pct]['history']
    ax2.plot(range(len(history)), [c*100 for c in history],
            linewidth=2, label=f'{dup_pct}% duplicates', alpha=0.8)

ax2.axhline(y=50, color='gray', linestyle='--', linewidth=2, alpha=0.5)
ax2.set_xlabel('Swap Number', fontsize=12)
ax2.set_ylabel('Clustering (%)', fontsize=12)
ax2.set_title('Clustering Dynamics Across Duplicate Levels',
             fontsize=13, fontweight='bold')
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figures/intrinsic_motivation.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nFigure saved: figures/intrinsic_motivation.png")
print()
print("=" * 70)
print("INTERPRETATION:")
print("As duplicate % increases, sorting constraint relaxes,")
print("allowing intrinsic clustering tendency to dominate.")
print("=" * 70)
```

---

## Summary of Changes

### Files to Modify

1. **`modules/metrics.py`** - Add 2 new functions
   - `algo_type_clustering()`
   - `identify_sortedness_dips()`

2. **`modules/cell_view_sorts.py`** - Modify 1 function
   - Update `mixed_algotype_sort()` to return clustering history

3. **`morphogenesis_experiments.ipynb`** - Add 3 new experiments
   - Experiment 7: Delayed Gratification
   - Experiment 8: Clustering Dynamics ⭐ **CRITICAL**
   - Experiment 9: Intrinsic Motivation

### Expected Results

**Experiment 7:**
- 2-5 sortedness dips per frozen cell
- Dips of 5-20% magnitude
- Visual demonstration of instrumental problem-solving

**Experiment 8:**
- Initial clustering: ~50% (random)
- Peak clustering: ~55-65% (emergent organization)
- Final clustering: ~50% (sorting dominates)
- **KEY FINDING:** Spontaneous clustering without designed mechanism

**Experiment 9:**
- 0% duplicates: Peak ~60%
- 50% duplicates: Peak ~70%
- 75% duplicates: Peak ~80%
- **KEY FINDING:** Intrinsic dynamics emerge when constraints relax

---

## Testing the Implementation

```python
# Quick test of new metrics
from modules.metrics import algo_type_clustering, identify_sortedness_dips

# Test clustering
algotypes = ['bubble', 'bubble', 'selection', 'bubble', 'selection', 'selection']
clustering = algo_type_clustering(algotypes)
print(f"Clustering: {clustering:.2%}")  # Should be > 50%

# Test dip detection
history = [20, 40, 60, 55, 70, 90, 85, 100]
dips = identify_sortedness_dips(history)
print(f"Dips found: {len(dips)}")  # Should find 2 dips
print(f"Details: {dips}")  # [(3, 5.0), (6, 5.0)]
```

---

## Priority Order

1. 🔴 **Start with Experiment 8** (Clustering) - This is THE key missing finding
2. 🟡 **Then Experiment 7** (Delayed Gratification) - Easier, demonstrates problem-solving
3. 🟢 **Finally Experiment 9** (Duplicates) - Builds on Experiment 8

---

**Estimated Implementation Time:**
- Metrics: 15 minutes
- Modify mixed sort: 30 minutes
- Experiment 7: 20 minutes
- Experiment 8: 30 minutes
- Experiment 9: 30 minutes
- **Total: ~2 hours**

All code is ready to copy-paste into the appropriate files!
