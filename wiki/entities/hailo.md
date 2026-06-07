---
title: Hailo
type: entity
subtype: company
created: 2026-06-07
updated: 2026-06-07
sources: 2
tags: [hailo, npu, edge-ai, accelerator, raspberry-pi, llm, vlm, computer-vision]
---

# Hailo

Israeli fabless semiconductor company making **edge-AI accelerators** (NPUs) — fixed-function neural-inference chips for low-power, on-device AI. Best known in the hobbyist/robotics world as the silicon inside Raspberry Pi's AI accelerator HATs.

## Accelerator family

| Chip | Class | Headline perf | On-chip RAM | Pi product |
|---|---|---|---|---|
| **Hailo-8L** | Vision CNN | 13 TOPS | — (uses host) | Raspberry Pi **AI Kit** / **AI HAT+ (13 TOPS)** |
| **Hailo-8** | Vision CNN | 26 TOPS | — (uses host) | Raspberry Pi **AI HAT+ (26 TOPS)** |
| **Hailo-10H** | **Generative AI** | **40 TOPS (INT4)** | **8 GB dedicated** | Raspberry Pi **[AI HAT+ 2](../sources/raspberry-pi-ai-hat-plus-2.md)** ($180) |

The key generational split: **Hailo-8/8L are vision-CNN accelerators** (object detection, segmentation, pose — INT8); the **Hailo-10H adds generative AI**, with its own 8 GB of DRAM so LLM/VLM weights don't consume host memory ([AI HAT+ 2](../sources/raspberry-pi-ai-hat-plus-2.md)). The 10H's vision performance is "comparable to the AI HAT+ (26 TOPS)," so it supersedes the older board for new builds that also want LLM/VLM workloads.

## How it works (toolchain)

- An NPU runs **pre-compiled, fixed-function models**, not arbitrary PyTorch. Models are compiled from ONNX to Hailo's **HEF** (Hailo Executable Format) using the **Hailo Dataflow Compiler / Model Zoo** on an **x86 host**; the Pi then runs the HEF via **HailoRT**.
- On Raspberry Pi OS the easy install is the `hailo-all` apt metapackage (PCIe DKMS driver + HailoRT + TAPPAS + `rpicam-apps` integration). The AI HAT+ 2's generative-AI path additionally uses Hailo's **[`hailo-apps`](../sources/hailo-apps-github.md)** repo (MIT; 30+ apps; vision CLIs `hailo-detect-simple`/`hailo-pose`/`hailo-seg`/`hailo-depth` + Hailo-10H-only `gen_ai_apps` for LLM/VLM/speech, e.g. Voice2Action). Core deps: HailoRT + Python binding; TAPPAS Core only needed for GStreamer pipelines (`--no-tappas-required` skips it).
- Consequence: a Hailo NPU accelerates models you've **compiled for it** — typically vision CNNs and (on the 10H) supported LLMs/VLMs. It is **not** a drop-in for running a researcher's PyTorch policy unchanged.

## Relevance in this wiki — NPU vs. Jetson for XLeRobot

Hailo is the wiki's first **non-CUDA onboard-compute** option for a Raspberry-Pi [XLeRobot](xlerobot.md) build, contrasting with the [Jetson onboard-compute ladder](../syntheses/platforms/jetson-onboard-compute-xlerobot.md):

- **Fits**: a local **LLM/VLM agent-reasoning layer** (replacing XLeRobot's cloud Gemini agent) and fast onboard perception, on a Pi 5, low power, no network.
- **Does not fit**: running LeRobot **control policies** (ACT / Diffusion Policy / SmolVLA / π0.5) — those are CUDA/PyTorch and belong on a [Jetson Orin Nano / NX](../syntheses/platforms/jetson-onboard-compute-xlerobot.md). Compiling a robot VLA to Hailo HEF is unproven today.
- **The bet**: NPU = compiled-model coprocessor (host stays the Pi); Jetson = general CUDA brain that runs the policies as-is.

## Related
- [Raspberry Pi 5](raspberry-pi-5.md) — the host the AI HAT+ boards plug into.
- [XLeRobot](xlerobot.md) — candidate deployment platform.
- [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — the CUDA alternative.
- [Jetson Orin Nano](jetson-orin-nano.md) — the validated XLeRobot onboard CUDA device.

## Mentioned in
- [Raspberry Pi AI HAT+ 2 (Hailo-10H)](../sources/raspberry-pi-ai-hat-plus-2.md)
- [hailo-apps (GitHub)](../sources/hailo-apps-github.md)
- [Hailo NPU vs Jetson for an onboard XLeRobot brain](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md)
