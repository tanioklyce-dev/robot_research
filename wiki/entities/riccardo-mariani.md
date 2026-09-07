---
title: Riccardo Mariani
type: entity
subtype: person
created: 2026-09-07
updated: 2026-09-07
sources: 1
tags: [riccardo-mariani, nvidia, functional-safety, halos, iso-iec-tr-5469, iso-iec-ts-22440, iec-61508, standards, certification, ieee]
---

# Riccardo Mariani

Head of Industry Safety at **NVIDIA** — he introduces himself on the [Industrial AI Podcast](../sources/industrial-ai-podcast-nvidia-safety-strategy.md) as *"VP of Industry Safety"* — leading the **[Halos](nvidia-halos.md)** initiative across automotive and robotics, plus NVIDIA's Technical Compliance and Certification team.

## Why he has a page

Because he occupies both sides of a boundary this wiki cares about: **he runs the safety programme of the company selling the platform, and he convenes the ISO/IEC group writing the standard that platform will be certified against.**

| Role | Body |
|---|---|
| **Convenor** | ISO/IEC JTC 1/SC 42/**JWG 4** — functional safety and AI systems |
| **Project leader / editor** | **ISO/IEC TR 5469** (published; the first international report on AI functional safety) and **ISO/IEC TS 22440** (the requirements standard built on it) |
| **Co-convenor** | MT 61508-1/2 — maintenance of **IEC 61508**, the base functional-safety standard |
| **Chair** | IEEE Functional Safety Standards Committee |
| Leads | NVIDIA Halos; NVIDIA TCC (compliance & certification) |

That is not a criticism — functional safety has always been written by the people who build the systems, and the alternative is standards authored by people who have never shipped one. But it is the reason his statements about **what TS 22440 will require** carry unusual weight, and the reason the wiki records them as *a convenor's account of a standard in progress* rather than as vendor claims.

> [!note] A correction this source forced
> The wiki's [Halos page](nvidia-halos.md) recorded NVIDIA holding *"IEC 61508 Convenor, ISO/IEC TS 22440 co-Convenor."* The roles are the other way around: **co-convenor of MT 61508**, **convenor** of the JWG 4 group that owns TS 22440. Fixed.

## Positions worth attributing to him

From the [podcast](../sources/industrial-ai-podcast-nvidia-safety-strategy.md):

- **"We want to get safety and AI good friends."** The programme thesis: AI has been treated as safety's adversary because it is non-deterministic and non-transparent; the response is architectural, not rhetorical.
- **Safety is a value driver, not a compliance cost** — because the autonomous systems the market wants require both AI and safety, so compatibility is what opens the market.
- **The classical pillars survive.** *"The use of AI and safety is new, but the principle of safety — redundancy and diversity, monitoring and validation — are still the key pillar."* Certified sensors, actuators, safety PLCs and MCUs, and the safety fieldbus protocols all remain.
- **Certification bodies will need a digital assessment lab** — synthetic data generation and simulation alongside their physical labs — because demonstrating IEC 62998-class failure rates from real-world data *"may take a while."*
- **But simulation does not replace real testing.** Asked directly: *"can we get rid of tests in the real world — I would say no."*
- **VLMs and VLAs as "safety reasoners" and "safety judges,"** with [Alpamayo](alpamayo.md) as the instance — the claim the wiki has the most counter-evidence against; see the [source page](../sources/industrial-ai-podcast-nvidia-safety-strategy.md) and [semantic safety](../concepts/safety/semantic-safety.md).

## Related

- [NVIDIA Halos](nvidia-halos.md) — the programme he leads.
- [Alpamayo](alpamayo.md) — the open reasoning-VLA family he cites as a safety-designed model.
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — TR 5469 and TS 22440 are now on that page because of this source.
- [Arash Ajoudani](arash-ajoudani.md) — the academic interaction-control tradition; the two lines meet at ISO 13849 / ISO/TS 15066 and nowhere else in this wiki.

## Mentioned in

- [Industrial AI Podcast #352 — NVIDIA's safety strategy](../sources/industrial-ai-podcast-nvidia-safety-strategy.md) — the interview; the source for everything on this page.
