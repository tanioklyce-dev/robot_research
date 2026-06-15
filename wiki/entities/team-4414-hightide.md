---
title: Team 4414 (HighTide)
type: entity
created: 2026-06-07
updated: 2026-06-14
sources: 2
tags: [frc, team, ai, llm-agent, swerve, competition, world-champion]
---

# Team 4414 — HighTide

A [FIRST Robotics Competition](first-robotics-competition.md) team — **HighTide**, from **Ventura, California** (FIRST California District; **rookie year 2012**) — that won the 2026 [REBUILT](../sources/frc-2026-game-manual.md) **FIRST World Championship**. Known for an unusually software-forward program: precomputed shot trajectories and an explicitly **AI-first development workflow**.

> [!note] Sourcing
> The *technical* profile (robot subsystems, software methodology) is drawn from the team's self-published [2026 Technical Binder](../sources/team-4414-hightide-2026-binder.md), which does **not** state location, roster, sponsors, or results. The *identity and results* facts come from [The Blue Alliance's 2026 record](../sources/tba-team-4414-2026.md).

## Team identity & 2026 results

Per [The Blue Alliance (2026)](../sources/tba-team-4414-2026.md):

- **Program:** HighTide, Team 4414; **Ventura, CA**; FIRST California District; **rookie year 2012**. Sponsors: fabworks., Gene Haas Foundation, DoD STEM, Google, West Coast Products, & family/community.
- **2026 robot:** **RIPCURRENT** (the FUEL shooter described below).
- **2026 record:** **70–2–0**; **#1 in the FIRST California district** (365 points).
- **2026 result:** **REBUILT FIRST World Champions** — Rank 1 and alliance captain at every event, won all five:

| Event | Rank | Record | Awards |
|---|---|---|---|
| Ventura County District | 1 | 17–0–0 | Winner; Innovation in Control (nVent) |
| Orange County District | 1 | 16–1–0 | Winner; Industrial Design |
| CA Southern State Championship | 1 | 17–0–0 | DCMP Winner; Innovation in Control (nVent) |
| Daly Division (Houston) | 1 | 15–0–0 | Division Winner; Excellence in Engineering (Littelfuse) |
| Einstein Field (Houston) | — | 5–1–0 | **Championship Winner** |

> [!note] World-champion validation of an AI-first program
> The AI-first dev loop documented below isn't aspirational — it produced a **world-championship** robot, making HighTide the wiki's strongest real-world data point for agent-assisted engineering yielding a top competitive result.

> [!warning] "Founded 2018" was wrong
> An earlier (2026-06-14) note here said "founded 2018" from a team-site search snippet. TBA lists **rookie year 2012**; any 2018 figure likely refers to a later *HighTide* rebrand, not the FRC team's founding. Corrected to lead with 2012.

> [!note] 2026 code is not public
> The public org [github.com/team4414](https://github.com/team4414) holds **only 2019-era repos** — the RIPCURRENT code, "Tide Apps," and agent skill files are not published.

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
- [Team 4414 HighTide — 2026 Technical Binder](../sources/team-4414-hightide-2026-binder.md) — robot + AI-first software methodology.
- [The Blue Alliance — Team 4414 (2026 season)](../sources/tba-team-4414-2026.md) — full competition record; REBUILT World Champions.
