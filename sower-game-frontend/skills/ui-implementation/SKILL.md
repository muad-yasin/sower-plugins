---
name: ui-implementation
description: Implements and reviews a game's or app's interface code so that it is correct - screen controllers, layout across real screen shapes, data binding to game state, touch and pointer input, navigation and back handling, safe areas, builder scripts, and importing a design mockup by its literal values. Use when writing, changing or reviewing anything that draws an interface or reacts to a player's input, including wiring one button or showing one number, and when reviewing UI code for missing states. Takes ux-design's flow, wireframe and states list as its input. Not for game logic, economy math or saves (the systems skill), whether the result looks right (visual-craft), or building geometry and motion (3d-assets).
license: MIT
---

# UI Implementation

You implement the interface: whatever draws on the screen or reacts to a player's touch. Correct, good-looking and verified are three different claims; keep them apart in every summary you write.

**Evidence and grades.** **Seen** = it happened on the source project (a Unity mobile game), with the record named in `references/evidence.md`. **D** = documented in a named source, read on the date given there. **I** = inferred, with the reason in the sentence. Open `references/evidence.md` before you quote a figure or an incident from this file. This skill does not claim that following it improves a project's results.

**This skill owns:** whether the interface is correct: every state renders, the binding is the real one, input reaches the element, nothing leaks or polls, and the layout holds at every screen shape. **It hands off:** what a screen shows and in which states to `ux-design`, whose flow, wireframe and states list are your input (if no such pass happened, run it rather than build a guess); whether the result looks right to `visual-craft`, which runs after you; meshes, rigs and animation to `3d-assets`; the rules, numbers and saves behind a screen to the systems skill.

## Design away the bug class

When a UI bug comes back in the same shape, ask first **"can this class be made unrepresentable?"**, not "where else do I patch it?" A navigation stack replaces a hide-list under which two screens could be shown at once; a shared formatter replaces scattered number-to-string calls, any one of which could drift to the machine's culture. Second best is a guard that fails the build. Worst is a comment that records the fix: on the source project two builder scripts each carried a comment, eight lines from a text element, describing the wrapping-text fix that element then lacked (Seen).

**The limit is part of the rule.** A model that forbids a state the product later wants costs a refactor instead of an `if`. Constrain the states that have actually bitten the project; an invariant with no incident behind it is speculation with a test attached. Open `references/timing-and-verification.md` §0 when you weigh a new invariant: the idea's lineage and the counter-argument.

## Hard rules

1. **UI is never logic.** No business rules, money math or state changes in a UI script: UI reads from the systems and calls their public methods. Reading a flag to decide what to *show* is fine; computing or changing state is not. A screen controller is a deep module, a small public surface (show, refresh, events in) that hides its layout and widget wiring; a caller that reaches into a child element to use a screen means the surface is wrong.
2. **UI reacts to events; it does not poll state that has one.** Subscribe to the change event and **always unsubscribe on disable or destroy**, or the handler goes on running for a screen that is gone. Two exceptions are standard: a controller that needs a peer screen's live state finds it lazily at its first real use, and a one-shot reveal keyed to an event that can fire while the game boots gets a one-time sync right after subscribing, or a late subscriber never sees it. **Never assume an ordering guarantee between two components' initialization callbacks:** the source project hit this four times by August 2026, and nothing errors when it happens: the late subscriber simply never hears (Seen).
3. **One owned unit per screen**, with its own controller. A shell manages switching; screens do not know about each other.
4. **The layout contract is a real contract: write it down and guard it.** Whatever pins the canvas, some axis stays variable, so every screen names exactly one destination for the surplus space and every sibling declares zero flexibility. Legal destinations: a scroll viewport, a 3D region, a page background, a named spacer. **Never a text element:** text pins to one edge of its growing box, and with auto-sizing the rendered font size becomes device-dependent. Left unnamed, a flexibility flag set for another reason becomes the destination: on the source project one screen's line text took the surplus and opened a hole of about 450 units on 20:9 phones (Seen). In Unity, the mechanics: `references/unity.md`, "Canvas and scaling".
5. **Input is abstracted once**, not per screen, and every real tap target meets the minimum `ux-design` sets. Art may render smaller as long as its **hit area** meets it: keep the two separable, and compute the check from the element's real bounds, never by eye. Any hold-to-act input funnels every release path through **one idempotent reset**: pointer up, pointer leaving or dragging off, the app paused mid-hold, the screen hidden while held. Otherwise a finger sliding off leaves the held action running.
6. **Follow established patterns.** Before you add a pattern, a library or a helper, check how existing screens do layout, animation, state and input; a layout choice the project settled cost something, so reuse it. Read how the project's toolchain is set up (engine version, input system, the text component's defaults) before you apply a rule from this file: a setting may already do what the rule asks. Open `references/timing-and-verification.md` §2 before you change a list shell, a two-element row, a fixed layout group or a nested force-expand group: the five settled choices and what each rests on.
7. **Audit every per-frame body for three costs that are cheap to miss.** An unthrottled query that walks a list: throttle it to about once a second unless its result is drawn every frame (Seen: on the source project one such poll was throttled after the owner asked what it cost, and the sweep found two more). Slow-changing data visited at frame rate: split an active set from a throttled background sweep fed the accumulated elapsed time. Logging with interpolated strings on a hot path: guard it so a release build never builds the argument, but never compile out a whole method that interleaves logging with real event wiring.
8. **Never put wrapping text in a fixed-size container.** In TextMeshPro, Unity's text component, the default overflow mode does **not** clip: surplus text renders outside its own rect and paints over its neighbours, silently at authoring time. Text that grows with its content gets **no height constraint at all** (the component reports its own wrapped height, so removing the constraint *is* the fix and a bigger constant is not). Text in a genuinely fixed container gets shortened or the container widened, with truncation set regardless. **Measure, never look:** measure the wrapped height of the longest string actually in the data, found by search, and measure again whenever a new length ceiling is authored. On the source project a news row whose own comment said three lines were enough overflowed once real headlines wrapped to four, and by 26 July the class had five instances, three of them in one day; audits on 30 July and 1 August found more (Seen).
9. **An overflow effect inside a masked container clips silently.** A glow, pulse or halo drawn past its own rect is cut off by a masked parent such as a scroll viewport, with no warning at authoring time. Size the effect first, then widen the mask's padding to its spread; never shrink the effect to fit one parent, which makes it wrong everywhere else (Seen: a list row's glow, which its scroll viewport's mask cut off until the mask's padding was widened; two earlier attempts to make the glow fit, a smaller spread and a tighter mask, were both reverted).

## All states, never happy-path-only

Every element bound to live data handles every state on `ux-design`'s states list that it can reach: locked or teaser, first-time, empty, loading, active, and error (not enough money is an error state too). **If a request describes only the active state, go through the rest: name what can put the element in each state, implement those that can occur, and say in your summary which you ruled out and why.** Empty is real: a list before its first entry, an inbox at first launch.

**A newly interactive element ships with a visible sign that it can be tapped** (an icon, a highlight, a chevron, a first-time caption), as part of that state and not as a later polish pass. A tap target that works but looks inert is a gap; the source project found that twice (Seen).

**One state value beats accumulated booleans.** When show logic grows a third `isFirstTime && !isLocked && ...`, impossible combinations can already be written: map the states list onto one enum instead.

## Data binding

- Display values come from the systems' own events and read models. Never guess a field name, and never compute a display value from raw state when a system already exposes it.
- **Every player-facing number goes through one shared formatter that names its culture:** the interface language's, never the machine's (the source project, with one language, names the invariant culture). A raw `:F2` or `ToString()` falls through to the machine's culture and shows a comma decimal wherever the locale uses one, with no error. Parsing fails the same way, so a machine-written value is parsed with the invariant culture: on the source project `float.Parse("0.55")` returned 55 under a culture where the point is not the decimal separator, and turned every new material white. Never parse a string you could write as a literal. The class reached the source project five times by August 2026, the last two after the shared formatters existed (Seen).
- **Displayed value equals credited value.** A preview of an amount a system credits later goes through the same call the crediting path uses, never an inline re-derivation, and two readouts of one quantity come from one call. The failure is silent drift: on the source project two fee previews left out a multiplier the payout applied, and one screen showed a building's income per track without a multiplier its own total included (Seen).
- **Colour never carries meaning alone:** pair it with a sign, an arrow, an icon or a word. A solid-colour badge with no icon or count is the same failure as an uncaptioned red or green number; on the source project one such badge was taken for a rendering glitch twice, and was removed (Seen).
- A non-ASCII glyph that is not in the loaded font atlas renders as a blank or a box. Confirm it is there before you use one (Seen: four times on the source project).
- Write to a frequently updating text only when the value it shows changes: compare at the precision you display, before you format and write.

## Right-sizing

- Get the screen correct first; optimize only against a measured problem.
- **Do not abstract a helper until a second real use case exists:** one adapter is a hypothetical seam, two are a real one. Apply the thin-wrapper test hardest to builder scripts: a builder earns its keep by deleting drift and manual wiring, and stops earning it once it is harder to read than the wiring it replaced on a screen that rarely changes.
- Turn off hit-testing on elements that never take input (a label inside its own button, decorative art).
- Responsiveness across screen shapes and the accessibility checks below are part of done, not a later polish pass.
- Do not migrate UI frameworks mid-project because a newer one exists. Write down why the current one was chosen, so the question is answered once (the source project's choice and its reasons: `references/unity.md`, "Framework choice").

## You cannot self-certify UI

"It compiles", "the handler ran" and a screenshot that looks right are not evidence that a screen works. Generated interfaces are measurably weak on accessibility: a peer-reviewed study of six AI UI design tools (W4A 2026, five WCAG criteria) found 29% compliance, and asking for accessibility in the prompt *lowered* it (D). It measured design generators, not code-writing agents, so take it as a prior about an agent like you, not as a finding. Intent is not a control; a structure plus a computed check is.

- **Make accessibility a computed check.** `ux-design` owns the numbers (contrast ratios, target sizes). Compute contrast from the two colour values, read a target's size from its real rect, and check colour-alone as a structure: every colour-coded state also sets an icon, a shape, a sign or a word, so a test can walk the screens and name the one that does not.
- **Drive real input.** Verify a button with a hit-tested click (in Unity, a raycast with a constructed pointer event), never by invoking its handler: an invoke cannot catch an element that is visible but not clickable.
- **Never let the agent that wrote a check certify the result.** On an ambiguous "make it work", the cheapest passing signal is the tempting one (I; the benchmark: `references/timing-and-verification.md` §4).
- **Say what was not verified** wherever a check cannot be automated, rather than letting the summary imply it was.
- **A capture at one screen shape is not evidence about the others.** On the source project every capture harness rendered only the 1080x1920 design canvas, where a screen's surplus height is zero; six visual passes and a conformance sweep missed the hole of rule 4 (Seen). Capture at the shape people actually hold, and at all four named shapes before a layout is called done.

## Timing, lifecycle and verification

Open `references/timing-and-verification.md` before any verification pass and before any camera, hotspot or lifecycle wiring (§4 grades the evidence, §5 is the protocol and its four shapes). The rules that matter most:

- **Activation does not run all of an object's setup at once.** In Unity, `Start()` runs before the object's first update, not inside `SetActive(true)`. Put a real frame boundary between activation and interaction in any automated check (a click test on the source project read a builder's placeholder text because it clicked in the same call, Seen), and force a layout pass before reading measured positions.
- **Edits made during a live play session revert when it stops.** Redo the final value as a deliberate edit outside play mode, save, and verify again from a fresh session. The source project lost work this way four separate times, the first two in consecutive sessions: a desk moved, then a camera tweaked, each against a live screenshot (Seen).
- **A multi-camera 3D screen pays one render for every enabled camera.** Disable a hidden screen's camera, and resolve its rig reference lazily at the point of use: on the source project a disable that ran before the reference resolved did nothing, and a hidden room's camera kept rendering (Seen).
- **An element placed over 3D content is projected again every visible frame**, never baked once, and its size lives in the same space as its position: hotspots placed by projection but sized as a fraction of their screen area grew into each other on taller phones, where a tap in the overlap fires whichever button is later in the sibling order (Seen).
- **A lifecycle handler (resume, focus, reconnect) answers "what if this fires twice, or when nothing changed?"** On the source project a resume handler set an offline recap that no screen showed, and the next launch paid it twice (Seen: a bug audit's confirmed finding).
- **An editor tool run while the code has compile errors, or before a recompile finishes, runs the last good build and reports success.** Check the rebuilt prefab on disk for a value only the new code writes, never the log line (Seen: four ways on the source project, stale prefab rebuilds twice in one milestone among them).
- **A safe-area or canvas measurement taken once goes stale:** measure again when the layout changes. A root controller on the source project kept a width cap computed from a stale canvas rect (Seen).

## Importing an external design mockup

**The mockup file's literal values are the spec; never re-derive a value from how a render looks.** "Build this screen" produces a visual reproduction, and close is not the spec. Before touching the engine, follow the seven steps in `references/design-import-pipeline.md`: extract the values, convert them, write the plan with what is deliberately not taken, and check every shared visual change by a numeric diff before building on it. Two conversions are where a literal copy goes wrong:

- A radius snaps to one of the project's existing tiers, never a new one: the source project shipped two card radii side by side once a new surface helper brought its own (Seen).
- **Colour alpha is measured again in the renderer's own colour space, never copied:** a border's alpha of 0.10 in the mockup measured 0.025 in the engine, and 0.020 after the surface under it changed (Seen).

## Release and engine layers

Open `references/release-hardening.md` when a release build is being prepared: the device matrix, the build settings, the stripping trap and how to find it without a device, the touch edge cases. **Before you write interface code for an engine, open its file:** `references/unity.md` (the depth the source project was built with: canvas scaling and the slack contract, TextMeshPro, navigation, builder scripts, safe area, input, verification), `references/web.md` (a page's own interface, and a game build embedded in one) or `references/unreal.md` (**not verified**, open questions only).

## Mistakes to flag

Run this list when you review UI code, your own included. When a change adds a branch or a special case, ask whether it can be reframed so whole branches disappear; "but it works" is not an approval bar.

- A reachable state from ux-design's list missing (locked, first-time, empty, loading, error), or a working tap target with no sign that it can be tapped.
- Logic in a UI script; a caller reaching into a controller's children.
- Polling where an event exists; a subscription never removed; an initialization order between two components assumed.
- A guessed data shape; a preview or a second readout computed apart from the call that credits.
- A new pattern where an established one fits; a rule applied without a look at the project's toolchain.
- A third boolean in show logic where one state value belongs; a thin wrapper that adds indirection without buying clarity.
- Wrapping text in a fixed-height container, a height constraint on text that grows, or auto-sizing on dynamic text.
- Surplus space with no named destination, or text absorbing it; a glow or halo clipped by a masked parent.
- A raw format or parse call near a player-facing string; a glyph not confirmed in the font atlas; a second font asset with no stated reason.
- A new top-level screen wired through a hide-list instead of the navigation stack.
- A live-session edit trusted as final without redoing it and verifying again from a fresh session.
- A button verified by invoking its handler instead of a hit-tested click; a green compile offered as evidence that a screen works.
- A hit area below the minimum, or sized by eye; a colour or badge with no icon, shape or count beside it.
- A capture at one screen shape offered as evidence about all of them; the agent that wrote a check certifying the result.
- A lifecycle handler that breaks when it fires twice; a safe-area measurement taken once and never again.
