---
title: Domestic Robots and the Dream of Automation — Understanding Human Interaction and Intervention (Schneiders et al. 2021)
type: source
url: https://doi.org/10.1145/3411764.3445629
venue: CHI '21, May 2021, Yokohama, Japan
local_path: raw/Domestic_Robots_and_the_Dream_of_Automation_Schneiders.pdf
sha256: 0df10d728e56ec904cb35135ea86f8c32b7e684603c0e15ba49e16756a4b6806
author: Eike Schneiders, Anne Marie Kanstrup, Jesper Kjeldskov, Mikael B. Skov
published: 2021-05
ingested: 2026-05-10
tags: [hri, domestic-robots, automation, vacuum-robot, lawnmower-robot, qualitative-study, aalborg]
---

## Summary

A qualitative CHI 2021 study of **24 Danish households** that own consumer domestic robots — robotic vacuum cleaners, hybrid robots (vacuum + mop), and robotic lawnmowers. The authors combine three methods (online interviews with 12 households, in-home **contextual technology tours** of 9 households, and **robot deployments** of 10 days into 3 novel-user households). Through thematic analysis the paper identifies three themes: (1) work routines and automation, (2) robot automation and the physical environment, (3) interaction and breakdown intervention. The headline contribution is an **empirical understanding of how domestic robot automation actually unfolds in real homes** — including its surprising failure modes, the new tasks it creates, and how household members divide labor around it.

> [!note] This is the earliest deployment-reality source in this wiki. Schneiders 2021 sits ~5 years before the Stretch / RUM / OK-Robot wave and tracks what "automation in the home" looks like for the *only* domestic robot category that has reached real consumer adoption: vacuums and lawnmowers.

## Key claims

### Motivation and adoption
- All 24 participants (excluding the 3 deployment households who didn't choose the robot) cited a single motivation for buying: **automating an undesirable and time-consuming task.** Examples: "you don't have to use time on it [the cleaning] manually, this really saves time" (P10).
- Result quality (cleaning, lawn) was reported as **improved** vs. manual labor, primarily because the robot runs more frequently than humans would. Not the primary purchase driver but a consistent secondary benefit.

### Task fragmentation (key finding)
- Before robot adoption, vacuuming or lawn mowing was perceived as **one coherent task**: prepare, execute, clean up.
- After adoption, the task **fragments** into:
  1. Larger environmental changes (e.g., adjusting furniture).
  2. **Per-run preparation and maintenance** (picking up socks, emptying dust bin, cleaning blades, charging).
  3. The main cleaning/mowing — the *only* sub-task the robot performs.
- "...it [successful cleaning] also requires that no socks or anything is lying around on the floor." — P16.
- Households were generally aware some setup would be needed pre-purchase, but **surprised by the frequency** of these maintenance sub-tasks.

### Adapting the home to the robot
- The home is modified for the robot, not vice versa. Furniture rearranged, cables tucked, dock locations chosen carefully, "robot-friendly" routines adopted. Consistent with prior Forlizzi/DiSalvo work.
- Some households use **third-party apps and infrastructure** (IFTTT, FloleVac, custom Raspberry Pi, Mi Home, Alexa, Google Home routines) to compensate for limited functionality in the manufacturer apps.

### Strict task division between household members (contradicts prior work)
- Schneiders finds that in **17 of 20** multi-person households, **one person was always responsible for the robot**; other members had very limited interaction.
- This **contradicts Forlizzi (2007)**, which found that introducing a Roomba turned cleaning into a household social activity. Schneiders explicitly flags this as a contradiction with prior literature, and aligns with Geeng & Roesner (2019) on smart-home single-responsible-member patterns.
- In two households, the non-responsible partner would *text* the responsible partner to ask them to start the robot.

> [!warning] Contradiction with prior HRI work
> Forlizzi (2007) framed the Roomba's social effect as positive transformation of cleaning into a shared activity. Schneiders found the opposite in 17/20 multi-person households a decade later. Possible explanations: cultural (Danish vs. US), generational, novelty effect in 2007, or maturation of the technology making it more "appliance-like." The dissertation flagged this as worth investigating.

### Under-trust drives co-located operation
- Despite remote-control capabilities, several participants chose to **stay in the same room while the robot operates**, watching it work. This is not a novelty effect — it occurred even in households that had owned the robot for years.
- Co-location is driven by **under-trust in the robot's ability** to handle cluttered or unusual environments. Better object recognition is expected to reduce this, but at the cost of on-board cameras → privacy concerns (only one household had rejected a robot for camera-related privacy reasons).

### New enjoyable tasks
- Contrary to Bittner et al.'s worry that automation removes healthy/enjoyable tasks, Schneiders observed automation creating **new enjoyable tasks** — primarily the maintenance and care of the robot itself ("the feeling of satisfaction when seeing a well-maintained, working robot").

### Type of work matters more than amount
- Even when the robot added work (carrying it between floors, blade-cleaning, base-emptying), no participant viewed the tradeoff as net-negative.
- The authors conclude that **type** of work matters more than **amount** — replacing a disliked manual task with new maintenance/engineering tasks is preferred, even at higher total time cost.

### Demographic limitations (acknowledged)
- Sample: Danish households only — trust in robots varies cross-culturally (Wang et al. 2010).
- Gender imbalance: 22 male, 5 female participants — limits gender generalizability.
- Study spans vacuum, hybrid, and lawnmower robots only — not mobile manipulators or assistive robots.

## Entities mentioned

- [Eike Schneiders](../entities/eike-schneiders.md) — first author (Aalborg University)
- iRobot Roomba — not given its own entity; referenced as the dominant consumer vacuum robot (Forlizzi 2007)

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — adjacent: domestic robots are the consumer-market precursor to PARs, with the same fragmented-task pattern observed in [Nanavati 2025 feeding deployments](nanavati2025-feeding-out-of-lab.md)
- [Accessible robot communication](../concepts/robotics/accessible-robot-communication.md) — under-trust + co-located monitoring foreshadows the monitoring problem [Huh et al. 2026](huh2026-accessible-robot-comm.md) tackle for blind users

## Open questions

- How does task fragmentation evolve as mobile manipulators (Stretch, humanoids) replace vacuum/lawnmower robots? The "preparation tasks" list expands rapidly when the robot must manipulate diverse objects.
- Does the strict-division finding hold cross-culturally and a decade later? Worth re-running with US households and modern robots.
- The "type of work" insight (maintenance > original task) suggests assistive robot designers should think hard about what new tasks they create for users with limited mobility — for whom "engineering maintenance" may not be a viable substitute for the original task.
