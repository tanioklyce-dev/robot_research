---
title: Low-rank adaptation (LoRA) and parameter-efficient fine-tuning
type: concept
created: 2026-08-31
updated: 2026-08-31
sources: 9
tags: [lora, peft, parameter-efficient-fine-tuning, low-rank, adapters, prefix-tuning, fine-tuning, transformer, vla, adaptation]
---

**Low-Rank Adaptation (LoRA)** — adapt a frozen pretrained model by learning each weight update as a **low-rank product** rather than a dense matrix. For `W₀ ∈ ℝ^{d×k}`, train `A ∈ ℝ^{r×k}` and `B ∈ ℝ^{d×r}` with `r ≪ min(d,k)` and compute `h = W₀x + BAx`, scaled `α/r`. `A` is Gaussian-initialised, `B` is **zero**, so training starts exactly at the pretrained model. Introduced by [Hu, Shen et al. (Microsoft, 2021)](../../sources/lora-paper.md); ICLR 2022.

LoRA is the dominant member of a broader family, **parameter-efficient fine-tuning (PEFT)**: adapt a large model by training a small number of new or selected parameters instead of all of them.

## Why it won

Three properties, in descending order of how often they are the actual reason:

1. **Memory, not FLOPs.** The saving is dominated by *not storing optimiser state and gradients* for the frozen bulk. Adam keeps two moments per trainable parameter; freezing 99.99% of them is what takes GPT-3 175B training from 1.2 TB to 350 GB of VRAM ([LoRA paper](../../sources/lora-paper.md), §4.2). This is why a 7B VLA fine-tunes on one consumer GPU ([TRL SFT Trainer](../../sources/huggingface-trl-sft-trainer.md)).
2. **Checkpoints become artifacts you can move.** 350 GB → **35 MB** at `r=4`. One frozen base serves many tasks by swapping adapters; hosting 100 adapted GPT-3s costs ~354 GB instead of ~35 TB.
3. **Zero inference latency, by construction.** `BA` is linear, so it folds into `W₀` before serving. This is the distinction from **adapter layers**, which add sequential depth that hardware parallelism cannot hide — +20.7% to +30.3% latency on GPT-2 medium at batch 1 (LoRA paper, Table 1), i.e. precisely in the online-serving regime a robot policy runs in.

## The empirical core: `ΔW` is rank-deficient

The claim that makes LoRA more than an engineering trick is that a **very** small rank suffices. On GPT-3 175B with `d_model = 12,288`, `r = 1` on `{W_q, W_v}` gives 73.4 on WikiSQL against 73.8 at `r = 8` — flat all the way to `r = 64`.

Two measurements support it rather than merely reporting it:

- **Subspace overlap.** SVD `A_{r=8}` and `A_{r=64}` from the same base; only the **top singular direction** overlaps meaningfully (Grassmann-normalised similarity > 0.5). Two seeds at `r=64` likewise share only their leading directions, while two random Gaussians share none. The extra rank is largely **training noise**.
- **Amplification.** Projecting `W_q` onto `ΔW_q`'s singular subspace gives a much smaller norm than projecting onto `W_q`'s own top directions (0.32 vs 21.67 at `r=4`) but much larger than random (0.02) — with an **amplification factor ≈ 21.5×**. So `ΔW` neither invents new directions nor repeats the dominant ones: it **turns up a gain on features the pretrained model already had but did not emphasise**.

> [!note] The consequence worth carrying
> If adaptation is amplification of latent structure rather than acquisition of new structure, then **what a fine-tune can achieve is bounded by what pretraining already contains**. That is a testable framing for every "we adapted the VLA to our robot in 200 demos" claim in this wiki — including [Gemini Robotics'](../../sources/deepmind-gemini-robotics-model-page.md) "any bi-arm robot in a few hours" and [X-VLA](../../entities/x-vla.md)'s 200-demo AIRBOT transfer. Nobody has run the §7.3 measurement on an action model.

## Practical settings, and where they came from

| Knob | Default | Origin |
|---|---|---|
| Target modules | `q_proj`, `v_proj` | LoRA §7.1: at a fixed budget, adapting **two** attention matrices at `r=4` beats **one** at `r=8` (73.7 vs 70.4). Breadth beats rank. |
| Rank `r` | 4–16 | Flat 1→64 in the paper; robotics practice sits higher, e.g. [X-VLA](../../sources/xvla-paper.md) at 9 M params ≈ 1% of a 0.9 B model. |
| `α` | set once, not tuned | §4.1 — with `α/r` scaling, tuning `α` under Adam ≈ tuning the learning rate. |
| LR | ~1e-4 for adapters | [TRL SFT Trainer](../../sources/huggingface-trl-sft-trainer.md) recommendation; higher than a full-FT LR. |
| MLP layers | *not* adapted in the paper | §4.2 explicitly defers MLP/LayerNorm/bias to future work. Later practice (`all-linear`) diverged; no ingested robotics source justifies its choice. |

## The PEFT family it belongs to

| Method | Mechanism | LoRA paper's objection |
|---|---|---|
| **Full fine-tuning** | update everything | checkpoint = model size; VRAM = pretraining VRAM |
| **BitFit** | train biases only | competitive but capped (GPT-3: 71.3 WikiSQL vs LoRA 73.4) |
| **Adapter layers** (Houlsby, Pfeiffer, Lin) | bottleneck MLPs inserted between blocks | **sequential depth ⇒ inference latency**, worse under model sharding |
| **Prefix / prompt tuning** (Li & Liang, Lester) | learn activations for virtual tokens | hard to optimise, **non-monotonic** in parameter count, and consumes sequence length |
| **[Soft-prompt conditioning](soft-prompt-cross-embodiment.md)** | per-*data-source* learnable embeddings | not a competitor — [X-VLA](../../entities/x-vla.md) **combines** it with LoRA |
| **LoRA** | low-rank `ΔW`, merged at deploy | — |

§4.1's structural argument: as capacity grows, adapters converge to an MLP and prefix methods to a model that cannot take long inputs; **LoRA converges to full fine-tuning**. It is a generalisation of it, not a substitute for it.

## Where it shows up in this wiki

Every VLA adaptation result here is a LoRA result:

- **[X-VLA](../../entities/x-vla.md)** — LoRA at **9 M params (1%)** matches fully-finetuned [π0](../../entities/pi-zero.md) at 3 B tuned: 93% [LIBERO](../../entities/libero.md), 54% Simpler-WidowX, ~300× fewer tuned parameters ([paper](../../sources/xvla-paper.md), Tab. 3). Also its unseen-embodiment transfer — AIRBOT cloth-picking from 200 demos, LoRA only.
- **[OpenVLA-OFT](../../entities/openvla-oft.md)** — the whole three-axis study is run *through* LoRA on ~500 demos ([paper](../../sources/openvla-oft-paper.md)). Its finding that autoregressive LoRA fine-tuning is still too slow (3–5 Hz) is a **throughput** objection, not a parameter-efficiency one — LoRA fixes training cost, not decoding cost.
- **[DreamGen](../../entities/dreamgen.md) / [GR00T N1](../../sources/groot-n1-paper.md)** — LoRA is how a **video world model** (WAN 2.1) is specialised to a robot's environment from ~88 h of teleop before generating 827 h of neural trajectories. A use outside policy learning entirely.
- **[FOREWARN](../../sources/forewarn-paper.md)** — Llama-3.2-11B-Vision-Instruct LoRA-tuned with a linear latent adapter, to make a VLM read a world model's latent states.
- **[TRL SFT Trainer](../../sources/huggingface-trl-sft-trainer.md)** — `peft_config=LoraConfig()`, the one-line invocation that makes all of the above ordinary.
- **[Jetson Thor vs DGX Spark](../../syntheses/platforms/jetson-thor-vs-dgx-spark.md)** — "LoRA-scale fine-tune" is the unit in which edge-training capability is quoted.

## Key references

- [LoRA: Low-Rank Adaptation of Large Language Models](../../sources/lora-paper.md) — Hu, Shen et al., Microsoft, 2021 (ICLR 2022). The primary.
- Aghajanyan, Zettlemoyer & Gupta 2020, *Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning* — the **direct antecedent**: pretrained LMs fine-tune efficiently within a low-dimensional random subspace. LoRA's hypothesis is that the *update* inherits this. Not ingested.
- Houlsby et al. 2019 (adapters), Li & Liang 2021 (prefix-tuning), Zaken et al. 2021 (BitFit) — the baselines. Not ingested.

## Related concepts

- [Soft-prompt cross-embodiment conditioning](soft-prompt-cross-embodiment.md) — the complementary axis; combined with LoRA in X-VLA.
- [Knowledge insulation](knowledge-insulation.md) — a different answer to the same worry: how to adapt without destroying what pretraining built.
- [VLA models](vla-models.md) — the model class LoRA is applied to throughout this wiki.
- [Scaling laws for VLAs](scaling-laws-vla.md) — LoRA's flat `r` curve is a *rank*-scaling result and sits oddly next to the data- and parameter-scaling literature.

## Open questions

- Does the §7.3 **amplification measurement** reproduce on an action model? Cheap to run, and it would say whether robot fine-tuning is amplification or acquisition.
- Why has attention-only targeting persisted as a default when the paper explicitly deferred the MLP question?
- Footnote 6's caveat — small `r` should fail when the downstream *distribution* is far from pretraining — is exactly the cross-embodiment case. It has not been tested at low rank on a genuinely novel embodiment.

## Mentioned in

- [LoRA paper](../../sources/lora-paper.md)
- [X-VLA paper](../../sources/xvla-paper.md)
- [OpenVLA-OFT paper](../../sources/openvla-oft-paper.md)
- [DreamGen paper](../../sources/dreamgen-paper.md)
- [GR00T N1 paper](../../sources/groot-n1-paper.md)
- [FOREWARN paper](../../sources/forewarn-paper.md)
- [Hugging Face TRL — SFT Trainer](../../sources/huggingface-trl-sft-trainer.md)
- [Wolfe — SFT blog](../../sources/wolfe-sft-blog.md)
