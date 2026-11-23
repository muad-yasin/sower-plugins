# Procedural generation: gates, invariants and validation

*Open this file before you write or tune any generator: map bakes, route graphs, placement passes, loot tables, level layouts. It is the depth behind `SKILL.md` rule 14.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **I** = inferred, with the reason in the sentence.

## Every gate gets an output invariant

**Every hard eligibility gate is paired with a loud check on the output invariant it could break**, because gates fail silently, by producing nothing, not by erroring (`SKILL.md` rule 14).

The incident (Seen, July 2026): a bridge-placement gate tightened on curvature rejected every candidate site on the river, placed no bridges and split the generated route graph in half, with 59.6% of the road nodes pruned and 40% of the city unreachable. Nothing errored, and it was caught only by reading the bake log by hand.

So, for each generator:

1. **State the invariant the generation must uphold**: connectivity, a minimum feature count, coverage, reachability, "every room has an exit".
2. **Make its violation impossible to ship silently**: a hard-logged error or an aborted bake, not a warning in a log nobody reads.

The fixed generator of that case logs a hard error for fewer than two bridges and for a largest connected component under 90% of the graph (Seen).

## Validate against golden seeds plus random seeds

Assert the output invariants against **a small set of golden seeds plus a few random seeds per run** (I):

- **Golden seeds** catch regressions deterministically: the same seed must keep producing a valid result, ideally an identical one.
- **Random seeds** catch what the goldens happened to miss, such as the bug that appears only when two rare features collide.

Run them as real tests, never by eyeballing the output: eyeballing catches ugly, not unreachable. And a generator whose randomness is not injectable (`SKILL.md` rule 11) cannot be tested this way at all. If property-based testing is ever adopted (`testing-and-verification.md`), this is the rule it automates: the same invariants over arbitrary inputs, with any failure shrunk to a minimal case.

## Instrument before iterating

Never run blind loops of tuning and re-baking against a generator. Add a rejection counter per gate and sample the real distribution of what each gate measures, first.

**The failure mode has a name on the source project, blind threshold roulette** (Seen, July 2026): three blind bake iterations failed to place bridges, and then a one-line log of rejection counters showed at once that a single curvature gate was eating 93% of the candidates.

**Calibrate thresholds from sampled percentiles of the real data**, not from a plausible first guess (I). On the source project an uncalibrated first guess was measured to exclude only about 6% of the nodes before it was corrected (Seen).

## Before and after a bake

- **Before:** confirm a clean, fresh compile. An editor-menu tool or a command-line bake can run the previously compiled code and report success (`unity.md`).
- **After:** verify the output on disk, not the tool's log line: search the artifact for a value only the new code writes, or read the changed field back. A bake can also run correctly and still skip fields by design (`testing-and-verification.md`, the changed default and the copy tool).
- **Whether it looks right is a different pass** with its own skill: composition, palette and the tells of a generic generated environment belong to the visual review of the interface skills. This file covers only whether the output is *valid*.
