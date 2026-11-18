---
title: "pollen-robotics/microduck_rl: expressive-motions and dance-steps branches (GitHub)"
type: source
subtype: code-repository
url: https://github.com/pollen-robotics/microduck_rl/tree/expressive-motions
fetch_url: https://raw.githubusercontent.com/pollen-robotics/microduck_rl/4dd6989ac3d156b9c002c3ac5d98c3c7dbb8f143/src/mjlab_microduck/tasks/expressive_motions.py
capture: bundle
local_path: raw/2026-11-17-microduck-rl-expressive-motions-branches.md
sha256: d84c0e3700ee96197ff0cf5058fc57180b85aeafd0ce3be426decbc86095deb9
author: Pollen Robotics (commits by Rémi Fabre)
published: 2026-10-30
ingested: 2026-11-17
license: Apache-2.0 (code)
format: "Two unmerged branches, read at their tips (expressive-motions 4dd6989, dance-steps bdb7989, both 2026-10-30). Captured as a bundle: seven commit messages, the motion-definition module, the environment configuration, the motion-table headers, the deleted 2026-02 imitation-learning doc with its commit messages, and the header of the runtime's emotion module. Reward functions in mdp.py, tests and the motion tables themselves were read but not captured. The notes/ directory the commits cite is not in the repository."
tags: [microduck, pollen-robotics, mjlab, motion-tracking, motion-retargeting, expressive-motion, dance, phase-conditioned-policy, reward-design, sim-to-real, open-duck-mini, primary, unmerged]
---

# pollen-robotics/microduck_rl: expressive-motions and dance-steps branches

## Summary

Two unmerged branches of [Pollen Robotics](../entities/pollen-robotics.md)' [Microduck](../entities/microduck.md) training repository. Over three days (2026-10-28 to 10-30) they teach the 25 cm biped body-language motions and then an 18-second dance. Six hand-written "expressive" motions came first (Sassy, Proud, Shy, Excited, Giggle, Hmph). Then came four versions of a dance called "Tremendous": a 50 Hz table re-solved onto the duck's own body with the feet planted. A last variant has the legs take four real steps. Each motion gets its own policy, trained with PPO in [mjlab](../entities/mjlab.md). The policy sees only the robot's standard 61-number observation plus a phase clock; the reference itself is given only to the critic. So each deployed policy carries its motion memorised in its weights, and it fits the same `61 → 14` slot as every other Microduck skill. One commit message reports that a scaled-down version of the dance ran on a physical robot with "good" transfer. It is the only report in the wiki of human-style motion on Microduck hardware, and it is one sentence with no video or numbers.

The branches matter for [motion retargeting](../concepts/robotics/motion-retargeting.md) because they show what the problem looks like on a non-humanoid. The human performance does not reach the duck limb by limb. It is reduced to **eight channels**: trunk roll, pitch, yaw and height, plus four head and neck joints. It is then re-solved against balance and joint limits that are far narrower than a humanoid's. That is a different job from the per-frame inverse kinematics of [SOMA Retargeter](soma-retargeter-github.md). It is also the clearest available explanation of why [NVIDIA's MicroDuck experiment](nvidia-soma-retargeter-blog.md) trained "a controller for each clip."

## Key claims

### Status
- Both branches fork from `develop` at `ceca017` (2026-10-09). Neither was merged as of the capture; `develop` was at `0daab16` (2026-11-10). They also carry Rémi Fabre's ground-grasp work of 2026-10-10 (an opening beak and graspable objects), which the expressive environment is built on.
- All seven expressive/dance commits are signed "Assisted-by: Claude:claude-opus-5-5".
- The design notes the commits cite (`notes/expressive/BRIEF.md`, `LEDGER.md`, `notes/dodge/tools/*.py`) are not in the repository. So the scripts that built the dance tables, and the source of the dance's poses, are not public.

### Six expressive motions (2026-10-28)
- Registered as `Mjlab-Expressive-<Name>-MicroDuck`: Sassy (a hip wiggle over a bow), Proud (chest out, head high), Shy (crouch, slow twist, head turned away), Excited (small squats, head bobbing), Giggle (a fast shake, leaning back), Hmph (trunk turned away, chin flick).
- Each is a **2.5–3.5 s one-shot** that starts and ends in the standing pose. Each channel is a sum of eased envelopes and sine oscillations written by hand, smooth by construction, with no captured data.
- **Built on the ground-pick environment**: same 61-number observation, 14 actions, and a phase command `[cos 2πφ, sin 2πφ, 0]` in the twist slots. The env docstring states that "robotd drives φ per tick exactly like the ground pick", so the deployment path already exists in the runtime.
- **Rewards**: Gaussian tracking of the eight channels; feet-planted costs (drift, lift, slip); a pull back to the standing leg pose at the end; joint targets clamped to the joint ranges with an "overrun tax"; a joint overspeed penalty; termination on a fall past 60°.
- **Friction realism**: foot friction raised to U(1.0, 2.0) with sticky elliptic contacts, on "Rémi's hypothesis: the real feet are very grippy, the sim let emotions glide."
- **Range is tiny**: the standing pose "is near full leg extension: only ~+3 mm is reachable upward, a squat goes to ~-15 mm." The BAM servo model sags about 2 mm under the robot's weight, and the zero of the height channel is set to that settled stance.

### Round 2: what failed and how the rewards were changed
- Round 1 evaluation: "every warm-started run dived the neck, the oscillations barely appeared, Hmph parked the left hip yaw on its stop, the stand net stepped at the hand-back."
- Fixes: training from scratch; a **wide head kernel** (std 0.4) beside the narrow one, because the narrow kernel "had no [gradient]" at large errors; a linear cost on neck deviation beyond 0.3 rad; **velocity tracking** of each oscillating trunk channel against the reference's derivative; a joint-limit proximity penalty on all 14 servos; and a still settle so the standing policy receives a motionless robot.
- Feasible amplitudes, as stated: Sassy wiggle 2.0 Hz, Giggle roll ±0.08 rad at 4 Hz, Excited squats 0 to −14 mm at 2.5 Hz.

### The dodge dance "Tremendous" (2026-10-29 and 10-30)
- **Source**: "combo A of the dodge dance (110 BPM, 32 beats, T = 18.25 s music excerpt)." It is stored as a 50 Hz table of the eight channels plus their analytic rates. The table is "re-solved on the stand footprint": static centre of mass at least 11 mm inside the soles, every joint at least 0.07 rad off its stops, reference speeds at most about 5 rad/s, ending still at the stand. Each key pose "keeps its trunk lean direction, face direction and head offset as far as" balance and joint ranges allow, with "min-jerk snaps that arrive ON the beat."
- **Training**: 18.25 s episodes (912 steps), "~6x longer than round 2's," 7,000 PPO iterations, with an actor MLP of 512-256-128.
- **Version 1 failure**: the runs "parked head_pitch ~2.3 rad off (chin down in both sky poses, beak above the horizon 0-3 % of the dance vs 87 % in the reference) and never leaned right." Again, the Gaussian kernels gave no gradient far from the target. The fix was linear deviation costs on the head joints and trunk roll.
- **The reference was checked before training**: every joint inside its range at 0.1 s steps (minimum margin 0.070 rad); no self-collision; mesh clearances of at least 5.9 mm.
- **Hardware test (v3 commit message)**: "Rémi tested tremendous-70 on the real duck: transfer is good, the choreography is too timid." Tremendous-70 is the version with trunk channels scaled to 70%. v3 therefore enlarges the motion: side tilt ±22° on the real hip-roll range, trunk twists ±12°, a limbo lean of −36°, a squash bounce to −22 mm on every beat, and head hits on the beat. v4 adds "a double ding hit, head-bob groove, bob-and-weave bar," fine-tuned from the v3 run ("v3 polished after the real-duck test"). No v3 or v4 hardware result is reported.
- **The real hip-roll range is wider than the export**: the commit uses ±0.52 rad because "the export's +-0.384 is conservative, the physical robot was posed at 0.463 rad and rests at -0.566."

### Dance with steps (dance-steps branch, 2026-10-30)
- The same dance, with the legs taking **four single-foot steps** (18 mm clearance, 0.32–0.37 s swings). "Every recorded pose re-solved on its stance on the training model" with "whole-body IK every 10 ms (feet 6-D, CoM, trunk roll / pitch / yaw)," retimed so every joint stays at or below 6 rad/s.
- **Body limits found in the process**: "no ankle roll, so flat parallel soles keep a fixed ~84 mm spacing (wider needs a deep crouch + pigeon toes); fore-aft stagger is free; the trunk twist lets the roll pass the hip-roll range but the shin then hits the battery: flat-footed roll stays ~15-17 deg."
- Rewards add foot-target tracking, a contact schedule, clearance and an unscheduled-lift cost. The critic also gets the step reference and its errors.
- Validated in tests and a 16-environment smoke run only. There is no trained-policy or hardware result.

### The earlier attempt: imitating a generated gait (February 2026, removed)
- The first training stack offered `Mjlab-Velocity-Flat-MicroDuck-Imitation`. Its reward matched reference gaits from Pirrone's `Open_Duck_reference_motion_generator`, which uses the Placo walk engine, fitted to 15th-degree polynomials per velocity command ([Open Duck Mini](../entities/open-duck-mini.md) lineage).
- Commit `7b1fc37` (2026-02-13, Antoine Pirrone): "CHECKPOINT OMG no imitation works very well." The imitation code was deleted on 2026-04-01 and a 96 MB `reference_motion.pkl` was dropped on 2026-08-25. All shipped skills are trained without a reference motion.

### The shipped alternative: keyframe "emotions"
- The onboard runtime ([`microduck`](microduck-runtime-repo.md)) already ships 13 emotions (angry, curious, defiant, devastated, excited, impatient, laugh, mmh, mock, no, sad, yes, yes_fast). Each is a keyframe JSON file plus a sound, in the format of `pollen-robotics/microduck_emotions`.
- They "drive the policy's commands, nothing below them": head angles, body pitch, body height and the beak, fed into the walking policy's command slots with zero velocity. So the shipped emotions can only use what the walker's command interface exposes. The expressive policies add trunk roll and yaw, oscillations and timed dynamics that the walker was not trained to produce.

## Entities mentioned
- [Microduck](../entities/microduck.md) · [Pollen Robotics](../entities/pollen-robotics.md) · [mjlab](../entities/mjlab.md) · [Open Duck Mini](../entities/open-duck-mini.md)

## Concepts touched
- [Motion retargeting](../concepts/robotics/motion-retargeting.md): human motion reduced to a few expressive channels and re-solved for a non-humanoid body.
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md): servo sag sets the zero of the height channel; foot friction raised to stop simulated motion from gliding.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md): one reported hardware test, qualitative.

## Reading it critically
- **The hardware claim is a commit message.** "Transfer is good" describes a single test of a scaled-down variant. There is no video, no repeat count and no tracking error measured on the robot.
- **The dance's source is not public.** "Every recorded pose" says poses were recorded, but not how: from video, from a performer, or posed by hand. Nothing here involves motion capture, SOMA or NVIDIA's retargeter.
- **Unmerged work in progress.** The branches may be rebased, merged or abandoned. The fetch URL is pinned to commit `4dd6989`, so a later branch change will not show up as drift; a re-check needs the branch.
- **The reward history is the most useful part.** The same failure recurs three times: narrow Gaussian kernels give no gradient once the policy is far off, so it parks a joint at a wrong pose. Each time the fix is a wider kernel or a linear cost. That pattern generalises beyond this robot.

## Open questions
- What is the "dodge dance," and how were its poses recorded?
- Do the expressive policies ship? They would need either a merge and a runtime slot for phase-driven one-shots, or the ground-pick slot reused.
- How does this compare with NVIDIA's MicroDuck experiment ([SOMA Retargeter post](nvidia-soma-retargeter-blog.md)), which used captured human motion from Bones? Did that work reduce to the same channels, and did it reach hardware?
- Would one policy conditioned on a reference input generalise across motions, instead of one memorised policy per motion? Nothing on these branches tries it.

## Related
- [SOMA Retargeter post](nvidia-soma-retargeter-blog.md) — NVIDIA's simulation-only MicroDuck experiment, also one controller per clip.
- [NVIDIA/soma-retargeter v0.2.0](soma-retargeter-github.md) — the humanoid retargeter; it has no MicroDuck configuration.
- [`pollen-robotics/microduck` runtime](microduck-runtime-repo.md) — where phase-commanded skills and keyframe emotions run.
- [Microduck launch](pollen-robotics-microduck.md) — the `microduck_rl` repository at launch.
