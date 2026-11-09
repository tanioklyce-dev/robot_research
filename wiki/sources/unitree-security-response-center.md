---
title: Unitree Security Response Center — vulnerability handling and rating standard
type: source
url: https://security.unitree.com/
author: Unitree Robotics
published: Unknown (retrieved 2026-11-08)
ingested: 2026-11-08
tags: [unitree, robot-security, disclosure, bug-bounty, primary-source]
---

# Unitree Security Response Center — vulnerability handling and rating standard

## Summary

[Unitree's](../entities/unitree.md) own disclosure rules, read on 2026-11-08 from text copied out of a browser, because automated retrieval returned only an application shell. No copy is kept in `raw/`. **The rules page contains no table linking flaws to firmware versions, and it restricts what researchers can publish.** The Bulletin tab was not read. Its three announcement titles, seen in a screenshot and translated here, concern a contribution-reward feature, standards for AI-generated vulnerability reports, and the platform's launch.

## Key claims

- **Rewards for flaws on the robot.** Critical $1,000–5,000, High $200–1,000, Medium $100–200, Low $20–100. Critical means non-interactive remote control of any robot function, for example through Wi-Fi, Bluetooth, cellular or GPS.
- **Fix targets.** Review within 1–2 business days and handling within 3. Critical, High and Medium fixed within **90 business days**, Low within 180, subject to "environmental or hardware constraints."
- **Payment.** After a fix has been verified for one month, tentatively once a quarter.
- **Scope.** `*.unitree.com`, `*.unifolm.com`, core apps, and products "within Unitree's security maintenance lifecycle." That lifecycle is not defined on this page.
- **Excluded reports.** Include flaws found with "automated scanning tools," already public, submitted to other platforms at the same time, of "limited scope," or with "stringent exploitation conditions."
- **Publication needs permission.** Details "shall not be disclosed to any third party without prior permission." Publishing requires an application and a written consent letter. The page states no date after which a researcher may publish without consent.
- **Legal language.** Exaggerating impact "will be subject to pursuit," and "any access, download, or dissemination of Unitree source code or data may violate the law."

> [!note] How to read this against other disclosure practice
> [Alias Robotics](alias-robotics-research-page.md) states a 90-day disclosure policy inspired by Google Project Zero. Unitree's 90 days is a fix target in business days, about four calendar months, and publication stays subject to Unitree's approval. A paid programme therefore doesn't by itself guarantee that users learn about flaws. The rule against automated tools may also matter as [AI-driven testing](cai-hacking-consumer-robots-paper.md) spreads.

## Entities mentioned

- [Unitree](../entities/unitree.md)

## Concepts touched

- [Robot security](../concepts/robotics/robot-security.md)

## Open questions

- Does the Bulletin publish fixed versions?
- When was this standard written, and did it apply to the researchers who published in 2026?
- Which products are inside the "security maintenance lifecycle," and for how long?
