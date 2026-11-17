---
title: "Northwestern Center for Robotics and Biosystems: assistive autonomy and human-in-the-loop topic pages (retrieved 2026-11-16)"
type: source
url: https://robotics.northwestern.edu/research/topics/human-robot-co-adaptation/index.html
local_path: raw/2026-11-16-northwestern-robotics-assistive-topic-pages.md
sha256: 9d8b1eec789c2d1141531ee9a74c77ae3ebd332b73a60ad3dc18e915be91f82c
capture: bundle
author: Center for Robotics and Biosystems, Northwestern University
published: Unknown (retrieved 2026-11-16)
ingested: 2026-11-17
format: text extracted from 5 research-topic pages
tags: [northwestern, argallab, todd-murphey, human-robot-co-adaptation, body-machine-interface, robot-learning-from-demonstration, motor-impairment, shared-control, interface-aware, human-in-the-loop, maxwells-demon, vibrotactile-feedback, assistive-robotics]
---

# Northwestern robotics: assistive autonomy and human-in-the-loop topic pages

## Summary

Five research-topic pages from Northwestern's robotics center. Four describe [argallab](../entities/argallab.md) projects and one describes Todd Murphey's human-in-the-loop work. The pages are short statements of research questions with funding sources. Together they give the clearest account in this wiki of two ideas: **a robot that hands control to the person gradually as the person learns**, and **learning from teachers whose demonstrations are noisy and sparse because of a motor impairment**. No results are reported on these pages.

## Key claims

**Robot machine learning for human motor learning** (argallab with Ferdinando Mussa-Ivaldi; NIH R01-EB024058)
- The more capable an assistive machine, the more complex its control, and commercial interfaces for people with severe impairments cannot supply signals of that complexity.
- The Shirley Ryan AbilityLab's **body-machine interface** turns the body into a joystick, offering high-dimensional control signals and, as a side effect, motor rehabilitation.
- **The proposal:** autonomy handles part of the control at first and *"gradually transfer[s] more and more control to the human operator."* Machine learning decides *"when to unlock additional control dimensions for human operation."*

**Robot learning from motor-impaired teachers** (NSF RI-1552706, the lab director's CAREER award)
- Assistance needs change over time, and so does how a person operates the robot. A robot that does not adapt *"will struggle to achieve widespread adoption."*
- The teacher's signals are **noisy** (artifacts of the impairment), **sparse** (commands cost more effort) and **filtered through a control interface**.
- **The hypothesis:** these constraints can be an advantage for algorithms that exploit them, for example sparsity in the problem space, and need not be treated only as limits.

**Interface-aware autonomy, control sharing and machine learning** and **human-robot co-adaptation** (overview pages)
- The recurring theme is automation that can be customized to a user's physical abilities, preferences *"or even financial means"*, and the recurring question is how to share control.
- Listed sub-projects: blended human-robot control, automated switching of control mode, dynamic allocation of autonomy, trust-based control, an assistive robotic arm and a robotic wheelchair.

**Human-in-the-loop automation** (Todd Murphey, with Katie Fitzsimons and Ola Kalinowska)
- Interfaces for task-based assistance and training that handle uncertainty from the person and from unknown dynamics *"while allowing users to be as autonomous as possible."* The work moves away from controllers that minimize trajectory error using prior models, toward data-driven methods.
- **Controllers as filters, based on Maxwell's Demon:** an optimal controller is used as a reference, and the system filters noise or human input, letting through what helps the task.
- **Optimal tactile feedback:** vibrotactile cues encode an optimized combination of state information about the best action. Tested with healthy people in a balancing task and impaired people in a tracking task; the page says performance improved with combined visual and tactile input.
- Listed publications include *"Ergodicity reveals assistance and learning from physical human-robot interaction"* (Science Robotics, 2019) and *"Operation and Imitation under Safety-Aware Shared Control"* (WAFR 2018, with Argall).

## Analysis

- **Control that migrates toward the person.** Most robot-learning work aims to move control from human to robot. The motor-learning project runs the other way: autonomy is a scaffold that is withdrawn as the person's skill grows. That is a different target from the autonomy levels in [levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md), which treat the split as a setting, not a trajectory.
- **A harder version of the imitation-learning data problem.** [Imitation learning](../concepts/learning/imitation-learning.md) normally assumes clean expert demonstrations. Here the demonstrator cannot produce them. The idea of exploiting sparsity is stated as a hypothesis on the page, without results.
- **The Maxwell's Demon filter is the baseline in an ingested paper.** The [interface-aware arm teleoperation paper](interface-aware-arm-teleoperation-sci-paper.md) compares against a task-agnostic version of it, and this page is where that method comes from.
- **Evidence weight.** Topic pages only, several apparently unchanged for years. They state questions and list papers; none of the listed papers is ingested.

## Entities mentioned

- [argallab](../entities/argallab.md)
- [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md) — source of the body-machine interface

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md)
- [Imitation learning](../concepts/learning/imitation-learning.md)

## Open questions

- Did unlocking control dimensions by a learned schedule work? The 2023 and 2024 body-machine-interface papers on the argallab's list are the place to look.
- What did the Science Robotics 2019 ergodicity paper measure, and does it give a usable metric for "assistance versus learning"?
