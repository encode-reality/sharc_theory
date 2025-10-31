# Build Instructions (Pandoc)
Requirements
- Pandoc 2.11+ with citeproc
- A LaTeX engine for PDF (e.g., xelatex) if generating PDF

Commands
- HTML (with bibliography):
  - `pandoc manuscript.md --citeproc -o manuscript.html`
- PDF (XeLaTeX recommended):
  - `pandoc manuscript.md --citeproc --pdf-engine=xelatex -o manuscript.pdf`
- Specify a CSL style (optional):
  - `pandoc manuscript.md --citeproc --csl=ieee.csl -o manuscript.pdf`

Citation styles (CSL)
- Common choices: IEEE (`ieee.csl`), APA (`apa.csl`), Chicago (`chicago-author-date.csl`), Nature (`nature.csl`).
- Download your preferred `.csl` from https://github.com/citation-style-language/styles and pass via `--csl=...`.

Journal templates
- If targeting a specific journal, provide the LaTeX/Pandoc template; the section headings can be adapted to match (e.g., adding Keywords, Data/Code availability, Author contributions). I can adjust the YAML front matter accordingly once you pick a venue.

Notes
- Citations resolve via `references.bib` in this folder.
- Figures are embedded SVGs and should render in HTML/PDF; for some LaTeX engines, PNG fallbacks may be preferable.
- Vega‑Lite blocks in `figures_and_tables.md` are for interactive rendering; export to static images if needed for journals without JS.
