---
title: Whole-organism agentic AI — brain + body for the fruit fly
type: synthesis
created: 2026-05-08
updated: 2026-05-08
revised: NeuroMechFly v2 ingested 2026-05-08 — body side now has two parallel open-source platforms
tags: [drosophila, connectome, biomechanical-simulation, embodied-ai, flywire, flybody, neuromechfly, brain-body]
---

In late 2024 through 2026 several independent research lines reached an inflection point on the same target organism:

- **Brain side.** [FlyWire](../../entities/flywire.md) released a complete adult *Drosophila melanogaster* connectome (139,255 neurons, ~50M synapses). Two open-source code paradigms exist for *using* it: Phil Shiu's UC Berkeley team turned it into a leaky-integrate-and-fire **dynamical brain simulation that runs on a laptop** ([Shiu et al. 2024](../../sources/shiu-fly-brain-paper.md), code: [Drosophila brain model](../../entities/drosophila-brain-model.md), MIT). Lappalainen et al. trained a connectome-constrained deep network that **predicts single-neuron activity across the fly visual system** ([Lappalainen et al. 2024](../../sources/lappalainen-flyvis-paper.md), code: [flyvis](../../entities/flyvis.md), MIT, v1.1.3 March 2026).
- **Body side.** Two parallel open-source platforms now exist for the same fly:
  - [flybody](../../entities/flybody.md) — HHMI Janelia + Google DeepMind, *Nature* 2025. Walking + flight unified, deep-RL end-to-end. Vanilla MuJoCo. Apache-2.0.
  - [NeuroMechFly](../../entities/neuromechfly.md) v2 — EPFL [NeLy lab](../../entities/nely-epfl.md), *Nature Methods* 2024 (model) + flygym v2.x.x package, ongoing through April 2026. Walking + **vision** + **olfaction** + **mechanosensory feedback** + brain↔VNC hierarchical control. MuJoCo with optional Warp/MJWarp GPU backend (~300× speedup). Apache-2.0.

For the first time, both halves of an "agent loop" exist in open form for the **same animal at full scale**. This is the first plausible target for *whole-organism agentic AI*: a brain + body + environment system where every neuron and every joint is anatomically grounded. As of May 2026, the body side has *two* viable platforms with sharp capability differences (see table below) — choosing one is a real engineering decision, not a default.

## Why this is different from robotics-flavoured agentic AI

The wiki's main throughline — VLAs, world models, sim-to-real, generalist policies — answers *"how do we make a robot useful?"* The fly program answers *"can we simulate an entire animal end-to-end?"* They share tooling (MuJoCo, deep RL, imitation learning, hierarchical control) but the **success criterion** is different:

| Axis | Robotics-flavoured agentic AI | Whole-organism agentic AI |
|---|---|---|
| Goal | Deploy on real robot | Match real animal behaviour & neural activity |
| Body model | Idealized robot URDF / USD | Anatomical reconstruction from microscopy |
| Controller | VLA, BC policy, RL policy | Same RL toolkit, but ultimately connectome-constrained |
| Validation | Real-hardware task success | Behavioural & single-neuron prediction accuracy |
| Time horizon | Months → product | Decade → mouse → human |

The two threads are converging on overlapping software (both lean on MuJoCo, dm_control, deep RL imitation), but the **scientific questions diverge sharply** at the controller layer.

## What's already there (May 2026)

| Component | Status | Source |
|---|---|---|
| Adult fly **connectome** (brain) | Done; public | [FlyWire](../../entities/flywire.md) (Dorkenwald et al. 2024) |
| Adult fly **VNC** connectomes (M+F) | Done; public | flybody refs 55–58 |
| **Brain dynamics simulation** (LIF) | Done, behaviourally validated; runs on laptop; MIT-licensed code | [Shiu et al. 2024](../../sources/shiu-fly-brain-paper.md), [Berkeley News](../../sources/berkeley-fly-brain-news.md) |
| **Body model** + walking + flight | Done; open-source (Apache-2.0) | [flybody](../../entities/flybody.md) |
| **Body model** + walking + **vision + olfaction + mechanosensory** + brain–VNC hierarchy | Done; open-source (Apache-2.0); GPU-accelerated | [NeuroMechFly v2](../../entities/neuromechfly.md) ([flygym GitHub](../../sources/flygym-github.md), [website](../../sources/neuromechfly-website.md)) |
| **Vision-guided flight** | Done | [flybody Paper](../../sources/flybody-paper.md) Fig. 4 |
| **Connectome-constrained neural-activity prediction** | Done for the visual system; open-source PyTorch (`TuragaLab/flyvis`) | [Lappalainen et al. 2024](../../sources/lappalainen-flyvis-paper.md); Mi et al. 2022 (ICLR) |
| **Brain ↔ body integration** | **Open** — gestured at in flybody Discussion; no working stack | — |
| Real muscle actuation | **Open** — flybody uses torque actuators | flybody Discussion |
| Proprioceptor + mechanoreceptor models | **Open** — sensors are idealized | flybody Discussion |

## Two body platforms — capability split

| Axis | [flybody](../../entities/flybody.md) (HHMI Janelia + DeepMind) | [NeuroMechFly v2](../../entities/neuromechfly.md) (EPFL / NeLy) |
|---|---|---|
| **Walking** | ✓ (DMPO imitation against APT-tracked real flies) | ✓ |
| **Flight** | **✓ unique** — phenomenological aerodynamics + WPG | — |
| **Vision** | Eye cameras for vision-guided flight | Compound eyes; ommatidia hex lattice |
| **Olfaction** | — | **✓ unique** — antennae + maxillary palps |
| **Mechanosensory** | Largely idealized | ✓ explicit joint / actuator / contact |
| **Brain–VNC architecture** | Flat MLP/CNN policies | ✓ explicit descending + ascending |
| RL stack | DMPO + Acme + Reverb + Ray (CPU-distributed) | Not surveyed |
| GPU backend | — | ✓ Warp / MJWarp (~300× speedup) |
| Latest activity | *Nature* 2025 + Apache-2.0 GitHub | flygym v2.0.1 released **2026-04-17** |

The two are **complementary, not competitive**. A flight-and-vision integration target picks flybody; an olfaction-and-mechanosensory integration target picks NeuroMechFly. Both lay in MuJoCo and both ship Apache-2.0, so an ambitious agent could conceivably swap between them — though no one has yet built the bridge.

## What integration would look like

A serious "fly agent" would need a controller that:
1. Reads sensory observations from the body simulator (eye cameras + proprioceptors + mechanoreceptors in flybody; **+ olfaction + brain–VNC interfaces** in NeuroMechFly v2).
2. Encodes them as input into a neural model whose **connectivity is constrained by FlyWire** (per Lappalainen 2024) or driven by **mechanistic LIF over the FlyWire connectome** (per Shiu 2024).
3. Outputs motor commands to the body's torque / wing / adhesion actuators.
4. Closes the loop end-to-end at biologically plausible timescales (flybody control step is 0.2 ms for flight, 2 ms for walking; the brain simulation's natural timescale is also ~ms).

The body environments exist (flybody + NeuroMechFly v2). FlyWire already has the wiring. [Shiu et al. 2024](../../sources/shiu-fly-brain-paper.md) already showed mechanistic LIF on the full FlyWire connectome runs on a laptop and predicts feeding/grooming behaviour. [Lappalainen et al. 2024](../../sources/lappalainen-flyvis-paper.md) already showed connectome-constrained deep nets work on real visual-system activity. The integration is plausible; it's a research engineering task, not a science-fiction proposition. **The brain side and (one of the two) body sides are even under the same PI** — Srinivas Turaga at HHMI Janelia is senior on both flybody and flyvis.

A NeuroMechFly-flavoured integration would cross institutions (Turaga's connectome-constrained controllers + NeLy's body), but it would be the *more sensorily complete* agent loop, since flyvis-style controllers respond to visual input and Shiu-style LIF responds to taste/mechanosensory input — both of which NeuroMechFly v2 surfaces from its body, and flybody mostly does not.

## Why this might matter for the rest of the wiki

- **Stress test of the MuJoCo/imitation-learning recipe.** flybody is a 102-DoF body with wings, fluid dynamics, and adhesion. If DMPO + imitation can do that, it's another data point that the recipe scales beyond the rigid-arm/wheeled-base norm of robotics RL.
- **Interpretability lever.** A connectome-constrained controller is *interpretable in a way no VLA is* — you can trace the wiring back to identified neurons. If "which neurons drive looming-evasion?" becomes answerable in silico, the same template applies in mouse and eventually human.
- **An "alternate way to good AI."** Berkeley's framing. Whether biology-inspired controllers prove competitive with end-to-end deep nets is open. But the *fly is now the smallest viable test bed* for that question.

## What's missing in this wiki

- Source page for **Mi et al. 2022** (ICLR) — connectome-constrained latent-variable model; currently referenced only via flybody-paper bibliography.
- Entity pages for **Srinivas Turaga**, **Yuval Tassa**, **Josh Merel**, **Janne Lappalainen** — referenced but not stubbed. ([Phil Shiu](../../entities/phil-shiu.md) now filed.)
- **Virtual rodent** as its own entity (Merel et al. 2020, ICLR) — direct ancestor of flybody, currently only mentioned in passing.
- *C. elegans* and Hydra body sims — currently only one-line references.
- Brian 2 spiking-NN simulator — substrate under [Shiu et al. 2024](../../sources/shiu-fly-brain-paper.md); entity page on demand.

The two open-source code artifacts are now filed as entities: [Drosophila brain model](../../entities/drosophila-brain-model.md) (Shiu's Brian 2 + LIF) and [flyvis](../../entities/flyvis.md) (TuragaLab's PyTorch connectome-constrained DMN). These are the concrete reproducibility surfaces for the brain side.

Other items deferred until the wiki has reason to dig into them more deeply.

## Related

- [flybody](../../entities/flybody.md) — body simulator (HHMI Janelia + DeepMind).
- [NeuroMechFly](../../entities/neuromechfly.md) — body simulator (NeLy / EPFL).
- [FlyWire](../../entities/flywire.md) — brain connectome.
- [Drosophila brain model](../../entities/drosophila-brain-model.md), [flyvis](../../entities/flyvis.md) — brain-side code artifacts.
- [Drosophila melanogaster](../../entities/drosophila.md) — model organism.
- [Connectome](../../concepts/bio/connectome.md) — concept.
- [Biomechanical simulation](../../concepts/bio/biomechanical-simulation.md) — concept.
- [Imitation learning](../../concepts/learning/imitation-learning.md) — shared training paradigm.
- [MuJoCo](../../entities/mujoco.md) — shared physics substrate with mainstream robotics.

## Sources

- [Berkeley News — researchers simulate an entire fly brain on a laptop](../../sources/berkeley-fly-brain-news.md)
- [flybody Paper (Vaxenburg et al. 2025, Nature)](../../sources/flybody-paper.md)
- [flybody GitHub](../../sources/flybody-github.md)
- [Shiu et al. 2024 — A Drosophila computational brain model (Nature)](../../sources/shiu-fly-brain-paper.md)
- [Lappalainen et al. 2024 — Connectome-constrained networks predict fly visual-system activity (Nature)](../../sources/lappalainen-flyvis-paper.md)
- [flygym GitHub (NeLy-EPFL/flygym)](../../sources/flygym-github.md)
- [neuromechfly.org website](../../sources/neuromechfly-website.md)
