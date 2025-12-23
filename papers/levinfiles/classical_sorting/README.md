# Classical Sorting Algorithms as a Model of Morphogenesis

This directory contains a complete replication and extension of the sorting algorithms research from Zhang, Goldstein, and Levin (2024).

## Directory Structure

```
classical_sorting/
├── modules/                    # Core implementation
│   ├── cell_view_sorts.py     # Main sorting algorithms
│   ├── core.py                # Data structures (Cell, StepCounter)
│   ├── metrics.py             # Sortedness calculation
│   ├── visualization.py       # Plotting functions
│   └── experiments.py         # Experiment functions
│
├── tests/                      # All test files
│   ├── test_*.py              # Unit and integration tests
│   ├── validate_experiments.py # Validation suite
│   └── diagnostics/           # Debug and analysis scripts
│
├── scripts/                    # Utility scripts
│   ├── *_cell*.py             # Notebook manipulation
│   ├── verify_*.py            # Verification scripts
│   └── check_*.py             # Structure checking
│
├── docs/                       # Documentation
│   ├── EXPERIMENT_PLAN.md     # Original plan
│   ├── EXPERIMENT6_ADDED.md   # Experiment 6 docs
│   ├── INSERTION_SORT_FIX.md  # Insertion sort debugging
│   ├── replication_summary.md # Replication notes
│   └── 2401.05375v1.pdf       # Original paper
│
├── figures/                    # Generated plots
├── reference_implementation/   # Original authors' code
│
├── morphogenesis_experiments.ipynb  # Main research notebook
└── validation_results.json          # Test results
```

## Quick Start

### Running the Notebook
```bash
jupyter notebook morphogenesis_experiments.ipynb
```

### Running Tests
```bash
# Run main validation
python tests/validate_experiments.py

# Run specific test
python tests/test_implementation.py

# Run notebook experiment tests
python tests/test_notebook_experiments.py
```

### Running Diagnostics
```bash
# Analyze algorithm stopping points
python tests/diagnostics/analyze_stopping_points.py

# Debug insertion sort with frozen cells
python tests/diagnostics/diagnose_insertion_n20.py
```

## Key Files

| File | Purpose |
|------|---------|
| `morphogenesis_experiments.ipynb` | Main research presentation notebook |
| `modules/cell_view_sorts.py` | Cell-autonomous sorting algorithms |
| `tests/validate_experiments.py` | Comprehensive validation suite |
| `tests/test_notebook_experiments.py` | Test all notebook experiments |
| `docs/EXPERIMENT6_ADDED.md` | Documentation for dynamics experiment |
| `docs/INSERTION_SORT_FIX.md` | Insertion sort frozen cell issue analysis |

## Experiments

The notebook contains 6 experiments:

1. **Basic Sorting** - Verify algorithms work correctly
2. **Dynamics Visualization** - Sortedness progression over time
3. **Array Size Comparison** - Efficiency across different sizes
4. **Frozen Cell Robustness** - Resilience to cell damage
5. **Chimeric Arrays** - Mixed algorithm cooperation
6. **Frozen Cell Dynamics** - Recovery trajectory analysis

## Implementation Notes

- All algorithms are cell-autonomous (no central controller)
- Frozen cells model biological damage/dysfunction
- Selection Sort includes group merging mechanism
- Supports mixed algotype (chimeric) arrays
- Compatible with Python 3.12+

## Validation Status

✓ All three algorithms achieve 100% sortedness on standard arrays
✓ Selection Sort group merging verified
✓ Frozen cell handling validated
✓ Chimeric array cooperation tested
✓ All notebook experiments validated

See `validation_results.json` for detailed results.

## Research Context

This implementation replicates experiments from:

> Zhang, T., Goldstein, A., & Levin, M. (2024). "Classical Sorting Algorithms as a Model of Morphogenesis: self-sorting arrays reveal unexpected competencies in a minimal model of basal intelligence." *Adaptive Behavior*, DOI: 10.1177/10597123241269740

The research demonstrates that distributed sorting algorithms exhibit emergent properties characteristic of biological intelligence: robustness, collective problem-solving, and cooperation among heterogeneous agents.

## Contact

For questions about this implementation, see the documentation in `docs/`.
