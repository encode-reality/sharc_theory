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

Stigmergic architectures are systems that leverage **stigmergy**, a mechanism of indirect coordination through the environment. This term was originally introduced in the context of social insects, like ants and termites, and has since been expanded to apply to biological, computational, and organizational systems.

### **Key Concepts of Stigmergy**
1. **Indirect Coordination:** Agents do not communicate directly but influence one another by modifying a shared environment. These modifications act as signals or cues for other agents to respond to.
   - Example: Ants deposit pheromones to guide others toward a food source.

2. **Self-Organization:** Through local interactions and feedback loops, complex global patterns or behaviors emerge without centralized control.

3. **Environmental Memory:** The shared environment serves as a medium for storing information about the system's state or goals, guiding future actions.

---

### **Stigmergic Architectures in Different Domains**
Stigmergic architectures have been proposed in several areas to achieve coordination and self-organization:

#### 1. **Biology**
   - Cells in biological systems often coordinate their activities by secreting and responding to chemical signals in their environment. For example:
     - **Tissue development:** Cells release growth factors that guide their neighbors in forming complex structures.
     - **Bacterial colonies:** Bacteria use quorum sensing to regulate group behavior based on local chemical concentrations.

#### 2. **Artificial Intelligence and Robotics**
   - **Swarm Intelligence:** Robots or agents operate independently but coordinate via stigmergic signals. Applications include:
     - Robotic swarms for search and rescue.
     - Distributed pathfinding or resource allocation.
   - **Reinforcement Learning:** The environment can serve as a feedback mechanism for training agents to optimize their behavior collaboratively.

#### 3. **Distributed Computing**
   - In distributed systems, nodes (or agents) interact indirectly through shared data structures (like distributed ledgers or blackboards). This avoids direct communication bottlenecks and enhances scalability.

#### 4. **Urban Planning and Human Systems**
   - **Crowd Behavior:** Humans coordinate in public spaces (like traffic or markets) through stigmergic principles, such as following implicit social rules or observing others' actions.
   - **Digital Collaboration Tools:** Platforms like wikis or open-source software repositories function stigmergically, where contributors build upon existing work without direct coordination.

---

### **Characteristics of Stigmergic Architectures**
1. **Decentralization:** Control is distributed, and no single agent oversees the system.
2. **Adaptability:** The system can dynamically adapt to changes in the environment or individual agents' behavior.
3. **Robustness:** The reliance on local rules and feedback makes these systems tolerant to failures or disruptions in individual components.

---

### **Applications of Stigmergic Architectures**
1. **Biologically Inspired Computing:**
   - Algorithms like ant colony optimization or particle swarm optimization are inspired by stigmergy.
2. **Social Computing:**
   - Platforms like GitHub or Wikipedia depend on contributors interacting with shared "stigmergic" artifacts (code, articles).
3. **Smart Systems:**
   - Smart cities can use stigmergic principles for traffic flow optimization, energy distribution, or emergency responses.
4. **Artificial Life:**
   - Simulating collective behavior in artificial ecosystems.

---

In the context of the paper you shared, stigmergic architectures are highlighted as an emergent property in biological systems that allow for **robust, scalable, and adaptive self-organization**. These architectures could inspire advancements in **machine learning**, enabling systems to better mimic the long-range coherence and adaptability found in nature.