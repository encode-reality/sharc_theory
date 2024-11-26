### Title and Authors
**Title**: [Bioelectric Gene and Reaction Networks: Computational Modelling of Genetic, Biochemical, and Bioelectrical Dynamics in Pattern Regulation](Alexis%20BIGR%20paper.pdf)

**Authors**: Alexis Pietak and Michael Levin  
**Publication**: Journal of the Royal Society Interface, 2017  

---

### Summary and Formalism

#### Objective
The paper develops the **Bioelectricity-Integrated Gene and Reaction (BIGR)** network framework. This framework combines **gene regulatory networks (GRNs)**, **reaction-diffusion models**, and **bioelectric signals** to study biological patterning, regeneration, and anatomical control mechanisms.

---

#### Key Contributions
1. **Integration of Bioelectric Signals into GRNs**:
   - Extends traditional GRNs to incorporate bioelectric signals such as transmembrane potential.
   - Models feedback loops between `V_mem`, gene expression, and biochemical reactions.

2. **Hybrid Modeling Approach**:
   - Incorporates voltage-sensitive dynamics, ion transport, and signaling molecule interactions.
   - Uses computational simulations to study `V_mem`-regulated concentration patterns, positional information, and regeneration.

3. **Mechanistic Insights**:
   - Identifies mechanisms for memory, hysteresis, and polarity regulation.
   - Explains phenomena like axial regeneration polarity in planaria.

4. **Applications**:
   - Models of planarian regeneration demonstrate `V_mem`-driven patterning and state stability.
   - BIGR networks provide hypotheses for bioelectric control in developmental and regenerative biology.

---

#### Formalism and Algorithmic Framework

1. **Regulatory Network Elements**:
   - **Nodes**: Concentrations of substances (e.g., ions, gene products, signaling molecules).
   - **Edges**: Activation or inhibition using Hill functions:
     - Activation:  
       ```math
       a_A = \frac{[A]/K_A^{n_A}}{1 + ([A]/K_A)^{n_A}}
       ```
     - Inhibition:  
       ```math
       b_A = \frac{1}{1 + ([A]/K_A)^{n_A}}
       ```

2. **Steady-State Dynamics**:
   - Describes relationships between `V_mem` and ion concentrations:  
     ```math
     \frac{dV_{\text{mem}}}{dt} = -\frac{1}{C_{\text{mem}}} J_{\text{mem}}, \quad J_{\text{mem}} = \sum_i z_i F J_i
     ```
   - Uses the Goldman-Hodgkin-Katz (GHK) equation to model ion flux.

3. **Feedback Mechanisms**:
   - `V_mem` modulates ion channel states, which in turn regulate `V_mem`.
   - Chemical reactions and `V_mem` dynamics are interlinked:  
     ```math
     r_{\text{reaction}} = k_f \prod \left(\frac{[X]}{K_X}\right) - k_r \prod \left(\frac{[Y]}{K_Y}\right)
     ```

4. **Forced Cycle Perturbation**:
   - Simulates transient changes in membrane permeability (e.g., for `Na^+` and `K^+`) to study hysteresis and memory:
     - Functions `f(t)` and `g(t)` control permeability modulation.
     - `V_mem` hysteresis loop area indicates memory capacity.

5. **Gap Junction Coupling**:
   - Models ion and molecule diffusion between cells using:  
     ```math
     F^{\text{gj}} = -D_i \nabla c - \frac{z_i F}{RT} c \nabla V
     ```

6. **Simulation Environment**:
   - Implemented in the **BioElectric Tissue Simulation Engine (BETSE)**.
   - Simulates ion transport, `V_mem` patterns, and network-level dynamics.

---

#### Applications Highlighted in the Paper

1. **Planarian Regeneration**:
   - Demonstrates anterior-posterior polarity restoration through `V_mem`-driven signaling.
   - Explores the role of gap junctions in `V_mem` gradient maintenance.

2. **Pattern Formation**:
   - Simulates emergent `V_mem` stripes and spots linked to signaling molecule gradients.

3. **Network Analysis**:
   - Explores memory, homeostasis, and state-switching in bioelectric circuits.

---

Let me know if you want the same format for other sections or specific elaborations! 
