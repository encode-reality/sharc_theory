# Money-Minsky-Policy-Mismatch — Session Handoff

**Date:** 2026-05-27
**Branch:** `blog/qm_type_theorem`
**Status:** Draft (`draft: true`). **Do not publish without explicit user approval.**

---

## What this document is

A handoff for the next agent picking up work on the blog post `content/posts/money-minsky-policy-mismatch.md`. The earlier session-by-session detail lives in the related files:

- `money_minsky_policy_mismatch_AUDIT.md` — original audit
- `PLOT_REVIEW.md` — earlier plot-review notes
- `BLOG_SETUP.md` — Hugo + theme setup

This file captures **only** what changed in the most recent two refinement passes and what remains open.

---

## Recent session work (May 27, 2026)

### Pass 1 — Refinement (content/throughline)
Implemented the plan at `/Users/legirl/.claude/plans/groovy-doodling-sundae.md` (first version, since overwritten — the file is now Pass 2's plan).

Major changes to `content/posts/money-minsky-policy-mismatch.md`:

- Added bridge between reservoir analogy and endogenous-money discussion in §1
- Added "real affordability" integrating sentence in §2
- Explicit transitions §2→§3, §3→§4, §5→§6, §6→§7
- Anchored sectoral-model implicit multiplier to Blanchard-Leigh (2013) empirical range (0.9-1.7)
- Expanded §5 variable explanations with units (action/100, hysteresis, stabilizer_slope, consolidation_passthrough)
- §6: Corrected code attribution from `fragility_regimes.py` to `keen_ode.py`
- §6: Explained k2 debt-drag parameter and honest two-calibration comparison
- §6: Added endogenous-money throughline acknowledgment
- §7: Three-experiment synthesis paragraph
- §7: Acknowledged "real resources" testing gap (no inflation model)
- IMF section: Added model-output parenthetical + actual-debt scatter overlay mention

### Pass 2 — Prose declutter (this session)
Implemented the plan at `/Users/legirl/.claude/plans/groovy-doodling-sundae.md` (current version on disk).

The user identified three anti-patterns that treated readers as needing constant signposting:

1. **Redundant throughline announcements** — explicit "this is the throughline" instead of letting content carry it
2. **Front-loaded "Minimal Vocabulary" glossary** — every term was already re-defined in-section
3. **Explicit "first principles" labeling** — audience can derive this from structure

Changes applied:

- **Deleted "Minimal Vocabulary" section entirely.** Migrated `constraint set` definition into §2, added inline `debt_ratio` definition in §5.
- **Folded §5 mini-glossary** (austerity/consolidation/multiplier/stabilizers/hysteresis) into prose flow. Each term is now defined at first use inline.
- **Folded §6 mini-glossary** (leverage/rate-shock/fragility) into the loaded-beam analogy paragraph.
- **Removed throughline announcements:**
  - "This post keeps one claim fixed:" + "The pervasive message of this post is therefore simple:" → merged into single blockquote
  - "This is the core shift in the whole article."
  - "This analogy is not the argument. It is a first-pass intuition."
  - "Here is the simplest operational distinction in the whole post."
  - "This is the part I want readers to keep."
  - "What I want the reader to leave with is simple:" → "The practical residue:"
  - "The point is not to hide behind models."
  - "The point of this post is not to win an argument by jargon."
- **Removed defensive meta-commentary:**
  - "That is not ideology. It is accounting."
  - "The code is not imposing a political opinion."
  - "The model is not trying to prove all of macroeconomics."
  - "The point is not 'always.'"
- **Renamed:**
  - §1 heading: "1. First Principle: Economies Are Open Flow Systems" → "1. Economies Are Open Flow Systems"
  - §2 heading: "2. Issuer, User, and Quasi-Sovereign: The Basic Distinction" → "2. Issuer, User, and Quasi-Sovereign"
  - Front-matter description: dropped "first-principles" label

### Late corrections in this session

- Added GDP-identity bridge in §4: "If you have taken any macroeconomics course, these variables should look familiar. Sum the three balances and set them to zero and you recover the GDP expenditure identity: `Y = C + I + G + (X − M)`..."
- **Fixed §4 plot placement.** The identity plot (`policy_sectoral_balances.png`) was previously after the three-policy-scenarios introduction. Moved it up to immediately follow the identity discussion. The policy-paths plot still follows the policy-comparison prose.

### Plot work (earlier in session)

The `wrong_target_control.png` concept diagram was iteratively repositioned. Final state in `experiments/money_minsky_policy_mismatch/plotting.py`:

- `left_x = 0.14`, `right_x = 0.55`, `box_w = 0.34`, `box_h = 0.12`
- Local `_control_box()` helper with `ha="center"`, `va="center"`, `fontsize=11`, line breaks in titles
- Feedback loop arrow: `loop_x = left_x - 0.02`, `connectionstyle="arc3,rad=-0.50"` (arcs right)
- "looped pressure" label at `(left_x - 0.11, 0.50)`, `rotation=90`
- `savefig` uses `pad_inches=0.15` to prevent label clipping

User confirmed final positioning. Do not adjust without explicit request.

---

## Current state

- **Draft:** `draft: true` in front matter. **Do not flip to `false` without user approval.**
- **Tests:** 98 tests passing across the `experiments/money_minsky_policy_mismatch/` package as of Pass 1.
- **Images:** All 8 embedded images render. Paths are `/images/money_minsky_policy_mismatch/...` (no `/sharc_theory/` prefix — `baseURL` in `hugo.toml` is `https://encodereality.com/` with no subdirectory).
- **Code-block invocation:** Uses `poetry run python ...` (this is a Poetry project, **not** uv — confirmed by user).

---

## What a future agent might pick up

These are *suggestions*, not commitments. Confirm with the user before acting.

1. **Final fresh-eye read.** Two refinement passes are complete. A third pass with fresh eyes might catch new patterns. The user has been the primary judge of when to stop refining.
2. **Image alt-text audit.** Alt-text on the 8 plot images may still feel auto-generated in places. Worth a pass.
3. **The "How to recognize this in real life" subsections** in §4, §5, §6 follow a consistent pattern. Good. No change suggested unless the user flags something.
4. **References section** at the end could use ordering by relevance to the post rather than apparent insertion order. Low priority.
5. **The deleted `bellsinequality.md`** at repo root is unrelated to this work but appears in `git status` from earlier session state — leave alone unless the user asks.

---

## Hard constraints (set by user across the project)

- **Poetry, not uv.** Any `uv run` instances should be reverted to `poetry run`.
- **Display name:** "Miadad Rashid" in front-matter `author`. Some files (CLAUDE memory) say "Miadad Kahn" — defer to the file front-matter.
- **No publishing this post.** Stays at `draft: true` until user says otherwise.

---

## Files modified this session

- `content/posts/money-minsky-policy-mismatch.md` — primary
- `experiments/money_minsky_policy_mismatch/plotting.py` — `wrong_target_control` positioning
- This handoff document (new)
