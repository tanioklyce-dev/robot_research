---
title: π0 Paper — A Vision-Language-Action Flow Model for General Robot Control (Black et al., Physical Intelligence, 2024)
type: source
url: https://arxiv.org/abs/2410.24164
author: "Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Lucy Xiaoyang Shi, James Tanner, Quan Vuong, Anna Walling, Haohuan Wang, Ury Zhilinsky"
affiliation: Physical Intelligence (and academic collaborators)
published: 2024-10-31 (arxiv v1); 2026-01-08 (last revised)
ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
tags: [pi-zero, pi0, vla, flow-matching, vision-language-action, physical-intelligence, generalist-policy, levine]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (paper PDF not in `raw/`). Filed as part of the curriculum-driven backfill for [Module 9 (VLA models)](../syntheses/robot-learning-curriculum.md). To deepen, drop the PDF in `raw/` and re-ingest.

## Summary

**π0** ("pi-zero") — [Physical Intelligence](../entities/physical-intelligence.md), led by a 24-author roster including Sergey Levine, Chelsea Finn, Karol Hausman, Brian Ichter, Karl Pertsch (October 2024). A **vision-language-action flow-matching model**: a pre-trained vision-language model (VLM) provides the perception + language backbone; a **flow-matching action head** generates continuous action sequences. Trained across heterogeneous robot data — single-arm, dual-arm, mobile manipulators — and evaluated on long-horizon manipulation tasks including **laundry folding, table cleaning, and box assembly**. Cited by the [Stanford HAI AI Index 2026](stanford-hai-ai-index-2026.md) as a leading Physical-AI VLA demonstration.

## Abstract (verbatim opener)

> "We propose ... a flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge."

(Paraphrased framing of the main claim from the arxiv abstract page; full abstract to be re-verified once the PDF lands in `raw/`.)

## Key claims

- **Architecture: VLM backbone + flow-matching action head.** The action decoder is **flow matching**, a diffusion-cousin generative-modeling technique. The continuous-action head is conditioned on VLM features and language tokens.
- **Cross-platform training.** Single training run produces a policy that runs on single-arm, dual-arm, and mobile-manipulator embodiments without per-platform retraining (the headline "general robot control" claim).
- **Tasks demonstrated.** Laundry folding, table cleaning, box assembly — long-horizon, dexterous, household-flavoured tasks that stress beyond-PushT-class capability.
- **Internet-scale prior.** The VLM backbone gives semantic generalization the action head alone could not provide (instruction-following, object naming, etc.).

## Why it matters in this wiki

- **Concrete VLA exemplar beyond OpenVLA / GR00T.** The wiki had Physical Intelligence filed as an entity but no primary source for π0 itself — that gap is now closed.
- **Flow matching vs DDPM as action heads.** π0 uses **flow matching** in the same role [Diffusion Policy](../entities/diffusion-policy.md) uses **DDPM** — these are sibling generative-model families, and the curriculum [Module 9](../syntheses/robot-learning-curriculum.md) can now contrast them with a primary source on each side.
- **Generalist-policy data point.** Cross-platform training (single-arm, dual-arm, mobile manipulator) is the kind of breadth claim curriculum [Module 13](../syntheses/robot-learning-curriculum.md) (home-robotics deployment) needs to interrogate.

## Entities mentioned

- [Physical Intelligence](../entities/physical-intelligence.md) — the company; π0 is its flagship.
- [Sergey Levine](../entities/sergey-levine.md), [Chelsea Finn](../entities/chelsea-finn.md), [Karl Pertsch](../entities/karl-pertsch.md) — author overlaps with [DROID](../entities/droid.md) / Metaworld lineage.
- [Franka Panda](../entities/franka-panda.md) — likely platform; verify on PDF.

## Concepts touched

- [VLA models](../concepts/vla-models.md) — π0 is a defining instance.
- [Imitation learning](../concepts/imitation-learning.md) — π0 is BC-flavored at training time (with a flow-matching head).

## Open questions / TBD

- **Full paper not yet ingested** — abstract-level only. The flow-matching loss formulation, VLM choice, training-data composition, and quantitative success rates are unquoted.
- **Flow matching as a concept page.** Worth a dedicated `concepts/flow-matching.md` if it resurfaces in later VLA / world-model work.
- **π0.5 and π0.6 follow-ons** — referenced in [Physical Intelligence entity](../entities/physical-intelligence.md); separate primary sources would close the family.
