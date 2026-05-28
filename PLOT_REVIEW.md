# Plot Review and Improvement Plan

Audit of the 6 new figures in `static/images/money_minsky_policy_mismatch/` against the prose they support in `content/posts/money-minsky-policy-mismatch.md`. Goal: each figure should land as obvious evidence the moment a reader's eye hits it, not a puzzle that requires reading the surrounding paragraph twice.

The user's specific report — "the most left and most right plots don't have any red lines which are supposed to be the household line" — is correct. The household line is rendered, but it is hidden behind another line (Spending) or visually flat against an exploding axis (Debt Ratio). That same problem (lines invisible because of overlap or scale) recurs in several other plots.

---

## 1. `comparative_constraints.png` — section 2

**Story the prose tells:**
> "Under that setup, the household eventually hits a borrowing ceiling, the currency user faces rising financing pressure and consolidation, and the sovereign issuer maintains nominal spending."

**What the plot actually shows:**

| Panel | Diagnosis |
|---|---|
| Spending | Household (red) is plotted but sits at exactly 48 — the same value as the sovereign issuer (green). The red line is *under* the green line for the entire 120-period run, so it appears to be missing. The currency user (orange) is visible because it collapses around period 85. |
| Output / Activity | Household at ~48 vs sovereign and user at ~190. The household line is technically visible but reads as a "floor", not a comparable trajectory. The reason is that household "output" = its own spending (no fiscal multiplier) while government output = `(A + G) / denom`. These are not on the same scale and the plot does not say so. |
| Debt Ratio | Currency user's debt ratio explodes to ~3500 by period 120, dwarfing the household (debt/income ≈ 0–4 range) and sovereign issuer (debt/output ≈ 0–2 range). Both household and issuer lines look pinned at zero. The user's story dominates; the household and issuer story disappears. |

**Fixes:**

1. **Differentiated line styles**: Household solid, currency user dashed, sovereign issuer dotted (or use a distinctive marker). Lines that overlap remain readable.
2. **Axis honesty for output**: Drop the "Output / Activity" panel as currently drawn. Replace with a **normalized "spending vs target"** panel (each entity's spending / its own pre-shock spending target), so all three are on the same 0–1.05 scale and the divergence is visible. Or split into two stacked panels: government output (user vs issuer, multiplier scale) above household activity (household scale) below.
3. **Debt ratio split**: Either log-scale the debt ratio panel (matplotlib `set_yscale("log")`) so all three trajectories are visible, or replace the panel with **"is the constraint binding?"** — a binary indicator panel showing when each entity hits its constraint (household at borrowing ceiling, user at forced consolidation, issuer never).
4. **Annotations**: Add a vertical arrow at the shock period labeled "private demand shock". Add text callouts: "household hits borrowing ceiling ≈ p85", "user forced consolidation ≈ p85", "issuer maintains spending throughout".
5. **Caption clarification**: Add a one-line subtitle to the figure: *"Household 'output' is its own spending; government 'output' is GDP via fiscal multiplier — they are not directly comparable in level, only in trajectory."*

---

## 2. `rollover_comparison.png` — section 2

**Story the prose tells:**
> "Under the same headline debt ratio, a short-maturity currency user hits spread pressure and forced consolidation sooner than a long-maturity user, while the issuer path is much less sensitive to rollover need."

**What the plot actually shows:**

| Panel | Diagnosis |
|---|---|
| Effective Interest Rate | User-short hits the 0.20 rate cap by period 25; user-long hits it by period 40. Issuer (green) is pinned at 0.02 — visually *invisible* because the y-axis spans 0.02–0.20 and the issuer line sits on the bottom edge. |
| Rollover Need | User-short explodes to ~150,000; user-long climbs to ~5,000; issuer lines are flat at the bottom and unreadable. The y-axis is dominated by the user-short explosion. |
| Total Debt Stock | Same problem: user-short at ~175,000, user-long ~12,000, issuer pinned to bottom. |

**Fixes:**

1. **Log scale on rollover and debt panels**: All four series become visible across the full time horizon.
2. **Inset for issuer detail**: A small inset axis showing issuer-only debt growth (slow, linear) so the reader sees it isn't zero, just dwarfed.
3. **Annotation at the rate cap**: Horizontal dashed line at 0.20 labeled "market lockout cap"; mark the periods at which user-short and user-long hit it.
4. **Color discipline**: User-short red, user-long orange (good); issuer-short and issuer-long should both be greens but distinct (e.g., bright green and dark green) — currently the legend lists two greens but they read as one line.
5. **Subtitle explaining the asymmetry**: *"Issuer rate is policy-set; user rate rises with debt + rollover spread, capped at lockout."*

---

## 3. `policy_lab.png` — section 5

**Story the prose tells:**
> "Under the default configuration, the austerity controller does what it is designed to do on its own terms: it lowers the deficit faster. But it does so with weaker output and higher underutilization than the state-targeting controller."

**What the plot actually shows:**

| Issue | Diagnosis |
|---|---|
| Resolution | The current PNG is rendered tiny (much smaller than the other figures). The DPI / figsize is wrong. |
| Deficit panel | A dense band of vertical lines suggests the deficit ratio is oscillating wildly period-to-period — likely because consumption-based revenue and step-changing JG policy interact stochastically. The signal is there but buried in noise. |
| Phase markers | No annotation showing where the controllers diverge from passive baseline. |

**Fixes:**

1. **Re-render at correct size**: Match the other 3-panel figures (15×5 inches at dpi=150).
2. **Smooth the deficit panel**: Apply a 5- or 10-period moving average so the trend is visible, with the raw series as a faint underlay. Or just plot the smoothed series.
3. **Annotation**: Mark the period at which austerity's deficit drops below the passive baseline (the "succeeded on its own terms" moment) and the period at which functional finance's underutilization undercuts austerity's.
4. **Subtitle**: *"Austerity wins the deficit panel; functional finance wins the underutilization and output panels — the disagreement is about what to stabilize first."*

---

## 4. `capacity_constraint.png` — section 7

**Story the prose tells:**
> "Under slack, extra spending raises output; near capacity, more of the effect turns into inflation."

**What the plot actually shows:**

This is the strongest of the six. Three clean panels: output (slack vs tight vs capacity dashed), inflation (slack flat at zero, tight elevated), spending ramp transition with dual axis.

**Minor fixes:**

1. **Shaded background on the ramp panel**: A faint green shade where output < capacity, faint red where output ≥ capacity. Makes the slack-to-tight transition visually obvious.
2. **Annotation at the ramp crossover**: "spending ramp crosses capacity ≈ p20 → inflation pressure begins".
3. **Subtitle**: *"Below capacity: full multiplier, no inflation. At capacity: spending mostly becomes inflation, not output."*
4. **Optional**: Replace the dual-axis on the third panel with a stacked normalized chart (output share vs inflation share of an extra dollar of spending). Cleaner story, no dual-axis cognitive load.

---

## 5. `external_constraint.png` — section 7

**Story the prose tells:**
> "Under low import dependence, domestic monetary space works; under high import dependence, the economy can still have domestic slack while FX stress and imported inflation start to bind."

**What the plot actually shows:**

| Panel | Diagnosis |
|---|---|
| Real Output | Two flat lines: low dep. at 150, high dep. at 95. No shock, no transition — just two equilibria. The level gap is the message but it's hard to interpret without knowing what 150 vs 95 means. |
| FX Stress | High dep. settles around 0.65, low dep. at 0. Story is clear. |
| Inflation (total + imported) | High dep. total and high dep. imported are exactly the same line — the dashed line is visible but they should not occupy the same y-values if "total" includes domestic inflation too. The model gives both as ~0.65 because there's no domestic inflation here. The implication is that the third panel is showing the same story as the FX stress panel. |

**Fixes:**

1. **Add a stress shock**: Currently the model is in steady state from period 0. Add a step increase in import_share or a drop in export_earnings at period 15 so each panel shows a transition rather than a flat equilibrium.
2. **Drop redundant inflation panel**: If imported = total, the third panel duplicates the second. Replace with **"output gap" or "real purchasing power"** — output divided by price level — to show that high dep. loses real output through inflation even if nominal output is stable.
3. **Annotation on output panel**: Label the level gap explicitly: "high import dep. operates at 63% of low-dep output — same domestic policy, different real ceiling."
4. **Subtitle**: *"Same domestic monetary policy. Different external exposure. The constraint that binds is real, not financial."*

---

## 6. `holder_composition.png` — section 5

**Story the prose tells:**
> "When more of the liabilities are held by high-MPC domestic households, interest payments recirculate into demand more strongly. When the same liabilities are held by foreign investors, more of the flow leaks out of the domestic economy. When the central bank holds more of the debt, remittances reduce the net fiscal cost."

**What the plot actually shows:**

All four series are perfectly flat (no period-to-period change) because debt is held constant and the model is in steady state. The user sees a legend with four colors and four flat horizontal lines. Story is *technically* there (the level differences) but visually static and unconvincing.

| Panel | Diagnosis |
|---|---|
| Output | Four flat lines at 157, 158, 158, 164. Tightly clustered. Looks like noise. |
| Net domestic interest flow | Four flat lines at -5, 0.4, 0.8, 3.7. Clearer ordering but still static. |
| Wealth concentration | Four flat lines at 0.42, 0.85, 0.97 (foreign-heavy is missing because foreign holders aren't tracked as domestic wealth). |

**Fixes:**

1. **Replace time-series panels with bar charts** for steady-state quantities. Three bar charts (output, net domestic flow, concentration) across the four scenarios is much more readable than four flat lines.
2. **Or: introduce a debt-buildup phase**: Have debt grow from 0 to D over the first 30 periods, so the wealth-concentration panel actually shows accumulation curves diverging.
3. **Foreign-heavy concentration**: Currently the y-axis goes 0–1 but foreign-heavy doesn't appear. Either add a "foreign claims share" line, or note in the caption that wealth concentration is *domestic-only* and foreign holdings represent leakage rather than concentration.
4. **Subtitle**: *"Same nominal debt, same coupon, same gov. Only the holder mix changes."*

---

## Cross-cutting fixes

These apply to all the new figures:

1. **Consistent y-axis treatment**: When one series explodes by 1000× while another stays bounded, default to a log scale OR a small-multiples layout (one panel per scenario). Otherwise the bounded series visually disappears.
2. **Annotations are not optional**: Every plot needs at least one text callout pointing at the moment / region where the headline happens. Right now most plots rely on the reader inferring meaning from line shape alone.
3. **Caption-as-subtitle**: The blog caption is HTML alt text — readers don't see it next to the figure unless they hover. A short bold subtitle inside the figure (one sentence under the title) does the work the alt text is currently expected to do.
4. **Dark theme readability**: Some lines disappear at the y-axis edge. Add a faint white border or use brighter colors for series pinned to extremes.
5. **Resolution discipline**: `policy_lab.png` is rendered at lower resolution than the others. Audit the `dpi` and `figsize` parameters across all `plot_*` functions.
6. **Plot-prose alignment**: A few figures sit *below* their introducing paragraph but don't get a "what to look for" sentence after them. Adding one line after each figure ("In the panel above, the orange line collapses at period 85 — that is the binding constraint moment") would tighten the read substantially. This is a prose change, not a plot change, but it is part of the same problem.

---

## Suggested execution order

Highest impact first:

1. **comparative_constraints.png** (most cited problem; fixes line-overlap and scale-mismatch issues that the user explicitly flagged).
2. **policy_lab.png** (resolution + deficit-noise are blocking issues).
3. **rollover_comparison.png** (log scale unblocks the issuer comparison).
4. **holder_composition.png** (replace flat time series with bars; major readability win).
5. **external_constraint.png** (add transition + drop redundant panel).
6. **capacity_constraint.png** (already strong; minor polish only).

After plot fixes, do a separate pass on the prose to add a one-line "what to notice" sentence after each figure.

---

## What I'd like confirmed before implementing

- **Replace the third panel of `comparative_constraints.png`** (debt ratio) with **"is the constraint binding?"** — a binary indicator panel? Or keep debt ratio but on log scale?
- **Bar chart vs. accumulation chart for `holder_composition.png`** — both work; bars are cleaner, accumulation charts preserve the "model is dynamic" framing.
- **Resolution / size standard** — the current 15×5 inches at dpi=150 is fine for blog inline rendering, but if you want larger high-DPI figures for printing, that should be a global decision before I re-render.
- **In-figure subtitles** — confirm you want the additional one-line subtitle inside each figure (under the bold title). Some folks prefer to keep figures clean and rely on the surrounding caption.

Once these four are confirmed, the actual work is mechanical: edit the relevant `plot_*` functions in `experiments/money_minsky_policy_mismatch/plotting.py`, regenerate, commit.
