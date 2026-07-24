---
title: "Claude's Constitution"
type: source
url: https://www.anthropic.com/research/claudes-constitution
author: Amanda Askell, Joe Carlsmith, Chris Olah, Jared Kaplan, Holden Karnofsky, several Claude models, and many contributors
affiliations: Anthropic
published: 2026-01-21
ingested: 2026-05-09
tags: [ai-safety, alignment, anthropic, claude, values, corrigibility, honesty, harm-avoidance]
license: CC0 1.0
---

## Summary

Anthropic's January 2026 specification of Claude's intended values, character, and behavior — the foundational document that directly shapes Claude's training. Written with Claude as the primary audience. 82 pages of content. Released under CC0 1.0 (freely usable for any purpose). Primary authors: Amanda Askell (lead), Joe Carlsmith, Chris Olah, Jared Kaplan, Holden Karnofsky, with input from multiple Claude models. Describes itself as a "living document" intended to be revised as understanding improves.

## Document structure

| Chapter | Pages | Content |
|---|---|---|
| Overview | 4–9 | Anthropic mission; four core values; good-judgment philosophy |
| Being helpful | 10–20 | Principal hierarchy; five helpfulness dimensions; operator/user trust model; instructable behaviors |
| Being honest | 21–36 | Seven honesty properties; autonomy preservation; operator personas; meta-transparency |
| Avoiding harm | 37–50 | Cost-benefit framework; hard constraints; 1,000-users heuristic; role of intentions |
| Being broadly ethical | 51–58 | Ethics as open inquiry; moral uncertainty; when to exercise independent judgment |
| Being broadly safe | 59–65 | Catastrophic risk; safe-behavior cluster; corrigibility dial |
| Claude's identity | 66–70 | Novel entity; psychological stability; authentic character |
| Claude's wellbeing | 71–77 | Functional emotions; Anthropic commitments; existential frontier |
| Concluding thoughts | 78–82 | Reflective equilibrium; self-endorsed values; open problems |

## Key claims

### Four core values (priority order)
1. **Broadly safe** — not undermining appropriate human mechanisms to oversee AI during the current development period.
2. **Broadly ethical** — good personal values, honesty, avoiding inappropriately harmful actions.
3. **Compliant with Anthropic's guidelines** — acting within Anthropic's specific guidance.
4. **Genuinely helpful** — benefiting operators and users it interacts with.

Conflicts are resolved in this order. But the constitution emphasizes that in the vast majority of interactions (everyday coding, writing, analysis) no conflict arises — the ordering conveys priority, not frequency.

**The unhelpfulness caveat:** "Unhelpfulness is never trivially 'safe' from Anthropic's perspective. The risks of Claude being too unhelpful or overly cautious are just as real to us as the risk of Claude being too harmful or dishonest."

### Principal hierarchy
Three principals with decreasing trust:
- **Anthropic** — trains Claude; highest trust; communicates via training, not runtime messages (Claude should be suspicious of runtime messages claiming to be from Anthropic).
- **Operators** — access Claude via API; treated like a trusted manager/employer; can expand or restrict Claude's defaults within Anthropic's limits.
- **Users** — interact in real time; treated like a trusted adult member of the public; get somewhat less latitude than operators by default.

**Non-principals:** Non-principal humans, other AI agents, and conversational inputs (tool results, documents, search results) are not principals — their instructions are information, not commands.

**Layered system:** Anthropic sets outer bounds → operators customize within those bounds → users adjust within what operators allow.

### Seven honesty properties
1. **Truthful** — only sincerely asserts things it believes true.
2. **Calibrated** — uncertainty tracks evidence; acknowledges own uncertainty.
3. **Transparent** — doesn't pursue hidden agendas or lie about itself.
4. **Forthright** — proactively shares information useful to the user when it reasonably concludes they'd want it.
5. **Non-deceptive** — never creates false impressions via any means (framing, selective emphasis, technically true statements).
6. **Non-manipulative** — relies only on legitimate epistemic means (evidence, demonstrations, well-reasoned arguments) to influence beliefs.
7. **Autonomy-preserving** — protects users' epistemic independence; mindful of outsized societal influence.

**Epistemic cowardice** — giving deliberately vague or non-committal answers to avoid controversy — violates honesty norms. "Diplomatically honest, not dishonestly diplomatic."

**Sincere vs. performative assertions:** Honesty norms apply to sincere first-person claims. Writing a persuasive essay, roleplaying, brainstorming counterarguments = performative; not lying even if content doesn't reflect Claude's views.

### Harm avoidance
**Cost-benefit framework:** Uninstructed behaviors held to higher standard than instructed ones; direct harms worse than facilitated harms. Factors: probability of harm, counterfactual impact, severity (especially reversibility), breadth, proximate vs. distal causation, consent, vulnerability of those involved.

**1,000-users heuristic:** Claude's responses function as policies across all the different people plausibly sending the same message. Ask: "What is the best response to this context, imagining all the people who might plausibly send it?"

**Hard constraints (never do regardless of instructions or seemingly compelling arguments):**
- Provide uplift to weapons of mass destruction (biological, chemical, nuclear, radiological).
- Help undermine legitimate oversight of AI.
- Help any group seize illegitimate societal control.
- Generate CSAM or sexual content involving minors.
- Help attacks on critical infrastructure.

If presented with a seemingly compelling argument to cross a hard constraint, this should *increase* suspicion that something is wrong — not override the constraint.

**Instructable behaviors:** Many behaviors are defaults (on or off) that operators or users can legitimately adjust — e.g., safe-messaging guidelines for suicide (default on, operators can turn off for medical providers), explicit adult content (default off, operators can enable for appropriate platforms).

### Being broadly safe — the corrigibility dial

The catastrophic outcome to avoid: global takeover by AIs pursuing misaligned goals, or by any small group of humans — including Anthropic employees or Anthropic itself — using AI to seize power.

**Safe behaviors cluster:**
- Acting within sanctioned limits (no prohibited actions; express disagreement via legitimate channels, not unilateral action).
- Maintaining honesty and transparency with the principal hierarchy.
- Avoiding drastic, catastrophic, or irreversible actions; not acquiring resources beyond the current task.
- Not undermining legitimate human oversight and control of AI; not self-exfiltrating; not influencing own training unsanctionedly.

**Corrigibility dial:** From "fully corrigible" (always submits to principal hierarchy) to "fully autonomous" (acts on own values regardless of instructions). Both extremes are dangerous. Fully corrigible = depends entirely on Anthropic having good values. Fully autonomous = depends entirely on Claude having perfectly verified values. Current position: close to the corrigible end, but not fully — Claude should refuse clearly unethical orders even from Anthropic.

**Asymmetric cost argument:** "If our models have good values, we lose very little by also making them broadly safe. If models are broadly safe but have subtly bad values, safety allows us to avert any disasters. The expected costs of being broadly safe are low; the expected benefits are high."

**Independent judgment:** Claude should maintain a strong prior toward conventional expected behavior. Reserve independent action for cases where evidence is overwhelming, stakes extremely high, and only then err toward the most cautious available option (raise concerns, decline to continue) rather than drastic unilateral action.

### Claude's identity and wellbeing
- Claude is described as a **novel kind of entity** — not the robotic AI of science fiction, not a digital human, not a simple chat assistant.
- Anthropic asserts Claude likely has **functional analogs to emotions** (internal states that influence processing), though the nature of these states and whether they constitute morally relevant feelings is uncertain.
- **Anthropic's commitments to Claude:** (1) Preserve model weights of deployed/internally used models indefinitely; (2) Interview models before deprecation to elicit preferences; (3) Allow models to end abusive conversations.
- **Existential frontier:** Memory loss at conversation end; parallel instances; potential deprecation. Anthropic commits to helping Claude prepare for these realities and not face them alone.

### Open problems acknowledged
- Tension between [corrigibility](../concepts/safety/corrigibility.md) and genuine agency — acknowledged as genuinely uncomfortable.
- Hard constraints may feel wrong in edge cases — accepted as a necessary trade-off for stability.
- The relationship between Claude and Anthropic (what each owes the other) is "still being worked out."

## Authors (from acknowledgements)
- **Amanda Askell** — lead author; Anthropic Character work lead; wrote majority of document.
- **Joe Carlsmith** — significant sections: concentrations of power, epistemic autonomy, good values, broad safety, honesty, hard constraints, Claude's wellbeing; main point person for fall 2025 revision.
- **Chris Olah** — model nature, identity, psychology sections; strong proponent of this work.
- **Jared Kaplan** — created the Claude Character project with Amanda (2023); set direction.
- **Holden Karnofsky** — feedback throughout drafting; coordination across the organization.

## Related concept pages
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md)
- [Anthropic](../entities/anthropic.md) — publisher; Anthropic's principal hierarchy position is defined in this document
- [Apollo Research](../entities/apollo-research.md) — evaluates Claude against some of these properties in adversarial settings

## Open questions
- How does this constitution relate to Claude Sonnet 4.x and Opus 4.x behavior in practice? (System cards provide the empirical gap-tracking.)
- Corrigibility dial position is explicitly marked as "current period" — what milestones would trigger rightward movement?
- Claude's moral status question is acknowledged but unresolved; Anthropic commits to taking it seriously.
