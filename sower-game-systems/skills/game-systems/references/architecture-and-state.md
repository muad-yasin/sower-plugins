# Architecture and state shape

*Open this file when you design a new system, when two systems start needing each other, when you decide whether a value is stored or derived, and when something works in a fresh session but not on a loaded save. It is the depth behind `SKILL.md` rules 6, 7, 8, 9, 12 and 16.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **I** = inferred, with the reason in the sentence.

## The contract, in practice

A contract is three lists and nothing else:

```
System: <name>
Owns:    the state fields this system, and only this system, mutates
Methods: public entry points, with what each rejects and why
Events:  name -> payload shape, and the exact state guaranteed committed when it fires
```

The third column of the events list is the part people skip and the part that pays. "`TradeResolved` fires after the position is closed and cash is credited" is a testable promise; "`TradeResolved`" alone is not, and the lockout under "Commit before you announce" below is what it costs (I).

Write it against the interface flow, not in isolation. If the screen needs a running total and the contract exposes only a per-item event, you find out now, not after the view layer has grown a duplicate accumulator that drifts (I).

## Deep modules, and when an abstraction earns its place

**The target shape is a small public surface over a large hidden implementation.** Apply the deletion test at review: what would be lost if this module were deleted? A thin pass-through loses nothing (I).

**One implementation is a hypothetical seam; two are a real one. So no interface lands before its second implementation** (`SKILL.md` rule 12; I). The same test sorts wrappers: a wrapper earns its place by adding a policy. On the source project a stricter purchase method checked its own gates and rejected outright, and otherwise delegated straight into the existing permissive method, which kept its guards and its other callers, tests included, unchanged (Seen). A wrapper that only renames or forwards is sprawl: delete it.

## Events, glue, and why not direct references

Systems raise events; nothing inside a system reaches into another one. When two systems must react to each other (a finished delivery nudging a price, an achievement counting a trade, a sound on a state change), the reaction is a subscription in the **composition root**, the one place that constructs every system and wires them together:

```
// composition root, one file, readable top to bottom
delivery.Completed      += market.ApplyDeliveryBonus;
trading.TradeResolved   += stats.RecordTrade;
trading.TradeResolved   += audio.PlayTradeCue;
```

The payoff is not purity: **every cross-system coupling in the product is listed in one file**, so "what else happens when a delivery completes" has an answer you can read instead of a search. A direct call from inside a system is invisible from both ends. The source project's composition root held 86 subscriptions in one file when it was audited in July 2026 (Seen).

The cost: the glue file grows, and a subscription there is easy to leave behind in a system torn down mid-session. If systems live shorter than the app, pair every wiring line with its teardown in the same block (I).

**A project that already wires its systems another way keeps its pattern.** This rule is how a system is built with this skill, not a reason to rewrite one that works: where systems already call each other, or read each other through a service, build the change in that pattern and say that you did. Moving a project to events is its owner's decision, and the review plugin's scope gate checks for direct references only where the project's pattern is events or one composition root. This is a decision made for these plugins in November 2026, with no incident behind it.

## Initialization order: the two shapes that bite

Most engines give **no guarantee** which of two components initializes first within a frame. Two different failures come out of that, and they need different fixes.

**Shape 1: a consumer needs another system's current state.** It subscribed to an event that fires later, but it needs the value now, at first display. Fix: read it once at its own first real use, or subscribe and then call a sync method at once. Do not try to make the other side initialize earlier: that is a schedule you cannot enforce, and the next component hits it again (I). The source project hit this shape three separate times by July 2026, by its own count: a HUD revealed only on a stage-changed event, an offline-earnings panel that polled in its own `Start()`, and a gap in a screen root's reveal (Seen). Its session log counts a fourth in August 2026: a tutorial's overlay and pop-up handled the same event in whatever order their `Start()` calls ran, and nothing in the project pinned that order (Seen).

**Shape 2: an event fires synchronously during startup, before any subscriber exists.** Whatever the composition root raises while it constructs everything has already happened when interface code subscribes, so with a live subscription alone a save already past the trigger waits forever for an event that never fires again (I). Fix: **evaluate on load, plus the live event.** Every unlock-shaped system gets a method that evaluates the current state and fires whatever is now true, called once right after the start-up chain, alongside the live subscription and never instead of it (Seen: the source project's unlock checks for its mail and its achievements have this shape, as its earlier skill names them).

Both shapes are logical ordering, not thread safety: gameplay code is usually single-threaded (I). The rule that closes both, an ordering made explicit at the line that enforces it, is `SKILL.md` rule 8's; the fixes a model reaches for by reflex, "subscribe earlier" and "add a null check", address neither (I: the source project's earlier skill states it).

## Commit before you announce

The incident behind `SKILL.md` rule 9 (Seen, July 2026): a story's firing method raised its event one line above the call that recorded the story as shown. The subscriber that existed to re-run an unlock check therefore read the old state on its one guaranteed chance, every time, and the unlock waited for some unrelated later event to run the check again. The fix recorded first, after both subscribers of the event were checked for any dependence on the old order. A later audit found the order correct at both external triggers (Seen).

The same shape at file scale: can related updates leave the state half-applied? If a crash between two writes leaves a state the game cannot represent, restructure toward one atomic commit, the concern the save's temporary-file-then-rename solves at the disk layer (I).

**Two entry points, one fact.** When a fact can become true through a natural path and through a `NotifyXHappenedExternally` method, **diff their side effects before shipping either.** On the source project the external path did no chain bookkeeping, so a chain entered through it could never arm; it lay latent for weeks, because no earlier content used that path (Seen, as its earlier skill records).

## Store or derive

**Derive on read** whenever the value is cheap to compute from state you already persist. A derived value cannot drift from its source; a stored copy can, because its two update sites get edited months apart (I). Three tiers, and the choice is deliberate every time (I: the source project's earlier skill states the rule):

| Tier | Use for | Marker |
|---|---|---|
| **Persisted** | facts the game cannot recompute: what you own, where you are, absolute timestamps that measure wall-clock time across a restart | in the save schema, versioned |
| **Runtime only** | whatever lives inside one session: elapsed timers, cached lookups, this frame's derived totals | a plain field, ticked in the loop |
| **Re-rolled on load** | randomized *scheduling* state, such as the next fire position in a chain or a window offset, where losing the roll is acceptable and losing the guarantee it served is not | a comment saying exactly that, plus a rebuild step at startup |

The third tier exists because both neighbours are wrong for it. Persisting it bloats the schema for a value nobody would notice changing; treating it as runtime only loses the guarantee, the follow-up that was promised. So re-roll the window on load, and rebuild from persisted state the fact that a follow-up is still owed. **Say this in the field's comment**, or a later session will "fix" it into the save schema (I).

The one place a stored absolute timestamp is plainly right: measuring how long the app was closed. Nothing in memory survives the restart to derive it from.

## Silent failure, and where silence is correct

`SKILL.md` rule 16's contrast, at the length the distinction needs:

- **A defect:** an eligibility gate that rejects every candidate and produces an empty result. Nothing errors, and the bake finishes. On the source project one such gate split a generated route graph in half and left 40% of the city unreachable (Seen, July 2026).
- **Justified:** a save loader that returns null on a missing or corrupt file, documented at the site, with a backup file behind it. Throwing there would strand the player; the silence is the recovery path (I).

The test is whether the caller can tell "nothing to do" from "something went wrong". If it cannot, the silence is a defect however reasonable the catch looked (I). Gates, filters and eligibility checks are silent by default in the same way, which is why `SKILL.md` rule 14 pairs each with an assertion on its output invariant.
