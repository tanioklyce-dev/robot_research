---
title: ACT (Action Chunking Transformer)
type: entity
subtype: method
created: 2026-05-25
updated: 2026-08-03
sources: 16
tags: [act, action-chunking, transformer, imitation-learning, behavior-cloning, aloha, mobile-aloha, tony-zhao, stanford, lerobot]
---

**ACT (Action Chunking Transformer)** — imitation-learning method introduced by **Tony Z. Zhao et al. (Stanford, RSS 2023)** as the default policy for [ALOHA](aloha.md). Predicts a **chunk** (sequence) of future actions per timestep from observation history, instead of one action at a time. The "chunking" formulation is the contribution: it improves trajectory coherence, reduces per-step inference latency, and is now near-default across 2024–2026 BC and [VLA models](../concepts/learning/vla-models.md).

## Approach (per the [Mobile ALOHA paper](../sources/mobile-aloha-paper.md) reference)

- Transformer-based encoder-decoder over a fixed observation window.
- Predicts an action chunk of length **k** (typically 50–100 timesteps).
- Executes the first k action steps before re-predicting (vs Diffusion Policy's `T_a < T_p` receding-horizon approach).
- **Action chunking** as a primitive: predicting longer sequences helps with non-Markovian / multi-modal demonstrations and absorbs per-step jitter.
- Compatible with **co-training over heterogeneous bimanual datasets**: Mobile ALOHA uses ACT as the default and shows co-training gains of up to +95% absolute success on hard mobile-manipulation tasks ([source](../sources/mobile-aloha-paper.md), Table 1).

## Why it matters

- **The default policy class for the [ALOHA](aloha.md) / [Mobile ALOHA](aloha.md) platform line** — and increasingly for the broader bimanual-teleop ecosystem ([LeRobot](lerobot.md) docs surface ACT as a reference policy as well).
- **Popularized action chunking** as an IL primitive. The 2023 result that predicting a sequence outperforms per-step prediction is now baseline assumption across [Diffusion Policy](diffusion-policy.md), the Pi VLAs, and [RUMs](robot-utility-models.md).
- **Method-agnostic co-training compatibility** — Mobile ALOHA shows ACT + co-training beats no-co-train in 5/7 tasks, with average +34% absolute improvement; Diffusion Policy + co-train also benefits (+30/+20 on Wipe Wine / Push Chairs) but less than ACT; VINN+chunking gets mixed results.

## Codebase evolution

- **Original ACT** — first introduced with original ALOHA (Zhao et al. RSS 2023).
- **[ACT++](act-plus-plus.md)** ([MarkFzp/act-plus-plus](https://github.com/MarkFzp/act-plus-plus)) — the mobile-extended successor shipped with [Mobile ALOHA](aloha.md). Adds the 16-dim action vector (14 arms + 2 base), the co-training-with-static-data recipe, and the action-chunk delay-shift trick.
- **LeRobot's ACT implementation** — independent re-implementation in the [LeRobot](lerobot.md) framework; covered in the **["Robot Learning: A Tutorial"](../sources/lerobot-robot-learning-tutorial.md)** with a runnable code example (`fracapuano/robot_learning_tutorial_act_example_model`). NVIDIA's archived **[Jetson AI Lab LeRobot tutorial](../sources/nvidia-jetson-ai-lab-lerobot.md)** uses ACT as the default policy trained *onboard a Jetson* (`policy=act_koch_real`) on Koch v1.1 — a concrete edge-training instance of ACT being chosen for its small footprint.

## Open questions

- The original 2023 ACT paper is **not yet ingested** in this wiki — the wiki's view of ACT comes via the Mobile ALOHA paper (which uses it as a baseline and describes its mechanics in passing) plus the [LeRobot tutorial](../sources/lerobot-robot-learning-tutorial.md) and references on [chelsea-finn.md](chelsea-finn.md) and [imitation-learning.md](../concepts/learning/imitation-learning.md). A direct ACT paper ingest would refine architectural details (encoder depth, action-chunk length k, training tricks, the [VAE](../concepts/learning/variational-autoencoder.md)-style action distribution model — a conditional VAE, whose substrate paper is now ingested as the [VAE Paper](../sources/vae-paper.md)).
- **Multi-task / language-conditioned ACT** — the wiki has no coverage of multi-task extensions; the published 2023/2024 work is single-task.

## Related
- [ALOHA / Mobile ALOHA](aloha.md) — the platform ACT was introduced with.
- [ACT++](act-plus-plus.md) — the mobile-extended codebase.
- [Diffusion Policy](diffusion-policy.md) — contemporary BC method; both use action chunking.
- [Tony Z. Zhao](tony-zhao.md) — first author.
- [Chelsea Finn](chelsea-finn.md) — senior author.
- [Imitation learning](../concepts/learning/imitation-learning.md) — concept; ACT is the canonical action-chunked BC reference.
- [LeRobot](lerobot.md) — surfaces ACT as a reference policy; LeRobot tutorial uses ACT as the canonical IL example.

## LeRobot ICLR 2026 benchmark numbers

From [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) Tables 2 + 3 (fp32):

- **52 M params** (smallest of the 4 reference policies).
- **Peak memory** 211 MB on RTX 4090/A100; 462 MB MPS; 817 MB CPU.
- **Avg latency** 5.0 ms RTX 4090, 13.8 ms A100 — **~100–200 Hz** on high-end GPUs.
- Paper attributes ACT's popularity dominance (Figure 7) to (1) small size + fast inference and (2) usability with as few as **50 real-world trajectories**.

## Mentioned in
- [Mobile ALOHA Paper](../sources/mobile-aloha-paper.md)
- [Mobile ALOHA project page](../sources/mobile-aloha-project-page.md)
- [Robot Learning: A Tutorial (LeRobot)](../sources/lerobot-robot-learning-tutorial.md)
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — supported by LeRobot; benchmark numbers above; explicitly cited as the dominant single-task BC policy in the ecosystem.
- [NVIDIA Jetson AI Lab — HuggingFace LeRobot (archived)](../sources/nvidia-jetson-ai-lab-lerobot.md) — ACT as the default onboard-Jetson training target on Koch v1.1.
- [VLA-0 paper](../sources/vla-0-paper.md) — borrows ACT's **prediction-ensembling / action-chunking** trick as its single biggest accuracy lever (+2 pts on LIBERO).
- [OpenVLA-OFT paper](../sources/openvla-oft-paper.md) — adopts ACT's **L1-regression continuous-action head** + action chunking; finds L1 matches diffusion at lower cost.
- [Introducing Waddle (Waddle Labs, 2026)](../sources/waddle-labs-introducing-waddle.md) — an [LLM agent](../concepts/agents/llm-agent-architecture.md) autonomously collected ~1,000 LEGO pick-and-place trials overnight and **trained an ACT policy from scratch** — ACT as the target of agent-driven data collection + training.
