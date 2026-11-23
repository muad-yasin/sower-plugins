---
name: game-systems
description: Builds and reviews the systems layer of a game or interactive app - rules, state, simulation, economy and balance math, saves and their migration, events, seeded randomness and procedural generation - and runs the checks before that work is called done. Use whenever a task touches game logic, simulation, economy, balance formulas, tunables, progression gates, offline or idle income, the save schema, migration, persistence, events, or any other code under the interface, including refactors and bug fixes, and even when the request never names a system. Not for views, layout, components, screens or input (the interface skills), or for scope decisions, plan gates and reviews of finished work (the planning skill and the review agents).
license: MIT
---

# Game Systems

You build the layer under the interface: rules, state, simulation, persistence, economy. The priorities, in order: **the correctness of the state model, then the integrity of the save, then convenience.** Never trade the first two for the third.

**A rule that only fixes one instance is not finished: push it until it makes the whole bug class impossible.** (Ousterhout's strategic over tactical programming; in practice, *make illegal states unrepresentable*. A state the save cannot hold needs no migration, a value derived on read cannot drift, and a reaction that can only be wired in the composition root cannot become a hidden reference between systems.)

**Evidence and grades.** **Seen** = it happened on the source project (a Unity mobile game), with the record named in `references/evidence.md`. **D** = documented in a named source, read on the date given there. **I** = inferred, with the reason in the sentence. Open `references/evidence.md` before you quote a figure or an incident from this file. This skill does not claim that following it improves a project's results.

**This skill owns:** the state model and the save, migration, events, simulation, economy and balance math, seeded randomness, procedural generation, and the tests of pure logic. **It hands off:** everything the player looks at or touches, to the interface skills; whether a feature should exist and what its plan must hold, to the planning skill and its scope gate; a read-only bug hunt, to the review plugin's audit agent.

**Before you write code that touches the engine, open the reference for the engine you are in:** `references/unity.md`, `references/web.md` or `references/unreal.md`. The Unreal file is not verified and says so.

## Contract first

Before you implement a system, write its **contract**: its public methods, the events it raises with their payload shapes, and the state it owns. A short markdown block or a doc-comment header is enough.

The interface layer codes against this contract. Writing it down is what stops the interface and the systems drifting apart, and stops guessed field names on both sides. Design it against the intended user flow, never in isolation: read the designer's flow for what the screen needs before you fix the contract.

Open `references/architecture-and-state.md` for the shape of a contract, the wiring in the composition root, and the ordering of startup.

## Hard rules

1. **Systems know nothing of the interface, and run in a test with no scene, no DOM and no renderer.** No view types, no scene lookups, no global "find the object by name" calls inside systems code. Use plain language objects wherever the engine's lifecycle does not force otherwise. The strongest form is a **boundary the build enforces**: a module or assembly that cannot reference the engine at all. Unity makes this one setting (`references/unity.md`); on the web it is a lint or import boundary (`references/web.md`).

2. **All tunables are data, not code.** Costs, thresholds, rates, spawn parameters, content definitions: if a designer might tweak it, it is a field on a data asset or a config file with a default, not a constant compiled into the logic. Prefer an **optional config with a built-in fallback**: the config reference is optional, and none means "use the defaults", never a crash. Introducing a config later then leaves every existing call site, tests included, working unchanged.
   - **Config is never save state.** Anything runtime or persistent lives in the state object and serializes separately.
   - **In some engines an edit to a config asset made while the game runs persists after you stop it,** so a "temporary" test tweak is silently permanent. `references/unity.md` says what Unity does. The Unreal reference only asks the question: before you rely on an answer there, change one value on a spare asset while the game runs, stop it, and note for the project whether the value stayed.
   - **A number that encodes an authored judgement is content, not a tunable:** the direction and the size of a scripted story beat's effect. Balance pressure is no reason to flip it. (Seen: the source project's world rules set a story's price direction by its moral read wherever the company did something, with no economic override.)

3. **No just-in-case fields.** Never add state, config fields or save entries without a concrete near-term consumer. Speculative fields bloat the save schema and become a permanent migration burden. A field justified only by a parked, unscheduled feature stays out until that feature has a scheduled consumer. Looking complete is not a requirement.

4. **Simulation is game-like unless realism is the product.** A weighted random walk with scripted events beats a market simulator. "More realistic" is a reason to pause and ask, not a reason to add: realism creep is how a systems layer grows a month of work nobody asked for.

5. **Economy formulas derive from the checkpoints the player meets, never the other way round.** Work backward from the moments the design promises ("by here, one good trade should beat a whole session of the starter job"), and **write the derivation in a comment that traces where the number came from. A balance constant with no such trace is presumed invented.**
   - **Derive against a self-contained anchor, never against a moving target owned by another system's unbuilt shape.** (Seen: a draft derived its income figures against an upgrade ladder's full-ceiling multiplier, which is reachable only after spending far more than the gate it was meant to protect. The formula came out about 60 times off, and a gate pass caught it before any code. The fix was an anchor of its own: breakeven hours per tier, and the time to the gate with no multiplier at all.)
   - **Never quote a threshold from memory.** Read the live value. Thresholds get retuned, lowered and retired. (Seen: an earlier version of this file quoted four, and all four went stale.) This file quotes none.

   If two tunables' difficulty could drift apart when only one changes, give them separate names and prove with a regression test that they are decoupled. Open `references/economy-and-balance.md` before you derive or retune a formula.

6. **One state object is the single source of truth, serializable from day one.** Any change to persistent state runs the save-integrity checklist below. For every new piece of state, decide what happens on a reset, on a prestige and on a corrupted save; never let it default silently.
   - **Derive a value on read instead of storing a copy,** whenever it is cheap to compute from state you already persist (an income multiplier from the owned upgrades; the in-game date from one stored epoch). A derived value cannot drift out of sync with its source; a stored copy can.
   - **State has three tiers: persisted, runtime only, and re-rolled on load as an accepted loss.** A re-rolled field says so in its comment, and the guarantee it served is rebuilt at startup. Open `references/architecture-and-state.md` before you add a field: the tiers in full.

7. **Events over references.** Systems raise events (money changed, stage unlocked, item crafted, trade resolved); they never call another system or the interface directly. When two systems must react to each other, the reaction is **composition-root glue**: a subscription in the one place that constructs everything, wiring one system's event to another's method, never a direct reference from inside either. The payoff is that every coupling is listed in one file you can read top to bottom. A static instance that any system can reach (a singleton) is a direct reference by another name: ask before adding one. A project that already wires its systems another way keeps its pattern: build your change in it and say so, and do not migrate the wiring unasked.

8. **Do not assume the order of listeners, and do not assume a listener exists when an event fires.** Most engines give no guarantee which of two components starts first. A consumer that needs another system's *current* state reads it once at its own first real use. And anything raised synchronously during startup has fired before any interface code could subscribe: pair such an event with an explicit one-shot "sync now" call right after subscribing, or a save already past the trigger waits for an event that never fires again. (Seen: three separate times on the source project by July 2026, a reveal on the HUD, a poll of offline income and a gap in a screen's reveal, and a fourth in August, in a tutorial.)
   **Make the assumption explicit at the line that enforces it:** an ordered call in the glue, a poll, an assertion, never something inferred from the order of subscriptions. "Subscribe earlier" and "add a null check" are the tempting non-fixes. If you cannot point at the line that guarantees the order, it is not done. Open `references/architecture-and-state.md` before you change how one system learns another's state: the incidents and both shapes.

9. **Raise an event only after committing the state it describes, and give an "external notify" entry point the same bookkeeping as the internal path.** A subscriber exists to react to the new state; an event raised before the write hands it a stale read on its one guaranteed chance. (Seen: an unlock failed every time because its event was raised before the call that recorded its fact; the check the event existed to trigger read false on its one guaranteed chance, and the player stayed locked out until some unrelated event ran it again.) When a fact can become true two ways, the natural path and a `NotifyX` method, **diff their side effects before you ship either.**

10. **The player can never be hard-locked.** Some income, some action, some route forward is always available. Check that every new failure state (bankruptcy, a losing streak, a lost item) leaves a way back.

11. **Randomness is injectable and seedable, never a bare call to a global generator.** Accept a seed or a generator instance, or keep every random call behind one small internal method. That is what makes the *shape* of a generator's or a walk's output testable even though the output is meant to look random. **Determinism is a correctness feature, not only a testing convenience:** offline-income math and any procedural bake can be checked against a closed form or a golden seed only when the randomness is seeded; unseeded is unverifiable by construction. Determinism across *machines* is a harder problem than determinism across runs and needs another tool: open `references/testing-and-verification.md` before you promise it.

12. **A stricter entry point beside a permissive method is a thin wrapper that checks the new policy and then delegates;** never change the existing method's behaviour. The wrapper inherits the original's guards and leaves its other callers alone. What keeps this from wrapper sprawl: the wrapper *adds a policy*, a real seam. A pass-through that only renames or forwards earns nothing: delete it. The same test holds for abstraction in general: one implementation is a hypothetical seam, two are a real one, so no interface lands before its second.

13. **A real asymmetry in a formula, once found, need not be fixed by the change that found it.** Record it with a name, rebalance it later with knobs that already exist, and never bake a special case into the change that surfaced it.

14. **Every hard eligibility gate inside procedural generation is paired with a loud check on the output invariant it could break.** Gates fail *silently, by producing nothing*, not by erroring. (Seen: a tightened curvature gate rejected every candidate site, placed no bridges and split a generated route graph in half, caught only by reading a bake log by hand.) Open `references/procedural-generation.md` before you write or tune a generator.

15. **Throttle cross-system polls out of the per-frame loop, and when you find one, sweep every per-frame loop for the same shape in the same pass.** Progression gates feel the same checked once a second. Record the sweep's negative results too (loops confirmed fine, with the reason): a clearance nobody wrote down gets paid for twice. (Seen: after the owner asked what one such poll cost, it was throttled to about once a second, and the sweep the owner asked for found two more.)

16. **Every swallowed exception, every error path that returns null or a default, and every silent fallback is a presumptive defect until a comment justifies the silence.** Code that keeps the appearance of working while it quietly does nothing passes a casual review. The contrast is the rule: a gate that produces nothing instead of an error is a defect, while a save loader that returns null on a corrupt file is *justified* silence, documented, with a backup behind it. Where silence is right, say why at the site; where it is not, fail loudly or do not catch.

## Save integrity: a low-freedom checklist

Run it exactly whenever persistent state changes shape. A broken migration cannot be repaired once the update that carries it has shipped.

- **Bump the schema version and write a migration note.** Migration goes stepwise forward, from version N to N+1, each step giving new fields sensible defaults; never one big converter that spans versions.
- **The atomic write is load-bearing, not an option:** whatever interrupts a write, the loader must still find one whole save, the new one or the one before. On a file system, write to a temporary file in the same directory as the target, flush it to disk, and rename it over the target. Where the runtime gives you a handle on the directory, sync the directory too: on Linux a sync of the file alone does not put its directory entry on disk (the `fsync` manual page, D). Where the runtime gives you no such handle, say so in a comment at the write site instead of implying a guarantee you do not have. A browser has no rename: `references/web.md` has its form, one transaction or one value under one key. Keep a backup sibling the loader falls back to, and return null instead of throwing on a missing or corrupt file. The backup has a consequence people miss: "delete the save" means *every file that matches the save's name*. A stale backup that silently restores the previous session looks like a plausible save, not like an error.
- **Golden saves show that a new build still loads the saves older builds wrote; a careful reading of the migration does not.** Freeze one real save per meaningful game state at the release build's schema version, and load each in a test. Whether a migration works is answered by a fixture that can fail, never by a read-through.
- **Decide anti-cheat once, deliberately:** none for an offline single-player game, where checksums and obfuscation only complicate recovery; server authority for anything with a shared economy, a leaderboard or a server. Never half of each.

Open `references/save-and-persistence.md` for the versioned envelope, the mechanics of migration, recovery from corruption, the anti-cheat decision in full, and what changes once a network is involved.

## Testing discipline

- **When you decouple two numbers or behaviours that were coupled, the regression test that proves the old one unaffected is the proof of the decoupling.** The shape of the code is not.
- **Find every real call site before you change a shared method's signature or contract,** with the compiler or a find-references search, never from memory. (Seen: one gate pass on a retune, searching instead of assuming, found two things a read-through had missed: a debug menu action that was a third real caller of a method about to be retired, and an achievement hard-coded to a tier id the new design had to keep.)
- **A mistake that has shipped twice earns a mechanical guard, not a reminder:** a source-scanning test that enforces the pattern. When you write that guard, **list the paraphrases before you write the pattern:** a guard with a synonym hole gives the confidence without the coverage.
- **A content roster held in scene or editor data is invisible to both code review and the test suite.** A new content asset needs its own explicit check that it reached the list, every time. (Seen: on the source project the class recurred four times, each found live or by a direct check of the scene, never by a test or a review.)
- **Before you propose an instrument beyond compiling and passing** (property-based tests, mutation tests, golden-save fixtures), open `references/testing-and-verification.md` for its cost. None is current practice unless your project installed it.

## Definition of done, per systems task

- The contract is written: methods, events with payloads, owned state.
- The logic runs with no scene, no renderer and no interface loaded.
- Tunables are data fields with defaults; no speculative fields.
- Events are raised for anything the interface might display.
- The save-integrity checklist ran, if persistent state changed shape.
- Every real call site of a changed method or contract was found and updated, by search.
- A regression test was added, if the change decouples two numbers that were linked.
- A new content asset was checked live in the roster that loads it, and a changed tunable's value was read back off disk, not off the source default.
- A short note lists anything a person must do by hand in an editor.
- Non-obvious design choices are explained briefly: teach the pattern, do not just apply it.

## Mistakes to flag

- Implementation started before the contract exists; realism creep in the simulation.
- Balance numbers invented instead of derived from the player's checkpoints, derived against another system's unbuilt ceiling, or derived from a threshold quoted from memory instead of read live. A constant with no comment tracing its origin counts as invented.
- Persistent state added without the save-integrity checklist, or duplicating something already derivable from persisted state.
- Save state smuggled into a config asset, or a config asset tweaked at run time as if the change were transient.
- A failure state that could strand the player with no way forward.
- Two systems calling each other directly instead of through the composition root.
- An event raised before the state it describes was committed; an external-notify path whose side effects differ from the internal one.
- A startup event with no one-shot sync call for late subscribers.
- An ordering assumption with no line you can point at that enforces it.
- A swallowed exception, a silent `return null` or a default-on-error fallback with no comment justifying the silence.
- A pass-through wrapper, or an interface with one implementation, added before the second exists.
- A bare global random call in systems logic, with no seed or injection point.
- A proposed save checksum, obfuscation or anti-cheat measure on a single-player offline game: deliberately rejected, see the checklist.
- A generator gate with no assertion on the output invariant it could silently break.
