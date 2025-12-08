# Request for Clarification: Cell-View Selection Sort Implementation

**To:** Zhang, T., Goldstein, A., Levin, M.
**Re:** Paper "Classical Sorting Algorithms as a Model of Morphogenesis" (arXiv:2401.05375v1)
**Date:** December 7, 2025
**From:** Independent Replication Team

---

## Purpose

We are attempting to replicate the experiments from your paper "Classical Sorting Algorithms as a Model of Morphogenesis: self-sorting arrays reveal unexpected competencies in a minimal model of basal intelligence." While we have successfully implemented and replicated the cell-view bubble sort and insertion sort algorithms, we have encountered a fundamental issue with the cell-view selection sort that prevents correct sorting.

## What We've Implemented

We have implemented the cell-view selection sort based on the specification in your paper (Page 8, Methods section):

> **Cell-view Selection Sort**
> 1. Each cell has an ideal target position to which it wants to move. The initial value of the ideal position for all the cells is the most left position.
> 2. Each cell can view and swap with the cell that currently occupies its ideal position.
> 3. If the value of the active cell is smaller than the value of the cell occupying the active cell's ideal target position, the active cell swaps places with that occupying cell.

We have also examined the reference implementation in your GitHub repository (https://github.com/Zhangtaining/cell_research), specifically `modules/multithread/SelectionSortCell.py`.

## The Problem

Our implementation fails to correctly sort arrays. Here is a concrete example:

### Test Case
**Input array:** `[3, 1, 4, 1, 5, 9, 2, 6]`
**Expected result:** `[1, 1, 2, 3, 4, 5, 6, 9]`
**Actual result:** `[1, 1, 4, 3, 5, 9, 2, 6]`

### Execution Trace

**Timestep 0:**
- Initial state: `values=[3, 1, 4, 1, 5, 9, 2, 6]`, `ideal_pos=[0, 0, 0, 0, 0, 0, 0, 0]`
- Cell at position 3 (value=1) swaps with position 0 (value=3)
- Result: `values=[1, 1, 4, 3, 5, 9, 2, 6]`, `ideal_pos=[0, 0, 1, 0, 1, 1, 1, 1]`

**Timestep 1:**
- All cells with `ideal_pos > 0` now want position 1, which contains value=1
- None of these cells can swap because no value is smaller than 1
- All cells increment their `ideal_position`
- Result: No swaps occur

**Termination:**
- Algorithm terminates because `swapped_any = False`
- Array remains incorrectly sorted: `[1, 1, 4, 3, 5, 9, 2, 6]`

### Root Cause

Once a minimum value (e.g., 1) occupies an early position, no other cell can displace it because the swap condition `cell.value < neighbor.value` cannot be satisfied. The algorithm gets "stuck" with cells unable to make progress, causing premature termination after only 1-2 swaps.

## What We've Tried

To resolve this issue, we have tested over 10 different variations of the algorithm:

1. **ideal_position management:**
   - Swapping `ideal_positions` when cells swap (per your specification)
   - Not swapping `ideal_positions` (per GitHub implementation)
   - Resetting both cells' `ideal_position` to 0 after swap
   - Resetting only the displaced cell's `ideal_position` to 0
   - Periodic global resets of all `ideal_positions`

2. **Comparison logic variations:**
   - Standard: `if cell.value < neighbor.value`
   - Inverted: `if neighbor.value < cell.value`
   - Directional: different comparisons for leftward vs. rightward movement

3. **Termination conditions:**
   - Persistent retrying (reset and try again when no swaps occur)
   - Multiple failed passes before giving up

**All variations produce incorrect sorting results.**

## Critical Missing Information

The paper's description and the GitHub implementation appear to be missing crucial details:

### Questions We Need Answered

1. **After a successful swap, what happens to `ideal_position` for both cells?**
   - Does the initiating cell's `ideal_position` swap with the displaced cell's?
   - Does one or both reset to 0?
   - Does neither change?

2. **After an unsuccessful comparison (no swap), how does `ideal_position` change?**
   - Simply increment by 1?
   - Reset to some value?
   - Something else?

3. **How does the algorithm avoid getting "stuck"?**
   - In our implementation, once minimum values occupy early positions, other cells cannot displace them
   - Is there a mechanism we're missing that allows cells to continue making progress?

4. **In the multithreaded GitHub implementation:**
   - When/how is the `update()` method called that resets `ideal_position`?
   - How does continuous threading differ from our timestep-based simulation?
   - Are there implicit behaviors from the threading model that affect the algorithm?

5. **Termination condition:**
   - Should the algorithm terminate when no swaps occur in a timestep?
   - Or should it continue (perhaps with resets) until reaching some other condition?

6. **Is there additional logic not mentioned in the specification?**
   - Do cells need to recognize when positions are "locked in"?
   - Is there a mechanism to skip over already-sorted portions?
   - Are there implicit rules about cell behavior we're missing?

## Additional Context

Our implementations of cell-view bubble sort and insertion sort work correctly and produce results matching the expected behavior. This suggests our overall framework is sound, but we're missing something specific to the selection sort algorithm.

## Request

Could you please provide:

1. **Complete pseudocode** or detailed step-by-step specification for the cell-view selection sort algorithm, including all conditions for updating `ideal_position`

2. **Clarification** on the differences between the specification in the paper and the multithreaded implementation in your GitHub repository

3. **Example trace** showing expected behavior on a small test array (e.g., `[3, 1, 4, 1, 5]`) including:
   - Initial state
   - Each timestep's swaps
   - `ideal_position` values after each timestep
   - Termination condition

4. **Any implicit assumptions** about the algorithm that may not be obvious from the paper's description

## Code Availability

We have documented our investigation and all tested variations in detail. If it would be helpful, we can share our implementation attempts for your review to identify what we might be doing incorrectly.

## Appreciation

Thank you for your groundbreaking work on minimal models of morphogenesis and collective intelligence. We find the paper's concepts fascinating and are eager to successfully replicate your experiments. Any clarification you can provide would be greatly appreciated.

Best regards,

---

**Contact Information:**
[Your contact information to be added here]

**Repository (if applicable):**
[Link to your replication repository]
