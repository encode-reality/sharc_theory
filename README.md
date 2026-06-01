# SHARC Theory

Research repository and blog exploring **scaled hierarchical and recursive cognitive systems** — from molecular to societal scales. Integrates non-equilibrium thermodynamics, cybernetics, complex systems theory, epistemology, and computational modeling.

**Blog:** https://encode-reality.github.io/sharc_theory/

---

## Quick Start

### Prerequisites

**macOS:**
```bash
brew install hugo gh uv
```

**Windows:**
```bash
winget install Hugo.Hugo.Extended
winget install GitHub.cli
```

### Clone and Run

```bash
git clone --recurse-submodules https://github.com/encode-reality/sharc_theory.git
cd sharc_theory
hugo server -D
# Open http://localhost:1313/sharc_theory/
```

If you already cloned without submodules:
```bash
git submodule update --init --recursive
```

---

## Blog Workflow

The blog is built with [Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, deployed to GitHub Pages via GitHub Actions.

A helper script `blog.sh` streamlines common tasks:

### Create a new post from scratch

```bash
./blog.sh new my-topic-name
# Edit content/posts/my-topic-name.md
# Set draft: false when ready
```

### Publish an existing writeup to the blog

Writeups in `papers/`, `models/`, or `media/` can be published without copying. The script creates a symlink so the source file remains the single source of truth:

```bash
# See what's available
./blog.sh list-writeups

# Publish a writeup (adds front matter if missing, creates symlink)
./blog.sh publish papers/kahn/persistant_computation/manuscript.md

# Optionally specify a custom slug
./blog.sh publish media/levin/consciousness_bioelectricity_synthetic_morphologies.md --slug levin-consciousness

# Remove from blog (source file untouched)
./blog.sh unpublish levin-consciousness
```

### Other commands

```bash
./blog.sh preview          # Start dev server (drafts visible)
./blog.sh build            # Build site to public/
./blog.sh list-posts       # Show all blog posts and their draft status
./blog.sh list-writeups    # Show all publishable writeups across the repo
```

### Full publish workflow

```bash
git checkout -b post/my-topic
./blog.sh publish papers/kahn/some_writeup.md --slug my-topic
# Edit source file: set draft: false, fill in description/tags
./blog.sh preview
git add content/posts/my-topic.md papers/kahn/some_writeup.md
git commit -m "Add post: My Topic"
git push -u origin post/my-topic
gh pr create --title "Add post: My Topic" --body "New blog post"
# Merge PR -> auto-deploys via GitHub Actions
```

---

## Repository Structure

```
sharc_theory/
├── content/posts/              Blog posts (or symlinks to writeups)
├── archetypes/default.md       Template for new posts
├── layouts/partials/           Custom Hugo partials (KaTeX, etc.)
├── themes/PaperMod/            Theme (git submodule)
├── hugo.toml                   Site configuration
├── blog.sh                     Blog helper script
├── .github/workflows/hugo.yaml GitHub Actions deployment
│
├── papers/                     Research papers and manuscripts
│   ├── kahn/                   Original research
│   ├── levinfiles/             Levin-related analyses
│   └── meta/                   Meta-analyses and notes
│
├── models/                     Computational models and simulations
│   └── evolutionary/           Evolutionary dynamics (abiogenesis, etc.)
│
├── media/                      Media analyses and transcripts
│   ├── blaise/                 Blaise Agüera y Arcas
│   ├── jonathan_goddard/       Jonathan Gorard
│   ├── joscha_bach/            Joscha Bach
│   ├── levin/                  Michael Levin
│   └── ...                     Other researchers
│
├── pyproject.toml              Python project config
└── uv.lock                     Python dependency lock
```

---

## Front Matter Reference

Every blog post needs YAML front matter:

```yaml
---
title: "Post Title Here"
date: 2026-03-05
draft: false
description: "A short summary for listings and SEO."
tags: ["complex-systems", "thermodynamics"]
author: "Miadad Kahn"
showToc: true
TocOpen: false
math: false          # Set true for LaTeX equations
---
```

Math support: use `$...$` for inline and `$$...$$` for display equations.

---

## Branch Naming

| Prefix | Purpose | Example |
|--------|---------|---------|
| `post/` | New blog post | `post/abiogenesis-findings` |
| `site/` | Site config or theme changes | `site/add-about-page` |
| `fix/` | Bug fixes | `fix/broken-katex` |

---

## Experiments (`experiments/`)

Runnable code that supports specific blog posts. Each experiment directory is self-contained with its own tests, CLI runner, and README.

### ideas_intelligence_creativity/

Supporting code for *"Beyond What Works."* Demonstrates the structural hierarchy of ideas, intelligence, and creativity through two experiments:

- **Experiment 1 — Fitness Landscape Optimization**: A fixed-strategy optimizer (intelligence) vs. a meta-strategy optimizer (creativity) on a rugged 2D landscape. The fixed system plateaus; the creative system makes discontinuous jumps by mutating its own search strategy.

- **Experiment 2 — The Generator Hierarchy**: Agent-based simulation with three levels in a grid world — a hardcoded agent (Level 0), weight evolution within a fixed neural architecture (Level 1), and architecture evolution via neuroevolution (Level 2). Environment shifts demonstrate that only Level 2 can handle qualitatively new challenges.

```bash
# Run Experiment 1
poetry run python experiments/ideas_intelligence_creativity/run_experiment_1.py --n-steps 1000 --n-peaks 20

# Run Experiment 2
poetry run python experiments/ideas_intelligence_creativity/run_experiment_2.py --meta-steps 20 --weight-generations 15
```

60 unit tests: `poetry run pytest experiments/ideas_intelligence_creativity/tests/ --no-cov`

---

## Models (`models/`)

Standalone computational models for long-running research questions.

### evolutionary/abiogenesis_blaise/

A primordial soup simulation exploring the spontaneous emergence of self-replicating programs. A population of random byte-tapes interact pairwise via a modified Brainfuck interpreter. Over millions of interactions, replicators emerge without external selection pressure.

- Core: `tape.py`, `brainfuck.py`, `soup.py`
- 81 unit tests with full coverage
- Jupyter notebooks for exploration (`01_basic_bff.ipynb`, `02_long_run_2M.ipynb`, `03_paper_parameters.ipynb`)

```bash
poetry run python models/evolutionary/abiogenesis_blaise/run_experiment.py --interactions 2000000
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
- [Poetry](https://python-poetry.org/)
- Hugo (extended version, for blog development)

### Setup

```bash
git clone https://github.com/encode-reality/sharc_theory.git
cd sharc_theory

# Install dependencies
poetry install

# Run tests
poetry run pytest --no-cov

# Start the blog locally
hugo server -D
```

### Running Tests

```bash
# All tests (models + experiments)
poetry run pytest --no-cov

# Just experiments
poetry run pytest experiments/ideas_intelligence_creativity/tests/ --no-cov

# Just models
poetry run pytest models/evolutionary/abiogenesis_blaise/tests/ --no-cov
```

---

## Tech Stack

- **Python 3.12+** with numpy, scipy, matplotlib, seaborn, networkx, numba
- **Hugo** with PaperMod theme, KaTeX math rendering
- **Jupyter** for interactive exploration

---

## Contact

Miadad Kahn — [miadad@encodereality.com](mailto:miadad@encodereality.com)
