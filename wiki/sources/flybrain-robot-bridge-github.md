---
title: "FlyBrain Robot Bridge (Frankweb33/flybrain-robot-bridge) — GitHub README and docs"
type: source
url: https://github.com/Frankweb33/flybrain-robot-bridge
fetch_url: https://raw.githubusercontent.com/Frankweb33/flybrain-robot-bridge/main/README.md
local_path: raw/2026-09-14-flybrain-robot-bridge-readme.md
sha256: e871166d7466b355082af8d60f01942721376867648b415e41d223b7eae662a2
author: "Frankweb33 (repo originally published as Himas1211/flybrain-robot-bridge; GitHub redirects the old name)"
published: 2026-09-14
ingested: 2026-09-27
venue: GitHub repository
format: "README + docs/VALIDATION.md + docs/MALECNS_INTEGRATION.md + src/.../brain/mock.py + file tree + commit log + GitHub API metadata"
github_stats: "221 stars, 37 forks, MIT, Python; created 2026-09-14, all 16 commits on 2026-09-14 (captured 2026-09-27)"
tags: [connectome, drosophila, malecns, fly-brain, biomimetic-robotics, optical-flow, esp32, udp, proof-of-concept, hype-check, mit]
---

# FlyBrain Robot Bridge

> [!warning] It contains no connectome
> The title says *"Connect a Drosophila connectome simulation to a physical robot."* The repository's own text says otherwise, clearly and more than once: *"The model is hand-designed and does not use connectome data"*; the MaleCNS backend *"checks the configured dataset path and then exits with `Not implemented yet`"*; the firmware *"has not been compiled or tested on a board"*; *"No hardware test has been performed."* The "brain" is **eight hand-written leaky integrators** in ~40 lines of NumPy (`mock.py`: *"Eight hand-designed leaky populations, not a connectome simulation"*). The repo is honest about all of this. What it demonstrates is how far a connectome-branded title travels: **221 stars in under two weeks** for a signal-flow scaffold.

## Summary

An **experimental Python pipeline** from a camera to a two-sided robot: `Camera → VisionEncoder → BrainBackend → MotorDecoder → UDP → robot`, with **IMU telemetry fed back** into the backend. The vision encoder computes OpenCV optical-flow magnitude in the left and right image halves plus a center-relative **looming** heuristic. The only working backend is a **mock**: eight leaky activity groups (`left_motion`, `right_motion`, `looming`, `balance_left/right`, `left_motor`, `right_motor`, `escape`) with a 0.12 s time constant, a small forward bias, cross-coupled optic flow → opposite motor (a Braitenberg-style steering rule), and **looming → reverse**. The decoder limits, smooths and optionally inverts two motor commands. A **MaleCNS backend** is a stub with named extension points (`load_graph`, `feed_sensory`, `step`, `get_motor_activity`, `reset`). An **ESP32 (M5 Atom Matrix) firmware scaffold** is present and deliberately disarmed. The roadmap ends with *"Record a physical Strandbeest robot demo."*

## Key claims (from the repo)

### What works (validated locally, per `docs/VALIDATION.md`)

- Editable install, `ruff`, **26 pytest tests** (malformed packets, out-of-order telemetry, speed limits, smoothing, escape, **500 ms watchdog**), and a 90-frame synthetic CLI run; CI on Python 3.11 and 3.12.
- Synthetic mode: deterministic frames, fixed time steps, synthetic IMU oscillation — *"a signal-flow demo, not a robot physics simulation."*

### What does not exist yet

- **No connectome data loaded**; MaleCNS deliberately unimplemented. *"Do not return mock activity under the MaleCNS name."*
- No webcam or video validation, no physical UDP link, no firmware compilation, no hardware behaviour, **no recorded robot**.
- IMU feedback uses **gyro yaw only**; no gait generator; UDP has no authentication, reliability or replay protection.

### Safety design (good practice worth noting)

- **Dry-run by default**; physical transmission requires `--send`.
- The PC sends **zero commands** when telemetry is absent or older than **500 ms**; the receiver must independently stop motors after 500 ms without a fresh command.
- Ctrl+C sends a best-effort stop; *"An optical-flow heuristic cannot protect people or equipment."*

### The integration notes are the useful part

`docs/MALECNS_INTEGRATION.md` lists what a real connectome backend would need: (1) a versioned graph loader keeping neuron IDs, weights and annotations; (2) **explicit sensory and motor population mappings, reviewed against the science**; (3) a documented neuron/synapse dynamics model and time-unit convention; (4) reproducible small-subgraph tests before scaling. And: *"Connectivity alone does not define a validated dynamical model."* That last sentence is the correct objection to the whole genre, and it is written by the repo's own author.

### Lineage cited

Janelia's [Male CNS connectome](male-cns-connectome-paper.md) and the [Google Research post](google-male-fruit-fly-brain-map-blog.md), plus community projects: `philshiu/Drosophila_brain_model` (the [Shiu et al.](shiu-fly-brain-paper.md) LIF model — the wiki's [Drosophila brain model](../entities/drosophila-brain-model.md)), `eonsystemspbc/fly-brain` (Eon Systems, where [Phil Shiu](../entities/phil-shiu.md) now works), `nftechie/doomfly`, `ornata/fly`, `DenisSergeevitch/desktop-fly`. None of their code is bundled.

## Entities mentioned

- [Drosophila brain model](../entities/drosophila-brain-model.md) · [Phil Shiu](../entities/phil-shiu.md) · [HHMI Janelia](../entities/hhmi-janelia.md) · [Drosophila](../entities/drosophila.md) · [FlyWire](../entities/flywire.md) (the lineage, though this repo targets MaleCNS)
- Not given pages: Eon Systems, the community fly repos listed above.

## Concepts touched

- [Connectome](../concepts/bio/connectome.md) — the repo is a stub for a fourth use: **connectome as a robot controller**. It does not yet do that.
- [Whole-organism agentic AI](../syntheses/agents/whole-organism-agentic-ai.md) — the brain-to-body goal, attempted here with a physical robot instead of [flybody](../entities/flybody.md) / [NeuroMechFly](../entities/neuromechfly.md).

## Open questions

- **What would the sensory→motor mapping be?** A fly robot bridge needs camera pixels mapped onto photoreceptor/optic-lobe inputs and descending-neuron outputs mapped onto two wheels or a Strandbeest crank. Neither mapping is biologically defined for a non-fly body. [FlyGM](flygm-connectome-graph-controller-paper.md) avoids the problem by *training* a controller on the connectome graph; a pure simulation (Shiu-style LIF) has no such escape.
- **Would a real connectome backend beat the mock?** Eight hand-tuned integrators already produce the target behaviours (steer toward flow, reverse on looming). The test of a connectome controller is whether it does something the mock cannot.
- **Why 221 stars?** The star count arrived within days of creation, with no release, hardware or demo. It is a clean data point on connectome-as-a-brand in the 2026 hype cycle, and a reminder that star counts are not an evaluation.
