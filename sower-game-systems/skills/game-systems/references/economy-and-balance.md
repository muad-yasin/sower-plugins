# Economy and balance math

*Open this file before any balance-tuning pass, any offline-income work, any new currency or income source, and any economy question after launch. It is the depth behind `SKILL.md` rules 5 and 13.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Derive from the fantasy, not from the spreadsheet

The design owns a short list of **player-facing checkpoints**: the moments the game promises, in order. "By the end of the second stage, one good trade beats a whole session of the starter job." "The big purchase should hurt the wallet." "No tier stalls longer than a session without a visible next thing." Formulas derive from those, never the reverse: a number that came out of a spreadsheet first and got its justification afterwards is the one that makes stage four feel like homework (I).

**Write the derivation at the constant: not the value, the trace.** Which checkpoint, what assumption about the player's rate, what the arithmetic was. An illustration, with numbers that are no project's:

```
// 2,000: the second shop's price. Checkpoint: buying it leaves change for one hire,
// so its trigger sits at 3,000. Player rate at this stage: ~X per run in the simulation
// harness, so ~N runs after the previous gate, inside "no tier stalls past a session".
```

That a model invents ungrounded balance formulas has no direct study behind it: it is inferred from the documented tendency to magic numbers and from weak numeric reasoning (I: the source project's earlier skill states this caveat). The guardrail is defensive, kept because it is cheap and because the incident below is real.

## The anchor rule, and the error of about sixty times

The incident behind `SKILL.md` rule 5 (Seen, July 2026): a draft of hiring income was checked against a target of about three weeks to fund a gate at the upgrade ladder's full ceiling, and the formula actually gave about 8.5 hours. The first of two gate passes caught it before the plan was approved. It also surfaced the deeper problem: the ceiling was reachable only after spending far more than the gate it was meant to threaten, so no number could be derived against it soundly. The numbers were derived again against an anchor of their own, breakeven hours per tier plus the time to the gate with no multiplier at all.

The structural form, worth knowing because it generalizes: **a derived value must never read a half-constructed value.** If a derivation depends on something that changes as the player progresses, state the progression point you derive *at*, and pin it (I). Two tunables that could drift apart need the decoupling test of `SKILL.md`'s Testing discipline; a worked case is in `testing-and-verification.md`.

## Read live, and recompute what is counted

`SKILL.md` rule 5 says to read a threshold live, never from memory. The same holds for anything counted, such as library sizes, roster counts and tier counts: recompute it from disk, because a hand-carried census goes stale silently and is trusted (I).

## Simulate offline, before and instead of waiting for live data

Run the cost and income formulas forward and plot the time to afford each rung of the ladder. If the systems layer is engine-free (`SKILL.md` rule 1), a plain test or console harness can tick income through simulated hours and print the time per rung, with no SDK, no players, no telemetry and no CI (I: the source project's earlier skill states the rule). For idle and incremental games the source project's earlier skill calls simulation close to mandatory, because exponential economies break in ways nobody predicts by reading the formulas (I).

The public body of work on that math: Anthony Pecorella's series "The Math of Idle Games" works through growth, cost, prestige and the balance of generators, with spreadsheet models for every chart (D, Game Developer, part I, 13 October 2016, first posted on Kongregate's developer blog, read 2026-11-22). His deck "Quest for Progress", subtitled "The Math and Design of Idle Games", is on GDC Vault's server under GDC Europe 2016 (D, read 2026-11-22); that the series works through that talk's topics is our reading of the article's "my most-recent talk" (I).

Keep the model as a living document and **derive it again after any retune**: a balance model that describes last month's numbers is worse than none (I).

## Simulate the player's session, not the aggregate

**Balance the net flow of each session, not only total faucets against total sinks.** A retune that keeps income per hour intact can still make a *session* feel like a loss, so check the curve per session at each stage (I).

A public case told for this (not checked at a source; stated here since September 2026): Diablo III's launch economy, where a session could end with no upgrade and less gold than it started with, although the economy balanced in aggregate. What Blizzard said when it removed the auction houses is narrower: the system "ultimately undermines Diablo's core game play: kill monsters to get cool loot", and the shutdown came on 18 March 2014 (D, Blizzard News, "Diablo® III Auction House Update", 17 September 2013, read 2026-11-22).

## Pacing bounds

Whatever bound the design agreed ("no tier stalls longer than a session without a visible next thing" is a good default) is measured against the time-to-threshold model, not against fresh arithmetic in the moment (I).

**Additive ladders compress under exponential income.** On the source project a ladder spaced in even steps of 5,000 looked fair in the numbers as written, and once compounding growth was modelled the real-time gaps collapsed to about 24 and 13 minutes; doubling each step evened them out (Seen, August 2026). It was found by modelling, not by playing.

**Watch for a threshold that straddles a boundary in another formula.** Ten days later the same ladder moved again because a partner's campaign halves its boost above a set net worth, so a partner pitched above it ran at half value for no reason a player could see; the ladder's steps are uneven since, on purpose (Seen, August 2026). When you move a threshold, re-solve everything derived from it in the same edit, and add a test that reads the related values from live data and fails if either half moves alone (Seen: the test that guards that campaign).

## An asymmetry found is not an asymmetry to fix here

The case behind `SKILL.md` rule 13 (Seen, July 2026): grounding a trading change in the real formulas showed that buying a dip out-levers shorting a crash, because the liquidation formula caps a short's payout at twice the stake while an upward swing has no cap. The owner kept the stake the same for both directions and left any rebalancing to a later pass with the knobs that already exist, rather than a compensating multiplier on one side.

## After launch, when it becomes real

The unit of analysis is **the flow of each currency**, every source and sink as a signed event, plus **the funnel between stages**: what share of players reaching stage N reach N+1, and the wall-clock time between. A cliff in the funnel points at one tunable, which is the reason to measure at all (I).

Two boundaries:

- This says **what** to measure. The telemetry mechanism is a separate decision with its own costs in privacy, size and consent: **never pre-install an analytics SDK on the authority of this paragraph** (I).
- **Tuning the economy from live telemetry**, with faucet and sink ratios, revenue per paying player and A/B tests, is deliberately not imported: it is machinery for a shared or heavily monetized economy, and for an offline single-player game with one small honest purchase it buys nothing (Seen: the source project's earlier skill records the decision). It is listed so that a reader knows it was considered and scoped out.

## The monetization boundary

One rule, a veto rather than craft: **no feature may sell the recovery from a player's mistake** (Seen: a boundary the source project's design review set in July 2026). It is the line between letting mistakes teach and monetizing them. Everything else about pricing is a product decision, not a systems one.
