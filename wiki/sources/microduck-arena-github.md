---
title: "pollen-robotics/microduck-arena — README and 'Train your first policy' guide"
type: source
url: https://github.com/pollen-robotics/microduck-arena
local_path: raw/2026-10-24-microduck-arena-readme.txt
sha256: e6a610daac60f0acba6b3834f81ef84e5ae282780823415f8e1e1bb1f4c7ce3c
author: Pollen Robotics
published: 2026-10-24
ingested: 2026-10-24
venue: GitHub repo (deployed as the Hugging Face Space pollen-robotics/microduck-arena)
format: "README.md + docs/guides/train-a-policy.md from main, fetched raw. No dated release cited; `published` is the capture date. The design doc is dated 2026-09-03; clip timings were measured 2026-10-05."
tags: [microduck, microduck-arena, pollen-robotics, hugging-face, leaderboard, benchmark, evaluation, reproducibility, onnx, mjlab, hf-jobs, hf-spaces]
---

# pollen-robotics/microduck-arena — README and training guide

## Summary

**[Microduck Arena](../entities/microduck-arena.md)** is Pollen's **server-side simulation leaderboard** for [Microduck](../entities/microduck.md) policies: *"Race a Microduck policy against every other policy, on a clock you can trust."* Its design centres on one honest constraint. The servo model is **chaotic**, so a run *"diverges after a few seconds of simulated time"* across machines. Only times measured on the Space's own x86_64 Linux hardware count; local times are *"indicative."*
- Entries are ONNX files with the **same 61→14 contract the real robot's `robotd` enforces**, published to the entrant's own Hub repo and raced at a pinned revision.
- Scoring is the mean over five perturbed starts, with failures counted at the time limit.
- The board can be rebuilt from the Hub by **re-measuring, never reading back** stored times.

## Key claims

### Contract and scoring
- *"One ONNX file with a 61-D observation input and a 14-D action output — the same contract `robotd` enforces on the real robot, so a policy the Arena accepts will load there too."* The file limit is 64 MiB. Wrong shapes are rejected with the reason, e.g. `observation width is 51, expected 61`.
- **Events**:

  | Event | Rig | Course | Command |
  |---|---|---|---|
  | `sprint-2m` | legs | 2 m flat | 0.25 m/s forward |
  | `roller-sprint-2m` | rollers | 2 m flat | 0.6 m/s forward |
  | `hill-climb-1m5` | legs | 1.5 m at 8° | 0.25 m/s forward |

  Stage events (e.g. `got-a-talent`) play a command timeline instead of racing.
- *"An entry is scored as the **mean finish time over five perturbed starts**, with any failure to finish counted at the event's time limit — so a policy that is quick four times and falls once ranks below a steady one. The replay you watch is the median finishing run, not the best."*
- The introduction also says runs happen *"at every commanded speed in the event's declared sweep, and the best result is recorded."* So the mean is taken over 5 seeds per speed and the best speed is kept. One entry is **33 simulated runs**, *"about 3 s on a developer laptop"*, CPU-bound and synchronous, with no queue.

### Reproducibility as the design centre
- Times are valid only on the Space's hardware: *"Elsewhere — a Mac, or another architecture — the same run gives different numbers: the servo model is chaotic enough that a run diverges after a few seconds of simulated time."*
- The Space's Docker build *"re-measures the golden run and fails if the physics does not reproduce, so a broken build is better than a silently wrong leaderboard."*
- The physics rig and robot assets are vendored from the **Microduck sandbox Space** (`pollen-robotics/microduck-simulator`) at a pinned commit. Re-vendoring forces a `RUNNER_VERSION` bump, because it *"can change what a policy scores."*
- **Recovery**: every published policy lives in its author's repo, tagged `microduck-policy` with a `manifest.json`. `arena recover` re-races what is missing. *"Times are re-measured, never read back: a ranking you cannot re-verify is not one worth restoring."*

### The reference policy, measured
- The vendored reference (`BEST_alpha_walking.onnx`) *"tracks about 44% of its commanded velocity, and below roughly 0.2 m/s commanded it does not walk at all. Both are measured."*

### Training path (guide)
- The **workshop** clones [`microduck-challenges`](https://github.com/pollen-robotics/microduck-challenges) and trains locally on an NVIDIA GPU or on **Hugging Face Jobs**. Every checkpoint is scored locally as it arrives; *"Publish and compete"* enters it.
- The shell form uses **[mjlab](../entities/mjlab.md) task IDs**: `uv run train Mjlab-Sprint2m-MicroDuck --env.scene.num-envs 4096 --agent.max-iterations 3000`. That makes the Arena's native training stack Pollen's mjlab, not [Isaac Lab](../entities/nvidia-isaac-lab.md).
- An existing `.onnx` from any stack can be scored with `arena score policy.onnx --event sprint-2m` and entered with `uv run publish --onnx … --enter --event sprint-2m`.

### Operations
- Entrant tokens are checked via whoami-v2 and dropped, never stored. Site OAuth scope is `openid profile`.
- Social clips are rendered by an HF Job (headless Chromium + ffmpeg). Measured on a 386-frame clip: **75 s on a t4-small vs 588 s on the Space's 8 vCPUs**, *"about a cent a clip."*
- Season points: first publication 100; 10 per run (capped at 3/day); 25 for a personal best; 250/150/100 for podium places.

## Entities mentioned
- [Microduck Arena](../entities/microduck-arena.md), [Microduck](../entities/microduck.md), [Pollen Robotics](../entities/pollen-robotics.md), [Hugging Face](../entities/hugging-face.md), [mjlab](../entities/mjlab.md)

## Concepts touched
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): the Arena is sim-only, but its contract guarantees that what it accepts will load on hardware.
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md): the chaos claim is a direct consequence of a high-fidelity, frictional servo model.

## Open questions
- **What physics does the Arena rig run?** It is vendored from `microduck-simulator`, but this README does not say whether that is MuJoCo, MJWarp or a JS engine (`app/src/rig.js` suggests at least the visual rig is browser-side). This decides how "foreign" an Isaac-Lab-trained policy is when raced here.
- **Leaderboard sim-to-real correlation.** Does the Arena rank predict real-robot performance? Nothing measured is published.
- The design doc (`docs/superpowers/specs/2026-09-03-microduck-arena-design.md`) and `docs/probe-results.md` are not ingested.
