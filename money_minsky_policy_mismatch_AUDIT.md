# Money, Minsky, and Policy Mismatch Audit

This document records the review of:

- `content/posts/money-minsky-policy-mismatch.md`
- `experiments/money_minsky_policy_mismatch/`
- the associated test suite

The objective was not to weaken the thesis. The objective was to preserve the core thesis while making the support structure honest:

> contemporary policy often relies on a model of government finance that treats the state like a household, even though that model does not correspond to how sovereign money, private credit creation, and balance-sheet constraints actually operate.

## Update Note: 2026-04-25

This audit captured the state of the project before the follow-on repair tasks were completed. Since then:

- `task-018` added `comparative_constraints.py`, which now replaces the old issuer-vs-user surface for the post's entity-comparison role.
- `task-019` added `policy_controllers.py`, which replaced the previously inert ABM austerity channel with a working policy-lab comparison.
- `task-020` added `capacity_constraint.py`, so the repo now includes a minimal real-capacity / price-pressure boundary model.
- `task-021` generated new figures and updated the experiment README.

The legacy cautions in this audit still matter:

- do not reuse `issuer_vs_user.png` as settled evidence
- do not reuse `austerity_minsky_shift.png` as settled evidence
- keep Keen/FIH claims calibration-specific
- keep JG discussion away from unsupported wage-calibration claims

But future sessions should not read this audit as saying the repo still lacks any comparative entity model, ABM policy divergence, or real-capacity boundary surface. Those gaps were addressed in the later task sequence.

## Update Note: 2026-04-26

The factor-refinement cycle is now also complete:

- `task-026` added `sovereign_securities.py`, which distinguishes debt stock from maturity structure and rollover pressure.
- `task-027` added `external_constraint.py`, which distinguishes domestic slack from imported-essential dependence and FX stress.
- `task-028` added `holder_composition.py`, which distinguishes recirculation, leakage, remittance, and wealth concentration across different liability holders.
- `task-029` resolved repo/collateral as an explicit limitation rather than a dedicated model surface for this post.

The accepted evidence chain is therefore broader than the original audit body reflects. The cautions below about legacy SFC behavior, legacy ABM claims, and overclaiming still stand, but future sessions should not read the original text below as if maturity structure, holder composition, or external constraint were still entirely absent from the package.

## What Was Checked

- Read the full draft post.
- Read the SFC, Keen ODE, ABM, experiment runner, and tests.
- Ran `poetry run pytest experiments/money_minsky_policy_mismatch/tests/ --no-cov`.
- Ran direct reruns and sensitivity probes outside the test suite.

At the time of the original audit, all 81 tests passed. That established internal consistency for that earlier package state. It did **not** establish that the prose was calibrated to what the models really showed, and it is no longer the current test count.

## Critical Findings

### 1. The current issuer-vs-user SFC result does not support the prose

The draft originally treated the issuer-vs-user simulation as evidence that the USER regime loses fiscal space and suffers output deterioration under the same shock. The current code does not support that cleanly.

Why:

- In `experiments/money_minsky_policy_mismatch/sfc_model.py`, household disposable income includes sovereign interest income: `YD = ... + interest_exp`.
- In the USER regime, higher sovereign spreads therefore raise transfers to households at the same time that they raise government interest expense.
- That mechanism can dominate the contraction channel before forced consolidation bites.

Direct rerun:

- `ISSUER` mean output over periods 60:80 after the shock: about `75.31`
- `USER` mean output over periods 60:80 after the shock: about `26268.49`
- `USER` output at period 80: about `78587.98`

Implication:

- The current issuer-vs-user experiment is **not usable as clean evidence** for the prose claim that the user regime visibly contracts relative to the issuer regime.
- It is, at best, a stylized financing-architecture toy model with an unstable interest-transfer feedback.

Action already taken in the draft:

- Removed the issuer-vs-user plot from the evidence chain.
- Narrowed the computational claim in the sectoral-balance section to the closed-economy accounting identity.

### 2. The ABM austerity channel is currently inert

The draft originally said the ABM austerity experiment shifts the Minsky distribution toward fragility. Direct reruns do not support that.

Direct reruns:

- `austerity_phi = 0.0, 0.2, 0.5, 0.8` produced identical sampled outcomes over periods 60:100 for:
  - hedge share
  - ponzi share
  - unemployment
  - JG share
  - output
- Comparing `austerity_phi = 0.0` vs `0.5` across seeds `42`, `99`, and `123` produced zero delta on the reported sampled metrics.

Implication:

- The current ABM austerity path is not discriminative enough to support any prose claiming that austerity accelerates the hedge-to-speculative-to-Ponzi transition in this model.
- The figure `austerity_minsky_shift.png` should not currently be used as evidence.

Action already taken in the draft:

- Removed the austerity-to-fragility figure from the post.
- Rewrote the section to say the computational support is uneven and that the ABM austerity channel is not yet being used as settled evidence.

### 3. The Keen ODE section was overclaiming

The draft originally said the simulation validates both propositions of FIH and generates crisis regardless of initial conditions. That is too strong.

Direct reruns:

- Under the default calibration, `d0` values `0.1`, `0.3`, `0.5`, `1.0`, `2.0`, and `3.0` all crossed the crisis threshold within 200 time units.
- But increasing debt drag to `k2 = 0.2` eliminated crisis within the same horizon; maximum debt stayed around `3.39`.

Implication:

- The result is calibration-dependent.
- The current model supports a narrower statement:
  - under the default calibration, the system exhibits early bounded cycles and later crisis-like debt escalation without an external shock
- It does **not** support:
  - a general proof of FIH
  - a claim that crisis is calibration-invariant
  - a claim that the model validates Minsky's propositions in the strong sense

Action already taken in the draft:

- Replaced “validates” language with calibration-specific, mechanism-level wording.

### 4. The JG experiment currently supports activation, not wage-level calibration

The draft originally described the JG experiment as a comparison across JG wage levels. The current implementation is informative mainly about JG on/off.

Direct reruns:

- `w_jg = 0.0` produced materially higher unemployment.
- Positive values `0.5`, `1.0`, and `1.5` produced identical sampled outcomes on:
  - unemployment
  - JG share
  - output
  - ponzi share

Implication:

- The current model supports the existence of an employment-buffer channel.
- It does **not** currently support comparative claims about JG wage calibration.

Action already taken in the draft:

- Rewrote the JG paragraph to say the current implementation is more sensitive to activation than to wage level.

### 5. The test suite is partly narrative-confirming rather than adversarial

Several tests are written to confirm the desired story rather than to challenge it.

Examples:

- `experiments/money_minsky_policy_mismatch/tests/test_keen_ode.py`
  - says the model is “inherently unstable”
  - asserts “all initial conditions produce crisis” for a narrow chosen set
- `experiments/money_minsky_policy_mismatch/tests/test_experiments.py`
  - says it validates results “consistent with the blog's claims”
  - JG test only checks `with_jg_share >= 0.0`
  - issuer/user tests do not assert the claimed output divergence
  - ABM austerity tests do not assert any directional effect

Implication:

- Passing tests here means the implementation is self-consistent.
- It does not mean the post's current interpretation is robust.

## Claim-Support Map

| Claim | Type | Current Support Level | Correct Framing |
|------|------|------------------------|-----------------|
| Household budgeting is the wrong model for sovereign issuers | Institutional / conceptual claim | Strong | Keep explicit; this is the thesis |
| Bank lending creates deposits | Operational / institutional claim | Strong | Keep explicit |
| Sectoral balances sum to zero across private, government, foreign sectors | Accounting identity | Strong in theory, partial in code | Keep full identity in prose, but say code verifies only the closed-economy subcase |
| Fiscal balances are poor universal policy targets | Accounting + policy interpretation | Moderate to strong | Keep, but anchor in identity and institutional consequences |
| Similar debt stocks can behave differently when maturity and rollover structure differ | Model-derived claim | Moderate | Keep as a stylized refinancing result, not a bond-market model |
| Domestic slack can coexist with external constraint when import dependence is high | Model-derived claim | Moderate | Keep as a complement to the capacity-boundary argument, not a full open-economy model |
| The same nominal debt stock can have different recirculation and leakage effects depending on holder mix | Model-derived claim | Moderate | Keep as a directional holder-composition result, not a full political-economy calibration |
| Current SFC code demonstrates issuer vs user output divergence | Model-derived claim | Weak / contradicted by reruns | Do not use as current evidence |
| Current Keen simulation validates FIH generally | Model-derived claim | Weak | Reframe as calibration-specific mechanism illustration |
| Current ABM demonstrates austerity-driven fragility shift | Model-derived claim | Unsupported by reruns | Remove as evidence until model is fixed |
| Current ABM shows JG wage-level calibration effects | Model-derived claim | Weak | Reframe as JG activation effect only |

## Draft Changes Applied

The post itself was revised to align with the evidence currently available.

Applied changes:

- Made the title and description less rhetorical.
- Tightened the opening to foreground model mismatch rather than rhetorical contrast.
- Replaced one inaccurate implication of endogenous money with a more precise statement about omitted state variables.
- Narrowed the sectoral-balance computational claim to the closed-economy identity.
- Removed the issuer-vs-user figure from the evidence chain.
- Narrowed the Keen section from “validation” to “stylized mechanism under the default calibration.”
- Narrowed the ABM Minsky section from strong demonstration to partial mechanism support.
- Removed the ABM austerity figure from the evidence chain.
- Narrowed the JG section from wage-level comparison to activation-versus-no-activation.
- Replaced “Goodharted” phrasing with more explicit target/indicator language.
- Kept the central political claim explicit: policy goes wrong when the state is modeled as if it were a household.

## Remaining Refinement Opportunities

- The post still relies more on literature claims than on simulations for the issuer/user distinction. That is acceptable, but it should remain clearly signposted.
- The SFC section could still use one short sentence stating why private net saving and government deficits are mirrors only in an accounting sense, not as a policy prescription.
- The Minsky section could still use one sentence distinguishing “mechanism illustration” from “empirical macro validation.”
- The JG section is now honest, but the figure should eventually be regenerated once wage-level sensitivity is meaningful.

## Pseudocode Briefs for the Developer

### 1. Fix or replace the issuer-vs-user SFC experiment

Purpose:

- prevent the USER regime from generating explosive output through sovereign-interest transfers
- recover a usable stylized contrast between financing architectures

Pseudocode:

```text
define alternative USER treatments for sovereign interest income:
    option A: do not feed sovereign interest directly into household disposable income
    option B: route interest through a separate wealth channel with lower consumption propensity
    option C: model consolidation and risk premia without positive transfer feedback dominating demand

for each treatment:
    run issuer and user under the same spending shock
    measure:
        output path
        debt path
        effective spending path
        sovereign rate path

accept if:
    USER no longer explodes mechanically through interest-income feedback
    divergence, if present, is interpretable as financing constraint rather than accounting artifact
```

### 2. Make the ABM austerity channel actually bind

Purpose:

- ensure austerity changes the simulated trajectory in a measurable way

Pseudocode:

```text
inspect current austerity rule:
    compute when deficit_ratio exceeds target
    log whether cut_fraction ever becomes positive
    log whether any JG workers are actually fired

if rule rarely binds:
    increase sensitivity of the rule
    or redefine austerity as one of:
        reduced JG wage
        delayed JG hiring
        direct public spending cut
        tax increase

for each austerity rule:
    run multiple seeds
    compare baseline vs austerity on:
        unemployment
        JG share
        hedge/speculative/ponzi shares
        output

accept if:
    austerity changes at least one of the target outcomes in a consistent direction across seeds
```

### 3. Convert the Keen experiment into a real robustness check

Purpose:

- determine whether crisis is robust or calibration-dependent

Pseudocode:

```text
for each parameter in {r, k1, k2, a1, delta}:
    sweep across a broad but plausible range

for each initial condition in {omega0, lambda0, d0} grid:
    solve model to horizon T
    record:
        crisis yes/no
        time to crisis
        max debt
        whether early bounded cycle exists

summarize:
    regions with crisis
    regions with delayed crisis
    regions with no crisis

accept if:
    prose can be tied to a map of where the mechanism appears
    not just a single chosen calibration
```

### 4. Upgrade the JG experiment from on/off to wage-calibration sensitivity

Purpose:

- make positive JG wages behave differently so the experiment can support comparative claims

Pseudocode:

```text
check whether JG wage level actually affects:
    household disposable income
    consumption
    re-hiring dynamics
    firm labor competition

if not:
    introduce wage-level transmission channels, for example:
        private hiring responds to JG outside option
        JG wage changes aggregate demand directly
        firms face tighter labor costs when JG wage is higher

rerun positive wage levels:
    low JG wage
    mid JG wage
    high JG wage

measure:
    unemployment
    JG share
    output
    fragility shares
    any inflation proxy if one is added later

accept if:
    different positive JG wages generate meaningfully different trajectories
```

### 5. Replace narrative-confirming tests with adversarial tests

Purpose:

- make the suite challenge the article rather than merely echo it

Pseudocode:

```text
for each headline article claim:
    create:
        one confirming scenario
        one boundary scenario
        one challenging scenario

examples:
    claim: rate hikes are dangerous under leverage
        challenge with low leverage and strong debt drag
    claim: austerity worsens fragility
        challenge with a rule that barely binds
    claim: issuer/user regimes diverge
        challenge with parameter sets where divergence should be weak

accept if:
    the suite can tell when a claim fails, weakens, or becomes conditional
```

## Bottom Line

The core thesis survives the audit and should remain explicit:

- policy frequently models the government as if it were a household
- that is the wrong architecture for a sovereign currency issuer
- once the wrong architecture is imposed, deficits become targets, private credit is under-modeled, and stabilization policy is mis-specified

What had to change was not the thesis. What had to change was the evidentiary discipline around the simulations. The current draft is now better aligned with that standard, but the code package still needs work before some of the stronger computational claims can be restored.
