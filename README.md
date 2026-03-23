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

## Contact

Miadad Kahn — [miadad@encodereality.com](mailto:miadad@encodereality.com)
