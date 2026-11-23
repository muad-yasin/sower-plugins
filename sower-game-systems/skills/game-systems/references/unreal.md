# Unreal: not yet verified

*Open this file before you write systems code in an Unreal project. Nothing in it has been confirmed against a real Unreal project: it lists the questions the Unity layer answers, so that they are answered here the first time one is built, and so that nobody mistakes an inference for practice meanwhile.*

**Do not fill any of these in from Unity knowledge or from documentation alone.** An answer written without having built it reads exactly like one written with, and someone who cannot tell the difference will trust it later (I). When a question is answered, replace it with the answer, say what verified it, and remove this warning for that section only.

The engine-agnostic rules of `SKILL.md` still apply: contract first, events over references, derive over store, save integrity, seeded randomness, a gate paired with an invariant. What is unknown is how each is *expressed* in Unreal.

## Open questions

**The engine-free boundary (rule 1)**
- Is there an equivalent of a compile-time wall between simulation code and engine types (a module in the build system that can be declared to have no engine dependency), or is the boundary necessarily conventional here?
- Can simulation logic be written against plain types with no `UObject` base, and if so, what does it cost in exchange (no reflection, no serialization, no Blueprint exposure)?
- How much of the systems layer can run in a commandlet or a standalone test harness with no world, no renderer, no level loaded?

**Data-driven tunables (rule 2)**
- What is the right home for balance data: data assets, data tables, developer settings, config files, and which of them are editable by a designer without a recompile?
- Which of those persist an edit made while the game is running, and which discard it? (In Unity the two behave oppositely; the source project recorded lost scene edits, and no incident of the asset direction: `unity.md`.)
- Is there an equivalent of the optional-config-with-fallback shape, where a missing asset means "use defaults" rather than a crash?

**Events and coupling (rules 7, 8, 9)**
- Which of the several delegate and messaging mechanisms is the right default for cross-system events, and which of them have ordering guarantees?
- Where is the composition root (the one place that constructs systems and wires them together) in an Unreal project's actual lifecycle? What is the equivalent of "this event already fired before anything could subscribe"?
- What is the initialization order between the relevant lifecycle entry points, and which parts of it are actually guaranteed rather than merely observed?
- Is Blueprint-level wiring an acceptable composition root, or does it reintroduce the invisible-roster problem (`unity.md`, "Content rosters serialized in a scene are invisible to everything")?

**State and saving (rule 6, save-integrity checklist)**
- What does the built-in save system actually guarantee: is the write atomic, is there a backup, what happens on a corrupt file?
- How is schema versioning normally expressed, and does the serializer leave missing fields at their defaults the way a stepwise migration strategy assumes?
- Where does save data live per platform, and what does console certification require that a desktop/mobile project does not?
- What is the equivalent of "content roster serialized into a scene file, invisible to code review and tests"? Almost certainly something is; find out what before it costs a shipped bug.

**Determinism and randomness (rule 11)**
- What is the standard seedable RNG, and is there a global one that logic will bind to by accident?
- What determinism guarantees exist across builds and platforms, particularly if any physics or engine-side simulation feeds gameplay results?

**Testing (`testing-and-verification.md`)**
- What is the automation-test story for logic with no world loaded, and how fast is it in practice?
- Can golden-save fixtures be loaded in a test the way an editor-mode test loads them elsewhere?
- Do the editor's build/bake tools have the "silently ran the previously compiled code and reported success" failure mode? If they do, what is the pre-run check that catches it?

**Per-frame cost (rule 15)**
- What is the idiomatic way to throttle a cross-system poll off the per-tick path, and does the engine's own timer mechanism make the accumulator pattern unnecessary?
