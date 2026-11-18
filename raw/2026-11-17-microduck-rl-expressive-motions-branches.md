# Capture: https://github.com/pollen-robotics/microduck_rl/tree/expressive-motions
Captured 2026-11-17 by git clone of pollen-robotics/microduck_rl. Two unmerged branches: expressive-motions (tip 4dd6989ac3d156b9c002c3ac5d98c3c7dbb8f143, 2026-10-30) and dance-steps (tip bdb798961031424ce0c30abaa3f19d843831a0af, 2026-10-30); both fork from develop at ceca017 (2026-10-09) and carry the ground-grasp commits of 2026-10-10 below the expressive work. develop was at 0daab16 (2026-11-10) without either. Bundle of verbatim items, each under a ==== FILE header: the full messages of the seven expressive/dance commits; src/mjlab_microduck/tasks/expressive_motions.py at 4dd6989; src/mjlab_microduck/tasks/microduck_expressive_env_cfg.py at 4dd6989; the first two lines of each motion_data CSV; docs/IMITATION_LEARNING.md as it stood before its deletion in 67a8750 (2026-02-27), with the messages of 7b1fc37, 90b240d and 28a1087; and the module header of robotd/src/emotion.rs from pollen-robotics/microduck (commit 46c8f1f). The notes/ directory the commits cite (notes/expressive, notes/dodge) is not in the repository.

==== FILE commit messages (git show -s, oldest first)

commit 8ca2adb9fbff1fa248cdaabe19cca03d426a78be
Author: RemiFabre
Date: 2026-10-28

Expressive body motions: phase-commanded one-shots with planted grippy feet

Six motions (Sassy, Proud, Shy, Excited, Giggle, Hmph) registered as
Mjlab-Expressive-<Name>-MicroDuck on the ground-pick env (61-D obs, 14 actions,
phase command, phi = t / T). Rewards track a smooth reference (trunk roll /
pitch / yaw-from-start / height, 4 head joints), keep the feet planted (drift,
lift, slip), settle back to the stand pose; targets clamped to the joint
ranges with the overrun tax. Foot friction U(1, 2) + elliptic cone, impratio
10. Warm start from alpha_ground_pick; Sassy also has a from-scratch twin.

Assisted-by: Claude:claude-opus-5-5

Branches: dance-steps expressive-motions 

commit da1e26a78d36cf77bd20eba3e6f7292a5be87be7
Author: RemiFabre
Date: 2026-10-28

Expressive round 2: velocity-tracked oscillations, head-dive guard, from scratch

Round 1 eval (notes/expressive/LEDGER.md): every warm-started run dived the neck, the oscillations
barely appeared, Hmph parked the left hip yaw on its stop, the stand net stepped at the hand-back.

New tasks Mjlab-Expressive-<Name>-R2-MicroDuck (motion key "<Name>-R2"), round 1 tasks unchanged:
1. All trained from scratch (MicroduckOnPolicyRunner). Wide head kernel (std 0.4) beside the
   narrow one, and a cost on |neck - reference| beyond 0.3 rad.
2. Velocity tracking of every oscillating trunk channel (Euler rates from the body angular velocity,
   height rate = root vz - mean foot vz) against d/dt of the reference; those channels' position
   weights x1.6. Feasible references: Sassy wiggle 2.0 Hz, Giggle roll +-0.08 at 4 Hz,
   Excited squats 0..-14 mm at 2.5 Hz.
3. Hmph turns -18 deg; joint_limit_proximity_penalty (margin 0.05) on all 14 servos.
4. Every r2 envelope closes (value and velocity 0) by phi 0.87; settle_from 0.88; a gated
   joint-speed cost after settle_from so the stand net receives a still robot.
Tests: r2 bounds / end-still / frequencies / env terms / from-scratch registry (52 pass).

Assisted-by: Claude:claude-opus-5-5

Branches: dance-steps expressive-motions 

commit 9b424b43432f587243acbcd27bd9598a9228d8fc
Author: RemiFabre
Date: 2026-10-29

Dodge dance: data-driven Tremendous reference, feet planted (Expressive-Tremendous tasks)

expressive_motions: DataMotion, a 50 Hz table of the 8 reference channels + their analytic rates
(motion_data/tremendous_planted.csv, built by notes/dodge/tools/planted_ref.py): combo A of the dodge
dance (110 BPM, 32 beats, T = 18.25 s music excerpt) re-solved on the stand footprint, static CoM
>= 11 mm inside the soles, every joint >= 0.07 rad off its stops, reference speeds <= ~5 rad/s,
back to the stand (value and rate 0) at 17.80 s. get_motion() finds data motions; kept out of
ALL_MOTIONS (their amplitudes exceed the small-motion test bounds).

Tasks Mjlab-Expressive-Tremendous-MicroDuck (full) and -Tremendous-70- (trunk channels x0.7, same
head): round 2 terms (from scratch, wide head kernel, neck-dev cost, rate tracking on roll / pitch /
dz, joint-limit proximity, still settle) + a wide trunk kernel (roll/pitch std 0.15), settle gate
ramp 0.01 phi, 7000 iterations.

Tests: tests/test_expressive_dance.py (11) + test_expressive_cfg.py (52) pass; local CPU rollout and
16-env x 3-it smoke training of both tasks OK.

Assisted-by: Claude:claude-opus-5-5

Branches: dance-steps expressive-motions 

commit 998f278d26ba625b1df714deecb3a6b017665407
Author: RemiFabre
Date: 2026-10-30

Dodge dance r2: linear deviation costs on the head joints and the trunk roll (data motions only)

The 1029 Tremendous runs parked head_pitch ~2.3 rad off (chin down in both sky poses, beak above the
horizon 0-3 % of the dance vs 87 % in the reference) and never leaned right (roll -2..-5 deg where the
reference asks +9.5..+13). Far off, the Gaussian kernels (head std 0.12 / 0.4, trunk 0.04 / 0.15) give
no gradient: round 1's neck dive again, now on head_pitch. Same fix as neck_dev, for DataMotion tasks only:
  head_dev        head_pitch + head_yaw, -5 per rad beyond 0.25 rad (also stops the -146 deg end yaw)
  head_roll_dev   head_roll,             -5 per rad beyond 0.15 rad
  trunk_roll_dev  trunk roll,           -10 per rad beyond 0.05 rad (~3 deg)
ex_head_dev_cost already reads any REF_CHANNELS channel (docstring updated). The 12 envelope motions
(round 1 and Sassy-R2 ... Hmph-R2) keep identical reward sets (checked against 9b424b4).

Reference checked first: every joint inside its range at 0.1 s steps (min margin 0.070 rad); no
self-collision in the training model (only the soles collide there); with every collision mesh on, the
sky holds are clear and the only hull overlaps (<= 2 mm, jaw shell vs neck XL330 during slips) vanish on
the true meshes (no vertex inside, >= 5.9 mm vertex gap).

Tests: test_expressive_dance.py 12 + test_expressive_cfg.py 52 pass. Local CPU rollout (every term
finite, phase clock exact), 16-env x 3-it smoke from scratch, and a resume smoke from the 1029
checkpoint OK.

Assisted-by: Claude:claude-opus-5-5

Branches: dance-steps expressive-motions 

commit bdb798961031424ce0c30abaa3f19d843831a0af
Author: RemiFabre
Date: 2026-10-30

Dodge dance with steps: TremendousSteps tasks (contact schedule + foot targets)

Same dance as Tremendous (combo A, 110 BPM, T = 18.25 s, phase skill phi = t / T), but the legs take real steps.
Reference motion_data/tremendous_steps.csv (notes/dodge/steps/tools/steps_ref.py): every recorded pose re-solved
on its stance on the training model (full lean-back, trunk twist, joints >= 0.07 rad off their stops, knees
bending the normal way, shins / thighs >= 4 mm off the battery hull), whole-body IK every 10 ms (feet 6-D, CoM,
trunk roll / pitch / yaw), retimed so every joint stays <= 6 rad/s. 4 single-foot steps (18 mm clearance,
0.32-0.37 s swings): left foot back into limbo_L (beat 9) and home into sky_R (beat 12), right foot back into
limbo_R (beat 21) and home into slip_L (beat 24). Starts and ends on the stand footprint, still.
Kinematic facts (ledger): no ankle roll, so flat parallel soles keep a fixed ~84 mm spacing (wider needs a
deep crouch + pigeon toes); fore-aft stagger is free; the trunk twist lets the roll pass the hip-roll range
but the shin then hits the battery: flat-footed roll stays ~15-17 deg.

expressive_motions: StepMotion(DataMotion) + step_reference() (per-foot displacement from phi = 0 in the start
heading frame, clearance, contact schedule, root displacement), STEP_MOTIONS["Tremendous-Steps"] (kept out of
DATA_MOTIONS: it has trunk yaw), get_motion finds it.
mdp: ex_step_foot_track / foot_dev / contact / clearance / unscheduled_lift / root_track / slip (contact-gated
foot speed + pivot), critic obs ex_step_ref (12) + ex_step_err (8); _ex_cache also captures root0.
env cfg: for StepMotion the planted-feet costs (feet_drift, feet_lift, foot_slip, feet_grounded) are replaced by
the step terms, feet_flat is gated by contact, yaw is velocity-tracked too. step_profile "feet" doubles the
step terms (hedge). Tasks Mjlab-Expressive-TremendousSteps-MicroDuck and ...-TremendousSteps-Feet-MicroDuck,
from scratch, 7000 it. Planted tasks unchanged (actor obs identical, reward sets identical).

Tests: test_expressive_steps.py 8 pass (clean single-foot steps, still ends, terms / signs / profiles, reward
functions on hand-made states), test_expressive_dance.py 12 + test_expressive_cfg.py 52 pass. CPU rollout:
every term finite, penalties <= 0, phase clock = episode clock, and a kinematic teleport onto the reference
reads foot track 0.96-0.98 (the spawn-noise offset) and zero channel errors. 16-env x 3-it smoke of both tasks OK.

Assisted-by: Claude:claude-opus-5-5

Branches: dance-steps 

commit 83d07f24a2be6788c97252a8ba14ff6760e93c10
Author: RemiFabre
Date: 2026-10-30

Dodge dance v3: bigger, more dynamic planted Tremendous (Expressive-Tremendous-V3[-Bold] tasks)

Rémi tested tremendous-70 on the real duck: transfer is good, the choreography is too timid.
New references from notes/dodge/tools/planted_v3.py (feet still planted on the stand footprint):
side tilt +-22 deg (r2 14) on the real hip-roll range, trunk twists +-12 deg, limbo -36 deg,
a squash bounce bottoming on every beat (dz to -22 mm), head hits + chin nods on the beat, back at
the stand on beat 32 with 0.8 s still before the hand-back. Bold = same poses, harder dynamics.

Env (v3 data motions only; older tasks keep their reward sets): ground-pick robot with hip roll
+-0.52 (as ground_grasp.py), yaw in the wide trunk kernel + rate-tracked + trunk_yaw_dev,
track_height_wide (dz std 12 mm), settle_legs_dev (linear pull to HOME in the settle window:
r2 ended 13 deg off HOME and the stand net stepped), joint_overspeed threshold 7 / 8 rad/s.

Assisted-by: Claude:claude-opus-5-5

Branches: expressive-motions 

commit 4dd6989ac3d156b9c002c3ac5d98c3c7dbb8f143
Author: RemiFabre
Date: 2026-10-30

Dodge dance v4: double ding hit, head-bob groove, bob-and-weave bar (Expressive-Tremendous-V4 task)

v3 polished after the real-duck test: bars 1-3, 7, 8 unchanged; the end of bar 4 hits the two dings
(8.50 / 8.64 s, frozen through the break), bar 5 is a head-bob groove (chin down on the beat, the body
rocking and bouncing), bar 6 a bob and weave (dip / rise). Reference from notes/dodge/tools/planted_v4.py
(same checks as v3: ZMP worst -43 mm, static CoM >= 12.3 mm, joints, flat feet, true-mesh clearances).
Trained by resuming the v3 run (1nf1lu2v model_6250).

Assisted-by: Claude:claude-opus-5-5

Branches: expressive-motions 

==== FILE src/mjlab_microduck/tasks/expressive_motions.py (4dd6989)

"""Expressive body motions (2026-10-28): smooth phase-indexed references for the Expressive task family.

Each motion is a one-shot of duration T seconds, driven like the ground pick by a phase φ = t / T ∈ [0, 1)
(command = [cos 2πφ, sin 2πφ, 0]); it starts from and ends in the normal standing pose (every reference channel is 0
at φ = 0 and back to 0 before φ = 1, leaving a short settle at the end).

Reference channels (REF_CHANNELS, offsets from the standing pose):
    roll, pitch      trunk orientation (ZYX Euler of trunk_base, rad). pitch > 0 = nose DOWN (bow), < 0 = chest out.
                     roll > 0 = right side down.
    yaw              trunk yaw relative to the heading at the start of the motion (rad), > 0 = turn LEFT.
    dz               trunk height offset (m): root z - mean foot-site z, minus its HOME value (STAND_HEIGHT).
                     HOME is near full leg extension: only ~+3 mm is reachable upward, a squat goes to ~-15 mm.
    neck_pitch       > 0 = neck back / head high      (HOME 0.349, range [-1.571, 1.047])
    head_pitch       > 0 = nod down (chin down)        (HOME 0.349, range [-1.571, 1.571])
    head_yaw         > 0 = look LEFT                   (HOME 0, range ±2.967)
    head_roll        tilt                              (HOME 0, range ±0.436)

A channel is a sum of components  amp · E(t) · W(t):
    E = cosine-eased trapezoid envelope (0 before t0, rises to 1 at t1, holds to t2, falls to 0 at t3),
    W = 1 (static offset) or sin(2π f (t - t0) + ph) (oscillation), so every reference is C1 (no jumps).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import torch

REF_CHANNELS = ("roll", "pitch", "yaw", "dz", "neck_pitch", "head_pitch", "head_yaw", "head_roll")
CH = {n: i for i, n in enumerate(REF_CHANNELS)}
HEAD_JOINTS = ("neck_pitch", "head_pitch", "head_yaw", "head_roll")
# root z - mean(left_foot, right_foot site z) when standing on HOME targets: FK gives 0.1171, the BAM servos sag
# ~2 mm under the weight (measured in the env, 2026-10-28), so the zero of the dz channel is the settled stand.
STAND_HEIGHT = 0.1152


@dataclass(frozen=True)
class Comp:
    ch: str
    amp: float
    env: tuple            # (t0, t1, t2, t3) seconds
    freq: float = 0.0     # Hz; 0 = static offset
    ph: float = 0.0       # oscillation phase at t0 (rad)


@dataclass(frozen=True)
class Motion:
    name: str
    period: float                       # T (s)
    comps: tuple
    note: str = ""
    settle_from: float = 0.88           # φ from which the legs are pulled back to HOME
    extra: dict = field(default_factory=dict)


def _E(t: torch.Tensor, t0, t1, t2, t3) -> torch.Tensor:
    up = 0.5 - 0.5 * torch.cos(math.pi * torch.clamp((t - t0) / max(t1 - t0, 1e-6), 0.0, 1.0))
    dn = 0.5 + 0.5 * torch.cos(math.pi * torch.clamp((t - t2) / max(t3 - t2, 1e-6), 0.0, 1.0))
    return up * dn


def reference(motion: Motion, phi: torch.Tensor) -> torch.Tensor:
    """(N,) phase -> (N, 8) reference offsets in REF_CHANNELS order."""
    if isinstance(motion, DataMotion):
        return _data_interp(motion, phi, 0)
    t = phi * motion.period
    out = torch.zeros(phi.shape[0], len(REF_CHANNELS), device=phi.device, dtype=phi.dtype)
    for c in motion.comps:
        e = _E(t, *c.env)
        w = 1.0 if c.freq == 0.0 else torch.sin(2 * math.pi * c.freq * (t - c.env[0]) + c.ph)
        out[:, CH[c.ch]] += c.amp * e * w
    return out


def bound(motion: Motion, ch: str) -> float:
    """Upper bound of |reference| on a channel (sum of |amp|; the table's max |value| for a data motion)."""
    if isinstance(motion, DataMotion):
        return float(_data_table(motion, torch.device("cpu"), torch.float64)[1][:, CH[ch]].abs().max())
    return sum(abs(c.amp) for c in motion.comps if c.ch == ch)


# ── The motions ──────────────────────────────────────────────────────────────
PI2 = math.pi / 2

# 1. SASSY (priority): bow a little to show the tail, then wiggle it: trunk yaw ±0.22 coupled IN PHASE with a hip-level
# roll ±0.07 at 2.5 Hz (tail swings right while the right side dips -> reads as a booty wiggle from behind and 3/4),
# over a small crouch so one leg can shorten. The head looks back over the LEFT shoulder (yaw +0.6) tilted (roll +0.3)
# for the whole shake; then a sassy hold: chin up, chest up, head still tilted; back to stand.
SASSY = Motion("Sassy", 3.5, (
    # body: bow + crouch for the shake, then chest-up for the final pose
    Comp("pitch", 0.08, (0.10, 0.45, 2.30, 2.60)),
    Comp("pitch", -0.05, (2.40, 2.65, 2.95, 3.20)),
    Comp("dz", -0.006, (0.10, 0.45, 2.30, 2.60)),
    Comp("yaw", 0.22, (0.30, 0.65, 2.15, 2.50), freq=2.5),
    Comp("roll", 0.07, (0.30, 0.65, 2.15, 2.50), freq=2.5),
    # head: looking back over the shoulder, tilted, the whole time; chin up in the final hold
    Comp("head_yaw", 0.6, (0.10, 0.50, 2.90, 3.20)),
    Comp("head_roll", 0.3, (0.10, 0.50, 2.90, 3.20)),
    Comp("head_pitch", -0.25, (2.30, 2.60, 2.95, 3.20)),
    Comp("neck_pitch", 0.12, (2.30, 2.60, 2.95, 3.20)),
), note="booty wiggle 2.5 Hz (yaw+roll in phase) over a bow, head over the left shoulder; chin-up hold",
   settle_from=0.92)

# 2. PROUD / puff-up: chest out (pitch back), the little height there is, head high and chin up; hold; a small settle nod.
PROUD = Motion("Proud", 3.0, (
    Comp("pitch", -0.14, (0.15, 0.85, 2.00, 2.55)),
    Comp("pitch", 0.04, (1.95, 2.10, 2.10, 2.35)),            # settle: a small forward dip as the chest comes down
    Comp("dz", 0.002, (0.15, 0.85, 2.00, 2.55)),
    Comp("neck_pitch", 0.25, (0.15, 0.85, 2.00, 2.55)),
    Comp("head_pitch", -0.30, (0.25, 0.95, 2.00, 2.55)),
    Comp("head_pitch", 0.08, (1.95, 2.10, 2.10, 2.40)),       # settle nod
), note="chest out, head high, chin up; hold; small settle")

# 3. SHY / bashful: small crouch, hunch forward, slow body twist side to side (kid twisting, 0.8 Hz), head down and
# turned away. Head-forward shallow (head mass forward makes the real duck step).
SHY = Motion("Shy", 3.5, (
    Comp("dz", -0.008, (0.15, 0.80, 2.75, 3.20)),
    Comp("pitch", 0.07, (0.15, 0.80, 2.75, 3.20)),
    Comp("yaw", 0.15, (0.50, 0.90, 2.45, 2.95), freq=0.8),
    Comp("head_pitch", 0.30, (0.15, 0.80, 2.75, 3.20)),
    Comp("neck_pitch", -0.10, (0.15, 0.80, 2.75, 3.20)),
    Comp("head_yaw", -0.50, (0.20, 0.90, 2.75, 3.20)),
    Comp("head_roll", 0.15, (0.20, 0.90, 2.75, 3.20)),
), note="crouch, hunch, slow 0.8 Hz twist, head down and turned away", settle_from=0.92)

# 4. EXCITED bounce: small squats at 3 Hz (dz from 0 to -12 mm), feet planted, head bobbing in sync, looking up.
EXCITED = Motion("Excited", 3.0, (
    Comp("dz", -0.006, (0.15, 0.45, 2.25, 2.60)),
    Comp("dz", 0.006, (0.15, 0.45, 2.25, 2.60), freq=3.0, ph=PI2),   # -0.006 + 0.006 cos: 0 .. -12 mm
    Comp("head_pitch", -0.10, (0.15, 0.45, 2.25, 2.60)),
    Comp("head_pitch", 0.10, (0.15, 0.45, 2.25, 2.60), freq=3.0, ph=-PI2),  # nod down at the squat bottom
    Comp("neck_pitch", 0.10, (0.15, 0.45, 2.25, 2.60)),
), note="3 Hz squats 0..-12 mm, head bobbing in sync, looking up")

# 5. GIGGLE: belly laugh, a fast small trunk shake (pitch ±0.04, roll ±0.03 at 5 Hz, 90° apart: a little circle)
# while leaning back with the head tossed back and bobbing.
GIGGLE = Motion("Giggle", 2.5, (
    Comp("pitch", -0.05, (0.10, 0.40, 1.70, 2.00)),
    Comp("pitch", 0.04, (0.25, 0.45, 1.60, 1.90), freq=5.0),
    Comp("roll", 0.03, (0.25, 0.45, 1.60, 1.90), freq=5.0, ph=PI2),
    Comp("head_pitch", -0.25, (0.10, 0.40, 1.75, 2.05)),
    Comp("head_pitch", 0.06, (0.25, 0.45, 1.60, 1.90), freq=5.0),
    Comp("neck_pitch", 0.15, (0.10, 0.40, 1.75, 2.05)),
), note="5 Hz pitch/roll shake, leaning back, head tossed back")

# 6. HMPH turn-away (my pick): snap the trunk away on planted feet (yaw -0.35: the hip yaws allow ~0.43, a true
# quarter turn needs a step), nose in the air, head turned further away, a small chin flick; hold; turn back.
HMPH = Motion("Hmph", 3.5, (
    Comp("yaw", -0.35, (0.15, 0.55, 2.40, 3.00)),
    Comp("roll", -0.04, (0.15, 0.55, 2.40, 3.00)),
    Comp("pitch", -0.05, (0.15, 0.55, 2.40, 3.00)),
    Comp("head_yaw", -0.50, (0.20, 0.55, 2.40, 3.00)),
    Comp("head_pitch", -0.25, (0.20, 0.55, 2.40, 3.00)),
    Comp("head_pitch", -0.10, (0.95, 1.10, 1.10, 1.40)),       # "hmph" chin flick
    Comp("neck_pitch", 0.15, (0.20, 0.55, 2.40, 3.00)),
    Comp("head_roll", -0.15, (0.20, 0.55, 2.40, 3.00)),
), note="trunk turned away on planted feet, nose up, chin flick, back")

MOTIONS = {m.name: m for m in (SASSY, PROUD, SHY, EXCITED, GIGGLE, HMPH)}


# ── Round 2 (2026-10-28 night, notes/expressive/LEDGER.md "Round 2") ────────────────────────────────────────────────
# Round 1 eval: the oscillations barely appeared (Sassy wiggle x0.37 and out of phase, Giggle shake x0.19, Excited
# sagged instead of bouncing), Hmph parked the left hip yaw on its stop, and the stand net stepped at the hand-back.
# Round 2 references: slower / feasible oscillations, Hmph turns -18°, and EVERY envelope closes (value AND
# velocity 0, the cosine envelope has zero slope at t3) by φ ≤ R2_END_PHI, then a still stand until the hand-back.
# Registered as Mjlab-Expressive-<Name>-R2-MicroDuck (motion key "<Name>-R2"), trained from scratch.
R2_END_PHI = 0.87

SASSY_R2 = Motion("Sassy", 3.5, (
    Comp("pitch", 0.08, (0.10, 0.45, 2.15, 2.45)),
    Comp("pitch", -0.05, (2.30, 2.50, 2.75, 3.00)),
    Comp("dz", -0.006, (0.10, 0.45, 2.15, 2.45)),
    Comp("yaw", 0.22, (0.30, 0.65, 1.95, 2.30), freq=2.0),      # 2 Hz: 4 swings of the tail
    Comp("roll", 0.07, (0.30, 0.65, 1.95, 2.30), freq=2.0),     # in phase with the yaw
    Comp("head_yaw", 0.6, (0.10, 0.50, 2.70, 3.00)),
    Comp("head_roll", 0.3, (0.10, 0.50, 2.70, 3.00)),
    Comp("head_pitch", -0.25, (2.25, 2.50, 2.75, 3.00)),
    Comp("neck_pitch", 0.12, (2.25, 2.50, 2.75, 3.00)),
), note="r2: booty wiggle 2.0 Hz (yaw ±0.22 + roll ±0.07 in phase) over a bow, head over the left shoulder; chin-up hold",
   settle_from=0.88)

PROUD_R2 = Motion("Proud", 3.0, PROUD.comps, note="r2: " + PROUD.note, settle_from=0.88)   # ends at φ 0.85 already

SHY_R2 = Motion("Shy", 3.5, (
    Comp("dz", -0.008, (0.15, 0.80, 2.55, 3.00)),
    Comp("pitch", 0.07, (0.15, 0.80, 2.55, 3.00)),
    Comp("yaw", 0.15, (0.50, 0.90, 2.25, 2.75), freq=0.8),
    Comp("head_pitch", 0.30, (0.15, 0.80, 2.55, 3.00)),
    Comp("neck_pitch", -0.10, (0.15, 0.80, 2.55, 3.00)),
    Comp("head_yaw", -0.50, (0.20, 0.90, 2.55, 3.00)),
    Comp("head_roll", 0.15, (0.20, 0.90, 2.55, 3.00)),
), note="r2: crouch, hunch, slow 0.8 Hz twist, head down and turned away; ends at φ 0.86", settle_from=0.88)

EXCITED_R2 = Motion("Excited", 3.0, (
    Comp("dz", -0.007, (0.15, 0.45, 2.15, 2.55)),
    Comp("dz", 0.007, (0.15, 0.45, 2.15, 2.55), freq=2.5, ph=PI2),    # -0.007 + 0.007 cos: 0 .. -14 mm, 6 bounces
    Comp("head_pitch", -0.10, (0.15, 0.45, 2.15, 2.55)),
    Comp("head_pitch", 0.10, (0.15, 0.45, 2.15, 2.55), freq=2.5, ph=-PI2),
    Comp("neck_pitch", 0.10, (0.15, 0.45, 2.15, 2.55)),
), note="r2: 2.5 Hz squats 0..-14 mm (height-rate tracked), head bobbing in sync, looking up", settle_from=0.88)

GIGGLE_R2 = Motion("Giggle", 2.5, (
    Comp("pitch", -0.05, (0.10, 0.40, 1.70, 2.00)),
    Comp("roll", 0.08, (0.25, 0.45, 1.55, 1.85), freq=4.0),            # the shake: ±0.08 rad at 4 Hz
    Comp("head_pitch", -0.25, (0.10, 0.40, 1.75, 2.05)),
    Comp("head_pitch", 0.06, (0.25, 0.45, 1.55, 1.85), freq=4.0),
    Comp("neck_pitch", 0.15, (0.10, 0.40, 1.75, 2.05)),
), note="r2: 4 Hz roll shake ±0.08 (roll-rate tracked), leaning back, head tossed back", settle_from=0.88)

HMPH_R2 = Motion("Hmph", 3.5, (
    Comp("yaw", -math.radians(18.0), (0.15, 0.55, 2.40, 3.00)),       # -18°: off the hip-yaw stops
    Comp("roll", -0.04, (0.15, 0.55, 2.40, 3.00)),
    Comp("pitch", -0.05, (0.15, 0.55, 2.40, 3.00)),
    Comp("head_yaw", -0.50, (0.20, 0.55, 2.40, 3.00)),
    Comp("head_pitch", -0.25, (0.20, 0.55, 2.40, 3.00)),
    Comp("head_pitch", -0.10, (0.95, 1.10, 1.10, 1.40)),
    Comp("neck_pitch", 0.15, (0.20, 0.55, 2.40, 3.00)),
    Comp("head_roll", -0.15, (0.20, 0.55, 2.40, 3.00)),
), note="r2: trunk turned away -18° on planted feet, nose up, chin flick, back", settle_from=0.88)

MOTIONS_R2 = {m.name: m for m in (SASSY_R2, PROUD_R2, SHY_R2, EXCITED_R2, GIGGLE_R2, HMPH_R2)}
# Every motion by key: "Sassy" (round 1), "Sassy-R2" (round 2). The reward / obs functions look motions up here.
ALL_MOTIONS = {**MOTIONS, **{f"{k}-R2": v for k, v in MOTIONS_R2.items()}}
TRUNK_CHANNELS = ("roll", "pitch", "yaw", "dz")


def get_motion(key: str):
    return ALL_MOTIONS[key] if key in ALL_MOTIONS else DATA_MOTIONS[key]


def reference_rate(motion: Motion, phi: torch.Tensor, h: float = 0.002) -> torch.Tensor:
    """(N,) phase -> (N, 8) time derivative of the reference (units / s), central difference over ±h seconds
    (a data motion interpolates its stored analytic rates)."""
    if isinstance(motion, DataMotion):
        return _data_interp(motion, phi, 1)
    dphi = h / motion.period
    return (reference(motion, phi + dphi) - reference(motion, phi - dphi)) / (2.0 * h)


def osc_channels(motion: Motion) -> tuple:
    """Trunk channels with an oscillating component (velocity-tracked in round 2; a data motion lists them)."""
    if isinstance(motion, DataMotion):
        return motion.rate_channels
    return tuple(ch for ch in TRUNK_CHANNELS if any(c.ch == ch and c.freq > 0.0 for c in motion.comps))


def peak_rate(motion: Motion, ch: str, n: int = 4001) -> float:
    phi = torch.linspace(0.0, 1.0, n, dtype=torch.float64)
    return float(reference_rate(motion, phi)[:, CH[ch]].abs().max())


# ── Data-driven motions (2026-10-29, notes/dodge): a 50 Hz table instead of envelopes ──────────────────────────────
# The dodge dance "Tremendous" (combo A, 110 BPM, 32 beats + tail, T = the music excerpt, 18.25 s) re-solved with
# BOTH FEET PLANTED on the stand footprint (notes/dodge/tools/planted_ref.py): every key pose keeps its trunk lean
# direction, face direction and head offset as far as a static CoM >= 10 mm inside the soles and the joint ranges
# allow; min-jerk snaps that arrive ON the beat; back to the stand (value and rate 0) before settle_from.
# File columns: t, the 8 REF_CHANNELS, then their analytic time derivatives d_<ch> (per s). Kept OUT of ALL_MOTIONS
# (its amplitudes exceed the small-motion test bounds); get_motion() finds it by key.
MOTION_DATA = Path(__file__).parent / "motion_data"


@dataclass(frozen=True)
class DataMotion:
    name: str
    period: float                       # T (s) = the table's duration (music excerpt)
    file: str                           # CSV in motion_data/
    trunk_scale: float = 1.0            # scales roll / pitch / yaw / dz (head channels untouched)
    note: str = ""
    settle_from: float = 0.982          # φ from which the legs are pulled back to HOME (stand reached at 17.80 s = φ 0.975)
    settle_ramp: float = 0.01           # φ width of the settle gate (0.18 s at 18.25 s)
    rate_channels: tuple = ("roll", "pitch", "dz")   # trunk channels velocity-tracked
    comps: tuple = ()                   # no envelope components
    # v3 (2026-10-30, LEDGER "Tremendous v3"): bigger / more dynamic dance. None / defaults = the 1029 / r2 behaviour.
    hip_roll_range: float | None = None # training robot's hip roll range (+-rad); None = the export's +-0.384
    overspeed: float = 5.0              # joint_overspeed threshold (rad/s)
    v3: bool = False                    # trunk yaw in the wide kernel + yaw dev cost, wide dz kernel, linear settle cost


_DATA_CACHE: dict = {}


def _data_table(motion: DataMotion, device, dtype):
    """(dt, values (n, 8), rates (n, 8)) on device, trunk channels scaled."""
    key = (motion.file, motion.trunk_scale, str(device), dtype)
    if key not in _DATA_CACHE:
        a = np.loadtxt(MOTION_DATA / motion.file, delimiter=",", comments="#")
        s = np.ones(len(REF_CHANNELS))
        s[[CH[c] for c in TRUNK_CHANNELS]] = motion.trunk_scale
        _DATA_CACHE[key] = (float(a[1, 0] - a[0, 0]),
                            torch.as_tensor(a[:, 1:9] * s, device=device, dtype=dtype),
                            torch.as_tensor(a[:, 9:17] * s, device=device, dtype=dtype))
    return _DATA_CACHE[key]


def _data_interp(motion: DataMotion, phi: torch.Tensor, which: int) -> torch.Tensor:
    dt, *tabs = _data_table(motion, phi.device, phi.dtype)
    tab = tabs[which]
    x = torch.clamp(phi * motion.period / dt, 0.0, tab.shape[0] - 1.0)
    i0 = torch.clamp(x.floor().long(), max=tab.shape[0] - 2)
    w = (x - i0.to(x.dtype)).unsqueeze(-1)
    return tab[i0] * (1.0 - w) + tab[i0 + 1] * w


_TREMENDOUS_NOTE = ("dodge dance A (Tremendous), feet planted on the stand footprint: slips / sways / limbos / dips "
                    "on every beat at 110 BPM, beak to the sky in bar 4 and at the end")
_V3_NOTE = ("dodge dance A (Tremendous) v3, feet planted: the same bars, bigger and more dynamic (notes/dodge/tools/"
            "planted_v3.py): side tilts +-22 deg on the real hip-roll range (r2: 14; the high-side shin meeting the trunk "
            "and the leg length stop it there), trunk twists +-12 deg, limbo lean -36 deg, a squash bounce bottoming ON "
            "every beat (dz to -22 mm, r2: -2.4), head hits (overshoot + settle) and chin nods on the beat, head yaw to "
            "+-0.74 rad, beak 61 deg up in the sky holds; back at the stand on beat 32 (17.45 s), still after")
# v3: the stand is reached at 17.4545 s (beat 32); settle_from 0.962 = 17.56 s, the gate is full from 17.74 s.
_V3 = dict(settle_from=0.962, rate_channels=("roll", "pitch", "yaw", "dz"), hip_roll_range=0.52, v3=True)
DATA_MOTIONS = {
    "Tremendous": DataMotion("Tremendous", 18.25, "tremendous_planted.csv", note=_TREMENDOUS_NOTE),
    "Tremendous-70": DataMotion("Tremendous", 18.25, "tremendous_planted.csv", trunk_scale=0.7,
                                note=_TREMENDOUS_NOTE + "; trunk channels x0.7, head unchanged (safer variant)"),
    "Tremendous-V3": DataMotion("Tremendous-V3", 18.25, "tremendous_v3.csv", note=_V3_NOTE, overspeed=7.0, **_V3),
    "Tremendous-V3-Bold": DataMotion("Tremendous-V3-Bold", 18.25, "tremendous_v3_bold.csv", overspeed=8.0,
                                     note=_V3_NOTE + "; BOLD: the same key poses, harder dynamics (design 6.5 / 8 rad/s, "
                                                     "ZMP allowed 35 mm out of the soles instead of 25, head hits 22 % "
                                                     "instead of 15 %, chin nods 0.16 rad instead of 0.12)", **_V3),
    # v4 = v3 polished after Rémi played v3 on the real duck; resumed from the v3 run (LEDGER "Tremendous v4").
    "Tremendous-V4": DataMotion("Tremendous-V4", 18.25, "tremendous_v4.csv", overspeed=7.0,
                                note=_V3_NOTE + "; V4 (notes/dodge/tools/planted_v4.py): bars 1-3, 7, 8 unchanged; a double "
                                                "hit on the two dings (8.50 / 8.64 s, frozen through the break), a head-bob "
                                                "groove opening the second half (chin down on the beat, the body rocking) "
                                                "and a bob-and-weave bar (dip / rise)", **_V3),
}

==== FILE src/mjlab_microduck/tasks/microduck_expressive_env_cfg.py (4dd6989)

"""Microduck EXPRESSIVE body motions (2026-10-28, notes/expressive/BRIEF.md): the body moves, the feet stay planted.

One env factory per motion name (tasks/expressive_motions.py), registered as Mjlab-Expressive-<Name>-MicroDuck.
Built ON the ground-pick env (same 61-D obs, 14 actions, phase command [cos 2πφ, sin 2πφ, 0] in the twist slots,
head/body command slots zero, DR / obs-noise / delay stack), one motion per episode from φ = 0 (standing):
    φ = t / T, T = the motion's period; episode length = T; robotd drives φ per tick exactly like the ground pick.

Rewards (functions of φ): track the reference (trunk roll / pitch / yaw-from-start / height offset, 4 head joints),
feet planted (horizontal drift from the start position, lift above the start height, slip speed, plus the ground
pick's feet_grounded / feet_flat), back to the standing leg pose at the end, the usual regularisers, targets clamped to
the joint ranges ±0.1 with an overrun tax (grasp lesson), joint overspeed, fall termination.

FRICTION REALISM (Rémi's hypothesis: the real feet are very grippy, the sim let emotions glide): foot friction
U(1.0, 2.0) instead of (0.7, 1.3), and the grasp env's sticky contacts (elliptic cone, impratio 10), so the motion
has to come from the joints, not from sliding the feet.
"""

import math
from copy import deepcopy
from dataclasses import replace
from functools import lru_cache

import mujoco
from mjlab.envs import ManagerBasedRlEnvCfg
from mjlab.envs.mdp.actions import JointPositionActionCfg
from mjlab.managers import CurriculumTermCfg, ObservationTermCfg, RewardTermCfg, TerminationTermCfg
from mjlab.managers.scene_entity_config import SceneEntityCfg
from mjlab.rl import RslRlModelCfg, RslRlOnPolicyRunnerCfg
from mjlab.tasks.velocity import mdp

from mjlab_microduck.robot.microduck_constants import MICRODUCK_GROUND_PICK_ROBOT_CFG, get_ground_pick_spec
from mjlab_microduck.tasks import mdp as microduck_mdp
from mjlab_microduck.tasks.expressive_motions import DataMotion, get_motion, osc_channels, peak_rate
from mjlab_microduck.tasks.microduck_ground_pick_env_cfg import make_microduck_ground_pick_env_cfg
from mjlab_microduck.tasks.symmetry import PpoWithSymmetryCfg

SERVO_JOINTS = ("left_hip_yaw", "left_hip_roll", "left_hip_pitch", "left_knee", "left_ankle",
                "neck_pitch", "head_pitch", "head_yaw", "head_roll",
                "right_hip_yaw", "right_hip_roll", "right_hip_pitch", "right_knee", "right_ankle")

FOOT_FRICTION = (1.0, 2.0)
RESET_JOINT_NOISE = 0.08          # robotd starts from the stand net's settled stance (up to ~0.14 rad off HOME)
TARGET_CLIP_MARGIN = 0.10
ACTION_OVERRUN_WEIGHT = -10.0
FALL_ANGLE_DEG = 60.0

# Tracking (positive). std ≈ the error still worth paying for.
W_TRACK_ROLL, STD_ROLL = 2.5, 0.04
W_TRACK_PITCH, STD_PITCH = 2.5, 0.05
W_TRACK_YAW, STD_YAW = 3.0, 0.08
W_TRACK_HEIGHT, STD_HEIGHT = 2.0, 0.004
W_TRACK_HEAD, STD_HEAD = 3.0, 0.12
W_SETTLE_LEGS = 4.0
# Feet planted (costs, negative weights).
W_FEET_DRIFT = -40.0      # per m of summed horizontal drift (1 cm on both feet: -0.8 / step)
W_FEET_LIFT = -100.0      # per m above the start height + 3 mm
W_FOOT_SLIP = -2.0        # per m/s of summed foot speed

# Round 2 (motion key "<Name>-R2", trained from scratch). See LEDGER.md "Round 2".
W_OSC_BOOST = 1.6         # position-tracking weight multiplier on the oscillating trunk channels
W_TRACK_RATE = 3.0        # velocity tracking of each oscillating trunk channel (rate vs d/dt of the reference)
RATE_STD_FRAC = 0.35      # rate kernel std = this x the channel's peak reference rate (floored below)
RATE_STD_MIN = {"roll": 0.15, "pitch": 0.15, "yaw": 0.15, "dz": 0.01}
W_TRACK_HEAD_WIDE, STD_HEAD_WIDE = 1.5, 0.4   # gradient at a 1.5 rad head error (r1's 0.12 kernel had none)
W_NECK_DEV, NECK_DEV_FREE = -5.0, 0.3         # per rad of |neck - reference| beyond 0.3 rad
W_JOINT_LIMIT, JOINT_LIMIT_MARGIN = 2.0, 0.05 # self-negating: -(intrusion into the last 0.05 rad / 0.05)^2 per joint
W_SETTLE_STILL = -0.05    # per (rad/s)^2 of summed servo speed after settle_from (still robot at the hand-back)
RATE_NAMES = {"roll": "track_roll", "pitch": "track_pitch", "yaw": "track_yaw", "dz": "track_height"}
# Data motions (the dodge dance, 2026-10-29): round 2 terms + a wide trunk kernel (the trunk swings ±13° on every beat,
# the narrow 0.04 / 0.05 rad kernels alone give no gradient while the policy is far off).
W_TRACK_TRUNK_WIDE, STD_TRUNK_WIDE = 1.5, 0.15
DATA_MAX_ITERATIONS = 7000      # 18.25 s episodes (912 steps): ~6x longer than round 2's, see LEDGER "dodge"
# Data motions, r2 (2026-10-30, LEDGER "Tremendous r2"): the 1029 runs parked head_pitch 2.3 rad off (chin down in both
# sky poses) and never leaned right (roll -2..-5° where the reference asks +9.5..+13°). Far off, the Gaussian kernels
# give no gradient, so the head joints and the trunk roll get neck_dev's linear cost (per rad beyond a free band).
W_HEAD_DEV, HEAD_DEV_FREE = -5.0, 0.25            # head_pitch + head_yaw (also stops the -146° yaw at the end)
W_HEAD_ROLL_DEV, HEAD_ROLL_DEV_FREE = -5.0, 0.15  # head_roll (range ±0.44, reference ±0.35)
W_TRUNK_ROLL_DEV, TRUNK_ROLL_DEV_FREE = -10.0, 0.05   # trunk roll: ~3° free, errors are ~5x smaller than the head's
# Data motions, v3 (2026-10-30, LEDGER "Tremendous v3"): the dance gets trunk twists (yaw), a squash bounce (dz to
# -21 mm), the real hip-roll range, and a longer still tail. r2 A ended ~13° off HOME at the hips / ankles (the 0.15-std
# settle_legs kernel has little gradient there) and the stand net stepped + turned 28° after the hand-back.
W_TRUNK_YAW_DEV, TRUNK_YAW_DEV_FREE = -10.0, 0.05     # trunk yaw: same linear cost as the roll
W_TRACK_HEIGHT_WIDE, STD_HEIGHT_WIDE = 1.0, 0.012     # dz: the 4 mm kernel alone is blind 15 mm off
W_SETTLE_LEGS_DEV, SETTLE_LEGS_DEV_FREE = -4.0, 0.03  # per rad of |leg joint - HOME| beyond 0.03, in the settle window


def _hip_roll_spec(hip_roll: float):
    def spec_fn() -> mujoco.MjSpec:
        """The ground-pick robot with the real hip-roll range (ground_grasp.py: the export's +-0.384 is conservative,
        the physical robot was posed at 0.463 rad and rests at -0.566)."""
        spec = get_ground_pick_spec()
        for jn in ("left_hip_roll", "right_hip_roll"):
            spec.joint(jn).range = [-hip_roll, hip_roll]
        return spec
    return spec_fn


@lru_cache(maxsize=4)
def expressive_joint_limits(hip_roll: float | None = None) -> dict:
    """{servo joint: (lo, hi)} on the ground-pick model (hip roll +-`hip_roll` if given), in the 14-servo order."""
    m = (get_ground_pick_spec() if hip_roll is None else _hip_roll_spec(hip_roll)()).compile()
    return {jn: tuple(float(v) for v in m.jnt_range[mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, jn)])
            for jn in SERVO_JOINTS}


def make_microduck_expressive_env_cfg(motion: str, play: bool = False) -> ManagerBasedRlEnvCfg:
    mo = get_motion(motion)
    cfg = make_microduck_ground_pick_env_cfg(play=play, rough=False)
    hip_roll = getattr(mo, "hip_roll_range", None)
    if hip_roll is not None:
        cfg.scene.entities = {"robot": replace(MICRODUCK_GROUND_PICK_ROBOT_CFG, spec_fn=_hip_roll_spec(hip_roll))}

    # ── One motion per episode, from φ = 0 (standing) ──────────────────────────
    cfg.episode_length_s = mo.period
    cfg.commands["twist"].randomize_phase = False
    cfg.commands["twist"].period = mo.period

    # ── Friction realism: grippy feet + sticky contacts ────────────────────────
    cfg.sim.mujoco.cone = "elliptic"
    cfg.sim.mujoco.impratio = 10.0
    cfg.events["foot_friction"].params["ranges"] = FOOT_FRICTION

    # ── Drop the ground-pick task terms ────────────────────────────────────────
    for name in ("mouth_ground_proximity", "mouth_perpendicular_to_ground", "ground_pick_return_pose_legs",
                 "ground_pick_return_pose_neck", "return_upright", "neck_vel_descent", "mouth_payload_force",
                 "upright"):
        cfg.rewards.pop(name, None)
    cfg.events.pop("sample_mouth_payload", None)
    cfg.events["reset_robot_joints"].params["position_range"] = (-RESET_JOINT_NOISE, RESET_JOINT_NOISE)

    # ── Reference tracking ─────────────────────────────────────────────────────
    def track(chs, w, std):
        return RewardTermCfg(func=microduck_mdp.ex_track, weight=w,
                             params={"motion": motion, "channels": chs, "std": std, "command_name": "twist"})

    cfg.rewards["track_roll"] = track(("roll",), W_TRACK_ROLL, STD_ROLL)
    cfg.rewards["track_pitch"] = track(("pitch",), W_TRACK_PITCH, STD_PITCH)
    cfg.rewards["track_yaw"] = track(("yaw",), W_TRACK_YAW, STD_YAW)
    cfg.rewards["track_height"] = track(("dz",), W_TRACK_HEIGHT, STD_HEIGHT)
    cfg.rewards["track_head"] = track(("neck_pitch", "head_pitch", "head_yaw", "head_roll"), W_TRACK_HEAD, STD_HEAD)
    cfg.rewards["settle_legs"] = RewardTermCfg(
        func=microduck_mdp.ex_settle_legs, weight=W_SETTLE_LEGS,
        params={"settle_from": mo.settle_from, "command_name": "twist", **_ramp(mo)},
    )

    # ── Feet planted (feet_grounded / feet_flat come from the ground pick) ─────
    cfg.rewards["feet_drift"] = RewardTermCfg(func=microduck_mdp.ex_feet_drift, weight=W_FEET_DRIFT)
    cfg.rewards["feet_lift"] = RewardTermCfg(func=microduck_mdp.ex_feet_lift, weight=W_FEET_LIFT)
    cfg.rewards["foot_slip"] = RewardTermCfg(func=microduck_mdp.ex_foot_slip, weight=W_FOOT_SLIP)

    # ── Regularisers: motion-blockers low (the trunk is MEANT to rotate) ───────
    cfg.rewards["body_ang_vel"].weight = -0.02
    cfg.rewards["angular_momentum"].weight = -0.01
    cfg.rewards["joint_overspeed"] = RewardTermCfg(
        func=microduck_mdp.joint_overspeed_penalty, weight=0.15, params={"threshold": getattr(mo, "overspeed", 5.0)},
    )
    jp = cfg.actions["joint_pos"]
    assert isinstance(jp, JointPositionActionCfg)
    limits = expressive_joint_limits(hip_roll)
    jp.clip = {jn: (lo - TARGET_CLIP_MARGIN, hi + TARGET_CLIP_MARGIN) for jn, (lo, hi) in limits.items()}
    cfg.rewards["action_overrun"] = RewardTermCfg(
        func=microduck_mdp.action_target_overrun_l1, weight=ACTION_OVERRUN_WEIGHT,
        params={"limits": [list(v) for v in limits.values()]},
    )
    cfg.curriculum["action_rate_weight"].params["weight_stages"] = [
        {"step": 0, "weight": -0.5},
        {"step": 500 * 24, "weight": -1.0},
        {"step": 1000 * 24, "weight": -1.5},
    ]

    # ── Critic: the reference, the errors, the feet offsets (actor stays 61-D) ─
    critic = cfg.observations["critic"].terms
    critic["ex_reference"] = ObservationTermCfg(func=microduck_mdp.ex_reference_obs, params={"motion": motion})
    critic["ex_error"] = ObservationTermCfg(func=microduck_mdp.ex_error_obs, params={"motion": motion})
    critic["ex_feet_offset"] = ObservationTermCfg(func=microduck_mdp.ex_feet_offset_obs)

    if motion.endswith("-R2") or isinstance(mo, DataMotion):
        _add_round2_terms(cfg, motion, mo)
    if isinstance(mo, DataMotion):
        cfg.rewards["track_trunk_wide"] = RewardTermCfg(
            func=microduck_mdp.ex_track, weight=W_TRACK_TRUNK_WIDE,
            params={"motion": motion, "channels": ("roll", "pitch", "yaw") if mo.v3 else ("roll", "pitch"),
                    "std": STD_TRUNK_WIDE, "command_name": "twist"},
        )
        devs = [("head_dev", W_HEAD_DEV, ("head_pitch", "head_yaw"), HEAD_DEV_FREE),
                ("head_roll_dev", W_HEAD_ROLL_DEV, ("head_roll",), HEAD_ROLL_DEV_FREE),
                ("trunk_roll_dev", W_TRUNK_ROLL_DEV, ("roll",), TRUNK_ROLL_DEV_FREE)]
        if mo.v3:
            devs.append(("trunk_yaw_dev", W_TRUNK_YAW_DEV, ("yaw",), TRUNK_YAW_DEV_FREE))
        for name, w, chs, free in devs:
            cfg.rewards[name] = RewardTermCfg(
                func=microduck_mdp.ex_head_dev_cost, weight=w,
                params={"motion": motion, "channels": chs, "free": free, "command_name": "twist"},
            )
        if mo.v3:
            cfg.rewards["track_height_wide"] = RewardTermCfg(
                func=microduck_mdp.ex_track, weight=W_TRACK_HEIGHT_WIDE,
                params={"motion": motion, "channels": ("dz",), "std": STD_HEIGHT_WIDE, "command_name": "twist"},
            )
            cfg.rewards["settle_legs_dev"] = RewardTermCfg(
                func=microduck_mdp.ex_settle_legs_dev, weight=W_SETTLE_LEGS_DEV,
                params={"settle_from": mo.settle_from, "free": SETTLE_LEGS_DEV_FREE, "command_name": "twist", **_ramp(mo)},
            )

    # ── A fall ends the episode ────────────────────────────────────────────────
    cfg.terminations["fell_over"] = TerminationTermCfg(
        func=mdp.bad_orientation, params={"limit_angle": math.radians(FALL_ANGLE_DEG)}, time_out=False,
    )
    return cfg


def _add_round2_terms(cfg: ManagerBasedRlEnvCfg, motion: str, mo) -> None:
    """Round 2: oscillations tracked in velocity too (and weighted up), a wide head kernel + neck-dive cost, joints
    kept off their stops, a still robot at the hand-back."""
    for ch in osc_channels(mo):
        cfg.rewards[RATE_NAMES[ch]].weight *= W_OSC_BOOST
        std = max(RATE_STD_FRAC * peak_rate(mo, ch), RATE_STD_MIN[ch])
        cfg.rewards[f"{RATE_NAMES[ch]}_rate"] = RewardTermCfg(
            func=microduck_mdp.ex_track_rate, weight=W_TRACK_RATE,
            params={"motion": motion, "channel": ch, "std": std, "command_name": "twist"},
        )
    cfg.rewards["track_head_wide"] = RewardTermCfg(
        func=microduck_mdp.ex_track, weight=W_TRACK_HEAD_WIDE,
        params={"motion": motion, "channels": ("neck_pitch", "head_pitch", "head_yaw", "head_roll"),
                "std": STD_HEAD_WIDE, "command_name": "twist"},
    )
    cfg.rewards["neck_dev"] = RewardTermCfg(
        func=microduck_mdp.ex_head_dev_cost, weight=W_NECK_DEV,
        params={"motion": motion, "channels": ("neck_pitch",), "free": NECK_DEV_FREE, "command_name": "twist"},
    )
    cfg.rewards["joint_limit_proximity"] = RewardTermCfg(
        func=microduck_mdp.joint_limit_proximity_penalty, weight=W_JOINT_LIMIT,
        params={"margin": JOINT_LIMIT_MARGIN, "asset_cfg": SceneEntityCfg("robot", joint_names=SERVO_JOINTS)},
    )
    cfg.rewards["settle_still"] = RewardTermCfg(
        func=microduck_mdp.ex_settle_still, weight=W_SETTLE_STILL,
        params={"settle_from": mo.settle_from, "command_name": "twist", **_ramp(mo)},
    )


def _ramp(mo) -> dict:
    """A data motion is 18 s long: its settle gate ramps over settle_ramp (φ) instead of the default 0.04."""
    return {"ramp": mo.settle_ramp} if isinstance(mo, DataMotion) else {}


def make_expressive_rl_cfg(motion: str) -> RslRlOnPolicyRunnerCfg:
    name = f"expressive_{motion.lower().replace('-', '_')}"
    iters = DATA_MAX_ITERATIONS if isinstance(get_motion(motion), DataMotion) else 3000
    return RslRlOnPolicyRunnerCfg(
        actor=RslRlModelCfg(
            hidden_dims=(512, 256, 128), activation="elu", obs_normalization=True,
            distribution_cfg={"class_name": "GaussianDistribution", "init_std": 1.0, "std_type": "scalar"},
        ),
        critic=RslRlModelCfg(hidden_dims=(512, 256, 128), activation="elu", obs_normalization=True),
        algorithm=PpoWithSymmetryCfg(
            value_loss_coef=1.0, use_clipped_value_loss=True, clip_param=0.2, entropy_coef=0.01,
            num_learning_epochs=5, num_mini_batches=4, learning_rate=1.0e-3, schedule="adaptive",
            gamma=0.99, lam=0.95, desired_kl=0.01, max_grad_norm=1.0, symmetry_cfg=None,
        ),
        wandb_project="mjlab_microduck",
        experiment_name=name,
        run_name=name,
        save_interval=250,
        num_steps_per_env=24,
        max_iterations=iters,
    )

==== FILE motion_data CSV headers (first two lines each)

-- tremendous_planted.csv (4dd6989)
# Tremendous, planted feet (notes/dodge/tools/planted_ref.py, 2026-10-29). 50 Hz, t = phi * T, T = 18.25 s; channels = expressive_motions.REF_CHANNELS offsets from the stand (rad, dz in m); d_* = time derivatives (per s, analytic min-jerk). Stand reached at 17.80 s, still after.
# t,roll,pitch,yaw,dz,neck_pitch,head_pitch,head_yaw,head_roll,d_roll,d_pitch,d_yaw,d_dz,d_neck_pitch,d_head_pitch,d_head_yaw,d_head_roll

-- tremendous_v3.csv (4dd6989)
# Tremendous v3 (notes/dodge/tools/planted_v3.py --variant v3, 2026-10-30): planted feet, bigger and more dynamic (twists, squash bounce on the beat, head hits). 50 Hz, t = phi * T, T = 18.25 s; channels = expressive_motions.REF_CHANNELS offsets from the stand (rad, dz in m); d_* = time derivatives (per s, analytic). Stand reached at 17.455 s (beat 32), still after.
# t,roll,pitch,yaw,dz,neck_pitch,head_pitch,head_yaw,head_roll,d_roll,d_pitch,d_yaw,d_dz,d_neck_pitch,d_head_pitch,d_head_yaw,d_head_roll

-- tremendous_v3_bold.csv (4dd6989)
# Tremendous v3_bold (notes/dodge/tools/planted_v3.py --variant bold, 2026-10-30): planted feet, bigger and more dynamic (twists, squash bounce on the beat, head hits). 50 Hz, t = phi * T, T = 18.25 s; channels = expressive_motions.REF_CHANNELS offsets from the stand (rad, dz in m); d_* = time derivatives (per s, analytic). Stand reached at 17.455 s (beat 32), still after.
# t,roll,pitch,yaw,dz,neck_pitch,head_pitch,head_yaw,head_roll,d_roll,d_pitch,d_yaw,d_dz,d_neck_pitch,d_head_pitch,d_head_yaw,d_head_roll

-- tremendous_v4.csv (4dd6989)
# Tremendous v4 (notes/dodge/tools/planted_v4.py, 2026-10-30): v3 with the double ding hit at 8.50 / 8.64 s, a head-bob groove (bar 5) and a bob-and-weave bar (bar 6). 50 Hz, t = phi * T, T = 18.25 s; channels = expressive_motions.REF_CHANNELS offsets from the stand (rad, dz in m); d_* = time derivatives (per s, analytic). Stand reached at 17.455 s (beat 32), still after.
# t,roll,pitch,yaw,dz,neck_pitch,head_pitch,head_yaw,head_roll,d_roll,d_pitch,d_yaw,d_dz,d_neck_pitch,d_head_pitch,d_head_yaw,d_head_roll

-- tremendous_steps.csv (bdb7989)
# Tremendous, STEPPING version (notes/dodge/steps/tools/steps_ref.py, 2026-10-30). 50 Hz, t = phi * T, T = 18.25 s; channels = expressive_motions.REF_CHANNELS offsets from the stand (rad, dz in m: root z - mean foot-site z - FK stand), d_* = time derivatives (per s); then the step channels: foot sites in the start frame (m, rad; z = clearance), contact schedule (1 = loaded / planted, 0 = swing), root xy (m).
# t,roll,pitch,yaw,dz,neck_pitch,head_pitch,head_yaw,head_roll,d_roll,d_pitch,d_yaw,d_dz,d_neck_pitch,d_head_pitch,d_head_yaw,d_head_roll,lf_x,lf_y,lf_yaw,lf_z,rf_x,rf_y,rf_yaw,rf_z,l_contact,r_contact,root_x,root_y

==== FILE docs/IMITATION_LEARNING.md (as of 67a8750^, deleted 2026-02-27)

# Imitation Learning for MicroDuck

This document explains how to use imitation learning with reference motions in the MicroDuck environment.

## Overview

The imitation learning system allows the robot to learn from reference motions generated by a motion planner (Placo walk engine). The system:

1. Loads polynomial-fitted reference motions from a pickle file
2. Tracks the gait phase during training
3. Rewards the policy for matching the reference motion
4. Provides phase observations to help the policy coordinate movements

The imitation reward is **only active during training**, not during inference/play mode. However, the phase observation is available in both modes.

## Setup

### 1. Generate Reference Motions

First, generate reference motion JSON files using the `Open_Duck_reference_motion_generator`:

```bash
cd ~/MISC/Open_Duck_reference_motion_generator
python scripts/auto_waddle.py --duck microduck --sweep --output_dir ./out
```

This will create JSON files with names like `0_-0.03_-0.02_-0.5.json` where the numbers represent `id_dx_dy_dtheta` (forward velocity, lateral velocity, angular velocity).

### 2. Generate Polynomial Coefficients

Convert the JSON files to polynomial coefficients using the existing script:

```bash
cd ~/MISC/Open_Duck_reference_motion_generator
python scripts/fit_poly.py --ref_motion ./out
```

This creates `polynomial_coefficients.pkl` containing 15th-degree polynomial coefficients fitted to each reference motion. Copy or symlink this file to your mjlab_microduck data directory:

```bash
cp polynomial_coefficients.pkl ~/MISC/mjlab_microduck/src/mjlab_microduck/data/reference_motions.pkl
# OR symlink it
ln -s ~/MISC/Open_Duck_reference_motion_generator/polynomial_coefficients.pkl \
      ~/MISC/mjlab_microduck/src/mjlab_microduck/data/reference_motions.pkl
```

## Usage

### Training with Imitation Learning

Once you have the reference motion file in place, simply use the imitation learning task:

```bash
uv run train Mjlab-Velocity-Flat-MicroDuck-Imitation --env.scene.num-envs 2048
```

This will train with the imitation reward enabled. The task automatically loads the reference motion file from:
- Default location: `~/MISC/mjlab_microduck/src/mjlab_microduck/data/reference_motions.pkl`
- Or set via environment variable: `export MICRODUCK_REFERENCE_MOTION_PATH=/path/to/your/file.pkl`

### Inference/Play Mode

Play mode works the same way - the imitation reward is disabled but the phase observation remains:

```bash
uv run play Mjlab-Velocity-Flat-MicroDuck-Imitation --wandb-run-path <...>
```

### Alternative: Environment Variable

You can also set a custom path:

```bash
export MICRODUCK_REFERENCE_MOTION_PATH=~/MISC/Open_Duck_reference_motion_generator/polynomial_coefficients.pkl
uv run train Mjlab-Velocity-Flat-MicroDuck-Imitation --env.scene.num-envs 2048
```

## Architecture

### Reference Motion Format

Each reference motion is keyed by velocity: `"dx_dy_dtheta"` (e.g., `"0.01_0.0_-0.4"`).

The motion contains:
- **joints_pos** (14 DOF): Joint positions (all joints including legs and head)
  - Left leg (5): hip_yaw, hip_roll, hip_pitch, knee, ankle
  - Head (4): neck_pitch, head_pitch, head_yaw, head_roll
  - Right leg (5): hip_yaw, hip_roll, hip_pitch, knee, ankle
- **joints_vel** (14 DOF): Joint velocities
- **foot_contacts** (2): Binary contact states for left/right feet
- **base_linear_vel** (3): Base linear velocity in world frame
- **base_angular_vel** (3): Base angular velocity in world frame

### Imitation Reward Components

The imitation reward is a weighted sum of:

- **Joint position tracking** (weight=15.0): Negative squared error
- **Joint velocity tracking** (weight=0.001): Negative squared error
- **Linear velocity XY** (weight=1.0): Exponential reward
- **Linear velocity Z** (weight=1.0): Exponential reward
- **Angular velocity XY** (weight=0.5): Exponential reward
- **Angular velocity Z** (weight=0.5): Exponential reward
- **Foot contacts** (weight=1.0): Binary matching reward

The reward is only non-zero when the commanded velocity magnitude exceeds a threshold (default: 0.01). This prevents the policy from moving when there is no command.

### Phase Observation

The policy (actor) receives a 2D phase observation: `[cos(phase * 2π), sin(phase * 2π)]`

This provides a continuous, periodic representation of where the robot is in the gait cycle, helping it learn coordinated movements.

### Privileged Observations (Critic Only)

During training, the critic receives additional privileged information that is not available to the actor or at deployment:

- **Full reference motion state** (36D):
  - Reference joint positions (14)
  - Reference joint velocities (14)
  - Reference foot contacts (2)
  - Reference base linear velocity (3)
  - Reference base angular velocity (3)

This asymmetric actor-critic setup allows the critic to better evaluate states by knowing the complete reference trajectory, while the actor must learn to track the motion using only the phase signal. This is a common technique in imitation learning that improves learning efficiency.

### Observation Dimensions

**Actor (Policy) Observations**: 53D
- base_ang_vel (3)
- projected_gravity (3)
- joint_pos (14)
- joint_vel (14)
- actions (14)
- command (3)
- imitation_phase (2)

**Critic Observations**: 89D
- All actor observations (53D)
- Full reference motion (36D): joint_pos (14) + joint_vel (14) + foot_contacts (2) + base_linear_vel (3) + base_angular_vel (3)

During inference/play, only the 53D actor observations are used.

### Motion Matching

During execution:
1. **Per-environment motion selection**: Each environment independently selects the reference motion closest to its commanded velocity
2. **Phase tracking**: Each environment maintains its own phase, which updates each timestep based on the motion's period
3. **Phase reset**: When an environment resets (due to falling/timeout) or switches to a different reference motion, its phase resets to 0.0
4. **Polynomial evaluation**: The polynomial is evaluated at the current phase to get the reference state
5. **Reward computation**: The reward compares the robot's actual state to the reference state

This ensures that each of the 2048 parallel environments can track different reference motions simultaneously based on their individual commanded velocities.

## Files

- `src/mjlab_microduck/reference_motion.py`: Reference motion loader
- `src/mjlab_microduck/tasks/mdp.py`: Imitation reward and phase observation functions
- `src/mjlab_microduck/tasks/microduck_velocity_env_cfg.py`: Environment configuration
- `src/mjlab_microduck/data/`: Directory for storing reference motion files

**Note**: Use `~/MISC/Open_Duck_reference_motion_generator/scripts/fit_poly.py` to generate polynomial coefficients from reference motions.

## Tuning

You can adjust the reward weights in the environment configuration:

```python
cfg.rewards["imitation"].params["weight_joint_pos"] = 15.0
cfg.rewards["imitation"].params["weight_joint_vel"] = 1e-3
cfg.rewards["imitation"].params["weight_lin_vel_xy"] = 1.0
cfg.rewards["imitation"].params["weight_lin_vel_z"] = 1.0
cfg.rewards["imitation"].params["weight_ang_vel_xy"] = 0.5
cfg.rewards["imitation"].params["weight_ang_vel_z"] = 0.5
cfg.rewards["imitation"].params["weight_contact"] = 1.0
```

You can also adjust the overall imitation reward weight:

```python
cfg.rewards["imitation"].weight = 1.0  # Adjust this value
```

## Verifying Reference Motion Playback

To verify that reference motions are played back correctly, use the replay script:

```bash
# List available motions
python replay_reference_motion.py ./src/mjlab_microduck/data/reference_motions.pkl --list-motions

# Replay a motion with robot hanging in air (to see leg motion clearly)
python replay_reference_motion.py ./src/mjlab_microduck/data/reference_motions.pkl \
    --motion-key "0.01_0.0_-0.4" \
    --hang

# Replay on ground with gravity
python replay_reference_motion.py ./src/mjlab_microduck/data/reference_motions.pkl \
    --motion-key "0.01_0.0_-0.4"

# Replay at different speed
python replay_reference_motion.py ./src/mjlab_microduck/data/reference_motions.pkl \
    --motion-key "0.01_0.0_-0.4" \
    --hang \
    --speed 0.5
```

The script:
- Plays reference motion at 50 Hz (matching training frequency)
- Shows phase progression and foot contacts
- Allows verifying that polynomials are evaluated correctly
- `--hang` mode freezes the robot base in space (pure kinematic replay, no dynamics)
  - Base position stays fixed
  - Only leg joints move according to reference motion
  - Perfect for verifying leg motion patterns

**Interactive keyboard controls:**
- `↑` (Up Arrow) - Switch to maximum forward motion
- `↓` (Down Arrow) - Switch to maximum backward motion
- `←` (Left Arrow) - Switch to maximum left translation
- `→` (Right Arrow) - Switch to maximum right translation
- `A` - Switch to maximum rotate left (counterclockwise)
- `E` - Switch to maximum rotate right (clockwise)
- `S` - Switch to standing motion (zero velocity)
- `Space` - Pause/resume playback

The script automatically finds and categorizes motions by velocity, making it easy to interactively explore different reference motions. Phase resets to 0 when switching motions.

## Inference with Imitation

When running inference with a policy trained using imitation learning, you need to enable imitation mode to include the phase observation:

```bash
python infer_policy.py output.onnx \
    --imitation \
    --reference-motion ./src/mjlab_microduck/data/reference_motions.pkl \
    --lin-vel-x 0.1 \
    --ang-vel-z 0.0
```

The `--imitation` flag:
- Enables phase tracking (updates each timestep based on gait period)
- Adds the 2D phase observation `[cos(phase * 2π), sin(phase * 2π)]` to the policy input
- Changes observation size from 51D to 53D

The `--reference-motion` argument is optional - if not provided, a default gait period of 0.72s is used. Providing the reference motion file ensures the phase tracking uses the correct period from your training data.

**Debug mode:**
```bash
python infer_policy.py output.onnx --imitation --debug
```

This will print the phase value and phase observation at each timestep.

==== FILE related commit messages (imitation era)

commit 7b1fc37f2720a56192d391791daa08aedef0b1f1
Author: apirrone
Date: 2026-02-13

CHECKPOINT OMG no imitation works very well

 aze | 0
 1 file changed, 0 insertions(+), 0 deletions(-)

commit 90b240d42f4398fd1c77bc2bcb1da465552bcbfa
Author: apirrone
Date: 2026-02-26

CHECKPOINT nice walk and standing in the same policy !!!

 aze | 0
 1 file changed, 0 insertions(+), 0 deletions(-)

commit 28a1087d832d67dfe35050179deb2ac39cd92417
Author: apirrone
Date: 2026-04-01

cleanup and readme

 src/mjlab_microduck/reference_motion.py            | 254 --------
 src/mjlab_microduck/tasks/__init__.py              |   5 +-
 src/mjlab_microduck/tasks/imitation_command.py     | 440 -------------
 src/mjlab_microduck/tasks/imitation_mdp.py         | 686 ---------------------
 src/mjlab_microduck/tasks/mdp.py                   | 398 ------------
 .../tasks/microduck_imitation_env_cfg.py           | 585 ------------------
 .../tasks/microduck_skating_stroke_env_cfg.py      | 316 ----------
 16 files changed, 46 insertions(+), 3844 deletions(-)

==== FILE pollen-robotics/microduck robotd/src/emotion.rs (46c8f1f), module header

//! Emotions: a head, body and beak timeline with a sound, played as a skill.
//!
//! An emotion is two files named after it: `sad.json`, the keyframes, and `sad.wav`, the sound,
//! which starts with them. `robot.do sad` plays it, so it goes on a pad button like any skill
//! (`robotctl pad bind y sad`).
//!
//! **The set ships inside the release** (`robotd/emotions/`, packaged as `emotions/`, regenerated
//! by `scripts/vendor-emotions.py`), so every robot on a release has them with nothing to install.
//! `[emotions] dir` is read on top: a file there adds an emotion or replaces the shipped one of the
//! same name, which is copying two files and restarting `robotd` — no release.
//!
//! **It drives the policy's commands, nothing below them.** While it plays, the head command, the
//! body pose and the mouth come from the keyframes and the twist is zero, exactly as if one client
//! sent `robot.head`, `robot.pose`, `robot.mouth` and a zero `robot.move` every tick — the pad's
//! body + head mode, scripted. So it reaches the motors through the same policy and the same
//! safety as a stick does, and a fall ends it like anything else. The sticks do nothing until it is
//! over; the robot then goes back to whatever the clients last asked for.
//!
//! The keyframes are the format of `pollen-robotics/microduck_emotions`, read as they are:
//!
//! ```json
//! {"keyframes": [{"t": 0.0, "neck": 0.0, "head_pitch": 0.1, "head_yaw": 0.0, "head_roll": 0.0,
//!                 "body_pitch": 0.0, "body_z": 0.0, "mouth": 0.0, "skill": null}, ...]}
//! ```
//!
//! Head values are the head command (radians, `head_pitch` > 0 is beak down), the body pitch and
//! height are the body pose, the mouth is 0..1. A missing field is 0, other fields are ignored, and
//! the emotion ends at the last keyframe. `"skill": "sit"` sits the robot at that keyframe, if it is
//! standing; it stays seated afterwards, and the sit toggle stands it up.

Shipped emotions in robotd/emotions/ at 46c8f1f: angry curious defiant devastated excited impatient laugh mmh mock no sad yes yes_fast 
