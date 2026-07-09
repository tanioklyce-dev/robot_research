---
title: Quality of Life Technology Center (CMU + Pitt)
type: entity
subtype: research-center
created: 2026-07-09
updated: 2026-07-09
sources: 0
tags: [assistive-robotics, nsf-erc, cmu, pitt, upmc, permma, herb, wheelchair, virtual-coach, defunct]
---

**Quality of Life Technology (QoLT) Center** — an NSF Engineering Research Center (ERC) run jointly by **Carnegie Mellon University and the University of Pittsburgh** (in association with UPMC), 2006 – mid-2010s, dedicated to "intelligent systems that enable older adults and people with disabilities to live more independently." One of the first large-scale, clinically-partnered, systems-level research programs in what this wiki calls [assistive robotics](../concepts/robotics/assistive-robotics.md) / PAR. Now **graduated** (NSF's term for an ERC whose federal funding has concluded); the constituent labs continue independently.

> [!note] Researched from the web (2026-07-09), not from an ingested source
> Claims below cite external URLs directly. No raw source document is filed; if QoLT becomes load-bearing for a synthesis, ingest the [2014 ERC annual report](https://erc-history.erc-assoc.org/wp-content/uploads/2020/02/QoLT-2014-AnnRpt-vol1.pdf) as a proper source.

## History and funding

- Established **June 2006** with a **$15M initial 5-year NSF grant** to CMU + Pitt ([CMU CS news release, 2006](https://www.cs.cmu.edu/news/2006/carnegie-mellon-university-pittsburgh-receive-15-million-nsfto-establish-center-focused); [Pitt University Times](https://www.utimes.pitt.edu/archives/?p=5458)).
- NSF award EEC-0540865 totaled **$29.56M**, running **2006-06-01 → 2014-05-31**; PI **Takeo Kanade** (CMU Robotics Institute, U.A. & Helen Whitaker University Professor), co-PI **Rory Cooper** (Pitt, FISA/PVA Chair of Rehabilitation Science and Technology; director of the Human Engineering Research Laboratories, HERL) ([Grantome record](https://grantome.com/grant/NSF/EEC-0540865)).
- The **QoLT Foundry** — the center's commercialization arm, staffed with executives-in-residence (director Curt Stone) — was added in **2008**; by late 2011 it had vetted ~35 business opportunities from center research ([CMU Piper, 2011](https://www.cmu.edu/piper/news/archives/2011/september/qoltfoundry.html)).
- The center's site now states "**QoLT has graduated**," directing inquiries to individual faculty by research area ([cmu.edu/qolt](https://www.cmu.edu/qolt/)).

> [!note] End-date ambiguity
> The NSF award record ends **May 2014** (8 years), while ERCs of that era were typically structured for ~10 years of support and some center materials continued into 2015–16. The wiki treats "2006 – mid-2010s" as the safe formulation; the exact wind-down year is unverified.

## Research program

The founding proposal organized work into four thrusts: **monitoring & modeling**, **mobility & manipulation**, **human–system interfaces**, and **person–society integration**, with CMU contributing robotics/AI and Pitt contributing clinical rehabilitation science — the stated goal being "compassionate intelligent QoLT systems" co-designed with end users ([Grantome abstract](https://grantome.com/grant/NSF/EEC-0540865)). The center's later self-presentation listed six areas with anchor faculty ([cmu.edu/qolt](https://www.cmu.edu/qolt/)):

| Area | Faculty |
|------|---------|
| Assistive technologies | Bigham, Dey, Mankoff |
| Computer vision | Hebert |
| Robotics & manipulation | Atkeson, Cooper, Kanade |
| Technology for aging | Beach, Forlizzi, Matthews |
| Transportation | Steinfeld |
| Virtual coaches | De la Torre, Hodgins, Siewiorek, Smailagic |

## Flagship systems

- **PerMMA** (Personal Mobility and Manipulation Appliance, HERL/Pitt, from 2006) — the center's signature robot: a smart powered wheelchair with **two dexterous robotic arms** for bi-manual manipulation of activities of daily living (fridge opening, feeding, reaching a ceiling light fixture ~9 ft up). Its control model is notable for this wiki: the system could be driven **by the user, by a remote human assistant over the internet, or a blend of both** — an early, concrete instance of the shared-autonomy spectrum later formalized in [levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md) ([HERL PerMMA page](https://www.herl.pitt.edu/research/permma); [performance evaluation, Med Eng Phys 2013](https://pubmed.ncbi.nlm.nih.gov/23769146/); Gen-II mobile base: [PMC3758530](https://pmc.ncbi.nlm.nih.gov/articles/PMC3758530/)).
- **HERB** (Home Exploring Robot Butler, CMU Personal Robotics Lab) — the center's other showcase robot, a bimanual mobile manipulator for household tasks; QoLT-era materials present PerMMA and HERB as the center's two quality-of-life robots ([Cybertherapy & Rehabilitation, 2014](http://www.cybertherapyandrehabilitation.com/2014/06/quality-life-technology-robots-people-disabilities-older-adults/)).
- **Virtual coaches** — sensor-instrumented coaching systems (e.g. power-wheelchair pressure-relief coaching, social coaching apps) from the Siewiorek/Smailagic/Hodgins/De la Torre group ([cmu.edu/qolt](https://www.cmu.edu/qolt/)).
- **Foundry-stage concepts** — Virtual Valet (remote car parking), Personalized Social Coach, Embedded Assessment of Wellness (sensor-laden appliances for passive well-being monitoring) ([CMU Piper, 2011](https://www.cmu.edu/piper/news/archives/2011/september/qoltfoundry.html)).

## Why it matters for this wiki

1. **Institutional ancestor of today's PAR field.** QoLT ran the systems-level, clinician-partnered, user-in-the-loop playbook — decades of which now surface in the wiki via [HCR Lab](hcrlab.md)'s in-home deployments and [Hello Robot](hello-robot.md)'s [Stretch](stretch.md). Charlie Kemp's Georgia Tech Healthcare Robotics Lab (Stretch's intellectual origin) was a contemporary of, not part of, QoLT — the two programs bracket the 2006–2016 era of assistive mobile manipulation.
2. **PerMMA anticipated the autonomy-preference debate.** Its user/remote-assistant blended control (2008–2013) prefigures the HRI 2020 finding (via [HCR Lab](hcrlab.md)) that users with severe motor impairments don't uniformly want more autonomy — the theme of [levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md).
3. **A cautionary data point on institutional sustainability.** A ~$30M, 8-year, two-university center "graduated" without producing a durable commercial assistive-manipulation platform; the field's current de-facto platform ([Stretch](stretch.md), 2020) came from a 2-person startup instead. Relevant background for the [assistive robotics research landscape](../syntheses/assistive/assistive-robotics-research-landscape.md)'s deployment-timeline pessimism.

## People

- **[Takeo Kanade](https://www.ri.cmu.edu/ri-faculty/takeo-kanade/)** — director (CMU); computer-vision pioneer.
- **Rory Cooper** — co-director (Pitt); HERL founder; wheelchair-technology researcher and Paralympic athlete.
- Participating faculty later prominent elsewhere: Jeffrey Bigham (accessibility/HCI), Anind Dey (ubicomp), Jodi Forlizzi (design), Martial Hebert (later CMU SCS dean), Jessica Hodgins, Dan Siewiorek, Aaron Steinfeld.

## Mentioned in

- [Assistive robotics research landscape](../syntheses/assistive/assistive-robotics-research-landscape.md)
- [Assistive robotics (concept)](../concepts/robotics/assistive-robotics.md)

## Open questions / TBD

- Exact wind-down year and whether NSF support ended at the year-8 review or ran a full 10 years — the [ERC-history annual reports](https://erc-history.erc-assoc.org/wp-content/uploads/2020/02/QoLT-2014-AnnRpt-vol1.pdf) would settle it.
- Did any QoLT Foundry opportunity become a surviving company? None surfaced in this research pass.
- HERB and the CMU Personal Robotics Lab (Siddhartha Srinivasa, later UW) may deserve their own entity page if manipulation-research lineage becomes a wiki thread.
