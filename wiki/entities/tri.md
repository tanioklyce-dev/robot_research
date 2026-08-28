---
title: Toyota Research Institute (TRI)
type: entity
subtype: company
created: 2026-05-10
updated: 2026-08-26
sources: 11
tags: [tri, toyota-research-institute, robotics-research, automated-driving, lbm, drake, organization, walden-robotics, spinout]
---

**Toyota Research Institute (TRI)** — research subsidiary of Toyota Motor Corporation. Headquarters: Los Altos, CA. Second site: Cambridge, MA. Mission: *"create new tools and capabilities focused on improving the human condition."* Houses one of the strongest US industrial-academic robotics research hybrids; recurring co-authorship with Stanford / Columbia / MIT across the [Diffusion Policy](diffusion-policy.md) and [UMI](umi.md) papers, and home of the **TRI LBM (Large Behavior Model)** referenced as a baseline in [RoboCasa365](robocasa.md).

## Drake

TRI **leads core development of [Drake](drake.md)** — the BSD-3 C++/Python model-based design and verification toolbox started at MIT CSAIL ([docs](../sources/drake-documentation.md)), still pushed daily after twelve years. That TRI funds Drake *while* shipping [Large Behavior Models](../concepts/learning/large-behavior-models.md) is the clearest institutional evidence in this wiki that the model-based and learned-policy programs are treated as complementary rather than successive.

## Research areas (homepage)

1. **Automated Driving Advanced Development**.
2. **Energy & Materials**.
3. **Human-Centered AI**.
4. **Human Interactive Driving**.
5. **Robotics**.

The robotics line is the wiki-relevant one; described as *robotics that amplify human capabilities*.

## TRI in this wiki's robotics-foundation-model line

TRI personnel co-author across at least three ingested sources:

- **[Diffusion Policy Paper](../sources/diffusion-policy-paper.md)** (RSS 2023) — Eric Cousineau, Benjamin Burchfiel, Siyuan Feng (TRI) with Cheng Chi (Columbia), Yilun Du (MIT), Shuran Song (Columbia).
- **[UMI Project Page](../sources/umi-paper.md)** (RSS 2024) — Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, **Russ Tedrake** (TRI VP of Robotics Research) — same TRI cohort, with Tedrake added.
- **[RoboCasa365 Paper](../sources/robocasa365-paper.md)** (ICLR 2026) — references **TRI LBM (Large Behavior Model)** as a baseline.

The pattern: TRI is the *industrial resourcing partner* in academic robotics-foundation-model research, not the lead author institution. They put grad students on real Franka arms in real-world environments alongside MIT / Stanford / Columbia.

## Notable TRI projects (referenced or surfaced on homepage)

- **TRI [LBM](../concepts/learning/large-behavior-models.md) (Large Behavior Model)** — generalist robot policy program led by [Russ Tedrake](russ-tedrake.md); "the multitask version of [Diffusion Policy](diffusion-policy.md)" with TRI's role framed as "the **science of LBMs**" — [Automated Podcast, 2026-07](../sources/automated-podcast-tedrake-rocket-ship.md). **[Primary paper now ingested](../sources/tri-lbm-paper.md)** (82 authors, Science Robotics 2026): ~1,700 h pretraining, blind-A/B statistical eval, 3–5× fine-tune data efficiency, smooth scaling. Referenced as a baseline in [RoboCasa365](../sources/robocasa365-paper.md).
- **Drake** — TRI/MIT open-source model-based simulation/dynamics library ([Tedrake](russ-tedrake.md)'s "horcrux"; he still writes production code — [podcast](../sources/automated-podcast-tedrake-rocket-ship.md)). Anchored on the Tedrake entity page.
- **ChargeMinder** — behavioral science for EV charging (homepage).
- **"Atlas robot development" reference on homepage** — homepage mentions Atlas robot development "through single AI models." Unclear whether this overlaps with [Boston Dynamics' Atlas](atlas.md) or refers to a separate TRI Atlas-related effort. Treat as TBD.

## Why it matters in this wiki

- **Co-affiliation hub** — Diffusion Policy, UMI, and (referenced) LBM converge here. Single entity page consolidates the cross-references.
- **[Russ Tedrake](russ-tedrake.md)** (with his own entity page) bridges MIT robot-locomotion research (Drake, model-based control) and TRI's data-driven robotics line; title reported as Senior VP of Large Behavior Models (earlier VP of Robotics Research). **The "TRI LBM talent flowing outward" watch has now resolved into a spin-out**: the LBM program's leadership — Tedrake plus [Ben Burchfiel](ben-burchfiel.md), [Siyuan Feng](siyuan-feng.md), Adrien Gaidon, and Rares Ambrus — left to found **[Walden Robotics](walden-robotics.md)** (spun out of TRI Jan 2026, launched 2026-07-15, $300M/$1.1B). Toyota Motor Corp + three Toyota-linked funds co-led the round, so TRI/Toyota remains a close partner and anchor investor rather than a severed tie.
- **TRI LBM as future ingest** — TRI's generalist policy program is a credible counterpart to [NVIDIA GR00T](nvidia-groot.md), [Physical Intelligence](physical-intelligence.md)'s π0 line, and [Gemini Robotics](gemini-robotics.md). Promotion to a primary source page would substantially strengthen the VLA/generalist-policy synthesis.

## Related

- [Diffusion Policy](diffusion-policy.md) — TRI co-authored.
- [UMI](umi.md) — TRI co-authored.
- [RoboCasa](robocasa.md) — TRI LBM cited as baseline in RoboCasa365.
- [Boston Dynamics](boston-dynamics.md) — homepage reference to "Atlas robot development" needs disambiguation.

## Mentioned in

- [TRI Website](../sources/tri-website.md) — homepage ingest.
- [Diffusion Policy Paper](../sources/diffusion-policy-paper.md) — TRI co-authors.
- [UMI Project Page](../sources/umi-paper.md) — TRI co-authors.
- [RoboCasa365 Paper](../sources/robocasa365-paper.md) — TRI LBM as baseline.
- [Automated Podcast — Tedrake (2026-07)](../sources/automated-podcast-tedrake-rocket-ship.md) — LBM program framing, "amplify not replace" as TRI-rooted philosophy, Tedrake's departure-to-startup signal.
- [TRI LBM paper](../sources/tri-lbm-paper.md) — the program's primary source; 82 TRI authors.
- [Walden Robotics — Launch from Stealth](../sources/walden-robotics-launch.md) — the TRI-LBM-leadership spin-out; Toyota as co-lead investor.

## Open questions / TBD

- ~~**TRI LBM primary source** — not ingested~~ — **ingested 2026-07-08** ([tri-lbm-paper](../sources/tri-lbm-paper.md)); full-PDF deep read still open.
- ~~**Drake** library — TBD entity page~~ — anchored as a section on [Russ Tedrake](russ-tedrake.md) (2026-07-08); promote to its own page if model-based-control coverage grows.
- ~~**Russ Tedrake** — entity page on demand~~ — created 2026-07-08 ([russ-tedrake](russ-tedrake.md)).
- **Founding year + org chart** — not surfaced on homepage.
- **Atlas robot development** reference on TRI homepage — overlap with [Boston Dynamics Atlas](atlas.md) unconfirmed.
