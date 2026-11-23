# Save integrity, schema migration and persistence

*Open this file before any change to the shape of persistent state, any migration, any offline or elapsed-time work, and before you choose where save data lives on a new platform. It is the depth behind `SKILL.md` rule 6 and its save-integrity checklist.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

A broken migration cannot be repaired once the update that carries it has shipped. Everything here is cheap compared with that (I).

## The versioned envelope

Practitioner guides quoted in a research report of ours describe the same checklist (not checked at a source; stated here since September 2026):

1. **A schema version at the root of the file.** Never parse a save without reading it first.
2. **Migrations that step forward**, from version N to N+1, one step per version, each giving new fields sensible defaults. Never one converter that branches across every historical version: by version four it cannot be reviewed, and it is where migration bugs live (I).
3. **An atomic write** (below).
4. **A backup sibling** that the loader falls back to.
5. **Tests**: golden files, round trips, migrations and corrupt files.

The failure to plan for is the boring one: someone adds a field and old saves stop loading (I). A serializer that keeps the constructed value of a field the file does not mention covers the trivial case for free, as Unity's does (D, Unity 6000.6 manual, "JSON serialization", read 2026-11-22). Whatever it cannot express, a renamed field, a change of units, a list that became a dictionary, gets an explicit migration step (I).

## Atomic write, and the durability part people skip

The pattern: write a temporary file, then rename it over the target. On Linux the rename is atomic: "If newpath already exists, it will be atomically replaced" (D, the `rename(2)` manual page, man7.org, read 2026-11-22). What it does not give is durability: a sync of a file does not necessarily put the entry in its directory on disk, and an explicit sync of the directory is needed for that (D, the `fsync(2)` manual page, man7.org, read 2026-11-22). An issue on npm's write-file-atomic library puts it in its title: "Rename atomicity is not enough" (D, npm/write-file-atomic, issue 64, read 2026-11-22). The full sequence:

1. create the temporary file **in the same directory** as the target, so both sit on one filesystem (I);
2. write it;
3. sync the temporary file;
4. rename it over the target;
5. sync the containing **directory**.

Skip step 5 and the application believes the rename is durable while a crash can bring the old file back (I, from the manual pages above). How much of this you can express depends on the runtime: some managed file APIs give no handle on a directory at all. Where you cannot do it, **say so in a comment at the write site** instead of implying a guarantee you do not have.

**On Windows the guarantee does not carry over.** The C runtime's `rename` refuses a target that already exists: "The new name must not be the name of an existing file or directory" (D, Microsoft Learn, "rename, _wrename", read 2026-11-22). Replacing a file there takes `MoveFileEx` with `MOVEFILE_REPLACE_EXISTING`, or `ReplaceFile`, which can also keep a backup copy of the original (D, Microsoft Learn, read 2026-11-22). None of the three pages promises atomicity, so never port a POSIX writer's guarantee to Windows by assumption; a refactor to a `File.Move`-shaped call is where this bites (I).

**The backup sibling's trap** (the checklist's rule on deleting every file that matches the save's name): on the source project four "fresh save" verification runs in one session were not fresh, because the loader restored the backup (Seen). The reliable tell is a version stamp written once and never rewritten that sits below the current schema version (Seen).

## Golden saves

**Golden saves show that a new build still loads the saves older builds wrote; a careful reading of the migration does not** (I: the source project's earlier skill states the rule). The usual name for that is backward compatibility, and the fixtures show it only for the states they hold. Whether an old build can open a save from a newer one is a different question, which they do not touch; a project meets it only if it lets players return to an earlier version (I). This is the part of save work a model cannot certify by inspection: it can write and run the check, not assert the answer (I).

- Freeze one real save per meaningful state (fresh, mid-progression, after a major purchase, endgame), captured at the release build's actual schema version.
- Commit them as test fixtures, one test per fixture: load it and assert the key fields survived with the right values.
- When the schema version moves, **add** a fixture at the new version. Never regenerate an old one: a regenerated fixture tests nothing, because the code that reads it also wrote it.

A fixture's value is that code which no longer exists produced it.

## Corrupt-save recovery

The loader returns null, or an explicit `LoadResult.Corrupt`, instead of throwing; falls back to the backup; and if that fails too, starts a new game. That is `SKILL.md` rule 16's justified silence: document it at the site, so that a later audit does not "fix" it into a throw (I). The caller has to be able to tell three outcomes apart, loaded, recovered from the backup, and a fresh start, so that a recovery can be shown to the player rather than passed off as a normal load (I).

## Anti-cheat: decide once, deliberately

The decision `SKILL.md`'s checklist names (I: the source project's earlier skill states it for an offline single-player game):

- **Offline, single-player, no shared economy:** local saves are trivially editable, and that is accepted. Checksums and obfuscation protect nothing here, with no other player and no revenue tied to the numbers, while they complicate the recovery path above. A player who edits their own save has bought the game and plays it their way.
- **A server, a leaderboard, a shared economy or real-money trade:** the opposite. The authoritative state lives on the server, the client is a view, and no number the client supplies is trusted. Hardening a save against duplication and real-money trading belongs to a shared economy (not checked at a source; stated here since September 2026).

The failure is doing half of each: obfuscation on a single-player save, or a client-authoritative number in a multiplayer economy. Pick the side that matches the product, and write down which.

## Saves over a network

A save over a network has failure modes a local save does not: a save that times out, a save that succeeds after the client gave up, two devices writing the same slot. The minimum is a monotonic version or timestamp per save, a last-write-wins rule that is written down, and a local queue, so that play never blocks on the network (I). With a server, the authoritative state lives there and the client proposes actions; an engine-free systems layer is what lets the same simulation run on the server as the authority and on the client as prediction (I; the web case is in `web.md`).

## Offline and elapsed-time earnings

Long elapsed times, capped windows and exponential income meet in one function here, so it earns its own invariant suite (I):

- monotonic in elapsed time;
- never negative;
- never above the cap;
- equal to a closed-form expectation for the simple case of one source;
- exercised over the *whole numeric range the game reaches*: lost float precision and integer overflow fail silently, not with a crash.

Trust the device clock as little as you can. Moving the system clock forward is the exploit to expect, and clamping elapsed time to the cap, which pacing asks for anyway, closes most of it for free (I). On the source project clock manipulation was treated as unfixable without server authority, and its in-game day stopped reading the device clock on 16 August 2026 (Seen). Server time is the only real answer, and it costs a network dependency at cold start (I).

## Where the save lives, by platform

- **Desktop and mobile:** a per-user application data directory, never next to the binary (I). Android's Auto Backup includes files in most of the directories the system assigns to the app, within a 25 MB backup quota, and excludes the cache directories (D, Android Developers, "Back up user data with Auto Backup", read 2026-11-22). When iCloud Backup is enabled, it includes an app's data and excludes `/tmp` and `/Library/Caches`, which the system purges (D, Apple Developer, "Optimizing your app's data for iCloud Backup", read 2026-11-22). Keep a save out of the cache directories.
- **In Unity, outside WebGL**, that directory is `Application.persistentDataPath` (`unity.md`). On WebGL that path ends in a hash of the URL of the directory the page is served from (D, Unity scripting reference, `Application.persistentDataPath`, read 2026-11-23), so a build served from a new directory no longer finds its old saves. The source project writes to a fixed folder that Unity mirrors to IndexedDB instead (Seen, October 2026; `web.md`).
- **Browser:** `web.md`. The constraint differs in kind, because browser storage can be *evicted*.
- **Console:** platform-mandated APIs and certification rules; unverified here.

## Before release 1.0

On the source project, saves made before release 1.0 do not matter, by the developer's standing call: migrations count from the store's 1.0 onward (Seen: its earlier skill and its notes on the PC build). Before that point saves are test data; do not spend real effort on compatibility with a build nobody outside the project ran (I). A public playtest is the moment to decide whether its players' saves count: that project's browser build went out as one in October 2026 (Seen).
