---
title: NVIDIA GR00T
type: entity
subtype: product
created: 2026-05-06
updated: 2026-05-15
sources: 12
tags: [groot, vla, nvidia, foundation-model, humanoid]
---

NVIDIA's open, commercially-licensed [VLA](../concepts/vla-models.md) foundation model line for humanoid robots. The flagship policy that ships with NVIDIA's Physical AI stack ([NVIDIA Isaac Lab](nvidia-isaac-lab.md), [NVIDIA Isaac Sim](nvidia-isaac-sim.md)). **Both site champions of the [October 2025 Seeed × NVIDIA × HF Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md) ran GR00T N1.5** (fine-tuned via NVIDIA Brev) on non-humanoid dual-arm platforms (XLeRobot, SO-ARM101) — the strongest external signal yet that GR00T fine-tunes work at weekend-hackathon data scales (150–300 episodes) outside the humanoid form factor it was designed for.

## Versions seen
- **N1** — original release; **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** ([arXiv 2503.14734](https://arxiv.org/abs/2503.14734), Mar 2025) — authors: Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, Adeet Parikh, Aaron Lo, Abhishek Joshi, Ajay Mandlekar, [Yuke Zhu](yuke-zhu.md). Featured in [NVIDIA GEAR Lab Publications](../sources/nvidia-gear-publications.md) as a top highlight.
- **N1.5** — winning policy at both sites of the October 2025 Seeed × NVIDIA × HF Embodied AI Hackathon; fine-tuned via NVIDIA Brev; deployed on Jetson Thor.
- **N1.6** — referenced as the version newly available in [NVIDIA Isaac Lab](nvidia-isaac-lab.md) alongside Newton 1.0 GA at GTC 2026 ([NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)).
- **N1.7 Early Access** — 3B parameters, built on a Cosmos-Reason2-2B backbone, **[EgoScale](../sources/egoscale-paper.md) pretraining on 20,854 hours of egocentric human video** across 20+ task categories ([Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)). The EgoScale paper (Zheng et al., NVIDIA GEAR, Feb 2026) is the primary source for this corpus and publishes a clean log-linear scaling law `L = 0.024 − 0.003·ln(D)` (R² = 0.9983) relating human-data scale to validation loss — see [Scaling laws — VLAs and human data](../concepts/scaling-laws-vla.md).

> [!warning] Version overlap
> N1.6 and N1.7 EA appear referenced in parallel — likely a GA + EA release pattern. Confirm when a primary GR00T page replaces this stub.

## Related
- [NVIDIA GEAR](nvidia-gear.md) — research lab; co-leads ([Jim Fan](jim-fan.md) + [Yuke Zhu](yuke-zhu.md)) own the GR00T program.
- [NVIDIA Cosmos](nvidia-cosmos.md) — backbone (Cosmos-Reason2-2B for N1.7).
- [NVIDIA Isaac Lab](nvidia-isaac-lab.md) — bundled training/eval framework.
- [VLA models](../concepts/vla-models.md) — concept page.
- [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) — third-party benchmark that tests GR00T.

## Mentioned in
- [NVIDIA Newton Contact-Rich Manipulation Blog](../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [Top 10 Physical AI Models 2026](../sources/top-10-physical-ai-models-2026.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md)
- [EgoScale Paper](../sources/egoscale-paper.md)
