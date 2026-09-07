---
title: Black Forest Labs
type: entity
subtype: company
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [black-forest-labs, flux, robin-rombach, patrick-esser, germany, freiburg, generative-models, flow-matching, physical-ai, video-generation, self-flow]
---

# Black Forest Labs

German generative-media lab, best known for the **FLUX** family of image models, now a **physical-AI** entrant. Founded by the team behind Stable Diffusion / latent diffusion — **Robin Rombach** (CEO) and **Patrick Esser** appear as authors on its research; hiring is stated as *"Germany and the US."*

The wiki's entry point is the [FLUX 3 launch](../sources/flux-3-launch.md) (2026-07-23), where the lab's self-description shifts from image generation to *"real-world visual intelligence: models that perceive, predict, and **act** across physical and digital environments."*

## Why it has a page

Because it is the clearest instance of a thesis this wiki has been tracking from the research side arriving as a **product roadmap**: that **predicting video forces you to learn physics**, and that a model good enough to generate video is therefore already most of a manipulation policy.

> If one model does both, it was never really only a content creation model. **It is a model of how the world behaves, and content creation is one thing one can do with it.**

Their compute allocation is the evidence they offer: **video prediction is over 95% of FLUX 3's total training compute**, because getting contact, motion, weight and cause-and-effect wrong *"looks wrong."* Audio is under 0.5% of tokens; actions are *"a low dimensional representation of a robot's state."* Content creation and physical AI are presented as **two applications of one backbone**, not two products.

That makes BFL a **different kind of entrant** from every robotics company in this wiki: it did not build a robot, a teleoperation fleet, or a robot dataset. It built a video model and rented the physics.

## Artifacts

| | |
|---|---|
| **FLUX 1 / FLUX 2** | image generation (FLUX 2, FLUX 2 Klein, FLUX 2 Max on their model page) |
| **[FLUX 3](flux-3.md)** (2026-07-23) | multimodal — image, video+audio, and **action** — from one backbone |
| **FLUX-mimic** | video-action model built with [mimic robotics](mimic-robotics.md) on the FLUX 3 backbone; **deployed at Audi** |
| **Self-Flow** ([arXiv 2603.06507](https://arxiv.org/abs/2603.06507), ICML 2026) | the mechanism: **Dual-Timestep Scheduling** — heterogeneous noise levels across tokens, unifying representation learning with generation. Chefer, Esser, Lorenz, Podell, Raja, Tong, **Torralba** (MIT), Rombach. **Not ingested; abstract only.** |

The lab also runs a public policy line — a blog post titled *"our co-founder and CEO urges G7 leaders to back open innovation"* — and its FLUX 3 launch plan includes an **open-weight tier ("FLUX 3 Dev") that is stated to cover action prediction**. Announced, not shipped.

> [!note] Thin, and vendor-sourced
> Everything here comes from BFL's own blog. Funding, headcount, revenue, and the FLUX 1/2 history are not asserted. The Self-Flow paper and the [mimic-video](https://arxiv.org/abs/2512.15692) paper are the technical primaries beneath the claims and neither is ingested.

## Related

- [FLUX 3](flux-3.md) · [mimic robotics](mimic-robotics.md)
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md) — BFL is now the strongest commercial argument on the generative side.
- [World-action model](../concepts/world-models/world-action-model.md) — the model class FLUX-mimic belongs to.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — where the Audi deployment lands.

## Mentioned in

- [FLUX 3 and FLUX-mimic launch](../sources/flux-3-launch.md)
