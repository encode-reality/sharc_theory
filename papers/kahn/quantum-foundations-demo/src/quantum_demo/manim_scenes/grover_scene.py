"""
Scene: GroverGeometry

Learning goal: Grover's algorithm is amplitude amplification via two
reflections in a 2D plane, steadily rotating the state toward the
target basis state.

Usage:
    manim -pql grover_scene.py GroverGeometry
"""

from manim import *
import numpy as np

# ---------------------------------------------------------------------------
# Attempt to import from quantum_demo; fall back to inline definitions.
# ---------------------------------------------------------------------------
try:
    from quantum_demo.grover import (
        grover_run,
        grover_optimal_iterations,
        reduced_grover_plane_coordinates,
        target_probability_trajectory,
    )
    from quantum_demo.states import equal_superposition, amplitudes_to_probabilities
except ImportError:
    def equal_superposition(dim):
        return np.ones(dim, dtype=np.complex128) / np.sqrt(dim)

    def amplitudes_to_probabilities(state):
        return (np.abs(state) ** 2).astype(np.float64)

    def grover_optimal_iterations(dim):
        return round(np.pi / 4 * np.sqrt(dim))

    def _phase_oracle(target_index, dim):
        d = np.ones(dim, dtype=np.complex128)
        d[target_index] = -1
        return np.diag(d)

    def _diffusion_operator(dim):
        s = np.ones(dim, dtype=np.complex128) / np.sqrt(dim)
        return 2.0 * np.outer(s, s) - np.eye(dim, dtype=np.complex128)

    def grover_run(dim, target_index, iterations):
        state = equal_superposition(dim)
        traj = [state.copy()]
        oracle = _phase_oracle(target_index, dim)
        diffusion = _diffusion_operator(dim)
        for _ in range(iterations):
            state = diffusion @ (oracle @ state)
            traj.append(state.copy())
        return traj

    def target_probability_trajectory(dim, target_index, iterations):
        states = grover_run(dim, target_index, iterations)
        return np.array([amplitudes_to_probabilities(s)[target_index] for s in states])

    def reduced_grover_plane_coordinates(state, target_index):
        dim = len(state)
        t = np.zeros(dim, dtype=np.complex128)
        t[target_index] = 1
        sp = np.ones(dim, dtype=np.complex128)
        sp[target_index] = 0
        sp = sp / np.linalg.norm(sp)
        x = float(np.real(np.vdot(t, state)))
        y = float(np.real(np.vdot(sp, state)))
        return x, y


class GroverGeometry(Scene):
    """Visualizes Grover's algorithm as rotations in a 2D amplitude plane."""

    def construct(self):
        # ── Configuration ────────────────────────────────────────────────
        DIM = 8                  # search space size (N = 8, i.e., 3 qubits)
        TARGET = 3               # marked item index
        NUM_ITERS = grover_optimal_iterations(DIM)

        # Pre-compute trajectory
        trajectory = grover_run(DIM, TARGET, NUM_ITERS)
        coords = [reduced_grover_plane_coordinates(s, TARGET) for s in trajectory]
        probs = target_probability_trajectory(DIM, TARGET, NUM_ITERS)

        # ── Title ────────────────────────────────────────────────────────
        title = Text("Grover's Algorithm: Geometry of Amplitude Amplification", font_size=28)
        title.to_edge(UP, buff=0.35)
        self.play(Write(title))

        # ── 2D Grover plane (left half) ─────────────────────────────────
        PLANE_CENTER = LEFT * 3.0 + DOWN * 0.3
        PLANE_SCALE = 2.8  # radius of the quarter-circle region

        # Draw axes: x = |target>, y = |s_perp>
        ax_x = Arrow(
            PLANE_CENTER + LEFT * 0.3,
            PLANE_CENTER + RIGHT * (PLANE_SCALE + 0.5),
            color=GREY_B, stroke_width=1.5, buff=0,
        )
        ax_y = Arrow(
            PLANE_CENTER + DOWN * 0.3,
            PLANE_CENTER + UP * (PLANE_SCALE + 0.5),
            color=GREY_B, stroke_width=1.5, buff=0,
        )
        lbl_x = MathTex(r"|w\rangle", font_size=22, color=RED_C)
        lbl_x.next_to(ax_x, RIGHT, buff=0.1)
        lbl_y = MathTex(r"|s_\perp\rangle", font_size=22, color=BLUE_C)
        lbl_y.next_to(ax_y, UP, buff=0.1)

        # Quarter arc showing the unit circle
        arc = Arc(
            radius=PLANE_SCALE, start_angle=0, angle=PI / 2,
            color=GREY, stroke_width=1,
        ).move_arc_center_to(PLANE_CENTER)

        self.play(
            Create(ax_x), Create(ax_y),
            Write(lbl_x), Write(lbl_y),
            Create(arc),
        )

        # ── Initial state: equal superposition |s> ──────────────────────
        x0, y0 = coords[0]
        initial_angle = np.arctan2(x0, y0)  # angle from y-axis (|s_perp>)
        # But we display: x-axis = |target>, y-axis = |s_perp>
        # So the point is at (x0 * PLANE_SCALE, y0 * PLANE_SCALE) from PLANE_CENTER
        def _to_screen(x, y):
            return PLANE_CENTER + RIGHT * x * PLANE_SCALE + UP * y * PLANE_SCALE

        init_point = _to_screen(x0, y0)
        init_arrow = Arrow(
            PLANE_CENTER, init_point,
            color=YELLOW, buff=0, stroke_width=3,
        )
        init_label = MathTex(r"|s\rangle", font_size=22, color=YELLOW)
        init_label.next_to(init_point, UR, buff=0.1)

        # Dashed line to show the small angle theta
        theta_arc = Arc(
            radius=0.7,
            start_angle=PI / 2 - np.arctan2(x0, y0),
            angle=np.arctan2(x0, y0),
            color=YELLOW,
            stroke_width=1.5,
        ).move_arc_center_to(PLANE_CENTER)
        theta_label = MathTex(r"\theta", font_size=20, color=YELLOW)
        theta_label.next_to(theta_arc, RIGHT, buff=0.05).shift(UP * 0.15)

        self.play(GrowArrow(init_arrow), Write(init_label))
        self.play(Create(theta_arc), Write(theta_label))
        self.wait(0.8)

        # ── Probability bar (right side) ─────────────────────────────────
        BAR_ANCHOR = RIGHT * 3.5 + DOWN * 2.0
        BAR_HEIGHT_MAX = 3.5
        BAR_WIDTH = 0.8

        bar_bg = Rectangle(
            width=BAR_WIDTH, height=BAR_HEIGHT_MAX,
            stroke_color=GREY, stroke_width=1, fill_opacity=0,
        )
        bar_bg.move_to(BAR_ANCHOR + UP * BAR_HEIGHT_MAX / 2, aligned_edge=DOWN)

        prob_tracker = ValueTracker(float(probs[0]))

        prob_bar = always_redraw(lambda: Rectangle(
            width=BAR_WIDTH,
            height=max(prob_tracker.get_value() * BAR_HEIGHT_MAX, 0.01),
            fill_color=interpolate_color(BLUE, GREEN, prob_tracker.get_value()),
            fill_opacity=0.85,
            stroke_width=1,
            stroke_color=WHITE,
        ).move_to(BAR_ANCHOR, aligned_edge=DOWN))

        prob_value_label = always_redraw(lambda: Text(
            f"P(target) = {prob_tracker.get_value():.3f}",
            font_size=22,
        ).next_to(bar_bg, UP, buff=0.2))

        bar_title = Text("Target Probability", font_size=22, color=GREEN_C)
        bar_title.next_to(bar_bg, UP, buff=0.55)

        self.play(
            Create(bar_bg), FadeIn(prob_bar),
            Write(prob_value_label), Write(bar_title),
        )
        self.wait(0.5)

        # ── Step-by-step Grover iterations ───────────────────────────────
        iter_label = Text("Iteration 0", font_size=22, color=GREY_B)
        iter_label.next_to(bar_bg, DOWN, buff=0.4)
        self.play(Write(iter_label))

        current_arrow = init_arrow
        current_label_mob = init_label

        # Colors for successive arrows
        iter_colors = [ORANGE, GOLD, GREEN_C, TEAL_C, BLUE_C, PURPLE_C]

        for i in range(1, NUM_ITERS + 1):
            xi, yi = coords[i]
            new_point = _to_screen(xi, yi)

            # ── Sub-step A: Oracle reflection (flip target component) ────
            # After oracle, the target amplitude is negated.
            # In the plane, this reflects across the |s_perp> axis (negate x).
            x_prev, y_prev = coords[i - 1]
            oracle_point = _to_screen(-x_prev, y_prev)

            oracle_arrow = Arrow(
                PLANE_CENTER, oracle_point,
                color=RED_C, buff=0, stroke_width=2.5,
            )
            oracle_note = Text(
                f"Step {i}a: Oracle (flip target amp)",
                font_size=18, color=RED_C,
            )
            oracle_note.to_edge(DOWN, buff=0.4)

            self.play(Write(oracle_note), run_time=0.4)
            self.play(
                Transform(current_arrow.copy(), oracle_arrow),
                run_time=0.8,
            )
            self.wait(0.4)

            # ── Sub-step B: Diffusion reflection ─────────────────────────
            color = iter_colors[(i - 1) % len(iter_colors)]
            new_arrow = Arrow(
                PLANE_CENTER, new_point,
                color=color, buff=0, stroke_width=3,
            )

            diffusion_note = Text(
                f"Step {i}b: Diffusion (reflect about |s>)",
                font_size=18, color=BLUE_C,
            )
            diffusion_note.to_edge(DOWN, buff=0.4)

            new_iter_label = Text(f"Iteration {i}", font_size=22, color=GREY_B)
            new_iter_label.move_to(iter_label)

            self.play(
                FadeOut(oracle_note),
                Write(diffusion_note),
                run_time=0.3,
            )
            self.play(
                ReplacementTransform(oracle_arrow, new_arrow),
                prob_tracker.animate.set_value(float(probs[i])),
                Transform(iter_label, new_iter_label),
                run_time=1.0,
            )

            # Fade out the old arrow, keep the new one
            if current_label_mob is not None:
                self.play(FadeOut(current_label_mob), run_time=0.3)
                current_label_mob = None

            self.play(FadeOut(diffusion_note), run_time=0.3)
            current_arrow = new_arrow
            self.wait(0.3)

        # ── Highlight final state near |target> ─────────────────────────
        final_note = Text(
            f"After {NUM_ITERS} iterations: P(target) = {float(probs[NUM_ITERS]):.3f}",
            font_size=24,
            color=GREEN_C,
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(final_note))
        self.wait(2)

        # ── Takeaway ────────────────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects])

        takeaway = VGroup(
            Text("Key Insight", font_size=34, color=YELLOW),
            Text(
                "Grover's algorithm amplifies the target amplitude via two reflections.",
                font_size=24,
            ),
            Text(
                "Oracle: reflects across the subspace orthogonal to |target>.",
                font_size=22,
                color=RED_C,
            ),
            Text(
                "Diffusion: reflects about the uniform superposition |s>.",
                font_size=22,
                color=BLUE_C,
            ),
            Text(
                "Each pair of reflections is a rotation toward |target>.",
                font_size=22,
                color=GREEN_C,
            ),
            MathTex(
                r"\text{Optimal iterations} \approx \frac{\pi}{4}\sqrt{N}",
                font_size=28,
                color=GREY_B,
            ),
        ).arrange(DOWN, buff=0.3)

        self.play(Write(takeaway), run_time=2.5)
        self.wait(3)
        self.play(FadeOut(takeaway))
