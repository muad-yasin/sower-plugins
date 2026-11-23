# Specs and ordering: the long form

*Open this file when you write a milestone spec in full, cut a scope list with Must, Should, Could and Won't, or move a shipped spec into an archive. It is the depth behind `SKILL.md` sections 1 and 2, which hold the rules.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## The one-page spec

```markdown
# <Milestone name>

**Goal.** <The question this milestone answers, in one sentence, and how its completion is checked.>

**Scope** (three to five items, each something a user can do)
1. ...
2. ...

**Non-goals** (deliberately not built yet)
- ...

**Success criteria**
- <What a user can do at the end that they could not at the start, and how that is checked.>
```

That is the whole artifact. If it takes more than a minute to read again, it is a design document: point to one instead of containing it. Both that bound and the count of three to five are the source project's earlier skill's rules, with no incident behind the numbers (I).

### Why success criteria are about what a user can do

"Build the trading backend" cannot be checked. "A player can place a trade on a live news event and see the position resolve" can be checked by one person without reading any code, and it survives a refactor, where the first describes an implementation that may not be the one that ships (I). The same test catches a milestone named after a class: if the name is a noun from the codebase, not something a user does, the spec describes work instead of value (I: the earlier skill names the smell).

### Why the list of non-goals is the important half

The scope list is what everyone agrees on; the non-goals are what stop the same argument from coming back in week three in different words. An exclusion nobody wrote down is not an exclusion (I). Write non-goals as claims, not omissions: "no multiplayer" is weaker than "no multiplayer in this milestone, and the save schema deliberately reserves no fields for it."

## Cutting a list that is too long

When cutting is hard, sort the candidates into Must, Should, Could and Won't before arguing about them (I: the earlier skill's method). Two properties matter more than the method:

- **The Won't items go to the parking lot in writing,** never dropped in silence: a written park can be recovered, while a silent drop reads later as an oversight and gets proposed again.
- **Sorting first makes the cut a visible decision,** instead of an argument about which idea is better, which nobody wins.

If everything lands in Must, the milestone is two milestones.

## Ordering several milestones

`SKILL.md` section 2 holds the rule: risk and dependency before ease. The usual forms of the mistake (I):

- polishing the interface of a loop nobody has confirmed is fun;
- building the content pipeline before one piece of content has been made by hand from end to end;
- deferring the third-party integration (payments, ads, sign-in, the store) because it is unpleasant, although it is the one with an outside clock and someone else's approval on it.

**Spec now, build later**, the case: on the source project a late stage's endgame numbers were specified and then held until a visual-polish pass and an economy retune had run, so that they would not be tuned twice; the stage later shipped in full (Seen, July 2026). Say in the spec what it waits on, or it decays into a parked idea that nobody reads again.

## Micro-goals inside a session

`SKILL.md` section 2 holds the rule. What it buys: a block that ends without its stated goal met is a signal on the same day, where a vague long session gives none until the milestone is late (I).

## How specs age

A spec has two lives:

1. **Live:** while the work is in flight, it sits where planning happens, and the review checkpoint checks against it.
2. **Archived:** once the milestone ships and settles, its full goal, scope, non-goals and criteria move to a specs archive, and the live document keeps a one-line stub under the same header.

**Keep the header identical,** so that every cross-reference that resolves in the live document still resolves in the archive (Seen: the source project's split of 22 July 2026 and its archive of 4 September 2026 both kept them). A renamed header breaks its references without a sound (I).

Two failure modes of the split, both seen on the source project:

- **A stub grows back into an essay.** Stubs allowed "a short note" on what is true today, from 31 July 2026, grew into several essays of many paragraphs, because nothing bounded "short"; the fix was a size check per section (Seen). Give a stub a size bound and check it mechanically.
- **The destination arrives bloated.** On the day of the split, 22 July 2026, an audit found the new specs file already carrying verification narrative, because sections had moved wholesale with it (Seen). Run the narrative check against the destination on the day of the split, not only against the file you split from.

## Untuned numbers

Record every first-pass constant (a price, a threshold, a duration, a drop rate) in **one consolidated ledger** that names the class, the field and the current value, instead of as a caveat inside whichever spec introduced it. A balance pass then reads one file, and a checkup can verify every named constant against its current value (Seen: the source project's ledger, added 11 July 2026). The source project's checkup first checked a sample of the ledger, then every constant from the same day, 22 July 2026, on its owner's call, because a sample risked a constant drifting for several runs before it was picked (Seen).
