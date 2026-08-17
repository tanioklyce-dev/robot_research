---
title: "Onboard compute for XLeRobot — Jetson Orin Nano vs Orin NX vs AGX Orin vs AGX Thor"
type: synthesis
created: 2026-06-03
updated: 2026-08-17
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
| SDK | **JetPack 7.2+** (since 2026-06-01) | **JetPack 7.2+** | **JetPack 7.2+** | **JetPack 7.1 + Isaac ROS 4.x** (shipping) / GR00T target |

> [!warning] Correction 2026-08-16 — the Orin tiers are no longer JetPack 6
> This row read **"JetPack 6"** for all three Orin modules until today, which was already two months stale when the page was last touched. **JetPack 7.2 (Jetson Linux r39.2), released 2026-06-01, extends JetPack 7 to the whole Orin family** — AGX Orin, Orin NX and Orin Nano — on **Ubuntu 24.04 / kernel 6.8 / CUDA 13.2.1 / TensorRT 10.16.2**, unifying the toolchain with Thor. **JetPack 7.2.1** followed on **2026-08-12** (live-web). **Primary source now ingested: [JetPack 7.2 with Jetson Linux 39.2](../../sources/nvidia-jetpack-7-2-release.md).**
>
> Two consequences that bite a build rather than a spec sheet:
>
> - **The Orin Nano dev kit no longer ships an SD-card image.** From JetPack 7.2 the flow is a **unified ISO written to a USB stick**, which then installs Jetson Linux to microSD or NVMe — *"do not flash the Jetson ISO to a microSD card."* ~~The ISO defaults to **Super Mode** flashing config.~~ **Corrected 2026-08-17 — the opposite is true; see below.** Any bring-up notes written against the JetPack 6 SD-card flow are wrong.
> - **Third-party carriers lag NVIDIA by weeks, and one change is a camera trap.** Seeed shipped **JetPack 7.2.0 / R39.2.0 for the reComputer J401 and J501 on 2026-06-30** *(vendor primary now says the J401 Orin NX 16 GB image is dated **2026-06-18** — [Seeed flash guide](../../sources/seeed-j401-flash-jetpack.md))* (this page recommends the J401/J4012 for the Orin NX tier). **R39.2.0 moves to a 22-pin Jetson CSI connector spec where R36.4.3 used 24-pin, so camera device trees need updating** — the most likely thing to break silently on an upgrade. AGX Orin 32 GB carrier support was still being asked about in that thread.
>
> - **Isaac ROS is listed "Coming soon" on JetPack 7.2, and Jetson Platform Services as N/A** ([primary](../../sources/nvidia-jetpack-7-2-release.md)). For a ROS robot that is the decisive line: **upgrading an Orin to 7.2 today means giving up Isaac ROS.** ~~The Thor column below reads "JetPack 7 / Isaac ROS 4" — treat that as a roadmap pairing, not a shipping one.~~ **Corrected 2026-08-17: Isaac ROS 4 ships for Thor and has since 2025-10-24. It is Orin that is gone.** See below.
> - **There is a PCIe boot bug on Orin Nano and Orin NX** with an overlay fix (`overlay_pcie.tbz2`): *"an intermittent boot issue caused by initialization failures… during power cycles or reboots."* On a battery robot that power-cycles daily, apply it.
> - **AGX Orin 32 GB gains Super Mode (MAXN_SUPER): 200 → 241 TOPS** in 7.2 — see the [module ladder](jetson-module-ladder-power-performance.md).
>
> **This does not change any recommendation on this page** — the tiering, power budget and model-rate arguments are unaffected. It changes the software baseline you start from, and it means the Orin/Thor split is now a *hardware-generation* split rather than a toolchain split.

> [!warning] Correction 2026-08-17 — version sweep over the whole Jetson cluster, from primaries
> Three claims in the block above were wrong or under-stated. All three were secondary-sourced; all three were fixed by reading the vendor's own release notes.
>
> **1. Isaac ROS 4 is shipping for Thor, and it is *Orin* that has no path.** Isaac ROS **4.5.0** is current (2026-07-06); **4.0** added Thor + JetPack 7.0 on **2025-10-24** and **4.2** added JetPack 7.1 on 2026-02-19 ([release notes and platforms](../../sources/isaac-ros-release-notes-and-platforms.md)). The supported-platform table — "the only hardware and software combinations that Isaac ROS tests and officially supports" — lists **Thor T5000/T4000 on JetPack 7.1**, x86_64, and DGX Spark. **No Orin appears at all.** The last Orin-supporting line is **3.2 (Dec 2024 / Jan 2025) on JetPack 6.1–6.2, Ubuntu 22.04, CUDA 12.6, ROS 2 Humble**. So the Orin tiers on this page face a closed door either way: stay on JetPack 6.2 and keep a frozen Isaac ROS 3.2, or move to 7.2 and have none. 4.x is also a **ROS 2 Jazzy** line — a distro migration, not an upgrade.
>
> **2. The unified ISO does *not* default to Super Mode — it preserves whatever profile was already set.** [r39.2 release notes](../../sources/nvidia-jetson-linux-r39-2-release-notes.md) issue **6279443**: "Jetson Orin Nano units that are updated to JetPack 7.2 using ISO install continue to use the same profile that was set before update. **Units will not default to 'Super' mode after the update.** To use 'Super' mode, you must flash the target using a Linux host or SDKM." The earlier claim came from secondary coverage. Also issue **6266271**: the ISO install prompts for a **QSPI capsule update and you must answer `y`** — skipping it fails the install.
>
> **3. The low end of the Orin NX power envelope has an open crash bug.** Issue **6236259**: on Orin platforms, dropping EMC below Fmax via `nvpmodel.service` during systemd init "can cause system crashes upon reboot," affecting **Orin NX 16/8 GB at 10 W**, **Orin Nano 8 GB at 7 W**, AGX Orin at 15 W — "especially noticeable when a display is connected." **This page recommends the Orin NX partly for its 10–40 W envelope, and 10 W is precisely the affected mode.** Workaround is to return to MAXN before reboot and reapply the mode after. Whether a headless robot is exempt is not stated in the release notes.
>
> **And a carrier-level ceiling that is new to this page:** Seeed's own flash guide says **"if you are using an Orin NX 16GB/8GB module, do not enable MAXN SUPER mode. The cooling capacity of the reComputer J401 carrier board is insufficient to support it"** ([Seeed flash guide](../../sources/seeed-j401-flash-jetpack.md)). Seeed separately markets the **reComputer Super J4012 at 157 TOPS in Super MAXN**. Same module, two sanctioned ceilings — the difference is the carrier's cooling. **The 157 TOPS figure in the table above is a Super-Mode number, so it is contingent on which Seeed box you buy.** The Robotics J30/40 (this wiki's battery-powered pick, quoted at 157 TOPS / 40 W) is not covered by that page and needs its own primary before the figure is relied on.
>
> **Net effect on the recommendation:** the Orin NX is still the sweet spot on power, price and carrier availability, but the ROS-perception story behind it is weaker than this page implied — Isaac ROS is not available to it on a current line, and its headline TOPS depends on a carrier that can cool Super Mode.

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

> [!warning] Added 2026-08-03 — the "3B-class VLAs become workable" verdict does not extend to MolmoAct2
> [MolmoAct2-SO100_101](../../sources/molmoact2-so100-101-model-card.md) is the first 2026-class open VLA with a checkpoint fine-tuned for this exact arm class — and it is **5B params at ~16 GB bf16** (~24–26 GB float32). Because Jetson memory is **unified and shared with the CPU**, a 16 GB Orin NX has well under 16 GB free once the OS, camera pipeline, and ROS stack are resident. **This checkpoint is not an Orin NX 16 GB target.**
>
> That splits the Orin NX recommendation by model generation: it remains the right call for **SmolVLA / diffusion-policy-class** models (the ones this page benchmarked), and it is **not sufficient** for the 5B 2026-class checkpoints. For MolmoAct2 specifically the plausible onboard tiers are **AGX Orin 64 GB** or **Thor** — or the [repo's own architecture](../../sources/molmoact2-github-repo.md), which expects the model to run **off-robot behind a FastAPI server** with the robot as a client. Given the XLeRobot's power budget, off-board serving is likely the realistic path, and it is what Ai2 ships.
>
> Caveat: this is **inference from a stated memory footprint, not a measurement**. No one has published MolmoAct2 on any Jetson, and the repo contains no Jetson support.

> [!note] The NPU alternative (not on this Jetson ladder)
> A [Raspberry Pi 5](../../entities/raspberry-pi-5.md) + **[AI HAT+ 2 / Hailo-10H](../../sources/raspberry-pi-ai-hat-plus-2.md)** (40 TOPS INT4, 8 GB, $180) is a *non-CUDA* onboard option. It can host a local **LLM/VLM agent layer + vision** but is **not** a substitute for any tier here when it comes to the control policy: a [Hailo](../../entities/hailo.md) NPU runs only models compiled to its HEF format, so it does **not** run LeRobot's PyTorch ACT/Diffusion/SmolVLA/π0.5 as-is. Use it alongside (Pi-as-host + onboard LLM), not instead of, the Jetson for policy inference.

## Related
- [Control-rate ladder](control-rate-ladder.md) — the 27.8 / 1.8 / 1.4 Hz measurements from this page's source, placed against control-rate *requirements* and LLM inference speed.
- [Jetson module ladder — performance and power](jetson-module-ladder-power-performance.md) — the hardware-neutral superset of this page's spec table: all 8 shipping SKUs (incl. Orin Nano 4 GB, Orin NX 8 GB, AGX Orin 32 GB, Thor T4000), both nvpmodel chapters merged, and a TOPS/W column. Notably it finds **AGX Orin 32 GB is *less* efficient than Orin NX 16 GB** (3.3 vs 3.9 TOPS/W) — a second axis supporting this page's "Orin NX usually beats AGX Orin here" verdict.
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — the measured onboard-Orin-Nano XLeRobot build this page is built on.
- [Raspberry Pi AI HAT+ 2 (Hailo-10H)](../../sources/raspberry-pi-ai-hat-plus-2.md) / [Hailo](../../entities/hailo.md) — the NPU alternative to this CUDA ladder.
- [XLeRobot + AGX Thor power budget](../projects/xlerobot-thor-power-budget.md) — the battery/runtime/two-rail analysis.
- [Anker C300 DC vs C300 vs C1000](anker-portable-power-stations.md) — the power-source side of the same decision.
- [Jetson Thor Platform Power & Performance (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md) — Thor's nvpmodel caps (why 70 W is reachable).
- [Jetson Thor vs DGX Spark](jetson-thor-vs-dgx-spark.md) — the train-vs-deploy split for the Thor tier.
- [GR00T inference on Jetson](gr00t-inference-on-jetson.md) — measured GR00T-3B rates across these same tiers (Thor 10.9–24 Hz, AGX Orin 5.8 Hz, Orin NX unbenchmarked and below the 16 GB memory floor) — the model-side check on this page's "3 B-class VLAs become workable" claims.
- [VLA models](../../concepts/learning/vla-models.md) — the policies whose edge latency drives this decision.
- [JetPack 7.2 / Jetson Linux 39.2 release page](../../sources/nvidia-jetpack-7-2-release.md) — the primary source behind the SDK row, the Isaac ROS gap, and the Orin Nano flashing change.
- [Seeed Jetson selection guide](../../sources/seeed-jetson-selection-guide.md) — corroborates the four-tier spec ladder; maps modules to buyable reComputer carriers (J30xx → Orin Nano, J40xx → Orin NX, J4012 → Orin NX 16 GB).
- [Seeed — choosing a Jetson carrier board](../../sources/seeed-jetson-carrier-board-selection.md) — the carrier-board-level decision (module tier → form → priorities); the **Robotics J401** carrier is the robot-oriented match for the Orin NX pick here.
