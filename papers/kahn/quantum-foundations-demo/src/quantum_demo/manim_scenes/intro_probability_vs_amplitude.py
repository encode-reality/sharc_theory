"""
Scene: ProbabilityVsAmplitude

Learning goal: Probabilities are derived from amplitudes, not primitive.
Shows that distinct amplitude vectors can produce identical probability
distributions, demonstrating that amplitudes carry strictly more information.

Usage:
    manim -pql intro_probability_vs_amplitude.py ProbabilityVsAmplitude
"""

from manim import *
import numpy as np

# ---------------------------------------------------------------------------
# Attempt to import from quantum_demo; fall back to inline definitions.
# ---------------------------------------------------------------------------
try:
    from quantum_demo.states import (
        amplitudes_to_probabilities,
        qubit_state,
    )
    from quantum_demo.gates import H, Z, apply_gate
    from quantum_demo.linalg import ket
except ImportError:
    # Inline fallbacks so the file is self-contained.
    def ket(index, dim):
        v = np.zeros(dim, dtype=np.complex128)
        v[index] = 1
        return v

    def amplitudes_to_probabilities(state):
        return (np.abs(state) ** 2).astype(np.float64)

    def qubit_state(alpha, beta):
        v = np.array([alpha, beta], dtype=np.complex128)
        return v / np.linalg.norm(v)

    H = np.array([[1, 1], [1, -1]], dtype=np.complex128) / np.sqrt(2)
    Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)

    def apply_gate(state, gate):
        return gate @ state


# ---------------------------------------------------------------------------
# Helper: build a Manim BarChart with given heights and labels.
# ---------------------------------------------------------------------------
def _bar_chart(values, labels, bar_colors, y_max=1.0, width=5, height=3):
    """Return a VGroup of rectangles + labels forming a simple bar chart."""
    chart = VGroup()
    n = len(values)
    bar_width = width / (2 * n)
    spacing = width / n

    for i, (val, label_text, color) in enumerate(zip(values, labels, bar_colors)):
        bar_height = (val / y_max) * height if y_max != 0 else 0
        bar = Rectangle(
            width=bar_width,
            height=max(bar_height, 0.02),
            fill_color=color,
            fill_opacity=0.85,
            stroke_color=WHITE,
            stroke_width=1.5,
        )
        bar.move_to(
            LEFT * width / 2
            + RIGHT * (i * spacing + spacing / 2),
            aligned_edge=DOWN,
        )
        lbl = Text(label_text, font_size=22).next_to(bar, DOWN, buff=0.15)
        val_lbl = Text(f"{val:.2f}", font_size=20).next_to(bar, UP, buff=0.1)
        chart.add(VGroup(bar, lbl, val_lbl))

    return chart


class ProbabilityVsAmplitude(Scene):
    """Demonstrates that quantum probabilities derive from amplitudes."""

    def construct(self):
        # ── Section 1: classical probability distribution ────────────────
        title_classical = Text("Classical Probability Distribution", font_size=32)
        title_classical.to_edge(UP, buff=0.5)
        self.play(Write(title_classical))

        classical_probs = [0.5, 0.5]
        classical_labels = ["|0>", "|1>"]
        classical_colors = [BLUE_D, BLUE_D]
        classical_chart = _bar_chart(
            classical_probs, classical_labels, classical_colors
        )
        classical_chart.move_to(ORIGIN)

        desc_classical = Text(
            "Two outcomes, each with probability 0.50",
            font_size=24,
        ).next_to(classical_chart, DOWN, buff=0.5)

        self.play(FadeIn(classical_chart, shift=UP), run_time=1.2)
        self.play(Write(desc_classical))
        self.wait(1.5)

        # ── Section 2: quantum state |+> with amplitudes ────────────────
        self.play(FadeOut(title_classical), FadeOut(classical_chart), FadeOut(desc_classical))

        title_quantum = Text("Quantum State  |+>", font_size=32).to_edge(UP, buff=0.5)
        self.play(Write(title_quantum))

        ket0 = ket(0, 2)
        plus_state = apply_gate(ket0, H)  # 1/sqrt(2) [1, 1]
        plus_amps = [float(np.real(a)) for a in plus_state]

        amp_labels = ["|0>", "|1>"]
        amp_colors = [GREEN_C, GREEN_C]
        amp_chart = _bar_chart(
            plus_amps, amp_labels, amp_colors, y_max=1.0
        )
        amp_chart.move_to(UP * 0.3)

        amp_title = Text("Amplitudes", font_size=26, color=GREEN_C)
        amp_title.next_to(amp_chart, UP, buff=0.3)

        state_tex = MathTex(
            r"|+\rangle = \frac{1}{\sqrt{2}}|0\rangle + \frac{1}{\sqrt{2}}|1\rangle",
            font_size=34,
        ).next_to(amp_chart, DOWN, buff=0.5)

        self.play(FadeIn(amp_chart, shift=UP), Write(amp_title))
        self.play(Write(state_tex))
        self.wait(1.5)

        # ── Section 3: squaring amplitudes into probabilities ────────────
        self.play(FadeOut(amp_title))

        arrow_text = Text("Square magnitudes:", font_size=24, color=YELLOW)
        arrow_text.next_to(amp_chart, UP, buff=0.3)
        sq_formula = MathTex(
            r"P(i) = |\alpha_i|^2", font_size=30, color=YELLOW
        ).next_to(arrow_text, DOWN, buff=0.15)

        self.play(Write(arrow_text), Write(sq_formula))
        self.wait(0.8)

        plus_probs = amplitudes_to_probabilities(plus_state)
        prob_chart = _bar_chart(
            list(plus_probs), amp_labels, [BLUE_D, BLUE_D], y_max=1.0
        )
        prob_chart.move_to(amp_chart.get_center())

        prob_title = Text("Probabilities", font_size=26, color=BLUE_D)
        prob_title.next_to(prob_chart, UP, buff=0.6)

        self.play(
            Transform(amp_chart, prob_chart),
            FadeOut(arrow_text),
            FadeOut(sq_formula),
            FadeIn(prob_title),
            run_time=1.5,
        )
        self.wait(1.0)

        # ── Section 4: show |-> has same probabilities, different amps ───
        self.play(
            FadeOut(amp_chart),
            FadeOut(prob_chart, target_position=UP),
            FadeOut(prob_title),
            FadeOut(state_tex),
            FadeOut(title_quantum),
        )

        title_compare = Text(
            "Same Probabilities, Different Amplitudes",
            font_size=30,
        ).to_edge(UP, buff=0.4)
        self.play(Write(title_compare))

        minus_state = apply_gate(apply_gate(ket0, H), Z)  # 1/sqrt(2) [1, -1]
        minus_amps = [float(np.real(a)) for a in minus_state]

        # Side-by-side amplitude charts
        left_header = Text("|+> amplitudes", font_size=22, color=GREEN_C)
        right_header = Text("|-> amplitudes", font_size=22, color=RED_C)

        left_chart = _bar_chart(
            plus_amps, amp_labels, [GREEN_C, GREEN_C], y_max=1.0, width=3, height=2.2
        )
        right_chart = _bar_chart(
            [abs(a) for a in minus_amps],
            amp_labels,
            [RED_C, RED_C],
            y_max=1.0,
            width=3,
            height=2.2,
        )

        left_group = VGroup(left_header, left_chart).arrange(DOWN, buff=0.2)
        right_group = VGroup(right_header, right_chart).arrange(DOWN, buff=0.2)

        side_by_side = VGroup(left_group, right_group).arrange(RIGHT, buff=1.5)
        side_by_side.move_to(UP * 0.5)

        # Show amplitude values with explicit signs
        plus_tex = MathTex(
            r"\alpha_0 = +\tfrac{1}{\sqrt2}", r",\;\;",
            r"\alpha_1 = +\tfrac{1}{\sqrt2}",
            font_size=28, color=GREEN_C,
        )
        minus_tex = MathTex(
            r"\alpha_0 = +\tfrac{1}{\sqrt2}", r",\;\;",
            r"\alpha_1 = -\tfrac{1}{\sqrt2}",
            font_size=28, color=RED_C,
        )

        plus_tex.next_to(left_group, DOWN, buff=0.35)
        minus_tex.next_to(right_group, DOWN, buff=0.35)

        self.play(FadeIn(side_by_side, shift=UP))
        self.play(Write(plus_tex), Write(minus_tex))
        self.wait(1.5)

        # Show that both give same probabilities
        same_prob_text = Text(
            "Both yield P(|0>) = 0.50,  P(|1>) = 0.50",
            font_size=26,
            color=YELLOW,
        ).to_edge(DOWN, buff=0.6)

        self.play(Write(same_prob_text))
        self.wait(1.5)

        # ── Section 5: takeaway ──────────────────────────────────────────
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        takeaway = VGroup(
            Text("Key Insight", font_size=34, color=YELLOW),
            Text(
                "Probabilities are derived from amplitudes.",
                font_size=28,
            ),
            Text(
                "Amplitudes carry phase information that probabilities discard.",
                font_size=26,
                color=GREY_B,
            ),
            Text(
                "This hidden structure is what makes interference possible.",
                font_size=26,
                color=GREY_B,
            ),
        ).arrange(DOWN, buff=0.4)

        self.play(Write(takeaway), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(takeaway))
