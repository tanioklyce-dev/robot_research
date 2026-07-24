---
title: jetson-examples (reComputer runner)
type: entity
subtype: software-tool
created: 2026-06-14
updated: 2026-06-14
sources: 4
tags: [seeed-studio, jetson, recomputer, jetson-containers, docker, edge-ai, one-command-deploy]
---

# jetson-examples (reComputer runner)

**`jetson-examples`** — Seeed Studio's open-source (MIT) catalog of **one-command demos** for running vision-AI and generative-AI models on NVIDIA Jetson. Installed with `pip3 install jetson-examples`, it exposes the **`reComputer`** CLI: `reComputer run <example>` selects/builds the appropriate Docker container for the host's JetPack/L4T and launches a working demo; `reComputer clean <example>` tears it down. It is the consumer-friendly layer **above [jetson-containers](jetson-containers.md)** — where jetson-containers builds and version-matches the `dustynv/*` images, jetson-examples bundles each model into a single named recipe.

## Why it matters in this wiki

It is the **"buy-the-carrier, run-one-command" path** onto the Jetson AI stack — the practical complement to Seeed's [reComputer](seeed-studio.md) carrier boards. Where [jetson-containers](jetson-containers.md) is the infrastructure answer to the aarch64 dependency problem, jetson-examples is the curated menu on top: ~37 recipes spanning LLM/VLM serving, object detection / depth / pose, image + audio generation, and robotics (ROS1, [Isaac ROS NVBlox](nvblox.md) 3D mapping). Relevant wherever the wiki discusses getting a model running on [Orin Nano](jetson-orin-nano.md) / NX / AGX silicon without hand-building the stack.

## Key facts

- **Tool:** `reComputer` CLI (`reComputer run|clean <example>`); `pip3 install jetson-examples`.
- **Publisher / license:** [Seeed Studio](seeed-studio.md) (Seeed-Projects/jetson-examples); **MIT**. 264★ / 40 forks; created 2024-06-24, actively maintained.
- **Substrate:** builds on [jetson-containers](jetson-containers.md) (`dustynv/*`, `autotag`) + Docker + NVIDIA Container Runtime.
- **Coverage:** ~37 recipes; JetPack **4.6 → 7.1** depending on recipe. Catalog spans LLMs (llama3/3.2, gemma4, qwen, nemotron-3-nano, gpt-oss, ollama), VLMs (llava family, live-llava, live-vlm-webui), detection/depth/pose (YOLO11/26/v10, NanoOWL, Depth-Anything v1–v3, MoveNet), gen-AI (ComfyUI, Stable Diffusion WebUI, Whisper, Parler-TTS, AudioCraft), and robotics (ros1-jp6, [nvblox](nvblox.md)).
- **Contribution:** Seeed advertises a **$250 bounty** per accepted new example.

## Related

- [jetson-containers](jetson-containers.md) — underlying container framework (jetson-examples wraps it).
- [Seeed Studio](seeed-studio.md) — publisher; reComputer carrier hardware.
- [Isaac ROS NVBlox](nvblox.md) — the `nvblox` recipe's payload.
- [Jetson Orin Nano](jetson-orin-nano.md) / [Jetson Thor](jetson-thor.md) — target silicon.
- [Ollama](ollama.md) — one of the LLM-serving recipes.
- [Ultralytics YOLO](ultralytics-yolo.md) — upstream of the YOLO detection recipes.

## Open questions

- Per-recipe RAM/tier matrix (which run on Orin Nano 8 GB vs requiring NX 16 GB / AGX) is not published; 30B-class recipes (`qwen3.6-35b`, `nemotron-3-nano`) imply large-memory tiers.
- How stale recipes get relative to upstream model churn.

## Mentioned in

- [Seeed jetson-examples (repo + reComputer runner)](../sources/seeed-jetson-examples.md) — repo + full recipe catalog.
- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md) — the `reComputer run nvblox` 3D-mapping recipe.
