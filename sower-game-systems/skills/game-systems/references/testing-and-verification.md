# Testing and verification for pure logic

*Open this file before a balance verification pass, before adopting any test tooling, and whenever the question is "is this actually right, not just green?". It is the depth behind `SKILL.md`'s Testing discipline and rule 11.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## What tests are for here

The systems layer is the one part of a game that can be tested cheaply and completely, because it has no renderer, no scene and no user; that is the argument for `SKILL.md` rule 1's engine-free boundary (I). So the tests worth writing answer questions that inspection cannot:

| Question | Answered by |
|---|---|
| Does this migration work? | a golden-save fixture that can fail |
| Does this formula give the stated pacing? | a simulation harness printing the time per rung |
| Are these two numbers really decoupled? | a regression test that pins the old output |
| Does this generator always give a valid world? | invariant assertions over golden and random seeds |
| Are the tests even real? | mutation testing |

A test that asserts only "no exception was thrown" answers none of them (I).

## The decoupling regression test

The case behind the Testing discipline's first rule (Seen, July 2026): a combo cap rose from 5 to 10 for pacing, on the owner's condition that the tip formula give the same results for the same play, and a separate reference constant took over the measuring job the cap had done implicitly. The first draft changed only the formula's denominator, which would have let a sustained combo push the fraction past 1; a validation pass caught it before any code shipped. The proof of the final version is a test asserting byte-identical tip output for one tap sequence under a cap of 5 and of 10. Without it, "I split the responsibilities" is an assertion; with it, a fact.

## Call sites and guards

The call-site rule and its case are `SKILL.md`'s. What the records add: the same retune's second gate pass, asked for by the owner, found one more gap of the same class, a scene-side array the plan had not covered (Seen, July 2026). Search, then search the scene data too.

**A guard is code too, and its gaps are invisible from inside.** On the source project the guard was a documentation grep for narrative written into its instruction files, and it cost three pattern widenings and one hole in its file list before it covered what it was meant to (Seen, August 2026). So list the paraphrases before you write the pattern, and know that a guard's file list is as easy to leave short as its pattern: nothing about a clean run tells you what it did not read (I).

## Things that are invisible to tests, and need their own check

- **Content rosters held in scene or editor-serialized data.** Neither a review nor the test suite can see them; in one of the source project's four cases a new hire failed with "unknown employee" (Seen, July 2026). The mechanism, the count and the check are in `unity.md`, "Content rosters serialized in a scene are invisible to everything".
- **A changed source default never reaches an asset already serialized.** Every existing asset keeps its old value, including through bake and copy tools that keep hand-tuned fields on purpose: on the source project a generator's copy into an existing graph asset left those fields alone, and the live asset kept an old value after a retune and a re-bake (Seen). After changing a tunable's default, **read the live asset's value back off disk** before trusting a verification pass, and where a copy tool skips fields by design, say so at the copy site.
- **A long editor or build operation's own success log.** Verify the output artifact instead: search the saved file for a value only the new code writes, check its timestamp against a marker, or read the changed field back. The two named failures there: the tool ran the previously compiled assembly and reported success, or it ran correctly and skipped fields by design (Seen, the source project's glossary).

The procedure for tuning against measured output, and its named failure, blind threshold roulette, are in `procedural-generation.md`.

## Determinism, and how far you actually need it

Three different problems wear the same word:

1. **Reproducible across runs on one machine**: a seeded generator. This is all a test harness, a replay or a golden-seed check needs, and it is nearly free (I).
2. **Reproducible across builds of the same binary**: mostly free too, with care over the iteration order of hash-based collections, which can differ (I).
3. **Reproducible across machines, compilers and platforms**: hard. Floating-point results can be made identical across computers "provided you use an executable built with the same compiler, run on machines with the same architecture, and perform some platform-specific tricks" (D, Gaffer On Games, "Floating Point Determinism", read 2026-11-22). Games that run in deterministic lockstep have also used fixed-point integer math for their simulation (not checked at a source; stated here since September 2026).

Know which one you are promising. Promising the third and delivering the first is a desync that appears only in the field, and no test added later fixes it (I).

## Instruments beyond compile-and-pass

`SKILL.md`'s Testing discipline points here. **None of these is installed by default: each is a proposal with a real cost, to be raised before it is adopted, and never written up as existing practice** (I: the source project's earlier skill proposes the last two).

- **Golden-save fixtures.** No new tooling; adopt freely. In `save-and-persistence.md`.
- **Property-based testing**: FsCheck for .NET, fast-check for JavaScript and TypeScript, Hypothesis for Python (D, each project's own page, read 2026-11-22). Instead of examples, a test asserts an invariant, and the framework generates many inputs and shrinks a failure to a minimal case. It fits this layer's shape: serializers, state machines, numeric and domain invariants. Properties worth having (I):
  - `deserialize(serialize(state)) == state` over generated states, which catches drift between what is derived and what is stored, and gaps in serialization;
  - a generated save of the previous version always loads into a valid current state, the property form of the golden fixture;
  - money never negative; a derived total always equals the sum of its sources; a purchase strictly lowers the currency and strictly raises the owned count;
  - `derive(state)` is idempotent and independent of call order, so a derive can never read a half-constructed value (`economy-and-balance.md`, the anchor rule);
  - connectivity and feature-count invariants for generators.

  **Cost:** a package, a build reference, and generators for your state type: real, but bounded, and plausible at all only because the layer is engine-free.
- **Mutation testing**: Stryker, for JavaScript and TypeScript, C# (Stryker.NET) and Scala (Stryker4s) (D, stryker-mutator.io, read 2026-11-22). It mutates production code (`>` to `>=`, `+` to `-`, a dropped call) and checks whether any test fails; a surviving mutant is a test that executes code without asserting its effect, such as a test that only checks that nothing threw. **If adopted:** point it at the systems and economy module only, and treat a survivor on a balance constant or a state transition as a real gap rather than chasing a global score. **Cost:** a tool and a slow run: an occasional, deliberate pass, never a gate on every change (I).

## A structural review pass, before calling it done

Cheap, with no tooling (I):

- **Does a branch rely on a silent fallback to paper over an unclear invariant?** Make the boundary explicit instead.
- **Can related updates leave the state half-applied?** Push toward a more atomic structure: the atomic save and "commit before you announce" (`architecture-and-state.md`) are the same shape at two scales.
- **Is feature-specific logic leaking into a general module?** Is a one-off boolean or nullable "mode" complicating shared control flow?
- **The deletion test:** what would be lost if this module were deleted? A thin pass-through loses nothing.
- **Could a whole branch or layer be deleted rather than polished?**
- **Prefer a few findings you are sure of to a long list of nits**, and treat a file growing past about a thousand lines as a prompt to ask why (I: the source project's earlier skill states the rule).

## Filing is part of running it

An audit is not done until its findings are written where the next audit will read them, **including the negative results**: modules confirmed correct, with the reason and the revision. A clearance survives only if it is recorded, and an unfiled audit is one that gets paid for twice (I: the source project's earlier skill states the rule; `SKILL.md` rule 15 applies it to polls).
