---
title: Robot safety standards (ISO 13482 and the machinery-safety framework)
type: concept
created: 2026-07-08
updated: 2026-07-08
sources: 1
tags: [iso-13482, iso-10218, ts-15066, safety-standards, certification, ce-marking, service-robots, personal-care-robots, assistive, regulation]
---

# Robot safety standards (ISO 13482 and the machinery-safety framework)

The international machinery-safety framework for robots that operate **near untrained people** — centered on **ISO 13482**, the first safety standard (2014) for robots in close contact with the general public. Everything earlier (the ISO 10218 industrial family) assumed a fenced robot or a trained operator. This page is web-researched (2026-07-08, sparked by the [awesome-physical-ai gap analysis](../../sources/awesome-physical-ai-github.md)); no primary standard document has been ingested — ISO standards are paywalled, so claims below rest on ISO's public abstracts/news and secondary sources.

## ISO 13482 in brief

- **ISO 13482:2014 — "Safety requirements for personal care robots"** ([ISO catalog](https://www.iso.org/standard/53820.html)). A machinery-safety *type-C* standard: conformity = an **ISO 12100-style risk assessment** against its hazard catalog (motion/collision, energy storage & charging, shape/edges, stability, localization errors, hazards from *autonomous decisions*, and — unusually — **psychological harm**), plus safety-related control functions (protective/emergency stops, speed/force limits, stability monitoring) at appropriate functional-safety integrity levels.
- **Three robot categories (2014)**: **mobile servant robot** (mobile manipulators in human environments — where a [Stretch](../../entities/stretch.md) or [XLeRobot](../../entities/xlerobot.md) would fall), **physical assistant robot** (worn/coupled — exoskeletons), **person carrier robot**. Out of scope: >20 km/h, toys, flying/waterborne, industrial (→ ISO 10218), **medical devices** (a therapeutic exoskeleton is regulated as a medical device instead), military.
- **2025 revision — retitled "Safety requirements for *service robots*"** ([ISO/FDIS 13482](https://www.iso.org/standard/83498.html); DIS voted 2024-11, FDIS registered 2025-06, approval slated 2025-07; final publication unconfirmed as of 2026-07-08). Expands from "personal care" to service robots in personal *and* professional/commercial use, restructures requirements **by robot type**, drops the person-carrier clauses. The retitle tracks where the market actually went: delivery/commercial service, not care.

## The surrounding framework

| Standard | Domain | Status |
|---|---|---|
| ISO 13482 | Personal-care → **service robots** | 2014; revision at FDIS (2025) |
| ISO 10218-1/-2 | Industrial robots / integration | **:2025 editions published**; ISO/TS 15066 (collaborative robots) folded into 10218-2:2025 |
| EU Machinery Regulation 2023/1230 | CE-marking legal basis (replaces Machinery Directive) | Fully applies **2027-01**; adds AI-relevant requirements |
| ISO 13482-adjacent (not researched) | UL 4600 (autonomous products), ISO 26262 (automotive), ISO 3691-4 (AGVs/AMRs) | see [awesome-physical-ai](../../sources/awesome-physical-ai-github.md) governance section |

CE marking is the commercial lever: **EN ISO 13482 is harmonized** under the EU machinery framework, so certification is the practical gateway to the EU market.

## Certification track record (thin but real)

- **CYBERDYNE HAL exoskeleton** (Tsukuba, JP) — **first ever**, certified by JQA against the *draft* standard, 2013-02 ([ISO news](https://www.iso.org/news/2014/09/Ref1882.html)).
- **Panasonic Resyone** (bed↔wheelchair) — first against the published 2014 standard; **Panasonic HOSPI** (hospital delivery) followed ([Panasonic newsroom](https://news.panasonic.com/global/topics/5001)).
- **Yujin GoCart** — Korea's first, 2021.
- A decade in: **dozens of certified robots, not thousands**; academic criticism of the category scheme as legally confusing (Fosch-Villaronga line of work).

## The looming collision with learned policies

> [!note] Open frontier
> The standard's machinery assumes **deterministic, verifiable safety functions**; everything this wiki tracks ([VLAs](../learning/vla-models.md), [LBMs](../learning/large-behavior-models.md), learned locomotion) is a stochastic learned policy. How a [GR00T](../../entities/nvidia-groot.md)-driven mobile servant robot demonstrates ISO 13482 conformity is essentially unresolved — the practical pattern is likely a certified classical **safety layer** (protective stops, speed/force limiting, geofencing) wrapping an uncertified learned policy. Connects directly to [Tedrake](../../entities/russ-tedrake.md)'s "deployment is the milestone the field has to *earn*" thesis and the EU Machinery Regulation's incoming AI requirements.

## Related concepts

- [Assistive robotics](assistive-robotics.md) — the deployment domain where this standard bites first (in-home robots near vulnerable users).
- [Levels of autonomy in assistive robotics](../../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) — autonomy level determines which safety functions must be machine-side.
- [VLA models](../learning/vla-models.md) / [Large behavior models](../learning/large-behavior-models.md) — the learned-policy side of the collision above.

## Current state

ISO 13482 remains the only game in town for non-industrial robot safety certification, but uptake is a trickle and the 2025 service-robot reframe is its bid for relevance in the delivery/commercial wave. No ingested source yet documents a learned-policy robot achieving certification. Watch items: final publication of the revision; EU Machinery Regulation application (2027-01); any VLA-era certification precedent.

## Mentioned in

- [awesome-physical-ai (GitHub list)](../../sources/awesome-physical-ai-github.md) — the governance/standards gap that prompted this page.
