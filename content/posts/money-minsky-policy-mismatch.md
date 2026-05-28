---
title: "Anything We Can Actually Do, We Can Afford"
date: 2026-04-01
draft: true
description: "A functional, systems view of why austerity mistakes money's role for households, currency users, and sovereign issuers."
tags: ["complex-systems", "economics", "monetary-theory", "policy", "mmt", "minsky"]
author: "Miadad Rashid"
showToc: true
TocOpen: true
---

> “Anything we can actually do we can afford.”

That line is commonly attributed to Keynes’s 1942 broadcast on finance. I am not using it as a slogan or a permission slip. I am using it as a diagnostic rule. Before asking where the money will come from, ask what a society can actually mobilize, what kind of entity is making the payment, and what constraint is really binding.

A household uses money. A business uses money. A city uses money. A euro-area government uses money under constraints it does not fully control. A sovereign currency issuer occupies a different position inside the monetary system. If we assign the same functional role to money in all of those cases, we will misread what can go wrong and what policy is for.

That is why the household-budget analogy is not just incomplete. In many policy arguments, it is a category mistake. It imports the constraint set of one kind of entity into another. In practice, that mistake often shows up as austerity politics: public authorities acting as though their primary responsibility were to mimic a family checkbook rather than to stabilize incomes, coordinate capacity, and respect the real limits of the system they govern.

In the related essay [Toward a Science of Politics](/posts/societies-as-complex-systems/), I argued that human institutions should be treated as **open systems**: systems that persist by managing flows, constraints, and feedback rather than by sitting in static equilibrium. The same framing helps here. A modern economy is not a wallet. It is a connected system of payments, debts, incomes, taxes, production, imports, and institutional rules.

That matters because policy depends on what kind of system you think you are steering. If you model a government as if it were a family checking account, you will watch the wrong signals and optimize the wrong target. You will treat budget arithmetic as the fundamental constraint even when the binding limit is elsewhere.

> Policy built on the household-budget analogy mis-specifies the relevant constraints of sovereign or quasi-sovereign macro systems.

That is a narrower claim than "deficits never matter," and it is much stronger. I am **not** claiming that governments can spend without limit. I **am** claiming that the real constraints are inflation, real capacity, external dependence, legal architecture, and private-sector fragility — not a universal rule that "government must budget like a household."

The simulations in this post are there to make that functional mistake visible, not to pretend that one essay settles macroeconomics. They let us ask, in explicit form, what changes when we assign money a different role for different entities and what follows when policy targets the wrong variable.

The support structure is layered:

- institutional and operational facts about what different entities are inside a monetary system
- a comparative-constraints model for household, currency-user, and issuer positions under the same shock
- a rollover and holder-composition layer showing why debt maturity and liability ownership change how fiscal pressure propagates
- a simple sectoral-flow model and a public-data-backed austerity counterfactual
- an agent-based policy lab comparing deficit-targeting and state-targeting controllers
- fragility, external-constraint, and capacity-boundary models that show why both financial structure and real limits matter

Each major claim stays attached to an explicit mechanism through code, data, and historical episodes.

All figures in this post are generated from the repo with:

```bash
uv run python -m experiments.money_minsky_policy_mismatch.run_experiment --experiment all --refresh-data
```

## What It Means To “Afford” Something

A household usually asks “Can we afford it?” and means: do we have enough money in our account, or enough reliable income, to make the payment?

At the macro level, that question splits in two:

- **financial affordability**: can the payments be made in the accounting unit?
- **real affordability**: does the economy have the actual capacity to produce and deliver what is being asked for?

For a sovereign issuer, those are not the same question. A state can authorize payment in its own currency and still run into a real constraint if:

- there are not enough trained workers
- energy is scarce
- key imports are unavailable
- factories, ports, or logistics are overloaded
- the economy is already operating close to full capacity

So when Keynes says “Anything we can actually do we can afford,” the phrase **actually do** carries the weight. If the economy can mobilize the real resources, finance should not be treated as the main barrier. If the resources are not there, financial permission alone does not solve the problem.

## 1. Economies Are Open Flow Systems

The simplest useful mental picture is not a household. It is a set of **connected reservoirs and flows**.

Imagine three connected reservoirs:

- the domestic private sector
- the government
- the foreign sector

Money flows between them through wages, taxes, spending, imports, exports, interest payments, and credit creation. If one reservoir tries to accumulate a surplus, at least one other reservoir must absorb the corresponding deficit. In systems language, this is a conservation relationship inside an open system.

That is why the complex-systems framing matters here. In the politics paper, I argued that open systems maintain **dynamic stability** by regulating flows and feedback. A macroeconomy works the same way. It does not become stable because everyone "acts responsibly" in isolation. It becomes stable or unstable depending on how the connected flows interact.

### What money is doing in this system

The reservoir picture shows flows between sectors. But what fills the reservoirs in the first place? The household analogy assumes money is a fixed stock that must be collected before it can be spent. In the actual plumbing, the answer is different: modern monetary systems work more like a layered ledger.

- A **unit of account** is the measuring unit in which prices, taxes, contracts, and debts are recorded.
- Commercial banks create deposits when they extend loans. This is often called **endogenous money**, which here simply means that money creation expands inside the system when credit expands.
- Governments that issue their own currency sit in a different institutional position from households or firms, because they operate within the legal and settlement architecture of that unit of account.

The practical implication is simple:

> not every entity inside a monetary system faces the same kind of budget constraint.

### Why the household analogy feels right but misleads

A household is a currency user. It must earn, borrow, or receive money before it can spend it. That model is correct for:

- a family
- a business
- a city
- a U.S. state

It is not automatically correct for:

- a sovereign government that issues its own currency
- a quasi-sovereign government such as a euro-area member, which uses a currency it does not fully issue or control

So the question is not "Does budgeting matter?" It is "What kind of entity are we talking about, and what constraints actually bind it?" Keynes’s line is useful here because it forces the constraint question in the right order: what can this system actually mobilize, and only then how should the accounting be organized?

## 2. Different Entities, Different Monetary Roles

The useful distinction here is functional, not moral. The question is not which actor is virtuous. The question is what monetary position the actor occupies and what that position allows or forbids. This part of the argument is mostly institutional: it is about settlement position, legal architecture, and funding exposure before it is about simulation.

- A **currency user** must obtain the currency first.
- A **currency issuer** spends in the currency it issues.
- A **quasi-sovereign** sits in between politically, but not monetarily: it has state functions, yet still faces externally imposed or market-imposed funding pressure in the relevant currency.

This is where many policy arguments go wrong. They import a currency-user model into cases where the institutional architecture is different.

Each type of entity faces a different **constraint set** — the list of limits that actually bind it. For a household, income and credit access bind directly. For a sovereign issuer, the relevant questions are different:

- Is there inflationary pressure?
- Is there unused labor, machinery, energy, or logistics capacity?
- Is the country highly dependent on imported essentials?
- Are there self-imposed legal barriers, such as debt ceilings or fiscal rules?
- Is the private sector already fragile under debt?

These are all questions about **real affordability**: whether the economy has the capacity, stability, and room to act — not whether the government has "enough money" in some household sense.

For a quasi-sovereign, there is an additional real constraint:

- Can the government refinance maturing debt without markets demanding a much higher borrowing premium, often called a **spread**?
- How much of its debt must be rolled soon rather than later, and on what terms?

This is why "government should budget like a household" is not a neutral simplification. It collapses distinct system positions into one false type.

This is also where the Keynes frame becomes operational. For a sovereign issuer, “Can we afford it?” usually means “Do we have the real resources, and can we mobilize them without generating unacceptable inflation or external stress?” It does not mean “Does the government resemble a family that might literally run out of its own unit of account?”

### Bonds are not one thing

A public security is not just “borrowing” in one universal household sense. For a household, a debt instrument is usually a financing obligation. For a sovereign issuer, a government bond can also function as an interest-bearing state liability, a savings vehicle for the private sector, and a piece of monetary plumbing used in reserve, collateral, and rate management. For a currency user or quasi-sovereign, the same security carries more refinancing risk because market access and rollover conditions can become binding in a way they do not for an issuer of the unit of account.

That does not mean bonds are irrelevant for sovereign issuers. It means their role has to be described functionally. The same instrument can be a safe asset for one balance sheet and a refinancing problem for another.

The distinction is easier to keep straight visually:

![Different entities sit in different monetary positions, so the right diagnostic variable changes with the entity.](/images/money_minsky_policy_mismatch/constraint_hierarchy.png)

That figure is deliberately simple. Before asking whether a policy sounds prudent, ask what kind of monetary position the entity actually occupies.

The repo now also includes a stylized comparative model, `comparative_constraints.py`, that lets the same private-demand shock hit three different monetary positions. The point of that model is not to estimate any one country. The point is to isolate financing architecture.

![A stylized comparison of household, currency-user, and sovereign-issuer responses to the same demand shock.](/images/money_minsky_policy_mismatch/comparative_constraints.png)

Under that setup, the household eventually hits a borrowing ceiling, the currency user faces rising financing pressure and consolidation, and the sovereign issuer maintains nominal spending because its problem is not prior funding in the same sense. That does **not** mean the issuer has no limit. It means this particular model is isolating funding position; the real-capacity and inflation boundary comes later.

`sovereign_securities.py` adds one more layer to that comparison. It keeps the focus on financing architecture, but distinguishes debt stock from refinancing flow by varying maturity structure and rollover pressure. Under the same headline debt ratio, a short-maturity currency user hits spread pressure and forced consolidation sooner than a long-maturity user, while the issuer path is much less sensitive to rollover need. That is still a toy model, not a bond-market microstructure model. Its job is narrower: to show that "the debt ratio" and "the amount that must be refinanced soon" are not the same state variable.

![The same debt stock can behave differently when maturity structure and rollover pressure differ across issuer and user regimes.](/images/money_minsky_policy_mismatch/rollover_comparison.png)

## 3. Two Models of the Same Economy

Section 2 established that different entities occupy different monetary positions. The practical problem is that public discourse routinely ignores this distinction. Campaign rhetoric and monetary institutions often talk about the same economy with different models in mind.

The campaign model usually defaults to the household script: government must "find the money" first, deficits are the main sign of irresponsibility, and cuts are presented as maturity by default. Operational institutions do not work from that picture. Central banks, treasuries, and bank supervisors already manage a balance-sheet system in which banks create deposits, reserves are supplied and drained operationally, and crisis policy works by stabilizing funding, settlement, and income flows.

![A schematic comparison of the household-budget story used in campaign rhetoric and the balance-sheet model used in operational institutions.](/images/money_minsky_policy_mismatch/campaign_vs_operational_models.png)

The split is visible in history. During the financial crisis and again during the pandemic shock, policy institutions did not wait for some prior stock of taxpayer money to appear before acting. They backstopped markets, expanded central-bank balance sheets, and coordinated with fiscal authorities because that is how the monetary plumbing actually works. Once the emergency passed, public discourse often snapped back to the language of belts, wallets, and "maxed-out national credit cards."

That operational view also changes how securities are understood. In practice, treasuries and central banks care about reserves, settlement, collateral quality, maturity structure, and liquidity conditions, not just the headline debt stock. A government bond can be part of savings infrastructure, collateral chains, and rate management at the same time that it appears in political rhetoric as if it were only a family loan.

That mismatch matters for austerity politics. The campaign model makes cuts sound like common sense. The operational model asks a different question: what happens to output, income, refinancing conditions, and financial stability if we cut into weakness? Once the entity type is misread, the function of government is misread with it.

## 4. Sectoral Balances: The Reservoir Accounting

Now we can make the reservoir analogy from section 1 precise and quantitative. The sectoral balance framework is the accounting that the campaign model leaves out.

In an open economy, the three-sector accounting identity is:

> private balance + government balance + foreign balance = 0

In plain language: if one part of the system is trying to spend less than it earns, at least one other part must be spending more than it earns. All three sectors cannot run a surplus at the same time.

The decisive code in the repo's `policy_sectoral_model.py` is just this:

```python
private_balance = output - taxes - consumption - investment
government_balance = taxes - government_spending
foreign_balance = imports - exports
```

If you have taken any macroeconomics course, these variables should look familiar. Sum the three balances and set them to zero and you recover the GDP expenditure identity: `Y = C + I + G + (X − M)`. The sectoral framework is that same identity rearranged so each sector's net position is visible. Whatever is left over in one sector must have been absorbed by the others — the conservation law of the reservoir picture, now in code.

![Three-sector identity in the deterministic sectoral model. The residual stays at machine precision because the balances are computed from the same accounting system.](/images/money_minsky_policy_mismatch/policy_sectoral_balances.png)

The sectoral identity is the first correction that the household-budget model fails to impose. A household that cuts spending reduces its own outflows without reducing its income. A government that cuts spending reduces someone else's income. The identity makes that feedback visible.

The bookkeeping point and the policy point are not the same. The identity is always true. The real question is what happens when one sector tries to improve its own balance by cutting into a system that is already losing demand.

The sectoral model compares three policy responses to the same private-demand shortfall:

- `supportive`: support demand during the slump
- `austerity`: cut government spending immediately
- `delayed_repair`: support first, repair later

![The same private-demand shock produces very different output and tax paths depending on whether policy supports demand, cuts immediately, or delays repair.](/images/money_minsky_policy_mismatch/policy_sectoral_paths.png)

Under the current calibration, immediate austerity lowers average post-shock output by about **13%** relative to the supportive path. Tax revenue falls by about the same amount because the model taxes output proportionally. The private balance is also squeezed. The model's implicit multiplier under these parameters is consistent with the empirical range: Blanchard and Leigh (2013) found that actual fiscal multipliers during the post-2010 consolidation period were 0.9 to 1.7, well above the 0.5 that forecasters assumed at the time. The sectoral model is not calibrated to match any specific country, but its demand response falls within that empirically supported range.

The intuitive meaning is straightforward:

> if households and firms are already pulling back, and imports are draining income outward, then government cuts remove income from the system at exactly the moment the private sector is trying to repair its balance sheet.

This connects directly to the broader systems argument in the politics paper. One subsystem can preserve the appearance of stability by exporting stress into another subsystem. In this case, a public effort to improve the budget can shift strain into household income, firm cash flow, and unemployment.

That is what I mean by an **external leakage** here: some of the flow leaves the domestic economy through imports or foreign claims instead of recirculating internally.

### How to recognize this in real life

If you hear all of the following at once:

- households are trying to save more
- firms are cutting investment
- the country imports more than it exports
- government is trying to reduce its deficit quickly

then the question should be:

> which sector is supposed to absorb the missing income?

That is the diagnostic use of the sectoral framework. It tells you when a policy is asking the system to do something arithmetically and behaviorally difficult at the same time.

In Keynes’s terms, this is a case where the economy can clearly do more than the policy is allowing it to do. Idle labor, unused capacity, and weak private demand are signals that the binding constraint is not a missing pile of money.

## 5. Austerity Is a Control Problem, Not Just a Moral Argument

The next intuition comes from control systems.

In any controlled physical system, failure often happens because the controller is targeting the wrong signal. If you optimize the gauge instead of the state that the gauge is supposed to represent, you can make the system less stable while appearing disciplined.

That is often what happens with deficit targeting. The budget number is treated as the key measure of affordability even when the real question is whether the economy is operating below capacity. Austerity — deliberate fiscal consolidation through spending cuts, tax increases, or both — becomes the default prescription. The evidence in this section is model-based in two different ways: a reduced-form counterfactual tied to public data, and a stylized agent-based policy lab that compares competing fiscal controllers.

The public-data-backed counterfactual in `austerity_counterfactual.py` models what happens next in a reduced-form update:

```python
growth = (
    trend_growth
    - multiplier * (action / 100.0)
    - hysteresis * max((trend - gdp) / trend, 0.0)
)
primary_deficit = (
    structural_primary_deficit
    + stabilizer_slope * max(-output_gap, 0.0)
    - consolidation_passthrough * (action / 100.0)
)
debt_ratio = (debt_ratio * (1.0 + effective_rate)) / (1.0 + growth) + primary_deficit
```

In words:

- `action` is the size of the fiscal tightening, measured in percent of GDP; dividing by 100 converts it to a ratio
- `multiplier` says how strongly output responds to that tightening — the model switches between a high-slack multiplier (1.4) when the economy is weak and a low-slack multiplier (0.6) when it is closer to trend
- `hysteresis` captures lingering damage when the economy operates below trend: lost skills, canceled investment, or long-term business failures that do not reverse when the downturn ends
- `stabilizer_slope` controls how much the deficit widens automatically when output falls below trend, representing automatic stabilizers such as lower tax receipts and higher transfer payments
- `consolidation_passthrough` is the fraction of the intended fiscal tightening that actually reaches the primary deficit after bureaucratic and timing lags
- `effective_rate` matters because debt service changes with financial conditions — especially for quasi-sovereigns, where markets can demand a larger spread as debt rises
- `debt_ratio` is government debt divided by GDP — the denominator matters because a shrinking economy can worsen the ratio even as debt itself grows slowly

The model is doing one specific thing: asking how the same observed consolidation path looks once we allow system state to matter.

The two cases in the repo are intentionally different:

- **Spain** is used as a quasi-sovereign euro-area case where borrowing conditions can worsen as markets demand a larger spread
- **United Kingdom** is used as a sovereign-issuer contrast case

![Observed IMF austerity paths versus a delayed-consolidation counterfactual for Spain and the United Kingdom.](/images/money_minsky_policy_mismatch/imf_counterfactual_cases.png)

The debt-ratio panels also show actual observed debt ratios from World Bank data as individual data points. This overlay lets the reader judge how far the model trajectories diverge from reality. The model is not claiming to reproduce the exact historical path; the data points are there so the reader can see where the model sits relative to what actually happened.

Under the default calibration:

- Spain ends about **10.5 GDP-index points higher**, about **21.2 debt-ratio points lower**, and about **3.9 unemployment points lower** under delayed consolidation than under the observed path.
- The United Kingdom ends about **4.45 GDP-index points higher**, about **9.86 debt-ratio points lower**, and about **1.51 unemployment points lower** under delayed consolidation.

These are model outputs under the default calibration, not historical measurements. The model uses real IMF consolidation timing and real World Bank initial conditions, but the counterfactual path is simulated. What matters is the mechanism:

- cuts can shrink GDP
- shrinking GDP can shrink tax revenue
- shrinking GDP can worsen the debt ratio because GDP is the denominator
- automatic stabilizers can undo part of the planned improvement

That is the control-system failure. A household that cuts spending usually improves its budget directly. A government cutting into recession can shrink the very income base that supports its budget.

In complex-systems language, this is a feedback mistake. The controller is trying to stabilize one visible variable while ignoring the coupled variables that feed back into it.

The control logic is easier to see schematically:

![A schematic control diagram showing how direct deficit targeting can feed back through output and the tax base, while state-target stabilization works through recovery first.](/images/money_minsky_policy_mismatch/wrong_target_control.png)

The ABM policy lab in `policy_controllers.py` makes the same control problem visible from another angle. It compares three stylized controllers: passive policy, an austerity controller that reacts to the deficit ratio, and a functional-finance controller that reacts to underutilization. Under the default configuration, the austerity controller does what it is designed to do on its own terms: it lowers the deficit faster. But it does so with weaker output and higher underutilization than the state-targeting controller.

![A stylized agent-based comparison of passive, austerity, and functional-finance fiscal controllers.](/images/money_minsky_policy_mismatch/policy_lab.png)

That is the point of the ABM result. The disagreement is not about whether budgets exist. It is about what the controller is trying to stabilize first. The ABM is still stylized and seed-based, so it should be read as a mechanism illustration, not as a historical estimate.

Even so, the control mistake is wider than any single model shown here. Debt maturity, rollover concentration, holder composition, collateral conditions, and external dependence all mediate how budget tightening propagates, especially for currency users and quasi-sovereigns.

`holder_composition.py` makes one part of that more concrete. It keeps the nominal debt stock fixed and varies who receives the interest income. When more of the liabilities are held by high-MPC domestic households, interest payments recirculate into demand more strongly. When the same liabilities are held by foreign investors, more of the flow leaks out of the domestic economy. When the central bank holds more of the debt, remittances reduce the net fiscal cost. The point is not that public debt is always good or bad. The point is that the same debt stock does not carry one universal macro meaning.

![The same nominal debt stock produces different recirculation, leakage, and wealth-concentration paths depending on who holds the liabilities.](/images/money_minsky_policy_mismatch/holder_composition.png)

In Keynes’s language, it is a mistake about what the society can afford. If the labor, machines, and productive slack are there, the real problem is to mobilize them without creating other bottlenecks. Austerity instead treats the budget itself as the bottleneck and confuses a public coordinating problem with a household budgeting problem.

### When the claim weakens

The post should not imply that austerity always fails. The repo includes a lower-multiplier, weaker-stabilizer boundary case on purpose. In that case, delayed consolidation still raises GDP, but it no longer improves the debt ratio.

That is important. It means the correct claim is conditional:

> austerity is a bad control rule when policymakers import household-budget logic into a weak, fragile, or architecture-constrained macro system.

Know which system you are in.

### How to recognize this in real life

If you see spending cuts proposed while the economy is already weak, ask:

- Will the cuts reduce income and tax receipts?
- Is the debt ratio likely to improve because debt falls, or worsen because GDP falls faster?
- Is this a sovereign issuer, a currency user, or a quasi-sovereign?

The diagnostic question is:

> is the policy targeting the budget indicator or the underlying state of the economy?

That is the control-system test from this section.

## 6. Fragility: The Same Force Hits a Loaded System Differently

The austerity analysis in section 5 treated the private sector as a background. But the private sector has its own debt structure, and that structure determines how much punishment the system can absorb. The final experiment asks: what happens when a rate shock hits a financial system that is already carrying heavy debt?

A lightly loaded beam and a heavily loaded beam do not respond the same way to an added force. The extra force can be identical; the outcome depends on how much stress is already inside the structure. The same logic applies to **fragility** in a financial system: when leverage (debt relative to income) is already high and cash flows are already committed, even a moderate rate shock — an increase in borrowing costs — can push the system into breakdown.

The fragility experiment calls the Keen-Minsky ODE solver defined in `keen_ode.py`. The core mechanism inside that solver is:

```python
profit = max(1.0 - omega_c - p["r"] * d_c, 0.0)
I_over_Y = invest(profit, d_c, p["k0"], p["k1"], p["k2"])
dd = (I_over_Y - profit) - d_c * gY
```

In words: profits are squeezed by debt service, investment depends on profitability and debt drag, and the debt ratio rises when investment and financing pressure outpace internal cash generation.

The experiment in `fragility_regimes.py` sweeps over a grid of rate shocks and initial debt levels, calling this solver at each point and recording whether the debt ratio crosses a crisis threshold. It then compares a more fragile and a more resilient calibration across that grid.

![The same rate hike produces very different crisis timing under fragile and resilient leverage dynamics.](/images/money_minsky_policy_mismatch/fragility_regimes.png)

The result is not that every rate hike causes crisis. The result is that the same tightening can land very differently depending on the economy's sensitivity to leverage.

The fragile and resilient calibrations differ in two parameters. The interest rate `r` shifts from 4% to 3%, but the more consequential change is `k2`, the debt-drag coefficient on investment, which rises from 0.04 to 0.20. A higher `k2` means firms reduce investment more aggressively when their leverage rises. In the resilient calibration, the economy self-corrects faster because highly indebted firms pull back on borrowing before debt spirals. In the fragile calibration, firms keep investing even as leverage climbs, which makes the eventual break sharper. The comparison is therefore not purely "same economy, different debt" but "different sensitivities to leverage, facing the same shock." That distinction matters for interpretation.

- In the current fragile grid, only about **11.1%** of the cells avoid crisis within the horizon.
- In the more resilient grid, about **61.1%** of the cells avoid crisis.

This matters because public debate often treats tightening as if it were applied to a neutral background. It is not. It is applied to a balance-sheet structure that may already be heavily loaded.

Once fragility is high, the system can become deviation-amplifying rather than self-correcting. That is the economic version of the positive-feedback problem described in the complex-systems paper.

This also affects what a society can meaningfully afford. A country may have idle workers and unfinished useful projects, but if the private financial structure is brittle, bad policy can block mobilization by collapsing cash flow and credit conditions. In that sense, fragility helps determine what the economy can *actually do*. A fragile system may fail to mobilize resources that nominally exist because the financial structure breaks down before that real capacity can be reached.

(The Keen ODE uses simplified debt accumulation without explicit bank credit creation. A fuller model would incorporate the endogenous money mechanism described in section 1, where bank lending expands the money supply and contraction can destroy it. The ABM model in the repo does this, but the reduced-form models featured here are easier to inspect and explain.)

### How to recognize this in real life

If rates are rising while you also see:

- high household debt
- weak business cash flow
- falling asset prices
- refinancing pressure in funding markets

then the question is not just "Did rates go up?" The question is:

> how loaded was the structure before the extra stress was applied?

That is the practical meaning of fragility.

## 7. What the Experiments Do and Do Not Establish

By this point the post is using several different support types, not one uniform kind of evidence. Before drawing conclusions, it is worth saying what job each one is doing.

- The entity distinction in sections 1 through 3 is primarily **institutional and operational**. It rests on what different entities are inside the monetary system.
- `comparative_constraints.py` is a **stylized comparative model**. It isolates how funding position changes adjustment under the same shock.
- `sovereign_securities.py` is a **stylized refinancing model**. It separates debt stock from maturity structure and rollover pressure.
- `policy_sectoral_model.py` is **accounting plus deterministic dynamics**. It makes the cross-sector feedback visible.
- `austerity_counterfactual.py` is a **public-data-backed reduced-form model**. It shows how consolidation timing can interact with GDP, debt ratios, and unemployment.
- `policy_controllers.py` is an **agent-based mechanism model**. It compares fiscal controllers that target different variables.
- `holder_composition.py` is a **stylized recirculation and distribution model**. It shows that who receives interest income changes leakage, remittance, and concentration outcomes even when nominal debt is unchanged.
- `external_constraint.py` is a **stylized external-boundary model**. It shows how imported-essential dependence and FX stress can bind before domestic bookkeeping does.
- `fragility_regimes.py` and `capacity_constraint.py` are **boundary models**. One is about financial loading; the other is about real capacity and price pressure.

Read together, these surfaces tell one connected story. The institutional distinction says unlike entities should not be assigned one household constraint set. The comparative and rollover models show that the same shock or the same debt stock can produce different adjustment paths when funding architecture differs. The sectoral identity establishes what is arithmetically possible: not every sector can improve its balance at the same time. The austerity counterfactual and policy-lab model show what can happen when policy nevertheless targets the budget first. The holder-composition model shows why liability ownership changes recirculation and leakage. The external and capacity models show why the true limits are real and state-dependent, not reducible to bookkeeping. The combination does not settle every macroeconomic dispute, but it does show that getting the system model wrong is not a harmless simplification.

They do **not** prove every proposition associated with MMT or Minsky.
They do **not** replace empirical macroeconomics.
They do **not** show that all fiscal tightening is always self-defeating.
They also do **not** provide a full macro model of inflation, trade, or distributional conflict. The new capacity-boundary model adds a deliberately minimal price-pressure mechanism, which is enough to show the direction of the real limit: under slack, extra spending raises output; near capacity, more of the effect turns into inflation. But that is still a boundary illustration, not a country-calibrated inflation model.

The refinement layer now adds minimal surfaces for maturity/rollover dynamics, holder composition, and external dependence. Those are useful because they show that the same nominal debt stock can carry different refinancing, leakage, and distribution consequences depending on structure and context. But they still do **not** model collateral and repo chains, detailed treasury-central-bank operating interactions, full trade dynamics, or a complete political economy of distribution.

External constraint deserves separate emphasis. `external_constraint.py` shows the mechanism in stripped-down form: under low import dependence, domestic monetary space works much as the post's core thesis suggests; under high import dependence, the economy can still have domestic slack while FX stress and imported inflation start to bind. That does not restore the household analogy. It identifies a different real limit.

![A stylized external-constraint model showing that high import dependence can turn slack into FX stress and imported inflation.](/images/money_minsky_policy_mismatch/external_constraint.png)

![A minimal capacity-boundary model showing slack output gains versus tight-capacity inflation pressure.](/images/money_minsky_policy_mismatch/capacity_constraint.png)

So the claim of this post remains limited and important at the same time. The household-budget frame misidentifies the constraint. That does not imply there is no constraint. It implies that the relevant limit shifts with entity type, institutional architecture, private fragility, and real capacity.

What they do show is enough for the main claim:

> once policymakers use the wrong system model, repeated policy mistakes become more likely because the wrong variables are treated as the important ones.

## 8. How to Spot Policy Mismatch Around You

Not every bad policy argument is cynical. Some are inherited habits, some are genuine confusion, and some are rhetoric designed to make one choice look inevitable. The useful thing is not to guess motives first. It is to check whether the argument assigns money and constraint to the right kind of entity.

When you hear a policy argument about budgets, debt, inflation, or tightening, ask these questions in order:

1. Is the claimed problem financial, or is it actually a real-resource problem?
   Are we missing money, or are we missing workers, materials, energy, housing, transport, institutional capacity, or time?
2. What kind of entity is this?
   Household, city, firm, euro-area member, or sovereign currency issuer.
3. What constraint is actually binding?
   Income, funding access, inflation, imported essentials, legal rules, private leverage, or rollover pressure.
4. Is the policy targeting a real state or a budget indicator?
   Output, employment, inflation, and financial stress are states of the system. The deficit is often an indicator, meaning a number that describes part of the system without by itself telling you whether the system is healthy.
5. If spending is cut here, whose income falls?
   Households, firms, local governments, or importers.
6. Is the policy ignoring a connected part of the system?
   Private debt, banking dynamics, trade leakage, rollover concentration, collateral/liquidity pressure, or pressure from higher borrowing spreads.
7. What kind of liability is being discussed?
   A household debt, a refinancing obligation, a safe asset, a collateral instrument, or some mixture of those.
8. Who holds it, and in what currency do the crucial payments have to be made?
   Domestic households, banks, pensions, foreign holders, the central bank, and whether critical imports or debts are priced in another unit.

Here are six fast examples.

**A household**
The household model applies. Income and credit access are direct constraints.
Misapplication: none. This is the case the analogy actually describes.

**A city or U.S. state**
This is still a currency user case.
Misapplication: treating it as if it could always finance deficits internally like a sovereign issuer.
What to watch instead: revenue, transfers, refinancing conditions, legal borrowing limits.

**A hospital wait-list crisis**
This may be described as a “funding problem,” but often the binding constraint is staffing, facilities, training pipelines, or organizational throughput.
Misapplication: treating the budget line alone as the bottleneck.
What to watch instead: nurses, doctors, rooms, equipment, scheduling, and local capacity to expand service.

**A housing shortage**
This is often presented as “we cannot afford to build enough,” but the binding constraints may be land use, materials, skilled labor, financing structure, and permitting time.
Misapplication: reducing the issue to public-budget arithmetic.
What to watch instead: build capacity, zoning, materials, labor, infrastructure, and credit conditions.

**A euro-area government**
This is a quasi-sovereign case.
Misapplication: assuming it has the same monetary freedom as a government that issues its own floating currency.
What to watch instead: borrowing spreads, creditor structure, ECB backstop conditions, recession feedbacks on GDP and debt ratio.

**A sovereign-issuer government in recession**
This is where the household analogy is often most misleading.
Misapplication: assuming immediate fiscal tightening will improve the budget mechanically.
What to watch instead: slack, inflation, private saving behavior, imports, private leverage, and whether GDP will fall faster than the deficit.

## 9. Conclusion

The household-budget analogy survives because it feels concrete. But familiar is not the same thing as correct. A household, a city, a euro-area government, and a sovereign currency issuer do not occupy the same place in the monetary system, so they do not share the same constraint set.

That is why I connected this post to the broader argument in [Toward a Science of Politics](/posts/societies-as-complex-systems/). Social systems are still physical systems in the relevant sense: they are made of flows, capacities, constraints, and feedbacks. If you use the wrong model of those flows and constraints, you should expect repeated policy mismatch.

The Keynes line is useful precisely because it forces the question into the right order:

> Anything we can actually do we can afford.

The right follow-up question is therefore: what does “actually do” mean here, and for whom? If the labor, materials, energy, and institutional capacity are present, then finance should be organized to mobilize them. If those real resources are absent, then the constraint is physical and organizational, not merely budgetary.

That does not make government omnipotent. It makes government functional. In a society that promises public health, infrastructure, basic security, and some degree of macroeconomic stability, the state's role is not to imitate a household budget. Its function is to help coordinate monetary, legal, and institutional arrangements so collective capacity can be used without colliding with inflationary, external, or financial limits.

The practical residue is modest but useful:

- the ability to tell a currency issuer from a currency user
- the habit of asking first whether a problem is financial or really about resources and capacity
- the habit of asking whether a policy is targeting an indicator or a real system state
- the intuition that cuts can shrink the income base they are supposed to "fix"
- the recognition that tightening depends on how loaded the financial structure already is

That is enough, I think, to evaluate many policy arguments more clearly, especially when they present austerity as inevitability rather than as one model-dependent choice among others. Whether the mismatch comes from habit, confusion, or more strategic rhetoric, the practical result is the same: people are taught to look for the wrong constraint and to misunderstand what public institutions are there to do.

## Reproducibility Notes

The rebuilt package for this post lives in:

- `experiments/money_minsky_policy_mismatch/comparative_constraints.py`
- `experiments/money_minsky_policy_mismatch/policy_sectoral_model.py`
- `experiments/money_minsky_policy_mismatch/austerity_counterfactual.py`
- `experiments/money_minsky_policy_mismatch/policy_controllers.py`
- `experiments/money_minsky_policy_mismatch/fragility_regimes.py`
- `experiments/money_minsky_policy_mismatch/capacity_constraint.py`
- `experiments/money_minsky_policy_mismatch/research_data.py`
- `experiments/money_minsky_policy_mismatch/plotting.py`
- `experiments/money_minsky_policy_mismatch/run_experiment.py`

Run the full figure bundle with:

```bash
uv run python -m experiments.money_minsky_policy_mismatch.run_experiment --experiment all
```

Run the test suite with:

```bash
uv run python -m pytest experiments/money_minsky_policy_mismatch/tests/ -v
```

Public data is downloaded by code and cached locally in an ignored directory:

- `results/money_minsky_policy_mismatch_data/`

Future refinements should extend these models rather than treat the prose as separate from the implementation.

## References

- IMF action-based dataset: [A New Action-based Dataset of Fiscal Consolidation in Latin America and the Caribbean and updated OECD tables](https://www.imf.org/-/media/files/publications/wp/2024/datasets/wp24210.zip)
- Olivier Blanchard and Daniel Leigh, [Growth Forecast Errors and Fiscal Multipliers](https://www.imf.org/external/pubs/ft/wp/2013/wp1301.pdf)
- Christopher House, Christian Proebsting, and Linda Tesar, [Austerity in the Aftermath of the Great Recession](https://sites.lsa.umich.edu/ltesar/wp-content/uploads/sites/697/2022/05/JME2020-1.pdf)
- Antonio Fatas and Lawrence Summers, [The Permanent Effects of Fiscal Consolidations](https://faculty.insead.edu/fatas/documents/Fatas_Summers_2017.pdf)
- Bank of England, [Money creation in the modern economy](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy)
- George Aspromourgos, [Keynes, the Environmental Crisis, and the Economic Capabilities of the State](https://hetsa.au/images/news/2023-hetsa-conf/2024_conference_papers/Aspromourgos_ESHET_Keynes_Environmental_Crisis.pdf), which cites Keynes’s 1942 broadcast wording: “Anything we can actually do we can afford.”
- World Bank API indicator documentation: [SL.UEM.TOTL.ZS](https://api.worldbank.org/v2/indicator/SL.UEM.TOTL.ZS?format=json) and [GC.DOD.TOTL.GD.ZS](https://api.worldbank.org/v2/indicator/GC.DOD.TOTL.GD.ZS?format=json)
