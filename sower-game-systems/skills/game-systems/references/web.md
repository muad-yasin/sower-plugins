# Web, JavaScript and TypeScript: partly verified

*Open this file before you write systems code for the web. The source project's browser build was a Unity WebGL build, online as a public playtest since 6 October 2026, with its saves kept in IndexedDB (Seen); no JavaScript or TypeScript game codebase stands behind this file. The architecture questions are the ones the Unity layer answers; lines from documentation give their source and read date, and inferences say so.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## The engine-free boundary, in a JS or TS codebase

Unity gives you a compile-time wall (`unity.md`); the web has none by default, so you build one (I):

- Put the systems layer in its own package or workspace folder **with no dependency on the framework** in its `package.json`: no React, no DOM types, nothing that renders. A boundary rule fails the build when someone imports upward: dependency-cruiser exists to "Validate and visualize dependencies. Your rules." (D, its repository's description, read 2026-11-22), and ESLint's `no-restricted-imports` is there to "Disallow specified modules when loaded by import" (D, ESLint's rule page, read 2026-11-22).
- Keep `dom` out of the systems package's `tsconfig` `lib` array. TypeScript's default `lib` brings "type definitions for things found in browser environments (like document)" (D, TypeScript's reference for `lib`, read 2026-11-22); without it, `window`, `document` and `localStorage` are compile errors inside the package, close to the Unity guarantee (I).
- The test for whether you got it right is the same: **can the systems package run under plain Node, with no jsdom and no test renderer?** If yes, the boundary is real (I).

## Where the state lives

`SKILL.md` rule 6's single source of truth survives intact, but one serializable state object collides with the framework's own state management, and that collision is the main design decision (I):

- **The systems layer owns the authoritative state object.** The UI framework's store holds a *projection* of it, or subscribes to it, and never becomes the second place a rule lives. A reducer that decides whether the player can afford something is rule 1 broken in a fashionable costume.
- **Events over references still holds**, and is easier here: an `EventTarget`, a tiny emitter or an observable, wired in one composition-root module. The ordering trap changes shape without going away: "If your Effect wasn't caused by an interaction (like a click), React will generally let the browser paint the updated screen first before running your Effect" (D, React's reference for `useEffect`, read 2026-11-22), so a subscription made in an Effect comes after the first paint, and an event raised during bootstrap has already fired. That is `architecture-and-state.md`'s Shape 2, with the same fix: an explicit call that evaluates the current state on mount, beside the subscription (I).
- **Immutability is the local idiom, and it costs something in a simulation loop**: structural sharing in a tick that runs every frame allocates. A mutable internal state with an immutable projection published on change is the shape that reconciles the two; measure before assuming either way (I).

## Persistence: the constraint with no desktop equivalent

This is the largest real difference from `save-and-persistence.md`. **Browser storage can be evicted.** Data is stored "best-effort" by default and evicted, when the browser needs the space, without interrupting the user; an origin can ask for persistent storage with `navigator.storage.persist()`, and data stored that way is deleted only if the user chooses to (D, MDN, "Storage quotas and eviction criteria", read 2026-11-22). The same page gives Web Storage at most 10 MiB on all browsers, "up to 5 MiB of local storage, and 5 MiB of session storage per origin", and Firefox's best-effort limit for other storage as the smaller of 10% of the disk and a 10 GiB group limit (D, the same read). Since Safari 17, WebKit gives a browser app's origin up to 60% of the disk and another app's up to 15%, and it evicts data over its overall quota, under storage pressure, or after the user has not interacted with the site for some time (D, WebKit blog, "Updates to Storage Policy", 10 August 2023, read 2026-11-22). Limits move: read the pages again before you rely on a figure.

What follows for a game save:

- **Ask for persistence explicitly** if the save matters, and handle the "no": it is a permission, and it can be refused (I).
- **A local-only browser save is not durable storage.** Design for it disappearing: cheap re-onboarding, an export and import of the save, or an account (I). On the source project the owner decided in October 2026 not to build an export or import code, and accepted that a tab closed in the instant of a save can lose that one save, with the 30-second autosave bounding the loss (Seen).
- **The temporary-file-then-rename pattern has no direct equivalent.** In IndexedDB "the default behavior of an error is to abort the transaction in which it occurred" (D, MDN, "Using IndexedDB", read 2026-11-22), so one transaction is the closest thing, and enough for a save held in one record (I). `localStorage` offers nothing of the kind, so a save spread over several keys can be left torn by a crash between writes: write the whole save as one value under one key, or in one IndexedDB transaction (I).
- **Schema versioning is unchanged and just as necessary**: a version at the root, migrations step by step, golden fixtures. IndexedDB adds its own database version, whose increase fires `onupgradeneeded`, where the store's schema is created (D, the same MDN page). That migrates the shape of the store, not your save payload, so you usually need both (I).
- **In a Unity WebGL build** the engine's persistent path ends in a hash of the URL of the directory the page is served from; the file name and the query string do not change it (D, Unity scripting reference, `Application.persistentDataPath`, read 2026-11-23). So the path follows that directory and not the build: saves survive an upload into the same directory, and are left behind when the directory changes. The source project writes to a fixed folder that Unity mirrors to IndexedDB (Seen, October 2026).

## Client against server: the question that decides everything else

Ask it before writing any state code, because retrofitting it is a rewrite (I):

- **Single-player, offline, no leaderboard:** client-authoritative is fine, saves are trivially editable, and `save-and-persistence.md`'s anti-cheat decision applies. A web build is *easier* to inspect and edit than a native one, since its source is right there; that changes nothing when there is nothing to protect.
- **Anything shared, such as leaderboards, multiplayer, purchases or a shared economy:** the server owns the state, and the client is a view that proposes actions. No number the client supplies is trusted. A framework-free systems layer lets the *same simulation code* run on the server as the authority and on the client as prediction, which is the strongest practical argument for the boundary on the web (I: no server-authoritative simulation stands behind this file). What saving over a network adds is in `save-and-persistence.md`, "Saves over a network".

## Determinism

- **The platform's generator cannot be seeded**: for `Math.random()` "The implementation selects the initial seed to the random number generation algorithm; it cannot be chosen or reset by the user" (D, MDN, `Math.random()`, read 2026-11-22). So `SKILL.md` rule 11 is not optional here: inject a small seeded generator (a 32-bit xorshift or a PCG variant is a dozen lines with no dependency), and keep `Math.random()` out of the systems package, where a lint rule can enforce it (I).
- **`Date.now()` inside simulation logic** is the same class of mistake: it makes the simulation unreproducible and trusts a clock the player controls. Pass elapsed time in from the composition root (I).
- **Floating-point determinism across machines** is as hard here as anywhere, and you cannot set the engine's compiler flags at all; if you need lockstep, use integer or fixed-point math (I). See the three levels of determinism in `testing-and-verification.md`.
- **Iteration order:** a `Map` "remembers the original insertion order of the keys" (D, MDN, `Map`, read 2026-11-22); plain objects order integer-like keys differently (not checked at a source; stated here since September 2026). Sort explicitly wherever iteration order feeds a result you care about (I).

## Testing

A framework-free systems package tests with a plain test runner under Node, with no jsdom and no test renderer (I). Everything in `testing-and-verification.md` applies unchanged: golden fixtures are JSON files, property-based testing is fast-check, mutation testing is Stryker, and the simulation harness is a script.

## Open questions nobody here has answered

- Whether an immutable state model costs enough in a per-frame tick to matter at this genre's scale.
- Whether one simulation package running as both server authority and client prediction is as clean in practice as on paper.
- What a real migration of an IndexedDB save across several versions costs to build and test.
