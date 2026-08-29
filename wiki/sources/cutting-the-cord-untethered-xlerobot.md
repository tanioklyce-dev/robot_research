---
title: "Cutting the Cord: System Architecture for Low-Cost, GPU-Accelerated Bimanual Mobile Manipulation"
type: source
url: https://arxiv.org/abs/2603.09051
author: "Artemis Shaw, Chen Liu, Justin Costa, Rane Gray, Alina Skowronek, Kevin Diaz, Nam Bui, Nikolaus Correll (CU Boulder)"
published: 2026-03
ingested: 2026-06-03
local_path: raw/2603.09051v1.pdf
sha256: db2bb3eab4fc81952820019998012a2cbb2c70b92e05d217ee655392e71b28b0
venue: arXiv 2603.09051v1
license: CC-BY-NC-ND 4.0
format: PDF (8 pp.)
tags: [xlerobot, jetson-orin-nano, onboard-compute, edge-ai, mobile-manipulation, bimanual, power-topology, lerobot, smolvla, act, diffusion-policy, slam, teleoperation, correll]
---

# Cutting the Cord: System Architecture for Low-Cost, GPU-Accelerated Bimanual Mobile Manipulation

## Summary

An **untethered evolution of the [XLeRobot](../entities/xlerobot.md)** from [Nikolaus Correll](../entities/nikolaus-correll.md)'s lab (CU Boulder): a low-cost bimanual mobile manipulator with **fully onboard GPU compute (NVIDIA [Jetson Orin Nano](../entities/jetson-orin-nano.md) Super)** for a total system cost **under $1,300** ($1,202 BOM). The paper's thesis is that the hard part of "cutting the cord" on a cheap mobile manipulator isn't the AI — it's the **systems engineering** of power integrity, structural stiffness, and thermal limits once you bolt a GPU onto a 3D-printed platform. Three contributions: **(1)** a stiffness-to-weight-optimized "High-Shell" print topology, **(2)** a **Tri-Bus power topology** that isolates the compute rail from motor-induced voltage transients, and **(3)** embedded autonomy (SLAM nav, IK manipulation, VR teleop) running on the Orin Nano. It is the wiki's first real-world, measured **onboard-Jetson XLeRobot build** — and the primary grounding for the [Jetson onboard-compute comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md).

## Key claims

### Platform & BOM
- **Total cost $1,202.28**, untethered. Headline BOM lines: **Jetson Orin Nano Super $249**, 17× Feetech STS3215 servos $271.83, **Anker SOLIX C300 $159.99**, Intel RealSense D435 $333.75, IKEA RÅSKOG cart $39.99. Dual SO-101 arms (5+1 DoF each) + LeKiwi omni base + 2-DoF neck = **17 DoF**, **1 kg/arm payload**, **>40 cm reach**, 1.20 m height.
- Positioned (Table I) against AhaRobot (~$2k, RTX 4060), Cone-E (<$12k), [Mobile ALOHA](../entities/aloha.md) (~$32k, RTX 3070 Ti), TB3+arms (~$3k, Pi 4, no GPU). "Ours" is the cheapest *untethered + GPU* entry.

### Tri-Bus power topology (the core systems contribution)
- Uses an **Anker SOLIX C300 (288 Wh / 300 W)** as the power-distribution unit — chosen over custom LiPo for built-in overcurrent protection. The paper states this unit exposes **three USB-C ports (two 140 W, one 100 W) and a 12 V DC car outlet rated 10 A**.
- **Problem:** on the original daisy-chained shared-bus design, concurrent bimanual + neck motion caused **voltage collapse from 12.2 V → 306 mV at t≈19 s**, forcing a power-cycle (repeated across all 5 trials). The 3 A / 5 A per-port ceilings couldn't handle peak dynamic loads → frequent **compute brownouts/resets**.
- **Fix — three isolated buses:** Bus A (wheels + neck) on a high-power USB-C rail; Bus B (the two arms, the high-draw load) consolidated on the **12 V/10 A car outlet**; the **Jetson isolated on its own USB-C rail**. A firmware "virtual fuse" caps each bus via a software Safe Operating Envelope `I(τ,α)` derived from the STS3215's 2.7 A stall current — arms capped ≈240 W (20 A @ 12 V), leaving **~60 W headroom for the Jetson (which draws 15–25 W)**.
- **Result:** revised Tri-Bus held **12.0 V (variance ≤0.1 V)** under identical stress, eliminating brownouts; **only 5 % battery discharge over 30 min** of full functional load.

### Onboard compute — Jetson Orin Nano benchmarks
- **Jetson Orin Nano Super: 67 INT8 TOPS, 102 GB/s memory bandwidth, 7–25 W** — "sufficient for vision backbones (YOLO), quantized LLMs (Llama 3.1), transformer policies (ACT, Diffusion Policy)." (Resolves the wiki's prior "no ingested TOPS figure for Orin Nano" open question.)
- **On-edge policy benchmark** (Orin Nano, MAXN SUPER, FP16 + fused SDPA; end-to-end camera→action latency):

  | Model | H | K | T | E2E latency | max replan freq |
  |---|---|---|---|---|---|
  | **ACT** | 100 | 50 | — | **36.0 ± 0.9 ms** | **27.8 Hz** |
  | **Diffusion Policy** | 20 | 10 | 10 | **539.6 ms** | **1.8 Hz** |
  | **SmolVLA (450 M)** | 20 | 10 | 10 | **713.8 ms** | **1.4 Hz** |

- **Key insight:** the bottleneck on edge is the **iterative action expert + denoising steps**, *not* the VLM. SmolVLA adds only minor overhead over Diffusion Policy — "high-parameter semantic heads are not the only prohibitive factor for high-frequency robotic control."
- **Thermal:** no throttling after **30 min continuous SmolVLA at peak load** (max GPU 54.6 °C), validating the passive ducting.
- **Limitation stated:** "The Jetson Orin Nano's limited CUDA kernels restrict high-frequency multi-modal transformers, while a **Jetson Thor (40–130 W) exceeds the power budget**" → motivates tiered compute or an additional power supply.

### Software / autonomy stack
- ROS 2 + **Pinocchio/Pink** task-IK (QP solver @ 100 Hz) + Open3D; classical RGB-D perception (HSV segmentation → 3D centroid → task-IK → Fin-Ray compliant grasp). **98.7 % grasp success** (N=75, 5 objects 17–858 g).
- **SLAM nav:** RealSense D435 + **RTAB-Map** (localization-only mode) + **Nav2**.
- **VR teleop** (Open-TeleVision-based): Meta Quest 3 / Vision Pro / Pico 4; controllers beat hand-tracking on a peg-in-hole task (48.2 s vs 68.3 s vs 248.7 s joypad baseline); doubles as an imitation-learning data-collection pipeline.

## Entities mentioned
- [Jetson Orin NX](../entities/jetson-orin-nx.md) — the drop-in upgrade from the Orin Nano this paper benchmarks.
- [XLeRobot](../entities/xlerobot.md), [Jetson Orin Nano](../entities/jetson-orin-nano.md), [Jetson Thor](../entities/jetson-thor.md) (as over-budget), [Nikolaus Correll](../entities/nikolaus-correll.md), [SO-ARM101](../entities/so-arm101.md) (SO-101 arms), [LeRobot](../entities/lerobot.md)/[LeKiwi](../entities/lekiwi.md), [SmolVLA](../entities/smolvla.md), [ACT](../entities/act.md), [Diffusion Policy](../entities/diffusion-policy.md), [Mobile ALOHA](../entities/aloha.md).
- [RTAB-Map](../entities/rtab-map.md) — the SLAM stack referenced.

## Concepts touched
- [VLA models](../concepts/learning/vla-models.md) — concrete on-edge VLA/BC latency numbers + the "action-expert-is-the-bottleneck" insight.
- [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — the comparison this source anchors.
- [XLeRobot + Thor power budget](../syntheses/projects/xlerobot-thor-power-budget.md) — corroborates the two-rail / power-transient problem and the C300 port set.

## Open questions / notes
- **C300 SKU question — resolved.** The paper cites its unit (ref [22]) as the **"Anker SOLIX C300 DC Portable Power Station," $159.99**, with **a 12 V/10 A car outlet + 3 USB-C (2×140 W + 1×100 W)**. The wiki's earlier web-sourced spec wrongly said the C300 *DC* lacked a 12 V car port; **the DC bank's 12 V car outlet is now confirmed** (user + this paper). Consequence: the DC bank serves both robot rails on its own (it does here), so the wiki's [Anker comparison](../syntheses/platforms/anker-portable-power-stations.md) no longer treats the AC station as required — only as a 600 W-surge upgrade.
- Design files are "doubleblind" (anonymized) in this v1 — no public repo link yet.
- No learned-policy *task* success on the real robot beyond grasping; VLA is benchmarked for latency, not deployed for closed-loop task completion. Onboard policy deployment is named as future work.
