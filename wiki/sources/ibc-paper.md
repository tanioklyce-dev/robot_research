---
title: IBC Paper — Implicit Behavioral Cloning (Florence et al., CoRL 2021)
type: source
url: https://arxiv.org/abs/2109.00137
author: Pete Florence, Corey Lynch, Andy Zeng, Oscar Ramirez, Ayzaan Wahid, Laura Downs, Adrian Wong, Johnny Lee, Igor Mordatch, Jonathan Tompson
affiliation: Google Research (Robotics at Google)
published: 2021-09-01 (arxiv); CoRL 2021
ingested: 2026-05-09
tags: [ibc, implicit-behavioral-cloning, energy-based-model, infonce, push-t, behavior-cloning, florence-2021, google-research]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (paper PDF not in `raw/`). Substantive technical claims about IBC's mechanics are cross-cited from [Diffusion Policy Paper](diffusion-policy-paper.md) §VII (Related Work), which describes IBC as the most direct predecessor to Diffusion Policy. To deepen this page, drop the IBC PDF in `raw/` and re-ingest.

## Summary

**Implicit Behavioral Cloning** (IBC) — Pete Florence et al. (Google Research, CoRL 2021) — proposes treating supervised policy learning as **implicit-model regression**: instead of `a = f(o)` (explicit policy), train an energy-based model `E(o, a)` and select actions by *minimizing* energy at inference. The headline finding: implicit models **generally outperform explicit models** (MSE regression, Mixture Density Networks) across robot policy learning, particularly on tasks with high-dimensional actions, visual inputs, and discontinuous / multi-valued action distributions. Also competitive with or superior to state-of-the-art **offline RL** on D4RL benchmarks **without using reward information** — a notable result. Introduced the **PushT** benchmark used heavily downstream.

## Abstract (verbatim opener)

> "We find that across a wide range of robot policy learning scenarios, treating supervised policy learning with an implicit model generally performs better, on average, than commonly used explicit models."

## Key claims

- **Implicit > explicit on average.** Across the evaluated robot policy-learning scenarios, implicit (energy-based) models outperform MSE / MDN explicit models.
- **Theoretical argument**: implicit models better approximate **complex, discontinuous, and multi-valued functions** — the precise failure modes of regressive BC on multi-modal demonstrations.
- **D4RL competitive without rewards**: matches or beats SOTA offline RL on D4RL despite not using reward labels, suggesting the method is competitive with reward-conditioned approaches via expressiveness alone.
- **Real-world contact-rich tasks** demonstrated; precision tasks particularly highlighted.
- **PushT benchmark**: introduced here (the 2D T-block pushing task that became canonical across imitation-learning and world-model literature). See [PushT](../entities/pusht.md) for full mechanics.

## Mechanics (cross-cited from Diffusion Policy paper)

From [Diffusion Policy Paper](diffusion-policy-paper.md) §I, §V, §VII:

- **Energy-based model**: train `E_θ(o, a)` such that the demonstration action has lowest energy for each observation. At inference, sample candidate actions and pick `argmin E`.
- **Training**: InfoNCE-style contrastive loss requiring **negative samples** drawn from a counter-distribution. Sampling these well is the practical challenge.
- **Failure modes** (per Diffusion Policy ablations): IBC scores 0.00 across most RoboMimic tasks (Lift mh 0.15/0.02; Can/Square/Transport/ToolHang ~0.00) — indicating it **does not scale to harder tasks** in the diffusion-policy comparison set. The Diffusion Policy paper attributes this to **training instability** stemming from the negative-sample requirement.
- **Strong only on PushT** in the Diffusion Policy benchmark: state PushT 0.90/0.84, image PushT 0.75/0.64. Strong because PushT is the task IBC was tuned on.

## Why it matters in this wiki

- **Origin of [PushT](../entities/pusht.md)** — the 2D pushing benchmark that propagates across [LeWM](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md), [JEPA-WMs](../entities/jepa-wms.md), and the [Diffusion Policy](../entities/diffusion-policy.md) ablation.
- **Direct ancestor of [Diffusion Policy](../entities/diffusion-policy.md)** — both papers share the diagnosis (regressive BC fails on multi-modal action distributions) but propose different solutions: IBC = energy-based implicit model; Diffusion Policy = denoising diffusion process. Diffusion Policy supersedes IBC empirically across the 12-task simulation sweep.
- **Conceptual lineage of "expressive policy classes"** — IBC, then BET, then VQ-BeT, then Diffusion Policy is the through-line of "make BC handle multi-modal action distributions properly". This paper is the first move.

## Entities mentioned

- [IBC](../entities/ibc.md) — the method itself.
- [PushT](../entities/pusht.md) — benchmark introduced in this paper.
- [Diffusion Policy](../entities/diffusion-policy.md) — direct successor; supersedes IBC empirically.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — IBC sits in the BC family but as an *implicit* (energy-based) variant.
- [Energy-based models](../concepts/learning/energy-based-models.md) — concept page (filed 2026-05-17 after [the Aleph EBM video ingest](2026-05-aleph-ebm-refuses-bullshit-video.md) surfaced [Kona](../entities/kona.md) as the second commercialized EBM line in this wiki).
- Multi-modal action distributions — the same modeling challenge that motivates [Diffusion Policy](../entities/diffusion-policy.md), [VQ-BeT](../entities/vq-bet.md), [BET](../entities/bet.md).

## Open questions / TBD

- **Full paper not yet ingested** — abstract-level only. Mechanics summarized via Diffusion Policy paper's secondary description.
- **D4RL details** — which D4RL tasks specifically; how "competitive without rewards" was measured. Not derivable from abstract.
- **InfoNCE training details** — negative-sample sampling strategy that distinguishes IBC from later EBM variants. Not derivable from abstract.
- **Author entity pages** — Florence, Lynch, Zeng (Google Research robotics line). Not yet filed.
