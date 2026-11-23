# Typography roles and world-to-screen spatial mapping

*Open the typography section before you name a new role for type or bring in a new typeface, and the mapping section before any placement or moving pass under a fixed 3D camera. Review of 2D icons and of the interface does not need the second half.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Typography roles: chrome or display, body, data and numerals

`SKILL.md` keeps the restraint and the shared type scale. Behind the scale: the source project replaced 21 ad hoc font sizes with ten named tiers after an audit of every call site (July 2026), and a later redesign replaced those with seven (Seen). **Which** faces is its own decision, and a type stack arrived at by default reads as generic the way an unanchored palette does (I).

**Where a product wears a diegetic conceit, the type stack carries weight.** A fictional phone's type does the work a real system font does: it is the fastest signal of what kind of device, and what kind of world, the player is holding (I). Treat the type stack like the palette: written down, checked against, and **a new face needs a stated reason tied to meaning.**

Three roles worth naming, even when families are shared across them:

- a **chrome or display** face: app names, headers, the interface's own furniture;
- a **body** face: prose, mail, dialogue, the reading surfaces;
- a **data** face for numerals: prices, tickers, timers, ledgers.

Sharing one family across two roles is a legitimate, anchored answer, not a compromise. **A third, hero face is a named tier, never a general-purpose face:** on the source project it was brought in for exactly two call sites, a third site is its own decision and never an inheritance, and the tier carries no curve from size to weight, so that nothing can adopt it by default (Seen, August 2026).

**The numerals role needs tabular figures** (`SKILL.md`). In TextMeshPro they may have to be baked into the font, because it exposes no arbitrary OpenType features: the source project's redesign planned exactly that, with proportional figures as the fallback (Seen: a plan of 5 August 2026).

## World-to-screen mapping for a fixed, non-orthogonal camera

Translating screen-relative language ("move it top-left", "make it bottom-right") into world coordinates is a gap this work keeps hitting (I). The procedure below is the one the source project used through three rounds of placement requests in one session, with the sampling of the floor's corners recorded for the first two (Seen, July 2026):

1. **Never place or move an object by judging where it will land on screen.** An isometric or angled camera does not map world axes to screen directions intuitively: the same amount of world "up" can read as screen left, screen right or both, depending on the axis that moved (I).
2. **Build the real mapping first.** Sample the engine's world-to-viewport projection at known landmarks, such as room corners, existing fixtures and wall planes, before placing anything new. Three or four samples show which world axis increases toward which screen direction, and how strongly; trust that over intuition.
3. **A camera's screen extremes are not always reachable together.** "Top left" may not be a reachable corner when two world axes pull the screen position in conflicting directions at the room's real proportions. Then favour the direction named most specifically, keep the other from getting worse, and **say so** instead of silently forcing a worse compromise (`SKILL.md` has the source project's case).
4. **Check real clearance, not only non-overlap,** against every neighbour's actual footprint before committing: a fixture that does not intersect another can still crowd it at the distance the camera renders it from (I).
5. **Reuse a shape by duplicating, rescaling or recolouring and repositioning it** for cheap, convincing variants, instead of new geometry wherever a family of shapes already reads right. The scaled-up form is the **modular kit**: a few base footprints, varied by material swaps and overlaid props, give many objects that read as distinct (I: the source project's earlier skill states the rule). Grow a kit rather than authoring one-offs, and include **at least one deliberate, hand-placed irregularity**, or the repeated rule shows.
6. **Prefer primitives with a proven record in the current pipeline** to an untested one that fits better on paper: on the source project the arch primitive proved dimensionally unpredictable, and the first desk ended on four cylinder legs (Seen, July 2026).
7. **Block out a genuinely new layout with placeholder shapes before building final geometry** (`SKILL.md`). A cube at the target position, checked for scale, clearance and its read on screen, is cheap to move; a finished prop is not. It matters most when the mapping of step 2 is being worked out for the first time in a new space (I).
