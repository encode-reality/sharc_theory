# Money, Minsky, and Policy Mismatch

## Simulation surfaces

### Core evidence chain (rebuilt)

- `policy_sectoral_model.py` — Deterministic three-sector policy model: fiscal balances are system outcomes, not household-style budget targets.
- `austerity_counterfactual.py` — Public-data-backed counterfactual using IMF action-based consolidation episodes plus World Bank context.
- `fragility_regimes.py` — State-dependent monetary-tightening experiment built on the Keen-style ODE.

### New simulation surfaces (2026-04-20)

- `comparative_constraints.py` — Three entity types (household, currency user, sovereign issuer) face the same demand shock. Shows how the binding constraint differs by monetary position: hard budget limit vs market-access constraint vs no financing constraint.
- `policy_controllers.py` — ABM policy lab with competing fiscal controllers (austerity vs functional finance). Austerity targets deficit/GDP; functional finance targets labor underutilization. Produces meaningful outcome divergence on output, underutilization, and deficit across seeds.
- `capacity_constraint.py` — Minimal real-capacity boundary model. Under slack, extra spending creates output. At capacity, extra spending creates inflation. Shows the real constraint on sovereign spending is productive capacity, not bookkeeping.

### Factor-refinement surfaces (2026-04-25)

- `sovereign_securities.py` — Toy maturity-ladder model with short/long debt, rollover pressure, and regime-dependent refinancing dynamics. Shows why the same debt/GDP can behave differently depending on maturity structure and whether the entity is an issuer or user.
- `external_constraint.py` — Import-dependence and FX-stress model. Shows that domestic monetary space works under low external dependence but faces real limits (imported inflation, FX pressure) when import dependence is high.
- `holder_composition.py` — Holder-mix and distribution channel. Same nominal debt held by high-MPC households, low-MPC asset holders, foreign investors, or central bank produces different recirculation, leakage, and wealth-concentration outcomes. Stylized — directional, not calibrated.

### Supporting / legacy

- `sfc_model.py` — Stock-flow consistent model (ISSUER/USER regimes). Fixed in 2026-04-20: `mpc_interest` and `max_sovereign_rate` parameters dampen the explosive interest-transfer feedback in the USER regime.
- `abm_model.py` — Agent-based model with Minsky fragility classifier. Extended in 2026-04-20: `fiscal_transfer` and `demand_sensitivity` parameters create a fiscal→demand→firm revenue channel.
- `keen_ode.py` — Goodwin-Keen-Minsky leverage cycle ODE.

## Reproducibility

- Public datasets are downloaded on demand.
- Normalized caches are written under `results/money_minsky_policy_mismatch_data/`.
- Those caches are ignored by git.
- The repo keeps the fetch/normalize code and the source URLs, not copied datasets.
- All simulation code is deterministic (seeded RNG for ABM).

## Main commands

Run all experiments (core + new):

```bash
uv run python -m experiments.money_minsky_policy_mismatch.run_experiment --experiment all
```

Run only the new simulation surfaces:

```bash
uv run python -m experiments.money_minsky_policy_mismatch.run_experiment --experiment new
```

Run the full test suite (200 tests):

```bash
uv run python -m pytest experiments/money_minsky_policy_mismatch/tests/ -v
```

Refresh the public data cache:

```bash
uv run python -m experiments.money_minsky_policy_mismatch.run_experiment --experiment all --refresh-data
```

## Source data

- IMF action-based fiscal consolidation dataset:
  `https://www.imf.org/-/media/files/publications/wp/2024/datasets/wp24210.zip`
- World Bank API indicators:
  - `SL.UEM.TOTL.ZS` unemployment rate
  - `GC.DOD.TOTL.GD.ZS` central government debt (% GDP)

## Output figures

All figures written to `static/images/money_minsky_policy_mismatch/`.

### Core figures

- `policy_sectoral_paths.png` — Output/tax paths under supportive, austerity, delayed repair
- `policy_sectoral_balances.png` — Three-sector accounting identity
- `imf_counterfactual_cases.png` — IMF austerity episodes vs counterfactual
- `fragility_regimes.png` — Fragile vs resilient regime comparison
- `keen_stable_vs_crisis.png` — Keen ODE stable cycle vs debt explosion

### New figures (generated 2026-04-20)

- `comparative_constraints.png` — Spending, output, and debt paths for household / currency user / sovereign issuer under the same demand shock
- `policy_lab.png` — Output, underutilization, and deficit under austerity / functional finance / passive controllers
- `capacity_constraint.png` — Slack vs tight capacity: output and inflation under different utilization levels

### Factor-refinement figures (generated 2026-04-25)

- `rollover_comparison.png` — Effective rate, rollover need, and debt stock for issuer/user × short/long maturity
- `external_constraint.png` — Output, FX stress, and inflation under low vs high import dependence
- `holder_composition.png` — Output, net domestic interest flow, and wealth concentration across HH/asset/foreign/CB holder mixes

### Concept diagrams

- `constraint_hierarchy.png` — Entity types and their constraint sets
- `campaign_vs_operational_models.png` — Household-budget story vs balance-sheet model
- `wrong_target_control.png` — Deficit-targeting vs state-targeting control flow

## Validation record

Last full validation: 2026-04-25

- 200 tests passed (pytest), 0 failures
- Figures generated from: `run_experiment --experiment new`
- Seed: 42 (default)
- Platform: macOS arm64, Python 3.12, uv
