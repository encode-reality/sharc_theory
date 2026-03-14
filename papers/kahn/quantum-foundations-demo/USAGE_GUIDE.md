# Usage Guide — Quantum Foundations Through Code

This guide shows how to use each module in the project, how the pieces connect, and how to produce the final blog assets. Work through it top to bottom to follow the pedagogical progression, or jump to any section as a reference.

All examples assume you're working from within the `quantum-foundations-demo/` directory and that `src/` is on your Python path. In a notebook, start with:

```python
import sys
sys.path.insert(0, '../src')  # or './src' if running from the project root
import numpy as np
```

---

## 1. Classical Probability — `quantum_demo.classical`

This module establishes the baseline that quantum mechanics departs from.

```python
from quantum_demo.classical import (
    normalize_probabilities,
    sample_classical,
    apply_stochastic_matrix,
    indicator_distribution,
)

# A probability vector: nonnegative, sums to 1
p = normalize_probabilities(np.array([3.0, 1.0]))
print(p)  # [0.75, 0.25]

# Sample from it (reproducible with a seeded RNG)
rng = np.random.default_rng(42)
outcome = sample_classical(p, rng=rng)
print(outcome)  # 0 or 1

# Deterministic state: all weight on outcome 0
delta = indicator_distribution(0, dim=3)
print(delta)  # [1. 0. 0.]

# Stochastic update: T @ p
T = np.array([[0.9, 0.2],
              [0.1, 0.8]])  # columns sum to 1
p_next = apply_stochastic_matrix(p, T)
print(p_next)  # new distribution
```

**Key point for later contrast**: classical probabilities are nonnegative, sum to 1, and have no notion of phase or sign.

---

## 2. Linear Algebra Helpers — `quantum_demo.linalg`

Low-level building blocks used by every other module.

```python
from quantum_demo.linalg import normalize, is_normalized, ket, dagger, is_unitary, projectors_from_basis

# Basis vector |1> in 2D
v = ket(1, dim=2)
print(v)  # [0.+0.j  1.+0.j]

# Normalize an arbitrary vector
w = normalize(np.array([3.0, 4.0], dtype=complex))
print(is_normalized(w))  # True

# Conjugate transpose
M = np.array([[1, 1j], [0, 1]])
print(dagger(M))

# Check unitarity (e.g., Hadamard)
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
print(is_unitary(H))  # True

# Computational basis projectors |i><i|
projs = projectors_from_basis(dim=2)
# projs[0] = |0><0|, projs[1] = |1><1|
```

---

## 3. Quantum States — `quantum_demo.states`

Create and inspect quantum state vectors.

```python
from quantum_demo.states import (
    basis_state,
    qubit_state,
    equal_superposition,
    amplitudes_to_probabilities,
    pretty_basis_labels,
)

# Computational basis states
ket0 = basis_state(0, dim=2)  # |0>
ket1 = basis_state(1, dim=2)  # |1>

# Custom qubit state (auto-normalized)
psi = qubit_state(1, 1j)  # (|0> + i|1>) / sqrt(2)
print(psi)

# Equal superposition over 4 states
s = equal_superposition(dim=4)
print(s)  # [0.5, 0.5, 0.5, 0.5]

# Born rule: amplitude -> probability
probs = amplitudes_to_probabilities(psi)
print(probs)  # [0.5, 0.5]

# Labels for multi-qubit systems
labels = pretty_basis_labels(num_qubits=2)
print(labels)  # ['00', '01', '10', '11']
```

### Demo A — Same Probabilities, Different States

This is one of the project's key demonstrations:

```python
from quantum_demo.gates import H, apply_gate

plus  = qubit_state(1, 1)   # (|0> + |1>) / sqrt(2)
minus = qubit_state(1, -1)  # (|0> - |1>) / sqrt(2)

# Both give 50/50 measurement probabilities
print(amplitudes_to_probabilities(plus))   # [0.5, 0.5]
print(amplitudes_to_probabilities(minus))  # [0.5, 0.5]

# But they evolve differently under H
print(apply_gate(plus, H))   # -> |0>  (deterministic 0)
print(apply_gate(minus, H))  # -> |1>  (deterministic 1)
```

The sign that was invisible to measurement completely determined the outcome after further evolution.

---

## 4. Quantum Gates — `quantum_demo.gates`

Explicit gate matrices and application functions.

```python
from quantum_demo.gates import I2, X, Y, Z, H, S, T, CNOT, apply_gate, phase_oracle, diffusion_operator
from quantum_demo.linalg import is_unitary

# Gate constants are numpy arrays
print(X)   # [[0, 1], [1, 0]]
print(H)   # [[1/sqrt2, 1/sqrt2], [1/sqrt2, -1/sqrt2]]

# All gates are unitary
for name, gate in [("X", X), ("Z", Z), ("H", H), ("CNOT", CNOT)]:
    print(f"{name} unitary: {is_unitary(gate)}")

# Apply a gate to a state
psi = apply_gate(ket0, H)       # H|0> = |+>
psi = apply_gate(psi, Z)        # Z|+> = |->
psi = apply_gate(psi, H)        # H|-> = |1>

# Grover building blocks
oracle = phase_oracle(target_index=2, dim=8)  # flips sign of |2>
diffusion = diffusion_operator(dim=8)          # 2|s><s| - I
```

**Key point**: `Z` changes the sign of the `|1>` amplitude without changing measurement probabilities. This invisible phase change has real consequences under subsequent gates.

---

## 5. Measurement — `quantum_demo.measurement`

Simulated Born-rule measurement with collapse.

```python
from quantum_demo.measurement import measure_state, repeated_measurements

# Single measurement
psi = equal_superposition(dim=4)
rng = np.random.default_rng(42)

outcome, collapsed, probs = measure_state(psi, rng=rng)
print(f"Observed: |{outcome}>")
print(f"Probabilities were: {probs}")
print(f"Collapsed state: {collapsed}")

# Collapsed state always re-measures the same outcome
outcome2, _, _ = measure_state(collapsed, rng=rng)
assert outcome2 == outcome  # always true for collapsed states

# Empirical histogram over many shots
counts = repeated_measurements(psi, shots=10_000, rng=np.random.default_rng(0))
print(counts)  # e.g., {0: 2513, 1: 2487, 2: 2500, 3: 2500}
# Each shot measures the ORIGINAL state (no inter-shot collapse)
```

---

## 6. Interference — `quantum_demo.interference`

The conceptual centerpiece of the project.

```python
from quantum_demo.interference import (
    hadamard_interference_demo,
    path_amplitude_sum,
    compare_probability_vs_amplitude_combination,
)

# Full Hadamard interference walkthrough
demo = hadamard_interference_demo()
print("H|0> amplitudes:", demo['H_ket0'])         # [1/sqrt2, 1/sqrt2]
print("H|0> probs:", demo['H_ket0_probs'])         # [0.5, 0.5]
print("HH|0> = back to |0>:", demo['HH_ket0'])    # [1, 0] (constructive)
print("ZH|0> probs:", demo['Z_H_ket0_probs'])      # [0.5, 0.5] (same!)
print("HZH|0> = |1>:", demo['HZH_ket0'])           # [0, 1] (destructive on |0>)

# Path amplitude sums — the core quantum rule
amp, prob = path_amplitude_sum([0.5, 0.5])    # constructive
print(f"Constructive: amp={amp}, P={prob}")    # amp=1.0, P=1.0

amp, prob = path_amplitude_sum([0.5, -0.5])   # destructive
print(f"Destructive: amp={amp}, P={prob}")     # amp=0.0, P=0.0

# Full classical vs quantum comparison
comparison = compare_probability_vs_amplitude_combination()
print(comparison['explanation'])
print("Classical total:", comparison['classical_probs']['total'])       # 0.5
print("Quantum constructive:", comparison['quantum_constructive']['probability'])  # 1.0
print("Quantum destructive:", comparison['quantum_destructive']['probability'])    # 0.0
```

**Key insight**: classical probabilities can only add (0.25 + 0.25 = 0.5). Quantum amplitudes can cancel (0.5 - 0.5 = 0) or reinforce (0.5 + 0.5 = 1.0) before squaring to get probabilities.

---

## 7. Multi-Qubit Systems — `quantum_demo.tensor`

Tensor products for composing qubits.

```python
from quantum_demo.tensor import tensor, basis_state_bits, expand_single_qubit_gate

# Tensor product of two qubit states
psi_2q = tensor(ket0, ket1)   # |0> ⊗ |1> = |01>
print(psi_2q)                  # [0, 1, 0, 0]

# Basis state from bitstring
psi = basis_state_bits('101')  # |1> ⊗ |0> ⊗ |1>
print(len(psi))                # 8 (2^3)

# Lift a single-qubit gate to a multi-qubit system
# Apply X to qubit 0 (leftmost) of a 2-qubit system
X_full = expand_single_qubit_gate(X, target=0, num_qubits=2)
print(X_full.shape)  # (4, 4)

# Apply it: X on qubit 0 flips |00> to |10>
result = X_full @ basis_state_bits('00')
print(result)  # = |10>

# Apply H to qubit 1 (rightmost) of a 2-qubit system
H_q1 = expand_single_qubit_gate(H, target=1, num_qubits=2)
result = H_q1 @ basis_state_bits('00')
# = |0> ⊗ H|0> = |0> ⊗ |+> = (|00> + |01>) / sqrt(2)
```

---

## 8. Grover's Algorithm — `quantum_demo.grover`

Amplitude amplification from scratch.

```python
from quantum_demo.grover import (
    grover_iteration,
    grover_run,
    grover_optimal_iterations,
    target_probability_trajectory,
    reduced_grover_plane_coordinates,
)

dim = 8          # search space of 8 items
target = 3       # looking for item 3

# How many iterations to maximize target probability?
opt_iters = grover_optimal_iterations(dim)
print(f"Optimal iterations for N={dim}: {opt_iters}")  # 2

# Run Grover and get state at each step
states = grover_run(dim, target_index=target, iterations=opt_iters)
print(f"States collected: {len(states)}")  # 3 (initial + 2 iterations)

# Track target probability over iterations
probs = target_probability_trajectory(dim, target, iterations=opt_iters)
print(f"Target probability: {probs}")  # [0.125, ~0.78, ~0.95]

# 2D geometric coordinates for visualization
coords = [reduced_grover_plane_coordinates(s, target) for s in states]
for i, (x, y) in enumerate(coords):
    print(f"Iter {i}: target_component={x:.3f}, s_perp_component={y:.3f}")
```

### Demo C — Oracle Phase Flip Is Invisible Until Diffusion

```python
state = equal_superposition(dim)
before_oracle = state.copy()

# Oracle flips sign of target amplitude
oracle = phase_oracle(target, dim)
after_oracle = apply_gate(state, oracle)

# Probabilities are UNCHANGED after oracle
print(amplitudes_to_probabilities(before_oracle))  # all 0.125
print(amplitudes_to_probabilities(after_oracle))   # all 0.125 (!)

# But the signed amplitudes changed (target went negative)
print(np.real(before_oracle[target]))  # +0.354
print(np.real(after_oracle[target]))   # -0.354

# Diffusion converts that sign change into a probability boost
diffusion = diffusion_operator(dim)
after_diffusion = apply_gate(after_oracle, diffusion)
print(amplitudes_to_probabilities(after_diffusion)[target])  # ~0.78
```

---

## 9. Bloch Sphere — `quantum_demo.bloch`

Map single-qubit states to 3D coordinates.

```python
from quantum_demo.bloch import bloch_coordinates

print(bloch_coordinates(ket0))                    # (0, 0, 1)   — north pole
print(bloch_coordinates(ket1))                    # (0, 0, -1)  — south pole
print(bloch_coordinates(qubit_state(1, 1)))       # (1, 0, 0)   — +x (|+>)
print(bloch_coordinates(qubit_state(1, -1)))      # (-1, 0, 0)  — -x (|->)
print(bloch_coordinates(qubit_state(1, 1j)))      # (0, 1, 0)   — +y
```

---

## 10. Visualization — `quantum_demo.viz`

All plot functions return a `matplotlib.Figure` and can be saved with `save_figure`.

### Static Plots

```python
from quantum_demo.viz.static_plots import (
    plot_probabilities,
    plot_real_amplitudes,
    plot_complex_amplitudes,
    plot_qubit_state_2d,
    plot_classical_vs_quantum_panel,
)

# Probability bar chart
fig = plot_probabilities(np.array([0.7, 0.2, 0.1]), labels=['A', 'B', 'C'], title="My Distribution")

# Signed amplitude bars (shows phase/sign structure)
fig = plot_real_amplitudes(qubit_state(1, -1), labels=['|0>', '|1>'], title="|-> State")

# Complex amplitude decomposition (3-panel: real, imaginary, |amp|^2)
fig = plot_complex_amplitudes(qubit_state(1, 1j), labels=['|0>', '|1>'], title="Complex State")

# Unit-circle diagram for a real qubit state
fig = plot_qubit_state_2d(qubit_state(1, 1), title="Qubit on Unit Circle")

# Classical vs quantum side-by-side comparison (3-panel)
fig = plot_classical_vs_quantum_panel(
    classical_probs=np.array([0.5, 0.5]),
    quantum_state=qubit_state(1, -1),
    labels=['|0>', '|1>'],
    title="Classical vs Quantum",
)
```

### State Comparison Plots

```python
from quantum_demo.viz.state_plots import plot_state_comparison, plot_oracle_phase_demo

# Compare |+> and |-> side by side (amplitudes + probabilities)
fig = plot_state_comparison(
    states=[qubit_state(1, 1), qubit_state(1, -1)],
    state_labels=["|+>", "|->"],
    basis_labels=["|0>", "|1>"],
    title="Same Probabilities, Different States",
)

# Oracle phase flip demo (3 stages x 2 rows)
fig = plot_oracle_phase_demo(
    before_oracle=before_oracle,
    after_oracle=after_oracle,
    after_diffusion=after_diffusion,
    target_index=target,
    labels=[str(i) for i in range(dim)],
)
```

### Grover Plots

```python
from quantum_demo.viz.grover_plots import plot_grover_trajectory, plot_grover_plane

# Target probability vs iteration
fig = plot_grover_trajectory(probs, title="Grover: P(target) vs Iteration")

# 2D rotation geometry
fig = plot_grover_plane(coords, title="Grover Geometry in 2D Plane")
```

### Saving Figures

```python
from quantum_demo.viz.export import save_figure

# Save to PNG (default)
save_figure(fig, 'assets/blog/grover-trajectory')

# Save to both PNG and SVG
save_figure(fig, 'assets/blog/grover-trajectory', formats=['png', 'svg'])

# Custom DPI
save_figure(fig, 'assets/blog/grover-trajectory', formats=['png'], dpi=300)
```

---

## 11. Manim Scenes — `quantum_demo.manim_scenes`

Four animation scenes for polished educational videos. Requires `manim` to be installed.

```bash
# Render a scene (from the project root)
manim -pql src/quantum_demo/manim_scenes/intro_probability_vs_amplitude.py ProbabilityVsAmplitude
manim -pql src/quantum_demo/manim_scenes/interference_scene.py InterferenceScene
manim -pql src/quantum_demo/manim_scenes/qubit_geometry.py QubitGeometry
manim -pql src/quantum_demo/manim_scenes/grover_scene.py GroverGeometry
```

| Scene | Class Name | What It Shows |
|-------|-----------|---------------|
| `intro_probability_vs_amplitude.py` | `ProbabilityVsAmplitude` | Classical vs quantum state representation; squaring amplitudes; two states with same probs |
| `interference_scene.py` | `InterferenceScene` | Constructive and destructive interference; classical vs quantum comparison |
| `qubit_geometry.py` | `QubitGeometry` | Unit-circle vector rotation; live probability readout; H and Z gate effects |
| `grover_scene.py` | `GroverGeometry` | 2D Grover plane; oracle + diffusion reflections; rotating toward target |

Flags: `-pql` = preview + quality low (fast). Use `-pqh` for high quality, add `--format=gif` for GIF export.

---

## 12. Notebooks — Pedagogical Walkthrough

The notebooks are the primary way to experience the project. They follow the learning order:

```bash
jupyter lab notebooks/
```

| Notebook | What You'll Build Intuition For |
|----------|---------------------------------|
| `01_classical_probability` | What probability vectors look like; the baseline ontology |
| `02_qubit_state_vector` | Amplitudes ≠ probabilities; Demo A (same probs, different states) |
| `03_measurement_and_born_rule` | Measurement destroys amplitude info; empirical convergence |
| `04_interference` | The centerpiece: constructive/destructive interference; Demo B & D |
| `05_two_qubits_tensor_products` | How multi-qubit state spaces grow; tensor products |
| `06_basic_quantum_gates` | Gates act on amplitudes; phase changes matter; Demo C |
| `07_grover_geometry` | Grover as amplitude amplification via geometric rotation |
| `08_blog_asset_generation` | Export all figures to `assets/blog/` for Hugo embedding |

---

## 13. Generating Blog Assets

Notebook 08 is a deterministic export script. Run it to populate `assets/blog/`:

```bash
jupyter nbconvert --execute notebooks/08_blog_asset_generation.ipynb --to notebook
```

Or run it interactively in Jupyter. It will produce:

```
assets/blog/
├── probability-vs-amplitude.png
├── same-probabilities-different-states.png
├── interference-cancellation.png
├── oracle-phase-demo.png
├── grover-trajectory.png
├── grover-plane.png
└── qubit-geometry.png
```

These are referenced by the Hugo blog draft at `content/drafts/quantum-foundations-through-code.md`.

---

## 14. Running Tests

```bash
cd papers/kahn/quantum-foundations-demo
python -m pytest tests/ -v
```

The test suite covers:

| Test File | What It Validates |
|-----------|-------------------|
| `test_linalg.py` | Normalization, basis vectors, projectors, unitarity |
| `test_classical.py` | Probability normalization, sampling, stochastic matrices |
| `test_states.py` | State construction, Born rule, basis labels |
| `test_gates.py` | All gates are unitary, correct action on basis states, oracle, diffusion |
| `test_measurement.py` | Measurement collapse, reproducibility, statistical convergence |
| `test_interference.py` | Hadamard interference chain, path amplitude sums |
| `test_tensor.py` | Kronecker products, bitstring basis states, gate expansion |
| `test_grover.py` | Probability increases, optimal iterations, 2D coordinates, norm preservation |
| `test_bloch.py` | Known Bloch coordinates for cardinal states |

---

## Putting It All Together — A Complete Example

Here's a self-contained script that uses every layer of the project to run Grover's algorithm and visualize the result:

```python
import sys
sys.path.insert(0, 'src')
import numpy as np

from quantum_demo.states import equal_superposition, amplitudes_to_probabilities, pretty_basis_labels
from quantum_demo.gates import apply_gate, phase_oracle, diffusion_operator
from quantum_demo.grover import grover_run, grover_optimal_iterations, target_probability_trajectory, reduced_grover_plane_coordinates
from quantum_demo.viz.static_plots import plot_real_amplitudes
from quantum_demo.viz.grover_plots import plot_grover_trajectory, plot_grover_plane
from quantum_demo.viz.state_plots import plot_oracle_phase_demo
from quantum_demo.viz.export import save_figure

# Setup
dim = 8
target = 3
opt_iters = grover_optimal_iterations(dim)
labels = [str(i) for i in range(dim)]

# Run Grover
states = grover_run(dim, target, opt_iters)

# 1. Show amplitude evolution
for i, s in enumerate(states):
    fig = plot_real_amplitudes(s, labels=labels, title=f"Amplitudes after {i} iterations")
    save_figure(fig, f'assets/figures/grover_amps_iter{i}')

# 2. Target probability trajectory
probs = target_probability_trajectory(dim, target, opt_iters)
fig = plot_grover_trajectory(probs)
save_figure(fig, 'assets/figures/grover_trajectory')

# 3. Geometric view
coords = [reduced_grover_plane_coordinates(s, target) for s in states]
fig = plot_grover_plane(coords)
save_figure(fig, 'assets/figures/grover_plane')

# 4. Oracle phase flip demo (Demo C)
s0 = equal_superposition(dim)
oracle = phase_oracle(target, dim)
s1 = apply_gate(s0, oracle)
diffusion = diffusion_operator(dim)
s2 = apply_gate(s1, diffusion)
fig = plot_oracle_phase_demo(s0, s1, s2, target, labels=labels)
save_figure(fig, 'assets/figures/oracle_demo')

print(f"Grover found target {target} with P={probs[-1]:.3f} after {opt_iters} iterations")
```
