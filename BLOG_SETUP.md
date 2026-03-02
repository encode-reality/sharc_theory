# Blog Setup & Workflow Guide

This repository uses [Hugo](https://gohugo.io/) with the [PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme, deployed to GitHub Pages via GitHub Actions.

**Live site:** https://encode-reality.github.io/sharc_theory/

---

## Prerequisites

### Install Hugo Extended

Hugo Extended is required (PaperMod uses SCSS).

**Windows (winget — recommended):**
```bash
winget install Hugo.Hugo.Extended
```

**Windows (scoop):**
```bash
scoop install hugo-extended
```

**Windows (chocolatey):**
```bash
choco install hugo-extended
```

Verify installation:
```bash
hugo version
# Must show "+extended" in the output
```

### Clone with submodules

If cloning the repo fresh, include submodules so the theme is pulled down:
```bash
git clone --recurse-submodules https://github.com/encode-reality/sharc_theory.git
```

If you already cloned without submodules:
```bash
git submodule update --init --recursive
```

---

## Local Development

Start the local dev server:
```bash
hugo server -D
```

- `-D` includes draft posts (those with `draft: true` in front matter)
- Site is available at `http://localhost:1313/sharc_theory/`
- Hugo watches for file changes and hot-reloads the browser automatically

Build the site locally (to inspect output):
```bash
hugo --gc --minify
# Output goes to public/ (gitignored)
```

---

## Writing a New Post

### 1. Create a branch
```bash
git checkout main
git pull origin main
git checkout -b post/my-topic-name
```

### 2. Scaffold the post
```bash
hugo new posts/my-topic-name.md
```

This creates `content/posts/my-topic-name.md` using the archetype template with pre-filled front matter. The post starts as `draft: true`.

### 3. Write and preview
Edit the file in your editor, then preview locally:
```bash
hugo server -D
```

### 4. Publish
When the post is ready, set `draft: false` in the front matter.

### 5. Commit and push
```bash
git add content/posts/my-topic-name.md
git commit -m "Add post: My Topic Name"
git push -u origin post/my-topic-name
```

### 6. Create a Pull Request
```bash
gh pr create --title "Add post: My Topic Name" --body "New blog post about ..."
```
Or use the GitHub web UI.

### 7. Merge and deploy
Merge the PR to `main`. GitHub Actions automatically builds and deploys the site.

---

## Front Matter Reference

Every post needs YAML front matter at the top:

```yaml
---
title: "Post Title Here"
date: 2024-11-09
draft: false
description: "A short summary shown in post listings and SEO."
tags: ["tag-one", "tag-two"]
author: "Miadad Kahn"
showToc: true       # Show table of contents
TocOpen: false      # TOC collapsed by default
math: false         # Set to true to enable KaTeX rendering
---
```

### Math support

For posts with LaTeX equations, set `math: true` in the front matter. Then use:

- Inline math: `$E = mc^2$`
- Display math: `$$\int_0^\infty e^{-x} dx = 1$$`

---

## Project Structure

```
sharc_theory/
├── archetypes/default.md         # Template for new posts
├── content/
│   ├── posts/                    # Blog posts go here
│   ├── archives.md               # Archives page
│   └── search.md                 # Search page
├── layouts/partials/
│   └── extend_head.html          # KaTeX injection (conditional)
├── static/                       # Static assets (favicon, images, etc.)
├── themes/PaperMod/              # Theme (git submodule — don't edit)
├── hugo.toml                     # Site configuration
├── .github/workflows/hugo.yaml   # GitHub Actions deployment
│
├── papers/                       # Research papers (not part of blog)
├── models/                       # Computational models (not part of blog)
├── media/                        # Media transcripts (not part of blog)
└── ...
```

---

## GitHub Pages Setup (one-time)

1. Go to https://github.com/encode-reality/sharc_theory/settings/pages
2. Under **Build and deployment > Source**, select **GitHub Actions**
3. Save

After this, every push to `main` triggers the deploy workflow automatically.

---

## Branch Naming Conventions

| Branch prefix | Purpose | Example |
|---------------|---------|---------|
| `post/` | New blog post | `post/abiogenesis-findings` |
| `site/` | Site config or theme changes | `site/add-about-page` |
| `fix/` | Bug fixes | `fix/broken-katex` |
