"""Visualization for Money-Minsky-Policy-Mismatch experiments."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import FancyBboxPatch

from experiments.money_minsky_policy_mismatch.config import (
    COLORS,
    KEEN_CRISIS_THRESHOLD,
    PLOT_DEFAULTS,
)


def _apply_style():
    """Apply consistent dark theme."""
    matplotlib.rcParams.update({
        "figure.facecolor": "#1e1e1e",
        "axes.facecolor": "#2a2a2a",
        "axes.edgecolor": "#555555",
        "axes.grid": True,
        "grid.color": "#3a3a3a",
        "text.color": "#e0e0e0",
        "axes.labelcolor": "#e0e0e0",
        "xtick.color": "#cccccc",
        "ytick.color": "#cccccc",
        "font.family": "sans-serif",
        "font.size": 12,
    })


def _add_box(ax, x, y, width, height, title, lines, facecolor):
    """Draw a rounded text box for conceptual diagrams."""
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.025",
        linewidth=1.5,
        edgecolor="#777777",
        facecolor=facecolor,
    )
    ax.add_patch(patch)
    ax.text(
        x + 0.02,
        y + height - 0.04,
        title,
        fontsize=13,
        fontweight="bold",
        va="top",
        ha="left",
        color="#f4f4f4",
    )
    ax.text(
        x + 0.02,
        y + height - 0.10,
        "\n".join(lines),
        fontsize=10,
        va="top",
        ha="left",
        color="#e0e0e0",
        linespacing=1.5,
    )


def plot_constraint_hierarchy(output_path=None):
    """Concept diagram: different entity types face different constraint sets."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(14, 6), dpi=PLOT_DEFAULTS["dpi"])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.95,
        "Different Entities Face Different Constraint Sets",
        fontsize=16,
        fontweight="bold",
        ha="center",
        va="top",
        color="#f4f4f4",
    )
    ax.text(
        0.5,
        0.89,
        "The useful first question is not 'is the budget prudent?' but 'what kind of entity is this?'",
        fontsize=11,
        ha="center",
        va="top",
        color="#cccccc",
    )

    _add_box(
        ax,
        0.04,
        0.18,
        0.27,
        0.58,
        "Currency user",
        [
            "Examples: household, firm, city, U.S. state",
            "",
            "Must obtain the currency before spending.",
            "Direct constraints:",
            "- income and cash flow",
            "- collateral and credit access",
            "- legal borrowing limits",
            "",
            "Best diagnostic variable:",
            "revenue and funding access",
        ],
        "#243447",
    )
    _add_box(
        ax,
        0.365,
        0.18,
        0.27,
        0.58,
        "Quasi-sovereign",
        [
            "Examples: euro-area government",
            "",
            "Has state powers but not full monetary control",
            "over the currency it spends.",
            "Direct constraints:",
            "- refinancing pressure",
            "- borrowing spreads",
            "- institutional rules and backstops",
            "",
            "Best diagnostic variable:",
            "market access plus system slack",
        ],
        "#3b2f48",
    )
    _add_box(
        ax,
        0.69,
        0.18,
        0.27,
        0.58,
        "Sovereign issuer",
        [
            "Examples: floating-currency national state",
            "",
            "Issues the unit it spends in.",
            "Direct constraints:",
            "- inflation and real capacity",
            "- imported essentials and external dependence",
            "- political or legal self-constraints",
            "- private-sector fragility",
            "",
            "Best diagnostic variable:",
            "unused resources and bottlenecks",
        ],
        "#244233",
    )

    ax.text(
        0.5,
        0.08,
        "Policy mismatch begins when all three positions are treated as if they obey the same household rule.",
        fontsize=11,
        ha="center",
        va="center",
        color="#dddddd",
    )

    fig.tight_layout()
    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


def plot_campaign_vs_operational_models(output_path=None):
    """Concept diagram: campaign rhetoric versus institutional operations."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(14, 6), dpi=PLOT_DEFAULTS["dpi"])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.95,
        "Two Models of the Same Economy",
        fontsize=16,
        fontweight="bold",
        ha="center",
        va="top",
        color="#f4f4f4",
    )
    ax.text(
        0.5,
        0.89,
        "Campaign language often uses a household-budget story while monetary institutions already manage a balance-sheet system.",
        fontsize=11,
        ha="center",
        va="top",
        color="#cccccc",
    )

    _add_box(
        ax,
        0.07,
        0.22,
        0.38,
        0.56,
        "Campaign model: household budget",
        [
            "Government must 'find the money' first.",
            "Deficit is treated as the main health signal.",
            "Cuts are coded as discipline by default.",
            "Public debt is narrated like family debt.",
            "Taxes are framed as funding before spending.",
            "",
            "Political style:",
            "moral language, thrift, belt-tightening",
        ],
        "#4a2d2d",
    )
    _add_box(
        ax,
        0.55,
        0.22,
        0.38,
        0.56,
        "Operational model: balance-sheet system",
        [
            "Banks create deposits when they lend.",
            "Treasury and central bank manage settlement.",
            "Automatic stabilizers move with output.",
            "Crisis policy backstops funding and incomes.",
            "Reserves, spreads, and liquidity matter.",
            "",
            "Operational style:",
            "cash flow, plumbing, buffers, and constraints",
        ],
        "#203d4b",
    )

    ax.text(
        0.5,
        0.10,
        "The tension is historical, not hypothetical: crisis management is usually run with the right plumbing model even when elections revert to household metaphors.",
        fontsize=11,
        ha="center",
        va="center",
        color="#dddddd",
    )

    fig.tight_layout()
    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


def plot_wrong_target_control(output_path=None):
    """Concept diagram: wrong-target austerity versus state-target stabilization."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(14, 6), dpi=PLOT_DEFAULTS["dpi"])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.95,
        "Control Logic in a Slump",
        fontsize=16,
        fontweight="bold",
        ha="center",
        va="top",
        color="#f4f4f4",
    )
    ax.text(
        0.5,
        0.89,
        "Austerity often targets the budget indicator directly. Stabilization targets the system state first.",
        fontsize=11,
        ha="center",
        va="top",
        color="#cccccc",
    )

    left_x = 0.14
    right_x = 0.55
    box_w = 0.34
    box_h = 0.12
    y_positions = [0.70, 0.52, 0.34, 0.16]

    left_boxes = [
        ("Wrong target: lower deficit now", "#4a2d2d"),
        ("Policy: cut spending or raise taxes", "#5a3b2b"),
        ("System effect: lower output and income", "#55302d"),
        ("Feedback: tax base shrinks,\nstabilizers rise", "#4a2d2d"),
    ]
    right_boxes = [
        ("Right target: stabilize output\nand employment", "#244233"),
        ("Policy: support demand\nwhile slack is high", "#2d4b35"),
        ("System effect: income and\ncapacity recover", "#244233"),
        ("Later effect: budget can improve\nwith recovery", "#2d4b35"),
    ]

    def _control_box(ax, x, y, w, h, title, facecolor):
        """Draw a box with center-aligned title text for the control diagram."""
        patch = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.02,rounding_size=0.025",
            linewidth=1.5, edgecolor="#777777", facecolor=facecolor,
        )
        ax.add_patch(patch)
        ax.text(
            x + w / 2.0, y + h / 2.0, title,
            fontsize=11, fontweight="bold", va="center", ha="center",
            color="#f4f4f4", linespacing=1.4,
        )

    for (title, color), y in zip(left_boxes, y_positions):
        _control_box(ax, left_x, y, box_w, box_h, title, color)
    for (title, color), y in zip(right_boxes, y_positions):
        _control_box(ax, right_x, y, box_w, box_h, title, color)

    # Downward arrows between boxes in each column
    for x_center in (left_x + box_w / 2.0, right_x + box_w / 2.0):
        for y_top, y_bottom in zip(y_positions[:-1], y_positions[1:]):
            ax.annotate(
                "",
                xy=(x_center, y_bottom + box_h),
                xytext=(x_center, y_top),
                arrowprops=dict(arrowstyle="->", color="#dddddd", lw=1.5),
            )

    # Feedback loop arrow: arcs from bottom-left box back up to top-left box
    # Place the arc to the LEFT of the left column so it doesn't overlap boxes
    loop_x = left_x - 0.02
    ax.annotate(
        "",
        xy=(loop_x, y_positions[0] + box_h),
        xytext=(loop_x, y_positions[-1]),
        arrowprops=dict(
            arrowstyle="->",
            color=COLORS["austerity"],
            lw=1.8,
            connectionstyle="arc3,rad=-0.50",
        ),
    )
    ax.text(
        left_x - 0.11,
        0.50,
        "looped\npressure",
        fontsize=9,
        color=COLORS["austerity"],
        rotation=90,
        ha="center",
        va="center",
    )

    fig.tight_layout()
    if output_path:
        fig.savefig(output_path, bbox_inches="tight", pad_inches=0.15)
        print(f"  Plot saved: {output_path}")
    return fig


def plot_policy_sectoral_paths(policy_data, output_path=None):
    """Compare output, tax revenue, and debt ratio across policy paths."""
    _apply_style()
    fig, axes = plt.subplots(3, 1, figsize=PLOT_DEFAULTS["figsize"],
                             dpi=PLOT_DEFAULTS["dpi"], sharex=True)

    scenario_order = [
        ("supportive", COLORS["functional_finance"], "Supportive"),
        ("austerity", COLORS["austerity"], "Immediate austerity"),
        ("delayed_repair", COLORS["issuer"], "Delayed repair"),
    ]
    shock_start = policy_data["shock_start"]

    for key, color, label in scenario_order:
        data = policy_data[key]
        t = np.arange(len(data["Y"]))
        axes[0].plot(t, data["Y"], color=color, lw=1.5, label=label)
        axes[1].plot(t, data["T"], color=color, lw=1.5, label=label)
        axes[2].plot(t, data["debt_ratio"], color=color, lw=1.5, label=label)

    for ax in axes:
        ax.axvline(shock_start, color="#bbbbbb", ls="--", lw=0.8, alpha=0.8)

    axes[0].set_ylabel("Output")
    axes[0].legend(fontsize=9)
    axes[1].set_ylabel("Tax revenue")
    axes[2].set_ylabel("Debt / output")
    axes[2].set_xlabel("Period")

    fig.suptitle("Sectoral Policy Model: Same Demand Shock, Different Fiscal Paths",
                 fontsize=14, color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


def plot_policy_sectoral_balances(policy_data, scenario="austerity", output_path=None):
    """Show the three-sector identity for one scenario."""
    _apply_style()
    fig, axes = plt.subplots(2, 1, figsize=PLOT_DEFAULTS["figsize"],
                             dpi=PLOT_DEFAULTS["dpi"], sharex=True)

    data = policy_data[scenario]
    t = np.arange(len(data["Y"]))
    private_balance = np.array(data["private_balance"])
    government_balance = np.array(data["government_balance"])
    foreign_balance = np.array(data["foreign_balance"])
    residual = private_balance + government_balance + foreign_balance

    axes[0].plot(t, private_balance, color=COLORS["hedge"], lw=1.5, label="Private")
    axes[0].plot(t, government_balance, color=COLORS["austerity"], lw=1.5, label="Government")
    axes[0].plot(t, foreign_balance, color=COLORS["output"], lw=1.5, label="Foreign")
    axes[0].axhline(0, color="#666666", lw=0.5)
    axes[0].set_ylabel("Sector balance")
    axes[0].legend(fontsize=9)

    axes[1].plot(t, residual, color="#ffffff", lw=1.0)
    axes[1].set_ylabel("Residual")
    axes[1].set_xlabel("Period")
    axes[1].ticklabel_format(style="sci", axis="y", scilimits=(-3, 3))

    fig.suptitle(f"Three-Sector Identity ({scenario.replace('_', ' ').title()})",
                 fontsize=14, color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


def plot_imf_counterfactual_cases(counterfactual_data, output_path=None):
    """Compare observed vs delayed consolidation in Spain and the UK."""
    _apply_style()
    fig, axes = plt.subplots(2, 2, figsize=(14, 8), dpi=PLOT_DEFAULTS["dpi"],
                             sharex="col")

    for row, country in enumerate(["ESP", "GBR"]):
        case = counterfactual_data["cases"][country]
        years = case["years"]
        observed = case["observed"]
        delayed = case["delayed"]

        axes[row, 0].plot(years, observed["gdp_index"], color=COLORS["austerity"],
                          lw=1.8, label="Observed consolidation")
        axes[row, 0].plot(years, delayed["gdp_index"], color=COLORS["functional_finance"],
                          lw=1.8, label="Delayed consolidation")
        axes[row, 0].set_ylabel(f"{case['country_name']}\nGDP index")
        axes[row, 0].legend(fontsize=8)

        axes[row, 1].plot(years, observed["debt_ratio"], color=COLORS["austerity"],
                          lw=1.8, label="Observed consolidation")
        axes[row, 1].plot(years, delayed["debt_ratio"], color=COLORS["functional_finance"],
                          lw=1.8, label="Delayed consolidation")
        actual_debt = case.get("actual_debt_ratio")
        if actual_debt:
            axes[row, 1].scatter(years, actual_debt, color="#dddddd", s=18,
                                 alpha=0.7, label="Actual debt ratio")
        axes[row, 1].set_ylabel(f"{case['country_name']}\nDebt / GDP")
        axes[row, 1].legend(fontsize=8)

    axes[1, 0].set_xlabel("Year")
    axes[1, 1].set_xlabel("Year")
    fig.suptitle("IMF Action-Based Austerity Paths Under Alternative Timing",
                 fontsize=14, color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


def plot_fragility_regime_comparison(fragility_data, output_path=None):
    """Compare crisis timing under fragile vs resilient calibrations."""
    _apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), dpi=PLOT_DEFAULTS["dpi"],
                             sharey=True, constrained_layout=True)

    extent = [
        fragility_data["initial_d"][0],
        fragility_data["initial_d"][-1],
        fragility_data["delta_r"][0],
        fragility_data["delta_r"][-1],
    ]
    for ax, key, title in [
        (axes[0], "fragile", "Fragile calibration"),
        (axes[1], "resilient", "Resilient calibration"),
    ]:
        grid = np.array(fragility_data[key]["grid"])
        im = ax.imshow(grid, aspect="auto", origin="lower",
                       cmap="RdYlGn_r", extent=extent)
        ax.set_title(title, fontsize=13, color="#e0e0e0")
        ax.set_xlabel("Initial debt ratio")
    axes[0].set_ylabel("Rate shock")
    fig.colorbar(im, ax=axes.ravel().tolist(), label="Time to crisis")
    fig.suptitle("Fragility Regimes: The Same Tightening Has Different Effects",
                 fontsize=14, color="#e0e0e0")

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# NEW: Keen ODE — stable limit cycle vs crisis (side-by-side)
# ---------------------------------------------------------------------------

def plot_keen_stable_vs_crisis(stable_dict, crisis_dict, output_path=None):
    """Two Keen ODE trajectories side-by-side: stable and crisis.

    Left column: stable limit cycle (low initial debt).
    Right column: crisis — debt explodes (high initial debt).
    Shows FIH Theorems 1 (stable regime exists) and 2 (stability breeds instability).
    """
    _apply_style()
    fig, axes = plt.subplots(3, 2, figsize=(14, 9), dpi=PLOT_DEFAULTS["dpi"],
                              sharex="col")

    for col, (data, label) in enumerate([
        (stable_dict, "Stable regime"),
        (crisis_dict, "Crisis regime"),
    ]):
        t = np.array(data["t"])
        axes[0, col].plot(t, data["omega"], color=COLORS["wage_share"], lw=1.5)
        axes[0, col].set_ylabel("Wage share (\u03c9)")
        axes[0, col].set_ylim(0, 1)
        axes[0, col].set_title(label, fontsize=13, color="#e0e0e0")

        axes[1, col].plot(t, data["lam"], color=COLORS["employment"], lw=1.5)
        axes[1, col].set_ylabel("Employment (\u03bb)")
        axes[1, col].set_ylim(0, 1)

        d = np.array(data["d"])
        axes[2, col].plot(t, d, color=COLORS["debt"], lw=1.5)
        axes[2, col].axhline(KEEN_CRISIS_THRESHOLD, color=COLORS["ponzi"],
                              ls="--", alpha=0.7, label="Crisis threshold")
        axes[2, col].set_ylabel("Debt ratio (d)")
        axes[2, col].set_xlabel("Time")
        if col == 1:
            # Shade crisis zone
            crisis_mask = d > KEEN_CRISIS_THRESHOLD
            if np.any(crisis_mask):
                axes[2, col].fill_between(
                    t, KEEN_CRISIS_THRESHOLD, d,
                    where=crisis_mask, alpha=0.2, color=COLORS["ponzi"],
                )
        axes[2, col].legend(fontsize=9)

    fig.suptitle("Keen-Minsky: Stability vs Instability", fontsize=15,
                 color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# NEW: Sectoral balances — visual proof of identity
# ---------------------------------------------------------------------------

def plot_sectoral_balances(sfc_data, output_path=None):
    """Line chart showing FB_priv + FB_gov = 0 every period."""
    _apply_style()
    fig, axes = plt.subplots(2, 1, figsize=PLOT_DEFAULTS["figsize"],
                              dpi=PLOT_DEFAULTS["dpi"], sharex=True)

    t = np.arange(len(sfc_data["Y"]))
    YD = np.array(sfc_data["YD"])
    C = np.array(sfc_data["C"])
    Pi = np.array(sfc_data["Pi"])
    I = np.array(sfc_data["I"])
    T = np.array(sfc_data["T"])
    G_eff = np.array(sfc_data["G_eff"])
    interest = np.array(sfc_data["interest_expense"])

    fb_priv = (YD - C) + (Pi - I)
    fb_gov = T - G_eff - interest

    # Panel 1: sectoral balances
    axes[0].plot(t, fb_priv, color=COLORS["hedge"], lw=1.5, label="Private sector")
    axes[0].plot(t, fb_gov, color=COLORS["austerity"], lw=1.5, label="Government")
    axes[0].axhline(0, color="#666666", ls="-", lw=0.5)
    axes[0].set_ylabel("Financial balance")
    axes[0].legend(fontsize=10)

    # Panel 2: residual (should be zero)
    residual = fb_priv + fb_gov
    axes[1].plot(t, residual, color="#ffffff", lw=1.0)
    axes[1].set_ylabel("Residual (FB_priv + FB_gov)")
    axes[1].set_xlabel("Period")
    axes[1].ticklabel_format(style="sci", axis="y", scilimits=(-3, 3))

    fig.suptitle("Sectoral Balance Identity: Private + Government = 0",
                 fontsize=14, color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# NEW: Austerity Minsky shift — baseline vs austerity distribution
# ---------------------------------------------------------------------------

def plot_austerity_minsky_shift(abm_baseline, abm_austerity, output_path=None):
    """Side-by-side stacked area: Minsky distribution baseline vs austerity."""
    _apply_style()
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), dpi=PLOT_DEFAULTS["dpi"],
                              sharey=True)

    for col, (data, label) in enumerate([
        (abm_baseline, "Baseline (no austerity)"),
        (abm_austerity, "With austerity"),
    ]):
        t = np.arange(len(data["hedge_share"]))
        hedge = np.array(data["hedge_share"])
        spec = np.array(data["speculative_share"])
        ponzi = np.array(data["ponzi_share"])

        axes[col].stackplot(t, hedge, spec, ponzi,
                             labels=["Hedge", "Speculative", "Ponzi"],
                             colors=[COLORS["hedge"], COLORS["speculative"],
                                     COLORS["ponzi"]], alpha=0.8)
        axes[col].set_title(label, fontsize=13, color="#e0e0e0")
        axes[col].set_xlabel("Period")
        axes[col].set_ylim(0, 1)
        if col == 0:
            axes[col].set_ylabel("Share of firms")
        axes[col].legend(loc="upper right", fontsize=9)

    fig.suptitle("Austerity Shifts the Minsky Distribution Toward Fragility",
                 fontsize=14, color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# Rate hike: crisis boundary heatmap
# ---------------------------------------------------------------------------

def plot_rate_hike_grid(rate_hike_data, output_path=None):
    """Heatmap: rate shock x initial debt -> crisis time."""
    _apply_style()
    grid = np.array(rate_hike_data["grid"])
    fig, ax = plt.subplots(figsize=(10, 6), dpi=PLOT_DEFAULTS["dpi"])

    im = ax.imshow(grid, aspect="auto", origin="lower",
                   cmap="RdYlGn_r",
                   extent=[
                       rate_hike_data["initial_d"][0],
                       rate_hike_data["initial_d"][-1],
                       rate_hike_data["delta_r"][0],
                       rate_hike_data["delta_r"][-1],
                   ])
    ax.set_xlabel("Initial debt ratio (d\u2080)")
    ax.set_ylabel("Rate shock (\u0394r)")
    ax.set_title("Time to Crisis: Rate Shock x Leverage",
                 fontsize=14, color="#e0e0e0")
    fig.colorbar(im, ax=ax, label="Time to crisis (darker = sooner)")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# SFC: austerity vs baseline
# ---------------------------------------------------------------------------

def plot_sfc_austerity(sfc_baseline, sfc_austerity, output_path=None):
    """Side-by-side: output and deficit under baseline vs austerity."""
    _apply_style()
    fig, axes = plt.subplots(2, 1, figsize=PLOT_DEFAULTS["figsize"],
                             dpi=PLOT_DEFAULTS["dpi"], sharex=True)

    t = np.arange(len(sfc_baseline["Y"]))

    axes[0].plot(t, sfc_baseline["Y"], color=COLORS["functional_finance"],
                 label="Functional finance", lw=1.5)
    axes[0].plot(t, sfc_austerity["Y"], color=COLORS["austerity"],
                 label="Austerity", lw=1.5)
    axes[0].set_ylabel("Output (Y)")
    axes[0].legend(fontsize=10)

    axes[1].plot(t, sfc_baseline["DEF"], color=COLORS["functional_finance"],
                 label="FF deficit", lw=1.5)
    axes[1].plot(t, sfc_austerity["DEF"], color=COLORS["austerity"],
                 label="Austerity deficit", lw=1.5)
    axes[1].axhline(0, color="#666666", ls="-", lw=0.5)
    axes[1].set_ylabel("Government deficit")
    axes[1].set_xlabel("Period")
    axes[1].legend(fontsize=10)

    fig.suptitle("Austerity vs Functional Finance (SFC Model)", fontsize=14,
                 color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# ABM: Minsky state distribution (stacked area)
# ---------------------------------------------------------------------------

def plot_minsky_distribution(abm_data, output_path=None):
    """Stacked area chart of hedge/speculative/Ponzi shares over time."""
    _apply_style()
    fig, ax = plt.subplots(figsize=PLOT_DEFAULTS["figsize"],
                           dpi=PLOT_DEFAULTS["dpi"])

    t = np.arange(len(abm_data["hedge_share"]))
    hedge = np.array(abm_data["hedge_share"])
    spec = np.array(abm_data["speculative_share"])
    ponzi = np.array(abm_data["ponzi_share"])

    ax.stackplot(t, hedge, spec, ponzi,
                 labels=["Hedge", "Speculative", "Ponzi"],
                 colors=[COLORS["hedge"], COLORS["speculative"], COLORS["ponzi"]],
                 alpha=0.8)
    ax.set_ylabel("Share of firms")
    ax.set_xlabel("Period")
    ax.set_ylim(0, 1)
    ax.legend(loc="upper right", fontsize=10)
    ax.set_title("Minsky Financial Fragility Distribution", fontsize=14,
                 color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# Issuer vs User
# ---------------------------------------------------------------------------

def plot_issuer_vs_user(issuer_data, user_data, output_path=None):
    """3-panel: output, effective G, sovereign rate under two regimes."""
    _apply_style()
    fig, axes = plt.subplots(3, 1, figsize=PLOT_DEFAULTS["figsize"],
                             dpi=PLOT_DEFAULTS["dpi"], sharex=True)

    t = np.arange(len(issuer_data["Y"]))

    axes[0].plot(t, issuer_data["Y"], color=COLORS["issuer"],
                 label="Currency issuer", lw=1.5)
    axes[0].plot(t, user_data["Y"], color=COLORS["user"],
                 label="Currency user", lw=1.5)
    axes[0].set_ylabel("Output (Y)")
    axes[0].legend(fontsize=10)

    axes[1].plot(t, issuer_data["G_eff"], color=COLORS["issuer"],
                 label="Issuer G", lw=1.5)
    axes[1].plot(t, user_data["G_eff"], color=COLORS["user"],
                 label="User G", lw=1.5)
    axes[1].set_ylabel("Effective spending (G)")
    axes[1].legend(fontsize=10)

    axes[2].plot(t, issuer_data["i_sovereign"], color=COLORS["issuer"],
                 label="Issuer rate", lw=1.5)
    axes[2].plot(t, user_data["i_sovereign"], color=COLORS["user"],
                 label="User rate", lw=1.5)
    axes[2].set_ylabel("Sovereign borrowing rate")
    axes[2].set_xlabel("Period")
    axes[2].legend(fontsize=10)

    fig.suptitle("Currency Issuer vs Currency User Under Fiscal Shock",
                 fontsize=14, color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# JG: unemployment + JG share comparison
# ---------------------------------------------------------------------------

def plot_jg_comparison(jg_data, output_path=None):
    """Two panels: unemployment rate and JG share across wage ratios."""
    _apply_style()
    fig, axes = plt.subplots(2, 1, figsize=PLOT_DEFAULTS["figsize"],
                              dpi=PLOT_DEFAULTS["dpi"], sharex=True)

    for ratio_str, data in sorted(jg_data.items()):
        ratio = float(ratio_str)
        label = "No JG (NAIRU)" if ratio == 0.0 else f"JG w/w\u2098={ratio:.0%}"
        color = COLORS["nairu"] if ratio == 0.0 else COLORS["jg"]
        alpha = 1.0 if ratio == 0.0 else 0.4 + 0.6 * ratio

        axes[0].plot(data["unemployment"], label=label, color=color,
                     alpha=alpha, lw=1.5)
        axes[1].plot(data["jg_share"], label=label, color=color,
                     alpha=alpha, lw=1.5)

    axes[0].set_ylabel("Unemployment rate")
    axes[0].set_ylim(0, None)
    axes[0].legend(fontsize=9)

    axes[1].set_ylabel("JG employment share")
    axes[1].set_xlabel("Period")
    axes[1].set_ylim(0, None)
    axes[1].legend(fontsize=9)

    fig.suptitle("Job Guarantee vs NAIRU: Unemployment Buffer Stock",
                 fontsize=14, color="#e0e0e0")
    fig.tight_layout()

    if output_path:
        fig.savefig(output_path, bbox_inches="tight")
        print(f"  Plot saved: {output_path}")
    return fig


# ---------------------------------------------------------------------------
# Save all plots
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# New simulation surface plots (tasks 018, 019, 020)
# ---------------------------------------------------------------------------

def plot_comparative_constraints(data: dict, output_path=None):
    """Spending, normalized activity, and debt for household / currency-user /
    sovereign-issuer under the same demand shock.

    Each entity's spending and activity are normalized to its own pre-shock
    target so the three trajectories are directly comparable on one axis,
    avoiding the apples-to-oranges scale problem (household activity vs
    GDP-via-multiplier).  Debt panel uses log scale so the household and
    issuer trajectories stay readable alongside the currency-user explosion.
    """
    from experiments.money_minsky_policy_mismatch._plot_theme import (
        themed, make_figure, style_panel, add_shock_marker, add_callout,
        polish_legend, PALETTE,
    )

    series = [
        ("household", "Household", PALETTE["household"], "-"),
        ("currency_user", "Currency user", PALETTE["currency_user"], "--"),
        ("sovereign_issuer", "Sovereign issuer", PALETTE["sovereign_issuer"], ":"),
    ]
    shock_period = data.get("shock_period", 30)

    with themed():
        fig, axes = make_figure(
            n_panels=3,
            title="Same shock, different constraints",
            subtitle="Each entity faces an identical private-demand shock at period "
                      f"{shock_period}. Their spending paths diverge because their "
                      "binding constraints differ.",
        )

        # ---- Panel 1: spending normalized to entity's own pre-shock level
        ax = axes[0]
        for key, label, color, ls in series:
            spending = np.array(data[key]["spending"])
            base = np.mean(spending[:shock_period])
            ax.plot(spending / max(base, 1e-9), color=color, linestyle=ls,
                    label=label, linewidth=2.0)
        ax.set_ylim(-0.05, 1.15)
        ax.axhline(1.0, color=PALETTE["muted"], linestyle="-",
                   linewidth=0.6, alpha=0.5)
        style_panel(ax, "Spending (normalized to pre-shock target)",
                    ylabel="Spending / target")
        add_shock_marker(ax, shock_period, "demand shock")
        polish_legend(ax, loc="lower left")

        # ---- Panel 2: real activity normalized
        ax = axes[1]
        for key, label, color, ls in series:
            output = np.array(data[key]["output"])
            base = np.mean(output[:shock_period])
            ax.plot(output / max(base, 1e-9), color=color, linestyle=ls,
                    label=label, linewidth=2.0)
        ax.set_ylim(-0.05, 1.15)
        ax.axhline(1.0, color=PALETTE["muted"], linestyle="-",
                   linewidth=0.6, alpha=0.5)
        style_panel(ax, "Activity (normalized to pre-shock level)",
                    ylabel="Activity / pre-shock")
        add_shock_marker(ax, shock_period, "demand shock")

        # ---- Panel 3: debt ratio on log scale
        ax = axes[2]
        for key, label, color, ls in series:
            ratio = np.array(data[key]["debt_ratio"]) + 0.01  # log-safe offset
            ax.plot(ratio, color=color, linestyle=ls, label=label, linewidth=2.0)
        ax.set_yscale("log")
        style_panel(ax, "Debt ratio (log scale)",
                    ylabel="Debt / income or output")
        add_shock_marker(ax, shock_period, "demand shock")

        fig.tight_layout()
        if output_path:
            fig.savefig(output_path)
        plt.close(fig)


def plot_policy_lab(data: dict, output_path=None):
    """Output, underutilization, and deficit for austerity / FF / passive controllers."""
    from experiments.money_minsky_policy_mismatch._plot_theme import (
        themed, make_figure, style_panel, polish_legend, PALETTE,
    )

    series = [
        ("austerity", "Austerity controller", PALETTE["austerity"], "-"),
        ("functional_finance", "Functional-finance controller",
         PALETTE["functional_finance"], "--"),
        ("passive", "Passive (no adjustment)", PALETTE["passive"], ":"),
    ]

    def _smooth(arr, window=7):
        a = np.asarray(arr, dtype=float)
        if len(a) < window:
            return a
        kernel = np.ones(window) / window
        # symmetric padding to avoid edge artifacts
        padded = np.pad(a, (window // 2, window // 2), mode="edge")
        return np.convolve(padded, kernel, mode="valid")[: len(a)]

    def _median_smooth(arr, window=15):
        """Median filter — robust against bang-bang oscillation."""
        a = np.asarray(arr, dtype=float)
        if len(a) < window:
            return a
        half = window // 2
        out = np.empty_like(a)
        for i in range(len(a)):
            lo = max(0, i - half)
            hi = min(len(a), i + half + 1)
            out[i] = np.median(a[lo:hi])
        return out

    with themed():
        fig, axes = make_figure(
            n_panels=3,
            title="Competing fiscal controllers under stressed conditions",
            subtitle="Same agent-based economy, three controllers. "
                      "Austerity wins on the deficit; functional finance "
                      "wins on output and underutilization. Series smoothed "
                      "with a moving average to reveal the trend.",
        )

        # ---- Panel 1: Output
        ax = axes[0]
        for key, label, color, ls in series:
            ax.plot(_smooth(data[key]["Y"]), color=color, linestyle=ls,
                    label=label, linewidth=2.0)
        style_panel(ax, "Output (real activity)", ylabel="Output")
        polish_legend(ax, loc="lower left")

        # ---- Panel 2: Underutilization (unemployment + JG share)
        ax = axes[1]
        for key, label, color, ls in series:
            jg = np.array(data[key]["jg_share"])
            unemp = np.array(data[key]["unemployment"])
            ax.plot(_smooth(jg + unemp), color=color, linestyle=ls,
                    label=label, linewidth=2.0)
        ax.set_ylim(0, 1.0)
        style_panel(ax, "Labor underutilization",
                    ylabel="Unemployed + JG share")

        # ---- Panel 3: Deficit ratio (long moving average suppresses the
        # bang-bang oscillation the austerity controller produces)
        ax = axes[2]
        for key, label, color, ls in series:
            ax.plot(_smooth(data[key]["deficit_ratio"], window=21),
                    color=color, linestyle=ls, label=label, linewidth=2.0)
        ax.axhline(0, color=PALETTE["muted"], linestyle="-",
                   linewidth=0.6, alpha=0.5)
        style_panel(ax, "Deficit / output (21-period MA)",
                    ylabel="Deficit ratio")

        fig.tight_layout()
        if output_path:
            fig.savefig(output_path)
        plt.close(fig)


def plot_capacity_constraint(slack_data: dict, tight_data: dict,
                              ramp_data: dict, output_path=None):
    """Slack vs tight capacity and the spending ramp transition."""
    from experiments.money_minsky_policy_mismatch._plot_theme import (
        themed, make_figure, style_panel, add_callout, polish_legend, PALETTE,
        FG_MUTED, FG_SPINE, BG_AXES,
    )

    with themed():
        fig, axes = make_figure(
            n_panels=3,
            title="Real constraints: spending under slack vs at capacity",
            subtitle="Below capacity: extra spending becomes real output. "
                      "At capacity: extra spending mostly becomes inflation.",
        )

        # ---- Panel 1: Output — slack vs tight
        ax = axes[0]
        ax.plot(slack_data["output"], color=PALETTE["slack"],
                label="Slack (high capacity)", linewidth=2.0)
        ax.plot(tight_data["output"], color=PALETTE["tight"],
                label="Tight (at capacity)", linewidth=2.0)
        ax.plot(tight_data["capacity"], color=PALETTE["capacity_line"],
                linestyle="--", label="Capacity ceiling", linewidth=1.2,
                alpha=0.8)
        style_panel(ax, "Real output", ylabel="Output")
        polish_legend(ax, loc="lower right")

        # ---- Panel 2: Inflation
        ax = axes[1]
        ax.plot(slack_data["inflation"], color=PALETTE["slack"],
                label="Slack", linewidth=2.0)
        ax.plot(tight_data["inflation"], color=PALETTE["tight"],
                label="Tight", linewidth=2.0)
        style_panel(ax, "Inflation rate", ylabel="Inflation")
        polish_legend(ax, loc="upper right")

        # ---- Panel 3: Spending ramp with shaded slack/tight regions
        ax = axes[2]
        ramp_output = np.array(ramp_data["output"])
        ramp_capacity = np.array(ramp_data["capacity"])
        ramp_inflation = np.array(ramp_data["inflation"])

        # find the period where output crosses capacity
        crossover = None
        for t in range(len(ramp_output)):
            if ramp_output[t] >= ramp_capacity[t]:
                crossover = t
                break

        if crossover is not None:
            ax.axvspan(0, crossover, color=PALETTE["slack"], alpha=0.08,
                       zorder=0)
            ax.axvspan(crossover, len(ramp_output), color=PALETTE["tight"],
                       alpha=0.08, zorder=0)

        ax.plot(ramp_output, color=PALETTE["output"], label="Output",
                linewidth=2.2)
        ax.plot(ramp_capacity, color=PALETTE["capacity_line"], linestyle="--",
                label="Capacity", linewidth=1.2, alpha=0.8)
        style_panel(ax, "Spending ramp: slack-to-tight transition",
                    ylabel="Output")

        ax2 = ax.twinx()
        ax2.plot(ramp_inflation, color=PALETTE["inflation"], label="Inflation",
                 linewidth=2.0, alpha=0.85)
        ax2.set_ylabel("Inflation", color=PALETTE["inflation"], fontsize=9.5)
        ax2.tick_params(axis="y", colors=PALETTE["inflation"])
        ax2.spines["right"].set_visible(True)
        ax2.spines["right"].set_color(FG_SPINE)
        ax2.grid(False)

        # Combined legend
        h1, l1 = ax.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        leg = ax.legend(h1 + h2, l1 + l2, loc="upper left", frameon=True,
                        facecolor=BG_AXES, edgecolor=FG_SPINE, fontsize=9)
        for text in leg.get_texts():
            text.set_color(FG_MUTED)

        if crossover is not None:
            add_callout(ax, crossover, ramp_capacity[crossover],
                        f"crosses capacity\n@ period {crossover}",
                        xytext=(-90, -45))

        fig.tight_layout()
        if output_path:
            fig.savefig(output_path)
        plt.close(fig)


def plot_rollover_comparison(data: dict, output_path=None):
    """Rate, rollover need, and debt stock for issuer vs user × short vs long maturity.

    Log scale on rollover and debt panels keeps the issuer trajectories
    readable alongside the currency-user explosion.
    """
    from experiments.money_minsky_policy_mismatch._plot_theme import (
        themed, make_figure, style_panel, add_horizontal_threshold,
        polish_legend, PALETTE,
    )

    series = [
        ("user_short", "Currency user — short maturity",
         PALETTE["household"], "-"),
        ("user_long", "Currency user — long maturity",
         PALETTE["currency_user"], "--"),
        ("issuer_short", "Sovereign issuer — short maturity",
         PALETTE["sovereign_issuer"], "-"),
        ("issuer_long", "Sovereign issuer — long maturity",
         "#74c0fc", "--"),
    ]

    with themed():
        fig, axes = make_figure(
            n_panels=3,
            title="Maturity structure matters: same debt, different dynamics",
            subtitle="Issuer rate is policy-set; user rate climbs with debt + "
                      "rollover spread, capped at market lockout. Log scales "
                      "on the right two panels.",
        )

        # ---- Panel 1: Effective rate (linear, with rate-cap reference)
        ax = axes[0]
        for key, label, color, ls in series:
            if key in data:
                ax.plot(data[key]["effective_rate"], color=color, linestyle=ls,
                        label=label, linewidth=2.0)
        # Rate cap reference line
        if "user_short" in data:
            cap = max(data["user_short"]["effective_rate"])
            add_horizontal_threshold(ax, cap, label="market lockout cap")
        style_panel(ax, "Effective interest rate", ylabel="Rate")
        polish_legend(ax, loc="center right")

        # ---- Panel 2: Rollover need (log scale)
        ax = axes[1]
        for key, label, color, ls in series:
            if key in data:
                vals = np.array(data[key]["rollover_need"]) + 1e-3
                ax.plot(vals, color=color, linestyle=ls, label=label, linewidth=2.0)
        ax.set_yscale("log")
        style_panel(ax, "Rollover need (log scale)",
                    ylabel="Rollover required")

        # ---- Panel 3: Debt stock (log scale)
        ax = axes[2]
        for key, label, color, ls in series:
            if key in data:
                vals = np.array(data[key]["debt_total"]) + 1e-3
                ax.plot(vals, color=color, linestyle=ls, label=label, linewidth=2.0)
        ax.set_yscale("log")
        style_panel(ax, "Total debt stock (log scale)", ylabel="Debt")

        fig.tight_layout()
        if output_path:
            fig.savefig(output_path)
        plt.close(fig)


def plot_external_constraint(low_data: dict, high_data: dict, output_path=None):
    """Low vs high import dependence: nominal output, FX stress, and the
    real purchasing-power gap that opens once imported inflation bites.
    """
    from experiments.money_minsky_policy_mismatch._plot_theme import (
        themed, make_figure, style_panel, add_callout, polish_legend, PALETTE,
    )

    with themed():
        fig, axes = make_figure(
            n_panels=3,
            title="External constraint: import dependence limits real output",
            subtitle="Same domestic policy, two economies. Under low import "
                      "dependence the multiplier works as expected. Under high "
                      "import dependence demand leaks abroad and FX stress "
                      "creates imported inflation.",
        )

        # ---- Panel 1: Nominal output
        ax = axes[0]
        ax.plot(low_data["output"], color=PALETTE["slack"],
                label="Low import dependence", linewidth=2.2)
        ax.plot(high_data["output"], color=PALETTE["tight"],
                label="High import dependence", linewidth=2.2)
        style_panel(ax, "Nominal output", ylabel="Output")
        polish_legend(ax, loc="center right")

        # Annotate the level gap
        last = len(low_data["output"]) - 1
        gap_pct = (1 - high_data["output"][last] / low_data["output"][last]) * 100
        add_callout(
            ax, last - 5, high_data["output"][last],
            f"high-dep operates at\n{100 - gap_pct:.0f}% of low-dep output",
            xytext=(-150, 35),
        )

        # ---- Panel 2: FX stress
        ax = axes[1]
        ax.plot(low_data["fx_stress"], color=PALETTE["slack"],
                label="Low dep.", linewidth=2.2)
        ax.plot(high_data["fx_stress"], color=PALETTE["tight"],
                label="High dep.", linewidth=2.2)
        style_panel(ax, "FX stress (currency pressure)", ylabel="Stress index")
        polish_legend(ax, loc="center right")

        # ---- Panel 3: Real purchasing power = output / (1 + cumulative inflation)
        ax = axes[2]
        for label, dataset, color in [
            ("Low dep.", low_data, PALETTE["slack"]),
            ("High dep.", high_data, PALETTE["tight"]),
        ]:
            output = np.array(dataset["output"])
            inflation = np.array(dataset["inflation"])
            price_level = np.cumprod(1.0 + inflation)
            real_purchasing = output / price_level
            ax.plot(real_purchasing, color=color, label=label, linewidth=2.2)
        style_panel(ax, "Real purchasing power\n(output ÷ price level)",
                    ylabel="Real output")
        polish_legend(ax, loc="upper right")

        fig.tight_layout()
        if output_path:
            fig.savefig(output_path)
        plt.close(fig)


def plot_holder_composition(data: dict, output_path=None):
    """Steady-state output, net domestic flow, and wealth concentration as
    horizontal bar charts across four holder-mix scenarios.

    Bars are clearer than time-series for steady-state comparison; the
    flat lines in the previous version conveyed no temporal story.
    """
    from experiments.money_minsky_policy_mismatch._plot_theme import (
        themed, make_figure, style_panel, PALETTE, FG_TEXT, FG_MUTED,
    )

    configs = [
        ("household_heavy", "Household-heavy",   PALETTE["holder_household"]),
        ("asset_heavy",     "Asset-holder-heavy", PALETTE["holder_asset"]),
        ("foreign_heavy",   "Foreign-heavy",     PALETTE["holder_foreign"]),
        ("cb_heavy",        "Central-bank-heavy", PALETTE["holder_cb"]),
    ]

    # Compute steady-state values (mean of last 10 periods)
    def _ss(key, field, transform=None):
        arr = np.asarray(data[key][field])
        val = float(np.mean(arr[-10:]))
        return transform(val) if transform else val

    labels = [label for _, label, _ in configs]
    colors = [color for _, _, color in configs]

    output_vals = [_ss(k, "output") for k, _, _ in configs]
    net_flow_vals = [
        _ss(k, "domestic_recirculation") - _ss(k, "foreign_leakage")
        for k, _, _ in configs
    ]
    concentration_vals = [_ss(k, "wealth_concentration") for k, _, _ in configs]

    with themed():
        fig, axes = make_figure(
            n_panels=3,
            title="Same nominal debt, different holders",
            subtitle="Identical debt stock and coupon. Only the holder mix "
                      "changes. Steady-state values shown as horizontal bars.",
        )

        def _draw_bars(ax, values, title, xlabel, fmt="{:.2f}",
                        center_at_zero=False):
            y_pos = np.arange(len(labels))[::-1]  # top-to-bottom order
            bars = ax.barh(y_pos, values, color=colors, edgecolor="none",
                           height=0.6)
            ax.set_yticks(y_pos)
            ax.set_yticklabels(labels, color=FG_TEXT, fontsize=9.5)
            ax.tick_params(axis="x", colors=FG_MUTED)
            ax.grid(axis="x", color="#2e333c", linewidth=0.6, alpha=0.7)
            ax.grid(axis="y", visible=False)
            ax.spines["left"].set_visible(False)

            # Value labels on each bar
            for bar, val in zip(bars, values):
                width = bar.get_width()
                ha = "left" if width >= 0 else "right"
                offset = max(abs(v) for v in values) * 0.02 if max(abs(v) for v in values) > 0 else 0.01
                x_label = width + (offset if width >= 0 else -offset)
                ax.text(x_label, bar.get_y() + bar.get_height() / 2,
                        fmt.format(val), va="center", ha=ha,
                        color=FG_TEXT, fontsize=9, fontweight="bold")

            if center_at_zero:
                ax.axvline(0, color=FG_MUTED, linewidth=0.8, alpha=0.6)
                lim = max(abs(min(values)), abs(max(values))) * 1.3
                ax.set_xlim(-lim, lim)
            else:
                ax.set_xlim(0, max(values) * 1.15 if max(values) > 0 else 1)

            style_panel(ax, title, xlabel=xlabel, ylabel="")

        _draw_bars(axes[0], output_vals,
                   "Output",
                   "Real activity (steady state)",
                   fmt="{:.1f}")
        _draw_bars(axes[1], net_flow_vals,
                   "Net domestic interest flow",
                   "Recirculation − leakage",
                   fmt="{:+.1f}",
                   center_at_zero=True)
        _draw_bars(axes[2], concentration_vals,
                   "Wealth concentration",
                   "Asset-holder share of domestic wealth",
                   fmt="{:.2f}")

        fig.tight_layout()
        if output_path:
            fig.savefig(output_path)
        plt.close(fig)


def save_all_plots(results: dict, plot_dir: str):
    """Generate and save all plots from experiment results."""
    plot_path = Path(plot_dir)
    plot_path.mkdir(parents=True, exist_ok=True)

    plt.switch_backend("Agg")
    plot_constraint_hierarchy(plot_path / "constraint_hierarchy.png")
    plot_campaign_vs_operational_models(
        plot_path / "campaign_vs_operational_models.png"
    )
    plot_wrong_target_control(plot_path / "wrong_target_control.png")

    if "keen_stable_vs_crisis" in results and results["keen_stable_vs_crisis"]:
        data = results["keen_stable_vs_crisis"]
        plot_keen_stable_vs_crisis(
            data["stable"], data["crisis"],
            plot_path / "keen_stable_vs_crisis.png",
        )

    if "policy_sectoral" in results and results["policy_sectoral"]:
        plot_policy_sectoral_paths(
            results["policy_sectoral"],
            plot_path / "policy_sectoral_paths.png",
        )
        plot_policy_sectoral_balances(
            results["policy_sectoral"],
            scenario="austerity",
            output_path=plot_path / "policy_sectoral_balances.png",
        )

    if "imf_counterfactual" in results and results["imf_counterfactual"]:
        plot_imf_counterfactual_cases(
            results["imf_counterfactual"],
            plot_path / "imf_counterfactual_cases.png",
        )

    if "fragility_regimes" in results and results["fragility_regimes"]:
        plot_fragility_regime_comparison(
            results["fragility_regimes"],
            plot_path / "fragility_regimes.png",
        )

    if "rate_hike" in results and results["rate_hike"]:
        plot_rate_hike_grid(results["rate_hike"],
                            plot_path / "rate_hike_grid.png")

    if "austerity" in results and results["austerity"]:
        data = results["austerity"]
        plot_sfc_austerity(data["sfc_baseline"], data["sfc_austerity"],
                           plot_path / "sfc_austerity.png")
        plot_minsky_distribution(data["abm_baseline"],
                                  plot_path / "minsky_distribution.png")
        plot_austerity_minsky_shift(
            data["abm_baseline"], data["abm_austerity"],
            plot_path / "austerity_minsky_shift.png",
        )

    if "jg" in results and results["jg"]:
        plot_jg_comparison(results["jg"], plot_path / "jg_comparison.png")

    # --- New simulation surfaces (tasks 018, 019, 020) ---

    if "comparative_constraints" in results and results["comparative_constraints"]:
        plot_comparative_constraints(
            results["comparative_constraints"],
            plot_path / "comparative_constraints.png",
        )

    if "policy_lab" in results and results["policy_lab"]:
        plot_policy_lab(
            results["policy_lab"],
            plot_path / "policy_lab.png",
        )

    if "capacity_constraint" in results and results["capacity_constraint"]:
        data = results["capacity_constraint"]
        plot_capacity_constraint(
            data["slack"], data["tight"], data["spending_ramp"],
            plot_path / "capacity_constraint.png",
        )

    # --- Factor-refinement surfaces (tasks 026, 027) ---

    if "rollover" in results and results["rollover"]:
        plot_rollover_comparison(
            results["rollover"],
            plot_path / "rollover_comparison.png",
        )

    if "external_constraint" in results and results["external_constraint"]:
        data = results["external_constraint"]
        plot_external_constraint(
            data["low_dependence"], data["high_dependence"],
            plot_path / "external_constraint.png",
        )

    if "holder_composition" in results and results["holder_composition"]:
        plot_holder_composition(
            results["holder_composition"],
            plot_path / "holder_composition.png",
        )

    if "issuer_user" in results and results["issuer_user"]:
        data = results["issuer_user"]
        plot_issuer_vs_user(data["issuer"], data["user"],
                            plot_path / "issuer_vs_user.png")
        plot_sectoral_balances(data["issuer"],
                               plot_path / "sectoral_balances.png")

    plt.close("all")
    print(f"  All plots saved to {plot_path}")
