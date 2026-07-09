---
title: Quality of Life Technology Center (CMU + Pitt)
type: entity
subtype: research-center
created: 2026-07-09
updated: 2026-07-09
sources: 1
tags: [assistive-robotics, nsf-erc, cmu, pitt, upmc, permma, herb, wheelchair, virtual-coach, defunct]
---

**Quality of Life Technology (QoLT) Center** — an NSF Engineering Research Center (ERC) run jointly by **Carnegie Mellon University and the University of Pittsburgh** (in association with UPMC), **2006–2016**, dedicated to "intelligent systems that enable older adults and people with disabilities to live more independently." One of the first large-scale, clinically-partnered, systems-level research programs in what this wiki calls [assistive robotics](../concepts/robotics/assistive-robotics.md) / PAR. Now **graduated** (NSF's term for an ERC whose federal funding has concluded); the constituent labs continue independently.

> [!note] Sourcing
> Initially researched from the web (2026-07-09); the [2014 ERC annual report](../sources/qolt-2014-annual-report.md) (Year 8, 166 pp) is now ingested and is the primary source. Remaining external-URL citations are from the original research pass.

## History and funding

- Established **June 2006** with a **$15M initial 5-year NSF grant** to CMU + Pitt ([CMU CS news release, 2006](https://www.cs.cmu.edu/news/2006/carnegie-mellon-university-pittsburgh-receive-15-million-nsfto-establish-center-focused); [Pitt University Times](https://www.utimes.pitt.edu/archives/?p=5458)).
- NSF award EEC-0540865 totaled **$29.56M**, running **2006-06-01 → 2014-05-31**; PI **Takeo Kanade** (CMU Robotics Institute, U.A. & Helen Whitaker University Professor), co-PI **Rory Cooper** (Pitt, FISA/PVA Chair of Rehabilitation Science and Technology; director of the Human Engineering Research Laboratories, HERL) ([Grantome record](https://grantome.com/grant/NSF/EEC-0540865)).
- The **QoLT Foundry** — the center's commercialization arm, staffed with executives-in-residence (director Curt Stone) — was added in **2008**; by late 2011 it had vetted ~35 business opportunities from center research ([CMU Piper, 2011](https://www.cmu.edu/piper/news/archives/2011/september/qoltfoundry.html)).
- The center's site now states "**QoLT has graduated**," directing inquiries to individual faculty by research area ([cmu.edu/qolt](https://www.cmu.edu/qolt/)).
- **Leadership transition:** Takeo Kanade was Founding Director; by Year 8 **Dan Siewiorek** had been "unanimously selected by a Search Committee constituted to conduct a nationwide search for a permanent replacement," with Cooper remaining Co-Director and Pitt-sub-award PI ([2014 annual report](../sources/qolt-2014-annual-report.md) §5.1.2).
- **Mid-life reorganization:** the Mobility & Manipulation thrust "wound down in Year 8," its projects folding into the **QoLTbots** testbed (HERB, PerMMA-1/2, Strong Arm patient-transfer robot, MEBot curb-climbing base); Sidd Srinivasa was among its faculty ([2014 annual report](../sources/qolt-2014-annual-report.md)).
- The 2013 NSF Site Visit Team flagged the sustainability plan as "overly reliant on NIH funding post-graduation"; one named spin-off emerged from the Foundry pipeline: **Navity** (from the NAViSection project, via a $50k NSF I-Corps grant) ([2014 annual report](../sources/qolt-2014-annual-report.md)).

> [!note] End date — settled (2026-07-09)
> The [2014 annual report](../sources/qolt-2014-annual-report.md) resolves the earlier ambiguity: it is the **Year 8** report (Year 8 ended 2014-05-31) and contains milestone tables planned through **Year 10**, a "Business Plan for Post-Graduation Self-Sufficiency," and an REU renewal for 2014–2016 — the standard 10-year ERC lifecycle, giving **graduation at the end of Year 10, May 31, 2016**. The May-2014 date on the base NSF award record marks the end of the initial award segment, not the center. (Caveat: the report is forward-looking; actual Year-9/10 disbursements aren't independently confirmed, but the center's own "graduated" status page corroborates a normal graduation rather than early termination.)

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

## Design philosophy: symbiosis over autonomy

The center's own words ([2014 annual report](../sources/qolt-2014-annual-report.md), Project Summary): *"Whereas the goal of traditional robot autonomy is intelligence to function with minimal human involvement, the goal of QoLT **symbiosis** is for intelligent systems to function in concert with a person."* This is an explicit institutional rejection — in 2014 — of maximal autonomy as the design target, anticipating the empirical autonomy-preference findings (HRI 2020 → Yang 2025) collected in [levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md).

## Why it matters for this wiki

1. **Institutional ancestor of today's PAR field.** QoLT ran the systems-level, clinician-partnered, user-in-the-loop playbook — decades of which now surface in the wiki via [HCR Lab](hcrlab.md)'s in-home deployments and [Hello Robot](hello-robot.md)'s [Stretch](stretch.md). Charlie Kemp's Georgia Tech Healthcare Robotics Lab (Stretch's intellectual origin) was a contemporary of, not part of, QoLT — the two programs bracket the 2006–2016 era of assistive mobile manipulation.
2. **PerMMA anticipated the autonomy-preference debate.** Its user/remote-assistant blended control (2008–2013) prefigures the HRI 2020 finding (via [HCR Lab](hcrlab.md)) that users with severe motor impairments don't uniformly want more autonomy — the theme of [levels of autonomy in assistive robotics](../syntheses/assistive/levels-of-autonomy-in-assistive-robotics.md).
3. **A cautionary data point on institutional sustainability.** A ~$30M, 8-year, two-university center "graduated" without producing a durable commercial assistive-manipulation platform; the field's current de-facto platform ([Stretch](stretch.md), 2020) came from a 2-person startup instead. Relevant background for the [assistive robotics research landscape](../syntheses/assistive/assistive-robotics-research-landscape.md)'s deployment-timeline pessimism.

## People

- **[Takeo Kanade](https://www.ri.cmu.edu/ri-faculty/takeo-kanade/)** — director (CMU); computer-vision pioneer.
- **Rory Cooper** — co-director (Pitt); HERL founder; wheelchair-technology researcher and Paralympic athlete.
- Participating faculty later prominent elsewhere: Jeffrey Bigham (accessibility/HCI), Anind Dey (ubicomp), Jodi Forlizzi (design), Martial Hebert (later CMU SCS dean), Jessica Hodgins, Dan Siewiorek, Aaron Steinfeld.

## Mentioned in

- [QoLT ERC 2014 Annual Report (Year 8)](../sources/qolt-2014-annual-report.md)
- [Assistive robotics research landscape](../syntheses/assistive/assistive-robotics-research-landscape.md)
- [Assistive robotics (concept)](../concepts/robotics/assistive-robotics.md)

## Open questions / TBD

- ~~Exact wind-down year~~ — **resolved 2026-07-09** via the [2014 annual report](../sources/qolt-2014-annual-report.md): standard 10-year lifecycle, graduation May 31, 2016.
- Did any QoLT Foundry opportunity become a surviving company? The report names one spin-off (**Navity**, from NAViSection); whether it survived is unknown.
- HERB and the CMU Personal Robotics Lab (Siddhartha Srinivasa, later UW) may deserve their own entity page if manipulation-research lineage becomes a wiki thread.
