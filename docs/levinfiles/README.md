### Title and Authors
**Title**: [Bioelectric Gene and Reaction Networks: Computational Modelling of Genetic, Biochemical, and Bioelectrical Dynamics in Pattern Regulation](Alexis%20BIGR%20paper.pdf)

**Authors**: Alexis Pietak and Michael Levin  
**Publication**: Journal of the Royal Society Interface, 2017  

### Summary and Formalism

#### Objective
The paper develops the **Bioelectricity-Integrated Gene and Reaction (BIGR)** network framework. This framework combines **gene regulatory networks (GRNs)**, **reaction-diffusion models**, and **bioelectric signals** to study biological patterning, regeneration, and anatomical control mechanisms.

---

#### Key Contributions
1. **Integration of Bioelectric Signals into GRNs**:
   - Extends traditional GRNs to incorporate bioelectric signals such as transmembrane potential ($V_{\text{mem}}$).
   - Models feedback loops between $V_{\text{mem}}$, gene expression, and biochemical reactions.

2. **Hybrid Modeling Approach**:
   - Incorporates voltage-sensitive dynamics, ion transport, and signaling molecule interactions.
   - Uses computational simulations to study $V_{\text{mem}}$-regulated concentration patterns, positional information, and regeneration.

3. **Mechanistic Insights**:
   - Identifies mechanisms for memory, hysteresis, and polarity regulation.
   - Explains phenomena like axial regeneration polarity in planaria.

4. **Applications**:
   - Models of planarian regeneration demonstrate $V_{\text{mem}}$-driven patterning and state stability.
   - BIGR networks provide hypotheses for bioelectric control in developmental and regenerative biology.

---

#### Formalism and Algorithmic Framework

1. **Regulatory Network Elements**:
   - **Nodes**: Concentrations of substances (e.g., ions, gene products, signaling molecules).
   - **Edges**: Activation or inhibition using Hill functions:
     - Activation:  
       $$ a_A = \frac{[A]/K_A^{n_A}}{1 + ([A]/K_A)^{n_A}} $$
     - Inhibition:  
       $$ b_A = \frac{1}{1 + ([A]/K_A)^{n_A}} $$

2. **Steady-State Dynamics**:
   - Describes relationships between $V_{\text{mem}}$ and ion concentrations:  
     $$
     \frac{dV_{\text{mem}}}{dt} = -\frac{1}{C_{\text{mem}}} J_{\text{mem}}, \quad J_{\text{mem}} = \sum_i z_i F J_i
     $$
   - Uses the Goldman-Hodgkin-Katz (GHK) equation to model ion flux.

3. **Feedback Mechanisms**:
   - $V_{\text{mem}}$ modulates ion channel states, which in turn regulate $V_{\text{mem}}$.
   - Chemical reactions and $V_{\text{mem}}$ dynamics are interlinked:  
     $$
     r_{\text{reaction}} = k_f \prod \left(\frac{[X]}{K_X}\right) - k_r \prod \left(\frac{[Y]}{K_Y}\right)
     $$

4. **Forced Cycle Perturbation**:
   - Simulates transient changes in membrane permeability (e.g., for Na$^+$ and K$^+$) to study hysteresis and memory:
     - Functions $f(t)$ and $g(t)$ control permeability modulation.
     - $V_{\text{mem}}$ hysteresis loop area indicates memory capacity.

5. **Gap Junction Coupling**:
   - Models ion and molecule diffusion between cells using:  
     $$
     F^{\text{gj}} = -D_i \nabla c - \frac{z_i F}{RT} c \nabla V
     $$

6. **Simulation Environment**:
   - Implemented in the **BioElectric Tissue Simulation Engine (BETSE)**.
   - Simulates ion transport, $V_{\text{mem}}$ patterns, and network-level dynamics.

---

#### Applications Highlighted in the Paper

1. **Planarian Regeneration**:
   - Demonstrates anterior-posterior polarity restoration through $V_{\text{mem}}$-driven signaling.
   - Explores the role of gap junctions in $V_{\text{mem}}$ gradient maintenance.

2. **Pattern Formation**:
   - Simulates emergent $V_{\text{mem}}$ stripes and spots linked to signaling molecule gradients.

3. **Network Analysis**:
   - Explores memory, homeostasis, and state-switching in bioelectric circuits.


### Title and Authors

**Title**: [Technological Approach to Mind Everywhere (TAME): an Experimentally-Grounded Framework for Understanding Diverse Bodies and Minds](Binder2.pdf)  
**Authors**: Michael Levin  
**Affiliations**: Allen Discovery Center at Tufts University; Wyss Institute for Biologically Inspired Engineering at Harvard University  

---

### Summary and Formalism

#### Objective
The paper proposes the **Technological Approach to Mind Everywhere (TAME)** framework, which aims to formalize an experimental and theoretical approach to understanding and manipulating cognition across a broad spectrum of physical and biological systems, including unconventional substrates. It views cognition and agency as continuous and scalable properties rather than binary phenomena.

---

### Key Contributions

1. **Gradualist Approach to Cognition**:
   - Suggests that cognitive capabilities exist on a continuum, dismissing binary distinctions between "minds" and "non-minds."

2. **Framework for Cognitive Scaling**:
   - Introduces hypotheses on how individual components combine to form collective intelligences or "Selves."
   - Defines Selves by their ability to:
     - Pursue goals.
     - Maintain and own compound memories.
     - Assign credit for rewards and punishments at scales larger than individual components.

3. **Bioelectric Networks**:
   - Highlights bioelectricity as a medium for multi-scale integration of cellular activity into cognitive and anatomical homeostasis.
   - Discusses the role of ion channels and gap junctions in scaling cognition.

4. **Morphogenesis as Basal Cognition**:
   - Identifies parallels between morphogenesis and behavior, suggesting that both are problem-solving activities within different "spaces."

5. **Trainability of Biological Systems**:
   - Proposes that tissues and cellular collectives can be trained for specific morphological outcomes, akin to learning in neural networks.

---

### Formalism in the TAME Framework

#### Key Definitions and Components

1. **Cognitive Capacity as a Continuum**:
   - TAME posits that cognitive properties, such as preferences and memory, are not binary but exist along a continuous spectrum.

2. **Goal-Directed Systems**:
   - Defines systems by their ability to reduce the difference between current states and desired "setpoints" through energy expenditure.  
   - Example of goal-directed behavior:  
     $$ \Delta = \text{Setpoint} - \text{Current State}, \quad \text{Minimize}(\Delta) $$

3. **Homeostasis and Allostasis**:
   - Homeostatic loops maintain setpoints, while allostatic systems adaptively manage larger, more complex states over time.  
     $$ \text{Homeostatic Response:} \quad J_i = -k \nabla S $$  
     where \( S \) is the stress signal and \( J_i \) is the corrective action.

4. **Bioelectric Circuitry**:
   - Voltage gradients ($ V_{\text{mem}} $) and gap junction connectivity play critical roles in creating scalable cognitive networks:  
     $$ V_{\text{mem}} = \frac{RT}{F} \ln\left(\frac{[K^+]_{\text{out}}}{[K^+]_{\text{in}}}\right) $$  
   - These bioelectric states influence morphogenesis and behavior.

5. **Trainability of Morphogenesis**:
   - Hypothesizes that bioelectric networks can be trained using reinforcement learning paradigms:  
     $$ R(t) = f\left(\text{Stimulus}, \text{Reward}\right), \quad \text{Update}(W) $$  
     where \( W \) are the weights representing bioelectric states.

---

### Applications

1. **Morphogenesis**:
   - Explains phenomena such as planarian regeneration and the ability to restore anatomical structures through bioelectric signaling.

2. **Bioelectric Memory**:
   - Describes bioelectric patterns as a distributed memory system capable of storing and reprogramming anatomical information.

3. **Scaling of Agency**:
   - Examines how small-scale agents (e.g., cells) integrate into larger Selves with expanded cognitive boundaries.

4. **Ethics and Artificial Life**:
   - Highlights the importance of understanding cognition in non-traditional substrates for developing ethical frameworks and guiding regenerative medicine.


### Title and Authors

**Title**: [Transmembrane Potential as a Regulator of Tumorigenesis in Xenopus Model](Brook_s%20DM&M%20Cancer%20Paper%20reduced%20for%20mailing.pdf)

**Authors**: Brook T. Chernet and Michael Levin  
**Publication**: Disease Models & Mechanisms, 2013  

---

### Summary and Formalism

#### Objective
The paper investigates the role of transmembrane potential ($ V_{\text{mem}} $) in tumor formation and regulation. Using the Xenopus laevis model, it demonstrates how depolarization is a key bioelectric marker and functional driver of tumor-like structures (ITLSs). Furthermore, it explores hyperpolarization as a potential strategy for suppressing tumorigenesis.

---

#### Key Contributions

1. **Bioelectric Signature of Tumors**:
   - Depolarized $ V_{\text{mem}} $ is identified as a consistent marker for ITLSs induced by oncogenes such as Gli1, KrasG12D, Xrel3, and mutant p53.  
   - This bioelectric signature appears before morphological or histological signs of tumor formation.

2. **Functional Role of $ V_{\text{mem}} $**:
   - Depolarization of cells promotes tumor-like behaviors such as overproliferation and invasion.  
   - Hyperpolarization, achieved through ion channel expression, suppresses ITLS formation.

3. **Molecular Mechanism**:
   - The sodium-butyrate transporter SLC5A8 mediates the effects of $ V_{\text{mem}} $ on tumorigenesis.  
   - Butyrate influx, driven by hyperpolarization, suppresses ITLSs through histone deacetylase (HDAC) inhibition.

4. **Predictive and Therapeutic Potential**:
   - $ V_{\text{mem}} $ serves as a non-invasive diagnostic marker for tumors.  
   - Hyperpolarization provides a novel therapeutic strategy to normalize tumors.

---

### Formalism

1. **Bioelectric Signature**:
   - Depolarization of $ V_{\text{mem}} $ occurs in ITLSs and precursor sites:
     $$
     V_{\text{mem}} = \frac{RT}{F} \ln\left(\frac{[K^+]_{\text{out}}}{[K^+]_{\text{in}}}\right)
     $$
     - Depolarization promotes tumorigenic pathways, whereas hyperpolarization restores normal cell behavior.

2. **Hyperpolarization Suppression Mechanism**:
   - Ion channels (e.g., Kir4.1, GlyR-F99A) are used to hyperpolarize cells:
     $$
     \Delta V_{\text{mem}} = \text{Hyperpolarizing Ion Flux}
     $$
   - This change leads to an increase in butyrate influx via SLC5A8:
     $$
     J_{\text{butyrate}} = SLC5A8 \cdot \text{[Butyrate]}_{\text{extracellular}}
     $$

3. **Butyrate and HDAC Inhibition**:
   - Butyrate acts as an HDAC inhibitor to regulate gene expression:
     $$
     \text{HDAC Activity} \propto \frac{1}{\text{[Butyrate]}}
     $$
     - High butyrate levels lead to histone hyperacetylation, resulting in cell cycle arrest and reduced proliferation:
       $$
       \text{Gene Expression} \propto \text{Histone Acetylation}
       $$

4. **Predictive Metrics for Tumor Formation**:
   - Sensitivity ($ S $) and Specificity ($ Sp $) are calculated based on depolarized foci predicting ITLS:
     $$
     S = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
     $$
     $$
     Sp = \frac{\text{True Negatives}}{\text{True Negatives} + \text{False Positives}}
     $$

---

### Applications

1. **Diagnostic**:
   - Non-invasive imaging using fluorescent voltage-sensitive dyes detects $ V_{\text{mem}} $ changes as early tumor markers.

2. **Therapeutic**:
   - Targeting ion channels to induce hyperpolarization suppresses tumor development, even in oncogene-expressing cells.

3. **Future Directions**:
   - Exploration of spatiotemporal dynamics of $ V_{\text{mem}} $ for optimizing tumor suppression strategies.
   - Development of therapies leveraging bioelectric modulation in clinical settings.

Let me know if you'd like more details on specific parts of the study!


### Title and Authors
**Title**: Bioelectric Gene and Reaction Networks: Computational Modelling of Genetic, Biochemical, and Bioelectrical Dynamics in Pattern Regulation  
**Authors**: Alexis Pietak and Michael Levin  
**Publication**: Journal of the Royal Society Interface, 2017  

### Summary and Formalism

#### Objective
The paper develops the **Bioelectricity-Integrated Gene and Reaction (BIGR)** network framework. This framework combines **gene regulatory networks (GRNs)**, **reaction-diffusion models**, and **bioelectric signals** to study biological patterning, regeneration, and anatomical control mechanisms.

---

#### Key Contributions
1. **Integration of Bioelectric Signals into GRNs**:
   - Extends traditional GRNs to incorporate bioelectric signals such as transmembrane potential (\(V_{mem}\)).
   - Models feedback loops between \(V_{mem}\), gene expression, and biochemical reactions.

2. **Hybrid Modeling Approach**:
   - Incorporates voltage-sensitive dynamics, ion transport, and signaling molecule interactions.
   - Uses computational simulations to study \(V_{mem}\)-regulated concentration patterns, positional information, and regeneration.

3. **Mechanistic Insights**:
   - Identifies mechanisms for memory, hysteresis, and polarity regulation.
   - Explains phenomena like axial regeneration polarity in planaria.

4. **Applications**:
   - Models of planarian regeneration demonstrate \(V_{mem}\)-driven patterning and state stability.
   - BIGR networks provide hypotheses for bioelectric control in developmental and regenerative biology.

---

#### Formalism and Algorithmic Framework

1. **Regulatory Network Elements**:
   - **Nodes**: Concentrations of substances (e.g., ions, gene products, signaling molecules).
   - **Edges**: Activation or inhibition using Hill functions:
     - Activation: \( a_A = \frac{[A]/K_A^{n_A}}{1 + ([A]/K_A)^{n_A}} \)
     - Inhibition: \( b_A = \frac{1}{1 + ([A]/K_A)^{n_A}} \)

2. **Steady-State Dynamics**:
   - Describes relationships between \(V_{mem}\) and ion concentrations:
     \[
     \frac{dV_{mem}}{dt} = -\frac{1}{C_{mem}} J_{mem}, \quad J_{mem} = \sum_i z_i F J_i
     \]
   - Uses the Goldman-Hodgkin-Katz (GHK) equation to model ion flux.

3. **Feedback Mechanisms**:
   - \(V_{mem}\) modulates ion channel states, which in turn regulate \(V_{mem}\).
   - Chemical reactions and \(V_{mem}\) dynamics are interlinked:
     \[
     r_{\text{reaction}} = k_f \prod \left(\frac{[X]}{K_X}\right) - k_r \prod \left(\frac{[Y]}{K_Y}\right)
     \]

4. **Forced Cycle Perturbation**:
   - Simulates transient changes in membrane permeability (e.g., for Na\(^+\) and K\(^+\)) to study hysteresis and memory:
     - Functions \(f(t)\) and \(g(t)\) control permeability modulation.
     - \(V_{mem}\) hysteresis loop area indicates memory capacity.

5. **Gap Junction Coupling**:
   - Models ion and molecule diffusion between cells using:
     \[
     F^{\text{gj}} = -D_i \nabla c - \frac{z_i F}{RT} c \nabla V
     \]

6. **Simulation Environment**:
   - Implemented in the **BioElectric Tissue Simulation Engine (BETSE)**.
   - Simulates ion transport, \(V_{mem}\) patterns, and network-level dynamics.

---

#### Applications Highlighted in the Paper

1. **Planarian Regeneration**:
   - Demonstrates anterior-posterior polarity restoration through \(V_{mem}\)-driven signaling.
   - Explores the role of gap junctions in \(V_{mem}\) gradient maintenance.

2. **Pattern Formation**:
   - Simulates emergent \(V_{mem}\) stripes and spots linked to signaling molecule gradients.

3. **Network Analysis**:
   - Explores memory, homeostasis, and state-switching in bioelectric circuits.

---

Let me know if you want further details or specific parts of this formalism elaborated! CHECK