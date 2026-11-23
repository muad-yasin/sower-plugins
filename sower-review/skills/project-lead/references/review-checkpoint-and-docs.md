# The review checkpoint and documentation discipline

*Open this file for the guard designs and the homes of the narrative: the depth behind `SKILL.md` sections 4 and 5, which hold the rules.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Part 1: the review checkpoint

### Why it is a named step

Small features are where scope creep hides: each one too minor for a review on its own, together the reason a milestone slipped (I: the source project's earlier skill states it). Run the checkpoint on anything reported finished, a two-hour fix included; its checklist is in `SKILL.md` section 4.

### Partial answers must declare themselves

A pass named after a big problem that solved a slice of it will be read by a later session as having solved the problem. On the source project a milestone shipped as a visual polish pass had touched only the interface chrome, and its owner flagged that it had never touched the 3D rooms (Seen). A feature that tracks only a checklist, read afterwards as "progression is now tracked", is the same shape (I: the earlier skill's example). The fix is one sentence in the report: *"this closes X; it does not touch Y or Z, which remain open."*

### Recurrence means a guard, not a reminder

`SKILL.md` section 4 holds the rule; on the source project a coverage test was written after a class of soft-lock recurred, and the navigation stack's own test later replaced it (Seen). Guard design, learned the expensive way:

- **List the paraphrases before you write the pattern.** A narrative leak sat for two weeks in a file the guard already covered, because its sentence said "verified" where the pattern said "confirmed"; the pattern was widened on 5 August 2026, and the next day it missed two more leaks worded another way (Seen).
- **A guard's file list is as easy to under-fill as its pattern,** and nothing about a clean run says what it did not read: an always-loaded document had been subject to the rule without ever being on the guard's list, until 8 August 2026 (Seen).
- **Pair a phrase check with a size check:** `SKILL.md` section 5 has the status line that reached 17,913 characters without tripping the phrase search (Seen).
- **Prefer an existing rule to an invented search** where one exists, such as a linter rule, a static analyser or a round-trip test: someone else maintains it, and its false positives are known (I).

### Recording deliberate overrides

`SKILL.md` holds the rule and its corollary, that a recorded decision outranks fresh reasoning. Write what was considered, what was rejected and why next to the decision, in the same pass, not as a footnote added later (I).

### The escalation triage

`SKILL.md` section 4 has the two questions. They decide whether to review; they are not a review (I).

## Part 2: documentation discipline

### Filing is part of shipping

`SKILL.md` section 5 holds the rule; on the source project the debt of unfiled narrative came back three times before it became one, on 11 July 2026 (Seen). Check that every pointer you write between documents points where the text lives: a dangling pointer is worse than none, because it reads as if there were something to read (I).

### Living documents and narrative destinations

Make every document one of two kinds, and say which:

- **Living documents,** read often or loaded automatically: the current state, the binding rules and pointers, never history or verification narrative.
- **Narrative destinations,** read on demand: history, build stories, incident logs, superseded specs. They are appended to, with each entry dated and left as written, so that a change of rule adds an entry instead of editing one.

**A designated narrative destination is exempt from the narrative guard, and the guard says so:** policing it would police the place the narrative is meant to land (Seen: the source project recorded that exception on 23 August 2026, and two more later).

### Keep checking after a split

On the source project, after each of its three splits, narrative crept back into the file that had been split, because it was written inline the first time instead of as a pointer (Seen). So the check is continuous, not one sweep after the split, and it runs against both ends: the file you split from and the file you split into (`specs-and-ordering.md` has the destination's case).

### Bound every carve-out

`SKILL.md` section 5 has the rule, and the source project's fourth instance of one drift pattern, this time inside a carve-out. The shape: a rule forbids X; an exception allows "a short note"; nothing defines short; the notes become essays, which the original guard cannot see because they are not technically X (I). If you grant an exception, give it a number and a check in the same edit.

### The automatic load is its own decision

Rules about the size of documents think per file, while an automatic load charges per spawn, and **a mechanism that charges per spawn is invisible to a rule that thinks per file.** On the source project four files were loaded into every agent spawn that was not a fork, about 90,000 tokens of preamble paid 5 to 15 times on a normal working day, and two of them served tasks most agents never do. Once two were taken out of the automatic load on 23 August 2026, a fresh spawn loaded about 47,000 (Seen). Ask now and then which files a given spawn needs; keep the binding subset inline as a short kernel, and load the rest on demand.

- **Verify such a change from a fresh session, never from the one that made the edit:** on the source project the instructions were taken when a session started and inherited by its spawns, so the editing session reported the old state (Seen: its observation of 23 August 2026).
- **Record the rollback** of such a change in one line next to it. That makes it cheap to reverse, and so cheap to try (I).
