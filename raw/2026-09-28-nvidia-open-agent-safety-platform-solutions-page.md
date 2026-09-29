<!-- captured 2026-09-29 via curl + BeautifulSoup text extraction from https://www.nvidia.com/en-us/solutions/ai/agent-safety/ -->

TITLE: NVIDIA Open Agent Safety Platform: Secure AI Agents
og:title: NVIDIA Open Agent Safety Platform
og:description: Open, customizable tools that enforce boundaries around AI agents.
og:url: https://www.nvidia.com/en-us/solutions/ai/agent-safety/
# NVIDIA Open Agent Safety Platform
Open, customizable tools that enforce boundaries around AI agents.
- Overview
- Benefits
- Technology
- Ecosystem
- Next Steps
- FAQ
- Overview
- Benefits
- Technology
- Ecosystem
- Next Steps
- FAQ
- Overview
- Benefits
- Technology
- Ecosystem
- Next Steps
- FAQ
Overview
## Engineering Full-Stack Safety
As agents become a digital workforce, developers need tools to verify the safety of their products. Without the right engineering solutions, AI agents can take actions with unintended consequences. NVIDIA Open Agent Safety Platform is an open reference design built with partners that continuously monitors and governs agent behavior, ensuring that AI agents follow the rules.
It features NVIDIA OpenShell™ , an open source runtime that provides governance tools to enforce what an agent can see, do, and interact with. The controls remain in force when agents behave unexpectedly, limiting how far mistakes spread. For organizations that want an additional, independent layer, NVIDIA Sentry provides out-of-band, in-silicon telemetry of agent activity and security-policy enforcement, enabling it to quarantine agents in milliseconds.
All of this is optimized to run on NVIDIA Vera CPU and NVIDIA BlueField DPU-based systems, and is also compatible with other hardware systems.
### Stronger AI Agent Security for Every Industry
NVIDIA Open Agent Safety Platform delivers full-stack governance, runtime control, and continuous monitoring to secure enterprise AI agents from testing to deployment.
### A Trusted Layer for AI Agents
NVIDIA introduces an open, full-stack safety platform to help teams keep AI agents isolated, observable, and governed as they take on more complex work.
Benefits
## A Layered Foundation for Agent Safety
Combine runtime governance, continuous threat detection, and hardware-isolated policy enforcement to keep AI agents contained, observable, and auditable.
### Defense in Depth
Multi-layered software and hardware work together to establish a secure runtime boundary around every agent. Policies are formally verified, so agent behavior is kept in check.
### Out-of-Band Agent Governance
Real-time, host-independent monitoring and enforcement maintain an independent security boundary, even if the host is compromised.
### Security at AI Agent Speed
In-silicon threat detection, identity governance, and policy enforcement work together to evaluate AI agents in real time and respond to detected deviations.
### Always-On Threat Detection
Gain continuous visibility into agent activity and behavior to detect threats as they emerge.
Technology
## Explore NVIDIA Open Agent Safety Platform
The software and hardware that govern, protect, and power AI agents at enterprise scale.
### NVIDIA OpenShell
- Separate how your agents execute from how they reach data, tools, and outside systems. Govern agent behavior with sandboxed execution and policy enforcement to safely scale agentic systems for your enterprise.
- Enforce deterministic governance with a zero-trust architecture that grants permissions based on intent and uses out-of-process enforcement that can't be bypassed.
### NVIDIA Sentry
- Observe every AI agent request and response using NVIDIA DOCA™ to enforce granular policy and provide complete, attested telemetry to inspect agent behavior and detect deviations at AI factory scale.
- Establish a verifiable identity for every agent to transparently authenticate each interaction and continuously govern access to data, tools, APIs, and services with zero-trust control.
- Enforce granular, zero-trust policies on every data access request to ensure agents and applications reach only the information they are authorized to use.
### NVIDIA BlueField
- Protect the full agentic AI stack—infrastructure, models, agents, and applications—with a unified, in-silicon security foundation across NVIDIA Vera systems.
- Extend zero-trust protection beyond software-only controls with a host-independent security domain that keeps enforcement separate from agent and host software.
- Monitor agent activity and behavior in real time through out-of-band visibility to detect and respond to emerging runtime threats.
### NVIDIA Vera CPU
- Vera is purpose-built for agentic reasoning, tool execution, and task planning—so the agent control plane lives on Vera.
- Vera achieves up to 80% faster sandbox performance than traditional CPU infrastructure, making “sandbox everything” the default instead of a tradeoff.
Ecosystem
## Leading Adopters Across All Industries
Industry leaders from across the AI ecosystem are joining NVIDIA to strengthen AI safety for every industry across the full stack of infrastructure, software, models and robotics.
## Next Steps
## Ready to Get Started?
Build and scale secure AI agents with NVIDIA Open Agent Safety Platform.
### Build
Access the open source OpenShell repository on GitHub.
### Documentation
Learn more about OpenShell by exploring the documentation.
## FAQ
### How do OpenShell, Sentry, BlueField-4, DOCA, and Vera work together?
Each component serves a distinct role:
- NVIDIA OpenShell governs how agents execute, what they can access and change, and where inference runs.
- Sentry with BlueField-4 delivers tenant isolation outside the agent’s execution environment and provides in-silicon threat detection, identity governance, and policy enforcement using DOCA.
- NVIDIA Vera CPUs provide high-performance, power-efficient compute for orchestration, sandboxed code execution, and data processing.
Learn more about NVIDIA Cybersecurity and NVIDIA AI Security Research .
### How do runtime controls differ from model safeguards?
Prompts, model safeguards, and agent frameworks influence what an agent attempts to do. Runtime controls enforce what it is allowed to do. OpenShell applies policy outside the agent process, while NVIDIA Sentry with NVIDIA BlueField-4 adds an independent security layer outside agent and host software.
### Can I use my existing agents and models?
Yes. OpenShell supports agents such as Claude Code, Codex, OpenCode, GitHub Copilot CLI, and OpenClaw. Teams can also bring custom agents and sandbox images. OpenShell supports open and closed models and provides a common runtime policy layer across agent workflows.
### Does OpenShell require BlueField-4?
No. OpenShell can run on supported local, on-premises, cloud, and Kubernetes infrastructure without BlueField-4. On systems with BlueField-4, Sentry adds hardware-isolated monitoring and enforcement that remain operational if the host or workload is compromised.
### How can teams audit agent activity and control permissions?
OpenShell provides an audit trail of allow and deny decisions and supports centralized collection of sandbox logs. Agents can request policy changes, with optional automatic approvals constrained by approved policy limits and enterprise governance. Operators retain control over the boundaries agents must follow.
- About Us
- Investors
- Venture Capital (NVentures)
- NVIDIA Foundation
- Research
- Corporate Sustainability
- Technologies
- Careers
- Newsroom
- Company Blog
- Technical Blog
- Webinars
- Stay Informed
- Events Calendar
- GTC AI Conference
- NVIDIA On-Demand
- Developers
- Partners
- Executive Insights
- Startups and VCs
- Documentation
- Technical Training
- Professional Services for Data Science
- Privacy Policy
- Your Privacy Choices
- Terms of Service
- Accessibility
- Corporate Policies
- Product Security
- Contact