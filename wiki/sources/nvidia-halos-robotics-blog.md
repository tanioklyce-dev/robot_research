---
title: "Inside NVIDIA Halos for Robotics: A Full-Stack Functional-Safety System for Physical AI (developer blog)"
type: source
url: https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/
author: Suhas Hariharapura Sheshadri, Riccardo Mariani, Samuel Ochoa, Deep Rodge, Sarah Todd (NVIDIA)
published: 2026-06-22
ingested: 2026-07-16
tags: [nvidia-halos, functional-safety, robot-safety, igx, jetson-thor, iec-61508, qnx, holoscan, metropolis, anab, tuv, outside-in, certification, physical-ai]
---

## Summary

The **technical deep-dive** companion to the [Halos for Robotics AI Trust Center page](nvidia-halos-robotics.md), authored by NVIDIA's functional-safety team (incl. **Riccardo Mariani**). It reframes [NVIDIA Halos](../entities/nvidia-halos.md) as a **three-layer** safety framework — **Platform/Hardware → Software → Ecosystem** — and puts hard numbers on each: **IGX Thor** silicon safety (IEC 61508 **SIL 3**-capable Functional Safety Island, **22,000+ safety mechanisms**), **Halos OS** (Linux + optional QNX partitioning), and the **ANAB-accredited AI Systems Inspection Lab** certification pathway. It also fully specifies the **Outside-In Safety Blueprint** pipeline (SIPP → SAIM → SEI → SDM) that the wiki previously only had from the [GitHub repo](halos-outside-in-safety-github.md).

## Key claims

### Three-layer framework
1. **Platform/Hardware** — IGX Thor + Holoscan Sensor Bridge.
2. **Software** — Halos OS / Halos Core.
3. **Ecosystem** — AI Systems Inspection Lab certification pathway.

> [!note] Layer-count framing
> The [AI Trust Center page](nvidia-halos-robotics.md) presents Halos as **4 layers** (Platform / OS / Middleware+Apps / Ecosystem); this blog collapses to **3** (Platform / Software / Ecosystem). Same stack, different granularity — not a contradiction.

### IGX Thor (hardware safety)
- **Up to 2,070 FP4 TFLOPS**, 14× Neoverse ARM cores, **128 GB @ 273 GB/s**.
- **Functional Safety Island (FSI)**: IEC 61508 **SIL 3**-capable, isolated, **up to 12K DMIPS** with its own I/O/power/clocks.
- **22,000+ safety mechanisms** across the SoC; IEC 61508 **SC 3** systematics on all safety IP.
- Diversity/redundancy (GPU/CPU, GPU/PVA, CCPLEX/FSI pairings); In-System Test (Logic + Memory BIST); freedom-from-interference (SMMU, GPU watchdog, NOC firewalls).

### Holoscan Sensor Bridge (HSB)
- Extends the safety chain to edge sensors over Ethernet; ConnectX RDMA + RTX GPU Direct; **end-to-end IEC 61508 SIL 2** protocol with watermarking; MACsec device auth/encryption. FPGA IP: sensor control, packetization, watermarking, MACsec.

### Halos OS (software safety)
- Built on NVIDIA's AV-safety foundation: **18,000 engineering-years**, **21 billion safety transistors assessed**, **7M lines of safety-assessed code**.
- **Two configs**: *Halos Core Linux* (Safety Extension Package + Edge Safety Link + FSI/Safety-MCU firmware) and *Halos Core Linux + QNX* (NV Hypervisor partitions Linux-for-AI from QNX-for-safety-critical).
- Ecosystem partners: **BlackBerry QNX**, Acontis (EtherCAT/FSoE), FreeRTOS (AWS safety bundle planned).

### Outside-In Safety Blueprint pipeline
- **SIPP** (Sensor Input Processing Pipeline) — Metropolis/**VSS** ingests facility cameras → detect/track → discrete events (ROI entry/exit, proximity, tripwire).
- **SAIM** (Safety AI Monitor) — watches perception for OOD inputs / camera blockage / connectivity loss → forces fallback.
- **SEI** (Safety Event Integrator) — fuses multi-camera events, confidence thresholds, discards stale events.
- **SDM** (Safety Decision Maker) — a **finite state machine on the IGX FSI** (isolated from main AI) that stops/slows/conditionally-mutes onboard safety when clear.
- **Digital-twin validation** via RTX Pro + [Isaac Sim](../entities/nvidia-isaac-sim.md) (synthetic camera streams, HIL).
- Reference use case: **Automated Trailer Loading** — mute onboard safety for full-speed forklift operation *only* while the trailer is worker-free; reinstate instantly on worker ROI entry.
- **Deploy skills** (LLM-based): **`warehouse-deploy`** and **`halos-deploy`** automate prerequisites, NGC downloads, config, VSS integration.

### Certification & ecosystem
- **Halos AI Systems Inspection Lab** = **ANAB-accredited ISO/IEC 17020 Inspection Body** — first worldwide accredited for AI + functional safety across **both AV and robotics**. Partners get an NVIDIA Inspection Certificate to present to a notified body (**TÜV Rheinland/SÜD, SGS, exida, CERTX, UL**) → avoid re-certifying the platform.
- **43+ ecosystem members** (16 automotive, 23 robotics, 4 cross-domain).
- **Standards leadership**: IEC 61508 **Convenor**; ISO/IEC TS 22440 **co-Convenor**; IEC TC 65 AhG 30; ISO 25785-1.
- Named robotics partners: **[Agility Robotics](../entities/digit.md)** (IGX Thor + Halos OS in Digit's safe human-detection; joining the Lab), **Boston Dynamics** (ecosystem), KION, Infineon, TI, NXP, Lattice, Ouster, FORT Robotics, Peer Robotics, and others.

## Entities mentioned

- [NVIDIA Halos](../entities/nvidia-halos.md) — the system
- [Jetson Thor](../entities/jetson-thor.md) (IGX Thor), [Digit](../entities/digit.md) / [Boston Dynamics](../entities/boston-dynamics.md), [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)

## Concepts touched

- [Robot safety standards (ISO 13482)](../concepts/robotics/robot-safety-standards.md) — this blog names the *actual* standards Halos targets (IEC 61508, ISO 26262, ISO 13849, ISO/IEC TR 5469, ISO 25785-1), answering the entity's old open question
- [Agent skills (portable SKILL.md)](../concepts/agents/agent-skills.md) — `warehouse-deploy` / `halos-deploy`

## Open questions

- Still unresolved: whether the **learned policy** itself is ever certified, or only the deterministic FSI-resident safety layer around it (the blog certifies the *platform + safety application*, not the AI policy).
- The AI-Trust-Center page named the Outside-In deploy skill `hoisa-deploy-profile`; this blog names `warehouse-deploy` + `halos-deploy` — likely multiple/renamed skills; worth reconciling on next Halos update.
