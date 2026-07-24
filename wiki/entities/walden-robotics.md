---
title: Walden Robotics
type: entity
subtype: company
created: 2026-07-15
updated: 2026-07-15
sources: 2
tags: [walden-robotics, russ-tedrake, tri, lbm, diffusion-policy, physical-ai, manufacturing, spinout, funding]
---

# Walden Robotics

**Walden Robotics** — Cambridge, MA physical-AI startup building general-purpose robots for **manufacturing and logistics**, powered by **[Large Behavior Models](../concepts/learning/large-behavior-models.md)** and **[Diffusion Policy](diffusion-policy.md)**. **Spun out of [Toyota Research Institute](tri.md) in January 2026**; launched from stealth **2026-07-15** with a **$300M seed at a $1.1B valuation**. Founded and led by **[Russ Tedrake](russ-tedrake.md)** (CEO). This is the venture the wiki had been tracking as Tedrake's "still-stealth physical AI startup" ([Automated Podcast, 2026-07](../sources/automated-podcast-tedrake-rocket-ship.md)) — Walden is its reveal.

Tagline: *"Robots ready to work. With you. Today."* Mission: *"a world where general-purpose robots dramatically improve the quality of life for all people—supporting us in factories, at work, at home, and beyond."* The name references **Thoreau's *Walden*** and deliberate living.

## What it builds

- **Full-stack**: hardware, software, "frontier-class AI," and applications ([launch](../sources/walden-robotics-launch.md)).
- **Model classes**: [LBMs](../concepts/learning/large-behavior-models.md) + [Diffusion Policy](diffusion-policy.md) — "let them quickly learn new tasks and continuously improve through real-world practice." This is the TRI Diffusion-Policy → LBM program commercialized.
- **Deployment model**: **"powerful autonomy combined with a human available for remote assistance"** — ship capability now, improve the policy from real-world practice (the virtuous data cycle [Tedrake argues for](russ-tedrake.md)).
- **Advertised tasks**: machine tending, tool setting, parts kitting, assembly.
- **Verticals**: automotive, aerospace, semiconductors, electronics, logistics, life sciences.

## Traction

- Robots doing **"useful work in production at a Toyota plant in North America since February 2026"** (NC facility) — "from first pilot to real work in under two months" ([launch](../sources/walden-robotics-launch.md)).

## Funding

- **$300M seed** at **$1.1B valuation** (2026-07-15).
- **Co-leads**: Toyota Motor Corp, Toyota Invention Partners, Toyota Ventures, **Deviation Capital**.
- **Participating**: NVIDIA, Boeing, AE Ventures, Samsung Ventures, Prologis Ventures, CoreWeave Ventures, Calibrate Ventures, Colle Capital, Shine Capital, NextView Ventures, Squarepoint Capital, One Madison Group, KAS Venture Partners, Menlo Ventures.
- The **Toyota-heavy cap table** (four Toyota-linked vehicles co-leading) mirrors the [TRI](tri.md) spin-out origin — Toyota is both former parent and anchor investor.

## Founding team

A near-wholesale transplant of TRI's robot-learning leadership — the same cohort behind [Diffusion Policy](diffusion-policy.md) and the [TRI LBM paper](../sources/tri-lbm-paper.md).

| Person | Role | Background |
|---|---|---|
| **[Russ Tedrake](russ-tedrake.md)** | CEO & co-founder | MIT Toyota Professor; former SVP of Large Behavior Models, TRI; led Team MIT in the DARPA Robotics Challenge; author of Drake + Underactuated Robotics. |
| **[Ben Burchfiel](ben-burchfiel.md)** | CTO & co-founder | Ex-Aurora Innovation production ML; co-led TRI's 60+ person robot-learning team; Diffusion Policy / OpenVLA / LBM 1.0. PhD Duke, postdoc Brown. |
| **[Siyuan Feng](siyuan-feng.md)** | Principal Architect & co-founder | Full-stack roboticist; DARPA Robotics Challenge bipedal locomotion; Diffusion Policy; co-led TRI's LBM effort. PhD Robotics, CMU. |
| **Adrien Gaidon** | CSO & co-founder | Adjunct Prof., Stanford; former Calibrate Ventures Partner; former ML division exec director, TRI. 100+ patents, 16,000+ citations. PhD (MSR-Inria). |
| **Rares Ambrus** | Head of AI & co-founder | Former head of computer vision / ML, TRI; robotics, autonomous driving, VR/AR. PhD KTH (Sweden); 70+ papers, 50+ patents. |
| **Kerri Fetzer-Borelli** | COO & co-founder | 10+ years building operating systems for R&D orgs; robotics/ballistics testing, nuclear-power background; scaled automated-driving + robotics ops. |
| **David Johnson** | CPO & co-founder | Founded and sold **Dexai Robotics** (kitchen automation); ex-Director of Sony's Robotic Gastronomy; PhD Physics, Stanford. |

## Why it matters in this wiki

- **Resolves a tracked open question** — the wiki flagged Tedrake's stealth startup (name/funding/team/focus TBD) on the [podcast source](../sources/automated-podcast-tedrake-rocket-ship.md) and [Tedrake entity](russ-tedrake.md). Walden is the answer: manufacturing, $300M/$1.1B, LBM+Diffusion-Policy, Toyota-backed.
- **The academic-lineage → commercial bridge** — this is where [Diffusion Policy](diffusion-policy.md) (RSS 2023) and the [TRI LBM paper](../sources/tri-lbm-paper.md) (Science Robotics 2026) leave the lab. The wiki's most-cited manipulation methods now have a named commercial vehicle.
- **A [TRI](tri.md) talent-outflow event** — Tedrake, Burchfiel, Feng, Gaidon, Ambrus all leaving TRI's robotics/ML leadership for one company is a significant reshaping of the TRI robotics org.
- **Manufacturing-first, not home-first** — unlike the wiki's assistive/home cluster ([Stretch](hello-robot.md), [1X NEO](1x-neo.md)), Walden targets industrial verticals with a human-remote-assist safety net, echoing the [K-Scale post-mortem](../sources/robot-report-kscale-labs-lessons.md) lesson that unit economics + real customers beat capability demos.

> [!warning] Contradiction — the company name
> The [Tedrake podcast](../sources/automated-podcast-tedrake-rocket-ship.md) strongly hinted the startup's name *"references LBMs"* (host: "at least for now, it's in the company name," unchallenged), and a Robotics Summit keynote was titled *"Building Great Behavior Models for Industry."* The actual name, **"Walden,"** references **Thoreau**, not Large Behavior Models. Most likely the "Behavior Models" phrasing lived in the keynote title / product framing rather than the corporate name; treat the earlier "it's in the company name" reading as unconfirmed.

## Related

- [Russ Tedrake](russ-tedrake.md) — CEO; the wiki's model-based-control ↔ learning bridge.
- [Toyota Research Institute](tri.md) — spin-out parent and anchor investor.
- [Large Behavior Models](../concepts/learning/large-behavior-models.md), [Diffusion Policy](diffusion-policy.md) — the commercialized model classes.
- [Physical Intelligence](physical-intelligence.md) — the closest comparable "founders-from-a-top-lab, generalist-policy startup" (π-line), though PI is broader/home-inclusive vs. Walden's manufacturing focus.

## Mentioned in

- [Walden Robotics — Launch from Stealth](../sources/walden-robotics-launch.md) — the launch ingest (primary source).
- [Automated Podcast — Tedrake (2026-07)](../sources/automated-podcast-tedrake-rocket-ship.md) — the pre-reveal stealth-startup discussion.

## Open questions

- **Robot hardware** — own build vs. integrated third-party arms/bases? Unspecified on launch.
- **Headcount** — not disclosed.
- **Tedrake's TRI status** — clean departure or dual role?
