---
title: "LoRA: Low-Rank Adaptation of Large Language Models (Hu, Shen et al., Microsoft, 2021)"
type: source
url: https://arxiv.org/abs/2106.09685
fetch_url: https://arxiv.org/pdf/2106.09685v2
local_path: raw/2106.09685v2.pdf
sha256: e9a0d3128767db616085dc0f4e6e455e672e89af823e8ed1282793682787395a
author: "Edward J. Hu*, Yelong Shen*, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen"
affiliations: Microsoft Corporation (Yuanzhi Li also CMU)
published: 2021-06-17
venue: ICLR 2022
ingested: 2026-08-31
tags: [lora, peft, parameter-efficient-fine-tuning, low-rank, adapters, prefix-tuning, fine-tuning, transformer, gpt-3, roberta, deberta, gpt-2, intrinsic-dimension, microsoft, primary-source, foundational]
---

## Summary

**LoRA** freezes a pretrained weight matrix `W₀ ∈ ℝ^{d×k}` and learns its task-specific update as a **rank-`r` product**, `W₀ + ΔW = W₀ + BA` with `B ∈ ℝ^{d×r}`, `A ∈ ℝ^{r×k}`, `r ≪ min(d,k)`. Only `A` and `B` receive gradients. The forward pass becomes `h = W₀x + BAx`, scaled by `α/r` (§4.1). `A` is initialised Gaussian and `B` **zero**, so `ΔW = 0` at step 0 and the adapted model starts exactly at the pretrained one.

The paper's practical claim is a resource claim, and it is large: on **GPT-3 175B**, LoRA cuts trainable parameters by up to **10,000×** and training VRAM by **3×** (1.2 TB → 350 GB), taking a **350 GB checkpoint down to 35 MB** at `r=4` on `W_q, W_v` — while **matching or beating full fine-tuning** on WikiSQL, MNLI-m and SAMSum (Table 4). Because `BA` is linear it can be **folded into `W₀` at deploy time**, so unlike adapter layers LoRA adds **zero inference latency by construction**, and unlike prefix-tuning it consumes no sequence length.

The paper's *intellectual* claim is the one that has aged better: **the update `ΔW` is drastically rank-deficient**. On GPT-3 with `d_model = 12,288`, `r = 1` on `{W_q, W_v}` already reaches 73.4 on WikiSQL versus 73.8 at `r = 8` (Table 6). §7 then shows *why*, with two measurements that most follow-on work never repeats.

> [!note] Why this is a foundational ingest for this wiki
> LoRA was referenced by name in **eleven** wiki pages before it had a page of its own — [X-VLA](xvla-paper.md), [OpenVLA-OFT](openvla-oft-paper.md), [DreamGen](dreamgen-paper.md), [GR00T N1](groot-n1-paper.md), [FOREWARN](forewarn-paper.md), [TRL SFT](huggingface-trl-sft-trainer.md), the [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) comparison and others. Every practical VLA fine-tune in this wiki is a LoRA fine-tune. This ingest supplies the primary.

## The four claimed advantages (§1)

1. **One base, many adapters.** Freeze the shared model; swap `A`/`B` per task. Hosting 100 adapted GPT-3s costs *350 GB + 100 × 35 MB ≈ 354 GB* instead of ~35 TB (footnote 4).
2. **Lower hardware barrier, ~3×** — no gradients and no Adam optimiser state for the frozen bulk.
3. **No inference latency** — merge `W = W₀ + BA` before serving; subtract and re-add to task-switch.
4. **Orthogonal to other methods** — composes with prefix-tuning (Appendix E).

Also reported: **25% training-throughput speedup** on GPT-3 175B (32.5 → 43.1 tokens/s per V100 at equal model-parallel sharding, footnote 5).

## The argument against the incumbents (§3)

This section is the paper's real polemic, and it is a *systems* argument rather than an accuracy one.

**Adapter layers add latency that FLOP-counting hides.** Adapters are ~1% of parameters, so they look free. But they are **sequential depth** — they cannot be absorbed into the parallel matmuls around them, and the effect shows up exactly where it hurts: **batch size 1, short sequences, online serving.** Table 1, GPT-2 medium on a Quadro RTX8000:

| Batch / seq len | 32 / 512 | 16 / 256 | 1 / 128 |
|---|---|---|---|
| Fine-tune or LoRA | 1449.4 ms | 338.0 ms | 19.8 ms |
| Adapter_L (11M) | +2.2% | +5.0% | **+20.7%** |
| Adapter_H (11M) | +3.0% | +8.4% | **+30.3%** |

And it worsens under model sharding, where extra depth means extra `AllReduce`/`Broadcast` synchronisation.

**Prompt/prefix tuning is hard to optimise and steals context.** Performance moves **non-monotonically** in trainable parameters — GPT-3 prefix-embedding degrades past 256 special tokens, prefix-layer past 32 (§5.5, Fig. 2) — and any token spent on the prefix is a token unavailable to the task.

> [!note] The generality claim
> §4.1 argues LoRA is *a generalisation of full fine-tuning*: applied to all matrices with `r` = full rank, it recovers full fine-tuning's expressiveness. Adapter methods converge to an MLP as capacity grows, prefix methods to a model that cannot take long inputs. Only LoRA's limit is the original model.

## Results

**GLUE (Table 2)** — RoBERTa-base **0.3 M** trainable → 87.2 avg vs 86.4 for full FT at 125 M. RoBERTa-large **0.8 M** → 89.0 vs 88.9 at 355 M. DeBERTa-XXL **4.7 M** → 91.3 vs 91.1 at 1.5 B.

**E2E NLG, GPT-2 (Table 3)** — GPT-2 M LoRA at 0.35 M: BLEU **70.4** vs 68.2 full FT (354.92 M) and 69.7 prefix-layer.

**GPT-3 175B (Table 4)**:

| Method | Trainable | WikiSQL | MNLI-m | SAMSum (R1/R2/RL) |
|---|---|---|---|---|
| Full fine-tune | 175,255.8 M | 73.8 | 89.5 | 52.0/28.0/44.5 |
| BitFit | 14.2 M | 71.3 | 91.0 | 51.3/27.4/43.5 |
| PreEmbed | 3.2 M | 63.1 | 88.6 | 48.3/24.2/40.5 |
| PreLayer | 20.2 M | 70.1 | 89.5 | 50.8/27.3/43.5 |
| Adapter_H | 40.1 M | 73.2 | 91.5 | 53.2/29.0/45.1 |
| **LoRA** | **4.7 M** | **73.4** | **91.7** | **53.8/29.8/45.9** |
| **LoRA** | 37.7 M | **74.0** | 91.6 | 53.4/29.2/45.1 |

Note the shape: LoRA at **4.7 M** beats Adapter_H at **40.1 M** on all three, and beats *full fine-tuning* at 175 B on two.

## §7 — the part worth reading twice

Three questions, on GPT-3 175B, at a fixed 18 M-parameter budget.

**7.1 Which matrices?** Spending the budget on `{W_q, W_v}` at `r=4` beats spending it on `W_q` alone at `r=8` (WikiSQL 73.7 vs 70.4). Spreading over all four attention matrices at `r=2` ties it (73.7 / MNLI 91.7).

> **Breadth beats depth of rank.** "Even a rank of four captures enough information in `ΔW` such that it is preferable to adapt more weight matrices than adapting a single type of weights with a larger rank." This is the origin of the `q_proj,v_proj` default that every PEFT library still ships.

**7.2 How small can `r` be?** (Table 6, WikiSQL / MultiNLI)

| Target | r=1 | r=2 | r=4 | r=8 | r=64 |
|---|---|---|---|---|---|
| `W_q` | 68.8 | 69.6 | 70.5 | 70.4 | 70.0 |
| `W_q, W_v` | **73.4** | 73.3 | 73.7 | 73.8 | 73.5 |
| all four | 74.1 | 73.7 | 74.0 | 74.0 | 73.9 |

Flat from `r=1` to `r=64`. The evidence that this is *rank deficiency* and not saturation is a **subspace-overlap measurement**: take `A_{r=8}` and `A_{r=64}` learned from the same base model, SVD both, and compute the Grassmann-based normalised similarity `φ(A_{r=8}, A_{r=64}, i, j) = ‖U_i^⊤ U_j‖_F² / min(i,j)` (Eq. 4). Result (Fig. 3): the **top singular direction overlaps with φ > 0.5**; the rest do not. Two different random seeds at `r=64` likewise share only their leading directions (Fig. 4), while two random Gaussians share none. **The extra rank is mostly noise accumulated during training.**

**7.3 What is `ΔW` doing to `W`?** Project `W_q` onto `ΔW_q`'s `r`-dimensional singular subspace and compare Frobenius norms (Table 7, layer 48):

| | via `ΔW_q` dirs | via `W_q`'s own top dirs | via random dirs |
|---|---|---|---|
| `‖U^⊤ W_q V^⊤‖_F`, r=4 | 0.32 | 21.67 | 0.02 |
| r=64 | 1.90 | 37.71 | 0.33 |

with `‖W_q‖_F = 61.95`, `‖ΔW_q‖_F = 6.91` (r=4).

Three readings, in the authors' order: `ΔW` correlates with `W` **more than random** — so it amplifies features already present; it does **not** repeat `W`'s top singular directions — so it amplifies *unemphasised* ones; and the **amplification factor is ~21.5×** (6.91 / 0.32).

> **The mechanism claim.** "The low-rank adaptation matrix potentially amplifies the important features for specific downstream tasks that were learned but not emphasized in the general pre-training model." Fine-tuning, on this account, is not *teaching* — it is **turning up a gain on something the pretrained model already had**. That is the sentence to carry into any argument about how much a robot fine-tune can be expected to add.

## Key claims

- `ΔW = BA`, `r ≪ min(d,k)`; `A ~ N(0,σ²)`, `B = 0`; output scaled by `α/r`, and `α` is fixed to the first `r` tried rather than tuned (§4.1).
- Applied only to **attention** matrices in this paper — `W_q, W_v` in most experiments. MLP, LayerNorm and bias adaptation explicitly **left to future work** (§4.2).
- GPT-3 175B: **10,000× fewer trainable params, 3× less VRAM, 25% faster training, 35 MB checkpoints, zero added inference latency** (§4.2).
- Inspired by **intrinsic dimensionality** results (Li et al. 2018a; Aghajanyan et al. 2020) — pretrained LMs fine-tune efficiently inside a low-dimensional random subspace. LoRA's hypothesis is the *update* inherits that property.
- Stated limitation: **batching different tasks in one forward pass is awkward** once `A`/`B` are merged into `W`. Keeping them unmerged is possible where latency permits — the seed of every multi-LoRA serving stack that followed.
- Honest caveat (footnote 6): small `r` is **not** expected to work universally — a downstream task in a *different language* from pretraining would plausibly need something closer to full rank.
- Future-work item #4 is a live thread: "the rank-deficiency of `ΔW` suggests that `W` could be rank-deficient as well."

## Entities mentioned

- [Microsoft](../entities/microsoft.md) — all authors; released `microsoft/LoRA` on GitHub with RoBERTa/DeBERTa/GPT-2 checkpoints.
- Models used as substrates, none of which have wiki pages: GPT-3 175B, GPT-2 M/L, RoBERTa base/large, DeBERTa-XXL.
- Compute: NVIDIA **V100** for all training; **Quadro RTX8000** for the latency table.

## Concepts touched

- [Low-rank adaptation (LoRA / PEFT)](../concepts/learning/low-rank-adaptation.md) — the concept page this source anchors.
- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) — prefix/prompt tuning is the family LoRA argues against here; [X-VLA](../entities/x-vla.md) later **combines** the two.
- [VLA models](../concepts/learning/vla-models.md) — LoRA is the default adaptation path for every VLA in this wiki.
- [Distributed representations](../concepts/learning/distributed-representations.md), [Attention Is All You Need](attention-is-all-you-need.md) — the architecture LoRA is defined against (`W_q, W_k, W_v, W_o`).

## Open questions

- **Does the amplification story hold for action models?** §7.3 measures `ΔW` against `W` in a *language* model adapting to a *language* task. When [OpenVLA](../entities/openvla.md) is LoRA-tuned onto a new robot, is it also amplifying latent-but-unemphasised features — or is it genuinely writing in new motor structure that the web-scale backbone never had? Nobody in this wiki has run Table 7 on a VLA. It is a cheap experiment with a real answer.
- **Why is attention-only still the default in 2026?** The paper deferred MLP adaptation "to a future work" and the field largely kept the deferral, even though later PEFT practice does target MLP/`all-linear`. No ingested robotics source justifies its target-module choice.
- **Where does `r` stop being flat for robot data?** X-VLA's 9 M-parameter (1%) LoRA matching fully-finetuned π0 is the wiki's strongest evidence that the flatness transfers ([X-VLA](xvla-paper.md), Tab. 3). But footnote 6's caveat — different *distribution* needs more rank — is exactly the cross-embodiment case.
- **The merged-batching limitation is now a product category.** vLLM/S-LoRA-style multi-adapter serving resolves §4.2's stated limitation; no primary on that is ingested.
