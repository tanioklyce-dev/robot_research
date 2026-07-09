---
title: "How can ISO 13482:2014 account for the ethical and social considerations of robotic exoskeletons? (Fosch-Villaronga et al.)"
type: source
url: https://doi.org/10.1016/j.techsoc.2023.102387
author: Eduard Fosch-Villaronga, Carlos José Calleja, Hadassah Drukarch (Leiden eLaw), Diego Torricelli (CSIC)
published: 2023-10-13 (Technology in Society 75, art. 102387)
ingested: 2026-07-08
venue: Technology in Society (Elsevier)
license: CC BY 4.0 (open access)
local_path: raw/ISO13482_personalcarerobots_S0160791X23001926-main.pdf
format: paper PDF (21 pp)
tags: [iso-13482, exoskeletons, personal-care-robots, regulation, safety-standards, robot-law, policy, systematic-review, leiden]
---

# How can ISO 13482:2014 account for the ethical and social considerations of robotic exoskeletons?

## Summary

The primary academic critique of [ISO 13482:2014](../concepts/robotics/robot-safety-standards.md) — the "Fosch-Villaronga line" the wiki's concept page previously cited unsourced. Via a **systematic literature review (71 works)**, the Leiden eLaw + CSIC team classifies the standard's **regulatory gaps and inconsistencies** for lower-limb exoskeletons (restraint-type physical assistant robots) into **six areas**, each with concrete policy recommendations (Appendix A): (1) risk scenarios missing from the hazard catalog; (2) insufficient safety requirements; (3) scarce verification & validation methods; (4) inadequate information-for-use provisions; (5) missing normative references; (6) confusing language. Bottom line: the standard was "a substantial step" but **fails to address safety sufficiently and comprehensively**, its category scheme confuses developers, and its **narrow physical-safety focus** ignores cognitive/psychological dimensions that materially affect physical safety. Written while the 13482 revision was in preparatory stage — this critique is part of the context for the [2025 "service robots" reframe](../concepts/robotics/robot-safety-standards.md).

## Key claims

**Structural/scope critiques (§4.1)**
- **"Personal care" is never defined** — the standard defines personal care robots negatively (service robots improving "quality of life," non-medical), making the protected scope unclear; the *medical-device boundary* (therapy/rehab exoskeletons → Medical Devices Regulation instead) is the most consequential and least clear line.
- **Function-based categorization confuses**: person carrier / mobile servant / physical assistant (subdivided **restraint-type** vs **restraint-free** — lower-limb exoskeletons are restraint-type, ISO 13482 §3.15) differ so much in embodiment and risk that shared requirements fit none well; the paper argues for **per-category standards**.
- **Narrow focus on physical safety** — privacy, cognitive accessibility (an unaccommodated cognitive disability makes a certified device unsafe in practice), and **gender/sex considerations** (acknowledged in the standard's drafting, then dropped) are absent though they materially affect safety.

**Missing hazards (§4.2)**
- Close physical HRI not fully covered; no guidelines for safe interaction within personal space; **cognitive/psychological hazards and overtrust ignored**; contact-with-third-parties, travel instability / instability-in-collision, and fatigue/long-term-use hazards absent.

**Missing safeguards & V&V (§4.4–4.6)**
- **No parameters for protective stops**; no provisions for **residual software faults (bugs)**; unsuitable for domain-specific safety functions; lifecycle requirements (incl. recycling/disposal) missing; **no safety test measures, measurement methods, or usable HRI models** for validation — i.e. even a willing developer lacks a defined way to *demonstrate* conformity.

**Context & program**
- ISO 13482 is "the sole European harmonized standard explicitly designed for lower-limb exoskeletons and other robots interacting with users in their daily lives" — which is why its gaps matter beyond pedantry.
- Funded by the **ERC Safe & Sound project** (GA 101076929; robot testbeds + open data + regulator-developer interaction as the proposed policymaking method) and **EUROBENCH** (exoskeleton benchmarking). Future work targets **mobile servant robots** — the category where the wiki's assistive platforms live.

## Entities mentioned

- Eduard Fosch-Villaronga (Leiden eLaw) — the field's leading robot-law/standards scholar; no entity page yet (create if he recurs).
- CYBERDYNE HAL-class lower-limb exoskeletons (the object of study); [RELab tenoexo](relab-ethz-tenoexo.md)-style hand orthoses sit near the same medical-device boundary.

## Concepts touched

- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — **primary source for the critique section**.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the physical-assistant-robot category and the cognitive-accessibility argument.

## Open questions

- How many of the six gap areas the **2025 service-robots revision** actually closes (restructuring by robot type responds directly to the per-category argument; psychological-hazard and V&V coverage unknown) — checkable when the final text publishes.
- Whether Safe & Sound's testbed-based regulatory method produced follow-on outputs (the promised mobile-servant-robot study would be directly relevant to the wiki's assistive line).
- The paper predates the learned-policy wave — its V&V critique (no way to demonstrate conformity) gets *harder*, not easier, with [VLA](../concepts/learning/vla-models.md)-class controllers.
