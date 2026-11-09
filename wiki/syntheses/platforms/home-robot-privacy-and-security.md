---
title: Home robot privacy and security — who sees what, and what a compromise can do
type: synthesis
created: 2026-11-08
updated: 2026-11-08
tags: [home-robot, privacy, security, teleoperation, consumer, data-collection, tau-robotics, 1x-neo, weave-robotics, flourish-1, unitree-g1, unitree-go2, comparison]
---

# Home robot privacy and security — who sees what, and what a compromise can do

A comparison of what home robots and robot services expose, as of **2026-11-08**. A robot differs from a smart speaker in two ways: it moves its sensors through the home, and it can act physically. This page asks four separate questions, because vendors tend to answer only the easiest one.

> [!note] Bottom line
> **Privacy depends on the business model.** Products that rely on remote operators necessarily let staff see into the home. Training on what the robot records is often part of the deal, and Tau makes it mandatory.
>
> **Security evidence exists only where someone looked.** Unitree has the longest vulnerability list because its robots are affordable enough to study. No public security assessment was found for NEO, Isaac, Flourish, Memo or Tau. **A clean record here means unexamined, not safe.**
>
> **Before buying, ask how the vendor handles security reports.** That separates vendors better than counting bugs: Unitree now runs a paid programme, and Hypershell told researchers it does not accept reports.

## The four questions

1. **Who can see through it live?** Remote operators or support staff.
2. **What is kept, and what is it used for?** Especially training models on footage of your home.
3. **What leaves the home without you asking?** Background telemetry.
4. **What can an attacker do, and from how far away?** Bluetooth range, the same network, or the internet.

## What each product exposes

| Robot or service | Live human access | Recording and training | Published security evidence |
|---|---|---|---|
| **[Tau cleaning](../../sources/tau-robotics-service-site.md)** | **Always.** One operator per robot, on-site in San Francisco | Every visit recorded, including unblurred faces. Trains models, **no opt-out**, perpetual licence, deletion on request. No audio, per its policy | None found |
| **[Weave Isaac](../../entities/weave-robotics.md)** | When needed. Its [privacy policy](https://www.weaverobotics.com/privacy) says staff "may remotely access" camera content | The policy lists model training among uses, and tells owners to limit what the robot films | None found |
| **[1X NEO](../../sources/1x-neo-order-page.md)** | At scheduled times, for complex tasks | **Unknown.** The [privacy policy](https://www.1x.tech/privacy-policy) (October 2025) covers the website and does not describe robot data | None found |
| **[Flourish 1](../../sources/flourish-robots-website.md)** | CEO says [none in normal use](../../sources/cnet-flourish-1.md) | Live video goes to its servers and is "discarded." Teaching needs a recording, and approved recordings train models | None found |
| **[Sunday Memo](../../sources/sunday-memo-site.md)** | Says it does not learn through in-home teleoperation | **Unknown.** The [privacy policy](https://www.sunday.ai/privacy-policy) (September 2025) does not describe robot data | None found; not on sale |
| **[Unitree G1](../../entities/unitree-g1.md) and [Go2](../../entities/unitree-go2.md)** | Not sold with remote operators | No training programme found; see telemetry at right | **Extensive.** Root-level flaws, and [undeclared telemetry on the G1](../../sources/cai-humanoid-robots-attack-vectors-paper.md). See [patch status](#patch-status-unitree) |
| **[Stretch](../../entities/stretch.md)** | Only if you set it up | Depends on your deployment; open ROS 2 stack | None reviewed here |
| **[Hookii](../../entities/hookii-neomow.md), [Hypershell](../../entities/hypershell-x.md), [HOBOT](../../entities/hobot-s7-pro.md)** | Not applicable | Hookii sent GPS unencrypted and stores property maps | [38 reported flaws](../../sources/cai-hacking-consumer-robots-paper.md), status unknown |

Policies were read on 2026-11-08 and can change. A policy says what a company permits itself, not what it does.

## What the comparison shows

**Remote operation makes camera access part of the product.** Tau, Weave and NEO all use it to complete tasks that autonomy can't. It can't be configured away while the service depends on it. Tau is the clearest case: it [says](../../sources/tau-robotics-service-site.md) recording is "how the service works, and it is why the service is priced the way it is," and [MIT Technology Review](../../sources/mit-technology-review-tau-cleaning.md) links the low price to the value of the data. Households are partly paying with footage of their homes.

**"Opt out" can mean losing the feature.** Flourish [lets you decline recording](../../sources/cnet-flourish-1.md), but a task can't be taught without one. Ask what stops working if you say no.

**Visitors don't consent.** Flourish's terms tell owners to inform household members and visitors about the camera. Tau's policy covers "any people present." Neither mechanism reaches a guest who walks in unaware.

**Distance sets the risk.** The flaws reviewed here group into three reaches:

| Reach | Example | What it means at home |
|---|---|---|
| **Bluetooth range** | UniPwn, UniBLEed, [HOBOT and Hypershell](../../sources/cai-hacking-consumer-robots-paper.md) | Someone nearby, possibly outside the home, without joining your network |
| **Same network** | [Go2 and G1 network flaws](../../sources/unitree-vulnerability-record-2026.md), [Hookii's debug access](../../sources/cai-hacking-consumer-robots-paper.md) | Any compromised device on home Wi-Fi becomes a path to the robot |
| **Vendor cloud** | Hookii's fleet credentials, 267 robots | One failure reaches every customer at once |

**Physical consequences are mostly untested.** Researchers showed exposed motor commands on an exoskeleton and a possible way to disable suction on a window cleaner. Neither paper demonstrated an injury. Treat this as a real hazard with no measured rate.

**Security claims often run ahead of the measurements.** The [G1 paper](../../sources/cai-humanoid-robots-attack-vectors-paper.md) confirmed outbound health data, but says it could not confirm the audio and video channels it warns about. Hardcoded keys and missing authentication are well evidenced. Covert surveillance is an inference.

## Patch status: Unitree

Full detail, with links, is in the [vulnerability record](../../sources/unitree-vulnerability-record-2026.md). **No fix below has been independently retested, and no accessible Unitree advisory maps flaws to firmware versions.**

| Robot | Update to at least | Reported effect | Still open or unknown |
|---|---|---|---|
| **Go2 (non-EDU)** | 1.1.13 | Closes CVE-2026-27509 and 27510, per Unitree via researchers | A certificate-validation flaw is recorded through 1.1.15.1 and rated difficult to exploit |
| **Go2 EDU** | Current | CVE-2026-27510 addressed | CVE-2026-27509 "will likely not be addressed" on EDU, so **isolation is essential** |
| **G1 EDU** | 1.5.5.0 | Reportedly blocks both August 2026 root chains | Not independently verified. Telemetry and configuration key status unknown |
| **G1 (non-EDU)** | Current | UniPwn probably mitigated | The 2026 CVEs name EDU only, so status is not established |

Unitree's conduct has changed. It [stopped responding](https://www.ieee-ras.org/news/exploit-allows-for-takeover-of-fleets-of-unitree-robots/) to the UniPwn researchers in 2025, then launched a programme in November 2025 and [paid bounties](https://boschko.ca/g1-ble-rce/) in 2026. Older criticism of its disclosure practices, including in the [2026 consumer-robot paper](../../sources/cai-hacking-consumer-robots-paper.md), doesn't describe its most recent behaviour.

## What to do

**Before paying for a robot or service:**

- Does a person ever see through its cameras? When, who, from where?
- Is footage used for training? What stops working if I decline?
- How long is it kept, and can I have it deleted?
- What works if the internet or the company goes away?
- Does the vendor have a security contact and publish fixes by version?

**If a robot is in your home:**

- Update the firmware and check the version yourself.
- Put it on an isolated network, away from computers and cameras. Assume local traffic can be read.
- Turn off Bluetooth where the robot allows it.
- Tell visitors it has cameras, and keep it out of private rooms when you can.

**If you run in-home research:** the same steps apply, and your consent process should cover bystanders and any vendor telemetry. [HIW-500](../../entities/hiw-500.md) collected G1 data in 12 homes, which shows how routinely such robots already go into private spaces.

## Limits of this page

- Vendor privacy policies, press and researcher write-ups. No robot was tested for this page.
- Robot vacuums, the one mature category, are not assessed. They are the most widely deployed camera-carrying home robots, and deserve their own review.
- The legal questions, such as GDPR compliance claims, are unresolved here.

## When this page should change

- A public security assessment of NEO, Isaac, Flourish, Memo or Tau.
- A Unitree advisory mapping flaws to firmware, or an independent retest of 1.5.5.0.
- 1X or Sunday publishing robot-specific privacy terms.

## Sources used in this synthesis

- [Unitree vulnerability record](../../sources/unitree-vulnerability-record-2026.md), [G1 attack vectors](../../sources/cai-humanoid-robots-attack-vectors-paper.md), [Hacking Consumer Robots](../../sources/cai-hacking-consumer-robots-paper.md)
- [Tau service pages](../../sources/tau-robotics-service-site.md), [MIT Technology Review on Tau](../../sources/mit-technology-review-tau-cleaning.md), [CBS on Tau](../../sources/cbs-news-tau-robotics.md)
- [1X order page](../../sources/1x-neo-order-page.md), [Weave Isaac 1](../../sources/weave-isaac-1-product-page.md), [eWeek on Isaac 0](../../sources/eweek-weave-isaac-0.md), [Flourish site](../../sources/flourish-robots-website.md), [CNET on Flourish](../../sources/cnet-flourish-1.md), [Sunday Memo](../../sources/sunday-memo-site.md)

## Related

- [Household robots compared](household-robots-comparison.md) · [Robot security](../../concepts/robotics/robot-security.md)
- [The home AI platform](../agents/home-ai-platform-trust-and-authority.md) · [Levels of autonomy in assistive robotics](../assistive/levels-of-autonomy-in-assistive-robotics.md)
