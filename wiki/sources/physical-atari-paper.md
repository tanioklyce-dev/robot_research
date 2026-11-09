---
title: "Physical Atari: A Robust and Accessible Platform for Real-time Reinforcement Learning on Robots"
type: source
url: https://arxiv.org/abs/2606.19357
local_path: raw/physical-atari-2606.19357v1.pdf
sha256: 20928b534a1b3afd25b6e8855eb9f81caaf765c4a1ab1fb5d020b45b990f9b41
author: "Khurram Javed, Joseph Modayil, Gloria Kennickell, Richard S. Sutton, John Carmack"
affiliations: "Keen Technologies, University of Alberta, Openmind Research Institute"
published: 2026-05-29
venue: "RLC 2026 (to appear, per arXiv comment)"
license: "Paper CC BY 4.0; code Apache-2.0"
format: paper (18 pp; 10 pp body + appendices)
arxiv: 2606.19357
project_page: https://keenagi.com/research/physical-atari/
code: https://github.com/Keen-Technologies/physical-atari-rlc
tags: [physical-atari, real-world-rl, real-time-rl, on-device-learning, atari, ale, keen-technologies, dynamixel, apriltags, distribution-shift, low-cost-hardware]
ingested: 2026-11-09
---

# Physical Atari: A Robust and Accessible Platform for Real-time Reinforcement Learning on Robots

## Summary

[Physical Atari](../entities/physical-atari.md) is a test rig for reinforcement learning that keeps running while the agent thinks. A camera watches a small screen playing Atari, and a three-servo robot moves a real joystick. The authors, from [Keen Technologies](../entities/keen-technologies.md), report that the agent learns six games in about 5.5 hours each, across 145 hours of runs with no human intervention.

The result most relevant to robot learning is the body swap. A policy moved to a second, identically built robot loses performance on all six games, and further learning on the new body recovers some or all of it.

The evidence supports a useful platform and a clear warning about unit-to-unit differences. **The rig is a narrow proxy for robotics, though.** The game is still emulated, the robot has 18 preprogrammed poses, and there is no contact with a changing physical scene.

## Key claims

### Hardware (Sec. 2, App. A, B, E)

- **Robotroller.** Three Dynamixel XC-330 servos actuate an unmodified Atari CX40+ joystick. All moving parts run on 608ZZ bearings, and printed parts take about 12 hours on a consumer printer. Purchased parts cost about $400.
- **Atari Devbox.** A Raspberry Pi 5 with a 5-inch display runs [ALE](../entities/ale.md) at 60 FPS and reads the joystick through GPIO. [AprilTags](../concepts/robotics/apriltags.md) mark the screen corners and carry the reward signal, so the agent gets everything through the camera.
- **Agent computer.** A Framework desktop with an AMD Ryzen AI Max+ 395, connected to an uncompressed-video camera (Razer Kiyo Pro).
- **Response time.** About 165 ms from screen to joystick, 123–165 ms across action pairs (Fig. 7). This excludes the time a neural network takes to choose an action.

### How the hardware was made reliable (Sec. 2.1)

Each fix followed a failure found in testing:

| Failure | Fix |
|---|---|
| Screws came loose | Thread-locking compound |
| Plastic gears wore out in XL-330 servos | Metal-geared XC-330 servos |
| Plastic servo horn broke in one build | Metal horn |
| The joystick itself wore out, traced to jerky motion from the high default P gain | PID retuned to P 1500, I 6000, D 1500 |
| The high I gain caused current spikes that needed a manual reboot | "High-current reflex": above 1200 mA, hold position and toggle torque for 1 ms |

### Learning setup (Sec. 4, App. D)

A convolutional value network takes a 128×128 smoothed camera frame, with a running average of recent actions merged in early. It uses 12-step returns, a replay buffer with some of each batch reserved for the newest experience, and a fixed ε of 2⁻⁶. Learning happens between sending an action and the next observation, following Travnik et al. (2018). One hyperparameter set covers all games.

### Results (Sec. 5)

- **Learning.** Pong, Seaquest, MsPacman, Assault, Asterix and Kangaroo each ran for 5.5 hours, with 4–5 repeats (Fig. 9). Runs improved on all six and were consistent.
- **Body swap.** Policies trained for 6 hours were evaluated on the training robot and on a second robot (Fig. 10). All six did worse on the second. Read off the bars, the second body keeps from about a fifth (Asterix) to about three-quarters (Seaquest) of the gain over an untrained policy. In Pong the paddle moved the right way and narrowly missed the ball.
- **Continued learning after the swap.** Tested on two games (Fig. 11). Read off the plot, Pong catches the same-body curve about 3–4 hours after the swap, with 2 seeds. Kangaroo improves and is still behind at hour 12, with 3 seeds.

### Limitations noted at ingest

- **"Weeks" isn't shown by the reported data.** The abstract says weeks of non-stop experiments without mechanical failures. The reported learning runs total about 145 hours, about six days, and the paper doesn't say how those hours split across units. No failure log or duty-cycle count is given.
- **"Under $1,000" isn't itemised.** The paper prices only the Robotroller parts, at about $400, and the build guides give no prices. It doesn't say whether the total includes the computer.
- **The body swap has an unmeasured cause.** The second setup changes both Robotroller and controller. The paper doesn't say whether the camera and Devbox also changed, and it doesn't measure how the two bodies differ. Response time isn't reported per unit, which would be the obvious check given the Pong timing failure.
- **Fig. 10 has no error bars or stated seed count.** The paper also doesn't say how many robot pairs were tested.
- **No baseline.** There is no comparison with the same agent in simulated ALE, with human scores or with another algorithm. The authors' inference that simulation would give a larger gap is untested and is posed as future work.
- **The hard parts of real-world RL are absent.** The emulator supplies the reward, and no run needed intervention, so reward design and scene resets don't arise. The agent chooses among preset poses and never commands the motors directly.
- **"First" claim.** The authors call it the first robot platform, to their knowledge, that is both affordable and durable. They compare durability with no other platform.

## Project page and code

The [project page](https://keenagi.com/research/physical-atari/) links printable parts and assembly guides for the [Robotroller](https://keenagi.com/research/physical-atari/robotroller.html) and [Devbox](https://keenagi.com/research/physical-atari/devbox.html). The [code](https://github.com/Keen-Technologies/physical-atari-rlc) is Apache-2.0 and has a sim-only mode. Users supply their own Atari ROMs. The README specifies Debian 13 for the Devbox, where the paper says Debian 12.

## Entities mentioned

- [Physical Atari](../entities/physical-atari.md), [Keen Technologies](../entities/keen-technologies.md)
- [Arcade Learning Environment](../entities/ale.md), [Dynamixel](../entities/dynamixel.md), [Raspberry Pi 5](../entities/raspberry-pi-5.md)

## Concepts touched

- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — long unattended learning on cheap hardware.
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md) — differences between two real bodies matter even with no simulator involved.
- [Continual learning](../concepts/learning/continual-learning.md) — continued learning recovers performance after a body change.
- [AprilTags](../concepts/robotics/apriltags.md) — used as a visual channel for reward.

## Open questions

- **What actually differs between the two bodies?** Measuring latency and servo response per unit would show whether timing explains the drop.
- **Does the size of the drop depend on training length?** Policies were swapped after 6 hours only. Longer training on several bodies might produce less unit-specific policies.
- **Would training across several units remove the need for adaptation?** The paper doesn't test the standard randomisation answer to this kind of shift.
- **How does a simulated-ALE policy score on the rig?** The authors propose this comparison, and it is the one that would turn the sim-gap inference into a measurement.
- **How far does the reflex idea transfer?** It protected servos that only reach preset poses. Arms in contact with objects are a different problem.
