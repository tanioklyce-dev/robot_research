---
title: PAN (Physical, Agentic, Nested) world model
type: entity
subtype: model
created: 2026-09-07
updated: 2026-09-07
sources: 3
tags: [world-model, glp, generative-latent-prediction, llm-backbone, video-diffusion, qwen2.5-vl, wan2.1, causal-swin-dpm, language-actions, mbzuai]
---

**PAN** — *Physical, Agentic, Nested* world model from [MBZUAI](mbzuai.md)'s Institute of Foundation Models ([Xing](eric-xing.md), Zhiting Hu, Zhengzhong Liu and a 33-author team), the first built instance of the [Generative Latent Prediction](../concepts/world-models/generative-latent-prediction.md) architecture. Previewed in [Critique of World Model](../sources/critique-of-world-model-paper.md), specified and evaluated in the [PAN technical report](../sources/pan-world-model-paper.md) (Nov 2025), demoed by Xing in the [LeCun debate](../sources/lecun-xing-jepa-glp-debate-2026.md) (Mar 2026).

## What was built (vs. what was proposed)

| Critique's GLP blueprint | PAN as shipped |
|---|---|
| Mixed **discrete + continuous** state; tokens as the stateful backbone | **256 continuous** query tokens from a frozen Qwen2.5-VL-7B |
| Enhanced LLM **+** diffusion embedding predictor, with a **Learned Switch** | Qwen2.5-VL-7B language model only; the mixed backbone is *"future work"* |
| Decoder as a **diagnostic that pressures the encoder** | Encoder **frozen**; decoder (Wan2.1-T2V-14B + Causal Swin-DPM) and query embeddings are the only trained parts in the joint stage |
| Multimodal decoder (sound, temperature, pain, text) | Video only |
| **RL on simulated experience**; a cache of precomputed simulations | Per-step planning loop with an external VLM (o3) proposing actions |

Actions are **natural-language captions** of what changes in a clip; the training data is filtered public video re-captioned by a VLM for temporal dynamics, size unstated ([source](../sources/pan-world-model-paper.md) §6).

## Results (own benchmark; open-source baselines Wan 2.1/2.2, Cosmos 1/2, V-JEPA 2; closed KLING, MiniMax, Gen-3)

- Action Simulation Fidelity **58.6 %** (agent 70.3, environment 47.0) — best open-source.
- Long-horizon: Transition Smoothness **53.6 %**, Simulation Consistency **64.1 %** — above all baselines incl. commercial.
- Step-wise simulation on AgiBot **56.1 %** — best open-source (V-JEPA 2 scored by latent similarity, not human judgement).
- Planning with an o3 agent: **+26.7 pts** open-ended (15 AgiBot scenarios), **+23.4 pts** structured (46 Language Table cases); several baselines *lowered* the agent's success.
- Compute: decoder adaptation 5 epochs on **960 H200s**; joint stage early-stopped after 1 epoch. Baseline numbers exist only in a dashboard screenshot.

## Reusable pieces

- **Causal Swin-DPM** — two-chunk sliding denoising window at staggered noise levels (K/2, K), chunk-wise causal attention so a chunk cannot see the next action, noised conditioning frame (k = 0.055). A concrete recipe for compounding error in long rollouts.
- **VLM-as-latent-backbone in a chat template** — state and action alternate as user turns, the assistant turn is a block of learnable query tokens. Cheap to reuse on any open VLM.
- **Re-encode your own output** at inference: `ŝ′ = [ŝ, h(ô)]`.

## What it does not settle

The Critique's argument for a decoder was that it diagnoses a lossy encoder; with the encoder frozen, nothing here tests that. The V-JEPA 2 comparison mixes measurement types. The planning gain is the result most worth an independent replication. See the [source page's read](../sources/pan-world-model-paper.md#the-wikis-read).

## Related

- [Generative Latent Prediction](../concepts/world-models/generative-latent-prediction.md) — the architecture class.
- [JEPA](../concepts/world-models/jepa.md), [LeWorldModel](leworldmodel.md) — the other side; LeCun's live objection to PAN's kind of model is in the [debate](../sources/lecun-xing-jepa-glp-debate-2026.md).
- [NVIDIA Cosmos](nvidia-cosmos.md), [Genie 3](genie-3.md), [WorldTrace](worldtrace.md) — generative-video kin; the same compounding-error problem attacked differently.
- [Generative-video vs JEPA](../syntheses/world-models/generative-video-vs-jepa-world-models.md) — where PAN lands on the paradigm table.

## Mentioned in

- [PAN technical report](../sources/pan-world-model-paper.md) — primary.
- [Critique of World Model](../sources/critique-of-world-model-paper.md) — §5 preview and blueprint.
- [LeCun & Xing debate](../sources/lecun-xing-jepa-glp-debate-2026.md) — demos, the rare-event data claim, the benchmark pitch.
