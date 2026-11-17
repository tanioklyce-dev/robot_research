---
title: Assistive robot forecast, 2026-Q4 to 2030-Q4 — dated predictions with a scorecard
type: synthesis
created: 2026-11-16
updated: 2026-11-16
tags: [forecast, predictions, scorecard, assistive-robotics, disability, aging-in-place, adl, feeding, dressing, bathing, medication, reimbursement, medicare, certification, iso-13482, stretch, kinova-jaco, levels-of-autonomy, calibration]
---

# Assistive robot forecast, 2026-Q4 to 2030-Q4

Predictions made on **2026-11-16** about robots that help disabled people and older adults with daily tasks at home: how many homes have one, which tasks they can do, who pays, and whether they are certified and safe. It is the companion to the [home robot and JEPA forecast](../society/home-robot-forecast-2026-2028.md) and uses the same method: each prediction is a number with an interval, or a probability, with a fixed resolution rule, scored **after the end of each quarter** through 2030-Q4.

> [!warning] These are judgment forecasts, not sourced facts
> The evidence is cited from this wiki. The numbers are the forecaster's estimates from that evidence, and no source states them. **The predictions on this page are frozen as of 2026-11-16.** Scoring is appended below; the forecasts themselves are never edited. A revised forecast goes on a new dated page. The 2029–2030 columns are extrapolation and should be read as a statement of today's beliefs.

## The short version

- **Assistive use is a different market from consumer chores.** For someone who cannot do a task at all, a slow, mostly teleoperated robot is already valuable, so usefulness arrives years before autonomy does.
- **The gate is certification and payment, not capability.** No general-purpose mobile manipulator is certified for home use by individuals, and US Medicare does not cover assistive robot arms. Even odds that a certified one is on sale come around the end of 2028.
- **Task order:** fetching and feeding first (both already exist in narrow forms), then medication fetch and multi-step sequences, then dressing. **Bathing and transfers stay research topics through 2030** (43% and 29% for even a small published study).
- **The numbers stay small.** About 10 homes have a mobile manipulator in assistive use today. The forecast is about 80 by the end of 2028 and 550 by the end of 2030.

## How this differs from the consumer forecast

- **Remote or shared control is a feature here.** In the consumer forecast, a remote human is a stopgap. For this population, users have said they want control, not maximal autonomy ([levels of autonomy](levels-of-autonomy-in-assistive-robotics.md); [Yang 2025](../../sources/yang2025-sense-of-agency.md)). Hello Robot ships Stretch with limited autonomy on purpose ([TechCrunch](../../sources/techcrunch-hello-robot-homes-2026.md)).
- **The failure cost is higher.** A dropped item or a wrong pill is not a nuisance for someone who cannot recover from it ([research landscape](assistive-robotics-research-landscape.md); [underserved domains](underserved-par-domains.md)).
- **The buyer is usually not the user.** Insurers and health systems decide. Kinova sells its wheelchair arm mainly where insurance codes exist ([Kinova](../../entities/kinova.md)).

## What is being counted

**Set R counts homes**, cumulative and worldwide, where a disabled or older person has had a **general-purpose mobile manipulator** (a robot with an arm that moves around the home, such as [Stretch](../../entities/stretch.md)) for assistive use for **a month or more**.

- **Included:** research deployments, vendor pilots and commercial sales, if the robot stayed in the home for a month.
- **Excluded:** single-purpose devices such as the [Kinova Jaco](../../entities/kinova-jaco.md) wheelchair arm and Obi-type feeding devices, which are established products and tracked through set E; arm-less carts such as [Labrador](../../entities/labrador-systems.md); lab studies and visits shorter than a month; consumer robots bought for chores (those are in the other forecast).

**Resolution method.** As in the companion forecast: build a tally with a source for each row and a low and high bound. A hit is an overlap between the 80% interval and the tally's bounds; mark it unresolved if the tally's own bounds span more than a factor of five.

## Evidence base (as of 2026-11-16)

**Deployments.**
- Only one home in the wiki has a month or more of documented deployment data: Henry Evans's, with Stretch, over three summers ([long-term deployments](long-term-in-home-robot-deployments.md)). Keith Platt has lived with a Stretch since 2024, going from nearly two hours to a few minutes to serve himself a protein shake; navigation is autonomous and manipulation teleoperated ([TechCrunch](../../sources/techcrunch-hello-robot-homes-2026.md)).
- A feeding system on a Kinova arm let one user feed himself 10 meals over five days at home; bite acquisition was 80% or better for most foods, at one to two and a half minutes per bite ([Nanavati 2025](../../sources/nanavati2025-feeding-out-of-lab.md)).

**Capability.**
- Fetch: 58.5% open-vocabulary pick-and-drop in 10 homes ([OK-Robot](../../sources/ok-robot-project-page.md)); 90% across five skills in 25 homes with a retry loop ([RUM](../../sources/robot-utility-models-paper.md)).
- Household tasks in general: 12.4% best full success on BEHAVIOR-1K ([AI Index](../../sources/stanford-hai-ai-index-2026.md)).
- Contact tasks: an unsafeguarded feeding policy violated its safety constraint in 85% of timesteps; a safety filter fixed that without hurting success ([PACS](../../sources/pacs-paper.md); [assistive robotics](../../concepts/robotics/assistive-robotics.md)).
- Dressing, bathing and medication are the field's measured research gaps ([systematic review](../../sources/nanavati2024-physically-assistive-robots-review.md)).

**Products, certification and payment.**
- [Stretch 4](../../entities/stretch.md) costs $29,950 and is certified for lab and research use only; 200–300 units were expected in the first run ([datasheet](../../sources/hello-robot-stretch-4-datasheet.md), [TechCrunch](../../sources/techcrunch-hello-robot-homes-2026.md)).
- The Kinova Jaco is a medical device at about $35,000, sold where insurers reimburse it, chiefly Germany and the Netherlands ([Jaco](../../sources/kinova-jaco-assistive-arm.md)).
- No learned-policy robot holds an ISO 13482 certification ([safety standards](../../concepts/robotics/robot-safety-standards.md)).

**Web check on 2026-11-16** (external, not ingested):
- Hello Robot's own pages still say Stretch 4 lacks the certifications for home use by consumers and is not for sale to individuals; its assistive program is a small pilot run with engineers and an occupational therapist ([safety guide](https://docs.hello-robot.com/stretch-4-safety-guide/), [Stretch Assist](https://hello-robot.com/assist/)). IEEE Spectrum guesses a home version could take about a year ([article](https://spectrum.ieee.org/stretch-4-home-robot)).
- Medicare has no coverage policy for assistive robotic arms, per an undated [Disability Rights California guide](https://www.disabilityrightsca.org/publications/how-to-get-medi-cal-to-cover-an-assistive-robotic-arm). At least one private plan classes them as experimental ([Molina policy](https://www.molinahealthcare.com/molinaclinicalpolicy/-/media/Molina/PublicWebsite/PDF/Common/Molina-Clinical-Policy/Wheelchair-Mounted-Robotic-Arm-Devices_R.pdf)).
- The Obi feeding device retails for roughly $11,500–$13,000 in the US ([retailer listing](https://especialneeds.com/products/obi-robotic-self-feeder)).

**The wiki's own earlier timeline.** In May 2026 the [research landscape](assistive-robotics-research-landscape.md) estimated: open-vocabulary fetch at 90% in any home in 3–7 years, multi-step sequences in 5–10, safe physical-contact assistance in 10–15, and commercial deployment at scale in 10–20. This forecast is **more optimistic on fetch and multi-step sequences**, because Helix 2.5, GR00T 2 and π\*0.6 arrived since then, and **about as cautious on contact tasks and scale**.

## Prediction set R: homes with a mobile manipulator in assistive use (cumulative)

Baseline estimate today: **about 10** (80% interval 5–20).

| ID | Checkpoint | Point estimate | 80% interval |
|---|---|---|---|
| R1 | 2026-12-31 | 10 | 5 – 25 |
| R2 | 2027-03-31 | 12 | 6 – 30 |
| R3 | 2027-06-30 | 15 | 7 – 40 |
| R4 | 2027-09-30 | 20 | 8 – 60 |
| R5 | 2027-12-31 | 25 | 10 – 90 |
| R6 | 2028-03-31 | 35 | 12 – 130 |
| R7 | 2028-06-30 | 45 | 15 – 200 |
| R8 | 2028-09-30 | 60 | 18 – 300 |
| R9 | 2028-12-31 | 80 | 20 – 450 |
| R10 | 2029-03-31 | 100 | 25 – 650 |
| R11 | 2029-06-30 | 130 | 30 – 900 |
| R12 | 2029-09-30 | 170 | 35 – 1,300 |
| R13 | 2029-12-31 | 220 | 40 – 1,800 |
| R14 | 2030-03-31 | 280 | 45 – 2,500 |
| R15 | 2030-06-30 | 350 | 50 – 3,300 |
| R16 | 2030-09-30 | 440 | 55 – 4,300 |
| R17 | 2030-12-31 | 550 | 60 – 5,500 |

**Reasoning.** Growth to 2028 comes from research groups and Hello Robot's pilot. The steeper climb from 2029 assumes a certified product exists (E2) and that at least one payer or care provider funds placements (E6–E8). Without both, the count stays in the low hundreds.

## Prediction set E: events (cumulative probability, %)

Each cell is the probability that the event **has happened on or before** that quarter's last day. *Published* means a peer-reviewed paper or a preprint with stated participants and trial counts.

| ID | Event | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 28Q1 | 28Q2 | 28Q3 | 28Q4 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Products and regulation** | | | | | | | | | | |
| E1 | Hello Robot sells a Stretch to individuals for home use, stating it is certified or cleared for that use | 1 | 3 | 7 | 12 | 18 | 25 | 32 | 38 | 44 |
| E2 | Any vendor sells a general-purpose mobile manipulator to individuals for assistive home use, with a third-party safety certification or medical-device clearance | 1 | 4 | 8 | 14 | 21 | 28 | 36 | 42 | 48 |
| E3 | A consumer home-robot vendor (1X, Weave, Sunday, Figure or similar) announces a disability or eldercare offering with at least one named user or pilot site | 5 | 12 | 20 | 28 | 36 | 43 | 50 | 56 | 61 |
| E4 | A mobile manipulator marketed for assistive home use ships at $10,000 or less | 1 | 3 | 6 | 10 | 14 | 19 | 24 | 29 | 34 |
| **Who pays** | | | | | | | | | | |
| E5 | US Medicare establishes a coverage policy or billing code for a wheelchair-mounted or mobile assistive robotic arm | 0 | 1 | 2 | 3 | 5 | 7 | 9 | 11 | 13 |
| E6 | A US state Medicaid program or a major US private insurer publishes a positive coverage policy (not "experimental") for an assistive robotic arm or mobile manipulator | 1 | 3 | 5 | 8 | 11 | 14 | 17 | 20 | 23 |
| E7 | Any national health system or insurer reimburses a general-purpose mobile manipulator (not a wheelchair arm) for assistive home use | 0 | 1 | 2 | 3 | 5 | 7 | 9 | 12 | 15 |
| E8 | A home-care agency or health system announces a pilot of mobile manipulators or humanoids in 10 or more homes to supplement caregivers | 2 | 5 | 9 | 14 | 19 | 25 | 31 | 37 | 42 |
| **Task capability, published** | | | | | | | | | | |
| E9 | Autonomous open-vocabulary fetch at 90% or better across 10+ unseen real homes, 100+ trials | 3 | 8 | 14 | 21 | 28 | 35 | 42 | 48 | 54 |
| E10 | A multi-step daily-living sequence of 5+ steps (for example fetch, open, deliver) done autonomously at 80% or better in 5+ unseen homes, 50+ trials | 1 | 3 | 6 | 10 | 15 | 20 | 26 | 32 | 38 |
| E11 | Robot-assisted feeding: an in-home study with 10+ users with disabilities, each using the system for a week or more | 2 | 5 | 9 | 14 | 19 | 25 | 30 | 35 | 40 |
| E12 | Medication fetch: a robot brings a pre-organized medication container on schedule for 5+ users at home for a month or more | 1 | 3 | 6 | 10 | 14 | 19 | 24 | 29 | 34 |
| E13 | Robot-assisted dressing with 5+ participants who have motor impairments, any garment, 70% or better success | 2 | 5 | 8 | 12 | 16 | 21 | 26 | 31 | 35 |
| E14 | Robot-assisted bathing or showering, with water contact on the body, with 3+ participants who are disabled or older adults | 1 | 2 | 4 | 6 | 9 | 12 | 15 | 18 | 21 |
| E15 | A bed-to-chair transfer of a human participant by a general-purpose or learned-policy robot | 0 | 1 | 2 | 3 | 5 | 7 | 9 | 11 | 13 |
| **Deployment evidence** | | | | | | | | | | |
| E16 | A published study of a mobile manipulator in 10+ homes of disabled or older users, a month or more each | 0 | 1 | 3 | 6 | 10 | 14 | 19 | 24 | 29 |
| E17 | A published in-home deployment of 6+ continuous months in one home, with measured independence or caregiver-time outcomes | 3 | 7 | 12 | 17 | 23 | 29 | 35 | 40 | 45 |
| E18 | A randomized or controlled trial of an in-home assistive manipulator reporting independence or caregiver-hours outcomes | 0 | 1 | 2 | 4 | 6 | 9 | 12 | 15 | 18 |
| **Access and control** | | | | | | | | | | |
| E19 | An end-to-end system lets users with no hand function command a mobile manipulator by eye gaze, switch or similar to do household tasks in their own homes, 3+ users | 2 | 5 | 9 | 13 | 18 | 23 | 28 | 33 | 38 |
| E20 | A person with an implanted brain-computer interface controls a robot arm or mobile manipulator for a daily-living task at home, outside a lab | 3 | 7 | 12 | 17 | 22 | 27 | 32 | 37 | 41 |
| **Safety** | | | | | | | | | | |
| E21 | A learned-policy robot gains ISO 13482 certification or medical-device clearance for a task with intentional contact with a person | 0 | 0 | 1 | 2 | 3 | 5 | 7 | 9 | 11 |
| E22 | A publicly reported injury to a disabled or older user from an assistive robot arm or manipulator in home use | 1 | 2 | 4 | 6 | 8 | 10 | 13 | 15 | 18 |

| ID | Event (short) | 29Q1 | 29Q2 | 29Q3 | 29Q4 | 30Q1 | 30Q2 | 30Q3 | 30Q4 |
|---|---|---|---|---|---|---|---|---|---|
| E1 | Stretch sold to individuals | 49 | 54 | 58 | 62 | 65 | 68 | 71 | 73 |
| E2 | Any certified assistive mobile manipulator | 54 | 59 | 63 | 67 | 70 | 73 | 76 | 78 |
| E3 | Consumer vendor's eldercare offering | 66 | 70 | 73 | 76 | 79 | 81 | 83 | 85 |
| E4 | Assistive mobile manipulator at $10k or less | 39 | 43 | 47 | 51 | 55 | 58 | 61 | 64 |
| E5 | Medicare coverage | 16 | 18 | 21 | 23 | 26 | 28 | 31 | 33 |
| E6 | Medicaid or private insurer coverage | 26 | 29 | 32 | 35 | 38 | 40 | 43 | 45 |
| E7 | Mobile manipulator reimbursed anywhere | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 39 |
| E8 | Care-provider pilot in 10+ homes | 47 | 52 | 56 | 60 | 64 | 67 | 70 | 73 |
| E9 | Fetch at 90%+ in unseen homes | 59 | 64 | 68 | 72 | 75 | 78 | 80 | 82 |
| E10 | 5+ step sequence at 80%+ | 43 | 48 | 53 | 57 | 61 | 65 | 68 | 71 |
| E11 | Feeding study, 10+ users at home | 45 | 49 | 53 | 57 | 60 | 63 | 66 | 68 |
| E12 | Medication fetch, 5+ users | 38 | 42 | 46 | 50 | 53 | 56 | 59 | 61 |
| E13 | Dressing with 5+ impaired users | 39 | 43 | 47 | 51 | 54 | 57 | 60 | 62 |
| E14 | Bathing with 3+ users | 24 | 27 | 30 | 33 | 36 | 38 | 41 | 43 |
| E15 | Bed-to-chair transfer | 15 | 17 | 19 | 21 | 23 | 25 | 27 | 29 |
| E16 | 10+ homes, 1+ month each | 34 | 39 | 44 | 48 | 52 | 56 | 59 | 62 |
| E17 | 6+ month deployment with outcomes | 50 | 54 | 58 | 62 | 65 | 68 | 70 | 72 |
| E18 | Controlled trial | 21 | 24 | 27 | 30 | 33 | 36 | 39 | 41 |
| E19 | Gaze or switch control at home, 3+ users | 42 | 46 | 50 | 54 | 57 | 60 | 63 | 65 |
| E20 | Implanted BCI controls a robot at home | 45 | 49 | 52 | 55 | 58 | 61 | 63 | 65 |
| E21 | Certified learned-policy contact task | 13 | 16 | 18 | 21 | 23 | 26 | 28 | 31 |
| E22 | Reported injury | 20 | 23 | 25 | 28 | 30 | 32 | 35 | 37 |

**Notes on resolution.**
- **E1–E2:** a pilot in which the vendor's staff place and supervise the robot does not count. The robot must be orderable by an individual.
- **E4:** the vendor must market it for assistive use. A hobbyist kit that happens to be cheap does not count.
- **E9–E15:** results with able-bodied participants or mannequins do not count for E11, E13, E14 or E15. For E9 and E10 the homes must be ones the system was not trained in.
- **E13–E15:** teleoperated demonstrations count only if a participant who needs the assistance is the one being assisted.
- **E20:** a company report counts if it shows the user at home and names the task.
- **E22:** device malfunctions without injury do not count.

## Reasoning

**Why fetch and feeding lead.** Both already work in narrow forms, and neither needs sustained contact with the body. Fetch rides directly on the progress of general household policies, which is why E9 passes 50% in late 2028.

**Why dressing, bathing and transfers trail.** Each needs safe, sustained physical contact with someone who cannot pull away, plus hardware the research robots do not have: compliant arms for dressing, water-tolerant hardware for bathing, and strength with safety for transfers ([underserved domains](underserved-par-domains.md)). The wiki's 10–15 year estimate for contact assistance still looks right, so E14 and E15 stay under 45% and 30% even for small studies.

**Why certification is slow.** E21, a certified learned-policy robot doing a contact task, is 31% by the end of 2030. Certification asks for a risk assessment over defined hazards, and a learned policy's behaviour is hard to bound. The likeliest route is a deterministic safety layer under the policy, as PACS demonstrates in research.

**Why payment lags products.** E5–E7 are the lowest rows. A payer needs outcome evidence (E16–E18), and that evidence needs deployments, which need a product. Each step takes a year or more. Kinova's history is the base rate: launched in 2010, still classed as experimental by US insurers in 2026.

**What could make this too pessimistic.** Consumer home robots (E3) could reach disabled and older users by a side door: bought as chore robots, used as assistive ones, without any medical classification. If that happens, set R undercounts real assistive use, and the companion forecast's counts become the better guide.

## Scoring

**Schedule.** Score each checkpoint in the first two weeks after the quarter ends, together with the [companion forecast](../society/home-robot-forecast-2026-2028.md).

| Checkpoint | Quarter end | Score in | Status |
|---|---|---|---|
| 1 | 2026-12-31 | January 2027 | pending |
| 2 | 2027-03-31 | April 2027 | pending |
| 3 | 2027-06-30 | July 2027 | pending |
| 4 | 2027-09-30 | October 2027 | pending |
| 5 | 2027-12-31 | January 2028 | pending |
| 6 | 2028-03-31 | April 2028 | pending |
| 7 | 2028-06-30 | July 2028 | pending |
| 8 | 2028-09-30 | October 2028 | pending |
| 9 | 2028-12-31 | January 2029 | pending |
| 10 | 2029-03-31 | April 2029 | pending |
| 11 | 2029-06-30 | July 2029 | pending |
| 12 | 2029-09-30 | October 2029 | pending |
| 13 | 2029-12-31 | January 2030 | pending |
| 14 | 2030-03-31 | April 2030 | pending |
| 15 | 2030-06-30 | July 2030 | pending |
| 16 | 2030-09-30 | October 2030 | pending |
| 17 | 2030-12-31 | January 2031 | pending |

**Method.**
- **Set E:** record 1 if the event happened by the quarter's end, else 0. The score is the **Brier score**: the squared difference between the forecast probability and the outcome, averaged over the 22 events. Lower is better; always answering 50% scores 0.25.
- **Set R:** build the tally, then record hit, miss or unresolved, plus the ratio of the tally's midpoint to the point estimate.
- **Calibration:** from checkpoint 3 on, group scored cells by forecast probability and compare with the observed frequency.
- **Evidence and disputes:** every resolution cites a source. Ambiguous evidence is marked unresolved and excluded from the average; never resolve in the forecast's favour.

### Scorecard

*(Appended after each checkpoint. Nothing above this line changes.)*

| Checkpoint | Set R result | Set E Brier | Events resolved yes | Notes |
|---|---|---|---|---|
| 1 (2026-Q4) | | | | |
| 2 (2027-Q1) | | | | |
| 3 (2027-Q2) | | | | |
| 4 (2027-Q3) | | | | |
| 5 (2027-Q4) | | | | |
| 6 (2028-Q1) | | | | |
| 7 (2028-Q2) | | | | |
| 8 (2028-Q3) | | | | |
| 9 (2028-Q4) | | | | |
| 10 (2029-Q1) | | | | |
| 11 (2029-Q2) | | | | |
| 12 (2029-Q3) | | | | |
| 13 (2029-Q4) | | | | |
| 14 (2030-Q1) | | | | |
| 15 (2030-Q2) | | | | |
| 16 (2030-Q3) | | | | |
| 17 (2030-Q4) | | | | |

## Known weaknesses of this forecast

- **Tiny numbers.** Set R starts at about 10 homes, so one research grant or one cancelled pilot moves it a lot.
- **Publication lag.** Research events resolve when a paper appears, often a year after the work.
- **Outside the wiki's view.** The wiki has little on Japan, Korea and Europe's care-robot programmes, on exoskeletons as products, or on dedicated devices such as Obi, which is cited here from a web check only.
- **Definitions carry weight.** "Assistive use" and "general-purpose" are judgment calls at the margins, especially if consumer robots are used assistively (see above).
- **Correlated cells.** As in the companion forecast, an event that resolves early scores well in every later column.

## Related

- [Home robot forecast](../society/home-robot-forecast-2026-2028.md) — the consumer counterpart, scored on the same dates
- [Assistive robotics research landscape](assistive-robotics-research-landscape.md) — the seven blocking problems and the May 2026 timeline this forecast revises
- [Underserved assistive domains](underserved-par-domains.md) — dressing, bathing, medication
- [Levels of autonomy in assistive robotics](levels-of-autonomy-in-assistive-robotics.md), [Long-term in-home deployments](long-term-in-home-robot-deployments.md), [Stretch as assistive platform](stretch-as-assistive-platform.md)
- [Assistive robotics](../../concepts/robotics/assistive-robotics.md), [Aging in place](../../concepts/robotics/aging-in-place.md), [Robot safety standards](../../concepts/robotics/robot-safety-standards.md)
