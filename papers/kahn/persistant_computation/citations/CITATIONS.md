# Citations Folder
Purpose
- Collect PDFs (or authoritative links) for every in-text citation used in `manuscript.md`.
- Maintain a manifest with status and retrieval notes per entry.

Scope
- Source of truth for citations is `papers/kahn/persistant_computation/references.bib`.
- This folder will hold downloaded PDFs where permitted and a manifest for any items pending download.

Manifest (initial)
- Status legend: AVAILABLE (PDF present here), LINKED (authoritative URL/DOI noted), PENDING (needs retrieval/verification).

| Key | Citation (from .bib) | Status | Notes |
|---|---|---|---|
| turing1936 | Turing (1936), On computable numbers... | PENDING | Classic; publisher PDF behind paywall; find OA copy |
| church1936 | Church (1936), An unsolvable problem... | PENDING | Likely JSTOR/Project Euclid; OA copy if available |
| cook2004 | Cook (2004), Universality in ECA | PENDING | Complex Systems; OA likely |
| berlekamp1982 | Berlekamp et al. (1982), Winning Ways vol. 2 | PENDING | Book; cite link only |
| rendell2013 | Rendell (2013), Turing machine in Life | PENDING | Book chapter; cite link only |
| fredkin1982 | Fredkin & Toffoli (1982), Conservative logic | PENDING | Springer or journal link |
| toffoli1987 | Toffoli & Margolus (1987), CA Machines | PENDING | MIT Press; cite link only |
| landauer1961 | Landauer (1961), Irreversibility... | PENDING | IBM JRD; OA scan exists |
| bennett1973 | Bennett (1973), Logical reversibility | PENDING | IBM JRD; OA scan exists |
| bennett1982 | Bennett (1982), Thermodynamics of computation (review) | PENDING | IJTP |
| deutsch1985 | Deutsch (1985), Universal quantum computer | PENDING | Proc. R. Soc. A |
| zuse1969 | Zuse (1969), Rechnender Raum | PENDING | Book; cite link only |
| fredkin1990 | Fredkin (1990), Digital mechanics | PENDING | Physica D |
| wolfram2002 | Wolfram (2002), NKS | PENDING | Book; cite link only |
| lloyd2000 | Lloyd (2000), Ultimate physical limits | PENDING | Nature |
| putnam1988 | Putnam (1988), Representation and Reality | PENDING | Book; cite link only |
| chalmers1996 | Chalmers (1996), Rock implements FSA? | PENDING | Synthese |
| piccinini2007 | Piccinini (2007), Computing mechanisms | PENDING | Philosophy of Science |
| piccinini2015 | Piccinini (2015), Physical Computation | PENDING | OUP book; cite link only |
| langton1990 | Langton (1990), Edge of chaos | PENDING | Physica D |
| crutchfield2001 | Crutchfield & Shalizi (2001), Pattern and prediction | PENDING | J. Stat. Phys. |
| simon1962 | Simon (1962), Architecture of complexity | PENDING | APS Proc. |
| shannon1948 | Shannon (1948), Mathematical theory of communication | PENDING | BSTJ; OA scan exists |
| hamming1950 | Hamming (1950), Error-correcting codes | PENDING | BSTJ |
| gallager1962 | Gallager (1962), LDPC | PENDING | IRE Trans. IT |
| gallager1968 | Gallager (1968), Info Theory & Reliable Comm. | PENDING | Book; cite link only |
| pross2004 | Pross (2004), Stability in chemistry & biology | PENDING | Foundations of Chemistry |
| pross2012 | Pross (2012), What Is Life? | PENDING | OUP book; cite link only |
| godel1931 | Gödel (1931), Undecidable propositions | PENDING | English translations available |
| ashby1956 | Ashby (1956), Introduction to Cybernetics | PENDING | Book; OA PDFs exist |
| eigen1971 | Eigen (1971), Selforganization... | PENDING | Naturwissenschaften |
| kauffman1986 | Kauffman (1986), Autocatalytic sets | PENDING | JTB |
| chernoff1952 | Chernoff (1952), Asymptotic efficiency | PENDING | AMS |
| parrondo2015 | Parrondo et al. (2015), Thermodynamics of information | PENDING | Nat. Phys. |
| sagawa2009 | Sagawa & Ueda (2009), Minimal energy cost | PENDING | PRL |
| berrou1993 | Berrou et al. (1993), Turbo codes | PENDING | ICC proceedings |
| mackay1999 | MacKay & Neal (1999), Sparse-matrix codes | PENDING | IEEE Trans. IT |
| polyanskiy2010 | Polyanskiy et al. (2010), Finite blocklength | PENDING | IEEE Trans. IT |
| conant1970 | Conant & Ashby (1970), Good regulator theorem | PENDING | IJSS |
| crutchfield1989 | Crutchfield & Young (1989), Statistical complexity | PENDING | PRL |
| bialek2001 | Bialek et al. (2001), Predictability & complexity | PENDING | Neural Computation |
| kadanoff1966 | Kadanoff (1966), Scaling laws | PENDING | Physics |
| wilson1971 | Wilson (1971), RG & critical phenomena | PENDING | PRB |
| schreiber2000 | Schreiber (2000), Transfer entropy | PENDING | PRL |
| england2013 | England (2013), Self-replication physics | PENDING | J. Chem. Phys. |
| hordijk2004 | Hordijk & Steel (2004), Autocatalytic sets | PENDING | JTB |
| friston2010 | Friston (2010), Free-energy principle | PENDING | Nat. Rev. Neurosci. |
| hoel2017 | Hoel et al. (2017), Causal emergence | PENDING | PNAS |

How to populate
- Option A (manual): place each PDF here, named `{key}.pdf`.
- Option B (scripted): use Crossref/Unpaywall to resolve DOIs and open-access links, then download to `{key}.pdf`.
- Option C (publisher links only): if PDFs are not permitted for redistribution, create `{key}.url` files with the canonical link.

Requests
- Approve network access for scripted retrieval, or confirm manual curation.
- If you have institutional access, share links or PDFs to place here.
