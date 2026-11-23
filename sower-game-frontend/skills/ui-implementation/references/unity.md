# Unity: the implementation layer

*Open this file before you write interface code in Unity: uGUI with TextMeshPro, the canvas and its slack contract, navigation, builder scripts, the safe area, input and verification, as the source project built them.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Framework choice, decided once

The source project built its interface on uGUI, with every screen built by an editor script, and kept it (Seen: its earlier skill records the choice). A research note of 26 August 2026 gave the argument for staying: a project committed to uGUI, with heavy animation and world-space needs, and a UI Toolkit that still needed its safe area handled by hand (I: the note's argument, not a measurement). Unity's comparison for 6000.6 bears on them: it recommends uGUI for runtime interfaces, with UI Toolkit as the alternative; it marks integration with animation clips and Timeline as uGUI's alone, and a data binding system and transition animations as UI Toolkit's alone; and it marks world-space rendering as supported by both (D, Unity manual 6000.6, "Comparison of UI systems in Unity", read 2026-11-22). A UI Toolkit screen that uses `Screen.safeArea` inverts its vertical coordinate itself (D, Unity's `Screen.safeArea` reference, read 2026-11-22).

Do not propose a migration mid-project (`SKILL.md`). With no data binding system in uGUI, events and builder scripts stand in for a view-model layer on this stack (I).

## Canvas and scaling

- The Canvas Scaler scales with the screen size against a reference of 1080 by 1920 (Seen: the source project's canvas).
- **`matchWidthOrHeight` is set at runtime, never by hand: 0 on a device no wider than the design, 1 on anything wider.** Never a blend. At 0.5 the canvas gets narrower than 1080 units on every screen taller than the reference: on the source project a category grid that asked for 984 units fitted the Editor's 1080 by 1920 view exactly and overflowed at 20:9, where the canvas was 966 units wide (Seen, August 2026).
- A root controller caps the root at 1080 design units and centres it on anything wider, so a tablet gets the phone with margins (Seen). Whether that is enough for a tablet is `ux-design`'s decision, in its `references/unity.md`.
- **So the width is the constant and the height the variable:** 1920 at 16:9, about 2400 at 20:9, about 2520 at 21:9, which hands every screen up to 600 units of surplus height (Seen).

### The vertical slack contract

`SKILL.md` rule 4 is the rule; these are its Unity mechanics. The destination is the one sibling with a nonzero `flexibleHeight`, and every other sibling declares `flexibleHeight = 0`. The legal destinations are a `ScrollRect` viewport, a 3D room area, a page background, or a named spacer from a helper that inserts the spacer *and* zeroes its siblings in one call, so that the destination cannot be half-set (Seen: the source project's helper).

The hole of rule 4 opened this way: a `flexibleHeight = 1`, added so that auto-sizing had a box to shrink in, made the line text the destination (Seen). Guard the contract with a test that fails the build when more or fewer than one sibling declares flexibility, not with a convention (Seen: the source project's guard).

## Canvas performance

Any change to one `Graphic` dirties the batch of its whole Canvas (not checked at a source; stated here since September 2026, after a Unite talk of 2017; Unity's tutorial on optimizing its UI now leads to a deprecation notice). Four rules follow from that cost model (I):

- Split a Canvas into sub-canvases when an element that updates often (a live countdown, a value on the HUD) shares one with mostly static content.
- Disable a Canvas that is off screen (`enabled = false`) instead of only hiding its content.
- Share one font asset and one material preset, so that text batches instead of splitting draw calls.
- Turn off Raycast Target on every `Graphic` that never takes input (a label on its own button, decorative art). Every pointer event walks the raycast list, so the cost is per touch, not per frame: an audit on the source project found 36 such entries on the one screen where touch latency was the mechanic, and filed them as low priority because the events still resolved correctly (Seen, August 2026).

## TextMeshPro

`SKILL.md` rule 8 is the rule; this is the component's side of it.

- **Auto Size costs on text that changes.** With it on, TextMeshPro "lays out the text multiple times to find a good fit", and its manual says to avoid it on dynamic text that changes often; for static text it suggests turning it on once, noting the size it picks and setting that size by hand (D, TextMeshPro package manual 3.2.0-pre.15, "UI Text GameObjects", read 2026-11-22).
- **The Overflow mode does not clip:** it "Extends the text beyond the bounds of the display area" (D, the same page). The page does not say which mode is the default; the source project's records name Overflow, and its cases are what that default did (Seen). Surplus text paints over its neighbours, and under a `LayoutElement.preferredHeight` or a fixed button width it shows only with real worst-case content. By 26 July 2026 the class had five instances, three of them that day: an article body and an email body; a 302-character blurb that needed 297 px in a 180 px slot and painted over the price above it; a 142-character header that needed 148 px in an 80 px slot; and a 346 px label at 42 pt in a 260 px button, past the right edge of the screen. Audits of 30 July and 1 August found more, and a session in early August measured 34 of 83 dialogue lines overflowing their card (Seen).
- **The fixes of rule 8, in TextMeshPro's terms.** For text that grows, delete its `LayoutElement.preferredHeight`: `TMP_Text` reports its own wrapped height through `ILayoutElement`, as the source project's audit of 30 July 2026 puts it, and that audit prescribed exactly this deletion, the fix already applied twice in the same file (Seen). For text in a fixed container, the overflow mode to set regardless is `Truncate` or `Ellipsis`.
- **Measure with `TMP_Text.GetPreferredValues(text, contentWidth, 0f)`.** The rects of a prefab asset are not laid out, so the source project's working procedure instantiated the prefab under a throwaway 1080 by 1920 canvas, activated the whole subtree, forced two layout passes, read the real rect and then measured every string in the content asset; a count of characters predicted overflow poorly (Seen, July 2026).
- A sampling point size that does not match the atlas gives artifacts, not errors: `timing-and-verification.md` §3.

## Navigation

**Every new top-level screen joins the navigation stack; no screen is shown or hidden by a manual hide-list.** Forward is a push, back is a pop, a full reset clears to the root, and the stack owns hiding whatever was on top, so a new screen needs no edit at any sweep site (Seen: the source project's stack replaced the hide-list for every top-level screen, modal and sub-panel). A hide-list makes "two screens shown at once" representable (I).

A mechanical coverage test is the guard: every screen root the stack declares is reachable through its own sweep, and no other file brings back a hard-coded pair of screens (Seen). Check that it passes before you call a screen done. The old full-sweep helper stays right for the few cases outside the stack, such as a full-screen dialogue's own sweep before it shows; do not use it for a new top-level screen (I: the source project's earlier skill states it).

Back presses, as the source project's owner set them on 16 August 2026: one press pops; a second press within 2 seconds jumps to the home screen; a third, or a lone press already at home, opens an exit confirmation instead of quitting. The stack handles hardware Escape too (Seen). Two later audits changed the details: the streak was timed in scaled game time rather than on the wall clock (found and fixed on 20 August), and pushing or popping a modal did not reset it (found on 3 September) (Seen). Time such a streak on the wall clock, and reset it on every change to the stack (I).

## Editor builder scripts

Screens are built by editor scripts run from a menu, not wired by hand: each builds the hierarchy, wires serialized fields through `SerializedObject` and saves a prefab. **Running one again overwrites the whole prefab**, so anything added to it by hand is gone at the next rebuild (Seen).

- The source project's builders left peer screen references unwired, and each controller found them at runtime in its own `Start()` (Seen). Where a reference is needed before every `Start()` has run, resolve it at the point of use instead, as the multi-camera rule of `SKILL.md` says.
- A new screen also needs scene-side data a builder cannot create, on the source project a registry entry and, if the home screen reaches it, a tile: name them in the handoff (Seen).
- Keep serialized fields few and clearly named.
- **A builder run while the project has compile errors, or before a recompile has finished, executes the last compiled assembly and still reports success.** On the source project this bit four ways: stale prefabs twice in one milestone; a recurrence that passed a check of the play state and an empty console and was caught only by reading the rebuilt prefab's YAML; and stale bakes while a shared editor carried another session's compile errors (Seen, July and August 2026). Confirm a clean compile before the run and check the output on disk after it, never the tool's own success line (`timing-and-verification.md` §1).

## Layout on first activation

**A screen that computes positions from a `RectTransform` on its first activation forces a layout pass first:** `Canvas.ForceUpdateCanvases()`, then `LayoutRebuilder.ForceRebuildLayoutImmediate()`. Unity defers layout, so a rect read at once can be stale or zero (Seen: the source project's verification plan of 31 July 2026). The source project hit two limits of that pass (Seen, July and August 2026):

- Under a `ContentSizeFitter`, whose final size is known only after the fitter has run against the new content, a one-shot rebuild is not enough. Solve again in `LateUpdate` whenever the rect is dirty, which also catches a rotation or a change of the safe area.
- `Canvas.ForceUpdateCanvases()` alone does the layout but never assigns a graphic's depth, so an element activated in the same editor tick sits at depth -1, invisible to the `GraphicRaycaster`, until real frames have run.

## Safe area

**The bottom is a shared inset; the top is a keep-out, not an inset** (Seen: the source project's rule since 30 August 2026).

- Bottom: shared code applies the reported bottom inset to the persistent strips at the bottom of the screen (a money HUD, a ticker), so that they clear a gesture bar.
- Top: **do not reserve a top band.** A band nobody paints is the black bar that came back across three design rounds on the source project, until the bars were removed structurally on 30 August 2026 (Seen). Every screen paints its own background to the true edge of the canvas, and a guard test over the real prefabs that fails the build keeps text and tap targets out of two named shapes: a sliver at each rounded corner and a box at the top centre, around the camera. It names the element and the shape it reaches into, so a new screen needs no safe-area handling of its own (Seen).
- In the plain Editor Game view `Screen.safeArea` reports no cutout at all: what that cost the source project, and what the reference says, are in `release-hardening.md`.

## Input

- The New Input System, abstracted once: one set of named tap zones defined in one place, not one per scene (I: the source project's earlier skill describes its input this way).
- **A hold input is one component, pure input plumbing that raises one held-changed event.** Reuse it instead of hand-rolling pointer handling (Seen: the source project's first hold input, July 2026, covered pointer up, a drag off the button, the app paused mid-hold and the screen disabled while held). `IPointerExitHandler` fires without a pointer up when a finger slides off (not checked at a source; stated here since September 2026), and the source project's records say a cancelled Android touch arrives through the pointer-up handler (I: stated when that input was built, not tested on its own). Every release path still goes through one idempotent reset (`SKILL.md` rule 5).
- A tap target's **hit area** is the bounds of its `Image` or `Button`, not the visible art. Invisible hotspots over 3D props keep the two separable, and the minimum is computed from `RectTransform` sizes (I).

## Verification

The rules are in `SKILL.md` and `timing-and-verification.md`; these are the Unity mechanics.

- **A real click** is `GraphicRaycaster.Raycast` with a constructed `PointerEventData`, never `onClick.Invoke()`, with a real frame boundary after any `SetActive(true)`, because `Start()` does not run inside it. In an editor driven through a bridge, step real frames before the raycast: an unfocused editor may render none between calls (Seen: the source project's pipeline notes).
- **A hotspot over 3D content** is projected again every visible frame by a rig in the scene, through `Camera.WorldToViewportPoint` against a world anchor. A position baked into a prefab cannot follow, because a prefab cannot reference a scene object (I).
