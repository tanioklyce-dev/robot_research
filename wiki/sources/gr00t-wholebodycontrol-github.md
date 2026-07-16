---
title: "GR00T Whole-Body Control (NVlabs/GR00T-WholeBodyControl GitHub)"
type: source
url: https://github.com/NVlabs/GR00T-WholeBodyControl
author: NVIDIA GEAR / NVlabs
published: 2026 (rolling)
ingested: 2026-07-15
license: Apache-2.0 (code) + NVIDIA Open Model License (weights)
format: GitHub repository
tags: [gear-sonic, motionbricks, decoupled-wbc, whole-body-control, humanoid, unitree-g1, nvidia, gear, groot, code, teleoperation, isaac-lab]
---

# GR00T Whole-Body Control (NVlabs/GR00T-WholeBodyControl)

## Summary

The **official code platform** for NVIDIA GEAR's humanoid [whole-body control](../concepts/robotics/whole-body-control.md) line — *"a unified platform for developing and deploying advanced humanoid controllers."* This single repo is the code home for **three** wiki-tracked systems at once: **[GEAR-SONIC](../entities/gear-sonic.md)** ([paper](sonic-paper.md)), **[MotionBricks](motionbricks-paper.md)** ([paper](motionbricks-paper.md)), and the previously-unnamed **"Decoupled WBC"** controllers used inside **[GR00T](../entities/nvidia-groot.md) N1.5 / N1.6** — plus a VR-teleoperation stack. **2.9k stars / 427 forks**; Python 56.8% + C++ 38.4%. Dual license: **Apache-2.0 (code) + NVIDIA Open Model License (weights)**.

## Key claims

**Repo layout / components**
- **`gear_sonic/`** — full training pipeline: **PPO**, data processing, configs (`pip install -e "gear_sonic/[training]"`; `accelerate launch … train_agent_trl.py`). Training requires [Isaac Lab](../entities/nvidia-isaac-lab.md).
- **`gear_sonic_deploy/`** — **C++ inference stack** for hardware deployment (TensorRT); `./deploy.sh --input-type zmq_manager real`.
- **`motionbricks/`** — [MotionBricks](motionbricks-paper.md) **preview release**: interactive demos + pretrained checkpoints (see the MotionBricks page for details).
- **`decoupled_wbc/`** — **"Controllers used in GR00T N1.5 and N1.6"** — this repo names the whole-body controllers behind those GR00T releases as *Decoupled WBC* (a new fact vs. the wiki's prior [GR00T](../entities/nvidia-groot.md) coverage).
- **VR teleoperation stack** — data collection via a **PICO** headset.

**GEAR-SONIC** is described as *"a humanoid behavior foundation model that gives robots a core set of motor skills learned from large-scale human motion data"* — motion tracking as the training task; one unified policy from walking to teleoperation. Checkpoints (ONNX + PyTorch) on Hugging Face; `download_from_hf.py` (`--low-latency` for the teleoperation variant).

**Platform / deps**: **[Unitree G1](../entities/unitree-g1.md)** is the primary supported robot. Deps: Isaac Lab (training only), MuJoCo (sim), TensorRT (C++ deploy), PyTorch, Accelerate.

## Entities mentioned

- [GEAR-SONIC](../entities/gear-sonic.md), [NVIDIA GEAR](../entities/nvidia-gear.md), [NVIDIA GR00T](../entities/nvidia-groot.md) — the code's owners/consumers.
- [Unitree G1](../entities/unitree-g1.md) — target robot.
- [Isaac Lab](../entities/nvidia-isaac-lab.md), [MuJoCo](../entities/mujoco.md) — training/sim deps.

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — the repo *is* the GEAR WBC toolchain (train → deploy).
- Sim-to-real ([Isaac Lab](../entities/nvidia-isaac-lab.md) → C++/TensorRT on hardware).

## Open questions

- **Decoupled WBC** has no standalone paper cited here — it's named only as the N1.5/N1.6 controller. Worth tracking whether it gets documented separately.
- Relationship between the repo's `gear_sonic` weights and the `nvidia/GEAR-SONIC` HF checkpoints referenced in the [SONIC paper](sonic-paper.md) (same or re-released?).
