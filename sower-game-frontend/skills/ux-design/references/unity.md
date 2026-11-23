# Unity: design-side specifics

*Open this file before you wireframe for a Unity project: what a designer has to know about the engine so that a wireframe survives implementation. The implementation half is `../../ui-implementation/references/unity.md`.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **I** = inferred, with the reason in the sentence. Where each line comes from: `evidence.md`, its section on this file.

## The canvas contract: width fixed, height variable

On the source project the Canvas Scaler scaled with the screen against a portrait reference of 1080 by 1920, matching width on any device no wider than the design and height on anything wider (Seen). So **every screen is authored at exactly 1080 design units wide** and handed a height from 1920 (16:9) through about 2400 (20:9) to about 2520 (21:9): up to 600 units of vertical surplus that the horizontal guarantee says nothing about.

**Design consequence:** name one destination for that surplus on each screen: a scroll viewport, a 3D room region, a page background or an explicit named spacer. **A text element is never one:** text stays pinned to one edge of its growing box, and with auto-sizing on, the rendered font size comes to depend on the device.

The failure is never the layout mechanism, which works as documented; it is leaving the destination unchosen, so that a flexible height set for another reason becomes it. On the source project one dialogue box did exactly that: a flexible height added to give auto-sizing room made its line text the destination, which left a hole of about 450 units on 20:9 phones while the box rendered perfectly at 1920. It survived six visual passes because every capture harness rendered only the reference canvas, the one shape where the surplus is zero (Seen). When you are shown a capture, ask which shape it is.

A design-width cap that centres the root on anything wider gives a tablet the phone with margins, not a stretched phone. On the source project that was enough for tablets, because its interface is a phone inside the fiction, so the margins read as deliberate (Seen). A product without that fiction needs its own decision for tablets; tall phones need one on every product.

## Safe area: top and bottom are different problems

- **The bottom is an inset.** A gesture bar sits under the content, and shared code nudges the persistent bottom strips clear of it. Nothing for the designer to do per screen.
- **The top is a keep-out, not an inset.** Reserving a top band leaves a black bar unless something paints it, and "something paints it" is the coordination that keeps failing: on the source project that bar came back across three design rounds (Seen). The better shape: every screen paints its own background to the true edge of the canvas, and content stays out of two named shapes, a sliver at each rounded corner and a box at the top centre around the camera. A guard test over the real prefabs that fails the build enforces it, which is where it belongs.

The cost to design is small. A left-aligned header usually clears the camera box (I), but a heading wide enough to reach the centre does not: on the source project one wide heading crossed it (Seen). Only content that is genuinely new at the top centre needs a deliberate look.

On the source project `Screen.safeArea` reported no cutout in the Editor, and a safe-area fix of July 2026 was reverted because the Editor showed no visible change, which the later record calls a false alarm; such a fix could only be confirmed on a real device (Seen). Unity's Device Simulator is the in-editor view that shows notch shapes (not checked at a source; stated here since September 2026). Accept the plain Game view as evidence of nothing, either way.

## States, in a project that builds its screens by script

Where Editor menu scripts build the screens instead of hand wiring, the states list you hand over is not a suggestion: it is the builder's argument list. A state you forget has no natural place to appear later, because the builder overwrites the whole screen each time it runs, so anything added to the prefab by hand is gone at the next rebuild (Seen). Name locked, first-time, empty, loading, active and error explicitly, including which of them share one rendering.

## Two things a wireframe must state that Unity will otherwise decide for you

- **Which element takes the surplus height** (above).
- **Whether a list's content can change at runtime.** It decides between a shell filled once and rows destroyed and rebuilt, and the wrong choice is not a performance problem: a shell filled once cannot show a changed set at all, so it gets replaced wholesale instead of extended. On the source project one list shipped as a shell filled once, on the assumption that its roster was fixed (Seen).
