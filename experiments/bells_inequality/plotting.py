"""Visualization for Bell's inequality experiments.

Matplotlib plots for Experiments 1 & 2, Plotly HTML for Experiment 3.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from experiments.bells_inequality.config import (
    COLORS, PLOT_DEFAULTS, CLASSICAL_BOUND, TSIRELSON_BOUND, OPTIMAL_ANGLES,
)


def _apply_style():
    sns.set_theme(style="darkgrid", palette="muted", rc={
        "figure.facecolor": "#1e1e1e",
        "axes.facecolor": "#2a2a2a",
        "axes.edgecolor": "#555555",
        "grid.color": "#3a3a3a",
        "text.color": "#e0e0e0",
        "axes.labelcolor": "#e0e0e0",
        "xtick.color": "#cccccc",
        "ytick.color": "#cccccc",
        "font.family": "sans-serif",
        "font.size": 12,
    })


# ── Experiment 1: Exhaustion histogram ────────────────────────────────

def plot_exhaustion(exhaustion_data, output_path=None):
    """Plot distribution of |S| across all LHV implementations.

    Shows histogram of |S| values for deterministic, random discrete,
    random continuous, and adversarial strategies, with classical bound
    and Tsirelson bound marked.
    """
    _apply_style()
    fig, ax = plt.subplots(figsize=(12, 7))

    # Collect |S| values
    det_S = np.abs(exhaustion_data["deterministic"])
    disc_S = np.abs(exhaustion_data["random_discrete"])
    cont_S = np.abs(exhaustion_data["random_continuous"])
    adv_S = exhaustion_data["adversarial"]  # already |S|

    # Histogram of random strategies — bins end at exactly the classical bound
    # so no bar visually extends past the |S|=2 dashed line
    bins = np.linspace(0, CLASSICAL_BOUND, 50)
    ax.hist(disc_S, bins=bins, alpha=0.5, color=COLORS["random_discrete"],
            label=f"Random discrete (n={len(disc_S)})", density=True)
    ax.hist(cont_S, bins=bins, alpha=0.5, color=COLORS["random_continuous"],
            label=f"Random continuous (n={len(cont_S)})", density=True)

    # Deterministic strategies as markers on x-axis
    ax.scatter(det_S, np.zeros_like(det_S) + 0.05, color=COLORS["deterministic"],
               marker="|", s=200, linewidths=2, zorder=5,
               label=f"Deterministic (all 16)")

    # Adversarial best values as markers
    ax.scatter(adv_S, np.zeros_like(adv_S) + 0.15, color=COLORS["adversarial"],
               marker="^", s=60, zorder=5,
               label=f"Adversarial optimized (n={len(adv_S)})")

    # Classical bound
    ax.axvline(CLASSICAL_BOUND, color=COLORS["bound_classical"],
               linestyle="--", linewidth=2, label=f"|S| = {CLASSICAL_BOUND} (classical bound)")

    # Tsirelson bound for reference
    ax.axvline(TSIRELSON_BOUND, color=COLORS["bound_tsirelson"],
               linestyle=":", linewidth=2,
               label=f"|S| = {TSIRELSON_BOUND:.3f} (Tsirelson bound)")

    ax.set_xlabel("|S| (CHSH value)", fontsize=14)
    ax.set_ylabel("Density", fontsize=14)
    ax.set_title("Exhausting the LHV Type: No Implementation Exceeds |S| = 2",
                 fontsize=15, fontweight="bold", pad=15)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.8)
    ax.set_xlim(0, 2.5)

    plt.tight_layout()
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=PLOT_DEFAULTS["dpi"],
                    facecolor=fig.get_facecolor(), bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ── Experiment 2: Quantum convergence ─────────────────────────────────

def plot_quantum_convergence(quantum_data, output_path=None):
    """Plot convergence of simulated S toward theoretical value.

    Shows S estimate vs number of measurement trials, with classical
    and Tsirelson bounds marked.
    """
    _apply_style()
    fig, ax = plt.subplots(figsize=(12, 7))

    n_trials = quantum_data["convergence_n"]
    S_vals = quantum_data["convergence_S"]
    S_theory = quantum_data["theoretical_S"]

    ax.plot(n_trials, S_vals, color=COLORS["quantum"], linewidth=1.5,
            alpha=0.8, label="Simulated S")

    # Theoretical value
    ax.axhline(S_theory, color=COLORS["quantum"], linestyle="--",
               linewidth=2, alpha=0.6,
               label=f"Theoretical S = {S_theory:.4f}")

    # Classical bound
    ax.axhline(-CLASSICAL_BOUND, color=COLORS["bound_classical"],
               linestyle="--", linewidth=2,
               label=f"Classical bound |S| = {CLASSICAL_BOUND}")

    # Tsirelson bound
    ax.axhline(-TSIRELSON_BOUND, color=COLORS["bound_tsirelson"],
               linestyle=":", linewidth=2,
               label=f"Tsirelson bound |S| = {TSIRELSON_BOUND:.3f}")

    # Shade violation region
    ax.axhspan(-3.0, -CLASSICAL_BOUND, color=COLORS["violation"], alpha=0.15)
    ax.annotate("Violation region\n(impossible for LHV)",
                xy=(n_trials[len(n_trials) // 3], -2.4),
                fontsize=11, color="#e0e0e0", ha="center",
                fontstyle="italic")

    ax.set_xscale("log")
    ax.set_xlabel("Number of measurement trials", fontsize=14)
    ax.set_ylabel("S (CHSH value)", fontsize=14)
    ax.set_title("Quantum CHSH Violation: Singlet State at Optimal Angles",
                 fontsize=15, fontweight="bold", pad=15)
    ax.legend(loc="lower right", fontsize=10, framealpha=0.8)
    ax.set_ylim(-3.2, -1.5)

    plt.tight_layout()
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=PLOT_DEFAULTS["dpi"],
                    facecolor=fig.get_facecolor(), bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ── Intuition: Quantum vs classical disagreement curves ───────────────

def plot_disagreement_curves(output_path=None):
    """Plot P(disagree) vs angle for quantum sin²(Δθ) and the classical bound.

    Shows that the quantum curve bows outward while any instruction-card
    model is bounded by a linear (or inward-bowing) envelope.
    """
    _apply_style()
    fig, ax = plt.subplots(figsize=(10, 6))

    theta_deg = np.linspace(0, 90, 500)
    theta_rad = np.radians(theta_deg)

    # Quantum prediction: P(disagree) = sin²(Δθ)
    p_quantum = np.sin(theta_rad) ** 2

    # Classical upper bound: linear interpolation (best any card model can do)
    p_classical = theta_deg / 90.0

    # Plot curves
    ax.plot(theta_deg, p_quantum, color=COLORS["quantum"], linewidth=2.5,
            label=r"Quantum: $\sin^2(\Delta\theta)$", zorder=5)
    ax.plot(theta_deg, p_classical, color=COLORS["classical"], linewidth=2.5,
            linestyle="--", label="Classical maximum (linear)", zorder=4)

    # Shade the gap
    ax.fill_between(theta_deg, p_classical, p_quantum,
                    where=(p_quantum > p_classical),
                    color=COLORS["violation"], alpha=0.18,
                    label="Quantum excess (violation region)")

    # Mark the three key angles from the blog post
    for deg, label_offset in [(30, (8, 8)), (60, (8, -14))]:
        rad = np.radians(deg)
        pq = np.sin(rad) ** 2
        pc = deg / 90.0
        ax.plot(deg, pq, "o", color=COLORS["quantum"], markersize=8, zorder=6)
        ax.plot(deg, pc, "s", color=COLORS["classical"], markersize=8, zorder=6)
        ax.annotate(f"{deg}°: QM = {pq:.2f}, classical ≤ {pc:.2f}",
                    xy=(deg, pq), xytext=label_offset,
                    textcoords="offset points", fontsize=10,
                    color="#e0e0e0", ha="left",
                    arrowprops=dict(arrowstyle="-", color="#888888", lw=0.8))

    ax.set_xlabel(r"Polarizer angle difference $\Delta\theta$ (degrees)", fontsize=13)
    ax.set_ylabel(r"$P(\mathrm{disagree})$", fontsize=13)
    ax.set_title("Why Instruction Cards Fail: Quantum Correlations Bow Outward",
                 fontsize=14, fontweight="bold", pad=15)
    ax.legend(loc="upper left", fontsize=10, framealpha=0.8)
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 1.05)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90])

    plt.tight_layout()
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=PLOT_DEFAULTS["dpi"],
                    facecolor=fig.get_facecolor(), bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ── Experiment 3: Interactive CHSH sweep (Plotly HTML) ────────────────

def generate_interactive_html(output_path):
    """Generate a self-contained HTML file with interactive CHSH angle sweep.

    Uses Plotly.js loaded from CDN. Four sliders control measurement
    angles; the plot updates via client-side JavaScript.
    """
    html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interactive CHSH Angle Sweep</title>
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #1e1e1e; color: #e0e0e0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    padding: 20px; max-width: 900px; margin: 0 auto;
  }
  h2 { margin-bottom: 10px; font-size: 1.3em; }
  .controls {
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 12px 24px; margin-bottom: 20px; padding: 16px;
    background: #2a2a2a; border-radius: 8px;
  }
  .control-group { display: flex; flex-direction: column; }
  .control-group label { font-size: 0.9em; margin-bottom: 4px; color: #aaa; }
  .control-group .value { font-weight: bold; color: #e0e0e0; font-size: 1.05em; }
  input[type=range] {
    width: 100%; accent-color: #CC6666; cursor: pointer;
  }
  .readout {
    display: flex; justify-content: space-around; margin-bottom: 16px;
    padding: 12px; background: #2a2a2a; border-radius: 8px;
    font-size: 1.1em;
  }
  .readout .label { color: #aaa; }
  .readout .val { font-weight: bold; font-size: 1.3em; margin-top: 4px; }
  .quantum { color: #CC6666; }
  .classical { color: #6699CC; }
  .tsirelson { color: #66CC99; }
  #plot { width: 100%; height: 420px; }
</style>
</head>
<body>

<h2>CHSH Angle Sweep: Quantum vs Classical</h2>

<div class="readout">
  <div style="text-align:center">
    <div class="label">Quantum |S|</div>
    <div class="val quantum" id="s-quantum">2.828</div>
  </div>
  <div style="text-align:center">
    <div class="label">Classical Bound</div>
    <div class="val classical">2.000</div>
  </div>
  <div style="text-align:center">
    <div class="label">Tsirelson Bound</div>
    <div class="val tsirelson">2.828</div>
  </div>
</div>

<div class="controls">
  <div class="control-group">
    <label>Alice a&#8321;: <span class="value" id="v-a1">0</span>&deg;</label>
    <input type="range" id="a1" min="0" max="360" value="0" step="1">
  </div>
  <div class="control-group">
    <label>Alice a&#8322;: <span class="value" id="v-a2">90</span>&deg;</label>
    <input type="range" id="a2" min="0" max="360" value="90" step="1">
  </div>
  <div class="control-group">
    <label>Bob b&#8321;: <span class="value" id="v-b1">45</span>&deg;</label>
    <input type="range" id="b1" min="0" max="360" value="45" step="1">
  </div>
  <div class="control-group">
    <label>Bob b&#8322;: <span class="value" id="v-b2">135</span>&deg;</label>
    <input type="range" id="b2" min="0" max="360" value="135" step="1">
  </div>
</div>

<div id="plot"></div>

<script>
const DEG = Math.PI / 180;

function E_quantum(a, b) { return -Math.cos(a - b); }

function chsh(a1, a2, b1, b2) {
  return E_quantum(a1, b1) - E_quantum(a1, b2) + E_quantum(a2, b1) + E_quantum(a2, b2);
}

// Sweep b1 from 0 to 360 while keeping other angles fixed
function computeSweep(a1, a2, b2) {
  const theta = [], qS = [];
  for (let d = 0; d <= 360; d += 1) {
    const b1 = d * DEG;
    theta.push(d);
    qS.push(Math.abs(chsh(a1, a2, b1, b2)));
  }
  return { theta, qS };
}

const layout = {
  paper_bgcolor: '#1e1e1e', plot_bgcolor: '#2a2a2a',
  font: { color: '#e0e0e0' },
  xaxis: { title: 'Bob b\u2081 angle (\u00B0)', gridcolor: '#3a3a3a',
           range: [0, 360] },
  yaxis: { title: '|S|', gridcolor: '#3a3a3a', range: [0, 3.2] },
  margin: { t: 30, b: 50, l: 60, r: 30 },
  showlegend: true,
  legend: { x: 0.02, y: 0.98, bgcolor: 'rgba(42,42,42,0.8)' },
};

function getAngles() {
  return {
    a1: +document.getElementById('a1').value * DEG,
    a2: +document.getElementById('a2').value * DEG,
    b1: +document.getElementById('b1').value * DEG,
    b2: +document.getElementById('b2').value * DEG,
  };
}

function update() {
  const a = getAngles();
  const a1d = +document.getElementById('a1').value;
  const a2d = +document.getElementById('a2').value;
  const b1d = +document.getElementById('b1').value;
  const b2d = +document.getElementById('b2').value;

  document.getElementById('v-a1').textContent = a1d;
  document.getElementById('v-a2').textContent = a2d;
  document.getElementById('v-b1').textContent = b1d;
  document.getElementById('v-b2').textContent = b2d;

  const S = Math.abs(chsh(a.a1, a.a2, a.b1, a.b2));
  const el = document.getElementById('s-quantum');
  el.textContent = S.toFixed(3);
  el.style.color = S > 2.0 ? '#CC6666' : '#6699CC';

  const sweep = computeSweep(a.a1, a.a2, a.b2);

  const traces = [
    // Quantum sweep curve
    { x: sweep.theta, y: sweep.qS, mode: 'lines',
      line: { color: '#CC6666', width: 2.5 },
      name: 'Quantum |S| (sweep b\u2081)' },
    // Classical bound
    { x: [0, 360], y: [2, 2], mode: 'lines',
      line: { color: '#FFFFFF', width: 2, dash: 'dash' },
      name: 'Classical bound (|S| = 2)' },
    // Tsirelson bound
    { x: [0, 360], y: [2.828, 2.828], mode: 'lines',
      line: { color: '#66CC99', width: 2, dash: 'dot' },
      name: 'Tsirelson bound (2\u221A2)' },
    // Current position marker
    { x: [b1d], y: [S], mode: 'markers',
      marker: { color: '#CC6666', size: 12, symbol: 'diamond',
                line: { color: '#fff', width: 2 } },
      name: 'Current setting', showlegend: false },
  ];

  Plotly.react('plot', traces, layout, { responsive: true });
}

['a1', 'a2', 'b1', 'b2'].forEach(id => {
  document.getElementById(id).addEventListener('input', update);
});
update();
</script>
</body>
</html>"""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")
    print(f"  Interactive plot saved: {output_path}")
    return output_path


def save_all_plots(exhaustion_data, quantum_data, img_dir, plot_dir):
    """Save all plots for the Bell's inequality experiments."""
    saved = []

    if exhaustion_data is not None:
        p = Path(img_dir) / "lhv_exhaustion.png"
        plot_exhaustion(exhaustion_data, output_path=p)
        saved.append(str(p))
        plt.close("all")

    if quantum_data is not None:
        p = Path(img_dir) / "quantum_convergence.png"
        plot_quantum_convergence(quantum_data, output_path=p)
        saved.append(str(p))
        plt.close("all")

    # Disagreement curves (no simulation data needed)
    p = Path(img_dir) / "disagreement_curves.png"
    plot_disagreement_curves(output_path=p)
    saved.append(str(p))
    plt.close("all")

    # Always generate interactive HTML
    p = Path(plot_dir) / "chsh_sweep.html"
    generate_interactive_html(p)
    saved.append(str(p))

    return saved
