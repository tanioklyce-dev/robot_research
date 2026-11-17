---
title: "A Minimal, Deterministic Approach to Shared Control for Safe Powered Wheelchair Driving (Loke et al., RSS 2026)"
type: source
url: https://www.argallab.northwestern.edu/publications/
fetch_url: https://www.argallab.northwestern.edu/files/2026/08/26rss_loke.pdf
local_path: raw/26rss_loke.pdf
sha256: b0cc7cbc51993d24ebb752c725684e85901fad43fd87f7fd252a9d0785360e29
author: "Larisa Y.C. Loke, Joel X. Goh, Kyle S. P. Puckett, Michelle H. Zhang, Nicole L. Zaino, Brenna D. Argall (Northwestern University; Shirley Ryan AbilityLab; LUCI Mobility)"
published: 2026
ingested: 2026-11-16
venue: "Robotics: Science and Systems (RSS) 2026"
format: paper (16 pp incl. appendix)
tags: [shared-control, shared-autonomy, powered-wheelchair, assistive-robotics, luci, react, argallab, case-study, longitudinal-evaluation, ros2, safety, user-study]
---

# A Minimal, Deterministic Approach to Shared Control for Safe Powered Wheelchair Driving

## Summary

**REACT** is a shared-control algorithm for powered wheelchairs from the [argallab](../entities/argallab.md), built on top of **LUCI**, a commercial sensor-and-compute add-on that already prevents collisions and drop-offs by throttling the driver's command. LUCI only slows the chair. REACT adds one thing: when LUCI's throttling becomes substantial, it picks a nearby safe heading and redirects, staying as close as possible to what the user commanded. It does not predict trajectories or infer goals, tasks or intent, so it makes no assumptions about the user or the control interface. The paper's second contribution is an evaluation protocol: five sessions per person, many driving tasks, three conditions (no assistance, LUCI, LUCI+REACT), run in a hospital with clinicians scoring. It is tested as **case studies with four wheelchair users**. Effects differ sharply by person, interface and task.

## Key claims

**Method** (§III)
- LUCI divides the 2-D control input space into eight zones and computes two safety thresholds per zone (linear and angular) at 10 Hz from mm-wave radar, ultrasonics and stereo depth. The threshold is the largest command it will pass to the chair.
- REACT acts only when the user's command exceeds the smoothed safe threshold and that threshold has fallen below a REACT threshold. It samples candidate headings near the user's, scores them by safety threshold and closeness to the user's heading, and issues the best. Otherwise the user's input passes through unchanged.
- The stated design reason: intent prediction and trajectory optimization *"may not generalize across users and interfaces"*, because a proportional joystick and a discrete sip/puff device produce qualitatively different input.
- Implemented in C++ in ROS 2 on a LUCI Dev Kit (a Sunrise Quickie Q500M chair). Users can switch REACT off; LUCI can be overridden with one button.

**Study** (§IV)
- Four participants: P1, 65, ALS, joystick; P2, 64, C4 complete spinal cord injury, sip/puff; P3, 29, cerebral palsy with vision and hearing impairments, joystick plus sight cane; P4, 54, C4 complete spinal cord injury, head array. P4 completed only one driving session and is excluded from the by-session tables.
- Sixteen driving tasks including weaving, ramps, doorways, an elevator, a van simulator, backing into a tight space and docking beside a bed. Clinicians score capacity with the Wheelchair Skills Test.

**Results** (§V, Tables III–V; three participants)

| | No assistance | LUCI | LUCI+REACT |
|---|---|---|---|
| Safe trials, P1 / P2 / P3 | 94 / 72 / 55% | 94 / 83 / 85% | 94 / 92 / 80% |
| Safety incidents, P1 / P2 / P3 | 3 / 16 / 33 | 3 / 9 / 4 | 2 / 3 / 7 |
| Capacity score, P1 / P2 / P3 | 91.3 / 84.0 / 49.3 | 92.4 / 88.9 / 84.0 | 90.2 / 96.0 / 78.7 |

- The skilled joystick driver (P1) sees almost no change. The sip/puff driver (P2) does best with REACT. The least skilled driver (P3) improves by about 30 points with either form of assistance and does slightly better with LUCI alone.
- **Rated best, wanted least.** P3 rated performance and confidence highest with LUCI+REACT but rated how often they would use it lowest. The authors attribute this to redirection being disorienting for someone with a vision impairment; P3 later preferred a less aggressive setting.
- For no user and task did both forms of assistance make control input choppier.
- **Sessions differ.** The same user on the same task under the same condition behaves differently across visits, which the authors take as a limit of single-session studies.
- In the final visit two participants chose to drive a van ramp, a task their caregivers normally do for them, and said they were confident doing so only with assistance.

**Stated limits** (§VI): four participants and no statistics; an unfamiliar chair and setting; uneven gaps between visits; uncontrolled distractions.

## Analysis

- **The design choice is the opposite of the learned-policy trend.** Most shared-autonomy work infers intent and optimizes a trajectory. REACT refuses to model the user at all, and the argument is that user models do not transfer across people and interfaces. With four users and four interfaces in the study, that is a claim about deployment, not about what is optimal for one person.
- **It builds on a product.** Perception and the safety envelope come from LUCI, and one author is from LUCI Mobility. That shortens the path to use and also means the results are tied to that system's thresholds.
- **The P3 result is the most useful finding for this wiki.** Objective scores and self-rated confidence rose while willingness to use fell. Any forecast or evaluation that scores assistive autonomy by task success alone would have counted that as a win ([levels of autonomy](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md)).
- **Evidence weight.** Case studies with n = 3 or 4 and no inferential statistics. The tables show direction for individuals, not an effect size.

## Entities mentioned

- [argallab](../entities/argallab.md), [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md)

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- Does the pattern hold in a larger cohort, and for discrete interfaces in particular?
- How does REACT compare with an intent-inferring method on the same users? The paper compares only against LUCI and no assistance.
- What happens over weeks of use at home, where the tasks and chair are the user's own?
