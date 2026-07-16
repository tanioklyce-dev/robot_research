---
title: "Halos Outside-In Safety Blueprint (NVIDIA/halos-outside-in-safety GitHub)"
type: source
url: https://github.com/NVIDIA/halos-outside-in-safety
author: NVIDIA
published: 2026 (early access)
ingested: 2026-07-15
license: Apache-2.0
format: GitHub repository
tags: [nvidia-halos, outside-in-safety, functional-safety, robot-safety, metropolis, vss, isaac-sim, igx, jetson-thor, forklift, amr, safety-agent, claude-code, code]
---

# Halos Outside-In Safety Blueprint (NVIDIA/halos-outside-in-safety)

## Summary

The **open-source (Apache-2.0) reference architecture** for the **Outside-In** half of **[NVIDIA Halos](../entities/nvidia-halos.md)** — *"extends robot perception beyond on-board sensors by using external infrastructure cameras and AI agents to dynamically control robot behavior and perform at maximum efficiency."* It's a blueprint for building **safety agents** from **fixed infrastructure cameras**: cameras → AI perception → a **Safety Core** decision engine that emits a MUTE/UNMUTE-style safety decision. **Early access, prototyping/evaluation only — explicitly _"not for production use in safety-related systems without your own certified safety layer."_** 54★; C++ 84%. This is the code behind the Outside-In Safety Blueprint named on the [Halos for Robotics](nvidia-halos-robotics.md) page.

## Key claims

**Three pillars**
1. **AI Perception** — backend built on **NVIDIA Metropolis Blueprint for Video Search & Summarization (VSS)**; a *swappable* component (bring your own perception).
2. **Safety Core** — the decision engine: event integration, logic evaluation, communication. Data flow: *"cameras feed AI perception, which publishes detections to the Safety Core, which emits a decision."* Also called the **Outside-In Safety Framework (OISF)**, historically the **Proactive Safety Framework (PSF)** (legacy binaries `libnvpsb.so`, `nvpss_daemon`, `nvpsd_gateway`).
3. **Closed-Loop Testing** — SIL + HIL harness via **[NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)**.

**Deployment profiles**
- **`base`** — Safety Core on an existing perception feed; MUTE/UNMUTE decision rendered as a VST overlay.
- **`sil`** — full closed loop with [Isaac Sim](../entities/nvidia-isaac-sim.md) driving a forklift (**requires a GPU with RT cores** — i.e. not [Jetson Thor](../entities/jetson-thor.md)).
- **`hil`** — hardware-in-the-loop **on [Jetson Thor](../entities/jetson-thor.md)** (under development).

**Reference use case**: **Automated Trailer Loading** — fixed cameras monitor workers + autonomous forklifts to decide real-time dock-entry safety. Targets AMRs / material handling.

**Stack / deploy**: NVIDIA Metropolis VSS Blueprint (perception), [Isaac Sim](../entities/nvidia-isaac-sim.md) (sim), Docker + Docker Compose. Prereqs: **NGC early-access entitlement**, Docker 28.3.3–29.5, NVIDIA Container Toolkit 1.17.8+; OS = x86 Ubuntu 24.04 *or* **IGX Thor (Jetson Linux BSP Rel 38.5)**. Deploy the VSS perception backend first, then launch a profile.

> [!note] Agentic deployment via a Claude Code skill
> The repo ships a **Claude Code skill, `hoisa-deploy-profile`**, to deploy a safety agent (alternative to manual Docker Compose) — a first-party instance of the agent-assisted-robotics-tooling pattern the wiki tracks (cf. the [Team 254 / wpilib-agent-tools](team-254-ai-in-frc-presentation.md) and [ROS 2↔MCP](../entities/ros2-mcp-server.md) threads).

## Entities mentioned

- [NVIDIA Halos](../entities/nvidia-halos.md) — the parent safety system; this is its Outside-In code.
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) (SIL/HIL harness), [Jetson Thor](../entities/jetson-thor.md) / IGX Thor (HIL target).
- [NVIDIA](../entities/nvidia.md); Metropolis VSS (perception backend).

## Concepts touched

- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — infrastructure-side (Outside-In) functional safety; a *deterministic safety envelope built from external perception*, complementing on-robot Inside-Out safety.
- [VLA models](../concepts/learning/vla-models.md)-adjacent: VLM/VSS perception as the safety sensor.

## Open questions

- **Not production-certified** — the repo is a prototyping blueprint; a real deployment needs "your own certified safety layer." Relationship to the [Halos](../entities/nvidia-halos.md) TÜV/ANAB certified path (which is about the *Inside-Out* IGX-FSI stack) is: this Outside-In blueprint is the *un-certified, swappable* infrastructure-perception side.
- No explicit ROS 2 / DeepStream / Holoscan integration surfaced in the README (Holoscan SensorBridge is the *Inside-Out* piece).
