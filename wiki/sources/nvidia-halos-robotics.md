---
title: "NVIDIA Halos for Robotics (AI Trust Center)"
type: source
url: https://www.nvidia.com/en-us/ai-trust-center/halos/robotics/
author: NVIDIA
published: 2026 (rolling)
ingested: 2026-07-15
format: product / documentation page
tags: [nvidia-halos, functional-safety, robot-safety, igx, jetson-thor, physical-ai, agility-robotics, digit, qnx, holoscan, certification, anab, tuv, humanoid, amr]
---

# NVIDIA Halos for Robotics (AI Trust Center)

## Summary

**NVIDIA Halos** is *"the comprehensive safety system for physical AI that takes robots from prototype to production"* — an **end-to-end, full-stack safety platform spanning silicon, operating systems, middleware, and applications**. "Halos" is **not an acronym**; it's a metaphor (a protective "safety halo" around the robot). It brings **autonomous-vehicle-grade functional safety to humanoids and industrial robots** — *"AV-Proven, Robotics-Ready,"* built on the same foundation that powers NVIDIA's AV safety stack. This is the productized answer to the "certified deterministic safety layer under an uncertified learned policy" pattern the wiki's [robot-safety-standards](../concepts/robotics/robot-safety-standards.md) page predicted, and the safety system named on the **[IGX T3000](../entities/jetson-thor.md)** Jetson Thor SKU.

## Key claims

**Full-stack architecture (4 layers)**
1. **Platform Safety (hardware)** — **NVIDIA IGX** (a System-on-Module based on the **[Thor](../entities/jetson-thor.md) SoC**) with a dedicated **Functional Safety Island (FSI)**; *"third-party assessed, safety-compliant."*
2. **Halos OS Foundation** — runs on IGX Thor, integrating **Linux + QNX**; components: **Halos Core** (the safety OS), **Safety Extensions Package (SEP)** (functional-safety modules), and **Holoscan SensorBridge (HSB)** (real-time sensor control + safety bridging → deterministic real-time control).
3. **Middleware & Applications** — safety blueprints + algorithmic safety.
4. **Ecosystem Integration** — OEMs, sensor partners, certification bodies.

**Inside-Out vs. Outside-In safety** (the source's central framing)
- **Inside-Out** — *"on-board robot sensors managing the immediate safety envelope."* Flagship: **[Agility Robotics](../entities/digit.md)' Digit** humanoid running **onboard IGX Thor + Halos Core**.
- **Outside-In** — *"external infrastructure (like external cameras) to monitor the environment and establish virtual zones"* (virtual fences, dynamic zoning, occlusion alerts). Use cases: autonomous forklift trailer loading, mobile-robot zoning in shared spaces. The **NVIDIA Halos Outside-In Safety Blueprint** is **open-source**.

**Certification pathway**
- **First ANAB-accredited inspection program for AI functional safety in physical AI.**
- **Halos AI Systems Inspection Lab** — "accelerates the time to certification."
- Third-party inspection by "recognized notified bodies"; **TÜV Rheinland** named (outside-in safety forklift use case).

**Safety features**: deterministic real-time control (via Holoscan), redundancy + fail-safe via the FSI architecture, third-party inspection pathway that shortens certification time.

## Entities mentioned

- [NVIDIA Halos](../entities/nvidia-halos.md) — this is its primary source (new entity).
- [Jetson Thor](../entities/jetson-thor.md) — IGX is a Thor-SoC SoM; IGX T3000 is the safety SKU.
- [Digit](../entities/digit.md) / Agility Robotics — inaugural humanoid partner.
- [NVIDIA](../entities/nvidia.md).

## Concepts touched

- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — Halos is the concrete **functional-safety productization** (deterministic safety functions) of that framework; complements, does *not* replace, ISO 13482-style certification.
- [Robot security](../concepts/robotics/robot-security.md) — the *safety* (physical harm) neighbor of the *security* (adversarial) axis; distinct concerns.

## Open questions

- **Which ISO/IEC standards exactly?** The page emphasizes functional safety + third-party assessment but doesn't name ISO 13482 / 10218 / IEC 61508 / ISO 26262 / SOTIF explicitly here — the AV heritage implies the 26262/21448 lineage. A spec doc would confirm.
- **Does Halos certify the learned policy, or only the layer beneath it?** The architecture certifies a deterministic safety envelope (FSI, SEP, protective zones) *around* the VLA — the [robot-safety-standards](../concepts/robotics/robot-safety-standards.md) open question (how the stochastic policy itself demonstrates conformity) is not obviously closed.
- **Semantic-harm gap** — Halos is *physical* functional safety; it says nothing about [LLM-planner](../concepts/agents/llm-agent-architecture.md) semantic decisions ([AI guardrails](../concepts/safety/ai-guardrails.md) territory). Still no source bridging physical + semantic safety.
