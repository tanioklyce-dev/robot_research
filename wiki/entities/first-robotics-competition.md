---
title: FIRST Robotics Competition
type: entity
created: 2026-05-08
updated: 2026-05-08
sources: 4
tags: [frc, competition, educational-robotics, stem]
---

# FIRST Robotics Competition

The world's leading high-school robotics competition, run by FIRST (For Inspiration and Recognition of Science and Technology), founded by Dean Kamen. Teams of students design, build, and program industrial-scale robots to compete in an annually changing game.

## Scale & reach
- ~3,700 teams across 30+ countries; ~90,000 students in 2026 ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md), §1.3).
- 56 Regional Competitions, 125 District Competitions, 15 District Championships, plus FIRST Championship (April 2026).
- Part of the broader FIRST program family: FRC (grades 9–12), FTC (grades 7–12), FLL (Pre-K–8).

## Competition format
- **Season cycle**: New game revealed at Kickoff (January); ~6-week build season; regional/district competitions (February–April); FIRST Championship (April).
- **Match structure**: 2:40 matches — 20s autonomous + 2:20 teleoperated. 3v3 alliance format ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md), §6).
- **Qualification + Playoffs**: Teams earn Ranking Points through match wins and BONUS RP thresholds; top teams form alliances for elimination bracket.
- **Awards**: Engineering Inspiration, Chairman's Award (now FIRST Impact), Woodie Flowers Finalist Award, and technical awards (Quality, Innovation, Industrial Design, etc.).

## 2026 game: REBUILT
- Presented by the Gene Haas Foundation ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md)).
- Season theme: **FIRST AGE** presented by Qualcomm (archaeology-inspired).
- Game: Score FUEL (foam balls) into HUBs, navigate BUMPS and TRENCHES, climb TOWERs.
- Distinctive mechanic: HUBs alternate active/inactive during TELEOP ALLIANCE SHIFTS based on AUTO performance.
- See [FRC 2026 Game Manual](../sources/frc-2026-game-manual.md) for full details.

## Robot constraints (2026)
- Weight: ≤115lb (without bumpers/battery); ≤135lb with bumpers ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md), R103/R408).
- Starting configuration: ≤110in perimeter, ≤30in tall.
- Extension: ≤12in beyond perimeter, one direction at a time.
- Mandatory control system: [roboRIO](roborio.md) + FRC Radio + FMS Ethernet.
- Approved languages: Java, C++, LabVIEW (WPILib); Python via RobotPy.
- No individual non-KOP part >$600 FMV; major mechanisms must be built after Kickoff.

## Technical infrastructure
- **Field Management System (FMS)**: Controls wireless, scoring, E-stop/A-stop, match timing. Ethernet-connected to each driver station.
- **[AprilTags](../concepts/robotics/apriltags.md)**: 32 fiducial markers (36h11 family) on field elements enable autonomous vision-based navigation and targeting ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md), §5.11).
- **Driver Station**: WPILib software on team laptops; communicates with roboRIO via FMS network during matches.
- **CAD**: Official field models in Onshape; low-cost build plans published for practice fields.

## Key vendors & ecosystem
- [AndyMark](andymark.md): Field elements, AM14U6 chassis (KitBot), FUEL, bumper materials.
- **REV Robotics**: NEO/NEO 550 motors, SPARK MAX/SPARK Flex controllers, Pneumatic Hub.
- **CTR Electronics / WCP**: Falcon 500 / Kraken X60 motors, Talon FX controllers, CANcoder.
- **Cross the Road Electronics (CTRE)**: Phoenix framework, Pigeon IMU.
- **WPILib**: Open-source FRC software framework (Java/C++/Python).
- **NI (National Instruments)**: [roboRIO](roborio.md) controller.
- **Limelight / PhotonVision**: Popular vision processing solutions for AprilTag detection.

## Culture
- **Gracious Professionalism**: Ethos of high-quality work while valuing others; coined by Dr. Woodie Flowers (1943–2019) ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md), §1.4.2).
- **Coopertition**: Cooperating while competing — teams routinely loan parts, share code, and mentor rivals.
- **Open-source culture**: Many teams publish robot code, CAD, and scouting tools on GitHub. Chief Delphi (community forum) is the primary knowledge-sharing platform.

## Relationship to research robotics
- FRC robots are industrial-scale (115lb, steel/aluminum, pneumatic/electric) but purpose-built for a single game — not general-purpose.
- Autonomous modes are typically hand-coded trajectory-following (WPILib PathWeaver/PathPlanner), not learned policies — but ML/RL approaches are emerging.
- AprilTag-based localization is shared technology with research robotics.
- FRC alumni are a significant pipeline into robotics research and industry.

## Mentioned in
- [FRC 2026 Game Manual](../sources/frc-2026-game-manual.md)
- [FRC KitBot 2026](../sources/frc-kitbot-2026.md)
- [Team 4414 HighTide — 2026 Technical Binder](../sources/team-4414-hightide-2026-binder.md)
