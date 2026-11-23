# Unity: visual-craft specifics

*Open this file before you judge a capture from a Unity project: the engine facts that change a visual judgement. Building the geometry is `3d-assets`'s, in its `references/unity.md`; this file is about judging what came out.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Colour space is the first thing to establish, and it invalidates a stored alpha

`SKILL.md` gives the lift: in a **linear** colour space a light colour at a low alpha over a dark surface reads about four to five times heavier than its number. Two details it leaves out. The correction belongs where that combination occurs, not everywhere: on the source project a gold strip over near-black took a multiplier of 0.40, while white strips over an already bright gold gradient shipped untinted (Seen). And the measured case: a mockup's gold border alpha of 0.10 matched at 0.025 in a real capture on 24 August 2026, and at 0.020 when the card fill changed three days later (Seen).

**Consequences for every visual check here:**

- **Where a colour is translucent or blended, take contrast measurements from a real capture, never from the palette constants.** An opaque pair is its stored values.
- **Measure any alpha imported from a mockup again** each time it lands on a new surface, instead of converting it once and trusting the conversion.
- **A surface whose colour is baked into its sprite takes a multiplier at runtime, never a palette colour.** On the source project this was the defect that closed a design milestone: sprites carrying a neutral top-light ramp or real gold pixels are painted white so that the bake reads as authored, and a controller that wrote a palette colour into `Image.color` tinted the bake instead of replacing it, quietly about 10% dark over the ramp and visibly gold over gold on a button (Seen). Route every runtime recolour through one shared helper per family, and pin it with a test.
- **A button whose fill is rewritten at runtime with a non-gold colour is not a primary button, whatever it was built with.** A rule that read a control's fill at build time is how a two-state toggle and a three-state card shipped wearing a one-state gold bake that no multiply could recolour (Seen). "Primary" claims that the accent is the button's only fill, not where its fill starts.

## The capture standard

**A capture is the ground truth, and its recipe is fixed:** Play Mode; the room's own camera rendered into a RenderTexture at a named canvas shape, keeping its live `rect`; `ResetAspect()` first; and never `ScreenCapture`, which captures the editor window (Seen: the source project's capture standard, August 2026). The recipe's details are in `../../3d-assets/references/unity.md`, "The capture standard". Two limits change a judgement:

- **The harness is no evidence about a renderer feature or a post-processing pass:** check screen-space effects in the real Game view. A weak reading from an unfaithful instrument looks the same as a weak effect (Seen).
- **Capture more than one canvas shape:** the design reference is the one shape where a screen's surplus height is zero (`../../ui-implementation/references/timing-and-verification.md` §5.4).

**"No console errors" is not "it is visible":** `SKILL.md` has the source project's wordmark, which had never been visible in the shipped build (Seen).

## Invisible geometry: check the layer before the position

Where several 3D scenes share world coordinates and only the cameras' culling masks separate them, a new piece on the wrong layer is invisible; the source project hit it three times in one room (Seen). **The signature to recognise: geometry that is provably present, active and correctly placed, and provably not on screen. That is a layer, not a position:** stop chasing coordinates the moment you see that pair. Inherit a layer from a sibling *renderer*, never from a group root, and read it back. An imported model defaults to layer 0, which the main camera renders and the room cameras cull, so an unset asset vanishes from its room *and* draws over the 2D interface (Seen). The mechanics: `../../3d-assets/references/unity.md`, "Layers, and the invisible-geometry bug".

## Materials and lighting

- **A black specular streak on a flat-shaded prop is the material's default smoothness, not the lighting:** on the source project URP/Lit's default produced one with no skybox or reflection probe, and the flat-shaded recipe sets a smoothness of about 0.15 with no metal (Seen). Copy an existing project material instead of building one from the shader; the recipe is in `../../3d-assets/references/unity.md`, "Materials".
- **Each room owns its key and fill lights, as children of its own root.** On the source project the first room's lights turned out to be the only lights in the scene when the second room was built, so hiding the first room's root would have left every other room dark (Seen, July 2026).
- **Check a light with a render toggled on and off, in the mode you care about,** not by its Inspector intensity. In Edit Mode, with every room root active, a fill of 0.45 contributed nothing, which the record explains as URP applying only the main light and the four brightest additional lights to each object; at runtime only one room is active, so the finding did not hold there (Seen: a finding of July 2026 whose scope was corrected on 1 August).
- **Bloom took three settings at once:** on the source project it was wired on all three room renderers by setting post-processing data on the renderers, raising the effect's intensity from its shipped 0 and switching post-processing on for the room cameras, and the record calls it all or nothing (Seen, August 2026).

## Play-Mode edits and the screenshot that lied

**Scene edits made in Play Mode revert when Play stops, and an anchor made separately that stays put can hide it:** `SKILL.md` has the source project's desk, which sat 1.5 to 2 m from its hotspot through several verification passes (Seen, July 2026). Redo the final value as a deliberate Edit Mode edit, mark the scene dirty, save, and verify again from a fresh Play session before you trust a live screenshot as final.

## Shared chrome

Where a project has a generated system of rounded panels, shadows and radii, **it is the source of truth, and a bespoke treatment on one screen is a regression** (I). Two rules from the source project:

- **Keep the radius table small and closed,** and let a shared helper decide which tier a surface gets, by its height, not by the call site's choice; a short card at a large radius is a capsule, a different primitive. No call site chooses it, no parameter exposes it and nothing can opt out: that is what stops the table from growing an axis (Seen).
- **A decoration that a helper applies by default is how unwanted chrome appears.** On the source project a helper added an inset top hairline to every card. Nobody had chosen it, its owner raised it more than once in one evening, and it was removed project-wide on 23 August 2026 (Seen). An edge, glow or accent that a shared helper applies should be opt-in, with the reason beside the parameter.
