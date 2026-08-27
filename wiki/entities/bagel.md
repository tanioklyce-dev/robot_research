---
title: BAGEL
type: entity
subtype: model
created: 2026-05-25
updated: 2026-05-25
sources: 0
tags: [bagel, image-generation, image-editing, mixture-of-transformers, world-model, web-pretrained]
status: stub
---

> [!note] Stub entity
> Filed 2026-05-25 during lint (12 mentions across 6 wiki files; all via π0.7 references). Primary source — [arXiv 2505.14683](https://arxiv.org/abs/2505.14683) ("BAGEL: Bidirectional Autoregressive Generative Encoder-decoder for Language and Images") — **not yet ingested**; deepen when filed.

**BAGEL** — **14B-parameter mixture-of-transformers** model from 2025 capable of image understanding, editing, and generation. Web-scale pretrained. The wiki tracks BAGEL because **[π0.7](pi07.md) uses it as the substrate for its subgoal-image world model** — the generator that produces multi-view target frames given a robot's current observation + subtask instruction.

## What we know via the wiki's existing references

- **14B parameters; mixture-of-transformers architecture**.
- **Web-scale pretrained** on image generation + editing tasks.
- **Subgoal-image world model in π0.7** ([paper](../sources/pi07-paper.md) §V-B):
  - Initialized from BAGEL.
  - Fine-tuned with conditional flow-matching loss on high-quality subtask-labeled segments from π0.7's training data.
  - At inference, generates multi-view target frames (`G^1_t, ..., G^n_t`) given current observation + subtask instruction + episode metadata.
  - This is **how web-scale knowledge (non-robot data, egocentric human video) flows into π0.7's policy** — BAGEL absorbs it during pretraining, then exposes it to π0.7 via generated subgoal images.
- **Follows the SuSIE lineage** ([SuSIE 2023](https://arxiv.org/abs/2310.10639), "Subgoal Synthesis via Image Editing") of using web-pretrained image-edit models as world models for robot policies.

## Why it matters in this wiki

- **Wiki's first separate-world-model entity for the policy-with-external-world-model architecture pattern.** Contrast with JEPA-style integrated world models ([LeWorldModel](leworldmodel.md), [V-JEPA 2](v-jepa-2.md), [JEPA-WMs](jepa-wms.md)) where the world model is the policy's predictor module rather than a separate generator.
- **The substrate enabling π0.7's "diverse data" pretraining** — without a web-pretrained generative model like BAGEL, π0.7 wouldn't be able to import egocentric-human-video and image-edit knowledge into the policy.

## Related

- [π0.7](pi07.md) — primary downstream user.
- [Physical Intelligence](physical-intelligence.md) — π0.7's lab.
- [Flow matching](../concepts/learning/flow-matching.md) — the loss used to fine-tune BAGEL into the subgoal-image world model.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — broader concept.
- [DINO-WM](dino-wm.md), [JEPA-WMs](jepa-wms.md), [LeWorldModel](leworldmodel.md) — JEPA-style integrated-world-model contrasts.

## Code & weights

- Paper: https://arxiv.org/abs/2505.14683
- HF: `bytedance/BAGEL-7B-MoT` (or similar; vendor not surfaced in this stub).

## Open questions

- **Primary source not yet ingested.** When the BAGEL paper lands, deepen with: architecture diagram, pretraining-data mix, image-edit + image-gen capabilities, and the mixture-of-transformers specifics.
- **Authorship** — not extracted; commonly ByteDance / Stepfun-AI per public references.
- **BAGEL alternatives** for the same role (image-gen + edit) — SD3, FLUX, etc. — could plausibly substitute as world-model generators in π0.7-style stacks.

## Mentioned in

- [π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities (Physical Intelligence, 2025)](../sources/pi07-paper.md)
