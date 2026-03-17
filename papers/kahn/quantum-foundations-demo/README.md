# Quantum Foundations Through Code

Learn the foundations of quantum mechanics by simulating amplitudes, measurement, and interference from scratch in Python.

This project builds the intuition needed for Grover's algorithm by contrasting classical probability distributions with quantum state vectors. It is **not** a production quantum SDK — it is a pedagogical project whose purpose is to make the mathematical structure of quantum mechanics visible through code.

## Core Thesis

- In classical probability, probabilities are primitive weights over observable outcomes.
- In quantum mechanics, **amplitudes** are primitive.
- Probabilities are **derived** from amplitudes via squared magnitude (Born rule).
- Because amplitudes can be signed and complex, they can **interfere**.
- This interference — not naive "parallelism" — is what enables distinctive quantum dynamics and quantum algorithms like Grover's.

## Quick Start

```bash
# From the repo root, activate the existing environment
# (this project uses the parent repo's venv)

# Run the tests
python -m pytest papers/kahn/quantum-foundations-demo/tests/ -v

# Launch notebooks
jupyter lab papers/kahn/quantum-foundations-demo/notebooks/
```

## Project Structure

```
quantum-foundations-demo/
├── src/quantum_demo/         # Reusable simulation modules
│   ├── linalg.py             # Linear algebra helpers
│   ├── classical.py          # Classical probability baseline
│   ├── states.py             # Quantum state vectors
│   ├── gates.py              # Quantum gates as matrices
│   ├── measurement.py        # Born rule measurement
│   ├── interference.py       # Interference demos
│   ├── tensor.py             # Multi-qubit tensor products
│   ├── grover.py             # Grover's amplitude amplification
│   ├── bloch.py              # Bloch sphere coordinates
│   ├── viz/                  # Visualization utilities
│   └── manim_scenes/         # Manim animation scenes
├── notebooks/                # Pedagogical Jupyter notebooks (01–08)
├── tests/                    # pytest test suite
├── assets/                   # Generated figures and animations
└── content/drafts/           # Hugo blog post draft
```

## Notebooks

The notebooks follow a deliberate pedagogical progression:

| # | Notebook | Concepts |
|---|---------|----------|
| 01 | Classical Probability | Probability vectors, stochastic updates, sampling |
| 02 | Qubit State Vector | Amplitudes, Born rule, same probs / different states |
| 03 | Measurement & Born Rule | Measurement, collapse, empirical convergence |
| 04 | Interference | Constructive/destructive interference, the key departure |
| 05 | Two Qubits & Tensor Products | Tensor products, computational basis |
| 06 | Basic Quantum Gates | H, X, Z, CNOT, unitarity, phase changes |
| 07 | Grover Geometry | Oracle, diffusion, amplitude amplification, 2D geometry |
| 08 | Blog Asset Generation | Export all figures for the blog post |

## Usage Guide

See **[USAGE_GUIDE.md](USAGE_GUIDE.md)** for a complete walkthrough of every module, function, and visualization — with runnable code examples showing how to use each piece and how they all connect.

## Design Principles

- **Clarity over performance**: explicit vectors and matrices, no framework abstractions
- **Mathematical transparency**: readers can inspect actual arrays at every step
- **Real-valued first**: start with real amplitudes for intuition, extend to complex where needed
- **Small dimensions**: 2-state and 4-state examples first
- **Reproducible**: seeded RNGs in all demos
- **No external quantum libraries**: built from scratch with numpy so readers see the underlying math

## Running Tests

```bash
cd papers/kahn/quantum-foundations-demo
python -m pytest tests/ -v
```

## Dependencies

All dependencies are managed by the parent repo's environment:
- numpy, matplotlib, jupyter, ipywidgets, pytest
- Optional: manim (for animation rendering)
