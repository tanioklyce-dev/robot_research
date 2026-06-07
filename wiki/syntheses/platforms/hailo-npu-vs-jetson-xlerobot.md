---
title: "Hailo NPU (AI HAT+ 2) vs Jetson (CUDA) for an onboard XLeRobot brain"
type: synthesis
created: 2026-06-07
updated: 2026-06-07
tags: [xlerobot, hailo, jetson, npu, cuda, raspberry-pi, onboard-compute, edge-ai, vla, llm, buying-decision, platforms]
---

# Hailo NPU (AI HAT+ 2) vs Jetson (CUDA) for an onboard XLeRobot brain

When you want an [XLeRobot](../../entities/xlerobot.md) to think **onboard** (untethered, no cloud), there are two fundamentally different silicon bets:

1. **CUDA path** — a [Jetson](../../entities/jetson-orin-nano.md) carries a general-purpose GPU and runs the robot's [LeRobot](../../entities/lerobot.md) PyTorch policies *as written*. Covered in depth in [Jetson onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md).
2. **NPU path** — a [Raspberry Pi 5](../../entities/raspberry-pi-5.md) + [AI HAT+ 2 / Hailo-10H](../../sources/raspberry-pi-ai-hat-plus-2.md) carries a fixed-function neural accelerator that runs only models **compiled to Hailo's format**.

The trap is treating these as two points on one "more TOPS = better" line. They aren't. **TOPS are not comparable across a CUDA GPU and a fixed-function NPU**, and — more importantly — they run *different software*. This page is about picking the right one for the job, and the usual answer is **both, for different layers**.

## The one distinction that decides everything

> [!warning] An NPU runs *compiled models*, not your code
> A [Hailo](../../entities/hailo.md) NPU executes models you have **compiled to HEF** (Hailo Executable Format) ahead of time, on an x86 host, via Hailo's Dataflow Compiler. A Jetson runs **arbitrary CUDA/PyTorch** — you `pip install lerobot` and your ACT / Diffusion Policy / SmolVLA / π0.5 checkpoint runs unchanged ([XLeRobot](../../entities/xlerobot.md) policy list).

Everything below follows from that. The Jetson is a *brain you program*; the Hailo is a *coprocessor you feed pre-baked models*.

## Spec snapshot

| | **Pi 5 + AI HAT+ 2** | **Jetson Orin Nano 8 GB** | **Jetson Orin NX 16 GB** |
|---|---|---|---|
| Accelerator | [Hailo-10H](../../entities/hailo.md) NPU | Ampere CUDA GPU | Ampere CUDA GPU + 2 DLA |
| Headline perf | 40 TOPS **INT4** | 67 TOPS INT8 | 157 TOPS INT8 |
| Memory for AI | **8 GB dedicated** on HAT | 8 GB shared | 16 GB shared |
| Runs PyTorch policies as-is? | **No** (compile to HEF) | **Yes** (CUDA) | **Yes** (CUDA) |
| Runs local LLM/VLM? | **Yes** (`gen_ai_apps`, Hailo-10H) | Yes (small, 8 GB cap) | Yes (better) |
| Price (board) | **$180** | ~$249 | ~$600 |
| Host | needs a Pi 5 (~$80) | self-contained | self-contained |

*(Jetson figures from [Jetson onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md); Hailo figures from [AI HAT+ 2](../../sources/raspberry-pi-ai-hat-plus-2.md).)*

## What each can actually run on XLeRobot

XLeRobot has (at least) **three distinct compute jobs**. They land on different silicon:

| Job | Example workload | Hailo AI HAT+ 2 | Jetson Orin Nano/NX |
|---|---|---|---|
| **Control policy** | ACT, Diffusion Policy, SmolVLA, π0.5 | ❌ not supported (unproven to compile) | ✅ ACT ~28 Hz on Nano; diffusion/SmolVLA usable on NX ([data](jetson-onboard-compute-xlerobot.md)) |
| **Perception front-end** | YOLO detection, pose, segmentation, depth | ✅ native (`hailo-detect`/`-pose`/`-seg`/`-depth`, YOLO26) | ✅ but competes with the policy for GPU |
| **Agent reasoning** | local LLM/VLM, speech-to-text, scene analysis | ✅ `gen_ai_apps` (Hailo-10H only), Voice2Action | ✅ small LLM/VLM (memory-limited on 8 GB) |

- The Hailo's hard "no" is the **control policy**. LeRobot policies aren't Hailo apps, and compiling a flow-matching/diffusion robot VLA through the Hailo toolchain is **unproven today** ([Hailo](../../entities/hailo.md), [hailo-apps](../../sources/hailo-apps-github.md)).
- The Hailo's strong "yes" is **perception + an onboard LLM/VLM agent layer** — exactly the parts XLeRobot otherwise offloads to a PC or to **cloud Gemini 3 Flash** ([XLeRobot](../../entities/xlerobot.md)). The [`hailo-apps`](../../sources/hailo-apps-github.md) repo ships these as ready-to-run CLIs.

## Why "both" is usually the real answer

The two paths are complementary, not competing, because they map onto **the layers XLeRobot already splits**:

- **Pi 5 is already the host/relay** in the stock design. Adding the AI HAT+ 2 upgrades that host into a *local perception + agent brain* for **$180**, killing the cloud dependency for reasoning and giving 30 fps onboard vision — without touching the policy path.
- **But the manipulation policy still wants CUDA.** If your robot must run ACT/diffusion/SmolVLA onboard and reactively, you still need a [Jetson Orin Nano/NX](jetson-onboard-compute-xlerobot.md). The Hailo does not remove that need.

So the architecture that actually maximizes capability per dollar/watt is often **Pi 5 + AI HAT+ 2 for perception & LLM-agent + a Jetson (or PC) for the policy** — each silicon doing the job it's good at.

> [!note] Power & PCIe caveats (unquantified)
> The AI HAT+ 2's sustained-LLM power draw isn't published, and the Pi 5 exposes a **single PCIe lane** the HAT shares with any NVMe SSD — both matter for an untethered build on XLeRobot's [288 Wh / 300 W C300 budget](anker-portable-power-stations.md). These are open questions, not solved numbers.

## Decision guide

| Your goal | Pick |
|---|---|
| Onboard **vision** to ground the agent, cheaply | **AI HAT+ 2** on the existing Pi 5 host |
| **Cut the cloud** for LLM/VLM/voice reasoning | **AI HAT+ 2** (Hailo-10H `gen_ai_apps`) |
| Run the **manipulation policy** onboard at all | **Jetson Orin Nano** (validated; ACT ~28 Hz) |
| Run **diffusion/SmolVLA-class** policies onboard | **Jetson Orin NX 16 GB** (the [sweet spot](jetson-onboard-compute-xlerobot.md)) |
| Maximize capability, untethered | **Pi 5 + AI HAT+ 2 (perception/agent) + Jetson (policy)** |

**Bottom line:** the AI HAT+ 2 is the cheapest way to give an XLeRobot a *local brain for perception and language*, and the wiki's first non-CUDA onboard option — but it is **not a Jetson substitute for the control policy**. Choose by *layer*, not by TOPS: NPU for compiled vision/LLM, CUDA for the PyTorch policy.

## Related
- [Jetson onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md) — the CUDA-side deep dive (Orin Nano → NX → AGX → Thor) this page complements.
- [Raspberry Pi AI HAT+ 2 (Hailo-10H)](../../sources/raspberry-pi-ai-hat-plus-2.md) — the NPU board.
- [hailo-apps (GitHub)](../../sources/hailo-apps-github.md) — the software that runs on it.
- [Hailo](../../entities/hailo.md) — accelerator family + HEF toolchain.
- [Raspberry Pi 5](../../entities/raspberry-pi-5.md) — the host.
- [XLeRobot](../../entities/xlerobot.md) — the robot whose three compute layers drive this split.
- [VLA models](../../concepts/learning/vla-models.md) — the policies that need CUDA.
