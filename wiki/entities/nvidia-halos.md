---
title: NVIDIA Halos (for Robotics)
type: entity
subtype: product
created: 2026-07-15
updated: 2026-07-15
sources: 3
tags: [nvidia-halos, functional-safety, robot-safety, igx, jetson-thor, physical-ai, qnx, holoscan, certification, anab, tuv, outside-in, metropolis]
---

# NVIDIA Halos (for Robotics)

**NVIDIA Halos** — NVIDIA's **full-stack functional-safety system for physical AI**, *"the comprehensive safety system … that takes robots from prototype to production,"* spanning **silicon → OS → middleware → applications** ([Halos for Robotics](../sources/nvidia-halos-robotics.md)). Not an acronym — a "safety halo" metaphor. Positioned as **"AV-Proven, Robotics-Ready"**: it ports NVIDIA's autonomous-vehicle safety foundation to **humanoids and industrial robots / AMRs**. It's the safety system that runs on the **[IGX T3000](jetson-thor.md)** Jetson Thor SKU.

## Architecture (4 layers)

1. **Platform Safety** — **NVIDIA IGX** (System-on-Module on the [Thor](jetson-thor.md) SoC) with a **Functional Safety Island (FSI)**; third-party assessed.
2. **Halos OS** — **Linux + QNX**; **Halos Core** (safety OS) + **Safety Extensions Package (SEP)** + **Holoscan SensorBridge** (deterministic real-time sensor/safety bridging).
3. **Middleware & Applications** — safety blueprints + algorithmic safety.
4. **Ecosystem** — OEMs, sensor partners, certification bodies.

## Two safety modes

- **Inside-Out** — onboard sensors manage the robot's immediate safety envelope. Flagship: **[Agility Robotics' Digit](digit.md)** (onboard IGX Thor + Halos Core) — the **inaugural humanoid partner**.
- **Outside-In** — external cameras / infrastructure establish virtual zones (fences, dynamic zoning, occlusion alerts) for forklift loading, shared-space AMRs. The **[Outside-In Safety Blueprint](../sources/halos-outside-in-safety-github.md) is open-source** (Apache-2.0, early access): 3 pillars — **AI Perception** (Metropolis VSS, swappable) → **Safety Core** (the *Outside-In Safety Framework / OISF*, ex-*Proactive Safety Framework*; emits a MUTE/UNMUTE decision) → **closed-loop SIL/HIL testing** ([Isaac Sim](nvidia-isaac-sim.md)). Reference use case: **automated trailer loading** (cameras watch workers + forklifts to gate dock entry). Ships a **Claude Code skill** (`hoisa-deploy-profile`) for deployment. **Not production-safety-certified** on its own — it's the *swappable, uncertified* infrastructure-perception side, vs. the certified Inside-Out IGX-FSI stack.

## Certification

The **first ANAB-accredited inspection program for AI functional safety in physical AI**; **Halos AI Systems Inspection Lab** shortens time-to-certification; third-party notified bodies incl. **TÜV Rheinland**.

## Why it matters in this wiki

- The **concrete functional-safety product** behind the wiki's long-standing [robot-safety-standards](../concepts/robotics/robot-safety-standards.md) question — a certified **deterministic safety layer** engineered to sit *beneath* an uncertified learned [VLA](../concepts/learning/vla-models.md)/[LBM](../concepts/learning/large-behavior-models.md) policy on the *same* [Thor](jetson-thor.md) module. It productizes the "certified classical safety layer wrapping a learned policy" pattern the wiki predicted.
- Firmly on the **physical-safety** side of the physical-vs-semantic safety gap — it complements, and is disjoint from, LLM [AI guardrails](../concepts/safety/ai-guardrails.md); and it is *safety*, not [robot security](../concepts/robotics/robot-security.md) (adversarial).

## Related

- [Jetson Thor](jetson-thor.md) — IGX (T3000) is the Thor-based safety module Halos runs on.
- [Digit](digit.md) — inaugural humanoid partner.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md), [Robot security](../concepts/robotics/robot-security.md), [AI guardrails](../concepts/safety/ai-guardrails.md) — the safety/security neighbors.

## Mentioned in

- [NVIDIA Halos for Robotics](../sources/nvidia-halos-robotics.md) — primary source.
- [Halos Outside-In Safety Blueprint (GitHub)](../sources/halos-outside-in-safety-github.md) — the open-source Outside-In code (Metropolis VSS + Safety Core + Isaac Sim SIL/HIL).
- [Jetson Thor T3000/T2000 blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md) — IGX T3000 runs Halos.

## Open questions

- Exact ISO/IEC standards targeted (26262/21448 AV heritage implied; 13482/10218 for service/industrial not named on the page).
- Whether the learned policy itself is certified, or only the deterministic layer around it.
