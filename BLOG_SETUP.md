# Agent Handoff: SHARC Theory / Encode Reality

This document is for a brand new agent entering the repository cold.

Read this first if the user asks you to:

- write or revise a blog post
- research a new topic for the blog
- add or refine supporting experiments
- generate figures or plots for an essay
- make site changes without re-discovering the repo structure

The goal is to give you enough context to work effectively without re-mapping the project from scratch every conversation.

## 1. What This Project Is

This repository is not just a blog. It is a joint human-AI research workspace for developing better descriptions of reality.

The project combines:

- long-form essays
- computational experiments
- formal and informal research notes
- curated papers
- curated transcripts and analyses of thinkers relevant to the project

The core epistemic stance of the project is:

- ideas should be made as precise as possible
- precision should lead to executable models when feasible
- essays and experiments should support each other
- "understanding" is stronger when a claim can be formalized, simulated, visualized, or operationalized

The user is not using AI as a copywriter. The intended mode is true collaboration: generate ideas, test them, refine them, and translate them into essays, models, and research artifacts.

## 2. The Project's Intellectual Direction

The repo centers on a recurring set of themes:

- complex systems
- computation as a lens for philosophy and science
- hierarchy, recursion, and generative structure
- epistemology and ontology
- intelligence, creativity, and representation
- non-equilibrium systems
- social, political, economic, and biological dynamics

The "house style" is not generic blog writing. The preferred style is:

- rigorous rather than rhetorical
- explanatory rather than slogan-driven
- structurally precise
- willing to move between philosophy, formalism, and simulation
- comfortable using math, pseudocode, or diagrams when they clarify the claim

If a topic can be reframed in terms of system architecture, information flow, computational constraints, generative structure, or dynamical behavior, that is usually the right move.

## 3. Fast Start for a New Agent

When a new conversation starts, do this first:

1. Read this file.
2. Run `git status --short`.
3. Open the relevant target file in `content/posts/` if the user is working on a post.
4. Open the matching folder in `experiments/`, `papers/`, `media/`, or `models/` if the topic already exists.
5. Check whether the topic is already partially developed in a draft, notes file, or experiment directory before inventing a new structure.

Important: this repo is often used with live uncommitted work in progress. Do not assume a clean worktree.

## 4. Source-of-Truth Map

These are the directories that matter most.

| Path | What it is for | How to treat it |
|------|----------------|-----------------|
| `content/posts/` | Canonical source for blog posts | Edit here for essays and post drafts |
| `experiments/` | Runnable Python experiments tied to specific essays | Add code, tests, plots, and runners here |
| `models/` | Larger standalone research models | Check local README/handoff docs before editing |
| `papers/` | Manuscripts, papers, references, demos | Use for local research context |
| `media/` | Transcripts, summaries, analyses of talks/interviews | Mine this before re-researching topics from scratch |
| `static/images/` | Canonical blog figure assets | Put final images here and reference them from posts |
| `static/plots/` | Interactive or auxiliary plot assets | Use when a figure is not just a static image |
| `layouts/partials/extend_head.html` | KaTeX injection and small theme overrides | Relevant when math rendering or header behavior changes |
| `archetypes/default.md` | Default Hugo front matter template | Useful, but note the author field is stale |
| `hugo.toml` | Canonical Hugo config | Check this for site behavior, menus, outputs, theme, and Markdown config |
| `themes/PaperMod/` | Active Hugo theme submodule | Avoid editing unless the task is intentionally theme-level |
| `public/` | Generated site output | Do not treat as source; it is ignored/generated |
| `results/` | Experiment caches and result artifacts | Useful for reruns and plot regeneration, not usually hand-edited |

Also note:

- `themes/hugo-coder/` and `themes/hugo-blog-awesome/` exist as submodules, but the active theme in `hugo.toml` is `PaperMod`.
- `static/CNAME` declares the custom domain `encodereality.com`.
- The old assumption that the site lives only at `encode-reality.github.io/sharc_theory` is stale. The canonical site config uses `https://encodereality.com/`.

## 5. How the Pieces Fit Together

The normal pattern in this repo is:

1. A topic begins as a research question or conceptual claim.
2. Local source material is gathered from `papers/`, `media/`, prior posts, and sometimes scratch notes.
3. A post draft is written in `content/posts/`.
4. If the claim benefits from executable evidence, a matching experiment is created or extended under `experiments/<topic>/`.
5. The experiment generates figures into `static/images/<topic>/` or `static/plots/<topic>/`.
6. The post embeds those figures and uses the code as evidence, intuition, or demonstration.

The essays are not supposed to float free of the research and code. The strongest work in this repo is where the essay and the experiment clearly reinforce each other.

## 6. Current Topic Map

This is the current high-level map of the blog/research content visible in the repo.

| Topic | Status in `content/posts/` | Main supporting location |
|------|-----------------------------|---------------------------|
| `societies-as-complex-systems` | Published (`draft: false`) | `papers/kahn/system_dynamics_of_political_systems/` |
| `paradox_of_individualism` | Published (`draft: false`) | Essay-first topic; no matching experiment directory currently |
| `ideas_intelligence_creativity` | Published (`draft: false`) | `experiments/ideas_intelligence_creativity/` |
| `models_define_world` | Published (`draft: false`) | `experiments/models_define_world/` |
| `bells_inequality` | Draft (`draft: true`) | `experiments/bells_inequality/` |
| `money-minsky-policy-mismatch` | Draft / active work (`draft: true`) | `experiments/money_minsky_policy_mismatch/` plus root working notes |
| `abiogenesis_blaise` | Research model, not a blog post folder | `models/evolutionary/abiogenesis_blaise/` |

Use this as orientation, but verify the actual front matter in `content/posts/*.md`. `README.md` and older docs may lag behind the true draft/published state.

## 7. Blog Post Conventions

Posts live in `content/posts/<slug>.md`.

Typical front matter:

```yaml
---
title: "Post Title"
date: 2026-03-26
draft: true
description: "Short summary."
tags: ["complex-systems", "economics"]
author: "Miadad Rashid"
showToc: true
TocOpen: true
math: true
---
```

Important conventions:

- Use `math: true` when the post contains LaTeX. KaTeX is injected by `layouts/partials/extend_head.html`.
- Newer posts use `author: "Miadad Rashid"`.
- `archetypes/default.md` still defaults to `author: "Miadad Kahn"`, so correct that manually when scaffolding a new post.
- Posts commonly use manual reference anchors like `[[1]](#ref-1)` with a references section at the end.
- Posts often include pseudocode or short formal definitions when it sharpens the argument.
- Figures should usually live at `/images/<topic>/...` and be stored in `static/images/<topic>/`.
- If a post links to source code, it usually points to the matching experiment folder in GitHub.

Current slug naming is not perfectly standardized:

- some posts use underscores, for example `ideas_intelligence_creativity`
- some use hyphens, for example `money-minsky-policy-mismatch`

Do not "normalize" an existing topic's slug unless the user explicitly wants that refactor.

## 8. Writing Workflow for a New Topic

When the user brings a new topic for the blog, the default workflow should be:

1. Find the core claim.
2. Determine whether the claim is mainly conceptual, empirical, computational, or mixed.
3. Search the repo for related material before doing new research.
4. Gather local context from:
   - `content/posts/`
   - `papers/`
   - `media/`
   - matching experiments or models
5. Build an outline that distinguishes:
   - the thesis
   - the structural argument
   - the evidence or examples
   - what should become executable
6. If the idea is modelable, propose or build a supporting experiment.
7. Generate plots/assets and wire them into the post.
8. Tighten the prose so the article reads as one argument, not a pile of notes.

This repo works best when an agent does more than summarize sources. The expected contribution is synthesis: turning material into a clearer, more operational model of the phenomenon.

## 9. Research Workflow for Agents

For research-heavy tasks, use this order of operations:

1. Search the local corpus first.
2. Check whether the user already has related notes or a draft in the repo.
3. Use the post/experiment structure already present to infer the expected level of rigor.
4. Only then expand outward to external research if needed.

What "good" research means in this project:

- prefer primary sources when possible
- do not flatten disagreements between schools of thought
- separate what is an accounting identity, empirical regularity, formal theorem, modeling assumption, and philosophical interpretation
- when making a strong claim, ask whether it can be computationally illustrated
- do not overstate certainty just because a metaphor sounds good

Useful local research reservoirs:

- `media/` for transcript-based idea mining
- `papers/` for manuscripts, PDFs, references, and demos
- prior posts for vocabulary and argument structure
- existing experiment code for reusable abstractions and plots

## 10. Code Workflow

The code side of this repo is mainly Python 3.12+.

Environment:

```bash
poetry install
```

Test commands:

```bash
poetry run pytest --no-cov
poetry run pytest experiments/ideas_intelligence_creativity/tests/ --no-cov
poetry run pytest experiments/models_define_world/tests/ --no-cov
poetry run pytest experiments/bells_inequality/tests/ --no-cov
poetry run pytest experiments/money_minsky_policy_mismatch/tests/ --no-cov
poetry run pytest models/evolutionary/abiogenesis_blaise/tests/ --no-cov
```

Notes:

- Root `pytest` configuration in `pyproject.toml` enables coverage by default. For quick iteration, `--no-cov` is usually the better choice.
- Experiment folders generally follow a pattern: `config.py`, core modules, `plotting.py`, `run_experiment.py`, and `tests/`.
- The repo favors runnable CLIs plus tests over purely notebook-based work.
- Use explicit seeds when generating stochastic results so plots are reproducible.

Representative runners:

```bash
poetry run python experiments/ideas_intelligence_creativity/run_experiment_1.py --n-steps 1000 --n-peaks 20 --seed 42
poetry run python experiments/ideas_intelligence_creativity/run_experiment_2.py --meta-steps 20 --weight-generations 15 --seed 42
poetry run python experiments/models_define_world/run_experiment.py --experiment recovery
poetry run python experiments/bells_inequality/run_experiment.py --experiment all --seed 42
poetry run python experiments/money_minsky_policy_mismatch/run_experiment.py --experiment all --seed 42
poetry run python models/evolutionary/abiogenesis_blaise/run_experiment.py --interactions 2000000
```

Where outputs usually go:

- cached or structured run output: `results/`
- blog images: `static/images/<topic>/`
- interactive or auxiliary plots: `static/plots/<topic>/`

## 11. Hugo / Site Workflow

This repo uses Hugo with the PaperMod theme.

Requirements:

- Hugo extended
- theme submodules initialized

Useful commands:

```bash
hugo server -D
hugo --gc --minify
git submodule update --init --recursive
```

Important site behavior:

- `-D` shows drafts
- `content/search.md` and `content/archives.md` define supporting site pages
- `hugo.toml` enables Goldmark passthrough and KaTeX-friendly math delimiters
- the site deploy workflow is `.github/workflows/hugo.yaml`
- the live site uses the custom domain `encodereality.com`

Do not edit `public/` as if it were source content.

## 12. Existing Local Handoff Docs

Some subprojects already contain their own deeper onboarding docs.

Most important example:

- `models/evolutionary/abiogenesis_blaise/AGENT_HANDOFF.md`

Also check local `README.md`, `QUICKSTART.md`, and related documents inside a target subdirectory before making changes there. The root repo is broad; local docs may be much more specific than this file.

## 13. Common Pitfalls

- The worktree may be dirty. Check `git status --short` before assuming anything.
- Older docs may be stale relative to actual post front matter and current drafts.
- `public/` is generated output, not the place to author content.
- The active theme is `PaperMod`, even though other themes are present.
- The post archetype still uses the old author name.
- Root-level scratch files may exist for active thinking. Treat them as working notes unless the user says they are canonical.
- Not every topic has both a post and an experiment yet. Do not assume symmetry.
- Some directories in `papers/` and `media/` are reference archives, not polished final documents.

## 14. What a Good Agent Should Optimize For Here

A good agent in this repo should:

- preserve the project's philosophical and technical seriousness
- turn vague ideas into explicit structures
- look for opportunities to make abstract claims testable
- connect essays to experiments whenever that improves clarity
- use the repo's existing research corpus before reinventing context
- avoid generic content marketing language
- help the user think, not just help the user publish

If you are unsure how to contribute, the right default is:

1. clarify the core claim
2. locate existing repo context
3. decide what should become argument, code, figure, or research note
4. build the smallest useful next artifact

That is the working style this repository is designed for.
