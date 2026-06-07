---
title: "Raspberry Pi AI HAT+ 2 (Hailo-10H)"
type: source
url: https://www.raspberrypi.com/products/ai-hat-plus-2/
author: Raspberry Pi Ltd
published: 2026
ingested: 2026-06-07
tags: [raspberry-pi, hailo, edge-ai, npu, llm, vlm, generative-ai, accelerator, xlerobot]
format: product page
---

# Raspberry Pi AI HAT+ 2 (Hailo-10H)

## Summary

Official Raspberry Pi product page for the **AI HAT+ 2**, an edge-AI accelerator HAT for the [Raspberry Pi 5](../entities/raspberry-pi-5.md) built around the **[Hailo](../entities/hailo.md)-10H** accelerator with **8 GB of dedicated on-board RAM**, priced at **$180**. Unlike the original AI HAT+ (Hailo-8/8L, a vision-CNN accelerator), the AI HAT+ 2 is explicitly a **generative-AI** board: it targets **local LLMs and vision-language models (VLMs)** "without a network connection." Marketing tagline: **"A HAT that speaks your language."**

> [!note] Naming correction
> The AI HAT+ **2** and "the Hailo-10H board" are the **same product** — not two separate things. The earlier-generation **AI HAT+** (no "2") is the Hailo-8L (13 TOPS) / Hailo-8 (26 TOPS) vision accelerator; the **AI HAT+ 2** is the Hailo-10H generative-AI accelerator. See [Hailo](../entities/hailo.md) for the full chip family.

## Key claims

- **Accelerator**: Hailo-10H, **40 TOPS (INT4)** inferencing performance.
- **On-board memory**: **8 GB dedicated RAM** (the accelerator has its own DRAM — important for fitting LLM/VLM weights without stealing the Pi's system memory).
- **Price**: **$180**.
- **Compatibility**: **Raspberry Pi 5** only.
- **Connection / form factor**: **HAT+ specification** (GPIO-based), "fully integrated into Raspberry Pi's camera software stack."
- **Vision parity**: computer-vision performance is "**comparable to Raspberry Pi AI HAT+ (26 TOPS)**" — i.e. it does the old board's vision job *and* adds generative AI.
- **Target workloads** (verbatim examples): "**speech to text, translation, or visual scene analysis**"; running **LLMs, VLMs, and generative AI models locally** "at the edge and without a network connection."
- **Software**: generative-AI model software via Hailo's GitHub — **`github.com/hailo-ai/hailo-apps`**; sample models provided by Hailo, custom models can be trained/compiled.
- **In the box**: optional heatsink; 16 mm stacking header, spacers, and screws for use alongside the Raspberry Pi Active Cooler.
- **Production lifespan**: guaranteed until at least **January 2036**.
- **Docs**: product brief `RP-009655-MM-raspberry-pi-ai-hat-plus-2-product-brief.pdf`; full docs at `raspberrypi.com/documentation/accessories/ai-hat-plus.html`.

> [!note] Not on the page
> Exact physical dimensions, weight, PCIe generation/lane details, power draw in watts, tokens/sec figures, and a list of specific supported LLMs are **not** stated on the product page. The launch date is not given either; `published: 2026` is inferred from the Jan-2036 (≈10-year) guarantee and should be treated as approximate.

## Setup (Raspberry Pi documented flow, general knowledge — not on this page)
The canonical Pi-5 install for the Hailo HATs is: update firmware (`sudo apt full-upgrade` + `rpi-eeprom-update`), seat the HAT on the GPIO header, then `sudo apt install hailo-all`, reboot, and verify with `hailortcli fw-control identify`. The AI HAT+ 2's **generative-AI** workflow additionally uses the **`hailo-ai/hailo-apps`** repo and Hailo's GenAI/Dataflow-Compiler toolchain (models are compiled to Hailo's **HEF** format on an x86 host, then run on the Pi). See [Hailo](../entities/hailo.md) for the runtime/toolchain detail.

## Relevance to this wiki — XLeRobot

The AI HAT+ 2 is the first **NPU (non-CUDA) onboard-compute option** documented here for the [XLeRobot](../entities/xlerobot.md) Raspberry-Pi build, an alternative to the [Jetson onboard-compute ladder](../syntheses/platforms/jetson-onboard-compute-xlerobot.md):

- **What it can plausibly do**: run the robot's **LLM/VLM agent-reasoning layer locally** (XLeRobot's stock RoboCrew/LangChain agent uses cloud Gemini 3 Flash — see [XLeRobot](../entities/xlerobot.md)), plus fast onboard vision (speech-to-text, scene analysis).
- **What it does *not* do**: it is **not a CUDA GPU**, so it does not run LeRobot's PyTorch control policies (ACT / Diffusion Policy / SmolVLA / π0.5) as-is. Those still need a Jetson or PC. Running a robot VLA on Hailo would require compiling it through Hailo's toolchain — **unproven for these policies today**.
- **Architecture takeaway**: a **Pi 5 + AI HAT+ 2 is a different bet than a Jetson** — fixed-function compiled-model NPU vs. a general CUDA device. It fits the "Pi-as-host + onboard LLM/perception" role; the validated path for the *control policy* is still [Orin Nano / Orin NX](../syntheses/platforms/jetson-onboard-compute-xlerobot.md). Full comparison: [Hailo NPU vs Jetson for an onboard XLeRobot brain](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md).

## Entities mentioned
- [Hailo](../entities/hailo.md) — accelerator vendor; Hailo-10H chip.
- [Raspberry Pi 5](../entities/raspberry-pi-5.md) — host platform.
- [XLeRobot](../entities/xlerobot.md) — candidate deployment platform.

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — onboard local LLM/VLM for an agent-reasoning layer.
- [VLA models](../concepts/learning/vla-models.md) — the policies an NPU like this can and can't run.

## Open questions
- Real tokens/sec for common LLMs/VLMs (e.g. a 7–8 B model) on the Hailo-10H — not published here.
- Can XLeRobot's SmolVLA / π0.5 be compiled to Hailo HEF at all, and at what latency? (No evidence today.)
- PCIe lane usage on the Pi 5 — does the HAT+ 2 leave room for an NVMe SSD, or contend for the single lane like the original AI HAT+?
- Power draw under sustained LLM load (the figure that would decide its fit on XLeRobot's 288 Wh / 300 W [C300 budget](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)).
