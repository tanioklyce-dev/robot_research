---
title: "Onboard compute for XLeRobot — Jetson Orin Nano vs Orin NX vs AGX Orin vs AGX Thor"
type: synthesis
created: 2026-06-03
updated: 2026-07-26
tags: [xlerobot, jetson, jetson-orin-nano, orin-nx, agx-orin, jetson-thor, onboard-compute, edge-ai, power-budget, vla, buying-decision, platforms]
---

# Onboard compute for XLeRobot — Jetson Orin Nano vs Orin NX vs AGX Orin vs AGX Thor

Which NVIDIA Jetson should ride on an untethered [XLeRobot](../../entities/xlerobot.md)? The platform is a ~$700–1,300 bimanual mobile manipulator (17 DoF, 17× [STS3215](../../entities/so-arm101.md) servos @ 12 V) powered by a **288 Wh / 300 W Anker C300** — so the compute decision is dominated by the **power and energy budget**, not raw TOPS. This page compares the four tiers the question usually comes down to — **Orin Nano → Orin NX 16 GB → AGX Orin → AGX Thor** — grounded in the first measured onboard build: [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md), which put a **Jetson Orin Nano** on an XLeRobot and benchmarked it.

> [!note] The power budget is the whole game
> On a 288 Wh pack, every onboard watt trades against runtime, and every compute watt also competes with ~240 W of motor draw for the C300's per-port current ceilings (the [Tri-Bus problem](../../sources/cutting-the-cord-untethered-xlerobot.md)). That reframes the comparison: it's **"how much capability fits in ~15–70 W,"** not "which is fastest." See [XLeRobot + Thor power budget](../projects/xlerobot-thor-power-budget.md).

## Spec comparison

| | **Orin Nano 8 GB** (Super) | **Orin NX 16 GB** (Super) | **AGX Orin 64 GB** | **AGX Thor (T5000)** |
|---|---|---|---|---|
| Arch | Ampere | Ampere | Ampere | **Blackwell** |
| GPU | 1024 CUDA + 32 Tensor | 1024 CUDA + 32 Tensor **+ 2 DLA** | 2048 CUDA + 64 Tensor | 2560 CUDA + 5th-gen Tensor |
| AI perf | **67 INT8 TOPS** | **157 INT8 TOPS** (sparse; 100 standard) | **275 INT8 TOPS** (sparse) | **~2070 FP4 TFLOPS / ~1035 FP8 TOPS** (≈7.5× AGX Orin) |
| CPU | 6× A78AE | 8× A78AE | 12× A78AE | 14× Neoverse-V3AE |
| **Memory** | **8 GB** LPDDR5, 102 GB/s | **16 GB** LPDDR5, 102 GB/s | **64 GB** LPDDR5, 204.8 GB/s | **128 GB** LPDDR5X, 273 GB/s |
| **Power** | **7–25 W** | **10–40 W** | **15–60 W** | **40–130 W** (nvpmodel 70/90/120 W) |
| Price | **~$249** (dev kit) | **~$600** (module) | ~$1,999 (dev kit) | **$3,499** (dev kit) |
| Weight / cooling | tiny, passive duct OK ([paper](../../sources/cutting-the-cord-untethered-xlerobot.md)) | tiny — **drop-in on the Nano dev-kit carrier** | larger, active heatsink-fan | largest; no RT cores |
| SDK | JetPack 6 | JetPack 6 | JetPack 6 | **JetPack 7 / Isaac ROS 4 / GR00T target** |

*(TOPS across the Orin trio are INT8; Thor's headline is FP4/FP8 — not directly comparable, so the "≈7.5× AGX Orin" relative figure is the honest anchor. Cross-reference [Jetson Thor](../../entities/jetson-thor.md), [Jetson Orin Nano](../../entities/jetson-orin-nano.md), [Orin power modes](../../sources/nvidia-jetson-platform-power-performance-orin.md), [Thor power modes](../../sources/nvidia-jetson-thor-platform-power-performance.md).)*

> [!note] Orin NX 16 GB shares the Nano's GPU core count and carrier
> The Orin NX 16 GB has the **same 1024-CUDA / 32-Tensor GPU as the Orin Nano** — its **2.3× TOPS (157 vs 67)** comes from higher clocks, a bigger power envelope (10–40 W), **2 DLA accelerators**, and 8 (vs 6) CPU cores. Crucially it's **pin-compatible with the Orin Nano Super Dev Kit carrier (P3768)**, so it's a literal drop-in upgrade for a Nano-based build like [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) — same enclosure, same wiring, +8 GB RAM. No standalone dev kit; budget ~$600 for the module on the existing carrier. Off-the-shelf, the robot-appropriate Orin NX 16 GB box is **Seeed's reComputer Robotics J4012** — the battery-powered Robotics-J40 carrier (19–54 V input, CAN + GMSL, 157 TOPS at 60 °C/40 W; [Seeed Jetson guide](../../sources/seeed-jetson-selection-guide.md)) — if you'd rather buy a robot-ready carrier than reuse the Nano dev kit's.

## The decisive axis — watts vs the 288 Wh budget

| | Orin Nano | Orin NX 16 GB | AGX Orin | AGX Thor |
|---|---|---|---|---|
| Draw | **7–25 W** | **10–40 W** | 15–60 W | 40–130 W (cap 70 W) |
| Fraction of a ~150 W robot draw | ~10–15 % | ~7–25 % | ~10–30 % | **~30–60 %** |
| Fits the C300 budget? | ✅ huge margin ([paper](../../sources/cutting-the-cord-untethered-xlerobot.md): **5 % battery / 30 min**, no throttle) | ✅ comfortable (≤40 W) | ✅ feasible, eats more runtime | ⚠️ **"exceeds the power budget"** ([paper](../../sources/cutting-the-cord-untethered-xlerobot.md)) — only viable software-capped to 70 W + a bigger pack |
| C300 wiring | one USB-C rail, isolated | one USB-C rail (≤40 W, easy) | one USB-C rail (≤60 W fits 140 W port) | needs the full 140 W USB-C / Micro-Fit; competes with motors |

The paper is explicit: the Orin Nano slots into the Tri-Bus with **~60 W of headroom to spare**, and Thor (40–130 W) **exceeds the budget** for a single-C300 build. The [Thor power-modes ingest](../../sources/nvidia-jetson-thor-platform-power-performance.md) shows you *can* software-cap Thor to **70 W (Mode 3)** — but even capped it's ~3× the Orin Nano and dominates the energy budget, which is why it belongs on a larger battery or a tethered/tiered setup.

## The capability axis — what each can actually run

The [paper's on-edge benchmark](../../sources/cutting-the-cord-untethered-xlerobot.md) (Orin Nano, FP16, end-to-end camera→action) is the reality check:

| Model | Orin Nano latency | Orin Nano max replan |
|---|---|---|
| **ACT** | 36 ms | **27.8 Hz** ✅ reactive control |
| **Diffusion Policy** | 540 ms | **1.8 Hz** ⚠️ slow |
| **SmolVLA (450 M)** | 714 ms | **1.4 Hz** ⚠️ slow |

- **Orin Nano** runs **ACT-class transformer policies at real-time (~28 Hz)** and classical perception/SLAM comfortably — but modern **diffusion/flow-matching policies crawl at ~1–2 Hz**, fine for slow/scripted tasks, too slow for reactive closed-loop. Its **8 GB** also caps model size (SmolVLA-450 M fits; 3 B-class VLAs are a squeeze). The paper's nuance: the bottleneck is the **iterative action expert + denoising steps**, not the VLM — so more compute (not just more memory) is what unlocks fast VLAs.
- **Orin NX 16 GB** — the **drop-in upgrade from the Nano**: same carrier/wiring, **2× RAM (16 GB)** and **~2.3× TOPS (157)** for **+~15 W and ~$600**. The extra compute should pull diffusion/SmolVLA off the ~1–2 Hz floor (the paper's bottleneck is exactly the compute-bound action expert), and 16 GB comfortably fits SmolVLA + perception/SLAM concurrently (3 B-class VLAs become workable, if tight). Stays firmly inside the Nano's power/size class — the **least-disruptive way to make onboard VLAs usable**.
- **AGX Orin** — **~4× the Nano's TOPS and 64 GB** lifts diffusion/SmolVLA-class policies further and lets **3 B-class VLAs ([π0](../../entities/pi-zero.md), [GR00T](../../entities/nvidia-groot.md))** fit with headroom. The max "run a VLA on battery" tier — but at 15–60 W, ~$2k, more weight/cooling, and a new carrier. For the XLeRobot it's often *more* than needed versus the Orin NX.
- **AGX Thor** — **128 GB Blackwell** is built to run **3 B+ VLAs fast and several concurrently** (it's NVIDIA's GR00T deploy target, JetPack 7 / Isaac ROS 4). That capability is real but it's a **humanoid / heavier-robot power class**, overkill for a $1.2k tabletop bimanual bot on a 288 Wh pack.

## Verdict

| Pick | When |
|---|---|
| **Jetson Orin Nano 8 GB (~$249, 7–25 W)** | **The validated default.** Cheapest, lightest, fits the power budget with huge margin; runs ACT at ~28 Hz + SLAM/IK/teleop onboard. Accept ~1–2 Hz on diffusion/SmolVLA and the 8 GB model-size cap. This is what [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) shipped, and it works untethered. |
| **Jetson Orin NX 16 GB (~$600, 10–40 W)** | **The drop-in VLA upgrade — likely the XLeRobot sweet spot.** Same carrier/enclosure/wiring as the Nano but 2× RAM and ~2.3× TOPS, still 10–40 W. The best battery-friendly step up for running diffusion/SmolVLA-class VLAs onboard without leaving the Nano's power/size class. Pick this when the Nano's 8 GB / ~1–2 Hz is the wall but AGX Orin is overkill. |
| **Jetson AGX Orin 64 GB (~$2k, 15–60 W)** | **Max VLA-on-battery.** When you need 64 GB / peak throughput for 3 B-class VLAs with headroom and can spend the watts, dollars, weight, and a new carrier. Still feasible on the C300 (shorter runtime) — but for this robot the Orin NX usually gets you there for less. |
| **Jetson AGX Thor (T5000, $3,499, 40–130 W)** | **Over-budget for stock XLeRobot.** The paper's own conclusion. Only with software-capping (70 W) **and** a bigger battery / tiered power / tether. Justified only if you're running large or multiple VLAs (GR00T/π0-class) and have moved to a humanoid-scale power system — see [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md). |

**Bottom line:** for the XLeRobot as-specced, **Orin Nano is the right default and the only one proven untethered**; **Orin NX 16 GB is the natural drop-in upgrade** when onboard VLAs need more than 8 GB / ~1–2 Hz (and usually the better buy than AGX Orin here); **AGX Orin** is for when you want 64 GB and peak throughput; **Thor is the wrong tool** until the robot (and its battery) grow up.

> [!note] The NPU alternative (not on this Jetson ladder)
> A [Raspberry Pi 5](../../entities/raspberry-pi-5.md) + **[AI HAT+ 2 / Hailo-10H](../../sources/raspberry-pi-ai-hat-plus-2.md)** (40 TOPS INT4, 8 GB, $180) is a *non-CUDA* onboard option. It can host a local **LLM/VLM agent layer + vision** but is **not** a substitute for any tier here when it comes to the control policy: a [Hailo](../../entities/hailo.md) NPU runs only models compiled to its HEF format, so it does **not** run LeRobot's PyTorch ACT/Diffusion/SmolVLA/π0.5 as-is. Use it alongside (Pi-as-host + onboard LLM), not instead of, the Jetson for policy inference.

## Related
- [Jetson module ladder — performance and power](jetson-module-ladder-power-performance.md) — the hardware-neutral superset of this page's spec table: all 8 shipping SKUs (incl. Orin Nano 4 GB, Orin NX 8 GB, AGX Orin 32 GB, Thor T4000), both nvpmodel chapters merged, and a TOPS/W column. Notably it finds **AGX Orin 32 GB is *less* efficient than Orin NX 16 GB** (3.3 vs 3.9 TOPS/W) — a second axis supporting this page's "Orin NX usually beats AGX Orin here" verdict.
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — the measured onboard-Orin-Nano XLeRobot build this page is built on.
- [Raspberry Pi AI HAT+ 2 (Hailo-10H)](../../sources/raspberry-pi-ai-hat-plus-2.md) / [Hailo](../../entities/hailo.md) — the NPU alternative to this CUDA ladder.
- [XLeRobot + AGX Thor power budget](../projects/xlerobot-thor-power-budget.md) — the battery/runtime/two-rail analysis.
- [Anker C300 DC vs C300 vs C1000](anker-portable-power-stations.md) — the power-source side of the same decision.
- [Jetson Thor Platform Power & Performance (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md) — Thor's nvpmodel caps (why 70 W is reachable).
- [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md) — the train-vs-deploy split for the Thor tier.
- [GR00T inference on Jetson](gr00t-inference-on-jetson.md) — measured GR00T-3B rates across these same tiers (Thor 10.9–24 Hz, AGX Orin 5.8 Hz, Orin NX unbenchmarked and below the 16 GB memory floor) — the model-side check on this page's "3 B-class VLAs become workable" claims.
- [VLA models](../../concepts/learning/vla-models.md) — the policies whose edge latency drives this decision.
- [Seeed Jetson selection guide](../../sources/seeed-jetson-selection-guide.md) — corroborates the four-tier spec ladder; maps modules to buyable reComputer carriers (J30xx → Orin Nano, J40xx → Orin NX, J4012 → Orin NX 16 GB).
- [Seeed — choosing a Jetson carrier board](../../sources/seeed-jetson-carrier-board-selection.md) — the carrier-board-level decision (module tier → form → priorities); the **Robotics J401** carrier is the robot-oriented match for the Orin NX pick here.
