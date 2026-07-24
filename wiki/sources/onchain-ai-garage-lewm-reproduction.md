---
title: "Onchain AI Garage — I Reproduced LeCun's JEPA World Model That Doesn't Predict Tokens (video, 2026-04-24)"
type: source
url: https://www.youtube.com/watch?v=VQ15-MhZE2k
author: Onchain AI Garage (YouTube channel)
affiliation: independent / newsletter ("AI Garage Weekly" at on-chain-ai-garage.com per the host's mention in the video)
published: 2026-04-24
duration: 27 min (1634 s)
ingested: 2026-05-14
tags: [video, reproduction, leworldmodel, lewm, jepa, sigreg, two-room, rtx-3060, wsl2, claude-code, popular-explainer]
---

> [!note] Ingest depth
> Read from the **full auto-generated YouTube transcript** (~26,000 chars, 798 snippets, 1634 s). The video has no slide deck or paper to cross-reference; the transcript is the entire source.

## Summary

**A walk-through video where the host trains [LeWM](../entities/leworldmodel.md) from scratch on Two Room** using the official `stable-worldmodel` repo, on a 5-year-old consumer GPU (RTX 3060, 12 GB VRAM) running WSL2 on Windows, using Claude Code as the implementation assistant. The first half is a popular-explainer for [JEPA](../concepts/world-models/jepa.md) and the LeWM paper's contribution; the second half is the actual reproduction. Result: **92% success rate on Two Room** (paper: 97%) after **4 epochs / ~8 hours of training** (paper: 10 epochs on an L40S in a few hours).

**Why this matters to the wiki.** Until this ingest, **the wiki had no independent reproduction of LeWM on record** — everything was paper-derived. This video is **the first concrete data point that LeWM trains and produces paper-ballpark numbers on consumer hardware**, validating the [LeWM hello-world project scope](../syntheses/projects/lewm-hello-world-project-scope.md) and the [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) as feasible. Specifically:

- **Hardware floor lowered.** The paper's headline GPU is an L40S (181 TFLOPS). This reproduction lands paper-ballpark Two Room numbers on an **RTX 3060 (13 TFLOPS, ~14× slower)** — i.e. the project is trainable on hobbyist hardware in single-overnight runs.
- **End-to-end pipeline works.** The host successfully runs `stable-worldmodel` install + LEWM training + CEM-MPC evaluation through a series of WSL2 gotchas (Python version downgrade, batch-size-128 OOM → batch 64 + 2× grad accumulation, `expandable_segments` tweak, num_workers 4→2 for CUDA-stability). The four gotchas the [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) documents are corroborated.
- **Training dynamics roughly match the paper.** Prediction loss: 0.08 → 0.014 (paper: 0.25 → ~0). SIGReg loss: 28 → 1.4 (paper: 40 → ~0). The host explicitly comments that the **SIGReg loss curve descending alongside the prediction loss** is the no-collapse signal — corroborating the curriculum's framing.

**Quality caveat.** This is a popular-explainer video, not a research artifact. The host appears to use Claude Code throughout for both planning and execution; some technical descriptions are slightly imprecise (e.g., conflating Two Room being the "smallest" environment with it being the "easiest"). Treat the *outcome* (92% on Two Room) as the load-bearing claim; the *narration* is curriculum-orientation material, not a paper-quality source.

## The setup

- **Hardware:** RTX 3060, 12 GB VRAM (consumer GPU, 5 years old, "~$300").
- **OS / environment:** Windows main PC + WSL2 (required because the [`stable-worldmodel`](../entities/stable-worldmodel.md) repo is Linux-only).
- **Software:** Python (downgraded from latest after dependency conflict), PyTorch, the official `stable-worldmodel` repo and `lewm` subpackage.
- **Dataset:** Two Room only (3.43 GB archive, 12.8 GB extracted, ~920K frames). Chosen because it's the smallest environment in the paper and the only one that fits the host's GPU + time budget. Other paper environments (PushT, Reacher, OGBench-Cube) were not attempted.
- **Helper:** Claude Code (in WSL) drove environment setup, smoke-test debugging, batch-size tuning, and the markdown handoff between the host's Windows planning session and the WSL training session.

## Training notes (the gotchas)

The host worked through several issues that **directly mirror the four gotchas the [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) documents**:

1. **Python version mismatch** — newest Python broke dependencies; had to downgrade.
2. **Batch 128 OOM at training time** (forward pass fits, full training state doesn't on 12 GB). Resolved via batch 64 + 2× gradient accumulation for an effective batch of 128.
3. **CUDA "unknown error"** intermittently surfaced; flagged as a "known WSL2 pain point." Mitigated by setting `expandable_segments` and reducing num_workers 4→2.
4. **Throughput shortfall** — initial estimate was 20 hours; reduced to ~8 hours by using `torch.compile` (~2× speedup) and dropping target epochs from 10 → 5 (the host's stated heuristic: "5 epochs gets us 90% of the way").

CUDA crashed in epoch 5; metrics had **plateaued from epoch 3**, so the host stopped at 4 epochs and proceeded to evaluation.

## Results (vs the paper)

| Metric | Onchain AI Garage (this video) | LeWM paper |
|---|---|---|
| Two Room success rate | **92% (46/50)** | **97%** |
| Epochs trained | 4 | 10 |
| Wall-clock | ~8 h | "a few hours" |
| Prediction loss trajectory | 0.08 → 0.014 | 0.25 → ~0 |
| SIGReg loss trajectory | 28 → 1.4 | 40 → ~0 |
| History size | 3 | (paper default) |

**5 points below the paper on a single environment, with 40% of the training epochs and 14× slower hardware**, is well within "successful reproduction" tolerance. The host also produced eval video clips showing the trained agent's CEM-MPC plan vs an expert demo, and a sample of one of the four failing episodes (agent got stuck in a corner trying to cross between rooms).

## The popular-explainer half (first ~12 min)

This is the part most useful as **curriculum-orientation material** for Modules 10–12. The host walks:

1. **JEPA vs token prediction.** LLMs predict the next token; JEPA predicts the next *latent state*; a world model predicts the next *meaningful state of the environment*. Three concrete examples: "John put the glass on the edge of the table…" (text), tennis-racket pull-back (video), cluttered-table robot gripper (physical scene).
2. **Pixel prediction vs latent prediction.** The "wasteful generative side vs the meaning-skipping JEPA side." Same framing as [Welch Labs](welchlabs-lecun-1b-bet-against-llms.md), but presented as a hands-on engineer rather than a polished mini-doc.
3. **The JEPA lineage.** I-JEPA 2023 → V-JEPA 2 2025 → VL-JEPA 2025 → LeWM 2026. The host explicitly names this as "a research program across modalities, not a single paper."
4. **LeWM's contribution.** "Earlier JEPA approaches needed a stack of stabilizers… LeWM throws out this whole stack. No frozen pre-trained encoder, no EMA target network, no stop-gradient trick. None of this. What stays? Prediction loss plus one regularizer." The host then names the regularizer ("Sig Reg") and flags that it appears in the loss curves later.

The framing is on-point but pop-rendered; **for the wiki this video is the popular-explainer companion to [Welch Labs](welchlabs-lecun-1b-bet-against-llms.md)**, with the distinction that it ends with an actual reproduction.

## What the video confirms that the wiki was previously inferring

1. **LeWM trains on 12 GB consumer GPUs.** The [LeWM-on-ROSOrin-Pro feasibility analysis](../syntheses/projects/lewm-on-rosorin-pro-feasibility.md) and [LeWM hello-world project scope](../syntheses/projects/lewm-hello-world-project-scope.md) assumed this; this video is the first independent confirmation.
2. **The `stable-worldmodel` install is the friction point, not the science.** Most of the host's day was spent on Python versions, WSL2 quirks, and batch sizing — not on understanding the architecture or hyperparameters.
3. **SIGReg loss descending alongside the prediction loss is the no-collapse signal.** The curriculum (Module 12) frames this as the diagnostic to watch; the host independently arrives at the same diagnostic in the video.
4. **Two Room is a real environment, fully runnable.** Earlier wiki entries flagged Two Room as "the LeWM failure-mode environment" — the paper's Two Room result is *weaker* than PLDM (it's where SIGReg's isotropic-Gaussian assumption is most strained). This video shows the failure-mode result is still 92% on consumer hardware, i.e. **"weakest result" is not "broken."**

## Entities mentioned

- **[LeWorldModel](../entities/leworldmodel.md)** — the model reproduced.
- **[Yann LeCun](../entities/yann-lecun.md)** — the host frames LeWM as part of LeCun's research program. Mentions LeCun's Turing Award (2018) and his "AI must build internal models of how the world works" position.
- **[Anthropic Claude (via Claude Code)](../entities/anthropic.md)** — implementation assistant; the host used Claude Code in WSL to drive the install + smoke tests + bug-fixes throughout.
- **Onchain AI Garage** — the channel and the host's "AI Garage Weekly" newsletter. Newsletter URL the host cites verbally: "on-chain-ai-garage.com" (not independently verified during this ingest).

## Concepts touched

- **[JEPA](../concepts/world-models/jepa.md)** — primary topic of the explainer half.
- **[Joint-Embedding Predictive Architecture / Siamese ancestors](../concepts/world-models/siamese-network.md)** — implicit; the host frames LeWM as JEPA-as-research-program.
- **[Latent space](../concepts/world-models/latent-space.md)** — the "latent vector Z" the encoder produces.
- **[World model](../concepts/world-models/world-model.md)** — the "world model level" of prediction the host distinguishes from "latent level" and "token level."
- **SIGReg** — named ("Sig Reg") and shown as a loss curve; explained as the no-collapse signal.
- **CEM-MPC** — the host names "CEM (Cross Entropy Method)" as the search algorithm used in evaluation. Light treatment, but correct.

## Curriculum hookup

This video is the **first independent reproduction artifact** in the wiki. Add as supplementary material to:

- **[Curriculum Module 12 — LeWorldModel deep-dive](../syntheses/curriculum/curriculum-12-lewm-deep-dive.md)** — popular-explainer + reproduction companion to the paper.
- **[LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md)** — corroborates the four gotchas the howto already documents.
- **[LeWM hello-world project scope](../syntheses/projects/lewm-hello-world-project-scope.md)** — concrete prior art for "what happens when someone outside the paper authors reproduces LeWM."

## Open questions / TBD

- **Was this *actually* a from-scratch train, or did the host use a HuggingFace pretrained checkpoint?** The host says training was from scratch, and the loss curves shown are training curves — but the wiki's [hello-world scope](../syntheses/projects/lewm-hello-world-project-scope.md) explicitly contrasts "loading the `quentinll/lewm-pusht` HF checkpoint" with "training from scratch." If a follow-up reproduction is desired, distinguishing these is critical.
- **The host's prediction-loss starting value (0.08) is substantially lower than the paper's (0.25)** — possibly due to a different normalization, Two Room being simpler than PushT, or different hyperparameters. Worth checking against `stable-worldmodel` defaults.
- **Newsletter URL** (`on-chain-ai-garage.com`) is mentioned verbally but not verified. If the author becomes a recurring source, this is worth confirming.
- **The host's use of Claude Code throughout** is wiki-relevant — it's the first example in the wiki of someone using a coding agent end-to-end to drive a JEPA reproduction. The pattern (plan in main session → handoff markdown → execute in WSL session) is a generalizable template.
