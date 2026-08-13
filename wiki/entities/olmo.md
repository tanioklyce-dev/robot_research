---
title: OLMo (Open Language Model)
type: entity
subtype: llm
created: 2026-07-24
updated: 2026-07-24
sources: 6
tags: [olmo, open-source-llm, language-model, ai2, dolma, reproducibility, open-data, apache-2]
---

# OLMo (Open Language Model)

**OLMo** (*Open Language Model*) is the **[Allen Institute for AI (Ai2)](ai2.md)** family of
**fully open** large language models — open not just in weights but in **training
data, code, intermediate checkpoints, and logs** ([Groeneveld et al. 2024](../sources/olmo-paper.md)).
It's the "open-everything" LLM whose **OLMo-7B** is one of the four backbones under
[Molmo](molmo.md), and the reason Molmo can claim a **100%-open** variant. The
family now spans dense **OLMo 1 → OLMo 2** and the sparse-MoE [OLMoE](olmoe.md).

## Key facts

- **"Truly open" release:** weights + the **full Dolma pretraining corpus** + training/eval code + **hundreds of intermediate checkpoints** + **W&B training logs**, all **Apache 2.0** ([OLMo paper](../sources/olmo-paper.md)). Strictly more open than the Pythia/BLOOM tier and far beyond Llama/Mixtral.
- **OLMo 1 sizes:** OLMo-1B (2T tokens) and OLMo-7B (2.46T tokens); a 65B was in progress.
- **OLMo 1 architecture:** decoder-only, LLaMA-lineage — **no biases, non-parametric LayerNorm, SwiGLU, RoPE**, full attention.
- **[OLMo 2](../sources/olmo-2-paper.md) (2024/25):** dense **7B / 13B / 32B**; stability recipe swaps to **RMSNorm + QK-norm + reordered norm + Z-loss**; adds a **Dolmino** late-stage/mid-training curriculum and a **Tülu 3** post-training recipe (SFT→DPO→**RLVR**). Sits on the **Pareto frontier** vs Llama 3.1 / Qwen 2.5 / Gemma 2 at fewer FLOPs.
- **Corpus:** [Dolma](dolma.md) (Soldaini et al. 2024), the ~3T-token open pretraining dataset released alongside.
- **Portable:** trained on **both NVIDIA and AMD GPUs** without loss.
- **Peers:** OLMo 1 competitive with LLaMA-7B / Llama-2-7B / MPT-7B / Pythia-6.9B / Falcon-7B; OLMo 2-Instruct competitive with GPT-3.5 Turbo / GPT-4o Mini.

## Why it matters in this wiki

OLMo is the **open LLM decoder** at the base of the wiki's open VLM/VLA stack: a
vision encoder + connector bolted onto OLMo is exactly [Molmo](molmo.md)'s
fully-open configuration ([Molmo-7B-O](molmo.md)), which in turn backs the
[MolmoAct](molmoact.md) VLA. Where the wiki tracks *open-data* robot-learning work
([SmolVLA](smolvla.md), [LeRobot](lerobot.md), Molmo's PixMo), OLMo is the
language-model-layer instance of the same reproducibility-first philosophy — the
"L" whose training data you can actually inspect.

## Related

- [OLMoE](olmoe.md) — the sparse-MoE sibling from the same lab.
- [Dolma](dolma.md) — the open corpus OLMo trains on.
- [Ai2](ai2.md) — the lab.
- [Molmo](molmo.md) — the VLM built on OLMo-7B (fully-open variant).
- [MolmoAct](molmoact.md) — the VLA one further step up the stack.
- [Qwen](qwen.md) — the *other* (open-weight but closed-data) backbone family Molmo also uses; the contrast case.
- [VLA models](../concepts/learning/vla-models.md) — where OLMo sits as the decoder layer.

## Open questions

- **RLVR** (RL with verifiable rewards, OLMo 2 / Tülu 3) recurs across the wiki's reasoning and robot-RL threads but has no concept page yet.

## Mentioned in

- [OLMo paper (Groeneveld et al. 2024)](../sources/olmo-paper.md) — the OLMo 1 primary source.
- [OLMo 2 (2 OLMo 2 Furious)](../sources/olmo-2-paper.md) — the second generation.
- [OLMoE (Muennighoff et al. 2024)](../sources/olmoe-paper.md) — the MoE sibling.
- [Dolma (Soldaini et al. 2024)](../sources/dolma-paper.md) — the corpus.
- [Molmo and PixMo paper (Deitke et al. 2024)](../sources/molmo-pixmo-paper.md) — uses OLMo-7B / OLMoE as backbones.
