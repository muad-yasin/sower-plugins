# sower-game-systems

Systems, simulation, state and persistence engineering for games and interactive apps - the layer
under the interface.

This is Sower Industries' working practice, extracted from one real project and generalized. Its
value is **named failure modes, each with its case**:

- the event raised before the state it described was written, so that an unlock failed every time;
- the income figures derived against another system's unbuilt ceiling, about 60 times off, which a
  gate pass caught before any code;
- the generator gate that rejected every candidate and split a route graph in half.

Install from this repository's marketplace, in a Claude Code session (this repository's root README says which version this form needs):

```
/plugin install sower-game-systems --marketplace muad-yasin/sower-plugins
```

## What's in it

One skill:

- **`game-systems`** - contract-first system design, loose coupling through events, state shape as a
  first-class decision, save/persistence integrity and migration, economy and balance math, seeded
  randomness and determinism, procedural-generation invariants, testing discipline for pure logic, a
  definition of done, and a list of mistakes to flag.

With nine reference files, loaded on demand:

| File | Read it when |
|---|---|
| `architecture-and-state.md` | designing a system, two systems start needing each other, or something works fresh but breaks on a loaded save |
| `save-and-persistence.md` | persistent state changes shape; any migration; choosing where saves live |
| `economy-and-balance.md` | any balance-tuning pass, new income source, or post-launch economy question |
| `testing-and-verification.md` | before adopting test tooling, or when the question is "is this right, not just green?" |
| `procedural-generation.md` | before writing or tuning any generator |
| `unity.md` | Unity work: the engine layer, from the source project's records and dated documentation |
| `web.md` | Browser work: storage and saves, and JavaScript or TypeScript game code; it rests on the source project's WebGL build and on dated documentation |
| `unreal.md` | Unreal work - **an unverified stub of open questions** |
| `evidence.md` | before a figure or an incident from `SKILL.md` is quoted, or when a rule may be retired: where each rule comes from, with its record or source and read date |

## What it assumes

- A project with a real separation between simulation/rules and presentation, or the intent to build
  one. The first hard rule is that boundary; most of the rest depends on it existing.
- A single-player or client-authoritative game as the default case. Where a server, shared economy or
  leaderboard changes the answer, the files say so explicitly - particularly around anti-cheat and
  save authority.
- That you will read the engine reference for the engine you are in. The core skill is deliberately
  engine-agnostic and therefore deliberately incomplete on specifics.

## What is still a stub

- **`unreal.md` is not guidance.** It is a labelled list of open questions. No Unreal project stands
  behind it, and nothing in it has been confirmed against one. Do not fill it in from Unity knowledge.
- **`web.md` is partly verified.** Behind it stand the source project's Unity WebGL build, a public
  playtest since October 2026 with its saves in IndexedDB, and documentation read and dated in the
  file; no JavaScript or TypeScript game codebase. Every inference is labelled as such in the
  sentence.
- **The instruments in `testing-and-verification.md` - property-based testing, mutation testing - are
  proposals with costs, not current practice.** They are written that way on purpose.

## Related plugins

`sower-game-frontend` (UX design, UI implementation, visual craft, 3D assets) · `sower-review` (scope
gating, bug audits, design critique) · `sower-writer` (drafting, sourcing, editing, and warm coverage of a real subject).

MIT licensed.
