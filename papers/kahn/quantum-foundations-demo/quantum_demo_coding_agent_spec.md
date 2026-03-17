# Quantum Foundations Through Code — Coding Agent Specification

## Objective

Build a Python project that **constructs the intuition for quantum mechanics through simulation code**, not through analogies alone. The goal is to create a sequence of code-driven demos that starts from simple linear algebra and probability, then shows where quantum mechanics departs from ordinary probability theory.

The core conceptual target is:

- In classical probability, probabilities are primitive weights over observable outcomes.
- In quantum mechanics, **amplitudes** are primitive.
- Probabilities are **derived** from amplitudes via squared magnitude.
- Because amplitudes can be signed and complex, they can **interfere**.
- This interference, not naive “parallelism,” is what enables distinctive quantum dynamics and eventually quantum algorithms like Grover.

The deliverables should support a Hugo blog post hosted on GitHub Pages. The codebase should therefore produce:

1. reusable Python functions,
2. static plots,
3. optional lightweight interactivity,
4. Manim animations for selected sections,
5. exported media/assets suitable for embedding in Hugo markdown.

---

## High-Level Product Requirements

Create a repo/project that can do the following:

1. **Simulate classical probability distributions** over finite state spaces.
2. **Simulate quantum state vectors** over finite-dimensional Hilbert spaces.
3. Show the distinction between:
   - probability evolution,
   - amplitude evolution,
   - measurement,
   - interference.
4. Build up from:
   - 1 classical bit vs 1 qubit,
   - 2-state systems,
   - tensor products / multiple qubits,
   - simple gates,
   - measurement,
   - amplitude amplification,
   - Grover-style geometric intuition.
5. Produce visual outputs that are pedagogically clean and blog-friendly.

The code should prioritize **clarity, inspectability, and mathematical transparency** over performance.

---

## Technical Stack

Use:

- **Python 3.11+**
- **numpy** for linear algebra
- **matplotlib** for static visualizations
- **ipywidgets** or **plotly** optionally for interactivity in notebooks
- **manim** for polished educational animations
- **Jupyter notebooks** for exploratory demos
- standard Python package layout for reusable modules

Optional:

- scipy for helper linear algebra if needed
- rich or textual only if needed for CLI demos, but keep optional

Do **not** rely on Qiskit/Cirq/PennyLane for the core educational logic. The point is to build the important mechanics **from scratch** so readers can see the underlying math directly.

External quantum libraries may be used only later for validation comparisons, and should be isolated from the core educational code.

---

## Repository Structure

Use a structure close to the following:

```text
quantum-foundations-demo/
├─ README.md
├─ pyproject.toml
├─ requirements.txt
├─ .gitignore
├─ src/
│  └─ quantum_demo/
│     ├─ __init__.py
│     ├─ linalg.py
│     ├─ classical.py
│     ├─ states.py
│     ├─ gates.py
│     ├─ measurement.py
│     ├─ interference.py
│     ├─ tensor.py
│     ├─ grover.py
│     ├─ bloch.py
│     ├─ viz/
│     │  ├─ __init__.py
│     │  ├─ static_plots.py
│     │  ├─ state_plots.py
│     │  ├─ grover_plots.py
│     │  └─ export.py
│     └─ manim_scenes/
│        ├─ __init__.py
│        ├─ intro_probability_vs_amplitude.py
│        ├─ qubit_geometry.py
│        ├─ interference_scene.py
│        └─ grover_scene.py
├─ notebooks/
│  ├─ 01_classical_probability.ipynb
│  ├─ 02_qubit_state_vector.ipynb
│  ├─ 03_measurement_and_born_rule.ipynb
│  ├─ 04_interference.ipynb
│  ├─ 05_two_qubits_tensor_products.ipynb
│  ├─ 06_basic_quantum_gates.ipynb
│  ├─ 07_grover_geometry.ipynb
│  └─ 08_blog_asset_generation.ipynb
├─ assets/
│  ├─ figures/
│  ├─ animations/
│  ├─ gifs/
│  └─ blog/
└─ content/
   └─ drafts/
      └─ quantum-foundations-through-code.md
```

---

## Core Pedagogical Progression

The demos should be organized in the following learning order.

### Stage 1 — Classical probability as the baseline

Implement a minimal classical finite-state probability model.

Concepts to demonstrate:
- finite sample spaces
- probability vectors
- normalization
- stochastic updates
- direct sampling from observable probabilities

The reader should clearly see that in the classical picture:
- the state is already a probability distribution,
- probabilities are nonnegative,
- probabilities sum to 1,
- there is no notion of phase,
- there is no interference.

### Stage 2 — Introduce amplitudes

Create a quantum state representation for finite-dimensional systems.

Concepts to demonstrate:
- state vector as complex vector
- normalization under L2 norm
- basis states
- Born rule: probability = squared magnitude
- amplitudes are not probabilities

The first important contrast demo should show two different state vectors with the same measurement probabilities but different signs/phases.

### Stage 3 — Interference

Create minimal examples where amplitudes combine and produce:
- reinforcement
- cancellation

This must be a centerpiece of the project.

Key pedagogical requirement:
show that two processes can yield identical classical probabilities at one intermediate stage, yet later evolve differently because the quantum states retained phase/sign structure that classical probabilities cannot represent.

### Stage 4 — Gates as linear transformations

Implement common gates as explicit matrices.

At minimum:
- Identity
- X / bit-flip
- Z / phase-flip
- H / Hadamard
- CNOT
- optional phase gates S and T

Demonstrate:
- unitary evolution preserves norm
- gates act on amplitudes, not probabilities directly
- sign/phase manipulations matter even when immediate probabilities do not change

### Stage 5 — Measurement and collapse

Implement measurement explicitly.

Demonstrate:
- probability extraction from amplitudes
- random sampling from the Born distribution
- post-measurement state collapse
- repeated measurement after collapse yields same result in projective measurement of same basis

### Stage 6 — Multi-qubit state spaces

Implement tensor products and basis labeling.

Demonstrate:
- how 2 qubits lead to 4-dimensional state vectors
- computational basis labeling |00>, |01>, |10>, |11>
- how amplitudes distribute across basis states
- optional entanglement preview, but keep it secondary to the amplitudes/probabilities story

### Stage 7 — Grover-style amplitude amplification

Implement a minimal search-space demo.

Requirements:
- construct equal superposition state
- oracle flips sign of target basis state amplitude
- diffusion operator reflects around equal superposition
- show repeated iterations amplify target probability
- include geometric interpretation in 2D reduced subspace

This section should explicitly support the blog’s thesis that the advantage is not “checking every possibility and reading them all out,” but **using interference to reshape amplitudes before measurement**.

---

## Required Modules and Functions

Below is the minimum function-level design. Refactor as needed, but keep equivalent functionality.

## `src/quantum_demo/linalg.py`

Purpose: small transparent linear algebra helpers.

Required functions:

```python
def normalize(vec: np.ndarray) -> np.ndarray:
    """Return vec normalized to unit L2 norm."""


def is_normalized(vec: np.ndarray, atol: float = 1e-9) -> bool:
    """Check whether vec has unit L2 norm."""


def ket(index: int, dim: int, dtype=np.complex128) -> np.ndarray:
    """Return computational basis vector |index> in C^dim."""


def projectors_from_basis(dim: int) -> list[np.ndarray]:
    """Return computational basis projectors |i><i| for i in range(dim)."""


def dagger(mat: np.ndarray) -> np.ndarray:
    """Conjugate transpose."""


def is_unitary(mat: np.ndarray, atol: float = 1e-9) -> bool:
    """Check U^† U = I."""
```

## `src/quantum_demo/classical.py`

Purpose: classical probability baseline.

Required functions:

```python
def normalize_probabilities(p: np.ndarray) -> np.ndarray:
    """Normalize nonnegative vector to sum to 1."""


def sample_classical(p: np.ndarray, rng: np.random.Generator | None = None) -> int:
    """Sample an index according to a classical probability distribution."""


def apply_stochastic_matrix(p: np.ndarray, T: np.ndarray) -> np.ndarray:
    """Apply stochastic transition matrix to probability vector."""


def indicator_distribution(index: int, dim: int) -> np.ndarray:
    """Deterministic classical state concentrated at one outcome."""
```

## `src/quantum_demo/states.py`

Purpose: state creation and basis utilities.

Required functions:

```python
def basis_state(index: int, dim: int) -> np.ndarray:
    """Alias for computational basis state."""


def qubit_state(alpha: complex, beta: complex) -> np.ndarray:
    """Create normalized 1-qubit state alpha|0> + beta|1>."""


def equal_superposition(dim: int) -> np.ndarray:
    """Uniform amplitude state over computational basis."""


def amplitudes_to_probabilities(state: np.ndarray) -> np.ndarray:
    """Born probabilities from amplitude vector."""


def pretty_basis_labels(num_qubits: int) -> list[str]:
    """Return ['00', '01', ...] labels for computational basis."""
```

## `src/quantum_demo/gates.py`

Purpose: explicit gate construction and application.

Required constants / functions:

```python
I2 = ...
X = ...
Y = ...
Z = ...
H = ...
S = ...
T = ...
CNOT = ...


def apply_gate(state: np.ndarray, gate: np.ndarray) -> np.ndarray:
    """Apply unitary to state."""


def phase_oracle(target_index: int, dim: int) -> np.ndarray:
    """Diagonal oracle that flips sign of target basis amplitude only."""


def diffusion_operator(dim: int) -> np.ndarray:
    """Grover diffusion operator: 2|s><s| - I where |s> is equal superposition."""
```

## `src/quantum_demo/measurement.py`

Purpose: measurement operations.

Required functions:

```python
def measure_state(
    state: np.ndarray,
    rng: np.random.Generator | None = None,
) -> tuple[int, np.ndarray, np.ndarray]:
    """
    Sample one computational basis outcome.
    Return (observed_index, collapsed_state, probabilities).
    """


def repeated_measurements(
    state: np.ndarray,
    shots: int,
    rng: np.random.Generator | None = None,
) -> dict[int, int]:
    """Empirical measurement histogram."""
```

## `src/quantum_demo/interference.py`

Purpose: build canonical demos showing why amplitudes are richer than probabilities.

Required functions:

```python
def hadamard_interference_demo() -> dict:
    """
    Return intermediate states showing H|0>, HZH|0>, HH|0>, etc.
    Use this to demonstrate constructive and destructive interference.
    """


def path_amplitude_sum(contributions: list[complex]) -> tuple[complex, float]:
    """Sum amplitudes first, then square magnitude."""


def compare_probability_vs_amplitude_combination() -> dict:
    """
    Build a tiny example showing that classical probabilities only add,
    whereas signed/complex amplitudes can cancel or reinforce.
    """
```

## `src/quantum_demo/tensor.py`

Purpose: multi-qubit composition.

Required functions:

```python
def tensor(*arrays: np.ndarray) -> np.ndarray:
    """Kronecker product of arbitrary number of arrays."""


def basis_state_bits(bits: str) -> np.ndarray:
    """Return basis state corresponding to bitstring, e.g. '101'."""


def expand_single_qubit_gate(gate: np.ndarray, target: int, num_qubits: int) -> np.ndarray:
    """Lift single-qubit gate to full Hilbert space."""
```

## `src/quantum_demo/grover.py`

Purpose: amplitude amplification and geometry.

Required functions:

```python
def grover_iteration(state: np.ndarray, target_index: int) -> np.ndarray:
    """Apply oracle then diffusion."""


def grover_run(dim: int, target_index: int, iterations: int) -> list[np.ndarray]:
    """Return sequence of states from initialization through iterations."""


def grover_optimal_iterations(dim: int) -> int:
    """Return nearest integer to pi/4 * sqrt(dim)."""


def target_probability_trajectory(dim: int, target_index: int, iterations: int) -> np.ndarray:
    """Probability of marked state across iterations."""


def reduced_grover_plane_coordinates(state: np.ndarray, target_index: int) -> tuple[float, float]:
    """
    Project state into the 2D plane spanned by |target> and equal superposition of non-target states.
    Return coordinates for geometric plotting.
    """
```

## `src/quantum_demo/bloch.py`

Purpose: optional Bloch-sphere-oriented helpers for single qubit intuition.

Required functions:

```python
def bloch_coordinates(state: np.ndarray) -> tuple[float, float, float]:
    """Map normalized 1-qubit state to Bloch coordinates."""
```

This is optional in the blog narrative, but useful for visualization.

---

## Visualization Requirements

The visual layer matters a lot. Build visualizations that make the conceptual distinctions explicit.

## Static plots

Create functions for:

1. **Probability bar chart**
   - input: probability vector
   - output: labeled bar chart

2. **Amplitude bar chart**
   - input: complex state vector
   - output: separate plots or stacked visual encoding for:
     - real part
     - imaginary part
     - magnitude squared

3. **Signed amplitude plot**
   - specifically for real-valued educational states
   - bar chart showing positive and negative values centered on zero
   - to make phase/sign visible where probabilities would hide it

4. **Qubit unit-circle / Bloch-inspired 2D state plot**
   - for purely real qubit examples, show vector on unit circle
   - overlay corresponding measurement probabilities

5. **Grover target probability trajectory**
   - x-axis: iteration
   - y-axis: probability of target state

6. **Grover 2D plane visualization**
   - draw reduced 2D plane
   - show equal superposition vector
   - show target axis
   - show state rotation through repeated oracle + diffusion steps

7. **Classical vs quantum comparison panels**
   - e.g. left: classical probability update
   - right: amplitude evolution + measured probabilities

## Minimal required plotting API

In `viz/static_plots.py` and related files implement at least:

```python
def plot_probabilities(probabilities: np.ndarray, labels: list[str] | None = None, title: str = ""):
    ...


def plot_real_amplitudes(state: np.ndarray, labels: list[str] | None = None, title: str = ""):
    ...


def plot_complex_amplitudes(state: np.ndarray, labels: list[str] | None = None, title: str = ""):
    ...


def plot_qubit_state_2d(state: np.ndarray, title: str = ""):
    ...


def plot_grover_trajectory(probabilities: np.ndarray, title: str = ""):
    ...


def plot_grover_plane(coords: list[tuple[float, float]], title: str = ""):
    ...
```

All plotting functions should support export to PNG and SVG.

---

## Manim Animation Requirements

Use Manim for a few high-value scenes only. Do not overbuild.

### Scene 1 — Probability vs amplitude

Animation idea:
- show a classical distribution over two states
- then show a quantum state with amplitudes instead
- animate squaring magnitudes into probabilities
- show two distinct amplitude vectors with same probabilities

Learning goal:
probabilities are derived, not primitive.

### Scene 2 — Interference

Animation idea:
- show two amplitude contributions merging
- first in-phase contributions add
- then opposite-sign contributions cancel
- compare with classical probability addition, which cannot cancel

Learning goal:
interference is the key nonclassical feature.

### Scene 3 — Real-valued qubit geometry

Animation idea:
- vector rotating on unit circle
- live display of probabilities for |0> and |1>
- optional application of H and Z on simple states

Learning goal:
single-qubit state as normalized vector; probabilities from squared projections.

### Scene 4 — Grover geometry

Animation idea:
- equal superposition vector
- oracle reflection
- diffusion reflection
- resulting rotation toward target
- growing target probability bar

Learning goal:
Grover is amplitude amplification via geometry/interference, not brute-force parallel inspection.

All Manim scenes should render to MP4 and optionally GIF snippets for Hugo embedding.

---

## Notebook Requirements

Each notebook should be narrative and reproducible. Use markdown cells to explain what the code is demonstrating.

### `01_classical_probability.ipynb`
- define classical probability vectors
- sample from them
- apply stochastic updates
- establish baseline ontology

### `02_qubit_state_vector.ipynb`
- define basis states
- define qubit states
- map amplitudes to probabilities
- show same probabilities, different states

### `03_measurement_and_born_rule.ipynb`
- implement measurement
- show empirical frequencies converge to Born probabilities
- show collapse

### `04_interference.ipynb`
- Hadamard-based interference demos
- path-sum toy examples
- explicit contrast with classical probability addition

### `05_two_qubits_tensor_products.ipynb`
- tensor products
- 4D state vectors
- basis labeling
- simple two-qubit state construction

### `06_basic_quantum_gates.ipynb`
- matrix action of H, X, Z, CNOT
- norm preservation
- phase changes with unchanged immediate probabilities

### `07_grover_geometry.ipynb`
- build oracle
- build diffusion operator
- iterate
- plot marked-state probability trajectory
- plot reduced 2D rotation geometry

### `08_blog_asset_generation.ipynb`
- deterministic asset export script
- generate all final figures/animations used in blog
- write outputs into `assets/blog/`

---

## Specific Demo Ideas That Must Exist

These should be implemented directly because they encode the main thesis of the post.

### Demo A — Same probabilities, different quantum states

Use states like:

- \((|0\rangle + |1\rangle)/\sqrt{2}\)
- \((|0\rangle - |1\rangle)/\sqrt{2}\)

Show that both yield 50/50 measurement in the computational basis.
Then apply another Hadamard and show:

- first goes to \(|0\rangle\)
- second goes to \(|1\rangle\)

This is one of the cleanest demonstrations that amplitudes retain meaningful structure hidden from raw probabilities.

### Demo B — Constructive vs destructive interference

Create explicit path-contribution examples, such as:

- contributions `[1/2, 1/2]` -> total amplitude `1` -> probability `1`
- contributions `[1/2, -1/2]` -> total amplitude `0` -> probability `0`

Use this as a bridge from abstract algebra to intuition.

### Demo C — Oracle phase flip is invisible at first glance

For Grover, show:
- before oracle: probability bars unchanged
- after oracle: probability bars still unchanged
- but signed amplitude plot changed
- after diffusion: target probability increases

This directly supports the conceptual point that sign/phase changes matter even when they do not immediately change measurement probabilities.

### Demo D — Classical probability cannot reproduce the same update law

Construct a side-by-side where:
- classical distribution remains unchanged under a sign-like operation because such an operation is not even meaningful there,
- quantum amplitude state evolves differently under subsequent unitary action because of sign/phase.

This should be one of the strongest comparative visuals in the whole project.

---

## Blog Integration Requirements (Hugo + GitHub Pages)

The final system must support embedding outputs into a Hugo blog.

Requirements:

1. Export figures with deterministic file names.
2. Export animations as MP4 and lightweight GIF/WebP where appropriate.
3. Create one draft blog markdown file containing placeholders for:
   - conceptual explanation,
   - embedded figures,
   - code snippets,
   - links to notebooks/repo.
4. Prefer Hugo shortcodes or standard markdown image/video embedding compatible with GitHub Pages hosting.

### Asset strategy

Expected Hugo-compatible output layout should be something like:

```text
static/posts/quantum-foundations/
├─ probability-vs-amplitude.png
├─ same-probabilities-different-states.png
├─ interference-cancellation.png
├─ grover-trajectory.png
├─ grover-plane.png
├─ qubit-geometry.mp4
└─ grover-geometry.mp4
```

If the local repo layout differs, keep an export script that can sync/copy into the Hugo site structure.

---

## Code Quality Requirements

The repo is educational, so code should be:

- small and explicit
- heavily type hinted
- documented with docstrings
- mathematically annotated where helpful
- accompanied by simple tests

Add a minimal `tests/` directory with at least:

- normalization tests
- Born rule tests
- unitarity tests
- measurement collapse tests
- Grover target probability increasing for early iterations

Suggested tests:

```text
tests/
├─ test_linalg.py
├─ test_states.py
├─ test_measurement.py
├─ test_gates.py
└─ test_grover.py
```

---

## Implementation Notes and Constraints

1. **Keep the first version real-valued where possible** for intuition.
   - especially for qubit geometry and Grover
   - then extend to complex amplitudes in selected examples

2. **Do not hide the math behind framework abstractions.**
   - explicit vectors and matrices are preferred
   - readers should be able to inspect actual arrays

3. **Keep dimensions small in visual demos.**
   - 2-state and 4-state examples first
   - use larger dimensions only for trajectory plots where basis bars remain readable

4. **Be consistent with basis ordering.**
   - standard computational basis ordering
   - document clearly

5. **Make random processes reproducible.**
   - pass numpy RNGs explicitly or set seeds in demos

6. **Separate simulation logic from presentation logic.**
   - reusable core functions should not depend on plotting code

---

## Stretch Goals

Only do these after the core flow works.

1. Bloch sphere 3D interactive visualization
2. entanglement preview notebook
3. double-slit-inspired amplitude simulator on finite lattice
4. simple Shor-related phase intuition demo
5. browser-friendly interactive widgets exported to blog where feasible

These are optional and must not distract from the main amplitudes-vs-probabilities narrative.

---

## Suggested README Framing

The README should explain that this repo is not a production quantum SDK. It is a pedagogical project whose purpose is to make the mathematical structure of quantum mechanics visible through code.

Suggested positioning:

- “Learn the foundations of quantum mechanics by simulating amplitudes, measurement, and interference from scratch in Python.”
- “This project builds the intuition needed for Grover’s algorithm by contrasting classical probability distributions with quantum state vectors.”

---

## Final Deliverables Expected From Agent

The coding agent should produce:

1. the full repo scaffold,
2. core simulation modules,
3. notebooks in pedagogical order,
4. static visualization utilities,
5. at least 2–4 Manim scenes,
6. export pipeline for blog assets,
7. a draft Hugo blog markdown file with embedded asset placeholders,
8. minimal tests,
9. setup instructions in README.

---

## Final Conceptual Standard

The project is successful if a technically literate reader can run the notebooks and come away with the following intuition:

- a quantum state is not a probability distribution,
- amplitudes are more primitive than probabilities,
- phase/sign information survives where probabilities do not,
- interference is the essential new dynamic,
- Grover’s algorithm works by **amplitude amplification** through interference and geometry, not by simply checking every candidate “in parallel” and reading them all out.

That conceptual result matters more than flashy visuals or breadth of features.

