---
title: NVIDIA Halos (for Robotics)
type: entity
subtype: product
created: 2026-07-15
updated: 2026-07-16
sources: 4
tags: [nvidia-halos, functional-safety, robot-safety, igx, jetson-thor, physical-ai, qnx, holoscan, certification, anab, tuv, outside-in, metropolis]
---

# NVIDIA Halos (for Robotics)

**NVIDIA Halos** — NVIDIA's **full-stack functional-safety system for physical AI**, *"the comprehensive safety system … that takes robots from prototype to production,"* spanning **silicon → OS → middleware → applications** ([Halos for Robotics](../sources/nvidia-halos-robotics.md)). Not an acronym — a "safety halo" metaphor. Positioned as **"AV-Proven, Robotics-Ready"**: it ports NVIDIA's autonomous-vehicle safety foundation to **humanoids and industrial robots / AMRs**. It's the safety system that runs on the **[IGX T3000](jetson-thor.md)** Jetson Thor SKU.

## Architecture (4 layers)

1. **Platform Safety** — **NVIDIA IGX** (System-on-Module on the [Thor](jetson-thor.md) SoC) with a **Functional Safety Island (FSI)**; third-party assessed. The [technical blog](../sources/nvidia-halos-robotics-blog.md) quantifies it: IGX Thor = up to **2,070 FP4 TFLOPS** / 128 GB; the **FSI is IEC 61508 SIL 3-capable** (isolated, ~12K DMIPS, own I/O/power/clocks); **22,000+ safety mechanisms** across the SoC.
2. **Halos OS** — **Linux + QNX**; **Halos Core** (safety OS) + **Safety Extensions Package (SEP)** + **Holoscan SensorBridge** (deterministic real-time sensor/safety bridging; end-to-end IEC 61508 **SIL 2** + MACsec). Two configs: *Halos Core Linux*, or *+ QNX* via NV Hypervisor (Linux-for-AI ∥ QNX-for-safety-critical). Built on NVIDIA's AV-safety base — **18,000 engineering-years, 21 B safety transistors, 7 M lines** of safety-assessed code.
3. **Middleware & Applications** — safety blueprints + algorithmic safety.
4. **Ecosystem** — OEMs, sensor partners, certification bodies.

> [!note] 3-layer vs 4-layer
> The [developer blog](../sources/nvidia-halos-robotics-blog.md) frames Halos as **3 layers** (Platform / Software / Ecosystem); the AI-Trust-Center page uses **4** (splitting Middleware & Apps out). Same stack, different granularity.

## Two safety modes

- **Inside-Out** — onboard sensors manage the robot's immediate safety envelope. Flagship: **[Agility Robotics' Digit](digit.md)** (onboard IGX Thor + Halos Core) — the **inaugural humanoid partner**.
- **Outside-In** — external cameras / infrastructure establish virtual zones (fences, dynamic zoning, occlusion alerts) for forklift loading, shared-space AMRs. The **[Outside-In Safety Blueprint](../sources/halos-outside-in-safety-github.md) is open-source** (Apache-2.0, early access): 3 pillars — **AI Perception** (Metropolis VSS, swappable) → **Safety Core** (the *Outside-In Safety Framework / OISF*, ex-*Proactive Safety Framework*; emits a MUTE/UNMUTE decision) → **closed-loop SIL/HIL testing** ([Isaac Sim](nvidia-isaac-sim.md)). Reference use case: **automated trailer loading** (cameras watch workers + forklifts to gate dock entry). Ships a **Claude Code skill** (`hoisa-deploy-profile`) for deployment. **Not production-safety-certified** on its own — it's the *swappable, uncertified* infrastructure-perception side, vs. the certified Inside-Out IGX-FSI stack.

## Certification

The **first ANAB-accredited inspection program for AI functional safety in physical AI** (ISO/IEC 17020 Inspection Body, first worldwide accredited across **both AV and robotics**); the **Halos AI Systems Inspection Lab** issues an Inspection Certificate partners present to a notified body (**TÜV Rheinland/SÜD, SGS, exida, CERTX, UL**), so they avoid re-certifying the platform. **43+ ecosystem members** (16 automotive, 23 robotics, 4 cross-domain), incl. **[Boston Dynamics](boston-dynamics.md)**, KION, Infineon, TI, NXP, Ouster, FORT Robotics. NVIDIA holds **standards-leadership** roles: **IEC 61508 Convenor**, **ISO/IEC TS 22440 co-Convenor**, IEC TC 65 AhG 30, ISO 25785-1 — targeting IEC 61508 / ISO 26262 / ISO 13849 / ISO/IEC TR 5469 / ISO 25785-1 ([blog](../sources/nvidia-halos-robotics-blog.md)), which answers the old "which standards?" open question.

## Why it matters in this wiki

- The **concrete functional-safety product** behind the wiki's long-standing [robot-safety-standards](../concepts/robotics/robot-safety-standards.md) question — a certified **deterministic safety layer** engineered to sit *beneath* an uncertified learned [VLA](../concepts/learning/vla-models.md)/[LBM](../concepts/learning/large-behavior-models.md) policy on the *same* [Thor](jetson-thor.md) module. It productizes the "certified classical safety layer wrapping a learned policy" pattern the wiki predicted.
- Firmly on the **physical-safety** side of the physical-vs-semantic safety gap — it complements, and is disjoint from, LLM [AI guardrails](../concepts/safety/ai-guardrails.md); and it is *safety*, not [robot security](../concepts/robotics/robot-security.md) (adversarial).

## Related

- [Jetson Thor](jetson-thor.md) — IGX (T3000) is the Thor-based safety module Halos runs on.
- [Digit](digit.md) — inaugural humanoid partner.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md), [Robot security](../concepts/robotics/robot-security.md), [AI guardrails](../concepts/safety/ai-guardrails.md) — the safety/security neighbors.

## Mentioned in

- [NVIDIA Halos for Robotics](../sources/nvidia-halos-robotics.md) — AI Trust Center product page (primary).
- [Inside NVIDIA Halos for Robotics (developer blog)](../sources/nvidia-halos-robotics-blog.md) — the technical deep-dive: IGX Thor safety specs, Halos OS configs, full Outside-In pipeline (SIPP/SAIM/SEI/SDM), ANAB lab, standards leadership.
- [Halos Outside-In Safety Blueprint (GitHub)](../sources/halos-outside-in-safety-github.md) — the open-source Outside-In code (Metropolis VSS + Safety Core + Isaac Sim SIL/HIL).
- [Jetson Thor T3000/T2000 blog](../sources/nvidia-jetson-thor-t3000-t2000-blog.md) — IGX T3000 runs Halos.

## Open questions

- ~~Exact ISO/IEC standards targeted~~ — **answered** by the [blog](../sources/nvidia-halos-robotics-blog.md): IEC 61508 (primary), ISO 26262, ISO 13849, ISO/IEC TR 5469, ISO 25785-1. (ISO 13482/10218 service/industrial still not explicitly named.)
- Whether the learned policy itself is certified, or only the deterministic FSI-resident safety layer around it.
- The Outside-In deploy skill is named `hoisa-deploy-profile` (Trust Center page) vs. `warehouse-deploy` / `halos-deploy` (blog) — reconcile on next update. See [agent skills](../concepts/agents/agent-skills.md).
