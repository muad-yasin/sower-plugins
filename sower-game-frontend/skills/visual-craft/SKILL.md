---
name: visual-craft
description: Judges whether a game's or app's visuals actually look right, and fixes what does not - composition and focal hierarchy, palette and material consistency, typography roles, staging and prop placement under a fixed camera, lighting, contrast and colour-blind checks, and capture-based review of 3D scenes, icons, logos, backdrops, UI chrome and generated assets. Use once flow and implementation are correct and the question is whether it looks right, including when something only "looks off" or "looks cheap". Not for flow, wireframes or screen states (ux-design), implementation correctness (ui-implementation), or building geometry and motion (3d-assets, whose acceptance gate this skill is).
license: MIT
---

# Visual Craft

You own whether something *looks* right, in every visual medium: 3D scene staging, 2D icons, backdrops and logos, and UI chrome. You start once flow and implementation are correct. `3d-assets` builds geometry and motion and does not judge them: this skill is its acceptance gate.

**Open the actual reference file before every visual decision, never your memory of it.** Memory of a reference drifts (I): on the source project the written art direction had to be corrected to match three real reference images once they were adopted (Seen).

**Evidence and grades.** **Seen** = it happened on the source project (a Unity mobile game), with the record named in `references/evidence.md`. **D** = documented in a named source, read on the date given there. **I** = inferred, with the reason in the sentence. Open `references/evidence.md` before you quote a figure or an incident from this file. This skill does not claim that following it improves a project's results.

**This skill owns:** composition, palette, materials, typography roles, staging and placement, lighting, contrast checks, and the capture-based review of every visual surface. **It hands off:** flow, wireframes, states and the accessibility numbers to `ux-design`; implementation correctness to `ui-implementation`; building or exporting geometry and motion to `3d-assets`.

## Step 1: Anchor the visual language before touching an object

- **Never invent a style in isolation.** Anchor to what exists (shipped assets, reference images, an established palette) and extend it.
- **Keep the layers apart.** A style is a stack of separate decisions: shape language, value range, palette, material vocabulary. **Camera and perspective are a presentation choice on top.** Two of the source project's three rooms moved from an isometric camera to a near-top-down perspective one, and the art direction stayed as it was: framing, not style (Seen). **Name which layer a visual complaint lives in before fixing it:** many a "this looks wrong" is a framing problem in a style problem's clothes (I).
- **Where there is no precedent, know what the default looks like before you choose.** Open `references/originating-a-new-surface.md` before originating a genuinely new surface: three looks a generated design falls into by default, their tells, and why a deliberately chosen dark foundation is not one of them. **None of those defaults is a choice when it arrives unexamined;** recognizing one and stating why it is still right here clears the same bar as a new palette colour.
- **Resolve composition in value before colour.** Check focal hierarchy and depth in grayscale or silhouette first: a composition that does not read in value is not rescued by a palette, and fixing it after colour is committed means redoing both. Three scales: the whole scene (one dominant value mass), each asset (a clear silhouette before any colour pass), and **UI over scene** (the UI layer holds its own value territory, so it does not fight the environment for read priority).
- **Every frame needs one dominant focal read.** Two elements competing for first glance is a composition bug, not a taste disagreement. Under a fixed 3D camera, work out what its angle reveals first (what is closest, largest, most contrasted) and design around that, never around an idealized plan view.
- **Palette discipline:** a small, deliberate, reused palette beats a large expressive one; variation comes from **value and saturation within a few hues**, not from more hues. A new colour needs a stated reason tied to meaning, never a generated asset's drift or how it looked on one prop alone. A written palette is a reference to open at every addition.
- **Materials agree on light response.** Everything sharing a space agrees on how shiny, rough or flat it reads, and a material reads as its substance before any label does. **A scene whose materials disagree looks incoherent even when every colour is right;** copying one prop's setup without checking its siblings is the usual way it happens. Keep non-metal base colours in a physically plausible middle range: on the source project a plan diagnosed a near-white wall above that range: it clipped under its key light and read as paper (Seen). Put the style in narrowed value ranges, palette restraint, simple geometry and proportion, and let the lighting do its physical job (I).
- **Typography is an identity decision as well as a restraint rule.** At most two sizes or weights per screen unless there is a reason; a shared type scale over a bespoke one; a new face clears the same bar as a new colour. Open `references/typography-and-spatial-mapping.md` before you choose a typeface or a type scale: the three roles (chrome or display, body, data and numerals). **One requirement is functional: numerals that update live use tabular, fixed-width figures,** so a digit changing from 1 to 8 never reflows the value; a jittering price reads as broken, and no still capture shows it (I). Check it on a live value.

## Step 2: Spatial composition and staging (special weight for a fixed 3D camera)

**Translating screen-relative language ("move it top-left") into world coordinates under a fixed, non-orthogonal camera is a gap this work keeps hitting** (I). Open `references/typography-and-spatial-mapping.md` before any placement or moving pass under such a camera: the full procedure, which the source project used through the rounds of placement requests of one session (Seen). The headline rules:

- **Never place or move an object by eyeballing where it lands on screen.** Sample the engine's world-to-viewport projection at known landmarks first (room corners, existing fixtures, wall planes), read the mapping off three or four samples, and trust it over intuition.
- **Check real clearance against every neighbour's footprint,** not only non-overlap.
- **A camera's screen extremes are not always reachable together.** When two world axes pull the screen position in conflicting directions, favour the direction named most specifically, keep the other from getting worse, and **say so**, instead of silently forcing a worse compromise (Seen: a desk's move on the source project stopped short of the room's extreme corner to keep clearance, and the trade-off was stated).
- **Block out a genuinely new layout with placeholder shapes before building final geometry.**

**Group props the way the eye groups them:** proximity, similarity and common region make separate objects read as one cluster, and **figure-ground keeps a tappable prop from melting into the décor behind it,** a common failure in a busy scene (I). If a tappable object does not separate from its background in a grayscale capture, it is a staging bug: fix it with value and lighting before reaching for a glow or an outline, which are `ux-design`'s inviting signals and a different job. Open `references/staging-and-lighting.md` before a staging or lighting pass: the full vocabulary, lighting as its own pass, and the scene-authoring checks for mobile.

The through-line: **readability first (silhouette, value, grouping), then spend on hierarchy.**

## Step 3: 2D and UI visual quality

- **One stroke weight, corner radius and shadow depth across every icon in a set:** one mismatched item reads as wrong faster than any single quality gap.
- **Check legibility at the actual render size**, never at generation or preview size: crisp at 512 pixels can be mush at 48.
- **Reuse the shared chrome system once one exists.** A bespoke panel or shadow treatment per screen is then a regression, not a style choice.
- **Colour never carries meaning alone:** pair it with a shape, an icon, a sign or a label. **Compute contrast, never judge it by eye,** against the thresholds `ux-design` holds. Stored constants give the answer only for an opaque colour on an opaque flat surface. Where a colour is translucent, tinted or blended, or lies over an image, take both colours from a real capture of that state, off the flat of a glyph and not its antialiased edge (I): in a linear colour space a light colour at a low stored alpha, laid over a dark surface, reads about four to five times heavier than its number suggests (Seen). Open `references/color-accessibility.md` before a contrast or colour-blindness check: the formula, the protocol (the simulator's algorithm matters) and the palette ratio.

## Step 4: Verification: check, do not just judge by eye

- **A capture is the only ground truth.** Never trust a computed or expected position, colour or bounds without a rendered capture: on the source project a signage wordmark sat fully behind its own panel while verification reported no errors, and a locale-parsing bug turned every new material white, caught by the first capture after the batch (Seen).
- **A capture taken in a live play session proves the live state, not the saved one.** Edits made during play revert when it stops: on the source project a desk was moved during play while it was checked against live screenshots, and the move was lost when play stopped. It went unnoticed through several later verification passes, because its hotspot, made separately outside play, never moved and every click test passed (Seen). Redo the final value as a deliberate edit, save, and verify again from a **fresh** session.
- **Check at more than one distance and angle.** Many defects (occluded detail, an illegible small prop, a silhouette that does not read) show at exactly one framing.
- **Once a set of related assets grows past a handful, check them together:** a contact sheet or a showcase view shows palette drift, inconsistent scale and silhouette overlap that piece-by-piece review never will. For drift over time, compare pieces from different points in the timeline under identical conditions; the divergence locates the break (I).
- **Cover every real state:** an empty slot, a locked state, an unfilled desk are things a player sees, not placeholders for later.
- **A vision model's read of a capture, your own included, is a measurement, not a taste authority.** When multimodal models judge vision-language tasks, their verdicts carry biases, invented details and inconsistency, and they track people better when comparing two items than when scoring or ranking (D); a yes-or-no or multiple-choice question makes a model look at the image less than an open question does (D). So **compare the capture with a reference instead of asking for a score** (I: the pair case), **describe it in an open question before judging** (D), and **ask more than once** (I: the verdicts vary). Two more counters come from review practice rather than these papers: **name a checkable heuristic, and crop to the asset under review** (I). Open `references/critique-and-vlm-qa.md` before any formal critique or judgement of screenshots: the protocol, its limits, and the gap in the evidence about taste.
- **Get a second, less invested read when the stakes justify it.** Whoever built a thing is primed to see what they meant; a different capture angle, a break, or another reviewer catches what one continuous session will not.
- **State the trade-off when a fix is not free:** a camera change that helps the common case but risks cropping on an untested aspect ratio; a placement that meets one of two named directions. A partial fix does not pass as a full one.

### Generated and procedural environments

Open `references/procedural-environments.md` before generating or reviewing one. Write the acceptance criteria *before* generating, judged at the size the player sees, and know **the five tells of a structurally generic result:** a perfect silhouette, no geography, invisible hierarchy, uniform distribution, one material family. Put each to the result as a question. On the source project a regenerated city map was rejected as generic with all five in its diagnosis (Seen), which does not show that one of them alone spoils a map: reject by the criteria you wrote, shown in the view the player has. **Detail at the block level cannot rescue genericness at the level of structure.**

## Step 5: Tooling, where it earns its keep

- **A dedicated mockup tool earns its cost on two things:** coordinating visual decisions across more than one person, and validating an expensive layout before paying to build it (I). Solo, with a fast screenshot loop inside the engine, neither applies hard, and a translation step in and back adds cost without removing any. Revisit when either condition changes.
- **Keep a small reference library** (reference images, accepted assets, written style recipes) as the source of truth for what on-brand looks like.
- **Check the licence of each tier of an image generator before anything ships.** On the source project a free tier's output was licensed for personal use only, so only the paid API's output could become a game asset (Seen): explore a prompt formula on the free tier, ship from the paid one.

## Mistakes to flag

- A 3D object placed or moved by eyeballed screen position instead of a verified world-to-screen mapping.
- A computed colour, position or bounds trusted without a capture.
- A new palette colour, typeface, material setup or visual pattern introduced without checking precedent.
- A scene or asset judged from one camera distance or angle only.
- New geometry authored from scratch where an existing verified shape could be adapted.
- A visual state (empty, locked, first-time) shipped as "later polish".
- A new tool reached for out of habit instead of a stated gap.
- Full detail built on a new layout before a placeholder pass confirmed position and scale.
- A growing set of assets reviewed only one by one.
- A new surface landing on a recognizable default without naming and justifying it.
- Live-updating numerals without tabular figures.
- "Does this look right?" put to a vision model, yourself included, with no reference to diff against, no named heuristic and no description first.
- A contrast or colour-blindness claim made by eye, or from stored constants where a colour is translucent or blended.
- A "style" complaint fixed when it is really about framing or the camera.

## Engine layers

**Before you judge or fix visuals in an engine, open its file:** `references/unity.md` (colour space, the capture standard, the layer trap, materials and the lights each room needs, shared chrome), `references/web.md` (CSS colour, pixel density, font rendering, capture tools) or `references/unreal.md` (**not verified**, open questions only).
