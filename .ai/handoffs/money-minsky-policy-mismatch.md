# Resume Brief: `money-minsky-policy-mismatch`

This note is the cold-start briefing for future sessions working on `content/posts/money-minsky-policy-mismatch.md`.

## Current State

- The post is now on the normal publish path (`draft: false`).
- The main argument is already in place and structurally coherent.
- The current work is a second refinement cycle on top of the published baseline, not a blank-page rewrite.
- The supporting code surface has already been narrowed to a rebuilt evidence chain after an audit of older models and claims.
- The first cycle (`task-016` through `task-022`) is complete.
- The follow-on completeness layer (`task-024` through `task-030`) is complete.
- `task-024`, `task-025`, `task-026`, `task-027`, `task-028`, `task-029`, and `task-030` are complete.
- Repo/collateral remains an explicit limitation, not a dedicated model in this cycle.

## Read These First

1. `content/posts/money-minsky-policy-mismatch.md`
2. `money_minsky_policy_mismatch_AUDIT.md`
3. `experiments/money_minsky_policy_mismatch/README.md`
4. `BLOG_SETUP.md`
5. `.ai/handoffs/money-minsky-policy-mismatch-factor-refinement.md`

## Core Thesis

The Keynes quote is the spine of the post:

> Anything we can actually do we can afford.

The post is using that line as a systems question, not a slogan. Its claim is that austerity frameworks misassign money's functional role by treating unlike entities as though they faced the same monetary constraint. Households, currency users, quasi-sovereigns, and issuers do not occupy the same place in the system, so they should not be analyzed with one universal budget metaphor.

The draft is not claiming there are no limits. It is claiming that the binding limits are real capacity, inflation, external dependence, legal architecture, and private-sector fragility.

## Voice And Reader Posture

- Write like an intellectually serious but epistemically humble explainer.
- Avoid triumphal or pompous language.
- Help readers identify when economic rhetoric is assigning money the wrong function.
- Keep the civic point visible: in the kind of society governments promise, their role is not identical to a household's budgeting role.

## Current Evidence Chain

Use these as authoritative support for the post:

- `experiments/money_minsky_policy_mismatch/comparative_constraints.py`
- `experiments/money_minsky_policy_mismatch/policy_sectoral_model.py`
- `experiments/money_minsky_policy_mismatch/austerity_counterfactual.py`
- `experiments/money_minsky_policy_mismatch/policy_controllers.py`
- `experiments/money_minsky_policy_mismatch/sovereign_securities.py`
- `experiments/money_minsky_policy_mismatch/external_constraint.py`
- `experiments/money_minsky_policy_mismatch/holder_composition.py`
- `experiments/money_minsky_policy_mismatch/fragility_regimes.py`
- `experiments/money_minsky_policy_mismatch/capacity_constraint.py`
- `experiments/money_minsky_policy_mismatch/research_data.py`
- `experiments/money_minsky_policy_mismatch/plotting.py`

Current figures that match the accepted chain:

- `constraint_hierarchy.png`
- `comparative_constraints.png`
- `campaign_vs_operational_models.png`
- `policy_sectoral_balances.png`
- `policy_sectoral_paths.png`
- `imf_counterfactual_cases.png`
- `wrong_target_control.png`
- `policy_lab.png`
- `rollover_comparison.png`
- `external_constraint.png`
- `holder_composition.png`
- `fragility_regimes.png`
- `capacity_constraint.png`

## Do Not Reintroduce These As Settled Evidence

- `issuer_vs_user.png`
- `austerity_minsky_shift.png`
- strong issuer-vs-user SFC output claims
- strong ABM austerity-to-fragility claims
- universal “FIH validated” language
- JG wage-level comparison claims

These are all covered in `money_minsky_policy_mismatch_AUDIT.md`. If future work repairs those models, that is a new validation task, not a default assumption.

## Section Map

- Intro through section 3: conceptually strong; mainly needs editorial tightening and smooth transitions.
- Section 4: solid core accounting argument; keep the sectoral identity and policy-path interpretation aligned to `policy_sectoral_model.py`.
- Section 5: now supported by both the reduced-form counterfactual and the ABM policy-lab; keep both stylized and conditional.
- Section 6: usable as a fragility/state-dependence argument; keep the calibration explanation explicit.
- Section 7: important guardrail section; it now needs to keep the expanded evidence taxonomy straight without overselling the new models.
- Sections 8-9: good closing structure; focus on clarity and avoiding repetition.
- Reproducibility notes: should stay synchronized with the actual package layout and commands.

## Current Task Split

Planner / editorial:

- `task-024`: omitted-factor scoping (`done` as of 2026-04-25)
- `task-025`: prose pass for bonds, liability hierarchy, and scoped omissions (`done` as of 2026-04-25)
- `task-029`: collateral/liquidity and repo scope decision (`done` as of 2026-04-25)
- `task-030`: factor-refinement integration and validation (`done` as of 2026-04-25)

Coding / implementer:

- `task-026`: toy sovereign-securities and rollover extension (`done` in repo; verified locally on 2026-04-25)
- `task-027`: external-constraint and imported-essentials extension (`done` in repo; verified locally on 2026-04-25)
- `task-028`: holder-composition and distribution channel extension (`done` in repo; verified locally on 2026-04-25)

`claude` remains the intended implementer for the coding lane. `codex` remains the planner/editorial partner.

## Current Execution Sequence

1. The initial publish-ready cycle is complete.
2. `codex` completed `task-024` and wrote `.ai/handoffs/money-minsky-policy-mismatch-factor-refinement.md`.
3. `codex` completed `task-025` by adding scoped prose on bonds, rollover, collateral/liquidity context, and external constraint to the post.
4. `claude` implemented `task-026` and `task-027`, adding `sovereign_securities.py`, `external_constraint.py`, their tests, README updates, and the new figures.
5. `codex` completed `task-029` and kept repo/collateral as a named limitation rather than a new model surface for this post.
6. `claude` implemented `task-028`, adding `holder_composition.py`, its tests, README updates, and the new figure.
7. `codex` completed `task-030`, integrating the refinement-layer models into the post, updating the audit/README, and verifying the full suite plus Hugo.

Concurrency rule:

- do not edit `content/posts/money-minsky-policy-mismatch.md` at the same time from both lanes
- do not pull simulation conclusions into the prose until the coding lane has produced validated artifacts

## Repro Commands

Run the test suite:

```bash
uv run python -m pytest experiments/money_minsky_policy_mismatch/tests/ -v
```

Run the accepted figure package:

```bash
uv run python -m experiments.money_minsky_policy_mismatch.run_experiment --experiment all --refresh-data
```

Core output location:

- `static/images/money_minsky_policy_mismatch/`

Public-data cache location:

- `results/money_minsky_policy_mismatch_data/`

## Start Here Next Session

1. Read the five files listed under "Read These First."
2. Check `git status --short` before touching anything.
3. Treat the current post, audit, and README as synchronized to the accepted evidence chain.
4. If a future session opens new work, create or claim a fresh hub task instead of implicitly resuming the closed refinement sequence.
5. If new code/model changes are made, re-check the audit assumptions before changing the prose.
