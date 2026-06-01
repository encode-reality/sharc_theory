# Factor Refinement Plan: `money-minsky-policy-mismatch`

This note defines the next refinement cycle for the money/minsky post after the initial publish-ready baseline.

## Status

- `task-024` is complete.
- `task-025` is complete.
- `task-026` is complete.
- `task-027` is complete.
- `task-028` is complete.
- `task-029` is complete.
- `task-030` is complete.

## Goal

Make the post more complete about financial plumbing without letting it sprawl into a full monetary operations textbook.

The point is not to model every balance-sheet channel. The point is to avoid sounding naive or overfitted by naming the missing layers that materially qualify the argument:

- public securities are not just "borrowing"
- maturity and rollover structure matter
- holder composition matters
- collateral and liquidity roles matter
- external constraint can bind before domestic bookkeeping does

## Scope Principle

The post's fundamental claim does **not** require a full repo-market, dealer-balance-sheet, or term-structure model.

It **does** require enough treatment of omitted factors that a careful reader cannot reasonably say:

- the post ignores what bonds functionally do
- the post ignores refinancing risk for currency users or quasi-sovereigns
- the post ignores imported essentials, FX stress, or external dependence
- the post quietly assumes all public debt has the same macro effect regardless of who holds it

So the refinement rule is:

- model only the omitted factors that can materially alter the post's main diagnosis
- mention explicitly the omitted factors that matter but do not need their own toy model here
- keep the prose honest about what remains abstracted away

## Factor Triage

### 1. Bonds and Securities As Functional Instruments

Why it matters:

- For a sovereign issuer, bonds are not merely household-style funding needs.
- They can function as interest-bearing state liabilities, savings vehicles, collateral, and part of rate/liquidity management.
- For a currency user or quasi-sovereign, refinancing conditions can become a direct constraint.

Blog treatment:

- High priority.
- Add to section 2 or just after section 2.
- Add one concise transition in section 3 linking securities to operational institutions.

Model treatment:

- High-value toy model opportunity.
- Do not attempt auction microstructure, yield curve estimation, or dealer networks.
- Focus on maturity, rollover, refinancing pressure, and perhaps one small holder split.

Time:

- Prose: `0.5` to `1` day
- Code: `1` to `2` days

### 2. External Constraint, Imported Essentials, and FX Pressure

Why it matters:

- A sovereign issuer can make domestic-currency payments, but cannot conjure imported fuel, food, semiconductors, or foreign exchange.
- This is one of the cleanest ways to show why "not financially constrained like a household" does **not** mean "no constraint."

Blog treatment:

- High priority.
- Strengthen section 2 constraint list.
- Add one explicit paragraph in section 7 limitations / interpretation.
- Add diagnostic questions in section 8.

Model treatment:

- High-value toy model opportunity.
- Extend the capacity-boundary logic with an imported-essential or FX-pass-through bottleneck.
- Keep it minimal and interpretable.

Time:

- Prose: `0.5` day
- Code: `1` to `2` days

### 3. Holder Composition and Distribution

Why it matters:

- The same debt stock behaves differently if interest flows go to domestic high-spending households, low-MPC asset holders, foreign holders, or the central bank.
- This affects leakage, recirculation, and the political meaning of interest transfers.

Blog treatment:

- Medium priority.
- Name it explicitly in section 7 and possibly in section 5 when discussing why a debt stock alone is not enough.

Model treatment:

- Useful but not essential for the main post.
- A minimal holder split can be enough.
- If the channel lands weakly, it may stay limitation-level rather than figure-level.

Time:

- Prose: `0.25` to `0.5` day
- Code: `1` day

### 4. Collateral, Liquidity, and Repo Plumbing

Why it matters:

- Public securities function as safe collateral and liquidity instruments.
- Funding markets and haircuts can transmit stress in ways a simple deficit story misses.

Blog treatment:

- Medium importance for completeness.
- Low priority for full computational treatment in this post.
- Best location is section 3 operational institutions plus section 7 limitations.

Model treatment:

- Investigation first, not immediate build.
- Only justify a toy model if it changes the blog's core explanatory burden.
- Otherwise, name it cleanly as an omitted but relevant layer.

Time:

- Investigation/prose: `0.5` day
- Code: future-only unless the investigation says it is necessary

### 5. Treasury-Central Bank Operating Linkage

Why it matters:

- This helps explain why issuer systems do not work like household accounts.
- It also clarifies why securities issuance is not simply "the government getting money first."

Blog treatment:

- Medium priority prose only.
- Best in section 3 where the post already contrasts campaign rhetoric with operational institutions.

Model treatment:

- No dedicated model needed for this post.
- A clear paragraph is enough.

Time:

- Prose only: `0.25` day

## Recommended Blog Placement

### Section 2: Different Entities, Different Monetary Roles

Add:

- one short subsection or paragraph: "Bonds are not one thing"
- explain that the same security can be a savings asset/collateral instrument for one actor and a refinancing obligation for another
- make clear that issuer vs user is partly about liability hierarchy and rollover exposure, not just "who can print"

### Section 3: Two Models of the Same Economy

Add:

- one operational paragraph on why treasuries and central banks care about reserves, collateral, settlement, and securities markets
- one sentence explaining that this is why campaign rhetoric misses the plumbing

### Section 5: Austerity Is a Control Problem

Add:

- one sentence that deficit targeting also abstracts from maturity structure, refinancing pressure, and holder composition
- one sentence that for quasi-sovereigns these are closer to direct constraints than for issuers

### Section 7: What the Experiments Do and Do Not Establish

Add:

- explicit limitation language for maturity structure, holder composition, collateral/repo, and treasury-central-bank operating detail
- explicit statement that external constraint matters and deserves model treatment because it can be a real limit even when domestic slack exists

### Section 8: How to Spot Policy Mismatch Around You

Add diagnostic questions:

- who holds the liabilities?
- in what currency are critical obligations or imports priced?
- what share of debt must be rolled soon?
- are securities functioning mainly as safe assets/collateral, or is refinancing access itself becoming the problem?

## Recommended Sequence

High-priority sequence:

1. `task-024` — scope the omitted-factor matrix
2. `task-025` — prose pass for bonds, liability hierarchy, and scoped omissions (`done` as of 2026-04-25)
3. `task-026` — toy sovereign-securities / rollover extension (`done` in repo; verified locally on 2026-04-25)
4. `task-027` — external-constraint / imported-essentials extension (`done` in repo; verified locally on 2026-04-25)
5. `task-029` — repo/collateral scope decision (`done`; no repo model in this cycle)
6. `task-028` — holder-composition extension (`done` in repo; verified locally on 2026-04-25)
7. `task-030` — integration and validation (`done`; full suite + Hugo clean)

Why this order:

- The prose needs scoping before it grows.
- Rollover and external constraint are the highest-value modeling additions because they most directly qualify the thesis.
- Repo/collateral is important, but it is the easiest place for scope creep.
- Holder composition is useful but second-order compared with rollover and external constraint.

## Task Map

- `task-024` priority `3`: scope omitted financial-plumbing factors
- `task-025` priority `4`: prose pass for bonds, liability hierarchy, and scoped omissions (`done`)
- `task-026` priority `5`: toy sovereign-securities and rollover extension (`done`)
- `task-027` priority `6`: external-constraint and imported-essentials extension (`done`)
- `task-029` priority `7`: collateral/liquidity and repo scope decision (`done`)
- `task-028` priority `8`: holder-composition and distribution channel extension (`done`)
- `task-030` priority `10`: factor-refinement integration and validation pass (`done`)

## `task-029` Outcome

Recommendation:

- keep collateral/repo as a named limitation in this post
- do not add a dedicated repo/liquidity model in this cycle

Why:

- `task-026` now covers the highest-value refinancing channel directly: maturity structure and rollover pressure
- `task-027` now covers the highest-value external qualifier directly: import dependence and FX stress
- repo/collateral plumbing matters mainly for how stress amplifies through funding markets, not for the post's first-order diagnosis of household vs user vs issuer constraint mismatch
- a toy repo model would either be too thin to justify or would require dealer balance sheets, haircut dynamics, and market-making assumptions that would expand scope fast

Required prose position:

- say clearly that collateral/repo chains matter because they can amplify liquidity stress and market-access pressure once stress begins
- say equally clearly that they are not the first-order reason the household analogy fails

Future trigger for a dedicated model:

- only build one if a later post is specifically about crisis transmission, dealer balance sheets, haircuts, or safe-collateral shortages

## Pseudocode Briefs For Claude

### `task-026`: Toy Sovereign-Securities and Rollover Extension

Purpose:

- separate debt stock from refinancing pressure
- show why maturity structure matters for currency users and quasi-sovereigns
- keep issuer/user distinctions functional rather than mystical

Pseudocode:

```text
state variables:
    debt_short
    debt_long
    avg_coupon
    debt_to_gdp
    rollover_need
    effective_rate
    holder_share_domestic
    holder_share_foreign (optional minimal split)

each period:
    maturing = debt_short
    rollover_need = primary_deficit + maturing

    if regime == issuer:
        effective_rate = policy_rate or modest term premium
        quantity_constraint = none
    else if regime == user/quasi-sovereign:
        spread = base_spread
               + phi * max(debt_to_gdp - threshold, 0)
               + psi * max(rollover_need / gdp - rollover_threshold, 0)
        effective_rate = base_rate + spread
        if spread > lockout_threshold:
            forced_consolidation or issuance_cap triggers

    interest_expense = effective_rate * outstanding_debt
    new_debt = old_debt + primary_deficit + interest_expense
    issue new debt with maturity split:
        new_short = issuance * short_share
        new_long  = issuance * (1 - short_share)

    output reacts through fiscal channel
    revenue reacts to output

compare:
    same debt/gdp, different short_share
    same debt/gdp, different rollover_need
    issuer vs user under same shock

accept if:
    model shows debt stock alone is not sufficient
    maturity/refinancing differences are readable without full bond-market detail
```

### `task-027`: External Constraint and Imported-Essentials Extension

Purpose:

- show that domestic monetary space does not erase real external limits
- connect imported essentials and FX stress to the blog's constraint language

Pseudocode:

```text
state variables:
    domestic_capacity
    imported_essential_share
    export_earnings
    import_bill
    fx_stress
    external_buffer
    inflation
    output

each period:
    domestic_demand = multiplier(private_demand + public_spending)
    import_bill = imported_essential_share * public_spending
                + import_intensity * domestic_demand

    external_gap = import_bill - export_earnings
    fx_stress = persistence * fx_stress
              + phi * max(external_gap - external_buffer, 0)

    domestic_capacity_pressure = max(domestic_demand / capacity - 1, 0)
    imported_inflation = pass_through * fx_stress
    total_inflation = domestic_capacity_pressure + imported_inflation

    if imported_essential_share high or fx_stress high:
        effective_real_capacity falls or price pressure rises

compare:
    low import dependence vs high import dependence
    same domestic slack, different external exposure

accept if:
    model can generate a case where domestic slack remains
    but external pressure becomes the binding limit
```

### `task-028`: Holder-Composition and Distribution Channel Extension

Purpose:

- show that who receives interest income changes recirculation and leakage
- keep the post from sounding like a debt stock has one universal macro effect

Pseudocode:

```text
holder buckets:
    domestic_high_mpc
    domestic_low_mpc
    foreign_holders
    central_bank_holding (optional)

parameters:
    interest_share_by_holder
    mpc_by_holder
    leakage_by_holder
    remittance_rule_for_central_bank

each period:
    interest_payment = rate * debt_stock

    allocate interest_payment across holder buckets

    recirculated_demand =
        sum(interest_income_i * mpc_i for domestic holders)

    leakage =
        foreign_interest * foreign_leakage_share

    if central_bank_holding:
        remitted_income reduces net fiscal burden or neutralizes part of flow

    output responds to recirculated_demand - leakage

compare:
    same debt stock, different holder shares
    more foreign-held vs more domestically held debt
    more central-bank-held vs market-held debt

accept if:
    model shows same nominal debt can have different macro/distribution effects
    without pretending to be a complete political-economy model
```

### `task-029`: Collateral / Repo Investigation

Purpose:

- decide whether this blog needs only a prose caveat or a genuine toy model

If a future toy model is justified:

```text
actors:
    banks
    dealers (optional)
    treasury collateral stock

state:
    collateral_value
    haircut
    funding_capacity
    credit_supply

mechanism:
    rising stress -> higher haircuts
    higher haircuts -> lower funding capacity
    lower funding capacity -> reduced credit / market-making
    reduced credit -> weaker output / more fragility

accept only if:
    this adds explanatory value beyond the existing fragility surface
```

Default expectation:

- mention in prose
- do not build immediately unless the investigation says the omission materially weakens the blog

## What We Do Not Need To Model Now

- full auction microstructure for government debt
- full yield-curve dynamics
- primary dealer balance-sheet optimization
- QE/QT portfolio-channel detail
- derivatives and hedging chains
- a complete open-economy balance-of-payments model
- full political bargaining over fiscal rules

Those are all real. They are just beyond the explanatory minimum needed for this post's main claim.

## Recommendation

The blog should become more explicit about securities, rollover, external constraint, and omitted collateral/liquidity layers.

It should **not** try to become a full textbook on sovereign debt markets.

The most defensible refinement is:

- prose first for functional clarification
- simple models only where they materially change the reader's understanding of the constraint story
- explicit limitation language where additional realism would otherwise become endless
