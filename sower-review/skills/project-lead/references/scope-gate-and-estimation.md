# The scope gate, estimation and the pre-mortem

*Open this file when you run the gate inline or need to defend one of its steps: it is the reasoning behind `SKILL.md` section 3. The executable version is the `scope-gate` agent.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Why a gate exists at all

A solo developer or a team of two has no product manager and nobody else who can say no, so the gate is where a bad plan can still be caught before it becomes code (I). It is sized to that: six yes-or-no items and four short judgement calls, not a phase.

## The knockout items

Each is yes or no, and **a single "no" means the verdict cannot be GO.** The `scope-gate` agent holds them in full, with what makes each one a "no"; a gap in the first counts only when it changes what gets built. In short:

1. **A buildable spec:** a one-sentence goal that names how its completion is checked, scope items stated as what a user can do when the work ships, written non-goals, and success criteria a person can check. More than five scope items is a reason to look for a second milestone: an advisory finding, not a knockout.
2. **Every item serves the goal;** anything that does not goes to a written parking lot.
3. **No dead end, and every one-way step named:** no new failure state may leave a user with no way back, and each step that cannot be undone, such as a migration or a release, is named with how far its effects reach. In a game some route to income or progress always stays reachable; on a site no flow leaves a user on a dead page.
4. **Claims about the world hold,** where the plan touches real people, companies, brands, prices or laws: each is checked by search against its primary source, a renamed name does not keep the original inside it, and the project's own content rules still hold. Where the writer plugin is installed, its fact-checking skill has the full rules.
5. **Risk first:** the unproven part is scheduled before the comfortable work.
6. **Cost matches payoff:** say whether the plan reuses an existing mechanic or builds new surface, and whether the cost fits what the user gets. A full movement system for what could be a tap on a hotspot fails it.

## The four judgement calls

The knockouts catch a broken rule; these catch a plan that is wrong in a way no rule covers. Two or three sentences each.

### Base rate (the outside view)

Before judging feasibility, ask how long this class of work takes for a team of this size and experience, and how it usually goes wrong. Anchor on comparable past milestones in the project's own history where they exist.

This is reference class forecasting, which bases a forecast on "actual performance in a reference class of comparable projects" and so, by its author's account, bypasses optimism bias and strategic misrepresentation (D, Bent Flyvbjerg, "From Nobel Prize to Project Management: Getting Risks Right", arXiv 1302.3642, abstract read 2026-11-22). **Treat "this one is different" as a warning sign, not as a reason** (I: our inference from the method).

Where there is no reference class, for work that really is the first of its kind, say so plainly and give the dependencies and the unknowns instead of a number. A made-up estimate is worse than an admitted absence of one.

### Pre-mortem

Assume it is later, and the milestone shipped late, broke or was no fun; write the two most likely reasons. This is Gary Klein's technique, and the point is the tense: the team takes the failure as given and explains it (D, "Performing a Project Premortem", Harvard Business Review, September 2007, the page's summary read 2026-11-21). No figure for the method's effect is used here, because none was found in what was read. If either reason is severe and cheap to prevent now, that alone sends the spec back (I).

### Key assumptions

List what the plan rests on, and tag each assumption:

- **Solid:** verified in the docs or the code, in this pass.
- **Caveated:** probably true, and worth stating so that it is on record.
- **Unsupported:** nobody has checked.

**An unsupported assumption that the milestone depends on is a blocker until it is checked.** The tags are the point: an untagged list of assumptions reads as reassurance (I).

### Reuse

Name what already exists that the plan should build on. Search for related class and system names before assuming that something does not exist yet; it is cheap, and reuse beats reinvention. If the plan reinvents a pattern the codebase already has, say which one.

## The verdict

Exactly one overall decision, then the detail per item. The agent's verdicts are **GO**, build as scoped; **NEEDS-SPEC**, either (narrow), where each amendment folds in without changing the goal, or (rethink), where the goal or the shape has to change and the rewritten plan comes back to a gate; and **KILL-DESCOPE**, where the goal is not worth its cost at this stage. **Name the cheaper goal that survives a KILL-DESCOPE:** killing without an alternative is not a review.

Per item, give the verdict, a concrete failure mode and the cheaper alternative where one exists, and when you flag a rule, name it and where it comes from. Add one sentence to each finding: **what would change this verdict.** If you cannot name it, you do not have a finding yet. When the developer pushes back, derive the finding again from the spec, the docs and the code: revise when they show you something you got wrong, not because they disagree (I).

A gate that never returns KILL-DESCOPE is not a gate (I): the source project's gate returned it in September 2026 on a rework plan, because it checked the finding the plan rested on and found it false (Seen). A gate that returns it to look rigorous is worse.

## After the gate: amendments are claims, and claims rot

The rule and its case are in `SKILL.md` section 3. The loop that works:

```
gate -> fold the amendments into the plan -> check every amendment against the repository at path and line -> gate again if anything moved
```

The same discipline caught two real bugs before any code existed, in two different plans: a chain of scripted events that could never arm in the session its prerequisite fired, and a fee preview that would have drifted from the amount the run actually paid (Seen, July 2026). **A finding accepted as prose is not a finding closed.**
