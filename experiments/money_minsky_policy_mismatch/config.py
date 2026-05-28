"""Configuration: default parameters, sweep ranges, colors, and plot settings."""

DEFAULT_SEED = 42

# ---------------------------------------------------------------------------
# Keen-style ODE defaults (Goodwin-Keen-Minsky leverage cycle)
# Source: minsky2.md design spec; calibrated to produce stable limit cycle
# at baseline and crisis under high-leverage / high-rate conditions.
# ---------------------------------------------------------------------------
KEEN_ODE_DEFAULTS = dict(
    r=0.04,          # base interest rate on private debt
    delta=0.03,      # depreciation rate
    alpha=0.02,      # labor productivity growth rate
    n=0.01,          # labor force growth rate
    a0=-0.04,        # Phillips curve intercept (negative = wage deflation at low employment)
    a1=2.0,          # Phillips curve slope (above threshold)
    lam0=0.9,        # Phillips curve employment threshold
    k0=0.05,         # autonomous investment share (~5% replacement/maintenance)
    k1=0.40,         # investment sensitivity to profit share (credit-financed expansion)
    k2=0.04,         # investment sensitivity to debt ratio (debt drag)
)

KEEN_ODE_INITIAL = [0.80, 0.92, 0.3]   # [omega_0, lambda_0, d_0]
KEEN_ODE_TSPAN = (0.0, 200.0)
KEEN_CRISIS_THRESHOLD = 5.0             # debt ratio above which we flag crisis

# ---------------------------------------------------------------------------
# SFC model defaults (minimal 3-sector: households, firms+banks, government)
# Source: minsky2.md lines 149-185, ported from R sfcr template
# ---------------------------------------------------------------------------
SFC_DEFAULTS = dict(
    G=20.0,           # government spending (exogenous baseline)
    tau=0.20,         # income tax rate
    rL=0.04,          # interest rate on firm loans (also base sovereign rate)
    c1=0.85,          # marginal propensity to consume out of disposable income
    c2=0.02,          # marginal propensity to consume out of wealth
    kappa0=10.0,      # autonomous investment
    kappa1=0.10,      # investment sensitivity to profits
    kappa2=0.20,      # investment sensitivity to debt ratio (debt drag)
    W=60.0,           # aggregate wage bill (simplified exogenous)
    # Issuer-vs-user parameters
    spread_phi=0.0,   # spread sensitivity to debt/GDP (0 = issuer, >0 = user)
    spread_threshold=0.5,  # debt/GDP level above which spread activates
    market_access_spread=0.15,  # spread level that triggers forced consolidation
    mpc_interest=0.10,  # MPC out of sovereign interest income (bondholders save more)
    max_sovereign_rate=0.06,  # rate cap: beyond this, market locks out entirely
)

SFC_INITIAL = dict(
    Nh=100.0,         # household net worth
    Lf=50.0,          # firm loans (debt)
    Bg=60.0,          # government bills/debt stock
)

# ---------------------------------------------------------------------------
# ABM defaults
# ---------------------------------------------------------------------------
ABM_DEFAULTS = dict(
    n_firms=50,
    n_households=500,
    n_banks=5,
    periods=200,
    tau=0.20,              # income tax rate
    w_jg=0.0,              # JG wage (0 = no JG)
    austerity_phi=0.0,     # austerity aggressiveness (0 = off)
    target_deficit=0.03,   # DEF/Y target if austerity on
    policy_rate=0.04,      # base policy rate
    bank_spread_phi=0.02,  # bank spread sensitivity to firm leverage
    base_productivity=2.0, # output per worker
    consumption_propensity=0.85,
    firm_markup=0.10,      # over wage costs
    loan_duration=20,      # periods to repay principal
    bank_capital_ratio_min=0.08,  # regulatory minimum
    invest_share=0.15,     # fraction of cash flow borrowed for investment
    confidence_sensitivity=0.2,  # how much animal spirits amplify investment
    fiscal_transfer=0.0,  # per-household fiscal transfer (default 0 for backward compat)
    demand_sensitivity=0.0,  # how much lagged HH consumption modulates firm revenue (0=off)
)

# ---------------------------------------------------------------------------
# Experiment parameter sweep ranges
# ---------------------------------------------------------------------------
AUSTERITY_SWEEP = dict(
    austerity_phi=[0.0, 0.2, 0.4, 0.6, 0.8],
    initial_debt_ratio=[0.5, 1.0, 1.5, 2.0, 2.5],
)

RATE_HIKE_SWEEP = dict(
    delta_r=[0.01, 0.03, 0.05],       # rate shock in absolute terms
    initial_d=[0.5, 1.0, 1.5, 2.0, 2.5, 3.0],
)

JG_SWEEP = dict(
    w_jg_ratio=[0.0, 0.35, 0.50, 0.65],  # JG wage relative to median
)

# ---------------------------------------------------------------------------
# Colors and plot settings
# ---------------------------------------------------------------------------
COLORS = {
    "hedge": "#2ecc71",
    "speculative": "#f39c12",
    "ponzi": "#e74c3c",
    "output": "#3498db",
    "employment": "#1abc9c",
    "debt": "#e74c3c",
    "wage_share": "#9b59b6",
    "deficit": "#e67e22",
    "issuer": "#2980b9",
    "user": "#c0392b",
    "austerity": "#e74c3c",
    "functional_finance": "#2ecc71",
    "jg": "#1abc9c",
    "nairu": "#95a5a6",
    "inflation": "#e67e22",
}

PLOT_DEFAULTS = dict(
    figsize=(12, 7),
    dpi=150,
    style="dark_background",
)
