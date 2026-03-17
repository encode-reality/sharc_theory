# SHARC Theory

**Scaled Hierarchical and Recursive Competencies** — a research project exploring how hierarchical systems evolve, adapt, and interact across scales, from molecular dynamics to societal organization.

The project combines computational models, formal essays, and curated research to investigate the principles governing complex systems: evolutionary dynamics, non-equilibrium thermodynamics, information theory, and the structure of intelligence and creativity.

Blog: [encodereality.com](https://encodereality.com/)

---

## Repository Structure

```
sharc_theory/
    content/          Blog posts (Hugo)
    experiments/      Runnable code supporting blog essays
    models/           Standalone computational models
    papers/           Research manuscripts, citations, and demos
    media/            Curated transcripts and analysis of talks/interviews
    static/           Images and assets served by the blog
    layouts/          Hugo template overrides
    themes/           Hugo themes (PaperMod)
```

---

## Blog (`content/posts/`)

The blog at [encodereality.com](https://encodereality.com/) publishes essays grounded in formal reasoning and supported by computational experiments. Current posts:

| Post | Topics | Status |
|------|--------|--------|
| [Toward a Science of Politics](https://encodereality.com/posts/societies-as-complex-systems/) | Non-equilibrium thermodynamics, cybernetics, dissipative systems | Published |
| [The Paradox of Individualism](https://encodereality.com/posts/paradox_of_individualism/) | Behavioral psychology, neuroscience, choice architecture, agency | Published |
| [Beyond What Works: Ideas, Intelligence, and the Courage to Be Creative](https://encodereality.com/posts/ideas_intelligence_creativity/) | Creativity, intelligence, epistemology, AI, philosophy of science | Draft |

---

## Experiments (`experiments/`)

Runnable code that supports specific blog posts. Each experiment directory is self-contained with its own tests, CLI runner, and README.

### ideas_intelligence_creativity/

Supporting code for *"Beyond What Works."* Demonstrates the structural hierarchy of ideas, intelligence, and creativity through two experiments:

- **Experiment 1 — Fitness Landscape Optimization**: A fixed-strategy optimizer (intelligence) vs. a meta-strategy optimizer (creativity) on a rugged 2D landscape. The fixed system plateaus; the creative system makes discontinuous jumps by mutating its own search strategy.

- **Experiment 2 — The Generator Hierarchy**: Agent-based simulation with three levels in a grid world — a hardcoded agent (Level 0), weight evolution within a fixed neural architecture (Level 1), and architecture evolution via neuroevolution (Level 2). Environment shifts demonstrate that only Level 2 can handle qualitatively new challenges.

```bash
# Run Experiment 1
python experiments/ideas_intelligence_creativity/run_experiment_1.py --n-steps 1000 --n-peaks 20

# Run Experiment 2
python experiments/ideas_intelligence_creativity/run_experiment_2.py --meta-steps 20 --weight-generations 15
```

60 unit tests: `pytest experiments/ideas_intelligence_creativity/tests/ --no-cov`

---

## Models (`models/`)

Standalone computational models for long-running research questions.

### evolutionary/abiogenesis_blaise/

A primordial soup simulation exploring the spontaneous emergence of self-replicating programs. A population of random byte-tapes interact pairwise via a modified Brainfuck interpreter. Over millions of interactions, replicators emerge without external selection pressure.

- Core: `tape.py`, `brainfuck.py`, `soup.py`
- 81 unit tests with full coverage
- Jupyter notebooks for exploration (`01_basic_bff.ipynb`, `02_long_run_2M.ipynb`, `03_paper_parameters.ipynb`)

```bash
python models/evolutionary/abiogenesis_blaise/run_experiment.py --interactions 2000000
```

---

## Papers (`papers/`)

Research manuscripts, reference materials, and interactive demos.

| Directory | Description |
|-----------|-------------|
| `kahn/persistent_computation/` | Manuscript on persistent computation with citations, figures, and glossary |
| `kahn/quantum-foundations-demo/` | Interactive quantum mechanics tutorial — 8 Jupyter notebooks with Python modules and tests |
| `kahn/representational_geometry/` | Representational geometry research |
| `kahn/system_dynamics_of_political_systems/` | System dynamics of political systems |
| `levinfiles/classical_sorting/` | Classical sorting algorithm research with visualizations |
| `marletto/` | Constructor theory references |

---

## Media (`media/`)

Curated transcripts, summaries, and analysis of talks and interviews that inform the project's theoretical foundations.

| Directory | Source | Topic |
|-----------|--------|-------|
| `jacob_foster/ideal_objects/` | Jacob Foster | Ideal objects, transformational creativity, AI and science |
| `jonathan_goddard/toe/` | Jonathan Goddard | Theory of Everything — constructor theory, set theory, causality, computational irreducibility |
| `blaise/` | Blaise | Computational symbiogenesis, abiogenesis |
| `joscha_bach/` | Joscha Bach | Cognitive architectures, consciousness |
| `andrew_wilson/` | Andrew Wilson | Deep learning strategies |
| `steve_keen/` | Steve Keen | Economics and complex systems |
| `levin/`, `seth_v_levin/` | Michael Levin | Bioelectricity, morphogenesis, collective intelligence |
| `jefflichtman/` | Jeff Lichtman | Connectomics |

---

## Getting Started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package manager) or pip
- Hugo (extended version, for blog development)

### Setup

```bash
git clone https://github.com/encode-reality/sharc_theory.git
cd sharc_theory

# Install dependencies (using uv)
uv sync

# Or with pip
pip install -e ".[dev]"

# Run tests
pytest --no-cov

# Start the blog locally
hugo server -D
```

### Running Tests

```bash
# All tests (models + experiments)
pytest --no-cov

# Just experiments
pytest experiments/ideas_intelligence_creativity/tests/ --no-cov

# Just models
pytest models/evolutionary/abiogenesis_blaise/tests/ --no-cov
```

---

## Tech Stack

- **Python 3.12+** with numpy, scipy, matplotlib, seaborn, networkx, numba
- **Hugo** with PaperMod theme, KaTeX math rendering
- **Jupyter** for interactive exploration

---

## Contact

For questions or collaborations: [miadad@encodereality.com](mailto:miadad@encodereality.com)
