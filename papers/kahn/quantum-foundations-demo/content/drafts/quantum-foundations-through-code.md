---
title: "Quantum Foundations Through Code: Why Amplitudes Matter More Than You Think"
date: 2026-03-13
draft: true
tags: ["quantum-mechanics", "python", "simulation", "grover"]
description: "Building intuition for quantum mechanics by contrasting classical probability with quantum amplitudes — from scratch in Python."
---

# Quantum Foundations Through Code

Most explanations of quantum computing start with a lie by omission. They tell you that a qubit can be "0 and 1 at the same time," that quantum computers "check every possibility in parallel," and that measurement "collapses" this parallelism into one answer. This framing is not just incomplete — it actively prevents you from understanding why quantum algorithms work.

The truth is simpler and stranger: **quantum mechanics replaces probabilities with amplitudes**, and amplitudes can interfere. That single fact is the engine behind everything from the double-slit experiment to Grover's search algorithm.

This post builds that intuition through code.

---

## Classical Probability: The Baseline

In classical probability, a system with $n$ possible states is described by a probability vector — $n$ nonneg real numbers summing to 1. You can sample from it, update it with stochastic matrices, and that's about it.

The key properties:
- Probabilities are **nonnegative**
- They **sum to 1**
- There is **no notion of phase or sign**
- There is **no interference**

![Classical probability distribution](/posts/quantum-foundations/probability-vs-amplitude.png)

---

## Enter Amplitudes

A quantum state over $n$ outcomes is a vector of $n$ **complex numbers** (amplitudes) whose squared magnitudes sum to 1. Probabilities are not primitive — they are **derived** from amplitudes via the Born rule:

$$P(i) = |\alpha_i|^2$$

Here's the crucial insight: **two quantum states can produce identical measurement probabilities while being fundamentally different states.**

Consider these two single-qubit states:

$$|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}, \qquad |-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}$$

Both give 50/50 odds when measured. But they are not the same state — the sign difference is real and consequential.

![Same probabilities, different quantum states](/posts/quantum-foundations/same-probabilities-different-states.png)

Apply a Hadamard gate to each:
- $H|+\rangle = |0\rangle$ — deterministically outcome 0
- $H|-\rangle = |1\rangle$ — deterministically outcome 1

The sign that was "hidden" from measurement probabilities completely determined the outcome after further evolution. **Amplitudes carry information that probabilities cannot represent.**

---

## Interference: The Key Departure

This is the centerpiece.

When amplitudes combine, they can:
- **Reinforce** (constructive interference): $\frac{1}{2} + \frac{1}{2} = 1 \Rightarrow P = 1$
- **Cancel** (destructive interference): $\frac{1}{2} + (-\frac{1}{2}) = 0 \Rightarrow P = 0$

Classical probabilities can only add: $0.25 + 0.25 = 0.5$. They can never cancel to zero.

![Constructive vs destructive interference](/posts/quantum-foundations/interference-cancellation.png)

This is not an analogy — it is the actual mathematical mechanism. When you apply $H$ twice to $|0\rangle$, the two "paths" through the $|0\rangle$ and $|1\rangle$ intermediate states interfere constructively back to $|0\rangle$. When you insert a $Z$ gate (phase flip) between the two Hadamards, the paths interfere destructively on $|0\rangle$ and constructively on $|1\rangle$.

---

## Gates: Linear Transformations on Amplitudes

Quantum gates are unitary matrices that act on amplitudes, not on probabilities. Some key gates:

- **X** (bit flip): swaps $|0\rangle \leftrightarrow |1\rangle$
- **Z** (phase flip): $|0\rangle \to |0\rangle$, $|1\rangle \to -|1\rangle$
- **H** (Hadamard): creates/destroys superposition

The Z gate is particularly instructive: it changes nothing about the measurement probabilities of a state, yet it completely alters how the state evolves under subsequent operations. The phase matters.

---

## Measurement and Collapse

When you measure a quantum state, you sample from the Born probability distribution. The state then "collapses" to the observed basis state. Repeated measurement of the collapsed state always gives the same result.

The key insight: measurement is **destructive**. It discards the amplitude information that made the state quantum.

---

## Multi-Qubit States

Two qubits give a 4-dimensional state space with basis states $|00\rangle, |01\rangle, |10\rangle, |11\rangle$. The state is constructed via tensor products of individual qubit states.

---

## Grover's Algorithm: Amplitude Amplification

Now we can understand Grover's search algorithm correctly.

Given a search space of $N$ items with one marked item, Grover's algorithm finds it in $O(\sqrt{N})$ steps. The popular explanation — "it checks all items in parallel" — is wrong. Here's what actually happens:

1. **Start in equal superposition**: all $N$ amplitudes equal to $1/\sqrt{N}$
2. **Oracle**: flip the sign of the marked item's amplitude (not its probability!)
3. **Diffusion**: reflect all amplitudes about their mean

The oracle changes a sign that is invisible to measurement probabilities. But the diffusion operator converts that sign change into an amplitude increase for the marked item and decreases for everything else.

![Oracle phase flip is invisible until diffusion](/posts/quantum-foundations/oracle-phase-demo.png)

Geometrically, this is a rotation in a 2D plane:

![Grover geometry: rotation in 2D plane](/posts/quantum-foundations/grover-plane.png)

Each iteration rotates the state vector toward the marked item by a fixed angle. After $\sim \frac{\pi}{4}\sqrt{N}$ iterations, the state is nearly aligned with the target.

![Grover target probability trajectory](/posts/quantum-foundations/grover-trajectory.png)

The advantage is not parallelism. It is **interference** — carefully orchestrated constructive interference on the target and destructive interference on everything else.

---

## The Bottom Line

| | Classical | Quantum |
|---|-----------|---------|
| State | Probability vector | Amplitude vector |
| Values | Nonnegative reals | Complex numbers |
| Normalization | Sum to 1 | Squared magnitudes sum to 1 |
| Phase/sign | Not meaningful | Determines evolution |
| Interference | Impossible | The essential feature |
| Measurement | Read probabilities directly | Derive probabilities, then sample |

The conceptual leap from classical to quantum is not about parallelism, superposition mysticism, or cats in boxes. It is about replacing probabilities with amplitudes — and gaining interference as a consequence.

---

## Code & Notebooks

All code and interactive notebooks are available in the [companion repository](https://github.com/yourusername/sharc_theory/tree/main/papers/kahn/quantum-foundations-demo).

Run the notebooks yourself to build hands-on intuition with the actual math.

---

*Built with numpy, matplotlib, and no quantum computing frameworks — because the point is to see the math directly.*
