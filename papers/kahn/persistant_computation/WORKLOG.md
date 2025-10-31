# Worklog — Persistent Computation Paper

- Folder: `papers/kahn/persistant_computation/`
- Sources:
  - `papers/kahn/persistant_computation/outline_structure.md`
  - `papers/kahn/persistant_computation/Unifying Automata Theory, Universal Computation, and Scale-Invariant Dynamics.pdf`

## Objectives
- Use the PDF and outline to write a publication‑ready paper, section by section.
- Keep all artifacts in this folder; update this worklog at each step.
- Maintain tight scope: unify automata theory, universal computation, and scale‑invariant dynamics under a coherent framework.

## Deliverables
- `proposal.md` — approach, scope, and section plan for approval.
- Section drafts (added after approval) and final manuscript.
- Optional: `references.bib` if we move to LaTeX.

## Workflow and Status
- DONE — Inventory inputs in this folder
- DONE — Create `WORKLOG.md`
- DONE — Draft and record figure/table list (see `figures_and_tables.md`)
- PENDING — Confirm venue, audience, length, and citation style
- IN PROGRESS — Lock section structure and terminology glossary (created `manuscript.md` and `glossary.md`)
- DONE — Draft Foundations/Related Work (Automata, Universality, Physical Computation) — in `manuscript.md` Section 3
- DONE — Draft Emergence and Scale Invariance — in `manuscript.md` Section 4
- DONE — Draft Core Framework: Persistent Computation (formal criteria) — in `manuscript.md` Section 5
- DONE — Draft Entropy/Redundancy and DKS — in `manuscript.md` Section 6
- DONE — Draft Incompleteness, Control, and Adaptation — in `manuscript.md` Section 7
- DONE — Draft Discussion, Implications, Limitations — in `manuscript.md` Sections 8–9
- DONE — Draft Introduction, then Abstract and Title — in `manuscript.md` Sections 1–2
- DONE — Add detailed citations and References section — in `manuscript.md` Section 11
- DONE — Insert figure/table placeholders within manuscript and expand sketches in `figures_and_tables.md`
- DONE — Switch to author–year citations and add `references.bib`
- DONE — Create SVG figure placeholders (`fig1`–`fig5`) and link in manuscript
- DONE — Add mermaid and vega‑lite code drafts in `figures_and_tables.md`
- DONE — Verified all Vega blocks labeled as `vega-lite`
- DONE — Add advanced vega‑lite sketches (F6–F13) to `figures_and_tables.md`
- DONE — Create additional SVG schematics (fig6 edge‑of‑chaos; fig7 robustness; fig8 cross‑domain montage)
- DONE — Fill Table 1 (cross‑scale mapping) in `manuscript.md`
- PENDING — Figures integration and citation pass
- PENDING — Editing, coherence pass, formatting/export

## Decisions Needed from User
- Approve or edit `proposal.md`
- Target venue/audience and expected length
- Preferred citation style (numeric vs author‑year)
- Risk appetite for formalism depth (light vs math‑forward)
- Figure preferences and any must‑cite works

## Drafting Order (proposed)
- Foundations and Related Work
- Emergence and Scale Invariance
- Core Framework (Persistent Computation)
- Entropy/Redundancy and Stability
- Incompleteness and Adaptive Systems
- Discussion and Implications
- Introduction → Abstract → Title

## Conventions
- Keep all new files in this folder; use short, descriptive filenames.
- Update this Worklog whenever a step completes or scope changes.

## Change Log
- Initial creation of worklog and setup tasks — pending user review of proposal.
- User approved proposal; created `manuscript.md` scaffold and `glossary.md`.
- Drafted Section 3 (Foundations and Related Work) and Section 4 (Emergence and Scale Invariance) in `manuscript.md`.
- Drafted Section 5 (Persistent Computation framework) in `manuscript.md`.
- Drafted Sections 6–7 (Entropy/Redundancy; Incompleteness/Control/Adaptation) in `manuscript.md`.
- Drafted Sections 8–10 (Discussion; Limitations; Conclusion) and completed Sections 1–2 (Abstract; Introduction).
- Added `figures_and_tables.md` with initial figure/table plan.
- Added numeric inline citations and a detailed References section; inserted figure/table placeholders at relevant sections; expanded figure/table sketches.
- Switched to author–year citations and created `references.bib`; added SVGs and mermaid/vega‑lite drafts; updated manuscript to embed figures.
- Added formal refinements and expanded citations (thermodynamics of information, finite‑blocklength coding, renormalization/coarse‑graining, computational mechanics, causal emergence, free‑energy principle) throughout the manuscript; updated manual References list.
- Removed manual References section and enabled Pandoc bibliography via YAML front matter; added `BUILD.md` with pandoc commands.
- Added Section 5.0 “Assumptions and Scope” and Appendix A (symbols) + Appendix B (units and conventions).
- Created `citations/` folder with `CITATIONS.md` manifest; awaiting approval to fetch PDFs via network.
