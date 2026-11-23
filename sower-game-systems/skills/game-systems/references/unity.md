# Unity: the engine layer behind the records

*Open this file before you write systems code in a Unity project: the engine-free assembly, ScriptableObjects as content, rosters held in a scene, editor tools that run the old assembly, domain reload, `JsonUtility`, the clash of two namespaces, and per-frame cost. It is written from the source project's records, made on Unity 6000.5; a line that rests on Unity's manual names the version and the read date.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## The engine-free assembly, enforced by the compiler

`SKILL.md` rule 1 says systems run with no scene. In Unity the build can enforce it: put the systems layer in its own assembly definition and turn on **No Engine References** (`"noEngineReferences": true`). "When enabled, Unity does not add references to UnityEditor or UnityEngine assemblies when it compiles the assembly" (D, Unity 6000.6 manual, "Assembly Definition Inspector window reference", read 2026-11-22), so every breach of rule 1 becomes a compile error instead of a review comment (I). It is one line of JSON.

Consequences the source project met (Seen):

- **Whatever touches the engine needs its own assembly.** The save system needs `Application` and `JsonUtility`, so it lives in a separate assembly with engine references beside the pure one, not inside it. Do not weaken the pure assembly for one class.
- **Write the boundary down, and check the note.** A rule of the form "assemblies A and B are engine-free, C deliberately is not" gets misremembered, even by the file that states it: the project's rule file named the wrong assembly until a code audit of 22 July 2026 caught it.
- **`is null`, never `==`, inside the engine-free assemblies.** Unity overloads `==` on `UnityEngine.Object` so that a destroyed object compares equal to null, and that overload needs an engine module the pure assembly does not reference: on the source project such a comparison would not compile there, and the fix was `is null`. The rule inverts in engine code: on anything derived from `UnityEngine.Object`, `is null`, `?.` and `??` bypass Unity's liveness check, and only `== null` sees a destroyed object (I: the source project's earlier audit agent states the rule). Check the operand's type before you change one into the other.

## ScriptableObjects, and the two Play Mode traps

`ScriptableObject` assets are Unity's form of `SKILL.md` rule 2: definitions, price parameters, stage thresholds, upgrade costs, dialogue, all assets with default values edited in the inspector, never constants in code. The optional config with a fallback, concretely (I):

```csharp
public void Initialize(PlayerState state, BalanceConfig config = null)
{
    _config = config;   // null is legal and means "use the built-in defaults"
}

private float StakeFraction => _config is null ? DefaultStakeFraction : _config.stakeFraction;
```

Every existing call site, tests included, keeps working when the config arrives later; a required reference gives a null reference on a scene somebody forgot to wire.

The two traps:

1. **A ScriptableObject is config, never save state.** It serializes for free, which is the temptation, and it is wrong: assets are part of the build, shared by every player, and not reset by a new game (I). Persistent state lives in your own serializable state object.
2. **Play Mode treats assets and scenes in opposite ways.** An asset field changed during Play Mode keeps its new value after Play stops (I: the source project's earlier skill states it; no incident of this direction was found), while a scene edit made during Play Mode is discarded, which cost the source project work four separate times by its count of 1 August 2026 (Seen). So a "temporary" tweak to an asset is silently permanent and a "permanent" tweak to a scene object silently lost. The habit that covers both: make final values as deliberate Edit Mode edits, save, and verify again from a fresh Play session.

## Content rosters serialized in a scene are invisible to everything

A `MonoBehaviour` composition root that holds `public ItemDefinition[] items` serializes that list **into the scene file**, where neither a code review nor the EditMode tests can see it. An asset that exists on disk, compiles and passes every test can still be missing from the game. On the source project this class recurred four times by July 2026, by its own count, each time found live in Play Mode or by a direct check of the scene, never by a test or a review (Seen).

The check is explicit, every time: after adding content, search the saved scene file on disk for the new asset's GUID. Where an editor tool fills the list by scanning a folder, **still search the scene**, and never trust the tool's own success log (Seen: the project's rule after it built such a tool).

## Editor tools silently run the old assembly

When the project has compile errors, or a recompile has not finished, a Unity editor-menu tool **still runs**, on the last assembly that compiled: it executes old code and reports normal success. The source project's glossary counts four ways this struck (Seen, July and August 2026): rebuilt prefabs that came out stale, twice in one milestone; a recurrence that passed both an "is not playing" and an "empty console" check and was caught only by reading the rebuilt asset's YAML; and stale map bakes while a shared editor carried another window's unfinished compile errors.

**Before any editor-menu tool runs, force and confirm a clean, fresh compile.** Its strongest form is a sentinel: read, from the live assembly, a value only the new code produces, before rebuilding anything (Seen: the fix after three passes had produced stale prefabs). **Afterwards, verify the output on disk**: search the artifact for a value only the new code writes, or check its timestamp. Never trust the log line.

## Domain reload, and why runtime state vanishes

- **A script recompile during an active Play session reloads the C# domain** (Seen, found and fixed in July 2026). It wipes every runtime field that is not serialized without re-running the lifecycle callbacks that filled them, so systems come back half-initialized. The fix that held is at editor level: an editor preference that queues recompiles until Play Mode ends, enforced by an editor script, and a composition root that detects the reload and disables itself instead of throwing null references (Seen). Do not edit scripts during Play and expect live runtime state to survive.
- **With domain reload off, statics persist.** In Unity 6000.6, "the Editor doesn't perform domain reload on entering Play mode by default", and with it off, static variables keep their values and static events keep their subscribers between Play sessions; reset them by hand with `[OnEnteringPlayMode]` or `[OnExitingPlayMode]`, or let `[AutoStaticsCleanup]` reset a static field when Play mode starts (D, Unity 6000.6 manual, "Enter Play mode without domain reload", read 2026-11-22). In an earlier research round of ours (2026-10-05), the 6000.3 manual said the domain reloads by default and 6000.6's notes applied the new default to new projects, so read your own project's setting. Static mutable state is what silently survives here, which is one more reason for rule 7's caution about singletons (I).

## Saving: JsonUtility and the round trip

`JsonUtility` is enough for a single-player save and needs no package (Seen: the source project stayed on it). Its edges in Unity 6000.6 (D, the manual's "JSON serialization" and "Serialization rules", read 2026-11-22):

- **Fields only, never properties**: "Unity serializes fields only, not properties". A state model built from auto-properties saves nothing.
- **A field missing from the file keeps its constructed value**, which makes "add a field, old saves still load" free; it is the only migration case that is (I). A renamed field, a change of units or a change of shape needs an explicit step.
- **A primitive or an array cannot be passed at the top level**: wrap it in a class or a struct.
- **Dictionaries depend on the engine version:** the 6000.6 rules list `Dictionary<TKey, TValue>` with `[SerializeField]` as supported; an older engine may drop one, so check yours.
- If you outgrow it, a fuller JSON package is the usual step up, at the cost of a dependency (I).

Write the save to `Application.persistentDataPath`, outside WebGL (on WebGL, `web.md`), and autosave on pause, on quit and on a timer (I: the source project's earlier skill states the rule). **`OnApplicationQuit` fires when Play Mode stops in the editor**, so a save deleted while a stale session is loaded comes back the moment Play stops: delete it with Play fully stopped, or with an in-play action that deletes and reloads the scene (Seen). And the backup sibling means deleting **every file that matches the save's name** (`save-and-persistence.md`).

## `System` against `UnityEngine`: the ambiguous names

A file with both `using System;` and `using UnityEngine;` has ambiguous `Random`, `Object` and several others. The compiler reports it, but the fix people reach for by reflex, deleting `using System`, binds `Random` to `UnityEngine.Random`: a static global with no injectable instance, so a systems file that binds to it has broken `SKILL.md` rule 11's seedability without an error (I: the source project's earlier skill states the rule). **Fully qualify `System.Random` and `UnityEngine.Random` in any file that imports both**, and prefer `System.Random` in the engine-free assembly, where `UnityEngine.Random` is not available at all.

## Per-frame cost

"Update is called every frame, if the MonoBehaviour is enabled" (D, Unity 6000.6 scripting reference, `MonoBehaviour.Update`, read 2026-11-22), and the cross-system gate polls that collect there feel the same checked about once a second with an accumulator (I). The source project's case behind `SKILL.md` rule 15 (Seen, July 2026): a new per-frame poll computed net worth up to seven times in a single frame; after the owner asked what it cost, it was throttled to about once a second, and the wider sweep the owner asked for found two more, an identical unthrottled call in another trigger and a scan over every stock and every position each frame, fixed with a precomputed set.

`Update` does not run on a component under an inactive GameObject: the reference's own example starts `Update` once the object is activated (D, the same page). That can be a useful structural guarantee, "this only runs while that panel is open" becoming a fact about the hierarchy instead of a flag someone must remember to clear (I).
