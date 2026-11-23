# Dark-pattern screening for monetization and engagement design

*Open this file before you finalize a design with a monetization or engagement angle. SKILL.md keeps the binding boundary; this file keeps the law as last read, the taxonomy and the reasoning.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = read in the named source on the date given. **I** = inferred, with the reason in the sentence. Where each line comes from: `evidence.md`, its section on this file.

## The law, as last read

Treat this as compliance, not taste, and check the current law of each market before you rely on a pattern being allowed.

- **The EU's Digital Fairness Act is a proposal.** The European Commission adopted it on 11 November 2026. Among its targets are dark patterns, addictive design, practices that push people to overspend, and personalisation that exploits a consumer's vulnerabilities (the Commission's page on the act, read 22 November 2026, D). A proposal is not yet law: read its status again before you cite it.
- Earlier versions of this file also cited Article 25 of the EU's Digital Services Act and a staff report of the US Federal Trade Commission on dark patterns, "Bringing Dark Patterns to Light" (not checked at a source; named here since September 2026). Whom each binds is a legal question: read the text before you say that it applies to a game.
- A satire whose own monetization is predatory gets read as the thing it mocks (Seen: the source project's design guardrails). For a satirical product that reputational risk comes on top of the legal one.

## The named taxonomy to check against

King, Fitton and Cassidy (2023), "Investigating Players' Perceptions of Deceptive Design Practices within a 3D Gameplay Context", surveyed players and named six categories of deceptive design in 3D games (as the source project's research notes cite the study; the paper itself was not read):

- Predatory Monetization
- Default to Purchase
- UI Misdirection
- Emotional Interpersonal Persuasion
- Physical Placement
- Narrative Obligation

Check four more shapes by name: manufactured urgency, confirmshaming, disguised ads, and the **endowment-effect setup**: showing a reward, then gating it behind a purchase or an ad to keep it. The last one can pass for a feature. On the source project a design review stopped an offline-earnings recap that would have shown the amount earned and then required an ad to claim it; at that stage the recap stayed free, with no ad (Seen).

## The time axis counts as much as the money axis

Zagal, Björk and Lewis, "Dark Patterns in the Design of Games" (2013), name temporal dark patterns, grinding and playing by appointment among them (the paper, read 22 November 2026, D). Hold a new timed mechanic against a schedule that clamps instead of accruing: on the source project time away is never made up, so an absence of any length leaves exactly one headline waiting and nothing is lost by being away (Seen, August 2026). That gives a returning player a reason to open the app without punishing the one who stayed away.

## The boundary, and the second look

**No feature may ever SELL the recovery from a player's own mistake** (Seen). It is the line between letting mistakes teach and monetizing them, and the one rule here that is a veto, not a heuristic.

Before anything with real stakes in player psychology or monetization is built, get a second look from someone who did not design it: the review plugin's `design-review` agent where it is installed, otherwise another reviewer.

## Recording an override

When a monetization decision knowingly goes against the usual advice, write down what was considered, what was rejected and why, next to the decision, not as a footnote added later. Two decisions on the source project look like defects to a later reviewer, and both were recorded (Seen): an ad the player opts into that cannot be skipped once it starts, and a shop and a settings screen written straight, with honest real-money wording, in a game whose voice is otherwise satirical. Unrecorded, both get "fixed" back toward the usual default by someone acting in good faith.
