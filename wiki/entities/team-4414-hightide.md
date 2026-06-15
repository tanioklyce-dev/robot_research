---
title: Team 4414 (HighTide)
type: entity
created: 2026-06-07
updated: 2026-06-14
sources: 1
tags: [frc, team, ai, llm-agent, swerve, competition, world-champion]
---

# Team 4414 — HighTide

A [FIRST Robotics Competition](first-robotics-competition.md) team from **Ventura County, California** (founded **2018**), competing in the 2026 [REBUILT](../sources/frc-2026-game-manual.md) season. Known for an unusually software-forward program: precomputed shot trajectories and an explicitly **AI-first development workflow** — and, as of 2026, a **REBUILT World Champion**.

> [!note] Sourcing
> The technical profile below is drawn from the team's self-published [2026 Technical Binder](../sources/team-4414-hightide-2026-binder.md), which does **not** state location, roster, sponsors, or results. The team-identity and 2026-results facts in the next section were added 2026-06-14 from **external sources** (The Blue Alliance, FIRST, the team's GitHub) — see citations there.

## Team identity & 2026 results

> [!note] Externally sourced (not from the binder)
> - **Program:** HighTide Robotics, Ventura County, CA; founded 2018 ([Team 4414 site](https://www.team4414.com/), [The Blue Alliance](https://www.thebluealliance.com/team/4414)).
> - **2026 robot name:** **RIPCURRENT** (the FUEL shooter described below).
> - **2026 record:** **70–2–0** in official play; ranked **#1 in the FIRST California district** (365 points) ([TBA 2026](https://www.thebluealliance.com/team/4414/2026)).
> - **2026 result:** **FIRST Championship Champions (world champions) for REBUILT**, as an alliance captain (Houston) ([TBA 2026](https://www.thebluealliance.com/team/4414/2026)). This is the strongest possible external validation of the AI-first program described below.
> - **Open source:** the public GitHub org [github.com/team4414](https://github.com/team4414) holds **only 2019-era repos** — the 2026 RIPCURRENT code, the "Tide Apps" suite, and the agent skill files are **not public**.

## 2026 robot

A REBUILT **FUEL (foam-ball) shooter** "optimized for high BPS single-stream shooting." Subsystems ([2026 binder](../sources/team-4414-hightide-2026-binder.md)):

- **Swerve drivetrain** — 25″ × 32″ base, geared 7.67:1 for low launch current; chamfered modules to free hopper/rotor volume within the 110″ perimeter.
- **Dye Rotor** — rotating ball storage (2× Kraken X60 + 1× X44); extending hopper holds 85+ balls under the trench, 100+ over the bump.
- **Intake** — 2× Kraken X60 (3.45:1) + 1× X44 (1.5:1); perimeter-sliding impact guards; deploys through ~1.3″ bumper gaps.
- **Shooter** — four Kraken X44s on a 3″ flywheel with a copper energy-storage mass and dual GT2 hood belts; 7075 aluminum for wear/impact resistance.
- **Turret** — single Kraken X44 at 55.7:1 with a constant-force-spring flex-wheel cable-chain tensioner; enables shoot-on-the-move.

## Software & AI-first development

HighTide is a concrete real-world instance of the practices surveyed in the [Team 254 "AI in FRC" presentation](../sources/team-254-ai-in-frc-presentation.md) ([2026 binder](../sources/team-4414-hightide-2026-binder.md)):

- **AI-first dev loop** — "Features are attempted by AI agents and reviewed by humans; little code is written by hand." Logs are fed back as debugging context.
- **State-machine architecture, no commands** — chosen explicitly because it is "easier for AI to reason about" (a deliberate break from WPILib's command-based framework).
- **Agent skill files** — scoped to "build autos, parse logs, or optimize loop time."
- **Shot Calculator** — physics sim that enumerates all scoring shots per input, picks the most error-robust, and bakes it into a runtime 2nd-order polynomial; pitch/yaw tilt compensation + turret 3D-vector tangential-velocity correction allow "shoot on the bump while under defense."
- **"Tide Apps" suite** — Nautilus (path planning), Alliance (path viz), TideScout (scouting + AI picklists), TideShot (BPS analysis), TideMatch (iPad review), TideLogs (server AdvantageScope repo), TideParts (inventory), a power-analyzer dashboard, and an early-season strategy simulator game.

## Engineering culture signals
- Heavy iterative prototyping (Rotor V1–V10, Shooter V1–V11).
- **Block-CAD-first** methodology: fast medium-fidelity block models with critical geometry as-is, then detailed parts layered on top — "robust to large changes and quick to repair."

## Related
- [FIRST Robotics Competition](first-robotics-competition.md)
- [Team 254 (The Cheesy Poofs)](team-254.md) — the AI-in-FRC reference program
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md)

## Mentioned in
- [Team 4414 HighTide — 2026 Technical Binder](../sources/team-4414-hightide-2026-binder.md)
