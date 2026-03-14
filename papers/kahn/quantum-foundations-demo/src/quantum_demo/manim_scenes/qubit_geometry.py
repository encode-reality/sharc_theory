"""
Scene: QubitGeometry

Learning goal: A single-qubit state is a normalized vector, and gates
are rotations / reflections on the unit circle. Live probability
readouts connect the geometry to measurement outcomes.

Usage:
    manim -pql qubit_geometry.py QubitGeometry
"""

from manim import *
import numpy as np

# ---------------------------------------------------------------------------
# Attempt to import from quantum_demo; fall back to inline definitions.
# ---------------------------------------------------------------------------
try:
    from quantum_demo.states import amplitudes_to_probabilities
    from quantum_demo.gates import H, Z, apply_gate
    from quantum_demo.linalg import ket
except ImportError:
    def ket(index, dim):
        v = np.zeros(dim, dtype=np.complex128)
        v[index] = 1
        return v

    def amplitudes_to_probabilities(state):
        return (np.abs(state) ** 2).astype(np.float64)

    H = np.array([[1, 1], [1, -1]], dtype=np.complex128) / np.sqrt(2)
    Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)

    def apply_gate(state, gate):
        return gate @ state


class QubitGeometry(Scene):
    """Visualizes a real-valued qubit state as a vector on the unit circle."""

    def construct(self):
        # ── Layout constants ─────────────────────────────────────────────
        CIRCLE_RADIUS = 2.2
        CIRCLE_CENTER = LEFT * 2.2

        # ── Title ────────────────────────────────────────────────────────
        title = Text("Single-Qubit State Geometry", font_size=32)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # ── Draw unit circle and axes ────────────────────────────────────
        circle = Circle(radius=CIRCLE_RADIUS, color=GREY, stroke_width=1.5)
        circle.move_to(CIRCLE_CENTER)

        # Axes labels: horizontal = alpha_0, vertical = alpha_1
        ax_h = Arrow(
            CIRCLE_CENTER + LEFT * (CIRCLE_RADIUS + 0.4),
            CIRCLE_CENTER + RIGHT * (CIRCLE_RADIUS + 0.4),
            color=GREY_B, stroke_width=1.5, buff=0,
        )
        ax_v = Arrow(
            CIRCLE_CENTER + DOWN * (CIRCLE_RADIUS + 0.4),
            CIRCLE_CENTER + UP * (CIRCLE_RADIUS + 0.4),
            color=GREY_B, stroke_width=1.5, buff=0,
        )
        label_h = MathTex(r"\alpha_0", font_size=24, color=GREY_B)
        label_h.next_to(ax_h, RIGHT, buff=0.1)
        label_v = MathTex(r"\alpha_1", font_size=24, color=GREY_B)
        label_v.next_to(ax_v, UP, buff=0.1)

        # Basis state markers on the circle
        ket0_dot = Dot(CIRCLE_CENTER + RIGHT * CIRCLE_RADIUS, color=BLUE_C, radius=0.06)
        ket1_dot = Dot(CIRCLE_CENTER + UP * CIRCLE_RADIUS, color=RED_C, radius=0.06)
        ket0_label = MathTex(r"|0\rangle", font_size=22, color=BLUE_C)
        ket0_label.next_to(ket0_dot, DR, buff=0.1)
        ket1_label = MathTex(r"|1\rangle", font_size=22, color=RED_C)
        ket1_label.next_to(ket1_dot, UL, buff=0.1)

        self.play(
            Create(circle), Create(ax_h), Create(ax_v),
            Write(label_h), Write(label_v),
            FadeIn(ket0_dot), FadeIn(ket1_dot),
            Write(ket0_label), Write(ket1_label),
        )

        # ── State vector (initially |0>) ────────────────────────────────
        angle_tracker = ValueTracker(0)  # angle in radians from |0> axis

        def _tip_point():
            a = angle_tracker.get_value()
            return CIRCLE_CENTER + CIRCLE_RADIUS * np.array(
                [np.cos(a), np.sin(a), 0]
            )

        state_arrow = always_redraw(
            lambda: Arrow(
                CIRCLE_CENTER, _tip_point(),
                color=YELLOW, buff=0, stroke_width=4,
            )
        )
        tip_dot = always_redraw(
            lambda: Dot(_tip_point(), color=YELLOW, radius=0.08)
        )

        self.play(GrowArrow(state_arrow), FadeIn(tip_dot))

        # ── Live probability display (right side) ────────────────────────
        prob_group_anchor = RIGHT * 2.8 + UP * 1.0

        p0_label = always_redraw(lambda: MathTex(
            r"P(|0\rangle) = " + f"{np.cos(angle_tracker.get_value())**2:.3f}",
            font_size=28, color=BLUE_C,
        ).move_to(prob_group_anchor))

        p1_label = always_redraw(lambda: MathTex(
            r"P(|1\rangle) = " + f"{np.sin(angle_tracker.get_value())**2:.3f}",
            font_size=28, color=RED_C,
        ).move_to(prob_group_anchor + DOWN * 0.55))

        angle_label = always_redraw(lambda: MathTex(
            r"\theta = " + f"{np.degrees(angle_tracker.get_value()):.1f}^\\circ",
            font_size=26, color=YELLOW,
        ).move_to(prob_group_anchor + DOWN * 1.3))

        state_label = always_redraw(lambda: MathTex(
            f"{np.cos(angle_tracker.get_value()):.3f}" + r"|0\rangle + "
            + f"{np.sin(angle_tracker.get_value()):.3f}" + r"|1\rangle",
            font_size=26,
        ).move_to(prob_group_anchor + DOWN * 2.0))

        self.play(
            Write(p0_label), Write(p1_label),
            Write(angle_label), Write(state_label),
        )
        self.wait(0.5)

        # ── Animate: sweep from |0> to |1> (0 to pi/2) ──────────────────
        sweep_note = Text("Rotate from |0> toward |1>", font_size=22, color=GREY_B)
        sweep_note.to_edge(DOWN, buff=0.5)
        self.play(Write(sweep_note))
        self.play(angle_tracker.animate.set_value(PI / 2), run_time=3, rate_func=smooth)
        self.wait(0.8)

        # ── Animate: sweep to several notable angles ─────────────────────
        self.play(FadeOut(sweep_note))
        notable_angles = [
            (PI / 4, r"\theta = 45^{\circ}:\ \text{equal superposition}"),
            (PI / 3, r"\theta = 60^{\circ}:\ \text{biased toward } |1\rangle"),
            (0, r"\theta = 0^{\circ}:\ |0\rangle"),
        ]

        for target_angle, desc_tex in notable_angles:
            desc = MathTex(desc_tex, font_size=24, color=GREY_B).to_edge(DOWN, buff=0.5)
            self.play(Write(desc))
            self.play(
                angle_tracker.animate.set_value(target_angle),
                run_time=1.8, rate_func=smooth,
            )
            self.wait(1.0)
            self.play(FadeOut(desc))

        # ================================================================
        # Part 2: Gate operations on |0>
        # ================================================================
        gate_title = Text("Applying Gates to |0>", font_size=28, color=YELLOW)
        gate_title.to_edge(DOWN, buff=0.5)
        self.play(Write(gate_title))
        self.wait(0.5)

        # Ensure we start at |0>
        self.play(angle_tracker.animate.set_value(0), run_time=0.8)

        # ── Apply H: |0> -> |+> = cos(pi/4)|0> + sin(pi/4)|1> ──────────
        h_label = Text("H |0>  =  |+>", font_size=24, color=GREEN_C)
        h_label.next_to(gate_title, UP, buff=0.3)
        self.play(Write(h_label))
        self.play(
            angle_tracker.animate.set_value(PI / 4),
            run_time=1.5, rate_func=smooth,
        )
        self.wait(1.2)
        self.play(FadeOut(h_label))

        # ── Apply Z to |+>: flips sign of |1> component ─────────────────
        # Z|+> = (1/sqrt2)|0> - (1/sqrt2)|1> => angle = -pi/4
        z_label = Text("Z |+>  =  |->", font_size=24, color=RED_C)
        z_label.next_to(gate_title, UP, buff=0.3)
        z_note = Text(
            "(Z flips the sign of the |1> amplitude)",
            font_size=20, color=GREY_B,
        ).next_to(z_label, UP, buff=0.15)

        self.play(Write(z_label), Write(z_note))
        self.play(
            angle_tracker.animate.set_value(-PI / 4),
            run_time=1.5, rate_func=smooth,
        )
        self.wait(1.0)

        # Point out: same probabilities as |+>
        same_prob_note = Text(
            "Same probabilities as |+>! Phase is invisible to measurement.",
            font_size=22,
            color=YELLOW,
        ).next_to(z_note, UP, buff=0.2)
        self.play(Write(same_prob_note))
        self.wait(2)

        # ── Cleanup and takeaway ─────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects])

        takeaway = VGroup(
            Text("Key Insight", font_size=34, color=YELLOW),
            Text(
                "A qubit state is a unit vector: rotations change probabilities.",
                font_size=26,
            ),
            Text(
                "Gates like H and Z are geometric operations on this vector.",
                font_size=24,
                color=GREY_B,
            ),
            Text(
                "Different vectors can yield the same probabilities (phase matters).",
                font_size=24,
                color=GREY_B,
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(takeaway), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(takeaway))
