# Current Spec: `money-minsky-policy-mismatch`

## Active Work

- Target draft: `content/posts/money-minsky-policy-mismatch.md`
- Baseline status: the first publish-ready cycle is complete and the post is currently on the normal Hugo publish path.
- Second refinement-cycle status: complete as of 2026-04-25.
- Coordination mode: mixed editorial + code. Future sessions should be able to continue prose work, evidence review, or reproducibility work from the same artifact set.

## Thesis

The post uses Keynes's line, "Anything we can actually do we can afford," as a diagnostic rule and then stresses that rule through simulation. The core claim is that austerity frameworks misassign money's functional role by treating households, currency users, quasi-sovereigns, and sovereign issuers as if they faced the same constraint set. They do not. The real limits on government action are capacity, inflation, external dependence, legal architecture, and private-sector fragility, not a universal household-budget rule.

The intended stance is functionalist and systems-engineering in spirit:

- ask what money is doing for each entity inside the system
- ask what variable is actually binding
- ask what the government is functionally responsible for stabilizing or mobilizing
- avoid treating budget rhetoric as if it described settlement reality

## Source Of Truth

- Draft post: `content/posts/money-minsky-policy-mismatch.md`
- Audit of model/prose alignment: `money_minsky_policy_mismatch_AUDIT.md`
- Supporting package overview: `experiments/money_minsky_policy_mismatch/README.md`
- Project-wide blog handoff: `BLOG_SETUP.md`

## Accepted Evidence Chain

- `comparative_constraints.py`
  Provides a stylized household vs currency-user vs sovereign-issuer comparison under the same demand shock.
- `policy_sectoral_model.py`
  Shows the three-sector accounting logic and policy-path comparison used in the sectoral-balance sections.
- `austerity_counterfactual.py`
  Provides the public-data-backed delayed-consolidation counterfactual for Spain and the United Kingdom.
- `policy_controllers.py`
  Provides the ABM policy-lab comparison between deficit-targeting and state-targeting fiscal controllers.
- `sovereign_securities.py`
  Provides the maturity/rollover surface used to distinguish debt stock from refinancing pressure.
- `external_constraint.py`
  Provides the import-dependence and FX-stress surface used to illustrate external real limits.
- `holder_composition.py`
  Provides the holder-mix surface used to distinguish recirculation, leakage, remittance, and wealth concentration.
- `fragility_regimes.py`
  Provides the state-dependent tightening / leverage-fragility experiment used in the fragility sections.
- `capacity_constraint.py`
  Provides the minimal slack-vs-capacity boundary model used to illustrate real-resource and price-pressure limits.

These modules, plus the figures generated from them, are the authoritative computational support for the current draft.

## Excluded Or Downgraded Evidence

- `sfc_model.py` issuer-vs-user result is not a clean evidence source for the current prose because the USER regime can mechanically explode through interest-transfer feedback.
- ABM austerity-shift claims are not currently supported and related figures should not be used as evidence.
- Keen/FIH language must stay calibration-specific and mechanism-level, not universal validation.
- JG discussion may use the activation effect, not wage-level calibration claims.

## Finish Criteria

- Prose is internally consistent and transitions cleanly between conceptual, institutional, and computational sections.
- Every quantitative claim and figure callout matches the current accepted evidence chain.
- References, links, image paths, and reproducibility notes are correct.
- The draft survives a final Hugo-facing editorial review without obvious overclaiming or stale assets.

## Voice

- intellectually serious, not grandiose
- epistemically humble about what simulations do and do not establish
- civic and explanatory rather than partisan or contemptuous
- explicitly useful to readers who want to identify misleading economic claims

## Refinement Layer Outcome

The refinement cycle added minimal modeled surfaces for:

- bonds and securities as refinancing instruments
- maturity structure and rollover risk
- holder composition and interest-income distribution
- external constraint, imported essentials, and FX-sensitive bottlenecks

These layers remain prose/limitation material rather than dedicated model surfaces:

- collateral/liquidity/repo plumbing
- treasury-central-bank operating linkage

## Active Board Shape

Planner / editorial lane:

- `task-024` scope omitted financial-plumbing factors (`done` as of 2026-04-25)
- `task-025` prose pass: bonds, liability hierarchy, and scoped omissions (`done` as of 2026-04-25)
- `task-029` collateral/liquidity and repo scope decision (`done` as of 2026-04-25)
- `task-030` factor-refinement integration and validation pass (`done` as of 2026-04-25)

Implementer / coding lane:

- `task-026` toy sovereign-securities and rollover extension (`done` in repo; verified locally on 2026-04-25)
- `task-027` external-constraint and imported-essentials extension (`done` in repo; verified locally on 2026-04-25)
- `task-028` holder-composition and distribution channel extension (`done` in repo; verified locally on 2026-04-25)

The first cycle's completed tasks (`task-016` through `task-022`) remain the published baseline. The follow-on completeness layer (`task-024` through `task-030`) is now also complete.

## Current Execution Sequence

1. `codex`: `task-024` omitted-factor scoping pass (`done`)
2. `codex`: `task-025` prose pass for bonds, liability hierarchy, and scoped omissions (`done` as of 2026-04-25)
3. `claude`: `task-026` toy sovereign-securities and rollover extension (`done` in repo; verified locally on 2026-04-25)
4. `claude`: `task-027` external-constraint and imported-essentials extension (`done` in repo; verified locally on 2026-04-25)
5. `codex`: `task-029` collateral/liquidity and repo scope decision (`done`; no repo model in this cycle)
6. `claude`: `task-028` holder-composition and distribution channel extension (`done` in repo; verified locally on 2026-04-25)
7. `codex`: `task-030` factor-refinement integration and validation pass (`done`; full suite + Hugo clean)

This sequence is the current handoff memory. If the order changes, update this section and the hub task state together.

## Default Next Steps

- No active refinement tasks remain on the board for this post.
- Future sessions should treat the current draft, audit, and README as synchronized to the full accepted evidence chain.
- Any new work should be a fresh scope decision, not an implicit continuation of `task-024` through `task-030`.
