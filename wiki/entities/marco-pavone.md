---
title: Marco Pavone
type: entity
subtype: person
created: 2026-08-16
updated: 2026-08-16
sources: 3
tags: [marco-pavone, stanford, autonomous-systems-lab, control-theory, safety, control-barrier-functions, nonlinear-control, robotics]
---

# Marco Pavone

Stanford roboticist and control theorist — Departments of **Mechanical Engineering** and **Aeronautics & Astronautics**, Stanford University; leads the **Autonomous Systems Lab (ASL)**. Co-author on five ingested sources, all on the same side of the field: **the control-theoretic layer underneath learned behavior**.

## Why he has a page

Because the wiki's coverage is heavily tilted toward learned policies, and Pavone appears each time the corpus reaches for the layer that *bounds* them. They form a coherent line rather than a coincidence:

- **[Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions](../sources/oscbf-paper.md)** (with Daniel Morton; IROS 2025) — **the wiki's first ingested control-barrier-function source.** CBFs inside an [operational space controller](../concepts/robotics/operational-space-control.md), with a task-consistent objective; 168 constraints at ~3 kHz, hardware on a [Franka Panda](franka-panda.md). Motivated in its first paragraph by learned policies that *"do not provide guarantees on safety"* — citing [Diffusion Policy](diffusion-policy.md).
- **[PACS — Path-Consistent Safety Filtering for Diffusion Policies](../sources/pacs-paper.md)** (with TUM's Römer, Balletshofer, Thumm, Schoellig and Althoff; ICRA 2026) — and this is the interesting one, because it partly **undercuts the paper above**. It shows that *reactive* safety filters, control barrier functions included, push a behavior-cloned policy off its demonstration manifold into unrecoverable out-of-distribution states: CBF filtering scores **0.04** average task success on robomimic where path-consistent braking scores **0.72**. Pavone is on both sides of that finding, which reads as a research line correcting itself rather than two camps disagreeing.
- **[Sentinel — Unpacking Failure Modes of Generative Policies](../sources/sentinel-paper.md)** (with Agia, Sinha and Bohg; CoRL 2024) — the third distinct attack on the same problem: not preventing harm but **detecting that the policy is failing**, by splitting failures into erratic (statistical temporal action consistency) and task-progression (VLM video QA) categories.
- **[Learning Control-Oriented Dynamical Structure from Data](../sources/learning-control-oriented-dynamical-structure.md)** (Richards, Slotine, [Azizan](navid-azizan.md), Pavone; ICML 2023) — SD-LQR: learn state-dependent-coefficient factorizations so a *learned* dynamics model retains the structure a stabilizing controller synthesis needs.
- Referenced in the [MIT drone adaptive control](../sources/mit-drone-adaptive-control.md) page as the senior author of that predecessor work.

The through-line: **make learned components admissible to classical control machinery** — by giving a learned model the structure a controller synthesis needs (SD-LQR), by wrapping a learned policy in a filter with an invariance proof (OSCBF), and then by measuring what that wrapping costs and fixing it (PACS). The third step is the one most research lines skip.

> [!note] Live-web facts not asserted here
> Pavone's other affiliations and roles (including industry positions) were not confirmed from an ingested source and are deliberately omitted. The affiliation on the ingested papers is Stanford; that is what this page claims.

## Related

- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — the hub page his two safety papers anchor.
- [Runtime failure detection](../concepts/robotics/runtime-failure-detection.md) — the third mechanism, from Sentinel.
- [Operational space control](../concepts/robotics/operational-space-control.md) — where the OSCBF work lands.
- [Navid Azizan](navid-azizan.md) — co-author on the ICML 2023 line.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — the certification frame his line of work would eventually feed.
- [Russ Tedrake](russ-tedrake.md) — the wiki's other model-based-control-meets-learning figure; the MIT/TRI stack OSCBF is the formal upgrade to.

## Mentioned in

- [Sentinel paper](../sources/sentinel-paper.md) — co-author.
- [PACS paper](../sources/pacs-paper.md) — co-author.
- [OSCBF paper](../sources/oscbf-paper.md) — senior author.
- [Learning Control-Oriented Dynamical Structure from Data](../sources/learning-control-oriented-dynamical-structure.md) — senior author.
- [MIT drone adaptive control](../sources/mit-drone-adaptive-control.md) — cited as senior author of the related ICML 2023 work.
