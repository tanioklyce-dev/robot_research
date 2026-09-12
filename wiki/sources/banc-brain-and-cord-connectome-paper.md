---
title: "Distributed control circuits across a brain-and-cord connectome — BANC (Bates et al., Nature 2026)"
type: source
url: https://doi.org/10.1038/s41586-026-10735-w
local_path: raw/2026-06-08-banc-brain-and-cord-connectome-nature.txt
sha256: f65379c82e18359b826d66939f50719564941019891796d1010435c75580d2a5
author: "Alexander Shakeel Bates … The BANC-FlyWire Consortium … Mala Murthy†, Jan Drugowitsch†, Rachel I. Wilson†, Wei-Chung Allen Lee† (91 authors)"
affiliations: "Harvard Medical School (Lee, Wilson, Drugowitsch labs); Princeton Neuroscience Institute (Murthy, Seung); Oxford; Cambridge/MRC LMB; Janelia; Allen Institute; Eyewire; BANC-FlyWire Consortium"
published: 2026-06-08
venue: "Nature (received 2025-08-01, accepted 2026-05-29); open access, PMC13518251; preprint 2025 on CAVE v626"
format: paper (version of record, ~38k words via Europe PMC JATS; figures and extended data absent)
doi: 10.1038/s41586-026-10735-w
project_page: https://banc.community
tags: [connectome, drosophila, female-cns, ventral-nerve-cord, BANC, flywire, distributed-control, local-feedback, descending-neurons, ascending-neurons, subsumption, embodied-cognition, transmission-EM, GridTape, primary-source]
ingested: 2026-09-12
---

# Distributed control circuits across a brain-and-cord connectome (BANC)

## Summary

**The female counterpart to the [male CNS connectome](male-cns-connectome-paper.md), and a paper with a thesis about control architecture rather than sex.** The BANC (Brain And Nerve Cord) team serially sectioned one adult female fly into **7,010 sections**, imaged them by transmission EM on GridTape at **4 × 4 × 45 nm**, segmented with CNNs, and proofread the expected **~160,000 neurons** with **155 proofreaders over ~3.5 years (~38.6 person-years)**, following FlyWire's community approach. Brain (~140,000 neurons) and ventral nerve cord (~20,000) are joined by **~1,300 descending and ~1,800 ascending neurons** — a connective that earlier brain-only and cord-only datasets had cut.

The analysis starts from the periphery. A new **adjusted-influence metric** — a linear dynamical-systems estimate of every neuron's steady-state effect on every other, cheap enough for billions of pairs — shows that **effector neurons (motor, endocrine, visceral efferent) are most strongly influenced by sensors in the same body part**: pharynx motor neurons by pharynx sensory cells, and so on for *"almost every body part."* These **local feedback loops** are linked by descending and ascending neurons that cluster into **behaviour-centric modules**, with single neurons *"positioned to influence the voluntary movements of multiple body parts, together with the endocrine cells or visceral organs that support those movements,"* and brain regions for learning and navigation *supervising* rather than commanding. The authors' summary, citing **Brooks (1986)** and **Maes (1993)**: an architecture *"distributed, parallelized and embodied, reminiscent of distributed control architectures in engineered systems."*

> [!note] Why a robotics wiki holds this paper
> Its Discussion sets three theories against one dataset — the *classical sandwich* (sense → central executive → act), the *ecological* view (no middle layer), and *embodied cognition* (modular distributed control tightly coupled to the body, *"an idea that takes inspiration from robotic design"*) — and reads the connectome as evidence for the third. The engineering references are the subsumption architecture and behaviour-based agents. The wiki's [control-abstraction-levels](../concepts/robotics/control-abstraction-levels.md) page and its whole-body-control thread are about exactly the sandwich-vs-distributed choice, from the other direction.

## Key claims

### The dataset (Main; Methods)

| Quantity | Value |
|---|---|
| Specimen | one adult female *D. melanogaster* |
| Imaging | 7,010 serial sections, GridTape TEM, 4 × 4 × 45 nm (public instance 8 × 8 × 45) |
| Missing | lamina and ocellar ganglion (as in the male CNS); present in FAFB |
| Reconstruction | CNN segmentation of cells, nuclei, mitochondria; synapse detection; neurotransmitter prediction extended across the CNS |
| Proofreading | 155 proofreaders, ~3.5 years, **~38.6 person-years**; every neck-connective axon verified at both anterior and posterior levels |
| Cross-checks | cell-type matches to FAFB (483,957 type-to-type connections) and MANC (434,357) |
| Access | banc.community; FlyWire Codex; CAVE (v888 for the print version, v626 for the preprint); Harvard Dataverse 10.7910/DVN/7WTH1N |

### A metric of influence

*"To interpret a whole brain-and-cord connectome, we need a way to estimate the influence of neuron A on neuron B for any pair of neurons."* Adjusted influence: inject a sustained signal at the source; each downstream neuron's activation is the input-fraction-weighted sum of its inputs; take the log of the target's steady-state response. Deterministic, linear, and *"inversely proportional to the network distance"*; agrees with prior path metrics without their hand-assigned layers. Unsigned.

### Local feedback modules

- Effectors are defined as motor neurons, endocrine cells and visceral efferents — and both sensors and effectors are *distributed*: the brain holds motor neurons for eyes, antennae, mouthparts and foregut; the VNC for legs, wings, halteres, abdomen, reproductive organs and hindgut.
- *"Most groups of effector neurons receive their strongest influence from sensors in the same body part"* — reciprocal loops, found *"in almost every body part,"* each also influenced by more distant sensors in functionally related parts.

### Behaviour-centric AN/DN modules

- DNs and ANs are *intermingled* when embedded by their direct connections — *"their connections can be similar."* Clustering by pre- and postsynaptic partners yields groups that map to behaviours (known functions colocalize; 9.3% of AN/DNs have a known function).
- *"Single ascending and descending neurons are often positioned to influence the voluntary movements of multiple body parts."* Modules interact with each other; the CNS as a whole partitions into **13 networks** (spectral clustering of 50,568 non-sensory, non-effector, non-optic neurons), and network-by-effector influence is strongly structured (n = 522,148 source–target observations).
- The central complex and mushroom body *supervise* — the worked example is the central complex correcting heading via ANs and DNs when target and actual directions misalign.

### The argument (Discussion)

> *"The classical theory is that actions are selected by a centralized executive brain function (sensing→cognition→action, the classical sandwich)… A radical alternative is the ecological theory, which dispenses with the middle layer… More recently, theories of embodied cognition have argued that sensing↔action loops could be implemented by a modular, distributed control architecture that is tightly connected to the body, an idea that takes inspiration from robotic design. Embodied cognition does not reject internal representations, but it argues that their role is limited."*

*"First, we found that the core elements of behavioural control are local feedback modules, in which effector neurons are influenced by the sensors positioned to monitor the relevant effectors."* The comparison the authors draw is to spinal and brainstem reflex loops and to Brooks's layered controller.

## Edition history

Preprint (2025, CAVE v626, Harvard Dataverse 10.7910/DVN/8TFGGB) → Nature version of record 2026-06-08 (CAVE v888, Dataverse 10.7910/DVN/7WTH1N, which *"supersedes"* the preprint deposit). This page reads the version of record.

## Why it matters in this wiki

- **Both sexes now have whole-CNS connectomes**: BANC (female, TEM, community-proofread, 2026-06) and the [male CNS](male-cns-connectome-paper.md) (FIB-SEM, Janelia-proofread, 2026-09). Two labs, two imaging modalities, two proofreading models, cross-matched to each other's cell types — the [connectome](../concepts/bio/connectome.md) page's "one animal, one map" caveat now has a second animal.
- **Distributed control, from the biology side.** The wiki's robotics pages argue about where control should live (a VLM planner over a fast controller; a monolithic policy; a whole-body controller with a semantic layer on top). This paper says the fly runs mostly on local sensor–effector loops with long-range coordination and light supervision — the Brooks answer — and cites the engineering literature for it.
- **The neck connective, measured from both sides.** The male CNS paper found the connective is a bottleneck *and* integrator carrying most feedback; BANC gives the counts (1,300 DNs, 1,800 ANs) and the behavioural clustering.
- **A brain-side substrate for closed-loop simulation** — the same role the male CNS page assigns to its dataset, now with an open CAVE/Codex toolchain and a community that has already built [FlyWire](../entities/flywire.md)-based models ([Shiu et al.](shiu-fly-brain-paper.md), [FlyGM](flygm-connectome-graph-controller-paper.md)).

## Entities mentioned

- [FlyWire](../entities/flywire.md) — the consortium model, Codex hosting, FAFB cross-matching.
- [Drosophila melanogaster](../entities/drosophila.md).
- [HHMI Janelia](../entities/hhmi-janelia.md) — Funke, Adjavon among authors; MANC cross-matching.
- Wei-Chung Allen Lee, Rachel Wilson, Jan Drugowitsch (Harvard), Mala Murthy, Sebastian Seung (Princeton) — no entity pages.

## Concepts touched

- [Connectome](../concepts/bio/connectome.md) — second complete adult CNS; the influence metric.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — a biological vote for distributed, local-loop control with supervision.
- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — brain-side dataset with motor-neuron effectors.

## Open questions

- **Neuron and synapse totals** for the final version are stated as "approximately 160,000" in the text read; the exact proofread count is in figures not captured.
- **Influence is unsigned.** Inhibition is not represented in the metric that carries the control-architecture argument.
- **Male vs female architecture.** Both papers say the sensory-motor periphery is largely shared; whether the *module* structure is, has not been compared.
- **Does anyone train a controller on BANC?** [FlyGM](flygm-connectome-graph-controller-paper.md) used FlyWire (brain only); BANC reaches the motor neurons.
