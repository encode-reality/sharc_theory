# BFF Abiogenesis - Quick Start Guide

## 🚀 Running the 2 Million Interaction Experiment

### Prerequisites

All dependencies are already installed! Just make sure you're in the right directory:

```bash
cd /Users/legirl/Documents/GitHub/sharc_theory/models/evolutionary/abiogenesis_blaise
```

### Launch Jupyter Lab

```bash
poetry run jupyter lab
```

This will open Jupyter Lab in your browser.

### Open the Notebook

In Jupyter Lab, navigate to:
```
notebooks/02_long_run_2M.ipynb
```

### Run the Experiment

1. **Click "Run" → "Run All Cells"** (or use Shift+Enter to run cells one by one)

2. **Expected Runtime**: 10-30 minutes
   - Depends on when phase transition occurs
   - You'll see progress bars and status updates

3. **What to Watch For**:
   - Initial operations: ~50-100 per interaction
   - **Phase transition**: Operations jump to 1000s+
   - Diversity collapse: From 100% → <50%
   - Population takeover by replicators

### What You'll Get

#### Real-Time Monitoring:
- Progress bar showing interactions completed
- Status updates every 100k interactions
- Auto-detection of phase transition
- Performance metrics (interactions/second)

#### Visualizations:
- 6-panel comprehensive analysis figure
- Operations over time (log scale)
- Diversity collapse
- Replicator dominance
- Frequency distributions

#### Saved Results:
- `experiments/checkpoints/run_2M_final_[timestamp].json` - Final soup state
- `experiments/run_2M_metrics_[timestamp].json` - Complete time series
- `experiments/run_2M_visualization.png` - Main figure
- `experiments/checkpoints/run_2M_transition_[timestamp].json` - State at transition (if detected)

## 📊 Expected Results

Based on Blaise's work, you should see:

### Phase Transition (80-90% probability with 2M interactions)

**Before Transition:**
- Operations: 10-100 per interaction
- Diversity: ~100% (all tapes unique)
- Activity: Sparse, random

**After Transition:**
- Operations: 1000-10,000 per interaction
- Diversity: 20-50% (replicators dominating)
- Activity: Dense, sustained computation

### Dominant Replicators

- Top replicator: 10-30% of population
- Top 5 replicators: 40-70% of population
- Remaining: Long tail of rare variants

## 🔬 Understanding the Results

### What is a "Phase Transition"?

It's the moment when self-replicating programs emerge and take over:

1. **Before**: Random bytes, mostly no-ops, low activity
2. **Transition**: First replicators appear
3. **After**: Replicators dominate, high computation

### Why Does It Happen?

**Dynamic Kinetic Stability** (Addy Pross):
- Replicators persist because they copy themselves
- Non-replicators fade away (overwritten)
- Natural selection emerges automatically

### Key Insight

**No fitness function needed!** The system wasn't told to evolve life. It just did, because:
- Replicators are **stable through reproduction**
- Everything else is **unstable** (gets overwritten)
- This is **why life exists**

## 🎯 Experiment Variations

### Quick Test (5 minutes)
Change in first cell:
```python
TOTAL_INTERACTIONS = 100_000  # Instead of 2_000_000
```

### Different Starting Conditions
```python
SEED = 123  # Try different seeds
SOUP_SIZE = 2048  # Bigger population
MUTATION_RATE = 0.001  # Add mutations
```

### Observe Specific Seeds

Some seeds evolve faster than others. Try:
- `SEED = 42` - Baseline
- `SEED = 7` - Often faster
- `SEED = 123` - Different trajectory

## 📈 Interpreting the Graphs

### Graph 1: Operations Over Time
- **Y-axis (log scale)**: Operations per interaction
- **Flat line → Vertical jump**: Phase transition!
- **Green dashed line**: Marks exact transition point

### Graph 2: Early Phase Detail
- **First 100k interactions** in detail
- Look for the **"ignition moment"**
- Rolling average smooths noise

### Graph 3: Diversity Collapse
- **Starts at 1.0** (100% unique)
- **Drops rapidly** when replicators emerge
- **Stabilizes** at new equilibrium

### Graph 4: Unique Tape Count
- Absolute number of distinct tapes
- Should drop from 1024 → ~200-500

### Graph 5: Frequency Distribution
- **Power law**: Few dominant, many rare
- **Orange bars**: Each unique tape's copy count
- **Log scale**: Shows full range

## 🔍 Analyzing the Dominant Replicator

The notebook shows you the actual bytes of the winning program:

```
Tape data (64 bytes):
00: 2b 5b 3c 2c 3e 2b 5d ...  # Hex dump
   +  [  <  ,  >  +  ]  ...  # ASCII interpretation

Instructions: 18/64 bytes (28% density)
Breakdown:
  '+': 12 occurrences
  ',': 8 occurrences
  '[': 4 occurrences
  ...
```

This tells you:
- **How the replicator works** (which instructions)
- **Complexity level** (instruction density)
- **Structure** (loops indicated by `[` `]`)

## 💾 Saved Data Format

### Final State JSON
```json
{
  "size": 1024,
  "tape_length": 64,
  "interaction_count": 2000000,
  "tapes": [
    {"length": 64, "data": [...]},
    ...
  ]
}
```

You can reload this later:
```python
from core.soup import Soup
soup = Soup.from_state(state)
```

### Metrics JSON
```json
{
  "config": {...},
  "results": {
    "transition_detected": true,
    "transition_point": 347000,
    "final_diversity": 0.234
  },
  "time_series": {
    "sampled_interactions": [1000, 2000, ...],
    "sampled_ops_mean": [12.3, 15.7, ...]
  }
}
```

## 🐛 Troubleshooting

### "No phase transition detected"

**This is normal!** Abiogenesis is probabilistic. Try:
1. Run longer (5M interactions)
2. Different seed
3. Larger soup (2048 tapes)

### Notebook runs slow

- Expected: ~100-1000 interactions/second
- If slower: May hit transition (good!)
- High ops = More computation = Slower but interesting

### Jupyter kernel crashes

- Reduce `SOUP_SIZE` to 512
- Reduce `TOTAL_INTERACTIONS` to 1M
- Close other notebooks

## 📚 Next Steps After Running

1. **Try different seeds** - See variety in evolution
2. **Add mutations** - Set `MUTATION_RATE = 0.001`
3. **Compare runs** - Load saved checkpoints
4. **Implement metrics** - Phase transition detection algorithms
5. **Track lineages** - See symbiogenesis events
6. **Go spatial** - 2D grid version

## 🎓 Further Reading

- **Blaise's Long Now Talk**: "What is Intelligence?"
- **Sean Carroll Podcast**: Deep dive on BFF
- **Paper references**: Von Neumann, Margulis, Pross
- **Book (2025)**: "What is Intelligence?" - Blaise Agüera y Arcas

---

**Ready to see life emerge from randomness?**

**Just run: `poetry run jupyter lab`** 🧬✨
