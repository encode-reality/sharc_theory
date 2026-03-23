---
title: "Bell's Theorem as a Type-Level Constraint"
date: 2026-03-22T12:00:00-05:00
draft: true
description: "Bell's inequality is not a statement about physics equations. It is a structural constraint on the space of programs that obey a particular dependency structure. Quantum mechanics violates it because it does not inhabit the same type."
tags: ["quantum-mechanics", "bell-theorem", "type-theory", "free-theorems", "CHSH", "computational-physics"]
author: "Miadad Rashid"
showToc: true
TocOpen: true
math: true
---

# Bell's Theorem as a Type-Level Constraint

Bell's theorem is usually presented as a result in physics — something about electrons, photons, and the strangeness of quantum mechanics.

It is not.

Bell's theorem is a structural result about programs. It states that any program with a certain dependency structure must satisfy a particular output constraint. No implementation can escape it. The result follows from the type signature alone, without inspecting any implementation detail.

Quantum mechanics violates this constraint. Not by being cleverer within the same structure, but by operating in a different computational space entirely. The violation is not a loophole. It is evidence that quantum correlations cannot be embedded into the type that produces classical correlations.

This essay develops that claim formally, demonstrates it computationally, and explains precisely where the embedding fails.

---

## The Type Signature of a Local Hidden-Variable Theory

A local hidden-variable (LHV) model has the following structure:

- A shared hidden state $\lambda$, drawn from some probability distribution $\mu(\lambda)$
- Alice's response function $A(a, \lambda) \in \{+1, -1\}$, depending on her measurement setting $a$ and the shared state
- Bob's response function $B(b, \lambda) \in \{+1, -1\}$, depending on his measurement setting $b$ and the shared state

The critical constraint is **locality**: Alice's output does not depend on Bob's setting, and Bob's output does not depend on Alice's setting.

In type notation:

$$
\lambda : \Lambda, \quad A : (\text{Setting} \times \Lambda) \to \{+1, -1\}, \quad B : (\text{Setting} \times \Lambda) \to \{+1, -1\}
$$

with the dependency constraint:

$$
A(a, \lambda) \text{ is independent of } b, \qquad B(b, \lambda) \text{ is independent of } a
$$

This defines a class of programs. The hidden state can be anything — a bit string, a real number, a probability distribution, a lookup table. The response functions can be arbitrary. The only constraint is the dependency structure.

Joint probabilities in this model factorize:

$$
P(A, B \mid a, b) = \int_\Lambda P(A \mid a, \lambda) \, P(B \mid b, \lambda) \, d\mu(\lambda)
$$

All correlations between Alice and Bob come from the shared $\lambda$. There is no other channel.

---

## Building Intuition: Photons and Polarizers

Before diving into the formal proof, it helps to see what this type constraint means physically. We will use photon polarization throughout this section — it provides the cleanest intuition. The formal sections that follow use spin-1/2 notation, but the structural argument is the same.

### The three-polarizer surprise

Start with a simple bench-top experiment that has nothing to do with entanglement — just single photons and polarizing filters.

**Two crossed polarizers.** Send 100 unpolarized photons toward a vertical ($0°$) polarizer. On average, half pass through — the polarizer transmits the component of polarization aligned with its axis. That gives us **50 photons**, now vertically polarized. Send those 50 into a horizontal ($90°$) polarizer. Malus's law gives the transmission probability as $\cos^2(\Delta\theta)$, where $\Delta\theta$ is the angle between the photon's polarization and the filter axis:

$$
50 \times \cos^2(90°) = 50 \times 0 = 0 \text{ photons}
$$

Nothing gets through. Crossed polarizers block everything. So far, no surprises.

**Now insert a 45° filter between them.** Same 100 unpolarized photons hit the vertical polarizer — **50 pass**, now vertically polarized. These 50 hit the new 45° filter:

$$
50 \times \cos^2(45°) = 50 \times \tfrac{1}{2} = 25 \text{ photons}
$$

Those 25 are now polarized at 45° (the filter resets their polarization to its own axis). They hit the horizontal filter:

$$
25 \times \cos^2(45°) = 25 \times \tfrac{1}{2} \approx 12 \text{ photons}
$$

**We went from 0 to 12 by adding a filter.** A device that can only block photons *increased* the total throughput. If photons carried a hidden property that predetermined pass/fail at every angle, adding a filter could only *reduce* what gets through — it would be one more gate to fail at. But the 45° filter does not merely check polarization; it *resets* it. Measurement is not a passive readout of a pre-existing property. It is an active transformation that prepares a new state.

This is already a crack in the instruction-card picture. The Bell argument applies the same logic to *pairs* of entangled photons.

### The hidden-instruction hypothesis

**The setup.** A source at the center emits pairs of entangled photons — one to Alice, one to Bob. Each experimenter has a polarizer set to some angle and a detector behind it. Each photon either passes through the polarizer ($+1$) or is absorbed ($-1$). Alice and Bob each choose their polarizer angle independently and record the outcome.

Suppose each photon pair leaves the source carrying a hidden "instruction card" $\lambda$ — a lookup table that pre-determines what each photon will do at every possible angle. Alice's photon consults the card and her angle to decide $+1$ or $-1$. Bob's does the same independently. This is exactly the LHV type from above:

- $\lambda$ = the instruction card
- $A(a, \lambda)$ = what Alice's photon does at angle $a$ given card $\lambda$
- **Locality** = Alice's card is consulted independently of Bob's setting, and vice versa

The question is: can *any* set of instruction cards reproduce what entangled photons actually do?

### The three-angle counting argument

Consider three polarizer angles: $0°$, $30°$, and $60°$. Each instruction card has three entries — one outcome per angle — and each entry is $+$ (pass) or $-$ (absorb). That gives $2^3 = 8$ possible cards.

Now, here is the crucial point: when Alice and Bob measure the same entangled pair at *different* angles, they **disagree** whenever their card prescribes different outcomes at those two angles. If the card says $+$ at $0°$ and $-$ at $60°$, then Alice (measuring at $0°$) gets "pass" while Bob (measuring at $60°$) gets "absorb" — they disagree. The last three columns of the table below ask exactly this question for each pair of angles: do the card's entries **differ**?

| Card | $0°$ | $30°$ | $60°$ | Differ at $0°$ vs $30°$? | Differ at $30°$ vs $60°$? | Differ at $0°$ vs $60°$? |
|:----:|:----:|:-----:|:-----:|:---:|:---:|:---:|
| 1 | $+$ | $+$ | $+$ | No | No | No |
| 2 | $+$ | $+$ | $-$ | No | Yes | Yes |
| 3 | $+$ | $-$ | $+$ | Yes | Yes | No |
| 4 | $+$ | $-$ | $-$ | Yes | No | Yes |
| 5 | $-$ | $+$ | $+$ | Yes | No | Yes |
| 6 | $-$ | $+$ | $-$ | Yes | Yes | No |
| 7 | $-$ | $-$ | $+$ | No | Yes | Yes |
| 8 | $-$ | $-$ | $-$ | No | No | No |

**The key observation.** Look at the last three columns. In every row where $0°$ and $60°$ differ (cards 2, 4, 5, 7), at least one of the two shorter intervals also differs — either the $0°$ and $30°$ entries are different, or the $30°$ and $60°$ entries are, or both. This is a logical necessity: if the card says $+$ at $0°$ and $-$ at $60°$, then somewhere between those two angles the card must switch from $+$ to $-$. The $30°$ entry is the only place it can happen, so at least one of the two adjacent pairs must show a difference. You can verify this row by row — there is no card where the outer pair disagrees but both inner pairs agree.

This means, for *any* distribution over the eight cards, the probability of a disagreement over the wide $0°$-to-$60°$ span cannot exceed the sum of disagreement probabilities over the two narrower spans:

$$
P(\text{disagree at } 0°,60°) \leq P(\text{disagree at } 0°,30°) + P(\text{disagree at } 30°,60°)
$$

This is Bell's original inequality (1964). It is not a statistical approximation — it is a theorem of classical probability, true for any mixture of instruction cards whatsoever.

**Now plug in the quantum predictions.** For entangled photon pairs, the probability that Alice and Bob get different outcomes when their polarizers differ by angle $\Delta\theta$ is:

$$
P(\text{disagree}) = \sin^2(\Delta\theta)
$$

Evaluate at our three angle separations:

- $P(\text{disagree at } 30° \text{ apart}) = \sin^2(30°) = \frac{1}{4}$
- $P(\text{disagree at } 60° \text{ apart}) = \sin^2(60°) = \frac{3}{4}$

The inequality requires:

$$
\frac{3}{4} \leq \frac{1}{4} + \frac{1}{4} = \frac{1}{2}
$$

But $\frac{3}{4} > \frac{1}{2}$. **Violated by 25 percentage points.**

**In concrete counts.** Out of 1,000 entangled pairs measured at $0°$ vs $60°$, quantum mechanics predicts **750 disagreements**. Any instruction-card model can produce at most **500**. The gap is 250 pairs — not a statistical fluctuation, but a structural impossibility.

### Why the cards fail

The inequality is a theorem, not an approximation. No amount of cleverness in designing instruction cards can circumvent it, because it follows from the logical structure of pre-assigned values.

The deeper reason is geometric. Quantum mechanics predicts disagreement rates that follow a $\sin^2(\Delta\theta)$ curve — a function that *bows outward* past 45°. Instruction-card models can only produce correlations that are *linear* or *bow inward* as a function of angle. The quantum curve exceeds the classical envelope at intermediate angles, and no classical mixture can close the gap.

{{< figure src="/images/bells_inequality/disagreement_curves.png" alt="Quantum vs classical disagreement probability as a function of polarizer angle" caption="Figure 0. Disagreement probability vs polarizer angle difference. The quantum prediction (red, sin²Δθ) crosses above the classical maximum (blue dashed, linear) beyond 45°. At 30° the quantum disagreement (0.25) is below the classical bound (0.33) — the cards can accommodate it. At 60° the quantum disagreement (0.75) exceeds the classical bound (0.67) — no mixture of instruction cards can reproduce this. The shaded region is structurally inaccessible to any local hidden-variable model." >}}

This is the same lesson as the three-polarizer experiment: measurement is not revealing a pre-existing property. If it were, the correlations would obey the instruction-card bound. They do not.

### Connecting to the formal proof

The instruction card is $\lambda$. The three-angle argument above is Bell's original 1964 inequality [[2]](#ref-2). The next section develops the CHSH inequality [[1]](#ref-1), which generalizes the argument to two settings per party with cleaner algebra, but the logic is identical: any LHV model produces $|S| \leq 2$, and quantum mechanics produces $|S| = 2\sqrt{2}$.

*A note on conventions.* This section used photon polarization, where the disagreement probability is $P = \sin^2(\Delta\theta)$. The formal sections use spin-1/2 particles, where the correlation function is $E = -\cos(\theta_a - \theta_b)$. The two conventions are related by a factor of 2 in the angles: a $30°$ polarizer difference corresponds to a $60°$ spin-axis difference. The structural argument — that no instruction-card model can reproduce quantum correlations — is convention-independent.

---

## The Bound as a Type Invariant

John Bell did not try to guess what $\lambda$ is. He asked: what must be true of *any* system with this type signature?

The specific form we use is the CHSH inequality [[1]](#ref-1), a two-setting generalization of Bell's original three-setting result [[2]](#ref-2). Alice chooses between settings $a_1$ and $a_2$; Bob chooses between $b_1$ and $b_2$. Define correlations:

$$
E(a, b) = \int_\Lambda A(a, \lambda) \, B(b, \lambda) \, d\mu(\lambda)
$$

and the CHSH quantity:

$$
S = E(a_1, b_1) - E(a_1, b_2) + E(a_2, b_1) + E(a_2, b_2)
$$

**Claim.** For any LHV model — any $\Lambda$, any $\mu$, any response functions $A$ and $B$ — we have $|S| \leq 2$.

**Proof sketch.** For a fixed $\lambda$, define $A_i = A(a_i, \lambda)$ and $B_j = B(b_j, \lambda)$, each in $\{+1, -1\}$. Expand the CHSH expression for this single $\lambda$:

$$
X(\lambda) = A_1 B_1 - A_1 B_2 + A_2 B_1 + A_2 B_2
$$

Collect the terms that share a common factor. The first two terms both contain $A_1$; the last two both contain $A_2$:

$$
= \underbrace{A_1 B_1 - A_1 B_2}_{\text{factor out } A_1} + \underbrace{A_2 B_1 + A_2 B_2}_{\text{factor out } A_2}
$$

Factor each group:

$$
= A_1(B_1 - B_2) + A_2(B_1 + B_2)
$$

Since $B_1, B_2 \in \{+1, -1\}$:
- If $B_1 = B_2$: then $(B_1 - B_2) = 0$ and $(B_1 + B_2) = \pm 2$, so $X = \pm 2$
- If $B_1 \neq B_2$: then $(B_1 - B_2) = \pm 2$ and $(B_1 + B_2) = 0$, so $X = \pm 2$

Therefore $X(\lambda) \in \{-2, +2\}$ for every $\lambda$. Averaging over any distribution:

$$
|S| = \left| \int X(\lambda) \, d\mu(\lambda) \right| \leq \int |X(\lambda)| \, d\mu(\lambda) = 2
$$

This is not a probabilistic result. It is a structural consequence of the dependency constraint. The bound holds for any distribution over $\lambda$ and any local response functions. In the language of type-driven development, this has the flavor of a *free theorem* — a behavioral constraint derivable from the type signature alone, without inspecting any particular implementation [[3]](#ref-3).

The analogy is productive but not literal. Wadler's free theorems are formal results in System F parametric polymorphism. Bell's result has the same structure — a universal constraint following from allowed dependencies rather than from implementation details — but is not derived within a type-theoretic framework. The parallel is in the reasoning pattern: the *shape* of the type constrains the *space* of possible behaviors.

---

## Experiment 1: Exhausting the Type

If the bound follows from the type, then no implementation should escape it. We verify this computationally by generating a large ensemble of LHV models across several classes:

1. **All 16 deterministic strategies**: enumerate every assignment of $A_1, A_2, B_1, B_2 \in \{+1, -1\}$. Every one produces $|S| = 2$.

2. **Random discrete models**: for $K$ hidden states with uniform distribution, assign random response tables. Sample 2,000 such models.

3. **Random continuous models**: draw $\lambda$ from uniform, Gaussian, and Beta distributions. Use random threshold functions $A(a, \lambda) = \text{sign}(\lambda - t_a)$. Sample 2,000 models.

4. **Adversarially optimized models**: use differential evolution to maximize $|S|$ over parameterized threshold-based response functions. Run 100 independent optimization restarts.

{{< figure src="/images/bells_inequality/lhv_exhaustion.png" alt="Distribution of |S| across LHV implementations" caption="Figure 1. Distribution of |S| across thousands of LHV implementations. No strategy exceeds the classical bound |S| = 2, regardless of the structure of λ, the distribution, or the response functions. The adversarial optimizer hits the wall at exactly 2." >}}

The result is definitive. Random strategies cluster well below the bound. Adversarial optimization reaches the bound but cannot exceed it. The deterministic strategies — which are the extremal points of the convex set of all LHV models — all land at $|S| = 2$ exactly.

This is not a failure of imagination. It is a structural impossibility. The bound is not something implementations approach; it is something the type enforces.

---

## The Quantum Type

Quantum mechanics assigns probabilities through a different mechanism.

In the classical model, probabilities compose directly:

$$
P(A, B \mid a, b) = \int P(A \mid a, \lambda) \, P(B \mid b, \lambda) \, d\mu(\lambda)
$$

In quantum mechanics, the fundamental objects are **amplitudes**, not probabilities. For a quantum state $|\psi\rangle$, the probability of an outcome is obtained via the Born rule:

$$
P(\text{outcome}) = |\langle \text{outcome} | \psi \rangle|^2
$$

The squaring — the passage from amplitude to probability — is a nonlinear operation. Amplitudes can interfere (add constructively or destructively) before the probability is extracted. This means the joint distribution $P(A, B \mid a, b)$ for an entangled state does not factorize through any shared classical variable.

For the singlet state $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$, the correlation between spin measurements at angles $\theta_a$ and $\theta_b$ is:

$$
E(\theta_a, \theta_b) = -\cos(\theta_a - \theta_b)
$$

This follows directly from the Born rule applied to projective measurements on the entangled state. The key mechanism is that the singlet state encodes correlations in amplitude space, and these correlations survive the Born rule in a form that no classical factorization can reproduce.

Specifically, for the singlet state there is no decomposition:

$$
P(A, B \mid a, b) \neq \int P(A \mid a, \lambda) \, P(B \mid b, \lambda) \, d\mu(\lambda)
$$

for any hidden variable $\lambda$ and any local response functions. This is Bell's theorem: the factorization demanded by the LHV type signature is incompatible with the observed correlations.

---

## Experiment 2: Quantum Violation

At the optimal CHSH angles — $a_1 = 0°$, $a_2 = 90°$, $b_1 = 45°$, $b_2 = 135°$ — the singlet state produces:

$$
|S| = 2\sqrt{2} \approx 2.828
$$

This is the **Tsirelson bound** [[4]](#ref-4): the maximum CHSH violation achievable by any quantum state. It exceeds the classical bound of 2 by a factor of $\sqrt{2}$.

We verify this by simulating projective measurements on the singlet state using the Born rule. For each of the four setting pairs, we sample 100,000 measurement outcomes from the joint distribution and estimate $E(a, b) = \langle A \cdot B \rangle$.

{{< figure src="/images/bells_inequality/quantum_convergence.png" alt="Convergence of simulated CHSH S toward theoretical value" caption="Figure 2. Convergence of simulated S toward the theoretical value S = −2√2 as the number of measurement trials increases. The estimate enters the violation region (|S| > 2) within a few hundred trials and stabilizes near the Tsirelson bound." >}}

The simulation converges to the theoretical value. The violation is not marginal — the quantum $|S|$ exceeds the classical bound by over 40%. With sufficient measurement statistics, the violation is unambiguous.

---

## Interactive: CHSH Angle Sweep

The magnitude of the CHSH violation depends on all four measurement angles. The interactive visualization below lets you vary the angles and watch $|S|$ update in real time.

The main curve sweeps Bob's angle $b_1$ from $0°$ to $360°$ while holding the other three angles fixed (adjustable via sliders). The classical bound $|S| = 2$ and the Tsirelson bound $|S| = 2\sqrt{2}$ are marked for reference.

<iframe src="/plots/bells_inequality/chsh_sweep.html" width="100%" height="720" style="border: none; border-radius: 8px; background: #1e1e1e;" loading="lazy"></iframe>

At the default settings ($a_1 = 0°$, $a_2 = 90°$, $b_1 = 45°$, $b_2 = 135°$), the quantum $|S|$ sits at $2\sqrt{2}$. As you move the sliders, observe that:

- The violation region is not a single point but a continuous range of angle configurations
- The maximum violation occurs when the four angles are evenly spaced at $45°$ intervals
- No angle configuration produces $|S| > 2\sqrt{2}$ — the Tsirelson bound is a quantum-level type constraint, just as $|S| \leq 2$ is a classical one

---

## Non-Embeddability

We can now state the conclusion precisely.

The LHV type defines a class of programs:

$$
\text{LHV} = \left\{ (A, B, \mu) \;\middle|\; A : \text{Setting} \times \Lambda \to \{+1,-1\}, \; B : \text{Setting} \times \Lambda \to \{+1,-1\}, \; A \perp\!\!\!\perp b, \; B \perp\!\!\!\perp a \right\}
$$

The CHSH inequality $|S| \leq 2$ is an invariant of this type. Any program in LHV satisfies it. This was established by proof and verified computationally across thousands of implementations.

Quantum mechanics produces correlations with $|S| = 2\sqrt{2}$. These correlations are observable, reproducible, and experimentally confirmed [[5]](#ref-5).

The implication is a **non-embeddability result**: the quantum correlations cannot be realized by any program of the LHV type. This is not a claim that we have failed to find the right hidden variable. It is a proof that no hidden variable with the LHV dependency structure can reproduce the data.

The failure is structural. It is not that $\lambda$ is the wrong variable, or that the distribution is wrong, or that the response functions are not clever enough. The entire type is wrong. The space of programs defined by local hidden variables and classical probability composition does not contain any program that produces the observed correlations.

This is the same pattern we encountered in *[The Models We Choose Define the Worlds We Can See](/posts/models_define_world/)*: representational constraints determine what dynamics can be expressed. An ODE cannot express network-dependent contagion. An LHV model cannot express quantum correlations. In both cases, the limitation is not in the parameter values — it is in the model's type signature.

---

## Closing

Bell's theorem is often presented as a paradox about nonlocality, or a philosophical puzzle about the nature of reality.

It is neither.

It is a constraint derivable from a dependency structure. If your model is local and classical, it satisfies $|S| \leq 2$. If the world produces $|S| > 2$, your model does not describe the world. Not because it needs better parameters, but because it inhabits the wrong type.

Quantum mechanics works because it computes in amplitude space. Amplitudes interfere before probabilities are extracted. This interference produces correlations that no classical factorization can replicate. The Born rule's nonlinearity — the squaring that converts amplitudes to probabilities — creates a gap between what classical programs can produce and what quantum systems actually produce.

> Bell's theorem does not tell us that reality is mysterious. It tells us that we chose the wrong abstraction.

---

## Experiments

The computational experiments supporting this essay are available in the project repository:

- **Experiment 1 -- Exhausting the Type**: [LHV Ensemble](https://github.com/encode-reality/sharc_theory/tree/main/experiments/bells_inequality) -- Thousands of local hidden-variable implementations, all bounded by |S| = 2.
- **Experiment 2 -- Quantum Violation**: [Singlet State Simulation](https://github.com/encode-reality/sharc_theory/tree/main/experiments/bells_inequality) -- Born rule measurements on the singlet state produce |S| = 2√2.
- **Experiment 3 -- Interactive Sweep**: [CHSH Angle Explorer](https://github.com/encode-reality/sharc_theory/tree/main/experiments/bells_inequality) -- Interactive Plotly visualization of CHSH value vs measurement angles.

<details>
<summary>Full source code</summary>

The complete implementation -- including LHV models, quantum simulation, adversarial optimization, and all plotting -- is available in the [`experiments/bells_inequality/`](https://github.com/encode-reality/sharc_theory/tree/main/experiments/bells_inequality) directory. Run it with:

```bash
python run_experiment.py --experiment all
```

</details>

---

## References

1. <a id="ref-1"></a>Clauser, J. F., Horne, M. A., Shimony, A., & Holt, R. A. (1969). "Proposed experiment to test local hidden-variable theories." *Physical Review Letters*, 23(15), 880-884.

2. <a id="ref-2"></a>Bell, J. S. (1964). "On the Einstein Podolsky Rosen paradox." *Physics Physique Fizika*, 1(3), 195-200.

3. <a id="ref-3"></a>Wadler, P. (1989). "Theorems for free!" *Proceedings of the Fourth International Conference on Functional Programming Languages and Computer Architecture*, 347-359.

4. <a id="ref-4"></a>Tsirelson, B. S. (1980). "Quantum generalizations of Bell's inequality." *Letters in Mathematical Physics*, 4(2), 93-100.

5. <a id="ref-5"></a>Aspect, A., Dalibard, J., & Roger, G. (1982). "Experimental test of Bell's inequalities using time-varying analyzers." *Physical Review Letters*, 49(25), 1804-1807.

---

*This essay is part of the [SHARC Theory](https://github.com/encode-reality/sharc_theory) research project.*
