---
title: Robot safety standards (ISO 13482 and the machinery-safety framework)
type: concept
created: 2026-07-08
updated: 2026-08-03
sources: 14
tags: [iso-13482, iso-10218, ts-15066, safety-standards, certification, ce-marking, service-robots, personal-care-robots, assistive, regulation, functional-safety, nvidia-halos]
---

# Robot safety standards (ISO 13482 and the machinery-safety framework)

The international machinery-safety framework for robots that operate **near untrained people** — centered on **ISO 13482**, the first safety standard (2014) for robots in close contact with the general public. Everything earlier (the ISO 10218 industrial family) assumed a fenced robot or a trained operator. This page is web-researched (2026-07-08, sparked by the [awesome-physical-ai gap analysis](../../sources/awesome-physical-ai-github.md)); no primary standard document has been ingested — ISO standards are paywalled, so claims rest on ISO's public abstracts/news, secondary sources, and the ingested [Fosch-Villaronga et al. critique](../../sources/fosch-villaronga-iso13482-exoskeletons.md) (which quotes the standard's clauses directly).

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
- A decade in: **dozens of certified robots, not thousands**.

## The documented gaps (Fosch-Villaronga et al., 2023)

The [primary academic critique](../../sources/fosch-villaronga-iso13482-exoskeletons.md) (Leiden eLaw, *Technology in Society* 2023; systematic review of 71 works, exoskeleton-focused) classifies the 2014 standard's deficiencies into **six areas** — missing hazards (cognitive/psychological, overtrust, third parties, travel instability), insufficient requirements, **scarce V&V methods** (no test measures or usable HRI models — no defined way to *demonstrate* conformity), incomplete information-for-use, missing normative references, and confusing language — plus structural problems: "personal care" never defined, the **medical-device boundary** unclear, function-based categories too heterogeneous (they argue for per-category standards), and a **narrow physical-safety focus** that drops privacy, cognitive accessibility, and gender considerations that materially affect safety. The 2025 revision's restructuring-by-robot-type responds directly to the per-category argument; how much else it closes is an open question on the [source page](../../sources/fosch-villaronga-iso13482-exoskeletons.md).

## The looming collision with learned policies

> [!note] Open frontier
> The standard's machinery assumes **deterministic, verifiable safety functions**; everything this wiki tracks ([VLAs](../learning/vla-models.md), [LBMs](../learning/large-behavior-models.md), learned locomotion) is a stochastic learned policy. How a [GR00T](../../entities/nvidia-groot.md)-driven mobile servant robot demonstrates ISO 13482 conformity is essentially unresolved — the practical pattern is likely a certified classical **safety layer** (protective stops, speed/force limiting, geofencing) wrapping an uncertified learned policy. Connects directly to [Tedrake](../../entities/russ-tedrake.md)'s "deployment is the milestone the field has to *earn*" thesis and the EU Machinery Regulation's incoming AI requirements.

A concrete instance of that predicted pattern arrived 2026-07-15: **[NVIDIA Halos](../../entities/nvidia-halos.md)** ([Halos for Robotics](../../sources/nvidia-halos-robotics.md)) — a **full-stack functional-safety system** (silicon → OS → middleware → apps) running on the **IGX [Thor](../../entities/jetson-thor.md)** SoM with a hardware **Functional Safety Island**, i.e. a deterministic safety layer *underneath* the learned VLA the same module runs. It splits safety into **Inside-Out** (onboard sensors, immediate envelope — [Agility Digit](../../entities/digit.md) is the flagship) and **Outside-In** (external cameras / virtual zones). Crucially it brings a **certification pathway**: the *"first ANAB-accredited inspection program for AI functional safety in physical AI,"* the Halos AI Systems Inspection Lab, and third-party notified bodies (TÜV Rheinland) — porting **autonomous-vehicle-grade** safety heritage. Two caveats remain: (1) Halos certifies the **deterministic envelope**, not obviously the stochastic policy itself, so ISO 13482 / EU-MR conformity *of the learned policy* is still unresolved; (2) Halos is **physical** safety only — it is disjoint from the *semantic*-harm layer below.

## Related concepts

- [Assistive robotics](assistive-robotics.md) — the deployment domain where this standard bites first (in-home robots near vulnerable users).
- [Levels of autonomy in assistive robotics](../../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) — autonomy level determines which safety functions must be machine-side.
- [VLA models](../learning/vla-models.md) / [Large behavior models](../learning/large-behavior-models.md) — the learned-policy side of the collision above.
- [AI guardrails](../safety/ai-guardrails.md) — **the other safety layer, and a disjoint one.** ISO 13482 governs *physical* harm via deterministic safety functions; LLM guardrails govern *semantic* harm via learned text classifiers. Neither knows the other exists. A robot that satisfies ISO 13482 will not crush you; nothing in the standard stops an [LLM planner](../agents/llm-agent-architecture.md) from deciding to throw away your medication. No ingested source bridges the two.

## Current state

ISO 13482 remains the only game in town for non-industrial robot safety certification, but uptake is a trickle and the 2025 service-robot reframe is its bid for relevance in the delivery/commercial wave. No ingested source yet documents a learned-policy robot achieving certification. Watch items: final publication of the revision; EU Machinery Regulation application (2027-01); any VLA-era certification precedent.

## Mentioned in

- [Fosch-Villaronga et al. — ISO 13482 and robotic exoskeletons](../../sources/fosch-villaronga-iso13482-exoskeletons.md) — **primary source for the documented-gaps section**.
- [NVIDIA Halos for Robotics](../../sources/nvidia-halos-robotics.md) — the productized functional-safety layer ([NVIDIA Halos](../../entities/nvidia-halos.md)) + ANAB/TÜV certification pathway.
- [awesome-physical-ai (GitHub list)](../../sources/awesome-physical-ai-github.md) — the governance/standards gap that prompted this page.
- [ASIMOV Benchmark paper](../../sources/asimov-benchmark-paper.md) — argues robotics safety was "predominantly about collision avoidance and hazard reduction," and that VLM-driven robots need a **[semantic safety](../safety/semantic-safety.md)** layer the standards tradition does not cover.
- [Responsibly advancing AI and robotics](../../sources/deepmind-gemini-robotics-safety-page.md) — places the standards tradition as the *physical* layer of three.
- [Gemini Robotics 2: Safety Evaluations](../../sources/gemini-robotics-2-safety-report.md) — the wiki's best single map of the applicable standards: **ISO 10218:2025** (absorbing ISO/TS 15066's SRMS / hand-guiding / SSM / PFL modes), **ISO 13482** plus the **forthcoming ISO 25785-1** for humanoid and dynamically stable robots, **ISO 13855** (separation distance), **ISO 13849-1** (stop-function integrity), **IEC 60204-1** (stop categories; Category 2 retains power to hold pose).
