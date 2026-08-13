---
title: sourccey-hardware GitHub repository (vulcan-forge/sourccey-hardware)
type: source
url: https://github.com/vulcan-forge/sourccey-hardware
author: Vulcan Robotics
published: 2026-07-10 (repo created; last push 2026-07-10)
ingested: 2026-08-13
license: CERN-OHL-S-2.0
tags: [sourccey, vulcan-robotics, open-source-hardware, cad, step-files, cern-ohl, git-lfs, 3d-printing, teleoperation]
---

## Summary

The open-hardware repository for [Sourccey](../entities/sourccey.md). It contains **115 STEP files** — 91 for the robot, 24 for the teleoperator — under **CERN-OHL-S-2.0**, plus a README explaining how to import them into OrcaSlicer. 16 stars, 5 forks, created 2026-07-10, **no commits since** (verified 2026-08-13).

That is the whole repository. There is no BOM, no wiring, no assembly guide, no URDF, no STLs, and no print profiles.

## Key claims

- **Contents**: "CAD models for the Sourccey robot and teleoperator system, distributed as STEP files." Organised as `Robot/{Accessories, Arms, Base Plates, Dome, Holders and Brackets, Linear Actuator, Walls, Wheels}` and `Teleoperator/`.
- **Part counts** (verified from the git tree, 2026-08-13):

  | Directory | Parts |
  |---|---|
  | `Robot/Arms` | 25 |
  | `Robot/Walls` | 18 |
  | `Robot/Dome` | 10 |
  | `Robot/Holders and Brackets` | 10 |
  | `Robot/Linear Actuator` | 10 |
  | `Robot/Base Plates` | 9 |
  | `Robot/Accessories` | 5 |
  | `Robot/Wheels` | 4 |
  | `Teleoperator/` | 24 |
  | **Total** | **115** |

- **STEP files are tracked in Git LFS** (`*.step filter=lfs diff=lfs merge=lfs -text` in `.gitattributes`); the blobs in the tree are ~130-byte pointers. A plain `git clone` or a raw-file download yields pointer stubs — **`git lfs pull` is required** to get actual geometry. Example: `Robot/Arms/Forearm.step` is a pointer to a 637 KB object.
- **README warns that STEP is not print-ready**: "STEP files are CAD exchange files, not preconfigured print files." Import instructions for OrcaSlicer include verifying dimensions, units (millimetres), and orientation before slicing.
- **License: CERN-OHL-S-2.0** (Strongly Reciprocal) — personal, educational, commercial and manufacturing use permitted, with **source-availability obligations on distributed modifications**.
- Disclaimer: "This hardware is provided without warranty"; users must validate designs before manufacturing.

## Analysis

> [!warning] Contradiction: "public STLs" vs. what is actually published
> The [Vulcan site](vulcan-robotics-sourccey-site.md) states "Public STLs allow replacements and open-source modifications," and press coverage repeats it — *"the STL files are public"* ([Interesting Engineering](https://interestingengineering.com/videos/meet-sourccey-the-open-source-home-robot-you-can-3d-print-and-teach-to-fold-your-laundry), Aug 2026). **No STL files exist in this repository.** It ships STEP only, and its own README stresses that STEP is not a print file. In practice a builder must import 115 STEP parts, orient each one, and author their own profiles — the specs page's per-part infill and layer-height guidance (10% crosshatch cosmetic / 20–40% gyroid load-bearing / 0.08–0.28 mm layers) has to be applied by hand. The gap between "3D print it yourself" as marketed and as shipped is real, though closable with one commit.

> [!warning] CERN-OHL-S is a different bargain from the rest of this wiki's open hardware
> [SO-ARM101](../entities/so-arm101.md), [LeKiwi](../entities/lekiwi.md) and [XLeRobot](../entities/xlerobot.md) are all **Apache 2.0** — permissive, fork-and-close-it-if-you-like. **CERN-OHL-S-2.0 is strongly reciprocal**: anyone distributing a modified Sourccey design must make their sources available under the same terms. For a hobbyist this is invisible; for anyone contemplating a commercial derivative it is the single most consequential fact in the repository, and it is the opposite of the ecosystem default. Note the asymmetry inside Vulcan's own org: **hardware is copyleft, software is Apache 2.0** (`lerobot-vulcan`, `lerobot-robot-sourccey`).

> [!note] What is missing is more informative than what is present
> A CAD dump is the *easy* half of open hardware. The hard half — BOM with suppliers and quantities, wiring/harness diagrams, servo ID assignment procedure, assembly sequence, torque specs, print profiles, and a **URDF** — is entirely absent. The URDF omission bites twice: it blocks simulation (Isaac, MuJoCo, Gazebo) and it is a prerequisite for the inverse kinematics behind the advertised Oculus Quest teleoperation, so one must exist internally. As of ingest, Sourccey is *published* hardware more than *reproducible* hardware.

> [!note] Repo activity
> Created 2026-07-10, last push 2026-07-10, zero subsequent commits through 2026-08-13 — across the month spanning the announced August 2026 "open source the platform" milestone. The active repos in the org are `lerobot-vulcan` and `lerobot-robot-sourccey` (both pushed 2026-08-09) and `sourccey-desktop` (2026-07-24).

## The rest of the `vulcan-forge` org

Verified via the GitHub API, 2026-08-13:

| Repo | License | Stars | Note |
|---|---|---|---|
| `sourccey-desktop` | none | 18 | Tauri + vanilla TS kiosk/desktop app; ships a Raspberry Pi autostart systemd unit |
| `sourccey-hardware` | CERN-OHL-S-2.0 | 16 | this source |
| `lerobot-vulcan` | Apache-2.0 | 12 | fork of [LeRobot](../entities/lerobot.md); policy zoo includes `xvla` |
| `lerobot-robot-sourccey` | Apache-2.0 | 1 | third-party LeRobot plugin registering Sourccey device types |
| `dimos-vulcan` | — | 1 | fork of `dimensionalOS/dimos`, an agentic robot OS |
| `lerobot` | Apache-2.0 | 3 | plain upstream mirror |
| `jetson-orin-gpio-patch` | — | 0 | archived, Apr 2025 — predates Sourccey; suggests earlier Jetson work |

**No `sourccey-electrical` repository exists**, despite the [docs page](vulcan-robotics-sourccey-site.md) advertising an "Electrical — wiring diagrams and board-level construction details" repo.

`lerobot-robot-sourccey` is the more interesting software artifact: it packages Sourccey as a **third-party LeRobot plugin** rather than a fork patch, relying on LeRobot's convention of auto-importing installed top-level packages prefixed `lerobot_robot_`. Registered types: robots `sourccey`, `sourccey_client`, `sourccey_follower`; teleoperators `sourccey_leader`, `bi_sourccey_leader`, `sourccey_teleoperator` (both leader arms + keyboard base control). Requires Python 3.12/3.13 and LeRobot 0.6.x, with a Linux-only `hardware` extra for GPIO.

## Entities mentioned

- [Sourccey](../entities/sourccey.md), [Vulcan Robotics](../entities/vulcan-robotics.md)
- [LeRobot](../entities/lerobot.md), [X-VLA](../entities/x-vla.md)
- Comparison: [XLeRobot](../entities/xlerobot.md), [LeKiwi](../entities/lekiwi.md), [SO-ARM101](../entities/so-arm101.md), [The Robot Studio](../entities/the-robot-studio.md)

## Concepts touched

- [End-user robot programming](../concepts/robotics/end-user-robot-programming.md) — serviceability and part-swapping as a design goal

## Open questions

- Will STLs, a BOM, wiring, and a URDF land with the August 2026 open-source milestone, or is the CAD dump the extent of it?
- Are the LFS objects actually served to anonymous clones, or does the bandwidth quota gate them? (Not tested here — testing would mean pulling ~60 MB of LFS objects.)
- `dimos-vulcan`: is Dimensional's agentic OS a planned Sourccey layer, or exploratory? DIMOS is otherwise uncovered in this wiki — a candidate for its own page.
- The archived `jetson-orin-gpio-patch` (Apr 2025) hints Vulcan once targeted Jetson. Was a Jetson-class Sourccey considered and dropped for cost?
