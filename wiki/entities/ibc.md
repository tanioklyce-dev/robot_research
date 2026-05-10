---
title: IBC (Implicit Behavioral Cloning)
type: entity
subtype: method
created: 2026-05-10
updated: 2026-05-10
sources: 1
tags: [ibc, implicit-behavioral-cloning, energy-based-model, infonce, push-t-origin, florence-2021, google-research]
---

**IBC — Implicit Behavioral Cloning.** Behavior-cloning method that **learns an energy function `E(o, a)` over observations and actions** rather than directly mapping observations to actions. At inference, the policy selects the action that *minimizes* energy at the current observation. Introduced by Florence et al., Google Research, CoRL 2021 ([arxiv 2109.00137](https://arxiv.org/abs/2109.00137)). Direct ancestor of [Diffusion Policy](diffusion-policy.md) and originator of the [PushT](pusht.md) benchmark.

## Approach

- **Energy-based model**: train a neural network `E_θ(o, a)` such that demo actions have low energy at their corresponding observations.
- **InfoNCE-style contrastive training**: requires drawing **negative samples** from a counter-distribution; the practical core difficulty.
- **Inference by argmin**: sample candidate actions, evaluate energy, select the lowest-energy one. Different sampling strategies (uniform, gradient-based, autoregressive) yield different trade-offs.
- **Multi-modal action support**: the energy landscape can have multiple valleys, naturally capturing multi-modal demonstration data — the failure mode of regressive BC.

## Key claims (from [IBC Paper](../sources/ibc-paper.md))

- Implicit (energy-based) models **outperform** explicit (MSE / MDN) models across robot policy-learning scenarios.
- **Theoretical argument**: implicit models better approximate complex, discontinuous, and multi-valued functions.
- Competitive with offline RL on D4RL **without using reward information**.
- Real-world contact-rich tasks demonstrated.

## Performance characteristics

From [Diffusion Policy Paper](../sources/diffusion-policy-paper.md) ablation Tables I–II:

- **Strong on PushT** (state 0.90/0.84, image 0.75/0.64) — the task IBC was tuned on.
- **Weak on RoboMimic harder tasks** (Can mh 0.02, Square ~0.00, Transport ~0.00, ToolHang ~0.00) — does not scale to more complex manipulation in the diffusion-policy comparison set.
- **Training instability** flagged as the main drawback by [Diffusion Policy Paper](../sources/diffusion-policy-paper.md) §V — the InfoNCE negative-sample requirement makes IBC sensitive to per-task hyperparameter tuning, in contrast to Diffusion Policy's largely consistent hyperparameters.

## Why it matters in this wiki

- **Origin of [PushT](pusht.md)** — the canonical 2D pushing benchmark used across [LeWM](leworldmodel.md), [DINO-WM](dino-wm.md), [JEPA-WMs](jepa-wms.md), and [Diffusion Policy](diffusion-policy.md).
- **First major attempt at multi-modal-BC via expressive policy classes** — predates BET, VQ-BeT, and Diffusion Policy. The conceptual lineage is: IBC (energy-based) → BET / VQ-BeT (action-discretization) → Diffusion Policy (denoising-diffusion).
- **Ancestor that motivated Diffusion Policy** — the Diffusion Policy paper directly diagnoses IBC's training instability and uses denoising-diffusion as the alternative.

## Related

- [Diffusion Policy](diffusion-policy.md) — direct successor; supersedes IBC empirically.
- [PushT](pusht.md) — benchmark introduced here.
- [BET](bet.md) — sibling multi-modal BC method (action-discretization rather than energy-based).
- [VQ-BeT](vq-bet.md) — BET's successor; also competes with IBC on multi-modal action distributions.
- [Imitation learning](../concepts/imitation-learning.md) — broader concept; IBC is the implicit-model variant.

## Mentioned in

- [IBC Paper](../sources/ibc-paper.md) — primary source.
- [Diffusion Policy Paper](../sources/diffusion-policy-paper.md) — direct successor; baseline in 12-task ablation.
- [PushT](pusht.md) — origin attribution.

## Open questions / TBD

- **Author entity pages**: Pete Florence (Google Research), Corey Lynch, Andy Zeng — the Google Research robotics line. Could surface if more Google-line work surfaces (e.g., RT-1, RT-2, PaLM-E).
- **EBM-line work in robotics** — Du, Mordatch, Igor's broader work on energy-based models for robot control. Scope question.
- **D4RL evaluation details** — abstract claims competitiveness without rewards but mechanics aren't ingested.
