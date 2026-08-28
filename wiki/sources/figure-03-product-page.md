---
title: Figure 03 product page (figure.ai/figure)
type: source
url: https://www.figure.ai/figure
author: Figure AI
affiliation: Figure AI
published: 2026-08-28
ingested: 2026-08-28
tags: [figure, figure-03, humanoid, specs, vendor-source, primary]
---

> [!note] Why this is filed separately
> Figure's [Figure 03 announcement](figure-03-announcement.md) contains **no absolute specifications** — no height, weight, payload, or runtime. Those numbers live only on this product page. Since they are the ones quoted in every comparison table, they get their own primary rather than being attributed to the announcement they are not in. `published` is the retrieval date; the page is undated and updated in place.

## Summary

Figure's consumer-facing page for [Figure 03](../entities/figure-03.md), retrieved 2026-08-28. Positioning has shifted decisively to the home: *"Figure takes care of household tasks like laundry, cleaning, and doing dishes, all autonomously."* The page carries the only official spec table Figure publishes.

## The official spec table (verbatim)

| Field | Value |
|---|---|
| Height | 5'8" (~173 cm) |
| Payload | 20 kg |
| Weight | 61 kg |
| Runtime | 5 hr |
| Speed | 1.2 m/s |
| System | Electric |

That is the complete list. **No DOF count, no reach, no compute, no price, no availability date, no degrees of freedom in the hands, no operating temperature.**

## Key claims

- *"Figure takes care of household tasks like laundry, cleaning, and doing dishes, all autonomously"* — stated flatly, in present tense, on the top-level product page.
- *"After meaningful progress in the workforce, Figure is now moving into the home."*
- *"Engineered for real homes, Figure navigates stairs, tight corners, and shifting layouts with ease"* — the stairs claim is the marketing form of the perception-conditioned S0 capability described in [Ramping Figure 03 Production](figure-ramping-03-production.md).
- Site-wide framing on figure.ai's landing page: *"The future of home help is here."*

## Contradictions

> [!warning] Height: 5'8" vs the 168 cm everyone cites
> 5'8" is **172.7 cm**. Secondary coverage almost universally reports Figure 03 as **168 cm**, which is 5'6" — and 168 cm was the figure attached to *Figure 02*. The likeliest explanation is that the Figure 02 number was carried forward by copy-paste through the secondary ecosystem. Figure's own page says 5'8"; this wiki uses ~173 cm and flags the 168 cm figure as unsourced.

> [!warning] "All autonomously" is doing heavy lifting
> The autonomy demonstrated in Figure's own technical posts is a **4-minute** dishwasher task under controlled conditions ([Helix 02](figure-helix-02.md)). The product page's present-tense claim that Figure 03 does laundry, cleaning and dishes autonomously is not supported by anything Figure has published. Figure 03 is **not purchasable** and CEO statements put home deployment at aspirational-2026.

## Entities mentioned

- [Figure 03](../entities/figure-03.md) · [Figure](../entities/figure.md) · [Helix](../entities/helix.md)

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the household-task framing.
- [VLA models](../concepts/learning/vla-models.md)

## Open questions

- Why does the spec table omit DOF when every competitor publishes it?
- The 20 kg payload equals Figure 02's widely-cited payload despite 9% less mass — is it a real re-rating or an inherited number?
