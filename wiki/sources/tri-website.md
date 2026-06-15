---
title: Toyota Research Institute — Website (tri.global)
type: source
url: https://www.tri.global/
author: Toyota Research Institute
published: continuously updated
ingested: 2026-05-09
tags: [tri, toyota-research-institute, organization, robotics, automated-driving, lbm]
---

> [!note] Ingest depth
> Lightweight ingest of the TRI homepage (mission statement + research-area list). LBM (Large Behavior Model) and other named robotics initiatives are referenced in *other* ingested sources but were not surfaced on the TRI homepage we fetched.

## Summary

**Toyota Research Institute (TRI)** — Toyota's R&D arm; subsidiary of Toyota Motor Corporation. Headquarters in Los Altos, CA; second site in Cambridge, MA. Five published research focus areas: **Automated Driving Advanced Development; Energy & Materials; Human-Centered AI; Human Interactive Driving; Robotics**. TRI is the institutional home of one of the strongest US academic-industry robotics-research hybrids — recurring author affiliation across the [Diffusion Policy](../entities/diffusion-policy.md) and [UMI](../entities/umi.md) papers (Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Russ Tedrake), and (via citations elsewhere in the wiki) home of **TRI LBM** (Large Behavior Model), referenced as a baseline in the [RoboCasa365 Paper](robocasa365-paper.md).

## Mission (verbatim)

> "TRI's mission is to create new tools and capabilities focused on improving the human condition."

## Research areas (from homepage)

1. **Automated Driving Advanced Development** — safe, scalable, inclusive automated driving solutions.
2. **Energy & Materials** — zero-emissions mobility materials.
3. **Human-Centered AI** — human behavior prediction; human-AI collaboration.
4. **Human Interactive Driving** — driver experience enhancement.
5. **Robotics** — described on the homepage as *robotics that amplify human capabilities*.

The recently-highlighted initiatives mentioned on the homepage include **ChargeMinder** (behavioral science applied to EV charging) and **Atlas robot development** (humanlike movement through single AI models). Note: this Atlas reference may collide with [Boston Dynamics' Atlas](../entities/atlas.md) or be unrelated; the TRI homepage didn't disambiguate. Treat as a TBD until confirmed.

## TRI in the wiki's robotics literature

TRI shows up consistently across the cross-institutional robotics-foundation-model line:

- **[Diffusion Policy Paper](diffusion-policy-paper.md)**: Eric Cousineau, Benjamin Burchfiel, Siyuan Feng — TRI co-authors with Cheng Chi (Columbia), Yilun Du (MIT), and Shuran Song (Columbia).
- **[UMI Project Page](umi-paper.md)**: Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, **Russ Tedrake** — same TRI cohort, now also with Tedrake (TRI VP of Robotics Research, MIT).
- **TRI LBM (Large Behavior Model)** — referenced in [RoboCasa365 Paper](robocasa365-paper.md) as a baseline. Not a primary ingest yet; TBD.
- **Drake** — TRI/MIT's open-source robot simulation and dynamics library; on the wiki's TBD list.

The pattern: TRI is consistently the *industrial arm* of academic robotics-foundation-model research — not the lead author, but the resourcing partner that puts grad students on Franka arms in real-world environments, alongside MIT/Stanford/Columbia.

## Why it matters in this wiki

- **Co-affiliation hub** — TRI co-authorship recurs across [Diffusion Policy](../entities/diffusion-policy.md) and [UMI](../entities/umi.md), and surfaces as a referenced baseline (LBM) in [RoboCasa365](../entities/robocasa.md). One entity page consolidates that.
- **TRI LBM as future ingest** — TRI's Large Behavior Model is a credible counterpart to NVIDIA GR00T / Pi VLAs in the generalist-policy landscape; primary source not yet filed.
- **Russ Tedrake's TRI VP role** — Tedrake's MIT affiliation and the wiki's interest in Drake/Pinocchio-style model-based control would intersect through TRI.

## Open questions / TBD

- **TRI LBM primary source** — referenced but not ingested. Likely substantial enough for its own source page.
- **Drake (Tedrake's library)** — open-source TRI/MIT simulation library; TBD entity page.
- **Russ Tedrake** — entity page; senior figure across TRI publications, MIT robot-locomotion line.
- **TRI Atlas robot development** — homepage references "Atlas robot development through single AI models"; unclear whether this overlaps with Boston Dynamics Atlas or is separate. Needs verification.
- **Founding year and leadership** — homepage didn't surface; could be added on a deeper fetch.

## Mentioned in

- [Diffusion Policy Paper](diffusion-policy-paper.md) — TRI co-authors.
- [UMI Project Page](umi-paper.md) — TRI co-authors.
- [RoboCasa365 Paper](robocasa365-paper.md) — TRI LBM as baseline.
