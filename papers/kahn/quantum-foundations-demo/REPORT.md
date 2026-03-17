# Build Report — Quantum Foundations Through Code

## Summary

Built a complete pedagogical quantum mechanics simulation project from spec, using Test-Driven Development throughout. The project constructs intuition for quantum mechanics by contrasting classical probability with quantum amplitudes, culminating in Grover's algorithm as amplitude amplification through interference.

## Deliverables Completed

### 1. Core Simulation Modules (9 modules)

All modules built with TDD — tests written first, then implementations verified.

| Module | Functions | Tests | Purpose |
|--------|-----------|-------|---------|
| `linalg.py` | 6 | 42 | Linear algebra helpers (normalize, ket, dagger, unitarity) |
| `classical.py` | 4 | 21 | Classical probability baseline |
| `states.py` | 5 | 32 | Quantum state vectors, Born rule |
| `gates.py` | 3 + 8 constants | 23 | Gate matrices (I, X, Y, Z, H, S, T, CNOT), oracle, diffusion |
| `measurement.py` | 2 | 16 | Measurement, collapse, repeated measurements |
| `interference.py` | 3 | 12 | Hadamard interference demo, path amplitude sums |
| `tensor.py` | 3 | 17 | Kronecker products, multi-qubit gates |
| `grover.py` | 5 | 11 | Grover iteration, trajectory, 2D geometry |
| `bloch.py` | 1 | 6 | Bloch sphere coordinates |

**Total: 180 tests, all passing.**

### 2. Visualization Modules (4 files)

| File | Functions | Purpose |
|------|-----------|---------|
| `viz/static_plots.py` | 5 | Probability bars, amplitude bars, complex amplitudes, qubit 2D, classical vs quantum panels |
| `viz/state_plots.py` | 2 | State comparison panels, oracle phase demo (Demo C) |
| `viz/grover_plots.py` | 2 | Grover trajectory plot, Grover 2D plane visualization |
| `viz/export.py` | 1 | Save figures to PNG/SVG |

### 3. Manim Animation Scenes (4 scenes)

| Scene | File | Learning Goal |
|-------|------|---------------|
| ProbabilityVsAmplitude | `intro_probability_vs_amplitude.py` | Probabilities are derived, not primitive |
| InterferenceScene | `interference_scene.py` | Interference is the key nonclassical feature |
| QubitGeometry | `qubit_geometry.py` | Single-qubit state as normalized vector |
| GroverGeometry | `grover_scene.py` | Grover is amplitude amplification via geometry |

### 4. Jupyter Notebooks (8 notebooks, 205 cells total)

| # | Notebook | Cells | Pedagogical Stage |
|---|---------|-------|-------------------|
| 01 | Classical Probability | 24 | Baseline: probability vectors, sampling, stochastic updates |
| 02 | Qubit State Vector | 23 | Amplitudes, Born rule, Demo A (same probs, different states) |
| 03 | Measurement & Born Rule | 22 | Measurement, collapse, empirical convergence |
| 04 | Interference | 31 | Centerpiece: constructive/destructive interference, Demo B |
| 05 | Two Qubits & Tensor Products | 29 | Tensor products, computational basis labeling |
| 06 | Basic Quantum Gates | 33 | Gates, unitarity, phase changes, Demo C (oracle phase flip) |
| 07 | Grover Geometry | 25 | Oracle, diffusion, amplitude amplification, 2D rotation |
| 08 | Blog Asset Generation | 18 | Deterministic export of all figures to assets/blog/ |

### 5. Blog Integration

- **Hugo draft**: `content/drafts/quantum-foundations-through-code.md` with embedded figure placeholders
- **Asset export**: Notebook 08 generates all blog figures to `assets/blog/`
- **Export utility**: `viz/export.py` supports PNG and SVG formats

### 6. Documentation

- **README.md**: Project overview, quick start, structure, design principles
- **This report**: `REPORT.md`

## Spec Coverage

### Required Demos

| Demo | Status | Location |
|------|--------|----------|
| Demo A: Same probabilities, different states | Done | Notebook 02 |
| Demo B: Constructive vs destructive interference | Done | Notebook 04, `interference.py` |
| Demo C: Oracle phase flip invisible until diffusion | Done | Notebook 06, `viz/state_plots.py` |
| Demo D: Classical cannot reproduce quantum update | Done | Notebook 04, `interference.py` |

### Required Test Categories

| Category | Status | File |
|----------|--------|------|
| Normalization tests | Done | `test_linalg.py`, `test_states.py` |
| Born rule tests | Done | `test_states.py`, `test_measurement.py` |
| Unitarity tests | Done | `test_gates.py`, `test_linalg.py` |
| Measurement collapse tests | Done | `test_measurement.py` |
| Grover probability increasing | Done | `test_grover.py` |

## Architecture Notes

- **No external quantum libraries**: everything built from scratch with numpy
- **Separation of concerns**: simulation logic has no plotting dependencies
- **Mathematical transparency**: explicit vectors and matrices throughout
- **Reproducible**: seeded RNGs in all stochastic operations
- **Uses parent repo's venv**: no separate pyproject.toml, integrates with existing environment
