---
title: Aging in place
type: concept
created: 2026-07-13
updated: 2026-07-13
sources: 1
tags: [aging-in-place, elder-care, assistive-robotics, adl, iadl, home-modification, caregiving, demand-side]
---

**Aging in place** — *"staying in your own home as you get older"* ([NIA](../../sources/nia-aging-in-place.md)), rather than moving to assisted living or a nursing home. It is the stated goal of most older adults ("stay in their own home, maintain independence for as long as possible, turn to family and friends for help when needed") and the **demand-side context** that motivates a large fraction of the assistive-robotics work this wiki tracks. This page exists to make that motivation explicit: the tasks assistive robots try to automate are, largely, the in-home-care tasks the aging-in-place literature enumerates.

## The in-home task taxonomy (what help is needed at home)

The [NIA guide](../../sources/nia-aging-in-place.md) lists the categories of help older adults receive at home. Split into the standard clinical framing:

**Activities of Daily Living (ADLs)** — intimate self-care:
- Bathing, dressing, grooming, using the toilet, eating, **transfers / mobility** (e.g. bed → chair).

**Instrumental Activities of Daily Living (IADLs)** — managing the household:
- Household chores (cleaning, laundry, yard work, grocery shopping), meal shopping + preparation, money management (bills, insurance forms), transportation, medication/health-care management.

Plus **safety** — home safety features and response to falls or emergencies.

> [!note] Where robots do and don't help today
> Current mobile-manipulation research overwhelmingly targets **IADLs** (fetch, pick-and-place, tidying, meal-adjacent tasks) — see [OK-Robot](../../entities/ok-robot.md), [Robot Utility Models](../../entities/robot-utility-models.md), [HomeRobot/OVMM](../../sources/ovmm-homerobot.md). The intimate **ADLs** (bathing, dressing, toileting) — which drive the *need* for a caregiver and often the decision to leave home — are exactly the domains the [PAR review](../../sources/nanavati2024-physically-assistive-robots-review.md) flags as **underserved**. Feeding is the one ADL with sustained robotics attention ([Nanavati feeding system](../../sources/nanavati2025-feeding-out-of-lab.md), [Kinova Jaco](../../entities/kinova-jaco.md)). See [underserved PAR domains](../../syntheses/assistive/underserved-par-domains.md).

## Who provides the help, and what it costs

- **Informal caregivers** (family, friends, neighbors) are the primary source, supplemented by formal caregivers and community services ([NIA](../../sources/nia-aging-in-place.md)). Assistive robots are implicitly proposed as a supplement to — not replacement for — this informal-care layer.
- **Cost framing:** home-based care can be expensive but "may cost less than moving into a residential facility." This is the economic argument an in-home robot has to beat or complement (personal funds / Medicare / Medicaid / VA / long-term-care insurance).

## Technology's near-absence in the mainstream guidance

Notably, the 2023 NIA guide's *only* named technology is **emergency medical alert systems** (wearable fall/lost-detection monitors). It mentions **no assistive robots, no smart-home automation, no AI** — a gap between mainstream elder-care guidance and the research frontier this wiki covers. (An [NIH in-home-technology initiative](https://www.nia.nih.gov/news/nih-initiative-tests-home-technology-help-older-adults-age-place) exists but is not ingested.) This grounds a recurring wiki theme: the reliability bar for a robot to enter this setting is set by *safety and independence*, not task throughput ([assistive robotics](assistive-robotics.md)).

## Related concepts

- [Assistive robotics](assistive-robotics.md) — the field building robots for these tasks.
- [Levels of autonomy in assistive robotics](../../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) — aging-in-place users often prefer *assistive autonomy* (staying in control) over full autonomy.
- [Long-term in-home robot deployments](../../syntheses/assistive/long-term-in-home-robot-deployments.md) — what the longitudinal record of robots-in-real-homes actually shows.
- [Robot safety standards (ISO 13482)](robot-safety-standards.md) — the certification pathway for robots operating in the home near older/impaired users.

## Key references

- [Aging in Place: Growing Older at Home (NIA)](../../sources/nia-aging-in-place.md) — the anchor source; NIH consumer guide (reviewed 2023-10-12).

## Mentioned in

- [Aging in Place: Growing Older at Home (NIA)](../../sources/nia-aging-in-place.md)
