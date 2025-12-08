# Selection Sort Resolution

**Date:** December 8, 2024
**Status:** Requires Full Group Merging Implementation

## Summary

After extensive investigation and analysis of the reference implementation, we've determined that **cell-view Selection Sort requires the full group merging system** to function correctly. A simple timestep-based model with reset mechanisms is insufficient.

## Key Findings from Reference Implementation

### 1. Group-Based Architecture

The reference implementation uses a sophisticated group system:

- **Initial State:** Each cell starts in its own group with boundaries `(i, i)`
- **ideal_position:** Starts at `left_boundary` (own position for single-cell groups)
- **Group Merging:** When adjacent groups are both sorted, they merge
- **Reset Mechanism:** `CellGroup.merge_with_group()` calls `cell.update()` which resets `ideal_position`

**Key Code Path:**
```python
# CellGroup.py:55-73 - merge_with_group()
for cell in self.cells_in_group:
    cell.left_boundary = self.left_boundary_position
    cell.right_boundary = self.right_boundary_position
    cell.update()  # ← This resets ideal_position!
```

### 2. Critical Dependencies

Selection Sort behavior depends on:

1. **Dynamic Boundaries:** Cells' search space expands as groups merge
2. **Synchronized Resets:** All cells in merged groups reset simultaneously
3. **Sorted Region Detection:** Groups only merge when locally sorted
4. **Thread Timing:** Continuous execution creates emergent coordination

### 3. Discrepancies: Paper vs. Implementation

| Aspect | Paper Description | Reference Implementation |
|--------|-------------------|--------------------------|
| **Initial ideal_position** | "most left position" (0 for all) | `left_boundary` (own position initially) |
| **Boundaries** | Not mentioned | Dynamic, expand via group merging |
| **Reset Mechanism** | Not specified | `update()` called on group merge |
| **Execution Model** | Not specified | Continuous threading with locks |

## Attempted Solutions (All Failed)

We tested 15+ variations:

### Approach 1: Simple Reset After No Swaps
- Reset all `ideal_position` to 0 when no swaps occur
- **Result:** Creates infinite loops, cells swap back and forth

### Approach 2: Sorted Region Detection
- Detect locally sorted regions, reset cells within them
- **Result:** Fails to recognize when to reset, gets stuck

### Approach 3: Two-Phase Execution
- Separate decision phase from execution to avoid race conditions
- **Result:** Reduces chaos but still doesn't converge to sorted state

### Approach 4: Cell Identity Tracking
- Ensure each cell acts once per timestep
- **Result:** Prevents double-processing but algorithm still fails

### Approach 5: Start with Own Position
- Match reference implementation's initial `ideal_position = current_position`
- **Result:** No improvement over starting at 0

## Why Simple Resets Don't Work

The fundamental issue: **Selection Sort's correctness depends on the group merging protocol**.

Without groups:
- Cells don't know when their search region should expand
- Resets are either too frequent (causing thrashing) or too rare (causing deadlock)
- No mechanism to "lock in" sorted regions while expanding search space

With groups (reference implementation):
- Sorted regions are explicitly recognized and preserved
- Boundaries expand only when adjacent regions are both sorted
- Resets happen at exactly the right time (on merge)
- Cells search within appropriate bounded regions

## Path Forward

### Option A: Implement Full Group Merging ⚠️ Complex
Implement the complete group merging system from the reference:
- Track groups with dynamic boundaries
- Detect sorted groups each timestep
- Merge adjacent sorted groups
- Call `update()` on all cells in merged groups

**Pros:** Would match reference behavior
**Cons:** Significant complexity, may still have timing differences due to threading

### Option B: Use Bubble + Insertion Only ✓ Recommended
Continue replication experiments using only the **two working algorithms**:
- ✓ **Bubble Sort** - working correctly
- ✓ **Insertion Sort** - working correctly
- ⚠️ **Selection Sort** - deferred until author clarification

**Pros:** Can proceed with replication immediately
**Cons:** Missing one algorithm from the paper

### Option C: Contact Authors 📧 In Progress
We have prepared `AUTHOR_INQUIRY_SELECTION_SORT.md` with specific questions:
- How does `ideal_position` update after swaps?
- When exactly does the reset mechanism trigger?
- How does the algorithm avoid getting stuck?

## Recommendation

**Proceed with Option B** (Bubble + Insertion only) for the following reasons:

1. ✓ Two algorithms are sufficient to demonstrate the core morphogenesis concepts
2. ✓ Allows immediate progress on notebook replication
3. ✓ Can add Selection Sort later after:
   - Author clarification, OR
   - Full group merging implementation, OR
   - Discovery of simpler working approach

## Technical Learnings

Despite not achieving a working Selection Sort, the investigation yielded valuable insights:

1. **Threading Model Impact:** Continuous threading creates emergent behaviors not easily replicated in timestep models
2. **Group Merging is Core:** Not just an optimization - it's fundamental to correctness
3. **Paper-Implementation Gap:** Significant details missing from paper description
4. **Reset Timing is Critical:** When and how resets occur determines algorithm success/failure

## Files Created During Investigation

- `test_selection_with_groups.py` - Group-based reset attempt
- `test_selection_with_reset.py` - Simple reset mechanism
- `test_selection_fixed.py` - Cell identity tracking
- `test_selection_correct.py` - Two-phase execution
- `test_selection_final.py` - Combined approaches
- `test_selection_no_reset.py` - Baseline without reset
- `test_selection_smart_reset.py` - Sorted region detection
- `test_selection_own_position.py` - Reference-matching initialization
- `debug_selection.py` - Detailed execution trace

All attempts documented for future reference.

## Next Steps

1. ✓ Document findings (this file)
2. → **Continue notebook replication with Bubble + Insertion sort**
3. → Optionally implement full group merging system
4. → Send author inquiry when ready

---

**Conclusion:** Selection Sort requires architectural features (group merging) that go beyond the paper's description. For productive progress, we recommend proceeding with the two working algorithms and revisiting Selection Sort after obtaining clarification from the authors or implementing the full group system.
