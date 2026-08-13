---
title: Unitree Go2
type: entity
subtype: robot
created: 2026-07-27
updated: 2026-08-13
sources: 4
tags: [unitree-go2, quadruped, robot-dog, china, affordable, edu, project-fetch, frontier-red-team]
---

**Unitree Go2** — Unitree Robotics' consumer/education-tier quadruped ("robot dog"), released 2023. The cheap end of the quadruped market, and **the** robot of Anthropic's Frontier Red Team robotics line: the [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) uplift study, its [Phase Two](../sources/anthropic-project-fetch-phase-two.md) autonomy re-run, and the real-hardware arm of the [robotics evaluation](../sources/anthropic-how-claude-performs-on-robotics-tasks.md). Sits opposite [Spot](spot.md) in the same way [Unitree G1](unitree-g1.md) sits opposite the $90k+ humanoids: an order of magnitude cheaper, sold direct, and consequently the default quadruped in hobbyist and university work.

> [!note] Identification resolved 2026-07-27
> Anthropic's original [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) post referred only to a **"quadruped robodog"** and named nothing; this page was first filed on secondary coverage with an explicit caveat. The [companion evaluation](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) (2026-07-09) settles it in its own words — *"a real Unitree Go2 (the quadruped robot of Project Fetch)"*. The caveat is retired. **Specs below still come from vendor/secondary material**, not an ingested primary datasheet.

## Specs (vendor/secondary, un-ingested)

- **12 DoF** (per Anthropic's [evaluation](../sources/anthropic-how-claude-performs-on-robotics-tasks.md), which uses it both simulated and as real hardware).
- ~15 kg, quadruped; top speed in the ~11 mph / 5 m/s range on the higher tiers.
- **Onboard lidar** (4D LIDAR L1 on most SKUs) + front-facing camera — the two sensors Project Fetch's Phase 2 required teams to read.
- Tiered SKUs: **Air / Pro / EDU**, with the EDU tier adding onboard compute (Jetson-class, ~40 TOPS on some configurations) and unlocked low-level joint control. Price spans roughly **$1.6k (Air) to ~$17k (EDU)** — the SKU used in Project Fetch is unknown.
- Ships pre-programmed behaviors (dance, bipedal stance, backflip on higher tiers) that Project Fetch participants unlocked as "outtakes."

## Why it appears in this wiki

The Go2 is the concrete instance of a claim Project Fetch makes in the abstract: **the hard part of touching unfamiliar robot hardware is the connection layer, not the control problem.** In that experiment the largest measured uplift was in establishing laptop↔robot communication and pulling sensor data — the Claude-less team was actively **misled by inaccurate online documentation** and dropped the simplest connection method, and spent one person's entire day extracting lidar. That is a property of the *SDK and its documentation*, not of quadruped locomotion, and it is the tax any cheap-tier platform with a fast-moving, thinly-documented API imposes.

## As an evaluation platform

The Go2 is the physical substrate for the whole Anthropic Frontier Red Team robotics line, which makes it the wiki's best-instrumented quadruped despite having no primary technical source:

- **[Project Fetch](../sources/anthropic-project-fetch-robot-dog.md)** (Aug 2025 / pub. Nov 2025) — humans program it, with and without Claude.
- **[Phase Two](../sources/anthropic-project-fetch-phase-two.md)** (Jun 2026) — Claude Opus 4.7 programs it alone: **9 min 35 s** vs the human teams' 181 / 361 min.
- **[How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md)** (Jul 2026) — Go2 in MuJoCo *and* real, across four [control abstraction levels](../concepts/robotics/control-abstraction-levels.md). Frontier models emitting raw torques manage roughly **2 seconds** of balance; with the start pose randomized (e.g. on its back) the best model could not stand it up **even once**. No model ever completed the real-world office loop.

## Position vs other quadrupeds in this wiki

- **[Spot](spot.md)** (Boston Dynamics) — the industrial/commercial reference quadruped: mature Python/gRPC **Spot SDK**, Autowalk, optional arm, ~$75k+. Where Spot's SDK is the thing that makes it programmable, the Go2's is the thing Project Fetch suggests you fight.
- **[Unitree G1](unitree-g1.md) / [H1](unitree-h1.md)** — the same vendor's humanoid line, and the wiki's much better-covered Unitree platforms (G1 is the de-facto benchmark robot for learned [whole-body control](../concepts/robotics/whole-body-control.md)).
- The wiki has **no ingested primary source on any quadruped platform** — Spot is grounded in a Boston Dynamics blog post and the Go2 only in a policy article that doesn't name it. See the [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md), which flags quadrupeds as an underrepresented tier.

## As DimOS's reference platform

The Go2 pro/air is the **only platform [DimOS](dimos.md) labels 🟩 stable** ([repo](../sources/dimos-github.md)) — its reference target for navigation, agentic control, spatial memory, and hosted teleop. Connection is over **WebRTC** (`unitree-webrtc-connect`), with an optional DDS bridge (`unitree-sdk2py`).

Practical consequences worth noting for anyone using a Go2 as a research base:

- **A full replay corpus ships with the framework.** `dimos --replay run unitree-go2` drives the entire SLAM / costmap / A* stack from a recorded session with no hardware attached; a published example session holds 4,164 `color_image`, 2,251 `lidar`, and 5,465 `odom` items over 292.5 s.
- **Agentic blueprints are turnkey** — `unitree-go2-agentic` (real hardware + LLM + MCP), `-ollama` (local LLM), `unitree-go2-relocalization` (premap + GTSAM pose-graph optimization).
- **Hosted teleop via dimTELE** — `teleop-hosted-go2-transport` gives browser or Quest driving over WebRTC with the robot dialling out, so no inbound ports on the robot's network.

This makes the Go2 the best-supported robot in the wiki's agentic-robotics coverage — a relevant data point when weighing it against [Spot](spot.md) at ~10× the price.

## Related
- Unitree Robotics — manufacturer (**no entity page yet**; the wiki has G1, H1, and Go2 but not the parent company).
- [Spot](spot.md) — the commercial-tier quadruped contrast.
- [Project Fetch](../sources/anthropic-project-fetch-robot-dog.md) — the only ingested source that uses it.

## Mentioned in
- [Project Fetch: Can Claude train a robot dog?](../sources/anthropic-project-fetch-robot-dog.md) — as an unnamed "quadruped robodog".
- [Project Fetch: Phase Two](../sources/anthropic-project-fetch-phase-two.md) — the same robot, Claude Opus 4.7 unaided.
- [How Claude Performs on Robotics Tasks](../sources/anthropic-how-claude-performs-on-robotics-tasks.md) — names it; 12-DoF; simulated + real.
