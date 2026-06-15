---
title: "Team 4414 HighTide — 2026 Technical Binder"
type: source
url: https://2026.team4414.com/
author: FRC Team 4414 (HighTide)
published: 2026
ingested: 2026-06-07
reverified: 2026-06-14
tags: [frc, ai, llm-agent, claude-code, mechanical-design, swerve, scouting, competition]
format: website (single-page technical binder)
---

# Team 4414 HighTide — 2026 Technical Binder

## Summary

A self-published single-page "technical binder" website documenting [Team 4414 (HighTide)](../entities/team-4414-hightide.md)'s robot for the 2026 [FIRST Robotics Competition](../entities/first-robotics-competition.md) season, [REBUILT](frc-2026-game-manual.md). The robot is a **FUEL (foam-ball) shooter** built around a swerve drivetrain, a rotating ball-storage "Dye Rotor," a multi-Kraken flywheel shooter, and a turret for shoot-on-the-move. The binder's most distinctive content is its **software story**: precomputed shot-trajectory tables with tilt compensation, and an explicitly **AI-first development workflow** in which "little code is written by hand" — features are attempted by AI agents and reviewed by humans, on a deliberately state-machine-based codebase chosen because it is "easier for AI to reason about." This makes HighTide a concrete real-world instance of exactly the practices surveyed in the [Team 254 "AI in FRC" presentation](team-254-ai-in-frc-presentation.md).

> [!note] Source type
> This is a vendor/team self-published marketing-style binder, not a peer-reviewed or third-party source. It documents design intent and claimed engineering; competition results, team location, awards, and roster are **not stated on the page** and are not asserted here.

The site is a JavaScript single-page app; content was extracted from the page's compiled bundle. Structure: Mechanical (§01–06), Software (§07), Prototyping (§08–10), and "Tide Apps" in-house tools (§11).

> [!note] Re-verified 2026-06-14
> Re-pulled the live SPA's compiled JS bundle and diffed against this page — **content unchanged** since the 2026-06-07 ingest (no new subsystems/sections; awards/sponsors/results/GitHub still absent from the binder itself). Separately, several open questions below were resolved via **external** web research on the same date — see the new "External context" section.

## External context (added 2026-06-14, not from the binder)

The binder omits team identity and results; these come from outside sources:

- **Team:** HighTide Robotics, **Ventura County, CA**; founded **2018** ([team4414.com](https://www.team4414.com/), [The Blue Alliance](https://www.thebluealliance.com/team/4414)).
- **2026 robot name:** **RIPCURRENT** (the FUEL shooter documented in this binder).
- **2026 results:** **70–2–0** official record; **#1 in the FIRST California district** (365 pts); **FIRST Championship Champions (world champions) for REBUILT**, as alliance captain ([TBA 2026](https://www.thebluealliance.com/team/4414/2026)). The AI-first program documented here is a **championship-winning** one — not just an aspirational write-up.
- **Open-source status:** public org [github.com/team4414](https://github.com/team4414) contains **only 2019-era repos**; the 2026 code, "Tide Apps," and agent skill files are **not public**.
- **Still unresolved:** which AI agent/model harness HighTide uses (Claude Code / Codex / Cursor / other) — not stated on the binder and not found in external sources.

## Robot overview

- 2026 REBUILT FUEL shooter; **"Optimized for high BPS single stream shooting"** (BPS = balls per second).
- Design intent tied to REBUILT field geometry: extending hopper that fits **under the TRENCH**, ability to **shoot on the BUMP while under defense**, and review tooling keyed to TELEOP **SHIFT timings**.

## Mechanical subsystems

### §01 Drivetrain — Swerve
- **A 25″ × 32″ swerve base, geared 7.67:1 for low current draw on launch.**
- Chamfered swerve-module corners "maximize hopper area and dye rotor diameter while staying within 110″ and keeping the dye rotor low."
- Left drive rail split to bias the battery to the very edge to accommodate dye-rotor packaging.

### §02 Bumpers
- **Structural bumpers that double as hopper walls and shooter mount.**
- ".060″ bent C channel aluminum holds bumper foam and nests inside the .090″ structure for easier assembly."
- Bumper backing used as hopper walls to gain ~1″ of capacity.
- Cutouts in the corners to access the main breaker, RSL, and radio. Mounted to the drivebase via 4 WCP bumper cones and nuts.

### §03 Dye Rotor (ball storage / indexer)
- **Powered by 2× X60s and 1× X44 bottom bar.** Two cross rails provide structure.
- 3D-printed "stadium" pieces funnel balls into the dye rotor.
- Large-flange 3D-printed hubs reinforced with steel shear pins, aluminum shear tubes, and an internal steel tapped "crown."
- **Extending hopper holds 85+ balls under the trench, 100+ with net over the bump.**

### §04 Intake
- **Powered by 2× Kraken X60s geared down 3.45:1**, plus **1× Kraken X44 geared down 1.5:1.**
- Deploys at the beginning of the match between ~1.3″ wide bumper gaps and stays down via steel latches.
- Oversized bent-aluminum impact guards let the intake slide along the field perimeter; passive rollers for jam-free operation.
- Roller stack: horizontal 1.25″ GoBilda Omni wheels → vertical 3″ Omni wheel → 3″ TTB urethane wheels.
- Cutout on the front panel adds capacity while keeping the starting configuration under the trench.

### §05 Shooter
- **Four Kraken X44s on a 3″ flywheel, copper mass for stored energy, dual GT2 belts on the hood.** ("4× Kraken X44 geared 1:1 to a 3″ flywheel.")
- Copper flywheel mass chosen because it is "slightly more dense than steel" (more stored rotational energy).
- 3× 1″ sushi-wheel feeder geared 16:14 with .5″ compression; 1″ sushi-wheel hood roller at 50% surface speed with 1″ compression.
- Dual GT2 3 mm-pitch 6 mm-wide belts directly over the hood side plates; belt teeth constrained by idlers to eliminate skipping; tapped .10″ steel plates act as belt guides.
- Compact bearing stack using WCP 21/32″ ultra-low-profile shoulder bolts threaded directly into the shooter-body mounting nut strips.
- All motors centered and vertically stacked for minimal protrusions. Uses 7075 aluminum ("harder and more wear resistant than 6061") for impact resistance against trench collisions.

### §06 Turret
- **A 55.7:1 reduction on a single Kraken X44, with a flex-wheel cable-chain tensioner.**
- Two back-to-back 8 lb constant-force springs retract a 1.625″ flex wheel to tension the cable chain; 44T idler gear machined down to 0.275″ thick for cable-chain clearance.
- The turret is the mechanism that lets the robot compensate for tangential velocity at runtime (shoot-on-the-move) — see Software.

## §07 Software

Headline: **"Precomputed trajectories, tilt-compensated shots, and an AI-first dev loop."**

### Shot Calculator
- **A physics-based simulation engine used to determine optimal exit velocities and release angles.**
- For a range of inputs (distance, robot velocity), compute **all** possible shots that score in the goal (upper limit shown green, lower limit red), then **"find the shot at each set of inputs that is most robust to errors."**
- **Precompute a 2nd-order polynomial** to look up hood angle / flywheel speed quickly at runtime.
- The polynomial handles robot **radial** velocity; **tangential** velocity is compensated at runtime with the **turret using 3D vector math.**
- The robot's pitch and yaw transform the calculated 3D shot trajectory to compensate for tilt — **"Allows us to shoot on the bump while under defense."**

### AI-first development
- **"Features are attempted by AI agents and reviewed by humans; little code is written by hand. Logs are added as context during debugging cycles."**
- **"Fully state-machine based, no commands. Easier for AI to reason about."** (A deliberate departure from WPILib's command-based framework.)
- **"Skill files which help agents build autos, parse logs, or optimize loop time."** (Agent skill/instruction files scoped to FRC tasks.)

## §08–10 Prototyping
- **Rotor Iterations** V1–V10 and **Shooter Iterations** V1–V11 documented — heavy iterative prototyping.
- **Chamfered swerve module** prototype.
- **Block-CAD methodology**: "Medium-fidelity block CAD for fast iteration before final part modeling." All power transmission and critical geometries modeled as-is, plate shapes left simple; final parts modeled directly on top of the block models. "Robust to large changes and quick to repair." The binder shows block-CAD vs. detailed-CAD comparisons.

## §11 "Tide Apps" — in-house software tools
A suite of custom team software:
- **Nautilus** — in-house high-fidelity autonomous path planning and visualization.
- **Alliance** — collaborative autonomous path visualization for match strategy ("the fastest way to draw accurate paths").
- **TideScout** — custom scouting app with multiplayer picklists, AI agents, high scalability, and qualitative data-driven insights (match data entry, pick-list rankings, film review). Includes a master strategic dashboard ranking team scoring efficiency/reliability for playoff picklists.
- **TideShot** — shooter performance / BPS analyzer.
- **TideMatch** — iPad match-review app that pairs match video with scouting data, matched to proper SHIFT timings.
- **TideLogs** — telemetry graphs; a server-based **AdvantageScope** repository ("anyone can view any log anywhere, anytime").
- **TideParts** — centralized inventory and part-tracking system for build season.
- **Power analyzer dashboard** — diagnostic dashboard for current draw and battery health across all subsystems.
- **Autonomous Sim / Strategy simulator** — an early-season V3 multiplayer top-down game with customizable robots, used to help decide robot architecture.

## Entities mentioned
- [Team 4414 (HighTide)](../entities/team-4414-hightide.md)
- [FIRST Robotics Competition](../entities/first-robotics-competition.md)
- [REBUILT (2026 game manual)](frc-2026-game-manual.md)

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — agents writing/debugging robot code; FRC skill files; state-machine codebase chosen for AI legibility.
- [AprilTags](../concepts/robotics/apriltags.md) — REBUILT field localization (used by any shoot-on-the-move targeting, though not named explicitly on the page).

## Open questions
- What model(s) and agent harness does HighTide use for its "AI-first" loop? (Claude Code? Codex? Cursor?) **Still unresolved** — not on the binder, not found via external search.
- ~~Are the "Tide Apps" and skill files open-sourced?~~ **Resolved (2026-06-14):** No — the public [github.com/team4414](https://github.com/team4414) org holds only 2019-era repos; 2026 code + Tide Apps are not public.
- ~~What competition results / awards did the robot achieve in 2026?~~ **Resolved (2026-06-14):** RIPCURRENT went 70–2–0 and won the **REBUILT World Championship** ([TBA 2026](https://www.thebluealliance.com/team/4414/2026)).
- How does a fully state-machine (no command-based) WPILib architecture perform in practice vs. the standard command framework? (Now partly answered by the championship result, though not isolated as a variable.)
