---
title: "Jetson Thor Expands: T3000, T2000 & IGX T3000 (NVIDIA blog)"
type: source
url: https://blogs.nvidia.com/blog/jetson-thor-robotics-edge-ai-agent/
author: Chen Su (NVIDIA)
published: 2026-07-15
ingested: 2026-07-15
format: company blog
tags: [jetson-thor, t3000, t2000, igx-t3000, nvidia, blackwell, edge-ai, physical-ai, cosmos-3-edge, halos, functional-safety, jetpack-7, agentic-ai]
---

# Jetson Thor Expands: T3000, T2000 & IGX T3000 (NVIDIA blog)

## Summary

NVIDIA extends the **[Jetson Thor](../entities/jetson-thor.md)** family *downward* with three new SKUs below the flagship T5000/T4000: **Jetson T3000** (32 GB), **Jetson T2000** (16 GB, entry-level), and the safety-certified **IGX T3000**. The Jetson line now advertises **"a scalable edge AI platform spanning performance from 70 TOPS to 2,000 teraflops"** — Orin-class at the bottom to Thor T5000 at the top. The post also brings **Cosmos 3 Edge** (a 4-billion-parameter embodied foundation model) to the Thor lineup and introduces **Jetson Agent Skills** that automate on-device memory optimization. Availability: **emulation mode later in July 2026 (JetPack 7.2.1)**; **general availability Q1 2027**. Pricing not disclosed.

## Key claims

**New SKUs**

| SKU | AI compute | Memory | CPU | Notes |
|---|---|---|---|---|
| **Jetson T3000** | 865 FP4 TFLOPS | 32 GB LPDDR5X (273 GB/s) | 8-core Neoverse Arm | 25 GbE; ~50% smaller / lower power than T5000; "inference performance comparable to T5000 for multimodal workloads" |
| **IGX T3000** | = T3000 | 32 GB | — | Adds **integrated functional safety**; runs **NVIDIA Halos for Robotics** full-stack safety system |
| **Jetson T2000** | 400 FP4 TFLOPS | 16 GB | — | Entry-level Thor architecture |

- **Platform range**: *"70 TOPS to 2,000 teraflops"* across the Jetson line.
- **Section 1 — "Unlocking Humanoid and Robotics Deployment With T3000"**; **Section 2 — "Going Wide on Edge AI With T2000."**

**Cosmos 3 Edge** — *"Delivering Cosmos 3 Edge to NVIDIA Thor Lineup"*: a **4-billion-parameter foundation model for embodied systems** that *"can post-train for specific embodiments in about a day"* — the edge sibling of [Cosmos 3](../entities/nvidia-cosmos.md) Nano/Super.

**Jetson Agent Skills** — new on-device agents that *"automate memory optimization, system configuration, and deployment"*, achieving *"significant memory savings in days instead of weeks."* Case studies: UBTech / Agile Robots / Connect Tech "up to 15 GB" reduced; SandStar "up to 4 GB"; NoTraffic "30% on Jetson TX2 NX"; GROOVE X (LOVOT) heterogeneous-accelerator optimization.

**Software / models**: NVIDIA Isaac, [Isaac GR00T](../entities/nvidia-groot.md), Nemotron open models, [Cosmos 3](../entities/nvidia-cosmos.md) Edge, **NemoClaw** blueprints for agentic orchestration; **JetPack 7.2.1+**.

**Availability**: T3000 emulation later July 2026 (JetPack 7.2.1); T2000 emulation in a future release; **GA Q1 2027**.

**Named robotics adopters**: 1X, Agile Robots, Amazon Robotics, [Boston Dynamics](../entities/boston-dynamics.md), FANUC, Hitachi, Techman Robot, UBTech (+ ecosystem partners ADLINK, Advantech, AAEON, Aetina, Auvidea, AVerMedia, [Seeed Studio](../entities/seeed-studio.md), Antmicro, RidgeRun, et al.).

## Entities mentioned

- [Jetson Thor](../entities/jetson-thor.md) — the product family being expanded.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — Cosmos 3 Edge (4B) delivered to Thor.
- [NVIDIA GR00T](../entities/nvidia-groot.md), [NVIDIA](../entities/nvidia.md), [Boston Dynamics](../entities/boston-dynamics.md), [Seeed Studio](../entities/seeed-studio.md).

## Concepts touched

- Edge physical-AI / agentic AI on-robot; [VLA](../concepts/learning/vla-models.md) inference at the edge.
- **Functional safety** — IGX T3000 + NVIDIA Halos for Robotics; connects to [robot safety standards](../concepts/robotics/robot-safety-standards.md) and the deterministic-safety-vs-learned-policy tension.

## Open questions

- **Pricing** for all three new SKUs — undisclosed.
- **Memory-tier consequence**: T3000 (32 GB) / T2000 (16 GB) are *not* the 128 GB of T5000 — how much do the 128 GB-dependent workflows (the wiki's [train-on-Spark/deploy-on-Thor](../syntheses/platforms/jetson-thor-vs-dgx-spark.md) "same 128 GB" claim) shrink on the smaller tiers? A 3B VLA (GR00T) needs headroom; 16 GB is the floor the wiki already flags for Orin NX.
- **Power** for T2000/T3000 not quantified here — but "~50% lower power than T5000" plus an entry tier is exactly what the [XLeRobot power-budget](../syntheses/projects/xlerobot-thor-power-budget.md) problem needed (Thor's 40–130 W was judged to *exceed* a 288 Wh mobile-robot budget in [Cutting the Cord](cutting-the-cord-untethered-xlerobot.md)).
- ~~**NVIDIA Halos for Robotics** — first mention in the wiki; worth its own source~~ — **ingested 2026-07-15**: [NVIDIA Halos for Robotics](nvidia-halos-robotics.md) + [NVIDIA Halos entity](../entities/nvidia-halos.md).
