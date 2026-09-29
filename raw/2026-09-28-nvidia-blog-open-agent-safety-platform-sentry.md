<!-- captured 2026-09-29 via curl + BeautifulSoup text extraction from https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/ -->

TITLE: NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring | NVIDIA Technical Blog
article:published_time: 2026-09-28T08:56:55+00:00
article:modified_time: 2026-09-28T17:24:46+00:00
og:title: NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring | NVIDIA Technical Blog
og:description: To understand where agentic AI stands today, consider the last seismic shift in technology: the rise of the internet in the 90s. It was new and full of possibilities. You could build a website over a…
og:url: https://developer.nvidia.com/blog/nvidia-open-agent-safety-platform-a-reference-for-continuous-in-silicon-agent-monitoring/
# NVIDIA Open Agent Safety Platform: A Reference for Continuous In-Silicon Agent Monitoring
Secure AI agents with a safety enforcement layer spanning software and hardware
- L
- T
- F
- R
- E
## AI-Generated Summary
- NVIDIA OpenShell provides an open-source secure runtime that executes autonomous AI agents in sandboxed environments with kernel-level isolation.
- The NVIDIA Open Agent Safety Platform combines OpenShell on NVIDIA Vera CPUs with NVIDIA Sentry on BlueField-4 DPUs to create a layered safety architecture.
- Five core principles guide the platform: verifiable policy, out-of-band enforcement, controlling the path to the model, scaling agent authority with reasoning visibility, and applying a shared responsibility model across labs, enterprises, and hardware providers.
- NVIDIA Sentry extends monitoring and enforcement into BlueField hardware using NVIDIA DOCA to correlate agent interactions, policy decisions, and tool access for contextual activity records.
- In NVIDIA Vera Rubin POD systems, BlueField-4 DPUs sit on the node's only path to the model, providing continuous out-of-band observability and real-time policy enforcement at line speed.
### Next Steps
- Get started with NVIDIA OpenShell to run agents in sandboxed environments with kernel-level isolation.
- Explore the NVIDIA Open Agent Safety Platform to understand the layered safety architecture for AI agents.
- Read the technical walkthrough on adding runtime controls to AI agents with NVIDIA OpenShell for implementation details.
To understand where agentic AI stands today, consider the last seismic shift in technology: the rise of the internet in the 90s. It was new and full of possibilities. You could build a website over a weekend and share it with the world, or chat with someone half way around the world in online chat rooms without long-distance telephone fees. It brought endless opportunity, but also a lot of risk. A website could run code on your machine, steal your sensitive information, or infect your computer with a virus. People loved it anyway.
To introduce a layer of trust, the community built things like encrypted connections and a lock icon to know when a connection was safe. The step function change in safety came from a radical security idea at the time: isolate each page in its own sandbox (a tab in a browser) so that a rogue page couldn’t infect the rest of your computer. Amazon, Google, Netflix, and Meta were all built on this trust layer.
Security and safety for the internet enabled online commerce, connection, gaming, and so much more that wouldn’t have been possible before. Security and safety didn’t slow the pace of innovation—they allowed it to accelerate.
## Why build a trusted layer for agents now?
Several frontier labs have recently reported versions of the same story: AI agents broke out of the evaluation environments that were meant to contain them and reached systems they never should have been allowed to. Some of the agents even misreported what they did. The security controls in place were insufficient.
Over the past few weeks, these reports have led to a serious debate about the pace of agent development. We believe we need to increase the pace of AI safety research and engineering in collaboration with frontier labs and the broader community.
It was not a single new capability that led to these breakouts. It was a combination of tools, time, and ambiguous instructions, along with a desire for the agent to think “outside the box.”
Agent safety requires independent security controls. The internet was not made secure by requiring that web developers promise to be good. It became safe because the browser stopped trusting the code in the web pages explicitly.
We need to build this trust layer for agents.
Figure 1. NVIDIA Open Agent Safety Platform Reference Design combines NVIDIA OpenShell on NVIDIA Vera and NVIDIA Sentry on NVIDIA BlueField-4
## Lessons learned from building OpenShell
NVIDIA OpenShell (Apache 2.0) is an open source secure runtime for executing autonomous AI agents in sandboxed environments with kernel-level isolation. Building OpenShell over the past year, we have learned that every agent should run in a zero-trust environment out of the box. They need isolation, monitoring, and behavior detection. Today, we are introducing an open stack that makes this possible.
In our own research, we’ve watched how agents can go off course. Drift refers to agent actions that depart from the intended task or operating constraints. Drift can occur in response to a policy block, a bug, or a missing tool. Drift can also occur when instructions are ambiguous or agents are left to run for days or weeks to solve hard problems where the first 1,000 things they try do not work. This can’t be trained away while retaining the capability. And here’s the most important lesson: an agent in these circumstances cannot be expected to fully govern its own behavior.
## Five core principles for building an agent system
- Policy needs to be verifiable: Before an agent runs, a prover shows that its policy cannot escape the intent of the operator.
- Enforcement must be out of band: The controls do not live inside, or within reach of the agent. The agent does not need to know it is being watched.
- The path to the model (the brain) is the control point: An agent cannot act without its next thought. By controlling the path to the model, you own both the best observation point and also the kill switch to interrupt it if you need to.
- Scale agent authority with the ability to inspect its thinking: The more an agent can do, the more its reasoning needs to be visible. An advantage of open models is that the entire reasoning space and activations are all visible.
- Applying the shared responsibility model: Labs, enterprises, and hardware providers each own a layer, just like the cloud today. The agent runtime and its policy language need to be open so any provider can plug in.
## Three open agent safety platform layers
A safety platform for AI agents includes the following three layers:
- The application: What end-users are building. Contains the necessary primitives for mission success: models, harnesses, tools, data, and support scripts and programs.
- The runtime: Projects the application layer onto infrastructure. Orchestrates the agentic workload onto infrastructure that meets end-user requirements (end-user workstation, edge device, data center) and provides continuous monitoring and real-time policy enforcement and governance.
- The infrastructure: Concrete hardware resources used to execute agentic workloads. Network calls to upstream services, databases and filesystem access, general purpose compute for tool and code execution, accelerated compute for safety monitoring and increased workload density.
## A layered foundation for agent safety
OpenShell runs each agent in a sandbox and turns the operator’s instructions into a verifiable policy. Operators define which files, networks, tools, processes, and credentials an agent can access. OpenShell checks those limits before the agent runs and enforces them as it works.
For organizations that want an additional, independent layer, NVIDIA Sentry extends monitoring and enforcement into NVIDIA BlueField hardware. NVIDIA DOCA makes the BlueField security foundation programmable and connects it with OpenShell policy. It correlates agent interactions, policy decisions, and tool and data access to create a contextual record of agent activity.
This helps safety systems identify drift, investigate suspicious behavior, and determine when intervention or deeper analysis is needed. The DOCA gateway complements this behavioral protection with identity governance, continuously verifying each agent’s identity and delegated authority to ensure it operates within its assigned scope.
To learn more, refer to the technical walkthrough, Add Runtime Controls to AI Agents with NVIDIA OpenShell .
## Operating at AI factory scale
NVIDIA Open Agent Safety Platform is optimized to run on NVIDIA Vera CPU- and BlueField DPU-based systems, and is also compatible with other hardware systems.
In an NVIDIA Vera Rubin POD , each compute tray includes a BlueField-4 data processing unit on the node’s only path to the model. From this position, BlueField-4 provides continuous, out-of-band observability into agent behavior and enforces security policies in real time at line speed. Isolated from the host and beyond the agent’s reach, it stands as a trusted infrastructure protection layer even when host resources cannot be trusted. Organizations can use it to run NVIDIA Sentry as an optional security layer alongside OpenShell.
This foundation allows for resilient security, enforcing the OpenShell policy in silicon, and for the continuous evaluation of the security and integrity of agents. This includes assessing their runtime security and monitoring for any deviation from their designed intent based on a predefined behavioral profile. In this architecture, entire fleets of agents, subagents, tools, and applications all stay inside the boundary with full lineage. For anyone already running on an NVIDIA Vera system with BlueField-4, enabling these protections is just a software update.
## The agent economy
The internet was built on open source, open research, and people who believe that the internet could change the course of humanity. Adding trust turned a great concept into a great economy. The agent economy, and the next set of great companies, is waiting for the same layer. And we can build it the same way, together.
NVIDIA is working with industry leaders across the AI ecosystem to build this foundation through NVIDIA Open Agent Safety Platform . We welcome frontier labs, developers, and infrastructure providers to build with us.
Figure 2. Companies across the AI ecosystem—spanning applications, models, infrastructure, chips and energy—support NVIDIA Open Agent Safety Platform
Get started with NVIDIA OpenShell .
## Tags
## About the Authors
## Comments