---
title: NVIDIA Jetson Orin NX
type: entity
subtype: hardware
created: 2026-08-28
updated: 2026-08-29
sources: 8
tags: [jetson, jetson-orin-nx, nvidia, edge-ai, onboard-compute, ampere, dla, super-mode, nvpmodel, robotics, xlerobot]
---

**Product page:** [developer.nvidia.com/embedded/jetson-orin-nx](https://developer.nvidia.com/embedded/jetson-orin-nx) · **Form factor:** 69.6 × 45 mm, **260-pin SO-DIMM**

**NVIDIA Jetson Orin NX** — the middle rung of the Ampere-generation Jetson ladder, between the [Orin Nano](jetson-orin-nano.md) and AGX Orin. Two SKUs (**16 GB** and **8 GB**), both on a 1024-core Ampere GPU with 32 tensor cores. **This wiki's default recommendation for a battery-powered robot that needs to run a VLA onboard** — not because it is the fastest, but because it is **pin-compatible with the Orin Nano carrier**, stays inside a 10–40 W envelope, and costs ~$600 for the module ([XLeRobot onboard compute](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)).

This page exists because "Orin NX" appeared on 37 wiki pages with its specs scattered across syntheses and no canonical home.

## Specifications

From NVIDIA's own module comparison table (retrieved 2026-08-28; re-parsed 2026-08-29), Super-Mode figures:

| | **Orin NX 16 GB** | **Orin NX 8 GB** |
|---|---|---|
| AI performance (headline) | **157 TOPS** | **117 TOPS** |
| GPU | 1024-core Ampere, 32 tensor cores | *same* |
| GPU max clock | 1173 MHz | 1173 MHz |
| CPU | **8-core** Arm Cortex-A78AE v8.2, 2 MB L2 + 4 MB L3 | **6-core** A78AE, 1.5 MB L2 + 4 MB L3 |
| CPU max clock | 2.0 GHz | 2.0 GHz |
| DLA (INT8) | **80 sparse / 40 dense TOPS** | **40 sparse / 20 dense TOPS** |
| GPU tensor core (INT8) | 77 sparse / **38 dense** TOPS | 77 sparse / **38 dense** TOPS |
| GPU tensor core (FP16) | 38 sparse / 19 dense TFLOPS | 38 sparse / 19 dense TFLOPS |
| GPU CUDA core | 2.4 FP32 / 4.8 FP16 TFLOPS | 2.4 FP32 / 4.8 FP16 TFLOPS |
| Memory | 16 GB 128-bit LPDDR5, **102.4 GB/s** | 8 GB 128-bit LPDDR5, 102.4 GB/s |
| Storage | none on module (external NVMe) | *same* |
| Camera | up to 4 cameras (8 virtual), 8-lane MIPI CSI-2 D-PHY 2.1 | *same* |
| PCIe | 1× x4 + 3× x1, Gen4 | *same* |
| Networking | 1× GbE | *same* |
| Power modes | **10 W / 15 W / 25 W / 40 W** | 10 / 15 / 25 / 40 W |
| Mechanical | 69.6 × 45 mm, 260-pin SO-DIMM | *same* |
| Price | **~$600** module ([XLeRobot compute](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)) | not recorded in this wiki |

> [!warning] Read the headline TOPS carefully — most of it is DLA, and all of it is sparse
> **157 = 77 (GPU tensor cores) + 80 (DLA)**, and both halves are **SPARSE INT8**. Two consequences for anyone sizing a robot-learning workload:
>
> - **More than half the headline comes from the two DLAs**, which are fixed-function inference accelerators. A stock PyTorch/TensorRT-on-GPU pipeline — which is what every VLA in this wiki actually runs — does not touch them unless the model is explicitly compiled for DLA, and DLA supports a restricted layer set. **The GPU-only figure is 77 sparse TOPS.**
> - **Sparse assumes 2:4 structured sparsity.** Without it the GPU tensor cores deliver **38 dense INT8 TOPS** — about **24% of the 157** on the box.
>
> So the honest range for "what will my VLA actually see" is **38–77 TOPS**, not 157. The same arithmetic applies to the 8 GB part (77 GPU + 40 DLA = 117). This does not change the module's ranking against its neighbours — they are quoted the same way — but it does mean the [TOPS/W figures in the module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) are **GPU+DLA+sparse throughout**, and should not be read as achievable on one workload.

> [!note] DLA count — resolved 2026-08-29
> **Orin NX 16 GB has 2× NVDLA v2; Orin NX 8 GB has 1×.** This was flagged as unresolved on 2026-08-28 because NVIDIA's table appeared to give "1× NVDLA v2" for the whole Orin NX series. That was a **parsing error on my side, not NVIDIA's**: the DL-accelerator row uses `colspan`, and the "2× NVDLA v2" cell spans five columns — through the Orin NX 16 GB — with the "1×" cell applying to the 8 GB alone. It matches the DLA INT8 split exactly (80 vs 40 TOPS). The wiki's [module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md) previously said "+2 DLA" for *both* SKUs, which was wrong for the 8 GB; corrected there.

Both SKUs also carry **1× PVA v2** (programmable vision accelerator) — absent entirely from the Orin Nano line.

## Super Mode is locked at flash time

The 157 / 117 TOPS figures are **Super Mode** numbers and are not available on a default flash ([NVIDIA Platform Power and Performance](../sources/nvidia-jetson-platform-power-performance-orin.md)):

- Super Mode (formerly `MAXN_SUPER`) is *"an experimental mode that allows a maximum number of cores and clock frequency for CPU, GPU, DLA, PVA, and SOC engines."*
- Access is **hardware-variant + flash-config dependent**: a module flashed with the standard `.conf` **physically cannot enter** the higher profiles. You must flash with the `-super` (or `-super-maxn`) variant.
- Standard-flash Orin NX 16 GB is recorded in this wiki at **100 TOPS vs 157 Super**.
- Runtime switching is `sudo nvpmodel -m <id>`, persistent across reboots.

**nvpmodel modes, Orin NX 16 GB** ([primary](../sources/nvidia-jetson-platform-power-performance-orin.md)):

| Flash | Name | Mode ID | Cores | CPU max | GPU max | DLA max | Mem max |
|---|---|---|---|---|---|---|---|
| Standard | MAXN | 0 | 8 | 1984 | 918 | 614.4 | 3200 |
| Standard | 10 W | 1 | 4 | 1190.4 | 612 | 153.6 | 2133 |
| Standard | 15 W | 2 | 4 | 1420.8 | 612 | 614.4 | 3200 |
| Standard | 25 W | 3 | 8 | 1497.6 | 408 | 614.4 | 3200 |
| Super | **MAXN_SUPER** | 0 | 8 | 1984 | **1173** | **1228.8** | 3200 |
| Super | 40 W | 4 | 8 | 1497.6 | 1173 | 908.8 | 3200 |

> [!note] Mode IDs are not portable across modules
> ID 1 means 7 W on an Orin Nano 8 GB, **10 W on an Orin NX**, 15 W on an AGX Orin, and 120 W on a Thor T5000. Always cross-reference per module.

## Three deployment traps

These are the things that bite in practice, all with primaries:

> [!warning] 1. Your carrier may not be able to cool Super Mode
> Seeed's own flash guide for the **J401** — the carrier under the reComputer J4012, this wiki's Orin NX recommendation — says: **"if you are using an Orin NX 16GB/8GB module, do not enable MAXN SUPER mode. The cooling capacity of the reComputer J401 carrier board is insufficient to support it"** ([Seeed flash guide](../sources/seeed-j401-flash-jetpack.md)). Seeed separately markets the **reComputer Super J4012 at 157 TOPS in Super MAXN**. Same silicon, two sanctioned ceilings; the variable is the carrier's cooling. **The headline TOPS is contingent on which box you buy.**

> [!warning] 2. The 10 W mode has an open crash bug
> [Jetson Linux r39.2 release notes](../sources/nvidia-jetson-linux-r39-2-release-notes.md), known issue **6236259**: reducing EMC below Fmax (~3200 MHz) via `nvpmodel.service` during systemd init *"can cause system crashes upon reboot,"* especially with a display connected. Affected modes include **Orin NX 8/16 GB at 10 W** — precisely the bottom of the envelope this module is chosen for. Workaround: switch to MAXN before rebooting, reapply after. Whether headless operation is exempt is **not stated**.

> [!warning] 3. Isaac ROS has no current line on Orin
> Isaac ROS **4.x** supports only Thor, x86_64 and DGX Spark; **no Orin appears in the supported-platform table at all** ([release notes and platforms](../sources/isaac-ros-release-notes-and-platforms.md)). The last Orin-supporting line is **3.2** (Dec 2024) on JetPack 6.1–6.2 / ROS 2 Humble. So an Orin NX faces a closed door either way: stay on JetPack 6.2 with a frozen Isaac ROS 3.2, or move to [JetPack 7.2](../sources/nvidia-jetpack-7-2-release.md) and have none. 4.x is also a **ROS 2 Jazzy** line — a distro migration, not an upgrade.

Also worth knowing: there is a **PCIe boot bug on Orin Nano and Orin NX** with an overlay fix (`overlay_pcie.tbz2`) — *"an intermittent boot issue caused by initialization failures… during power cycles or reboots."* On a battery robot that power-cycles daily, apply it. And **JetPack 7.2 / R39.2 moved to a 22-pin CSI connector spec** where R36.4.3 used 24-pin, so camera device trees need updating — the most likely thing to break silently on upgrade ([XLeRobot compute](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)).

## Where it sits in the ladder

- **vs [Orin Nano](jetson-orin-nano.md)**: **identical GPU** (1024 CUDA / 32 tensor). The 2.3× headline TOPS (157 vs 67) comes from higher clocks, a bigger power envelope, **the DLAs**, and 8 vs 6 CPU cores. Crucially **pin-compatible with the Orin Nano Super Dev Kit carrier (P3768)** — a literal drop-in: same enclosure, same wiring, +8 GB RAM ([XLeRobot compute](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)).
- **vs [AGX Orin](jetson-agx-orin.md) 32/64 GB**: the AGX buys **memory and IO** (256-bit LPDDR5 at 204.8 GB/s, 2× the bus width) at a 15–60 W envelope and ~$2k. For a battery robot that is usually more than needed.
- **vs [Thor](jetson-thor.md)**: a different power and price class entirely, and NVIDIA's [GR00T](nvidia-groot.md) deploy target.
- **Efficiency**: ~3.9 TOPS/W at 40 W, the sweet spot of the Ampere ladder at module level — though JetPack 7.2's AGX Orin 32 GB Super Mode (241 TOPS at 60 W ≈ 4.0) now edges past it ([module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md)). The reason to pick Orin NX for a battery robot was never efficiency alone; it is **envelope, carrier compatibility and price**.

> [!note] The practical break in the ladder is memory, not TOPS
> Orin NX 16 GB sits **exactly on [GR00T](nvidia-groot.md)-3B's stated 16 GB inference floor** — the module's entire shared RAM. The [GR00T-on-Jetson page](../syntheses/platforms/gr00t-inference-on-jetson.md) extrapolates ~2–3 Hz there and **recommends off-board serving instead**. That extrapolation is the wiki's inference, not a measurement. For SmolVLA/diffusion-class policies the 16 GB is comfortable and fits perception/SLAM concurrently.

## Carriers

| Board | Notes |
|---|---|
| **Orin Nano Super Dev Kit (P3768)** | Pin-compatible; the cheapest path if you already own one. |
| **Seeed reComputer J4012 / J401** | This wiki's default. **Cannot cool Super Mode** (see trap 1). |
| **Seeed reComputer Super J4012** | Marketed at 157 TOPS Super MAXN; 4× MIPI CSI. |
| **Seeed reComputer Robotics J4012 (J40)** | **The battery-robot carrier** — **XT30, 19–54 V input**, CAN + GMSL2, 157 TOPS at 40 W / 60 °C. No primary in the wiki yet; the 157 figure needs one before it is relied on. |
| **reServer Industrial J4012** | Fanless, 12–36 V, 5× Ethernet. |

Carrier details from the [Seeed Jetson selection guide](../sources/seeed-jetson-selection-guide.md) and [carrier-board guide](../sources/seeed-jetson-carrier-board-selection.md).

## Related

- [Jetson Orin Nano](jetson-orin-nano.md) — the tier below; same GPU, pin-compatible carrier.
- [Jetson AGX Orin](jetson-agx-orin.md) — the tier above; buys memory and IO, not efficiency.
- [Jetson Thor](jetson-thor.md) — the Blackwell generation above.
- [Jetson module ladder — power and performance](../syntheses/platforms/jetson-module-ladder-power-performance.md) — the full cross-module comparison.
- [Onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — where the buying recommendation is argued.
- [GR00T inference on Jetson](../syntheses/platforms/gr00t-inference-on-jetson.md) · [VLA deployability landscape](../syntheses/platforms/vla-deployability-landscape.md)
- [XLeRobot](xlerobot.md) — the fleet this module is specced for.

## Mentioned in

- [Jetson Linux Developer Guide — Platform Power and Performance (Orin)](../sources/nvidia-jetson-platform-power-performance-orin.md) — Super Mode, nvpmodel tables.
- [Seeed — flash JetPack OS to J401 carrier board](../sources/seeed-j401-flash-jetpack.md) — the Super-Mode cooling caveat.
- [Jetson Linux r39.2 release notes](../sources/nvidia-jetson-linux-r39-2-release-notes.md) — the 10 W crash bug.
- [JetPack 7.2 with Jetson Linux 39.2](../sources/nvidia-jetpack-7-2-release.md) — JetPack 7 extended to the Orin family.
- [Isaac ROS release notes and platforms](../sources/isaac-ros-release-notes-and-platforms.md) — no Orin on 4.x.
- [Seeed Jetson selection guide](../sources/seeed-jetson-selection-guide.md) · [Seeed carrier-board selection](../sources/seeed-jetson-carrier-board-selection.md) — the carrier matrix.
- [Cutting the Cord — untethered XLeRobot](../sources/cutting-the-cord-untethered-xlerobot.md) — the Orin Nano build this is the upgrade from.

## Open questions

- **Price of the Orin NX 8 GB** — not recorded anywhere in this wiki.
- **No like-for-like VLA benchmark across the Orin SKUs.** NVIDIA's GR00T table tests only AGX Orin and Thor; the Orin Nano figures come from a third-party paper on small policies. **Orin NX VLA latency is unmeasured** — every figure in this wiki for it is extrapolation.
- **Does DLA offload actually help a VLA?** If half the headline TOPS is DLA and no VLA stack uses it, the obvious question is whether a vision encoder could be compiled to DLA to free GPU for the action head. Nothing in this wiki tests it, and it is a cheap experiment on hardware this fleet owns.
- **Robotics J30/40 needs a primary** before its 157 TOPS / 40 W / 60 °C figure is relied on.
- **Is a headless robot exempt from the 10 W reboot crash?** The release notes do not say.
