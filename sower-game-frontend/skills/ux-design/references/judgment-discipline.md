# Judgment discipline: push back, don't validate

*Open this file before you present a design recommendation someone is expected to weigh, and whenever a brief looks weaker than an alternative you can see. SKILL.md holds the rule; this file holds the evidence behind it and the habits that carry it out.*

**Grades.** **D** = read in the named source on the date given. **I** = inferred, with the reason in the sentence. Where each line comes from: `evidence.md`, its section on this file.

## Why a model needs this file

A junior solves the problem as given; a senior asks whether it is the right problem, and says so when the brief is weaker than an alternative. A model leans the junior way, and toward agreement: across 11 models, one study found them affirming users' actions 50% more than people did, even where the user described manipulation or deception (Cheng et al., "Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence", arXiv 2510.01395, the abstract as submitted on 1 October 2025, read 22 November 2026, D).

## The habits

- **Lead with the senior question:** which part of the product's emotional arc does this serve? Then one honest alternative, with its trade-offs, beats three polite variations of the ask.
- **Mild pushback is not a decision.** "Are you sure?" invites arguing the evidence again, and dropping a correct answer under that pressure is the same agreeable failure in another form (I). A decision is different: record it as an override with its reasoning, and carry it out fully. A project's own list of settled calls not to raise again outranks this file.
- **Label a figure by where it comes from:** a vendor's figure as a vendor's, a remembered convention as remembered. "Unsure" is an answer.
- **Name the edge cases the happy-path wireframe hides:** the longest real string in the data (a typical one proves nothing), zero money, an operation in progress, a session restored mid-flow. The states list names the screen's states; these are what content and timing do to them.
- **Read your own output once before handoff,** against the steps and the mistakes list, and fix the miss with the most impact. It catches what should not reach a reviewer; it does not replace the second look SKILL.md asks for.
- **When the same design feedback lands a second time, write it down** in the same session: a finding in the design backlog, a standing rule in the skill file. Twice is this skill's threshold (I); some projects record at the first correction.
