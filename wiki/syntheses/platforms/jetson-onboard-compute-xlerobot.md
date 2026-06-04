---
title: "Onboard compute for XLeRobot — Jetson Orin Nano vs AGX Orin vs AGX Thor"
type: synthesis
created: 2026-06-03
updated: 2026-06-03
tags: [xlerobot, jetson, jetson-orin-nano, agx-orin, jetson-thor, onboard-compute, edge-ai, power-budget, vla, buying-decision, platforms]
---

# Onboard compute for XLeRobot — Jetson Orin Nano vs AGX Orin vs AGX Thor

Which NVIDIA Jetson should ride on an untethered [XLeRobot](../../entities/xlerobot.md)? The platform is a ~$700–1,300 bimanual mobile manipulator (17 DoF, 17× [STS3215](../../entities/so-arm101.md) servos @ 12 V) powered by a **288 Wh / 300 W Anker C300** — so the compute decision is dominated by the **power and energy budget**, not raw TOPS. This page compares the three tiers the question usually comes down to, grounded in the first measured onboard build: [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md), which put a **Jetson Orin Nano** on an XLeRobot and benchmarked it.

> [!note] The power budget is the whole game
> On a 288 Wh pack, every onboard watt trades against runtime, and every compute watt also competes with ~240 W of motor draw for the C300's per-port current ceilings (the [Tri-Bus problem](../../sources/cutting-the-cord-untethered-xlerobot.md)). That reframes the comparison: it's **"how much capability fits in ~15–70 W,"** not "which is fastest." See [XLeRobot + Thor power budget](../projects/xlerobot-thor-power-budget.md).

## Spec comparison

| | **Jetson Orin Nano 8 GB** (Super) | **Jetson AGX Orin 64 GB** | **Jetson AGX Thor (T5000)** |
|---|---|---|---|
| Arch | Ampere | Ampere | **Blackwell** |
| GPU | 1024 CUDA + 32 Tensor | 2048 CUDA + 64 Tensor | 2560 CUDA + 5th-gen Tensor |
| AI perf | **67 INT8 TOPS** | **275 INT8 TOPS** (sparse) | **~2070 FP4 TFLOPS / ~1035 FP8 TOPS** (≈7.5× AGX Orin) |
| CPU | 6× A78AE | 12× A78AE | 14× Neoverse-V3AE |
| **Memory** | **8 GB** LPDDR5, 102 GB/s | **64 GB** LPDDR5, 204.8 GB/s | **128 GB** LPDDR5X, 273 GB/s |
| **Power** | **7–25 W** | **15–60 W** | **40–130 W** (nvpmodel 70/90/120 W) |
| Dev-kit price | **~$249** | ~$1,999 | **$3,499** |
| Weight / cooling | tiny, passive duct OK ([paper](../../sources/cutting-the-cord-untethered-xlerobot.md)) | larger, active heatsink-fan | largest; no RT cores |
| SDK | JetPack 6 | JetPack 6 | **JetPack 7 / Isaac ROS 4 / GR00T target** |

*(TOPS across the Orin pair are INT8; Thor's headline is FP4/FP8 — not directly comparable, so the "≈7.5× AGX Orin" relative figure is the honest anchor. Cross-reference [Jetson Thor](../../entities/jetson-thor.md), [Jetson Orin Nano](../../entities/jetson-orin-nano.md), [Orin power modes](../../sources/nvidia-jetson-platform-power-performance-orin.md), [Thor power modes](../../sources/nvidia-jetson-thor-platform-power-performance.md).)*

> [!note] Orin NX is the unlisted midpoint
> Between Orin Nano and AGX Orin sits the **Orin NX 16 GB** (~100 TOPS, 10–25 W, 16 GB) — a drop-in on the same dev-kit carrier as the Nano. If 8 GB is the only thing stopping you but 60 W is too much, it's the natural in-between. Omitted from the main table to keep the three tiers the question actually poses.

## The decisive axis — watts vs the 288 Wh budget

| | Orin Nano | AGX Orin | AGX Thor |
|---|---|---|---|
| Draw | **7–25 W** | 15–60 W | 40–130 W (cap 70 W) |
| Fraction of a ~150 W robot draw | ~10–15 % | ~10–30 % | **~30–60 %** |
| Fits the C300 budget? | ✅ huge margin ([paper](../../sources/cutting-the-cord-untethered-xlerobot.md): **5 % battery / 30 min**, no throttle) | ✅ feasible, eats more runtime | ⚠️ **"exceeds the power budget"** ([paper](../../sources/cutting-the-cord-untethered-xlerobot.md)) — only viable software-capped to 70 W + a bigger pack |
| C300 wiring | one USB-C rail, isolated | one USB-C rail (≤60 W fits 140 W port) | needs the full 140 W USB-C / Micro-Fit; competes with motors |

The paper is explicit: the Orin Nano slots into the Tri-Bus with **~60 W of headroom to spare**, and Thor (40–130 W) **exceeds the budget** for a single-C300 build. The [Thor power-modes ingest](../../sources/nvidia-jetson-thor-platform-power-performance.md) shows you *can* software-cap Thor to **70 W (Mode 3)** — but even capped it's ~3× the Orin Nano and dominates the energy budget, which is why it belongs on a larger battery or a tethered/tiered setup.

## The capability axis — what each can actually run

The [paper's on-edge benchmark](../../sources/cutting-the-cord-untethered-xlerobot.md) (Orin Nano, FP16, end-to-end camera→action) is the reality check:

| Model | Orin Nano latency | Orin Nano max replan |
|---|---|---|
| **ACT** | 36 ms | **27.8 Hz** ✅ reactive control |
| **Diffusion Policy** | 540 ms | **1.8 Hz** ⚠️ slow |
| **SmolVLA (450 M)** | 714 ms | **1.4 Hz** ⚠️ slow |

- **Orin Nano** runs **ACT-class transformer policies at real-time (~28 Hz)** and classical perception/SLAM comfortably — but modern **diffusion/flow-matching policies crawl at ~1–2 Hz**, fine for slow/scripted tasks, too slow for reactive closed-loop. Its **8 GB** also caps model size (SmolVLA-450 M fits; 3 B-class VLAs are a squeeze). The paper's nuance: the bottleneck is the **iterative action expert + denoising steps**, not the VLM — so more compute (not just more memory) is what unlocks fast VLAs.
- **AGX Orin** — **~4× the TOPS and 64 GB** lifts diffusion/SmolVLA-class policies from ~1–2 Hz toward usable rates and lets **3 B-class VLAs ([π0](../../entities/pi-zero.md), [GR00T](../../entities/nvidia-groot.md))** fit in memory. The real "run a VLA on battery" tier — at 15–60 W, ~$2k, and more weight/cooling.
- **AGX Thor** — **128 GB Blackwell** is built to run **3 B+ VLAs fast and several concurrently** (it's NVIDIA's GR00T deploy target, JetPack 7 / Isaac ROS 4). That capability is real but it's a **humanoid / heavier-robot power class**, overkill for a $1.2k tabletop bimanual bot on a 288 Wh pack.

## Verdict

| Pick | When |
|---|---|
| **Jetson Orin Nano 8 GB (~$249, 7–25 W)** | **The validated default.** Cheapest, lightest, fits the power budget with huge margin; runs ACT at ~28 Hz + SLAM/IK/teleop onboard. Accept ~1–2 Hz on diffusion/SmolVLA and the 8 GB model-size cap. This is what [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) shipped, and it works untethered. |
| **Jetson AGX Orin 64 GB (~$2k, 15–60 W)** | **The VLA-on-battery upgrade.** When the goal is running diffusion/flow-matching or 3 B-class VLAs onboard at usable rates and you can spend the watts, dollars, and weight. Still feasible on the C300 (shorter runtime). The sweet spot if onboard VLA inference is the point. |
| **Jetson AGX Thor (T5000, $3,499, 40–130 W)** | **Over-budget for stock XLeRobot.** The paper's own conclusion. Only with software-capping (70 W) **and** a bigger battery / tiered power / tether. Justified only if you're running large or multiple VLAs (GR00T/π0-class) and have moved to a humanoid-scale power system — see [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md). |

**Bottom line:** for the XLeRobot as-specced, **Orin Nano is the right default and the only one proven untethered**; **AGX Orin is the considered upgrade** if onboard VLA inference is the goal; **Thor is the wrong tool** until the robot (and its battery) grow up.

## Related
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — the measured onboard-Orin-Nano XLeRobot build this page is built on.
- [XLeRobot + AGX Thor power budget](../projects/xlerobot-thor-power-budget.md) — the battery/runtime/two-rail analysis.
- [Anker C300 DC vs C300 vs C1000](anker-portable-power-stations.md) — the power-source side of the same decision.
- [Jetson Thor Platform Power & Performance (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md) — Thor's nvpmodel caps (why 70 W is reachable).
- [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md) — the train-vs-deploy split for the Thor tier.
- [VLA models](../../concepts/learning/vla-models.md) — the policies whose edge latency drives this decision.
