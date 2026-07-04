---
title: NVIDIA GR00T
type: entity
subtype: product
created: 2026-05-06
updated: 2026-07-04
sources: 16
tags: [groot, vla, nvidia, foundation-model, humanoid]
---

NVIDIA's open, commercially-licensed [VLA](../concepts/learning/vla-models.md) foundation model line for humanoid robots. The flagship policy that ships with NVIDIA's Physical AI stack ([NVIDIA Isaac Lab](nvidia-isaac-lab.md), [NVIDIA Isaac Sim](nvidia-isaac-sim.md)). **Both site champions of the [October 2025 Seeed × NVIDIA × HF Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md) ran GR00T N1.5** (fine-tuned via NVIDIA Brev) on non-humanoid dual-arm platforms (XLeRobot, SO-ARM101) — the strongest external signal yet that GR00T fine-tunes work at weekend-hackathon data scales (150–300 episodes) outside the humanoid form factor it was designed for.

## Versions seen
- **N1** — original release; **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** ([arXiv 2503.14734](https://arxiv.org/abs/2503.14734), Mar 2025); **full paper now ingested** — see [GR00T N1 Paper](../sources/groot-n1-paper.md). Corporate NVIDIA authorship (~50 contributors; research leads [Jim Fan](jim-fan.md) + [Yuke Zhu](yuke-zhu.md)). Featured in [NVIDIA GEAR Lab Publications](../sources/nvidia-gear-publications.md) as a top highlight.
- **N1.5** — winning policy at both sites of the October 2025 Seeed × NVIDIA × HF Embodied AI Hackathon; fine-tuned via [NVIDIA Brev](nvidia-brev.md); deployed on [Jetson Thor](jetson-thor.md).
- **N1.6** — referenced as the version newly available in [NVIDIA Isaac Lab](nvidia-isaac-lab.md) alongside Newton 1.0 GA at GTC 2026 ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)).
- **N1.7 Early Access** — 3B parameters, built on a Cosmos-Reason2-2B backbone, **[EgoScale](../sources/egoscale-paper.md) pretraining on 20,854 hours of egocentric human video** across 20+ task categories ([Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)). The EgoScale paper (Zheng et al., NVIDIA GEAR, Feb 2026) is the primary source for this corpus and publishes a clean log-linear scaling law `L = 0.024 − 0.003·ln(D)` (R² = 0.9983) relating human-data scale to validation loss — see [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md).

> [!warning] Version overlap
> N1.6 and N1.7 EA appear referenced in parallel — likely a GA + EA release pattern. The N1 primary paper is now on file ([GR00T N1 Paper](../sources/groot-n1-paper.md)); no N1.5/N1.6/N1.7 primary paper yet.

## N1 architecture & data (from the primary paper)

- **Dual-system VLA** ([GR00T N1 Paper](../sources/groot-n1-paper.md)): Eagle-2 VLM (SmolLM2 + SigLIP-2; System 2, 10 Hz) + flow-matching Diffusion Transformer (System 1, 120 Hz), trained jointly end-to-end. GR00T-N1-2B = 2.2B params (1.34B VLM); 16-action chunk in 63.9 ms on an L40; K=4 Euler steps at inference; VLM features taken from middle layer 12.
- **Data pyramid**: 8,375.7 h total pretraining corpus — real robot 3,288.8 h + human video 2,517 h + DexMimicGen sim 1,742.6 h + **827 h of video-model-generated "neural trajectories"** (~10× multiplier over the 88 h of in-house GR-1 teleop). ~50k H100 GPU-hours to pretrain.
- **Headline results**: real [Fourier GR-1](fourier-gr-1.md) tabletop 76.8% vs Diffusion Policy 46.4%; 10%-data GR00T within 3.8 points of full-data DP; sim average 45.0% vs DP 33.4% at 100 demos.
- Extends the [LeRobot](lerobot.md) dataset format (`modality.json`, rotation-representation semantics) — the concrete lineage behind GR00T's presence in LeRobot-ecosystem tooling like [Rosetta](rosetta.md).

## Related
- [NVIDIA GEAR](nvidia-gear.md) — research lab; co-leads ([Jim Fan](jim-fan.md) + [Yuke Zhu](yuke-zhu.md)) own the GR00T program.
- [NVIDIA Cosmos](nvidia-cosmos.md) — backbone (Cosmos-Reason2-2B for N1.7).
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — bundled training/eval framework.
- [VLA models](../concepts/learning/vla-models.md) — concept page.
- [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) — third-party benchmark that tests GR00T.

## Mentioned in
- [GR00T N1 Paper](../sources/groot-n1-paper.md) — **primary source**
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md)
- [EgoScale Paper](../sources/egoscale-paper.md)
- [DreamDojo Paper](../sources/dreamdojo-paper.md)
