"""
Scene: InterferenceScene

Learning goal: Interference is the key nonclassical feature of quantum mechanics.
Signed amplitudes can reinforce (constructive) or cancel (destructive),
while classical probabilities can only add.

Usage:
    manim -pql interference_scene.py InterferenceScene
"""

from manim import *
import numpy as np

# ---------------------------------------------------------------------------
# Attempt to import from quantum_demo; fall back to inline definitions.
# ---------------------------------------------------------------------------
try:
    from quantum_demo.interference import (
        path_amplitude_sum,
        compare_probability_vs_amplitude_combination,
    )
except ImportError:
    def path_amplitude_sum(contributions):
        total = sum(contributions)
        return total, float(abs(total) ** 2)

    def compare_probability_vs_amplitude_combination():
        return {
            "classical_probs": {"paths": [0.25, 0.25], "total": 0.5},
            "quantum_constructive": {"amplitudes": [0.5, 0.5], "probability": 1.0},
            "quantum_destructive": {"amplitudes": [0.5, -0.5], "probability": 0.0},
        }


# ---------------------------------------------------------------------------
# Helper: draw an arrow labeled with an amplitude value.
# ---------------------------------------------------------------------------
def _amplitude_arrow(start, end, label_text, color=WHITE, font_size=24):
    """Return a VGroup containing an Arrow and a label."""
    arrow = Arrow(start, end, color=color, buff=0, stroke_width=4)
    label = Text(label_text, font_size=font_size, color=color)
    label.next_to(arrow, UP, buff=0.12)
    return VGroup(arrow, label)


class InterferenceScene(Scene):
    """Shows constructive vs destructive interference and contrast with classical addition."""

    def construct(self):
        # ── Title ────────────────────────────────────────────────────────
        title = Text("Quantum Interference", font_size=36)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))
        self.wait(0.5)

        # ================================================================
        # Part 1: Constructive interference  [0.5, 0.5] -> 1.0
        # ================================================================
        section_1 = Text("Constructive Interference", font_size=28, color=GREEN_C)
        section_1.next_to(title, DOWN, buff=0.35)
        self.play(Write(section_1))

        # Number line from -1 to +1
        number_line = NumberLine(
            x_range=[-1.2, 1.2, 0.5],
            length=8,
            include_numbers=True,
            font_size=22,
        ).shift(UP * 0.3)
        nl_label = Text("Amplitude axis", font_size=20, color=GREY_B)
        nl_label.next_to(number_line, DOWN, buff=0.15)
        self.play(Create(number_line), Write(nl_label))

        # First contribution: 0.5 from origin
        origin = number_line.n2p(0)
        mid = number_line.n2p(0.5)
        end_con = number_line.n2p(1.0)

        arrow1 = _amplitude_arrow(origin, mid, "+0.5", color=BLUE_C)
        self.play(GrowArrow(arrow1[0]), Write(arrow1[1]))
        self.wait(0.4)

        # Second contribution: another 0.5
        arrow2 = _amplitude_arrow(mid, end_con, "+0.5", color=TEAL_C)
        arrow2[1].shift(DOWN * 0.45)  # offset label to avoid overlap
        self.play(GrowArrow(arrow2[0]), Write(arrow2[1]))
        self.wait(0.3)

        # Result
        total_dot = Dot(end_con, color=GREEN_C, radius=0.1)
        total_label = MathTex(
            r"\text{sum} = 1.0", font_size=28, color=GREEN_C
        ).next_to(total_dot, UP, buff=0.2)
        self.play(FadeIn(total_dot, scale=1.5), Write(total_label))

        # Show resulting probability
        prob_con = MathTex(
            r"P = |1.0|^2 = 1.0", font_size=30, color=GREEN_C
        ).shift(DOWN * 1.5)
        self.play(Write(prob_con))
        self.wait(1.5)

        # Clear for Part 2
        part1_mobs = VGroup(
            arrow1, arrow2, total_dot, total_label, prob_con, section_1
        )
        self.play(FadeOut(part1_mobs))

        # ================================================================
        # Part 2: Destructive interference  [0.5, -0.5] -> 0.0
        # ================================================================
        section_2 = Text("Destructive Interference", font_size=28, color=RED_C)
        section_2.next_to(title, DOWN, buff=0.35)
        self.play(Write(section_2))

        # First contribution: +0.5
        arrow3 = _amplitude_arrow(origin, mid, "+0.5", color=BLUE_C)
        self.play(GrowArrow(arrow3[0]), Write(arrow3[1]))
        self.wait(0.4)

        # Second contribution: -0.5 (goes back to origin)
        arrow4 = _amplitude_arrow(mid, origin + RIGHT * 0.01, "-0.5", color=RED_C)
        # Slight offset so arrow is visible; label below
        arrow4[1].next_to(arrow4[0], DOWN, buff=0.12)
        self.play(GrowArrow(arrow4[0]), Write(arrow4[1]))
        self.wait(0.3)

        # Result
        cancel_dot = Dot(origin, color=RED_C, radius=0.1)
        cancel_label = MathTex(
            r"\text{sum} = 0.0", font_size=28, color=RED_C
        ).next_to(cancel_dot, UP, buff=0.5)
        self.play(FadeIn(cancel_dot, scale=1.5), Write(cancel_label))

        prob_des = MathTex(
            r"P = |0.0|^2 = 0.0", font_size=30, color=RED_C
        ).shift(DOWN * 1.5)
        self.play(Write(prob_des))
        self.wait(1.5)

        # Clear for Part 3
        part2_mobs = VGroup(
            arrow3, arrow4, cancel_dot, cancel_label, prob_des,
            section_2, number_line, nl_label,
        )
        self.play(FadeOut(part2_mobs))

        # ================================================================
        # Part 3: Classical vs Quantum comparison table
        # ================================================================
        section_3 = Text(
            "Classical vs Quantum Combination", font_size=28, color=YELLOW
        )
        section_3.next_to(title, DOWN, buff=0.35)
        self.play(Write(section_3))

        data = compare_probability_vs_amplitude_combination()

        # Build a comparison table as aligned Text groups
        col_headers = VGroup(
            Text("", font_size=22),
            Text("Path A", font_size=22, color=BLUE_C),
            Text("Path B", font_size=22, color=TEAL_C),
            Text("Combined", font_size=22, color=YELLOW),
            Text("Probability", font_size=22, color=GREEN_C),
        ).arrange(RIGHT, buff=0.7).shift(UP * 0.8)

        # Classical row
        cl = data["classical_probs"]
        classical_row = VGroup(
            Text("Classical", font_size=22),
            Text(f"{cl['paths'][0]:.2f}", font_size=22),
            Text(f"{cl['paths'][1]:.2f}", font_size=22),
            Text(f"{cl['total']:.2f}", font_size=22),
            Text(f"{cl['total']:.2f}", font_size=22, color=GREEN_C),
        ).arrange(RIGHT, buff=0.7)

        # Quantum constructive row
        qc = data["quantum_constructive"]
        constructive_row = VGroup(
            Text("Quantum (+)", font_size=22, color=GREEN_C),
            Text(f"+{qc['amplitudes'][0]:.1f}", font_size=22),
            Text(f"+{qc['amplitudes'][1]:.1f}", font_size=22),
            Text("+1.0", font_size=22),
            Text(f"{qc['probability']:.2f}", font_size=22, color=GREEN_C),
        ).arrange(RIGHT, buff=0.7)

        # Quantum destructive row
        qd = data["quantum_destructive"]
        destructive_row = VGroup(
            Text("Quantum (-)", font_size=22, color=RED_C),
            Text(f"+{qd['amplitudes'][0]:.1f}", font_size=22),
            Text(f"{qd['amplitudes'][1]:.1f}", font_size=22),
            Text(" 0.0", font_size=22),
            Text(f"{qd['probability']:.2f}", font_size=22, color=RED_C),
        ).arrange(RIGHT, buff=0.7)

        table = VGroup(col_headers, classical_row, constructive_row, destructive_row)
        table.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        table.move_to(DOWN * 0.3)

        for row in table:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        # ── Highlight the key contrast ───────────────────────────────────
        box_destruct = SurroundingRectangle(
            destructive_row[-1], color=RED, buff=0.1
        )
        note = Text(
            "Classical probabilities can never cancel to zero!",
            font_size=24,
            color=RED_C,
        ).to_edge(DOWN, buff=0.5)
        self.play(Create(box_destruct), Write(note))
        self.wait(2)

        # ── Takeaway ────────────────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects])

        takeaway = VGroup(
            Text("Key Insight", font_size=34, color=YELLOW),
            Text(
                "Quantum amplitudes are signed and sum before squaring.",
                font_size=26,
            ),
            Text(
                "Same-sign amplitudes reinforce (constructive interference).",
                font_size=24,
                color=GREEN_C,
            ),
            Text(
                "Opposite-sign amplitudes cancel (destructive interference).",
                font_size=24,
                color=RED_C,
            ),
            Text(
                "Classical probabilities are non-negative and can only add.",
                font_size=24,
                color=GREY_B,
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(takeaway), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(takeaway))
