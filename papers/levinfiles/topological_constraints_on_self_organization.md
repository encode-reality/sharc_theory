Here is an in-depth breakdown of the article "Topological Constraints on Self-Organization in Locally Interacting Systems," with a focus on the key formalisms:
# Topological constraints on self-organisation in locally interacting systems

[Paper](topological_constraints_on_self_organization.pdf)

---

### **1. Problem and Context**
The article investigates the conditions under which locally interacting systems can self-organize into an ordered phase. The focus is on how the topology of interaction graphs influences the system's ability to maintain long-range order. The study considers:
- Biological systems capable of self-organization (e.g., tissues and multicellular morphogenesis).
- Machine learning systems (e.g., autoregressive language models) that face challenges in achieving long-term coherence.

---

### **2. Key Formalisms**
#### **Graph-Theoretic Framework**
The system is modeled as a graph \( G \) with vertices representing interacting units and edges representing pairwise interactions. A graph Hamiltonian \( H \) is introduced to represent the interactions:
\[
H = \bar{H} \odot G,
\]
where \( \bar{H} \) is the matrix of coupling strengths, and \( \odot \) denotes element-wise multiplication.

#### **Windowed Hamiltonians**
- A **windowed Hamiltonian** \( H_u \) is defined for localized interactions within a finite window \( \omega \). 
- A **local Hamiltonian** is the sum of windowed Hamiltonians:
\[
H = \sum_u H_u,
\]
capturing interactions within overlapping windows across the graph.

#### **Scaling of Free Energy**
Key quantities:
- Change in free energy \( \Delta F \) is given by:
\[
\Delta F = \Delta E - T \Delta S,
\]
where \( \Delta E \) is the energy change and \( \Delta S \) is the entropy change.
- Ordered phases exist if the scaling of entropy \( O(f_S(P)) \) matches the scaling of energy \( O(f_E(P)) \), where \( P \) is the domain wall perimeter.

---

### **3. Theoretical Results**
#### **Topological Equivalence Theorem**
The authors show that systems with identical graph topology have equivalent asymptotic free energies, irrespective of interaction details. This is formalized as:
\[
F \sim F_0 + \langle H - H_0 \rangle_0,
\]
where \( F_0 \) is the free energy of a reference system with equivalent topology.

#### **Application to the Potts Model**
The Potts model, a generalization of the Ising model, is analyzed:
- Domain wall formation disrupts order.
- In 1D systems, thermal fluctuations always favor disorder, precluding long-range order.

#### **Autoregressive Models**
These models, used in language processing, are interpreted as one-dimensional systems with local Hamiltonians. The analysis shows:
- Finite context windows inherently limit long-range coherence.
- The inability to converge to a single ordered state stems from entropy scaling.

#### **Hierarchical Systems**
Multiscale systems (e.g., biological tissues) are studied:
- **Cliques** (complete subgraphs) represent localized order.
- Interaction between cliques allows global disorder while maintaining local order.
- Hierarchical structures enable complex patterns by embedding local coherence into broader irregularity.

---

### **4. Methodology**
#### Steps for Analyzing Systems:
1. **Start in an ordered configuration.**
2. **Create a domain wall.**
3. **Estimate the energy gain \( \Delta E \).**
4. **Analyze the asymptotic scaling of free energy \( \Delta F \).**

The methodology simplifies the combinatorics by leveraging the constraints of windowed Hamiltonians.

---

### **5. Implications and Applications**
- **Biological Systems:** The hierarchical and multiscale structure of biological systems enables self-organization over large scales.
- **Machine Learning Systems:** Current natural language models lack the topological features necessary for long-range coherence.
- **Future Directions:** Proposes designing systems with hierarchical and stigmergic architectures inspired by biological systems to enhance self-organizing capabilities.

---

### **6. Summary of Formal Theorems**
- **Proposition 1:** Ordered phases exist if entropy and energy scalings are equivalent.
- **Theorem 1:** Systems with identical graph topology exhibit equivalent asymptotic free energies.
- **Theorem 2:** One-dimensional local Hamiltonians cannot maintain long-range order at non-zero temperatures.
- **Theorem 4:** Hierarchical systems allow for parameter regimes where local cliques maintain order while global order is absent.

---

Let me know if you'd like a detailed explanation of any specific formalism or derivation!