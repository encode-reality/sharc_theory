#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")" && pwd)"
CONTENT_DIR="$REPO_ROOT/content/posts"

# ────────────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────────────

usage() {
  cat <<'EOF'
Usage: ./blog.sh <command> [options]

Commands:
  new <slug>                 Scaffold a new blog post (hugo new)
  publish <file> [--slug s]  Publish an existing writeup to the blog via symlink
  unpublish <slug>           Remove a published symlink (does not delete source)
  preview                    Start Hugo dev server with drafts
  build                      Build the site (output to public/)
  list-posts                 List current blog posts and their status
  list-writeups              Find all markdown writeups in papers/, models/, media/

Examples:
  ./blog.sh new my-new-topic
  ./blog.sh publish papers/kahn/persistant_computation/manuscript.md
  ./blog.sh publish media/levin/consciousness_bioelectricity_synthetic_morphologies.md --slug levin-consciousness
  ./blog.sh unpublish levin-consciousness
  ./blog.sh preview
EOF
  exit 1
}

slugify() {
  local name
  name="$(basename "$1" .md)"
  echo "$name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//'
}

has_front_matter() {
  head -1 "$1" | grep -q '^---$'
}

add_front_matter() {
  local file="$1"
  local title="$2"

  # Extract first heading as title if not provided
  if [[ -z "$title" ]]; then
    title=$(grep -m1 '^#' "$file" | sed 's/^#\+\s*//' | sed 's/\*//g' || true)
  fi
  if [[ -z "$title" ]]; then
    title="$(basename "$file" .md | tr '-' ' ' | tr '_' ' ')"
  fi

  local date
  date="$(date +%Y-%m-%d)"

  local tmp
  tmp="$(mktemp)"
  cat > "$tmp" <<FRONTMATTER
---
title: "${title}"
date: ${date}
draft: true
description: ""
tags: []
author: "Miadad Kahn"
showToc: true
TocOpen: false
math: false
---
FRONTMATTER
  cat "$file" >> "$tmp"
  mv "$tmp" "$file"
  echo "  Added front matter to: $file"
}

# ────────────────────────────────────────────────────────
# Commands
# ────────────────────────────────────────────────────────

cmd_new() {
  local slug="${1:?Usage: ./blog.sh new <slug>}"
  hugo new "posts/${slug}.md"
  echo "Created: content/posts/${slug}.md"
  echo "Edit it, then set draft: false when ready to publish."
}

cmd_publish() {
  local src="${1:?Usage: ./blog.sh publish <file> [--slug <slug>]}"
  local slug=""

  shift
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --slug) slug="$2"; shift 2 ;;
      *) echo "Unknown option: $1"; exit 1 ;;
    esac
  done

  # Resolve to absolute path
  if [[ ! "$src" = /* ]]; then
    src="$REPO_ROOT/$src"
  fi

  if [[ ! -f "$src" ]]; then
    echo "Error: File not found: $src"
    exit 1
  fi

  # Generate slug from filename if not provided
  if [[ -z "$slug" ]]; then
    slug="$(slugify "$src")"
  fi

  local dest="$CONTENT_DIR/${slug}.md"

  if [[ -e "$dest" ]]; then
    echo "Error: $dest already exists. Use a different --slug or unpublish first."
    exit 1
  fi

  # Add front matter to source if missing
  if ! has_front_matter "$src"; then
    echo "Source file has no Hugo front matter."
    read -rp "Add front matter to source file? [Y/n] " yn
    case "${yn:-Y}" in
      [Yy]*) add_front_matter "$src" "" ;;
      *) echo "Aborted. Add front matter manually, then re-run."; exit 1 ;;
    esac
  fi

  # Create relative symlink
  local rel_path
  rel_path="$(python3 -c "import os.path; print(os.path.relpath('$src', '$CONTENT_DIR'))")"
  ln -s "$rel_path" "$dest"

  echo "Published: $dest -> $rel_path"
  echo ""
  echo "Next steps:"
  echo "  1. Edit the source file to set draft: false when ready"
  echo "  2. Run: ./blog.sh preview"
  echo "  3. Commit both the source and the symlink"
}

cmd_unpublish() {
  local slug="${1:?Usage: ./blog.sh unpublish <slug>}"
  local dest="$CONTENT_DIR/${slug}.md"

  if [[ ! -L "$dest" ]]; then
    echo "Error: $dest is not a symlink (or does not exist)."
    echo "Only symlinked posts can be unpublished. Directly-created posts should be deleted manually."
    exit 1
  fi

  rm "$dest"
  echo "Unpublished: removed symlink $dest"
  echo "Source file is untouched."
}

cmd_preview() {
  echo "Starting Hugo dev server (drafts enabled)..."
  echo "Site: http://localhost:1313/sharc_theory/"
  hugo server -D
}

cmd_build() {
  hugo --gc --minify
}

cmd_list_posts() {
  echo "Blog posts in content/posts/:"
  echo ""
  for f in "$CONTENT_DIR"/*.md; do
    [[ -f "$f" ]] || continue
    local name
    name="$(basename "$f")"
    local draft
    draft="$(grep -m1 '^draft:' "$f" 2>/dev/null | awk '{print $2}' || echo "?")"
    local symlink=""
    if [[ -L "$f" ]]; then
      symlink=" -> $(readlink "$f")"
    fi
    printf "  %-50s draft=%-6s%s\n" "$name" "$draft" "$symlink"
  done
}

cmd_list_writeups() {
  echo "Markdown writeups available to publish:"
  echo ""
  for dir in papers models media; do
    if [[ -d "$REPO_ROOT/$dir" ]]; then
      echo "[$dir/]"
      find "$REPO_ROOT/$dir" -name '*.md' \
        ! -name 'README.md' \
        ! -name 'BUILD.md' \
        ! -name 'WORKLOG.md' \
        ! -name 'QUICKSTART.md' \
        ! -name 'AGENT_HANDOFF.md' \
        ! -path '*/venv/*' \
        ! -path '*/node_modules/*' \
        ! -path '*/.venv/*' \
        ! -path '*/reference_implementation/*' \
        -print | sort | while read -r f; do
          local rel="${f#$REPO_ROOT/}"
          local has_fm="no"
          if head -1 "$f" 2>/dev/null | grep -q '^---$'; then
            has_fm="yes"
          fi
          printf "  %-80s front-matter=%s\n" "$rel" "$has_fm"
      done
      echo ""
    fi
  done
}

# ────────────────────────────────────────────────────────
# Dispatch
# ────────────────────────────────────────────────────────

cmd="${1:-}"
shift || true

case "$cmd" in
  new)            cmd_new "$@" ;;
  publish)        cmd_publish "$@" ;;
  unpublish)      cmd_unpublish "$@" ;;
  preview)        cmd_preview ;;
  build)          cmd_build ;;
  list-posts)     cmd_list_posts ;;
  list-writeups)  cmd_list_writeups ;;
  *)              usage ;;
esac
