---
title: "GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation (Yang et al., 2026)"
type: source
url: https://arxiv.org/abs/2605.22036
local_path: raw/2605.22036.pdf
sha256: a38f1b541a9710de653654bd04ba1316473305b141830d7941699e46d07864b9
author: "Jiahao Yang, Zihan Wang, Xiangyang Li, Xing Zhu, Yujun Shen, Yinghao Xu†, Shuqiang Jiang† (†corresponding)"
affiliations: "State Key Laboratory of AI Safety, ICT / Chinese Academy of Sciences; UCAS; Robbyant (Ant Group); National University of Singapore; HKUST"
published: 2026-05-21
venue: "arXiv preprint (v1), cs.CV, CVPR-style formatting; no peer-reviewed venue as of ingest"
format: paper (15 pp; 9 pp body + references + supplement)
arxiv: 2605.22036
code: https://github.com/jahhaoyang/GA-VLN
tags: [vision-language-navigation, VLN-CE, bird's-eye-view, BEV, 3D-foundation-model, VGGT, MLLM, LLaVA-Video, SigLIP, token-efficiency, stretch-3, habitat, R2R-CE, RxR-CE, robbyant]
ingested: 2026-09-12
---

# GA-VLN: Geometry-Aware BEV Representation for Efficient Vision-Language Navigation

## Summary

**Replace the video the navigation MLLM sees with a top-down map of where it has been.** GA-VLN lifts SigLIP patch features from the last eight RGB-D frames into 3D with depth and pose, adds features from a frozen **3D foundation model (VGGT-1B)** projected the same way, and mean-pools everything into an agent-centric **bird's-eye-view grid** (0.25 m cells, ±10 m) whose non-empty cells become the tokens a LLaVA-Video-7B backbone reads alongside the current front view and the instruction. Actions are discrete {forward, left, right, STOP}, emitted four at a time; the BEV is rebuilt once per eight actions.

Against the image-based MLLM navigators it competes with, the token count per step falls from **4,003 to 514**, MLLM compute from **32.2 to 8.7 TFLOPs**, latency from **343 to 259 ms**, and R2R-CE success rises from **51.5% to 61.0%** in the matched ablation — **without DAgger augmentation or VQA co-training**, which every strong baseline uses. Depth, pose, and rotation noise modelled on a [Stretch 3](../entities/stretch.md) cost under 2 points, and the model runs zero-shot on a physical Stretch 3 in a ~60 m² apartment with no obstacle-avoidance module, qualitatively.

> [!note] "State of the art" is true on R2R-CE, mixed elsewhere
> On **R2R-CE** val-unseen GA-VLN leads every column (SR 61.0 / SPL 55.2 vs InternVLA-N1's 58.2 / 54.0). On **RxR-CE** it leads SR (55.4 vs 53.5) but trails InternVLA-N1 on SPL (45.2 vs 46.1). On **NavRAG-CE**, after one extra fine-tuning epoch, it leads OSR (46.4) but **Dynam3D has the higher SR (24.7 vs 22.2) and SPL**. The abstract's *"state-of-the-art results"* is a fair summary of the main benchmark and an overstatement of the third.

## Key claims

### Benchmarks (Tab. 1, val unseen)

| | R2R-CE NE↓ / OSR / SR / SPL | RxR-CE SR / SPL | NavRAG-CE OSR / SR / SPL |
|---|---|---|---|
| **GA-VLN** (no DAgger) | **4.80 / 67.6 / 61.0 / 55.2** | **55.4** / 45.2 | **46.4** / 22.2 / 18.2 |
| InternVLA-N1 (DAgger) | 4.83 / 63.3 / 58.2 / 54.0 | 53.5 / **46.1** | — |
| StreamVLN (DAgger) | 4.98 / 64.2 / 56.9 / 51.9 | 52.9 / 46.0 | — |
| NaVILA (no DAgger) | 5.22 / 62.5 / 54.0 / 49.0 | 49.3 / 44.0 | — |
| Dynam3D (3D end-to-end) | 5.34 / 62.1 / 52.9 / 45.7 | — | 38.4 / **24.7** / **18.8** |

Training data: R2R-CE (10.8k trajectories), RxR-CE (20k), EnvDrop (146k), ScaleVLN (155k), SRDF (319k), MP3D + HM3D scenes in Habitat, 2 epochs. Monocular 60° forward camera.

### The efficiency ablation (Tab. 2, 3)

| | Tokens/step | MLLM TFLOPs | Latency | R2R-CE SR |
|---|---|---|---|---|
| Image-based baseline | 4,003 | 32.19 | 342.9 ms | 51.5 |
| + depth-projected BEV | 394 | 5.15 | 212.9 ms | 59.2 |
| + VGGT priors (**GA-VLN**) | 514 | 6.76 (+1.97 for VGGT) | 258.7 ms | **61.0** |

- **The explicit projection does most of the work** (+7.7 points, 8× fewer tokens); the 3D foundation model adds +1.8 for a 22% latency increase.
- The same ordering holds with the SRDF corpus removed (46.5 → 51.5 → 53.6), which the authors offer as evidence the gain is architectural, *"independent of data volume."*
- Grid size: 0.25 m beats 0.125 m (51.3) and 0.5 m (50.5). History: 32 steps ≈ 48 (54.4); 64–96 saturate or fall — *"more distant observations offer limited benefit due to their reduced spatial relevance and accumulated noise in the BEV space."*
- Naively appending depth tokens (8,006 tokens) scores 38.6 SR — worse than RGB alone — so *"simply appending depth features is not"* the answer (Tab. 8).

### Robustness and the real robot (Tab. 4, Sec. 4.5, Supp. A)

- Gaussian noise *"modeled after real-world error profiles of Stretch 3"*: depth σ = 0.05 m → SR 59.1; pose 0.05 m → 59.8; rotation 5° → 58.3 (from 61.0). Credited to grid aggregation and VGGT's cross-view consistency.
- Physical Stretch 3, ~60 m² apartment matched to simulator layouts, observations over Wi-Fi to a workstation. Adaptations: 15° turn step, BEV from up to 16 frames updated every 4 steps, two-round dialogue disabled. **No obstacle avoidance or navigable-point filtering.** Limitations stated: *"the agent occasionally executed paths dangerously close to obstacles (e.g., hugging walls), as it optimized for the shortest path trained in simulation,"* and discrete actions gave *"imprecise stopping."* Results are qualitative figures; no success count.

## Why it matters in this wiki

- **A second navigation lineage.** The [visual-navigation-policies](../concepts/robotics/visual-navigation-policies.md) page traces the RAIL image-goal line (GNM → ViNT → NoMaD → OmniVLA): ~50M-parameter models, normalized waypoints at 3–4 Hz. GA-VLN belongs to the *other* line — NaVid, NaVILA, StreamVLN, InternVLA-N1 — 7B MLLMs on the Habitat VLN-CE benchmarks with discrete 0.25 m / 15° actions. The two lines do not cite each other and are not evaluated on the same thing; this page is the wiki's first primary from the MLLM side.
- **What a 3D foundation model buys.** The [spatial-intelligence](../concepts/world-models/spatial-intelligence.md) page collects claims that geometry-trained models transfer; here the measurement is +1.8 SR points on top of explicit projection, with depth already available. Small, positive, and paid for in latency.
- **Token economy as the design variable.** 4,003 → 514 tokens is the whole efficiency story; the MLLM's compute falls 4.8× and success rises. The [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) has no entry for this class; at ~259 ms per four-action decision on a workstation it would sit near 4 Hz, in the reactive band, but the robot-side loop (Wi-Fi round trip) is unmeasured.
- **[Robbyant](../entities/robbyant.md)** — Ant Group's robotics arm appears as an author affiliation on an academic VLN paper, not only as a model vendor.
- **Stretch 3 as the default research body**, again — one of four papers ingested today that deploy on a Stretch.

## Entities mentioned

- [Stretch](../entities/stretch.md) — Stretch 3, noise model and real-world deployment.
- [Robbyant](../entities/robbyant.md) — affiliation of three authors.
- [Habitat](../entities/habitat.md) — simulator for VLN-CE.
- [SigLIP](../entities/siglip.md) — visual encoder.
- VGGT-1B, LLaVA-Video-7B, InternVLA-N1, StreamVLN, NaVILA, Dynam3D — no entity pages.

## Concepts touched

- [Visual navigation policies](../concepts/robotics/visual-navigation-policies.md) — the MLLM-VLN lineage, first primary.
- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md) — explicit vs implicit geometry, measured.
- [Cross-embodiment](../concepts/learning/cross-embodiment.md) — discrete forward/turn actions are the most embodiment-agnostic navigation interface there is.

## Open questions

- **Real-world success rate.** None reported; the deployment is qualitative.
- **Depth dependence.** The BEV needs metric depth and pose; how it degrades on a robot without a depth camera or with drifting odometry beyond σ = 0.05 m is untested.
- **Why does the VGGT gain shrink under noise?** Not measured separately; the robustness table is for the full model only.
- **NavRAG-CE.** Second on SR after one fine-tuning epoch; whether more closes the gap to Dynam3D is not shown.
