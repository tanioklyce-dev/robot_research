---
title: RT-2
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [rt-2, vla, action-tokens, pali-x, google-deepmind, robotics-transformer, web-knowledge-transfer]
---

**RT-2 (Robotics Transformer 2)** — Google DeepMind's 2023 VLA that adapts a pretrained vision-language model to robot control by **emitting actions as discrete tokens in the model's own vocabulary** (Zitkovich et al., CoRL 2023). The founding instance of the discrete-action-token family in the wiki's [VLA taxonomy](../concepts/learning/vla-models.md), and the direct ancestor of [OpenVLA](openvla.md).

## Mechanism (as documented via [RT-H](rt-h.md))

- **Backbone:** [PaLI-X](pali-x.md) 55B — a ViT image encoder feeding an encoder-decoder transformer that converts image + language token streams into action tokens.
- **Action encoding:** each action dimension discretized into **256 bins**, encoded as integer values. Actions comprise delta end-effector position, delta axis-angle rotation, gripper open/close, and a termination flag (plus 2 base dimensions on the mobile platform).
- **Co-training:** the robot action task is mixed with the full internet-scale PaLI-X training mixture, which is the source of its headline capability — semantic generalization transferred from web data to control.
- **Data:** the "Kitchen" dataset of **70K demonstrations** across 6 semantic task categories, shared with RT-1.

## Position in this wiki

Cited throughout — the origin of "web knowledge transfers to robot control," and the baseline that [OpenVLA](openvla.md), [π0](pi-zero.md), and [TurboVLA](turbovla.md) all measure against. It had **no page until 2026-08-04** despite being referenced across the VLA thread; this stub is built from [RT-H](../sources/rt-h-paper.md)'s description of it rather than from the RT-2 paper itself.

RT-H's finding against it: a flat task→action model shares data poorly as tasks become semantically diverse, and **RT-H beats it by +15 pp** by inserting a language-motion layer (p = 0.043 at n=80). Under teleoperated corrections (RT-2-IWR) it *degrades* from 25% to 13%.

> [!warning] Secondhand
> Everything here comes from RT-H's methods and related-work sections. **The RT-2 paper (arXiv 2307.15818) is not ingested** — a standing gap, since RT-2 is the most-referenced un-ingested model in the wiki's VLA thread. The same is true of **RT-1**.

## Related
- [RT-H](rt-h.md) — the action-hierarchy successor
- [OpenVLA](openvla.md) — the open reimplementation of the discrete-action-token recipe
- [VLA models](../concepts/learning/vla-models.md) — the taxonomy RT-2 founds

## Mentioned in
- [RT-H paper](../sources/rt-h-paper.md)
