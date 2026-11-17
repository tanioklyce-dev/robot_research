---
title: "Shirley Ryan AbilityLab research labs and the argallab (lab pages, retrieved 2026-11-16)"
type: source
url: https://www.sralab.org/research
secondary_url: https://www.argallab.northwestern.edu/about/
local_path: raw/2026-11-16-shirley-ryan-abilitylab-research-labs.md
sha256: 2902a4365efed6315c13f337aab4c156e05f0af4fcab7075820ed757b73366b0
capture: bundle
author: Shirley Ryan AbilityLab; argallab (Northwestern University)
published: Unknown (retrieved 2026-11-16; individual pages dated 2016–2026)
ingested: 2026-11-16
format: text extracted from 17 institutional and lab web pages
tags: [shirley-ryan-abilitylab, argallab, brenna-argall, northwestern, assistive-robotics, rehabilitation-robotics, shared-control, shared-autonomy, powered-wheelchair, assistive-robot-arm, prosthetics, bionic-leg, brain-machine-interface, chicago]
---

# Shirley Ryan AbilityLab research labs and the argallab

## Summary

A capture of 17 pages from the [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md) (SRAlab), a rehabilitation hospital in Chicago with research labs inside it, and from the Northwestern site of its robotics autonomy group, the [argallab](../entities/argallab.md). The part that matters most to this wiki is the argallab, directed by Brenna Argall. It adds autonomy to **assistive machines people already use** (powered wheelchairs and wheelchair-mounted robot arms) and studies how control should be shared between the user and the machine. It runs its studies with people who have motor impairments, inside the hospital. The other robotics-related groups work on powered prostheses, therapy robots and brain-machine interfaces. These are the institution's own pages, so descriptions of quality and standing are self-reported.

## Key claims

**The institution** ([research page](https://www.sralab.org/research))
- SRAlab reports *"more than 350 studies under way"* and organizes its building around five "Ability Labs" (Arms + Hands, Legs + Walking, Strength + Endurance, Think + Speak, Pediatric), described as spaces where clinicians, scientists, engineers and patients work in the same room.
- It was the **Rehabilitation Institute of Chicago** until **March 2017**, when it moved and took its present name (argallab news page). Its address is 355 East Erie, Chicago.
- The research page links about 30 labs. Several researchers hold Northwestern University faculty appointments; one co-director of the Robotics Lab is at the University of Illinois at Chicago.

**The argallab (Assistive & Rehabilitation Robotics Lab)**
- **The problem it states:** *"As need increases, access decreases."* The more severe a motor impairment, the harder it is to operate the machines meant to help. The lab's answer is to turn the machine into a robot and *"offload some of the control burden from the user onto the machine."*
- **The dimensionality argument for arms** (project page, 2017): a robot arm needs 6-D control and a standard joystick gives 2-D. With a switch-based head array or sip-and-puff, operating an arm *"is too difficult to be practical."* Autonomy lets the arm partly control itself.
- **The wheelchair vision:** *"partial-autonomy in powered wheelchairs will be the standard"*, offered by a therapist the way seating options are today. The system is modular and built to attach to existing commercial chairs and interfaces, *"to mitigate costs not covered by insurance."* Perception work covers doorways, inclines, drop-offs and docking locations.
- **Users want to stay in the loop.** Argall (2023): *"most people don't want a 100%-driverless car solution for their wheelchairs... If robotic intelligence steps in at the wrong time, you're actually taking away agency from the person."*
- **Interface awareness** is the lab's newer line: people with impairments may produce unintended signals at the interface, so the autonomy models how the person actually uses the interface and interprets commands accordingly.
- **Where it sits:** the lab calls itself *"the only academic robotics autonomy lab in the country located inside of a rehabilitation hospital."* Argall says she knows of *"one other autonomous robotics researcher in the world who has a lab in the hospital."*
- **Her critique of the field:** claims that results *"could be deployed in assistive technologies"* are often *"not grounded in the clinical practicalities of the problem."* Many robotics groups *"use wheelchairs as just another robotic platform, but we always run studies with actual humans who have impairments in our chairs."*
- **Industry link:** a collaboration with **LUCI**, described as the first provider of a sensor-based safety system for wheelchairs, and an earlier NIH SBIR with Innovative Design Labs to move control-sharing components toward a product.
- **Output:** the publication list runs to 71 items through 2026. Recent ones include a minimal, deterministic shared-control method for safe wheelchair driving (RSS 2026), interface-level intent inference for teleoperation assistance (RSS 2025), a study of unintended interface operation with people with spinal cord injury (IJRR 2025), and learning to control robots through high-dimensional body-machine interfaces (ACM THRI 2024). The lab also published on accessibility barriers to robotics research itself (RSS 2023 workshop).
- **People** (2026): the lab's page lists a postdoctoral fellow, PhD and master's students in mechanical engineering and computer science, a research engineer, a project administrator and an occupational therapist. The lab leads **Project DRIVE**, a participant in the NSF Convergence Accelerator program.

**Brenna Argall**
- Professor of Computer Science, Mechanical Engineering, and Physical Medicine and Rehabilitation at Northwestern. PhD in Robotics from Carnegie Mellon (2009), postdoc in robot learning at EPFL (2009–2011). NSF CAREER award 2016 for *"Robot Learning from Motor-Impaired Teachers and Task Partners"*. Inducted into the AIMBE College of Fellows in March 2023, the 11th SRAlab-affiliated researcher to be so.

**Other robotics-related groups**
- **Regenstein Foundation Center for Bionic Medicine:** founded 2006 by Todd Kuiken, now led by Levi Hargrove. More than 63 staff; over 200 papers and $25 million in grants, by its own count (page dated 2021). It comprises four groups, including the Max Näder Center and the Neural Engineering for Prosthetics & Orthotics Lab.
- **Open-source bionic leg:** a powered knee-and-ankle prosthesis built with the University of Michigan from parts that are easy to buy, released so other groups can test control methods on the same hardware (Azocar et al., *Nature Biomedical Engineering*, 2020).
- **Neural Engineering for Prosthetics & Orthotics Lab:** control systems for powered prosthetic legs and hands, including pattern-recognition control from muscle signals.
- **Robotics Lab** (Sandro Mussa-Ivaldi and James Patton): the sensory-motor system studied through interaction with machines; therapy robots, error augmentation, and body-machine interfaces.
- **Max Näder Center:** outcomes research on prosthetics, orthotics, exoskeletons and wearable sensors.
- **Slutzky Neuroprosthetics Lab:** brain-machine interfaces for arm and hand movement and for speech, and muscle-signal interfaces for stroke rehabilitation.

## Analysis

- **A different bet from the rest of this wiki's assistive material.** Most assistive sources here put a general-purpose mobile manipulator in the home ([Stretch](../entities/stretch.md), the feeding studies). The argallab instead adds autonomy to devices that are already prescribed and paid for. That route sidesteps the certification and payment gates the [assistive forecast](../syntheses/assistive/assistive-robot-forecast-2026-2030.md) identifies, at the cost of a narrower set of tasks.
- **Interface awareness is the transferable idea.** It treats the input device as noisy in a user-specific way and models that before inferring intent. Any teleoperated or shared-control robot with a limited input channel faces the same problem ([levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md)).
- **The agency finding agrees with other sources here.** Argall's statement that users do not want full autonomy matches the [sense-of-agency study](yang2025-sense-of-agency.md) and Hello Robot's autonomy-as-a-feature position ([TechCrunch](techcrunch-hello-robot-homes-2026.md)).
- **Evidence weight.** This capture is institutional web pages, some last edited in 2016–2017. It establishes what the labs work on and claim. It does not give results. Three papers were ingested afterwards: [REACT wheelchair shared control](react-shared-control-wheelchair-paper.md), [interface-aware arm teleoperation](interface-aware-arm-teleoperation-sci-paper.md) and the [open-source bionic leg](open-source-bionic-leg-paper.md); five [project pages](shirley-ryan-abilitylab-project-pages.md) were captured too.

## Entities mentioned

- [Shirley Ryan AbilityLab](../entities/shirley-ryan-abilitylab.md)
- [argallab](../entities/argallab.md)

## Concepts touched

- [Assistive robotics](../concepts/robotics/assistive-robotics.md)

## Open questions

- What do the shared-control wheelchair studies with spinal-cord-injured participants actually measure and find? The RSS 2026 and IJRR 2025 papers are the ones to ingest.
- How far has the LUCI collaboration moved lab methods into a product?
- Does interface-aware assistance carry over to a mobile manipulator such as Stretch, or only to wheelchair-mounted arms?
- Institutional facts such as bed count, rankings and research budget are not on the captured pages.
