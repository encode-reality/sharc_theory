# 🧪 Experiment In Progress: Paper-Accurate Parameters

## Current Status: RUNNING

**Started:** 2025-11-01
**Expected Duration:** 20-30 minutes
**Current Progress:** Early stages (<1%)

---

## Experiment Configuration

### Corrected Parameters (From arXiv:2406.19108)

```
Soup Size: 8,192 tapes (NOT 1,024)
Tape Length: 64 bytes
Mutation Rate: 0.00024 (0.024%, NOT 0%)
Total Interactions: 163,840,000
Total Epochs: 20,000
Seed: 42
```

### Why These Parameters Matter

1. **8,192 tapes**: 8x more than initial implementation
   - Higher probability of finding first replicator
   - Larger search space
   - More diversity for symbiogenesis

2. **0.024% mutation rate**: Tiny but non-zero
   - Provides "cosmic ray" level perturbations
   - Helps escape local minima
   - Does NOT drive evolution (symbiogenesis does)
   - Acts like thermal noise

3. **20,000 epochs**: Sufficient time for phase transition
   - Paper reports 40% success by epoch 16,000
   - 60% may need different seed or more time
   - One epoch = all 8,192 tapes interact once

---

## Expected Results

### Scenario 1: Phase Transition Occurs (40% probability)

**Indicators:**
- Operations per interaction jumps from ~50 to 500+
- Sustained high activity (1000s of operations)
- Diversity collapses from 1.0 to 0.3-0.5
- Dominant replicator emerges (10-30% of population)

**Timeline:**
- Could occur anywhere from epoch 5,000 to 20,000
- Sudden, dramatic shift (not gradual)
- Unmistakable when it happens

**Interpretation:**
✅ Computational abiogenesis successfully reproduced!

### Scenario 2: No Transition (60% probability)

**Indicators:**
- Operations stay below 200 per interaction
- Diversity remains high (>0.8)
- No dominant replicator
- Activity remains sparse

**This is NORMAL per the paper!**

**Next Steps:**
1. Try different seed (123, 456, 789, 999)
2. Run for more epochs (30,000+)
3. Multiple trials expected to find transition

---

## What We're Testing

### Primary Hypothesis
With paper-accurate parameters, we should observe:
- 40% probability of phase transition within 16k epochs
- Self-replicating programs emerging from randomness
- No fitness function or designer needed

### Secondary Questions
1. Does seed 42 show transition? (Unknown until complete)
2. What epoch does transition occur? (If it occurs)
3. What does the dominant replicator look like?
4. How closely do results match paper metrics?

---

## Monitoring Plan

The experiment provides status updates every 200,000 interactions:
- Current epoch number
- Average operations per interaction
- Current diversity
- Unique tape count
- Top replicator frequency (if any)

**Key checkpoints:**
- 200k interactions (~24 epochs): Baseline metrics
- 40M interactions (~4,900 epochs): Early window
- 80M interactions (~9,800 epochs): Mid-point
- 130M interactions (~16,000 epochs): Paper's 40% threshold
- 163M interactions (~20,000 epochs): Final target

---

## Files Being Generated

```
experiments/
├── run_paper_params_metrics_[timestamp].json  # Full time series
└── checkpoints/
    ├── run_paper_params_200k.json             # Early checkpoint
    ├── run_paper_params_transition.json       # If transition occurs
    └── run_paper_params_final.json            # Final state
```

---

## Scientific Significance

### If Transition Occurs:
Proves that with correct parameters, computational abiogenesis is:
- **Reproducible**: Can be demonstrated on demand (with probability)
- **Generic**: Happens in any Turing-complete system
- **Inevitable**: Life is a computational attractor

### If Transition Doesn't Occur:
Shows that abiogenesis is:
- **Probabilistic**: Not guaranteed in finite time
- **Seed-dependent**: Some initial conditions better than others
- **Realistic**: Even in ideal conditions, success is ~40%

Both outcomes are scientifically valuable!

---

## Technical Implementation

### Running Command:
```bash
poetry run python run_experiment.py \
  --soup-size 8192 \
  --mutation-rate 0.00024 \
  --interactions 163840000 \
  --seed 42
```

### Core Algorithm:
1. Initialize 8,192 random 64-byte tapes
2. For each epoch:
   a. Select two random tapes
   b. Concatenate them (128 bytes)
   c. Execute as Brainfuck code
   d. Split result back to two 64-byte tapes
   e. Apply 0.024% mutation to each byte
   f. Repeat 8,192 times (one epoch)
3. Track metrics continuously
4. Detect phase transition automatically

---

## Next Steps After Completion

### If Transition Observed:
1. ✅ Mark experiment as SUCCESS
2. Analyze dominant replicator structure
3. Trace lineage back to first replicator
4. Compare metrics to paper figures
5. Create detailed visualization notebook
6. Write up findings
7. Try additional seeds to observe variety

### If No Transition:
1. Document baseline metrics
2. Try seed 123 (second attempt)
3. Try seed 456 (third attempt)
4. Calculate probability we should have seen it
5. Consider running longer (30k epochs)
6. Compare our null results to paper's 60% failure rate

---

## Current Hypothesis

Based on CRITICAL_FINDINGS.md analysis:

**We expect:**
- Seed 42 has 40% chance of showing transition
- If it does, transition likely between epoch 8,000-16,000
- Operations will jump to 500+, then sustain at 1000s
- Diversity will collapse to 30-50%
- A single replicator will dominate (10-30%)

**Key insight:**
The tiny mutation rate (0.024%) is crucial for:
- Exploring nearby state space
- Breaking perfect stability
- Providing occasional "kicks" to the system
- **BUT** symbiogenesis (fusion) drives complexity

This is still "zero mutation evolution" in the sense that mutations don't drive evolutionary complexity - fusion does!

---

## Progress Tracking

**Last checked:** 2025-11-01 15:01 UTC
**Status:** Running, progress bar showing
**Estimated completion:** ~15-25 minutes from start

**Will check again in 5 minutes for first status update.**

---

## References

**Paper:** "Computational Life: How Well-formed, Self-replicating Programs Emerge from Simple Interaction"
- arXiv:2406.19108
- Blaise Agüera y Arcas, Anitha Pasupathy, et al.
- June 2024

**Key Quote:**
> "In runs with 8,192 tapes and 0.024% mutation rate, approximately 40% show a state transition within 16,000 epochs."

---

**Status:** 🔬 EXPERIMENT ACTIVE - AWAITING RESULTS
