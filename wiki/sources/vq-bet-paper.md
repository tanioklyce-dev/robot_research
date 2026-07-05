---
title: VQ-BeT — Behavior Generation with Latent Actions (paper)
type: source
url: https://arxiv.org/abs/2403.03181
author: Seungjae Lee, Yibin Wang, Haritheja Etukuru, H. Jin Kim, Nur Muhammad Mahi Shafiullah, Lerrel Pinto
published: 2024-03 (ICML 2024, PMLR 235:26991-27008; arXiv 2403.03181v2)
ingested: 2026-05-16 (abstract-level); deepened 2026-07-04 from full PDF
local_path: raw/VQ-BeT_2403.03181v2.pdf
format: 'pdf (18 pp.: main 1–9, appendices A–C)'
tags: [vq-bet, behavior-cloning, vector-quantization, residual-vq, transformer, mingpt, nyu, icml-2024, stretch]
---

## Summary
The primary [VQ-BeT](../entities/vq-bet.md) paper from NYU's Pinto group, ICML 2024. Direct successor to [BET](../entities/bet.md) (NeurIPS 2022). Replaces BET's **k-means action clustering** with a **Residual VQ-VAE** (SoundStream lineage) that tokenizes continuous actions (or action chunks) end-to-end with gradient information, then trains a MinGPT transformer to predict hierarchical latent action codes. Evaluated across **eight environments** spanning simulated manipulation, autonomous driving (nuScenes), and real robots — SOTA in 5/7 unconditional and 6/7 goal-conditional benchmarks vs BeT, [Diffusion Policy](../entities/diffusion-policy.md), and BESO, at **5× faster inference in simulation and 25× on a real [Stretch](../entities/stretch.md)**. The strongest performer in the [Robot Utility Models](robot-utility-models-paper.md) ablation at full data scale.

## Key claims

### Residual VQ action tokenizer (§2.3, §3.2; Table 13)
- **Two-stage training.** Stage 1: Residual VQ-VAE over actions/action chunks — encoder φ, decoder ψ; first codebook quantizes φ(a), each residual is recursively quantized by the next layer; final latent = Σ residual embeddings. Loss = L1 reconstruction + VQ commitment (λ=1); codebooks updated by EMA, not gradients. Stage 2: freeze the tokenizer, train the transformer.
- **N_q = 2 residual layers in ALL experiments** — the "hierarchy" is exactly two levels: the first-layer code is the **primary code** (coarse dataset-wide clustering), the second the **secondary code** (refinement).
- **Codebook sizes 8–16 per layer → 64–256 code combinations**; latent dim 512 (256 for BlockPush).
- **Offset head** ζ_offset adjusts the decoded centroid for full continuous fidelity: action = ψ(Σ codes) + offset. Ablation: "offset prediction is quite important."
- **Stage-2 loss**: **Focal loss** on codes — Focal(primary) + β·Focal(secondary), β=0.1 typical (0.5–0.6 for Ant/real-world) — plus L1 offset loss.

### Architecture (§3.3; Table 13)
- Backbone: **MinGPT**, 6 layers / 6 heads / 120-dim embeddings (BlockPush: 4/4/72). **No total parameter count is published** — "VQ-BeT models are small and fast."
- Observation windows: 3–10 typical; **100 for Multimodal Ant**. Vision: ResNet-18 (sim); Dobb·E's HPR encoder fine-tuned (real world).
- **Action chunking mostly off** (length 1; UR3 10, PushT 5, nuScenes 6): where tried, chunking *hurt* (Fig. 5: Ant collapses ~3.2→0.5 goals) — "since VQ-BeT models are small and fast, action chunking isn't necessary even when running on a real robot in real time." A notable counterpoint to the [Diffusion Policy](diffusion-policy-paper.md)/ACT chunking orthodoxy.
- Causal primary→secondary code prediction: off in sim (hurt in Kitchen, called "anomalous"), **on and important for real-world performance** (§4.6).

### Benchmarks (Tables 1–2; App. Tables 8–10)
Eight environments: PushT, Image PushT, Franka Kitchen, Image Kitchen, BlockPush, UR3 BlockPush, Multimodal Ant, nuScenes.
- **Unconditional** (vs BC / BeT / DP-C / DP-T): PushT **0.78** (DP-T 0.74); Image PushT **0.68** (DP-C 0.66); Kitchen **3.66**/4 (DP-T 3.44); Ant **3.22** (DP-C 3.12); UR3 **1.84**; loses Image Kitchen (2.98 vs DP-C 3.11) and BlockPush (1.79 vs DP-T 1.93).
- **Goal-conditional** (vs GCBC / C-BeT / C-BESO / CFG-BESO): SOTA 6/7 — e.g. PushT 0.39 vs C-BESO 0.30; Image PushT 0.10 (all baselines ≤0.02); Kitchen 3.78; Ant 1.72. Loses BlockPush (0.87 vs C-BESO 0.93; attributed to trivially simple 2-D action space + largest dataset).
- **nuScenes driving**: avg L2 **0.73 m** / collision 0.29% — best L2 among all methods including full-information ones (Agent-Driver 0.74, UniAD 1.03, GPT-Driver 0.84).
- Keeps its lead at 1/4 and 1/10 data (App. Table 8).

### Inference speed (Table 3, Fig. 7, Table 7)
- Headline: **5× vs Diffusion Policy in sim, 25× on real robots**.
- Kitchen conditional single-step: VQ-BeT **15.1 ms** vs DP-C 100.5 / DP-T 98.6 ms (10-step diffusion). PushT per step: VQ-BeT 3.17 ms vs DP-T 77.5 / DP-C 103.1 ms.
- Real robot: RTX A4000 18.06 ms vs 573.49 ms; **Stretch onboard 4-core CPU: 207 ms vs 5,244 ms** — the 25×.
- Context for the 25×: **receding-horizon Diffusion Policy fails completely (0/30) on Stretch** — the low-cost robot's controller noise pushes open-loop rollouts out of distribution within ~3 timesteps, forcing diffusion to run fully closed-loop (47/60 closed-loop). A materially important finding for the wiki's budget-hardware thread ([XLeRobot](../entities/xlerobot.md), [Cutting the Cord](cutting-the-cord-untethered-xlerobot.md)'s 1.8 Hz on-edge Diffusion number).

### Real-robot results (§4.7; Tables 5–6)
- [Stretch](../entities/stretch.md) in a kitchen setup; Dobb·E-style Stick collection; **45 demos/task**; 12 tasks (5 single-phase, 3 two-phase, 4 long-horizon).
- Single-phase: **47/50** vs modified DP-T 45/50 vs BC 29/50. Two-phase: **19/30** vs DP-T 11/30 (the "73% improvement on long-horizon tasks" headline). Long-horizon: ≥3× DP's success at end of all four tasks; the margin **widens** toward episode end.
- Multimodality preserved: closes fridge and toaster doors in both orders across rollouts.

### Ablations (§4.6, Fig. 5; App. B.1 Table 12)
- Vanilla (single-layer) VQ instead of residual VQ: "significant negative impact." β=1 (equal code-loss weights): similar drop — the primary/secondary hierarchy carries the expressivity.
- **Codebook-size insensitivity**: scaling from 64–256 combos to up to 65,536 (10–250×) has little impact; with 256× more combos, full-code prediction accuracy falls to 0.08× but **primary-code accuracy retains 0.8×** and task performance drops only ~4.5% — VQ-BeT leans on primary-code resolution and de-weights secondary codes as codebooks grow.
- Behavior entropy over task-completion order (§4.3): best on 4/5 envs (Kitchen p4-entropy 4.07 vs BeT 4.01, DP-T 3.89) — mode capture, not just success rate.

### Author lineage
- **Seungjae Lee** — RUM co-author; **Etukuru, [Shafiullah](../entities/mahi-shafiullah.md), [Pinto](../entities/lerrel-pinto.md)** — the [Dobb·E](../entities/dobb-e.md) → [RUM](../entities/robot-utility-models.md) → VQ-BeT NYU continuity.
- Code: <https://github.com/jayLEE0301/vq_bet_official>; project page <https://sjlee.cc/vq-bet/>.

## Entities mentioned
- [VQ-BeT](../entities/vq-bet.md) — primary source. [BET](../entities/bet.md) — predecessor. [Diffusion Policy](../entities/diffusion-policy.md) — main baseline. [PushT](../entities/pusht.md), [Franka Panda](../entities/franka-panda.md) (Kitchen), [Stretch](../entities/stretch.md), [Dobb·E](../entities/dobb-e.md) (HPR encoder + Stick), [Robot Utility Models](../entities/robot-utility-models.md) — downstream consumer. BESO / C-BESO — diffusion-BC baseline without a wiki page.

## Concepts touched
- [Imitation learning](../concepts/learning/imitation-learning.md) — headline BC method; the anti-chunking finding qualifies the action-chunking convention.
- [Latent space](../concepts/world-models/latent-space.md) — discrete latent *action* space via residual VQ (vs the latent *state* spaces of the WM line).
- [Curriculum Module 7 — BC lineage on PushT](../syntheses/curriculum/curriculum-07-bc-lineage-pusht.md) — IBC → BeT → DP → VQ-BeT is the module's spine; this deepening supplies the VQ-BeT-side numbers.

## Open questions
- ~~Codebook size / hierarchy depth / transformer dims~~ — resolved above (N_q=2, 8–16 codes/layer, MinGPT 6/6/120).
- ~~What does long-range modeling buy?~~ — behavior-entropy metric + widening long-horizon margins on Stretch.
- **Parameter count still unpublished** — "small and fast" is qualitative; only layer dims are citable.
- Training cost vs Diffusion Policy (the orthogonal axis to the 5× inference win) — still not reported.
- No RL fine-tuning anywhere — pure BC; the RVQ token space seems natural for RL-over-tokens follow-ups (cf. [π*0.6](pistar06-paper.md)'s advantage conditioning) but the paper doesn't go there.
