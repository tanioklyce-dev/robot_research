---
title: "Sexual dimorphism in the complete Drosophila male central nervous system connectome (Berg, Beckett, Costa, Schlegel, Januszewski … Rubin, Jefferis; Cell 2026)"
type: source
url: https://doi.org/10.1016/j.cell.2026.08.015
local_path: raw/2025-10-30-male-cns-connectome-biorxiv-v2.txt
sha256: b5e7529ac96defbf3cd5fbf2b7de3df34ddeadec399318a1f19ec680a3c552aa
author: "Stuart Berg*, Isabella R. Beckett*, Marta Costa*, Philipp Schlegel*, Michał Januszewski*, Elizabeth C. Marin*, Aljoscha Nern*, Stephan Preibisch*, Wei Qiu*, Shin-ya Takemura* … Harald F. Hess, Gerald M. Rubin†, Gregory S.X.E. Jefferis† (111 authors in the Cell version; 100 on the preprint)"
affiliations: "HHMI Janelia FlyEM Project Team; MRC Laboratory of Molecular Biology and Dept. of Zoology, University of Cambridge (Cambridge Drosophila Connectomics Group); Google Research Connectomics (Zürich, Mountain View); Oxford, Champalimaud, Columbia, Harvard, CNR"
published: 2026-09-03
venue: "Cell (online 2026-09-03); preprint bioRxiv 10.1101/2025.10.09.680999 v1 2025-10-09, v2 2025-10-30 (PMC12636603, CC BY)"
format: paper (journal version not obtained; preprint v2 full text ~35k words via Europe PMC JATS XML)
doi: 10.1016/j.cell.2026.08.015
project_page: https://male-cns.janelia.org/
secondary_urls:
  - https://research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/ (Google Research blog, 2026-09-03; snapshot raw/2026-09-03-google-research-male-fly-connectome-blog.md)
  - https://www.janelia.org/project-team/flyem/male-cns-connectome (Janelia project page; data access)
  - https://www.hhmi.org/news/scientists-complete-full-map-fruit-fly-brain-connectome (HHMI news)
license: "dataset CC BY 4.0 (Janelia); preprint CC BY"
tags: [connectome, drosophila, male-cns, ventral-nerve-cord, neck-connective, sexual-dimorphism, flood-filling-networks, FIB-SEM, hhmi-janelia, google-research, flywire, neuprint, sensorimotor, primary-source]
ingested: 2026-09-12
---

# Sexual dimorphism in the complete Drosophila male central nervous system connectome

## Summary

**The first complete, proofread, synaptic-resolution wiring diagram of an adult animal's entire central nervous system — brain, both optic lobes, and ventral nerve cord (VNC) from a single male fruit fly — and the first male fly brain.** Seven enhanced FIB-SEM microscopes imaged **160 teravoxels at 8 nm isotropic** over 13 months; Google's flood-filling networks segmented the volume; **44 person-years** of proofreading produced **166,691 neurons**, **11,691 cell types**, 46 M presynapses connected to 312 M postsynaptic densities, and a connectome graph of **25.6 M edges**. Because the **neck connective is intact**, the dataset joins what earlier datasets split — the female brain ([FlyWire](../entities/flywire.md), hemibrain) and the male/female nerve cords (MANC, FANC) — so *"full sensory-to-motor circuits"* can be traced in one animal, *"from eyes to legs in one go"* as Jefferis put it to Janelia's news office.

The paper's science is comparative: against the female FlyWire brain it finds **7,205 isomorphic, 114 dimorphic, 262 male-specific and 69 female-specific** cell types (preprint counts) — sex-specific and dimorphic neurons are **4.8% of the male and 2.4% of the female central brain**, concentrated in higher-order centres while *"the sensory and motor periphery are largely isomorphic."* Dimorphism nonetheless *"propagates through the nervous system via dimorphic connectivity"*: small differences in wiring reach brain-wide, and *"numerous circuit switches reroute sensory information to form antagonistic circuits controlling opposing behaviours."* Three companion papers published the same day use the dataset for the visual system, the gustatory system, and social behaviour.

> [!note] Which edition this page reads, and what the journal version changed
> The **Cell** version (2026-09-03, 111 authors) could not be fetched; this page is written from the **bioRxiv v2 preprint** (2025-10-30, 100 authors), which the Janelia site itself points to as *"the manuscript describing the dataset."* Search-engine summaries of the Cell abstract give **166,700 neurons, 11,710 types, 8,069 isomorphic / 138 dimorphic / 289 male-specific / 71 female-specific** — every comparative count revised upward between preprint and journal, consistent with the **MaleCNS v0.9 → v1.0** data release (2025-10-03 → 2026-06-08) in between. The wiki holds the preprint numbers as read and the journal numbers as reported; neither should be quoted as the other. Edition history below.

## Key claims

### The dataset (Results, "A complete connectome of a whole male CNS")

| Quantity | Value |
|---|---|
| Imaging | 7 eFIB-SEM systems, 13 months, **160 teravoxels**, 8×8×8 nm, 0.082 mm³ |
| Segmentation | flood-filling networks (Google); 46 M presynapses / 312 M PSDs auto-detected, precision/recall 0.82/0.81 |
| Proofreading | **~44 person-years**; all fragments with >100 synapses; 98.9% of 141,780 detected nuclei belong to a proofread neuron |
| Neurons | **166,691** (incl. sensory axons); graph of **25.6 M edges** between 166,391 neurons |
| Cell types | **11,691** |
| Completeness | 94% pre- / 42% postsynaptic; **40.1%** of connections with both ends in proofread neurons — the metric the authors propose as the more useful one |
| Annotations | superclass (direction of flow), hemilineage, cell type; *fruitless*/*doublesex* expression; neurotransmitter predictions; motor neurons annotated with exit nerve and muscle innervation |
| Access | neuPrint, Clio, Neuroglancer, MaleCNS Cell Type Explorer, natverse `malecns`; **CC BY** |

- Some R1–6 photoreceptors at the volume edge and some sensory/motor neurons were not reconstructable — *"a small number of cells."*
- *"Going forwards we suggest that the fraction of synaptic connections for which both pre- and postsynaptic sites belong to a proofread neuron is more useful"* than the conventional per-site completion rates.

### Sensory-to-motor flow (Results, "Information flow from sensory to motor")

- Information *"primarily traverses the CNS in a feedforward manner"*: in via brain and VNC nerves, out *"mostly via VNC motor neurons."* Feedforward connections are predominantly excitatory; feedback connections have *"a larger inhibitory proportion."*
- **The neck connective is a bottleneck and an integrator.** Descending neurons constrain brain→VNC flow, ascending neurons VNC→brain, but *"neck connective neurons are integrators not just simple relays"*: ascending neurons output as many synapses onto VNC-intrinsic neurons as descending neurons do, and receive more from VNC-intrinsic neurons than from direct sensory input. They *"participate in the majority of feedback connections."*
- Maximum-flow analysis is used to find bottlenecks from sensors to effectors across the whole CNS — possible only because the connective is intact.

### Dimorphism (Results, "Identifying sexually dimorphic circuit elements" onward)

- Three classes: **isomorphic** (matched type and connectivity in both sexes), **dimorphic** (present in both, differently wired), **sex-specific**. Preprint: 7,205 / 114 / 262 male-specific + 69 female-specific; discussion sums these as *"331 sex-specific and 114 sexually dimorphic cell types."*
- High but incomplete correspondence with *fruitless*/*doublesex* expression; validation against prior clone data (e.g. 2,905 *fru*+ neurons in males vs 1,994 ± 76 expected).
- Sex differences concentrate in higher centres; *"within higher centres, male-specific connections are organised into hotspots defined by male-specific neurons or arbours."*
- Per-modality comparisons (visual, auditory, olfactory, gustatory) plus a connectivity-based method for finding dimorphic *edges*, contrasted with morphology-based typing; dimorphic neurons are *"strongly clustered and interconnected."*

### Companion papers (same day; not ingested)

- [**The organization of visual pathways in the Drosophila brain**](male-cns-visual-pathways-paper.md) — Hoeller, Zhao, Nern, Rogers, Romani, Reiser; *Cell*, doi 10.1016/j.cell.2026.08.014. (abstract-level page)
- [**The complete gustatory connectome of adult Drosophila**](male-cns-gustatory-connectome-paper.md) — Tastekin … Jefferis, Ribeiro; *Cell*, doi 10.1016/j.cell.2026.08.016. (abstract-level page)
- [**Networks of sexually dimorphic neurons that regulate social behaviors in Drosophila**](dimorphic-social-networks-paper.md) — Rubin, Managan, Dreher … Branson, Schretter, Otopalik; *Current Biology*, doi 10.1016/j.cub.2026.08.013. (abstract-level page)

The [Google Research post](../../raw/2026-09-03-google-research-male-fly-connectome-blog.md) adds two things the paper does not: the reconstruction pipeline's successor **PATHFINDER** (synthetic neurons in training data), and that a **complete female brain + nerve cord** map has also appeared in *Nature* (s41586-026-10735-w, uningested) — so both sexes now have whole-CNS connectomes.

## Edition history

| Edition | Date | Neurons | Types | Isomorphic / dimorphic / male-sp. / female-sp. | Authors |
|---|---|---|---|---|---|
| bioRxiv v1 | 2025-10-09 | — | — | — | — |
| **bioRxiv v2 (this page's local copy)** | 2025-10-30 | 166,691 | 11,691 | 7,205 / 114 / 262 / 69 | 100 |
| Cell (abstract verified via PubMed 42691995; body not read) | 2026-09-03 | 166,700 | 11,710 | 8,069 / 138 / 289 / 71 | 111 |

The MaleCNS data release moved from v0.9 (2025-10-03) to v1.0 (2026-06-08) between the two; the Google Research blog quotes **125 M synaptic connections**, a figure not in the preprint text. The female [BANC](banc-brain-and-cord-connectome-paper.md) map (Nature, 2026-06-08) is the companion dataset the Google post calls the *"complete female fruit fly brain and nerve cord map"*; its own paper leads with control architecture rather than sex (which gives 46 M presynapses → 312 M PSDs, 25.6 M graph edges). Re-fetch the Cell version when accessible and reconcile.

## Why it matters in this wiki

- **Closes the dataset gap the wiki flagged.** The [connectome](../concepts/bio/connectome.md) page's fly-simulation line had a brain-only model ([Shiu et al.](shiu-fly-brain-paper.md), on FlyWire) and a body-only model ([flybody](flybody-paper.md)), with nerve-cord wiring from other animals. This is the first same-animal brain + VNC map with an intact neck connective, and it annotates motor neurons down to **exit nerve and muscle** — the interface a brain-to-body simulation needs.
- **The neck connective as an architectural finding.** Descending/ascending neurons are a bottleneck *and* integrators, and carry most feedback. For anyone modelling a fly (or drawing analogies to hierarchical robot control), the brain–body interface is not a thin command channel.
- **Scale and cost.** 44 person-years of proofreading on top of automated segmentation is the current price of one complete insect CNS; the Google post frames PATHFINDER as the attempt to bring that down.
- **A bridge to embodied control already exists**: [FlyGM](flygm-connectome-graph-controller-paper.md) (Jin, Zhu, Zhang, Sui, Tsinghua, 2026) instantiates the FlyWire whole-brain graph as a message-passing RL controller for flybody and beats rewired, random, MLP and GNN controls. With this dataset or [BANC](banc-brain-and-cord-connectome-paper.md) the efferent set could be the real motor neurons.

## Entities mentioned

- [HHMI Janelia](../entities/hhmi-janelia.md) — FlyEM Project Team; Rubin, Hess, Reiser, Card, Jayaraman among senior authors.
- [FlyWire](../entities/flywire.md) — the female brain the comparison is made against (its annotations updated here).
- [Drosophila melanogaster](../entities/drosophila.md).
- Google Research Connectomics (Januszewski, Jain), MRC LMB / Cambridge (Jefferis, Schlegel, Costa, Marin) — no entity pages.

## Concepts touched

- [Connectome](../concepts/bio/connectome.md) — first complete adult CNS; the neck-connective finding.
- [Biomechanical simulation](../concepts/bio/biomechanical-simulation.md) — the brain-side dataset for a flybody-style closed loop.

## Open questions

- **Journal-version numbers.** Obtain the Cell text and reconcile the revised counts and the "125 M connections" figure.
- **How much of the 60% incomplete-connection fraction matters** for circuit-level simulation — the authors' own proposed metric says 40.1% of connections are fully proofread at both ends.
- **Individual variability vs sex.** With one male and one female, every difference is confounded with individual variation; the Google post says as much for isomorphic regions.
- **Muscle-level completeness** of the motor-neuron annotations for a full sensorimotor loop.
