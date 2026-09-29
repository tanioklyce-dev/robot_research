<!-- captured 2026-09-29 via curl + BeautifulSoup text extraction from https://developer.nvidia.com/blog/inside-nvidia-halos-for-robotics-a-full-stack-functional-safety-system-for-physical-ai/ (datePublished 2026-06-22, dateModified 2026-08-06). Body text verified identical to Wayback captures 20260625091135 and 20260802084232 apart from link whitespace; the 08-06 modification changed only the auto-generated summary box. -->

# Inside NVIDIA Halos for Robotics: A Full-Stack Functional Safety System for Physical AI
- L
- T
- F
- R
- E
## AI-Generated Summary
- NVIDIA Halos for Robotics unifies AI compute and safety in a single platform extending the company's autonomous vehicle safety stack to industrial robots, humanoids, and autonomous mobile robots.
- The foundation combines NVIDIA IGX Thor hardware with built-in functional safety features and NVIDIA Holoscan Sensor Bridge to extend the safety chain to sensor edges.
- Halos OS provides a certified safety operating system with Linux and QNX configurations, including Halos Core for hardware error management and the Edge Safety Link protocol.
- The NVIDIA Halos Outside-In Safety Blueprint enables robots to use external infrastructure cameras and AI agents for real-time functional safety while maintaining operational throughput.
- An automated trailer loading reference use case demonstrates dynamic safety muting and reactivation based on worker presence detected by outside-in perception.
- The NVIDIA Halos AI Systems Inspection Lab offers an ANAB-accredited inspection pathway with 43 ecosystem members to accelerate third-party certification.
### Next Steps
- Register for NVIDIA Halos Core early access to begin developing safety applications on IGX Thor.
- Explore the NVIDIA Halos Outside-In Safety Blueprint repository to build outside-in safety agents with warehouse-deploy and halos-deploy skills.
Physical AI —robots working autonomously alongside people in factories, warehouses, hospitals, and homes—is arriving faster than most expected. Traditional safety which was built for structured environments can not work anymore as the spaces become more unstructured and robots move out of cages. AI-driven safety is the key.
Marking a major milestone in the arrival of physical AI, NVIDIA is today announcing the launch of NVIDIA Halos for Robotics which brings together powerful AI compute and safety in one single platform. NVIDIA Halos OS is a comprehensive, full-stack safety system built on years of NVIDIA investing in autonomous vehicle (AV) safety, now extended into the world of industrial robots, humanoids, and autonomous mobile robots (AMRs). NVIDIA IGX Thor and NVIDIA Halos OS are the foundational hardware and software platform of NVIDIA Halos.
Agility , maker of the humanoid robot Digit, is incorporating NVIDIA IGX Thor and Halos OS into its proprietary safe human detection system—and joining the NVIDIA Halos AI Systems Inspection Lab—to accelerate the development of safe humanoids for industrial environments. This adoption shows that the industry is ready to move beyond ad hoc safety implementations and toward a shared, standards-aligned foundation. Halos is that foundation.
This post introduces NVIDIA Halos for Robotics and explains how it’s structured and what it means for teams building the next generation of safe autonomous machines.
## How is NVIDIA extending a proven safety stack from AVs to robotics?
NVIDIA has a deep and long-standing investment in functional safety. The company has accumulated over 18,000 engineering years on vehicle safety, assessed more than 21 billion safety transistors, and produced over 7 million lines of safety-assessed code. More than 22,000 platform safety monitors have been developed, 330+ research papers on AV safety published, and 30+ certificates and assessment reports issued.
This body of work was built for AVs, one of the most demanding safety domains in engineering. The key insight behind Halos OS is that this proven foundation doesn’t need to be rebuilt for robotics. It can be extended.
The same safety development processes (software product lifecycle, hardware development process), the same development tools with proven confidence in use, and the same foundational functional safety standards (ISO 26262 → IEC 61508, ISO 13849) are shared across the AV and robotics stacks. Third-party assessments by TÜV SÜD and TÜV Rheinland confirm compliance across both domains.
This continuity is a structural advantage: building on Halos for AV, Halos for robotic safety inherits years of safety engineering work rather than starting from scratch.
NVIDIA is helping shape the future of robotics safety through its convenorship of IEC 61508, the leading functional safety standard for robotics, and ISO/IEC TS 22440 , an emerging standard for functional safety and AI, alongside its leadership of IEC TC 65 AhG 30 and active contribution to ISO 25785-1. These leadership positions underscore the influence and thought leadership of NVIDIA in robotics safety.
## What is NVIDIA Halos for Robotics?
NVIDIA Halos for Robotics is organized into the same full-stack comprehensive safety system that unifies safety elements from platform hardware and software across three layers similar to NVIDIA Halos for AVs.
At the foundation of the Halos stack is hardware platform safety: for robotics, that is provided by the NVIDIA IGX Thor platform and NVIDIA Holoscan Sensor Bridge (HSB) .
Building on that foundation, Halos OS is a safety software stack running on IGX Thor for robots and AMRs. Think of it as the same proven stack that keeps AVs safe on DRIVE AGX, now extended to robotics.
It includes Halos Core, the base safety operating system for developing and deploying safety applications and a collection of Blueprints including NVIDIA Halos Outside-In Safety Blueprint to extend robot perception with external worksite cameras and AI agents to dynamically control robot behavior.
Figure 1. NVIDIA Halos layered architecture
### NVIDIA IGX Thor provides platform safety
NVIDIA IGX Thor is an industrial-grade AI compute module that combines AI perception performance with built-in functional safety hardware—all in a single platform. Up to 2,070 FP4 TFLOPs of AI performance, 14x Neoverse ARM CPU cores, and 128 GB of memory at 273 GB/s bandwidth. This gives IGX the headroom to run demanding real-time robotics workloads alongside safety monitoring functions.
Autonomous vehicles
Robotics
Platform safety
NVIDIA DRIVE AGX, NVIDIA DRIVE Hyperion
NVIDIA IGX Thor and NVIDIA Holoscan Sensor Bridge
Halos OS
Halos Core and Halos applications and blueprints
Ecosystem safety
Halos AI Systems Inspection Lab – 43 members: 16 AV, 23 Robotics, 4 spanning both
Table 1. Platform safety and ecosystem across Halos AVs and robotics
Built-in hardware safety distinguishes IGX from general-purpose compute platforms. This hardware includes:
- IEC 61508 SIL 3 capable Safety Island (FSI) : A dedicated functional safety island with up to 12K DMIPs, its own I/O, power, and clocks—physically isolated from the main compute domain
- High diagnostic coverage : Over 22,000 safety mechanisms provide diagnostic coverage across the SoC
- IEC 61508 SC 3 systematics : All IPs supported for safety usage are developed with SC 3 capability per IEC 61508
- Diversity and redundancy : Multiple engines and interfaces can be paired for ASIL and SIL decomposition (GPU/CPU, GPU/PVA, CCPLEX CPU/FSI CPU)
- In-System Test (IST) : Logic and Memory BIST across the whole SoC for latent fault coverage
- Freedom from Interference (FFI) and Dependent Failure Initiator (DFI) support : Rich features including SMMU in CCPLEX and GPU, GFX execution watchdog, hardware Context Switch in GPU, NOC firewalls, and clock/voltage/thermal monitors
The IGX built-in hardware safety features are controlled by the Safety Extension Package (SEP) service of Halos Core. SEP is a collection and dispatch mechanism for hardware errors to the FSI and Safety MCU (SMCU), including FSI and SMCU reference firmware, an Error Propagation Layer (EPL), and the Edge Safety Link safety protocol.
An application note describing the use of IGX and Halos OS in the context of safety is available under NDA.
### NVIDIA Holoscan Sensor Bridge extends functional safety capabilities
HSB connects sensors and actuators to IGX over Ethernet, extending the safety chain all the way to the sensor edge. Key capabilities include:
- Low latency: ConnectX RDMA and RTX GPU Direct enable real-time sensor streaming
- Scalable: Easily scales to hundreds of sensors and hundreds of Gbit/s
- Multimodal: Domain-agnostic protocol supports any sensor or actuator type
- Safe and secure: MACsec for device authentication and encrypted data flow, plus end-to-end IEC 61508 SIL 2 safety protocol, watermarking, and camera testing support services included in Halos Core
Figure 2. NVIDIA Holoscan Sensor Bridge data flow from the camera through FPGA IP to host GPU processing
### Ecosystem support for platform safety
The platform safety is supported by a growing ecosystem of partners including IGX ODM partners including Advantech, Nexcobot , Inventec, and Connect Tech . Safety MCU and sensor partners include Infineon, NXP Semiconductors , and Texas Instruments. HSB chip partners include Texas Instruments, STMicroelectronics , NXP Semiconductors, and Lattice Semiconductor.
## The Halos OS for robotics software safety environment
NVIDIA Halos OS sits between the hardware and your application, giving robotics teams the certified building blocks they need — currently Halos Core (the safety OS) and Halos Applications (safety blueprints like Outside-In Safety). Robotics middleware and Halos Infra tools are available but not yet for safety applications.
Figure 3. NVIDIA Halos OS for robotics stack on NVIDIA IGX
### The safety operating system: Halos Core
At the foundation of NVIDIA Halos OS is Halos Core, which is the next generation of NVIDIA DriveOS and certified to automotive safety standards. The software layer runs on IGX Thor. Two configurations are currently available: Halos Core Linux and Halos Core Linux plus QNX (Figure 3).
Figure 4. Halos Core configurations include Linux-only (left) and Linux plus QNX with NV Hypervisor (right)
Halos Core Linux provides a complete safe software foundation: a Linux runtime for application and compute workloads, the SEP for hardware error collection and dispatch, the Edge Safety Link safety communication protocol, FSI RTOS, and Safety MCU RTOS firmware.
Halos Core Linux and QNX adds an NV Hypervisor layer that partitions IGX into isolated virtual machines: a Linux VM for AI and application workloads, and a QNX VM for safety-critical functions. QNX is a real-time operating system with a long pedigree in certified safety systems, and its inclusion enables stronger software partitioning for higher safety integrity use cases.
### Ecosystem support for Halos OS
Halos OS ecosystem partners at this layer include Blackberry on QNX , Acontis on EtherCAT/FSOE solution, FreeRTOS (AWS is the steward of FreeRTOS and will offer a Safety Certification Bundle as part of Halos OS), and others.
Both configurations are available now for early access . To learn more, see the NVIDIA IGX Safety Product Brief with detailed architecture documentation available for registered developers through the NVIDIA developer portal.
## Developing functional safety agents with NVIDIA Halos OS
As part of the NVIDIA Halos OS application layer, NVIDIA has reference blueprints for developers building functional safety agents.
### Outside-in safety
NVIDIA Halos Outside-In Safety Blueprint extends robot perception beyond onboard sensors. It uses external infrastructure cameras, AI perception, and safety logic to accelerate development of real-time, functional safety solutions that also maximize operational throughput.
Running on NVIDIA IGX and available as open source, it enables robots to safely operate alongside workers at higher efficiency while dynamically adapting to complex environments. It also provides documentation support for AI functional safety standards such as ISO/IEC TR 5469 and the upcoming ISO/IEC TS 22440.
Figure 5. Halos Outside-In Safety Blueprint spans industrial facility, AI safety pipeline, and digital twin validation
The blueprint provides several customizable components to implement outside-in safety agents starting with sensor input such as live stream cameras and outputting safety signals to autonomous vehicles or robots.
- Sensor Input Processing Pipeline (SIPP): NVIDIA Metropolis Blueprint for video search and summarization (VSS), the reference perception stack, is used to ingest all camera streams from facility infrastructure and convert them into actionable events and analytic data. VSS is an AI-based perception pipeline that detects and tracks objects of interest across cameras. It outputs the location, speed, and trajectory of each tracked object and maps this data to discrete events, such as an entry into or exit from a region of interest (ROI), a proximity event between two objects, or a forklift crossing a tripwire at a doorway.
- Safety AI Monitor (SAIM): Continuously monitors the perception pipeline for conditions that could compromise detection accuracy—including out-of-distribution inputs, camera blockage, connectivity drops, and image anomalies. . If the input becomes out-of-distribution (OOD)—for example, due to unexpected changes in environmental conditions such as facility lighting dimming—the accuracy and reliability of the AI model can no longer be assured. When this occurs, the SAIM detects and flags the condition, preventing downstream decision-making from relying on potentially degraded AI outputs. The SAIM generates an alert that propagates through the safety chain, causing the Safety Decision Maker to fall back to a safe operating state—reactivating the robot’s onboard safety functions—until conditions recover. This mechanism ensures safe system operation even when real-world conditions fall outside those represented in the training dataset.
- Safety Event Integrator (SEI): Fuses events from multiple camera perspectives and ensures they meet a high confidence threshold before forwarding them to the Safety Decision Maker. Events arriving with significant delay based on their timestamps are discarded as stale to ensure safety decision making is always based on the most recent events. Features like event fusion, staleness checks, and event processing logic can all be customized within the SEI.
- Safety Decision Maker (SDM): Runs a finite state machine on IGX’s dedicated Functional Safety Island—isolated from the main AI compute domain— to act on integrated events—sending safe stop signals, adjusting robot operating speed, or temporarily muting onboard safety constraints when the outside-in system confirms the area is clear. The SDM’s logic can be customized to implement new behaviors and output signals for different use cases.
- Integrate to existing robotics development workflow: Running on NVIDIA RTX Pro with NVIDIA Isaac Sim, this domain generates synthetic camera streams for testing and hardware-in-the-loop validation, with action signals feeding back into the real system.
## Automated trailer loading reference use case
The automated trailer loading (ATL) example is a safety concept inspected by TÜV Rheinland built using NVIDIA Halos Outside-In Safety Blueprint to tackle one of the most common pain points in warehouse automation: getting autonomous forklifts to load trailers efficiently without constant safety stops.
Current inside-out systems often can’t operate freely inside trailers due to space limitations and onboard sensor detection mistakes such as misunderstanding cargo and trailer walls as obstacles. This can limit the forklift’s movement to a crawl or stopping entirely.  Muting onboard safety can bring back operation efficiency inside the trailer, but doing so safely and intelligently becomes critical. That’s where outside-in safety comes in.
In the ATL example, the SIPP is implemented using the NVIDIA VSS Blueprint for warehouse operations which takes in multiple camera streams, detects and tracks objects, and maps them to events against a configured region of interest around the loading area and a tripwire at the entrance of the trailer. The SDM always knows whether people are present in the loading area and whether the forklift is inside or outside the trailer.
Figure 6. Dual-camera view of a warehouse loading area with object detection active, tracking a forklift and workers within a defined region of interest
When the forklift is inside the trailer and no workers are present in the loading area, the SDM temporarily mutes the forklift’s onboard safety system, enabling it to operate at full efficiency. The moment a worker steps into the loading area, the ROI entry event propagates through the SEI to the SDM, which fully reactivates the forklift’s safety system.
Figure 7. Dual-camera view of the same loading area with no workers or forklift present, showing the SDM-muted safety state
If the SAIM detects that camera conditions have degraded—a light goes out, steam obscures a camera—it sends an additional out-of-distribution event and the SDM responds accordingly.
Figure 8. Simulated warehouse showing a forklift triggering an out-of-distribution sensor event, with the system switching to standard mode as logged in the terminal output
The result is higher throughput and more reliable safety coverage than inside-out alone can provide. Safety and productivity are no longer in tension.
## Ecosystem safety: The NVIDIA Halos AI Systems Inspection Lab
Safety certification is not something any single company can do alone. The NVIDIA Halos AI Systems Inspection Lab is an ANAB-accredited ISO/IEC 17020 Inspection Body , the first worldwide program accredited for AI and functional safety in both autonomous vehicles and robotics,  providing a structured pathway from design to certificate.
This process works as follows: a Partner/ODM asks the Lab to inspect the correct integration of Halos safety, AI safety and cybersecurity requirements in their product. The NVIDIA pool of safety and regulatory experts assesses the system against preassessed Halos stack elements (IGX SoM, Halos Core, and Halos Applications) and issues an Inspection Certificate and Inspection Report. The partner then takes this NVIDIA Inspection Certificate to a third-party Certification Agency—TÜV Rheinland, TÜV SÜD, SGS, exida, CERTX, or UL Solutions—to obtain final system certification.
Because the Halos elements and their integration with the end product are preassessed, partners don’t need to reevaluate the platform from scratch. They can focus their certification effort on their own application logic, dramatically reducing time and cost to certification.
Agility is using the Lab to inspect how the Digit safety-related software, AI components, and cybersecurity protections meet rigorous standards including IEC 61508, ISO 13849, and ISO/IEC TR 5469 before final third-party certification.
The Halos AI Systems Inspection Lab member ecosystem spans over 43 companies and is growing. New members joining include Agility, Lyte AI , Neurealm , Ouster, and Peer Robotics . They joined existing members  including Boston Dynamics, KION Group, Infineon, Texas Instruments, NXP Semiconductors, Lattice Semiconductor, Synapticon, Reynolds & Moore , SecEdge (cybersecurity), and FORT Robotics .
## Get started with NVIDIA Halos for Robotics
To get started developing safety applications for robotics on NVIDIA IGX, register for NVIDIA Halos Core early access .
To start building outside-in safety agents, visit NVIDIA/halos-outside-in-safety on GitHub. Developers can now use two agent skills— warehouse-deploy and halos-deploy —to build and run outside-in safety agents with a single prompt. These skills handle prerequisites, NGC downloads, configuration, and the NVIDIA VSS Blueprint for warehouse operations plus Halos SIL deployment automatically. This means your team can skip manual setup and start adapting NVIDIA Halos Outside-In Safety Blueprint to your use case.
