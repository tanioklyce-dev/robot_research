---
title: NVIDIA Halos (for Robotics)
type: entity
subtype: product
created: 2026-07-15
updated: 2026-09-07
sources: 5
tags: [nvidia-halos, functional-safety, riccardo-mariani, iso-iec-ts-22440, iso-iec-tr-5469, robot-safety, igx, jetson-thor, physical-ai, qnx, holoscan, certification, anab, tuv, outside-in, metropolis]
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

The **first ANAB-accredited inspection program for AI functional safety in physical AI** (ISO/IEC 17020 Inspection Body, first worldwide accredited across **both AV and robotics**); the **Halos AI Systems Inspection Lab** issues an Inspection Certificate partners present to a notified body (**TÜV Rheinland/SÜD, SGS, exida, CERTX, UL**), so they avoid re-certifying the platform. **43+ ecosystem members** (16 automotive, 23 robotics, 4 cross-domain), incl. **[Boston Dynamics](boston-dynamics.md)**, KION, Infineon, TI, NXP, Ouster, FORT Robotics. NVIDIA holds **standards-leadership** roles — **corrected 2026-09-07**: [Riccardo Mariani](riccardo-mariani.md) is **co-convenor of MT 61508** (maintaining IEC 61508) and **convenor** of **ISO/IEC JTC 1/SC 42/JWG 4**, the group that owns **ISO/IEC TS 22440**, of which he is also project leader — this page previously had the "co-" attached to the wrong standard. Also IEC TC 65 AhG 30, ISO 25785-1 — targeting IEC 61508 / ISO 26262 / ISO 13849 / ISO/IEC TR 5469 / ISO 25785-1 ([blog](../sources/nvidia-halos-robotics-blog.md)), which answers the old "which standards?" open question.

## What the Mariani interview adds (2026-09-07)

The wiki's first non-marketing source on Halos is [an interview with the person who runs it](../sources/industrial-ai-podcast-nvidia-safety-strategy.md). It corroborates the architecture above and adds four things.

**The runtime supervisor, described as a mechanism.** Around an AI perception pipeline sit *"a combination of monitors, let's say scaffolding"*, and a supervisor — runtime software designed to **IEC 61508** and **ISO 13849** — that checks the pipeline's inputs and outputs, **evaluates the uncertainty the model reports**, judges whether the perception output is accurate enough, and only then *"gives a green light."* So Halos filters **perception**, one stage earlier than a [safety filter](../concepts/robotics/safety-filters.md) filters action, and its admissibility test is **model uncertainty** rather than set invariance. That makes uncertainty estimation a certified-path dependency — awkward against the [contact-rich survey](../sources/safe-learning-contact-rich-survey.md)'s finding that current foundation models have *"weak uncertainty estimation."*

**What MUTE/UNMUTE is actually for.** The Outside-In blueprint's mute decision reads like a safety *reduction* until you have the use case. Mariani's: an autonomous forklift entering a trailer may **mute its safety function** to work faster inside, and re-enable it when *"people start to be around, maybe around the corner."* The infrastructure's job is not only to stop the robot — it is to **license it to go faster where nobody is**, which is where the productivity argument for outside-in sensing actually lives.

**The standards line, from its convenor.** **ISO/IEC TR 5469** (published; the first international report on AI functional safety, he was editor) → **ISO/IEC TS 22440** (the requirements standard, he convenes it; *"will be published next year"*, i.e. ~2027), with **ISO/PAS 8800** as the automotive equivalent and **IEC 62998** supplying the sensor failure rates. TS 22440 carries an annex on **AI tools**, covering simulation tooling and the accuracy you must demonstrate for it. See [robot safety standards](../concepts/robotics/robot-safety-standards.md).

**A prediction, and a concession.** Certification bodies will need *"kind of an assessment lab that is more so digital"* — synthetic data generation and simulation alongside physical labs — because demonstrating IEC 62998-class failure rates from real-world data *"may take a while"*; NVIDIA published a **CVPR tech brief** on a Halos safety evaluation framework toward this. But asked whether simulation removes real testing: ***"I would say no. That, I think, everyone is clear."***

> [!note] "An independent organization within NVIDIA"
> Mariani's own description of the [inspection lab](#certification) flow, using **Agility** as the example: NVIDIA inspects whether a partner's Halos integration was completed correctly *"using an independent organization within NVIDIA,"* and that inspection certificate becomes an input the notified body relies on. His justification is sound — *"this system are so complex that a very high level analysis will never reveal the issue"* — and ANAB accreditation to ISO/IEC 17020 is a recognized structure for in-house inspection bodies. It is still worth naming the shape plainly: **the platform vendor is now part of the certification chain for the platform it sells**, and no source states a rejection rate.

**Also stated**: Halos targets **machinery**, not only robots (designed to ISO 13849; partners *"in the PLC world"* integrating PLC functions; a soft PLC can run alongside the AI pipeline; the partners are *"the traditional guys… many of them"*, unnamed). And NVIDIA presents **VLMs/VLAs as "safety reasoners"** and *"safety judges"*, naming [Alpamayo](alpamayo.md) — the one claim here the wiki has substantial counter-evidence against.

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
- [Industrial AI Podcast #352 — NVIDIA's safety strategy](../sources/industrial-ai-podcast-nvidia-safety-strategy.md) — **the first non-vendor-authored source**: [Mariani](riccardo-mariani.md) on the supervisor mechanism, the standards line, the inspection-lab structure, and the limits of simulation.

## Open questions

- ~~Exact ISO/IEC standards targeted~~ — **answered** by the [blog](../sources/nvidia-halos-robotics-blog.md): IEC 61508 (primary), ISO 26262, ISO 13849, ISO/IEC TR 5469, ISO 25785-1. (ISO 13482/10218 service/industrial still not explicitly named.)
- Whether the learned policy itself is certified, or only the deterministic FSI-resident safety layer around it. **Sharpened 2026-09-07**: NVIDIA now offers [Alpamayo](alpamayo.md), an open reasoning VLA, as a *safety* component — so the question is no longer only "is the policy certified" but "does a learned model sit **inside** the certified envelope or advise it from outside," and the interview does not say.
- **Does the ANAB inspection ever fail anyone?** A vendor-internal accredited inspection feeding an external notified body is only as informative as its rejection rate. No source states one.
- **The CVPR tech brief on the Halos safety evaluation framework** is named by Mariani and not located.
- The Outside-In deploy skill is named `hoisa-deploy-profile` (Trust Center page) vs. `warehouse-deploy` / `halos-deploy` (blog) — reconcile on next update. See [agent skills](../concepts/agents/agent-skills.md).
