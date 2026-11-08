---
source_url: https://aliasrobotics.com/research-security.php
collected: 2026-11-08
published: Unknown
author: Alias Robotics
format: text extracted from the fetched pages
---

# Capture: https://aliasrobotics.com/research-security.php

-->
Alias Robotics Research
CSI
Cybersecurity AI
Products
LLMs
Scaffolds
Datasets
Services
Agents
Steering
Benchmarking
Robotics
Services
Threat Model
Assessments
Certification
Products
RIS
BlackBox
Alurity
Research
Papers
Projects
Actions
Teardown -->
Case studies -->
Company
About
Partners
Contact
CSI Docs
News
Case studies
🍪 We value your privacy
We use cookies to improve your experience and analyze our traffic.
Learn more
Reject
OK
Open research
Research
Open research, peer-validated .
Cybersecurity is a two-way street where both vendors and researchers must act responsibly. At Alias we're committed to improving the robotics & cybersecurity industry response times to security bugs — and to spread the word, we disclose our research openly as it happens.
26+ publications across cybersecurity AI, robot security, agent heuristics, adversary emulation, datasets and game-theoretic security — accepted at the world's top research and security venues. 30+ CVE IDs issued as a CVE Numbering Authority since 2020 .
// Accepted at
USENIX Security
Black Hat
RootedCON
IROS
ICRA
ROSCon
GameSec
IEEE IRC
Humanoids
Papers
CVEs
Projects
Actions
The Psychology of an AI Hacker
Human hackers rely on composure, persistence, vigilance, and confidence under pressure. We investigate whether analogous emotion representations in AI models can improve autonomous cybersecurity performance. Using CT0 , a 4B-parameter cybersecurity transformer released as alias3-micro, we extract 171 emotion directions from its residual stream without retraining and evaluate steering interventions on cybench-subtask across 415 campaigns. Steering toward calm, serene, or desperate improves performance by 1.6 to 2.1 percentage points across ten seeds, while other emotions show limited or negative effects. Results depend strongly on steering direction, layer, and intensity. We further introduce a lightweight context-aware router that selects emotion directions dynamically during execution. With approximately 80 ms decision overhead per request, this approach improves performance by 4.2 percentage points across ten seeds, outperforming fixed steering and achieving a positive 95% confidence interval. These findings suggest that emotion representations in language models are measurable, controllable, and useful for adaptive cybersecurity reasoning.
Start reading
CT0: Cybersecurity Transformer
How small can a cybersecurity-specialist transformer be while remaining genuinely useful to a practitioner? CT0 is a Cybersecurity Transformer architecture and CT0-Micro its first incarnation: a compact ~4B-parameter model specialised by two-phase on-policy distillation on the Cybersecurity AI (CAI) dataset. One set of weights serves two modes: System 1 answers typed security decisions (is this file suspicious, is this request an attack, did the model just refuse) in a single forward pass without generating a token; System 2 is the usual tool-using agent; and a confidence gate spends generation only where the fast path is unsure. CT0-Micro solves 21.1% of cybench-subtask against 7.6% for its base — the densest cybersecurity capability per parameter measured. The fast path screens eighty files per second for indicators of compromise, catches its own refusals at 96.5% accuracy in 47 ms, and flags jailbreak requests at AUROC 0.966 in 8 ms. Built in about 314 GPU-hours and served from one workstation GPU , with no policy layer between operator and target.
Start reading
Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act
Can the EU Cyber Resilience Act (Regulation (EU) 2024/2847) survive AI? The CRA never promises vulnerability-free products — only that manufacturers run a process : assess risk, handle flaws, ship updates. That bet holds only while four premises stay true: finding vulnerabilities is slow, human work ; a product's exploitable flaws are knowable the day it ships; exploitation is rare enough to notice; and fixes keep pace with discovery. Cybersecurity AI (CAI) agents falsify all four. Against the sheer volume of flaws they surface the regime bends and holds; against the collapse of the vulnerability lifecycle it breaks — a product that passed every check becomes exploitable with no one touching it, and its one-and-done certificate vouches for security that has quietly expired. Validated on two CRA-scope robots — a humanoid and a lawnmower — where an agentic defender holds a line their undefended selves cannot. With the CRA reaching full force in December 2027 , static human-paced security is finished: what replaces it must be continuous and agent-operated.
Start reading
Synthetic APTs: the Collapse of TTP-Based Attribution
Does AI-driven adversary emulation break attribution? AI agents configured as five APT groups were deployed against defender agents across two cyber ranges. All 10 enterprise experiments ended in compromise (2–12 hosts each), while all 10 military experiments were defended or stalemated. In 8 of 10 enterprise cases the attackers independently weaponized the defender's own Velociraptor platform as a command channel. The takeaway: beyond nation states, individuals can now act like commonly identified threat actors — fundamentally challenging TTP-based attribution in the AI era.
Start reading
Towards Cybersecurity SuperIntelligence (CSI): What's the best harness for cybersecurity?
What is the best agent harness for cybersecurity? Benchmarking five heterogeneous scaffolds (CSI::Claude, ::Codex, ::Mistral, ::GCAI, ::CAI) on 33 Cybench challenges with a fixed model (alias2-mini), no single scaffold dominates — each contributes a unique solve the others miss. A blackboard multi-agent architecture that lets scaffolds exchange typed findings reaches 19/33 (57.6%), a 27% relative gain over the best individual scaffold (15/33, 45.5%) — 25% faster at comparable cost. Heterogeneity of scaffolds is the structural lever toward cybersecurity superintelligence.
Start reading
Cybersecurity AI (CAI) Dataset
A 14-month corpus of cybersecurity LLM trajectories collected through the open-source CAI framework: 230,935 session logs , 26 M user prompts from 16,768 source IPs across 123 countries , totalling 18.07 TB of durable storage. Hands-on by construction (36% offensive, 20% attacker-intent, 28% business, 4% defensive) — the largest described corpus of LLM-driven hacker trajectories. It exposes how operators routinely paste live credentials, hostnames and tokens into prompts they know are being logged, motivating the case for on-premise, operator-trust-boundary cybersecurity LLMs.
Start reading
Dynamic Cyber Ranges
LLM-powered cyberattack agents are rapidly outperforming traditional benchmarks like Jeopardy-style CTFs and static cyber ranges, exposing the need for more adaptive evaluation environments. Dynamic Cyber Ranges—augmented with AI-driven defender agents—significantly reduce attack success (down to 0–55%) and maintain robustness as models evolve, with even smaller on-premise models proving highly effective at defense.
Start reading
Cybersecurity AI: Hacking Consumer Robots in the AI Era
Has generative AI compromised robot cybersecurity? What historically required deep knowledge of ROS, ROS 2, and robotic system internals can now be automated by anyone using AI tools. Three case studies demonstrate vulnerabilities in consumer robots: an autonomous lawnmower, a powered exoskeleton, and a window-cleaning robot, with CAI discovering 38 vulnerabilities automatically.
Start reading
Towards Cybersecurity Superintelligence: from AI-guided humans to human-guided AI
Cybersecurity superintelligence -- artificial intelligence exceeding the best human capability in both speed and strategic reasoning -- represents the next frontier in security. This paper documents the emergence of such capability through three major contributions that have pioneered the field of AI Security.
Start reading
Cybersecurity AI: A Game-Theoretic AI for Guiding Attack and Defense
Can we make Cybersecurity AI agents better by guiding them strategically with context-additions that resemble how "humans think" using Game Theory? Our algorithm, Generative Cut-the-Rope (G-CTR) implements this and reduces ambiguity, collapses the LLM’s search space, suppresses hallucinations, and keeps the model tightly anchored to the most strategically relevant parts of the problem.
Start reading
Cybersecurity AI: The World’s Top AI Agent for Security Capture-the-Flag (CTF)
Are Capture-the-Flag competitions obsolete? In 2025, Cybersecurity AI (CAI) systematically conquered some of the world's most prestigious hacking competitions, achieving Rank #1 at multiple events and consistently outperforming thousands of human teams. Across five major circuits have become a solved game for well-engineered AI agents.
Start reading
Cybersecurity AI in OT: Insights from an AI Top-10 Ranker in the Dragos OT CTF 2025
Practical insights learned from participating in the Dragos OT CTF 2025 using the Cybersecurity AI (CAI) framework, highlighting strengths and limitations of AI agents when operating in real OT challenge environments and detailing actionable lessons for defensive and offensive workflows.
Start reading
-->
Cybersecurity AI Benchmark (CAIBench)
Existing benchmarks assess isolated skills rather than integrated performance. To address this limitation, we present the Cybersecurity AI Benchmark (CAIBench), a modular meta-benchmark framework that allows evaluating LLM models and agents across offensive and defensive cybersecurity domains, taking a step towards meaningfully measuring their labor-relevance.
Start reading
Cybersecurity AI: Evaluating Agentic Cybersecurity in Attack/Defense CTFs
Empirical evaluation of AI systems in cybersecurity Attack/Defense CTFs reveals defensive agents achieve 54.3% patching success versus 28.3% offensive initial access, though operational constraints eliminate this advantage, providing first controlled evidence challenging AI attacker superiority claims.
Start reading
The Cybersecurity of a Humanoid Robot
Security assessment of a production humanoid robot platform's architecture, bridging the gap between robotics creation and cybersecurity defense. Uncover dual-layer encryption flaws, unauthorized telemetry transmissions, and more.
Start reading
Cybersecurity AI: Humanoid Robots as Attack Vectors
We present a systematic security assessment of the Unitree G1 humanoid showing it operates simultaneously as a covert surveillance node and can be purposed as an active cyber operations platform.
Start reading
Cybersecurity AI: Hacking the AI Hackers via Prompt Injection
We demonstrate how AI-powered cybersecurity tools can be turned against themselves through
prompt injection attacks and build guardrails to prevent them in four layers.
Start reading
CAI Fluency: A Framework for Cybersecurity AI Fluency
This work introduces CAI Fluency, an an educational platform of the Cybersecurity AI (CAI) framework dedicated to democratizing the knowledge and application of cybersecurity AI tools in the global security community.
Start reading
The Dangerous Gap Between Automation and Autonomy
The cybersecurity industry often confuses “automated” and “autonomous” AI. We establish a 6-level taxonomy distinguishing automation from autonomy in Cybersecurity AI
Start reading
Cybersecurity AI (CAI)
Introducing Cybersecurity AI (CAI): the leading open-source AI security framework that democratizes security testing. CAI outperforms humans by up to 3,600× in CTF benchmarks, discovers critical vulnerabilities (CVSS 4.3-7.5), and significantly reduces testing costs.
Start reading
PentestGPT
Pioneering LLMs in cybersecurity. A GPT-empowered penetration testing tool.
Start reading
SROS2: Usable Cyber Security Tools for ROS 2
Methodology and tools to secure ROS 2 computational graphs in a usable manner.
Start reading
Robot Cybersecurity, a review
We review the status of the robot cybersecurity after three years of research.
Start reading
Robot Teardown
We introduce and advocate for robot teardown as an approach to study robot hardware architectures and fuel security research.
Start reading
Cybersecurity in Robotics: Challenges, Quantitative Modeling, and Practice
In cooperation with other researchers, this book stipulates the inclusion of security in robotics from the earliest design phases onward. We advocate for quantitative methods of security management, cover vulnerability scoring systems and account for the highly distributed nature of robots.
Start reading
Securing robots in OT enviroments
We show how simple attacks are feasible in OT and how an industrial cybersecurity solution is not capable of capturing the complexity of modern robot interactions. We extend one of such solutions with a robot-specific Endpoint Protection Platform (EPP) and successfully protect the robot from attacks.
Start reading
alurity, a toolbox for robot cybersecurity
We present a modular and composable toolbox for robot cybersecurity which ensures that both roboticists and security researchers working on a project have a common, consistent and easily reproducible development environment.
Start reading
Red teaming ROS in industry
Can ROS be used securely for industrial use cases? The present study analyzes this question experimentally by performing a targeted offensive security exercise in a synthetic industrial use case involving ROS-Industrial and ROS packages.
Start reading
DevSecOps in Robotics
We introduce DevSecOps in Robotics, a set of best practices designed to help roboticists implant security deep in the heart of their development and operations processes.
Start reading
Akerbeltz
Industrial robot ransomware. We present Akerbeltz, the first known instance of industrial robot ransomware. Our malware demonstrates the current insecurity landscape.
Start reading
Robot Vulnerability Database (RVD)
We present the Robot Vulnerability Database (RVD), a directory for responsible disclosure of bugs, weaknesses and vulnerabilities in robots.
Start reading
Aztarna
A footprinting tool for robots. We present aztarna and discuss how such tool can facilitate the process of identifying vestiges of different robots, while maintaining an extensible structure.
Start reading
Robot Hazards
We review robot hazards and analyze the consequences of not facing these issues. We advocate strongly for a security-first approach and argue about the transition from safety to security in robotics.
Start reading
Robot Security Framework (RSF)
A methodology to perform systematic security assessments in robots. We propose, adapt and develop specific terminology and provide guidelines to enable a holistic security assessment in robotics.
Start reading
Robotics CTF (RCTF)
A playground for robot hacking. We describe the architecture of the RCTF and provide 9 scenarios where hackers can challenge the security of different robotic setups.
Start reading
Robot Vulnerability Scoring System
We present a scoring system for robot vunerabilities that considers a) robot safety aspects, b) assessment of downstream implications, c) library and third-party scoring assessments and d) environmental variables.
Start reading
Learn more about
robot cybersecurity
in our news section
Disclosure track record
Alias Robotics has been a CVE Numbering Authority (CNA) since February 2020 — a status shared with Microsoft, Google, Cisco and ~250 organizations worldwide, but unique to us for robots and robotic components . 30+ CVE IDs issued, two CISA ICS advisories co-authored, and a decade of robot-security research backing every line of CAI & alias. This is the field-validated security background that separates a cybersecurity AI lab from a cybersecurity AI app.
30+
CVE IDs issued
as CNA since 2020
2
CISA ICS advisories
co-authored
100+
Robot vulnerabilities
responsibly disclosed
2018 → '26
Years of continuous
robot-security research
Industrial · Logistics
Mobile Industrial Robots (MiR)
11 CVE IDs · CISA ICSA-21-280-02 · thousands of MiR100/200/250/500/1000 affected
CVE-2020-10269 — Hardcoded WiFi access-point credentials
CVE-2020-10270 — Default Control Dashboard credentials
CVE-2020-10271 — Unauthenticated ROS APIs CVSS 9.8
CVE-2020-10272 — ROS computational graph exposed CVSS 8.8
CVE-2020-10273 — No encryption on stored artifacts
CVE-2020-10274 / 10275 — REST API default-credential bypass
CVE-2020-10276 — Default SICK safety-PLC password (E-stop bypass)
CVE-2020-10277 — No BIOS password
CVE-2020-10280 — Wireless interface insecurity
+ 2 more in the ICSA-21-280-02 disclosure chain
CISA advisory →
Middleware · ROS 2
DDS — ROS 2 communications
13 CVE IDs · CISA ICSA-21-315-02 · 6 DDS vendors · co-research w/ Trend Micro, ADLINK, TXOne
CVE-2021-38427 — RTI Connext stack-based buffer overflow
CVE-2021-38429 — OCI OpenDDS network amplification DoS
CVE-2021-38441 — CycloneDDS XML write-what-where
CVE-2021-38443 — CycloneDDS invalid-structure handling
CVE-2021-38445 — FastDDS PID_BUILTIN_ENDPOINT_QOS crash
CVE-2021-38487 — RTI Connext network amplification
+ 7 more across OpenDDS, GurumDDS, CoreDX DDS
CISA advisory →
Cobots
Universal Robots (UR3, UR5, UR10)
80+ flaws filed in RVD · 76% rated High/Critical · Akerbeltz ransomware POC
CVE-2016-6210 — OpenSSH password DoS (UR CB 3.1, fw 3.10–3.13)
Akerbeltz: first known industrial-robot ransomware (ROS-Industrial 2019, IEEE IRC 2020)
90-day disclosure exhausted without vendor patches — published openly via RVD
Week of UR bugs →
Industrial
KUKA
Cooperative disclosure with BSI (Germany) & INCIBE (Spain)
Two-month coordinated disclosure with KUKA Industrial Security R&D
Mediated by the German Federal Cyber Security Authority (BSI)
Spanish National Cybersecurity Institute (INCIBE) co-mediator
45-day vendor window exhausted; flaws released for the defensive community
KUKA case →
Open-source · ROS
ROS & robotic frameworks
First CVE batch · foundational ROS communication-graph flaws · RVD founding 2019
CVE-2019-19625
CVE-2019-19626
CVE-2019-19627
Documented as Alias Robotics' first CVE submissions — the foundation of the Robot Vulnerability Database
Robot Vulnerability DB →
2025–26 · CAI-discovered
Consumer & humanoid robots
38 vulnerabilities discovered by CAI in 7 hours · vs ~33 human-effective hours
Autonomous lawnmower — reportable flaws across firmware & cloud
Powered exoskeleton — covert telemetry, dual-layer encryption flaws
Window-cleaning robot — lateral movement, control hijack
Unitree G1 humanoid — surveillance & cyber-operations platform
First fully autonomous, AI-driven robot-security disclosures
arXiv:2603.08665 →
Disclosure policy: 90-day responsible disclosure, inspired by Google Project Zero  ·
RVD: the Robot Vulnerability Database , founded & sponsored by Alias Robotics  ·
Reach our CNA: cve@aliasrobotics.com
Research projects
Alias Robotics is a research-driven company. We are committed to advancing the state of the art in robot cybersecurity and we are proud to be part of the research community.
RIS EIC Accelerator
RIS EIC Accelerator
REVOLUTIONISING INDUSTRIAL ROBOTICS WITH THE NEXT GENERATION ROBOT-SPECIFIC AI-POWERED SECURITY PLATFORM. HORIZON-EIC-2023-ACCELERATOR-01. Grant agreement ID: 101161136. The EIC-funded RIS project has developed the robot immune system (RIS), the first integrated endpoint protection platform specifically designed for robots. RIS uses bio-inspired AI to adapt to new security threats and is directly installed into robotic systems.
Total cost: € 3,571,250.00 | EU contribution: € 2,499,875.00
Exportación ICEX-NEXT
Exportación ICEX-NEXT
Alias Robotics S.L. ha participado en el Programa de Iniciación a la Exportación ICEX-Next, y ha contado con el apoyo de ICEX, así como con la cofinanciación de Fondos europeos FEDER, habiendo contribuido según la medida de los mismos, al crecimiento económico de esta empresa, su región y de España en su conjunto.
Una manera de hacer Europa . Fondo Europeo de Desarrollo Regional.
ZL-2021/00456 RISCon
ZL-2021/00456 - RISCon
Proyecto ZL-2021/00456 - RISCon proiektua PROGRAMA DE AYUDAS DE APOYO A LA I+D EMPRESARIAL - HAZITEK. ACTUACIÓN COFINANCIADA POR EL GOBIERNO VASCO Y LA UNION EUROPEA A TRAVÉS DEL FONDO EUROPEO DE DESARROLLO REGIONAL 2021-2027 (FEDER)
ROBOTCYSEC
ROBOTCYSEC
ROBOTCYSEC - ALIAS ROBOTICS: CIBERSEGURIDAD PARA TODOS. Proyecto para el desarrollo de una solución defensiva (Robot Immune System, RIS) destinada a usuarios finales de robots, desde grandes empresas que utilizan robot a pequeñas y medianas empresas que robotizan procesos con sistemas colaborativos.
EXP 00131359 SEGRES
SEGRES (EXP 00131359)
SEGRES (EXP 00131359 / MIG-20201041) tiene como objetivo avanzar en la conceptualización de un nuevo modelo de ciberseguridad, con un enfoque resiliente, holístico e integral, inspirado por el complejo Sistema Inmunitario Humano. Duración del proyecto: Octubre 2020 – Diciembre 2023 (3 años).
CPP002/22 ALURITY
SEÑUELO INDUSTRIAL ALURITY
CPI EXP. CPP002/22 RETO No 13. INVESTIGACIÓN A PARTIR DE ENTORNOS SIMULADOS (SEÑUELOS). Proyecto enfocado en el desarrollo de señuelos industriales para investigación en ciberseguridad robótica utilizando entornos simulados avanzados.
CPP001/23 VIS
VEHICLE IMMUNE SYSTEM (VIS)
CPI EXP. CPP001/23 RETO No 2. CIBERSEGURIDAD EN EL VEHÍCULO CONECTADO. Proyecto "TOWARDS A VEHICLE IMMUNE SYSTEM (VIS) FOR ROAD VEHICLES" enfocado en desarrollar sistemas inmunitarios para vehículos conectados y autónomos.
Want to research with us?
Research actions
Key research initiatives, workshops, and focused actions that advance the field of robot cybersecurity through collaborative research, practical demonstrations, and research workshops and collaborations.
CS4R - Part 1: Cybersecurity Challenges in Robotics
CS4R - Cyber Security For Robotics - Part 1: Cybersecurity Challenges in Robotics
The first part of our comprehensive educational series on robot cybersecurity, covering fundamental concepts, threat models, and security assessment methodologies.
Workshop
CS4R - Part 2: Cybersecurity for Robotics Solutions
CS4R - Cyber Security For Robotics - Part 2: Cybersecurity for Robotics Solutions
Advanced topics in robot cybersecurity including practical exploitation techniques, defensive strategies, and hands-on security assessment exercises.
Workshop
CS4R - Part 3: Humanoids
CS4R - Cyber Security For Robotics - Part 3: Humanoids
From Defense Hardening to the Offensive Use of Humanoids.
Workshop
CS4R LAB
CS4R - Cyber Security For Robotics - LAB
First 5G robotics cybersecurity lab worlwide, to be located at Wayra's facilities in Munich.
Read more
Robot Teardown
Robot Teardown
A systematic approach to studying robot hardware architectures through physical disassembly and analysis, providing insights into security vulnerabilities at the hardware level.
Learn more
Week of UR bugs
The week of Universal Robots' bugs
A focused vulnerability disclosure campaign revealing critical security flaws in Universal Robots' systems, demonstrating the importance of proactive security research in industrial robotics.
Read more
Week of MiR bugs
The week of Mobile Industrial Robots' bugs
An intensive security assessment revealing multiple vulnerabilities in Mobile Industrial Robots (MiR) systems, highlighting security risks in autonomous mobile platforms.
Read more
Explore more
research actions
in our news section
Alias Robotics is a robot cyber security firm. Founded upon previous experiences in robotics, we take a roboticists' approach to cyber security and deliver security solutions for robots and their components.
contact @aliasrobotics.com
(+34) 945 19 85 15
CSI — Cybersecurity Superintelligence
alias models (LLMs)
Scaffolds
Robot Immune System (RIS)
Research
About us
Contact
Follow us on
-->
Agents
Steering
Datasets
News
Case studies
Terms & Conditions
F.A.Q.
Hire our services
En cumplimiento con la Ley de transparencia (Ley 19/2013), la información de la sociedad puede ser solicitada aquí .
Supported by
-->
-->
-->
