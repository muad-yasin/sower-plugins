# Staging vocabulary and lighting as its own discipline

*Open this file before a staging or set-dressing pass, before a lighting pass, and whenever a scene reads flat or busy, or its props will not separate from the background. `SKILL.md` holds the through-line, readability first and hierarchy after, and the figure-ground test in grayscale.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Gestalt grouping is the staging vocabulary, not decoration theory

In a fixed-camera scene there are no cuts and no camera moves: **the static arrangement carries all the meaning,** and Gestalt grouping is what the eye uses to parse it (I).

- **Proximity, similarity, common region:** compose set dressing in clusters of related details, so that separate objects read as one intentional group. The cheap workflow is the kit rule, duplicate and then shrink, rotate and offset, which turns a scatter of props into a grouped form instead of confetti (I). Its failure twin is procedural tell #4, uniform distribution (`procedural-environments.md`); hand-placed dressing fails the same way when nothing clusters.
- **Figure-ground:** the grayscale test in `SKILL.md` is the check, and the fix is separation by value and light before any glow or outline.
- **Classical framing rules (thirds, leading lines, symmetry) steer the eye's path; they are not laws.** Centring a subject against the thirds is a valid move for tension when the subject really is the centre of attention. A classical idea that pays in prop work is **negative space**: a hero prop keeps a readable gap around its silhouette. Dynamic-symmetry armatures exist as a reasoning tool, but they are more than a fixed 2.5D room needs (I).
- **Gate readability in greybox, before detail:** block out, mass the colours and judge readability before any detail pass, the same discipline as a blockout before detail and a grayscale check first (I). Published productions describe such passes, among them a month-long blockout for Valorant and a redesign of de_cache that traded busy contrast for readability (not checked at a source; stated here since September 2026).

## Lighting is a separate discipline from material authoring

Materials decide how a surface responds; **light decides where the eye goes, what mood the room carries and how deep it reads,** largely apart from the colour of the surfaces. Judge them in two passes, not one (I).

- **The basic toolbox is four light types:** directional (global, one direction), ambient (global, all directions), spot (local, one direction) and point (local, all directions). Game lighting is openly a box of hacks, a permission to break physical correctness for readability (not checked at a source; stated here since September 2026, after a talk by Robert Yang at a GDC level-design workshop).
- **Three-point lighting (key, fill, rim) assumes control of the camera, which a fixed camera has.** The usual caveat in games is that a rim light is a rim light from one side only. **A fixed camera turns that into an advantage: a rim or back light placed for the one real camera stays a rim light, and lifts a hero prop off the background for free** (I). If the camera ever moves or rotates, the rim stops working, and the setup has to be worked out again without depending on the camera, with key and fill only.
- **Motivated and unmotivated light:** light justified by a visible fixture (a desk lamp, a neon sign, a rack's own glow) reads as world-building, while unmotivated light is a pure tool of attention. In a stylized scene a motivated source can do character work and direct attention in one prop: prefer it where one plausibly exists (I).
- **Mood is two dials:** high-key (bright, low contrast) reads cheerful and inviting, low-key (dark, high contrast) moody and tense, and warm against cool splits comfort and danger from calm and isolation. **Name the quadrant a room should sit in before you touch its lights,** so that a tuning pass has a target, not a feeling (I).
- **On mobile, much of the lighting can be authored as texture:** baked lightmaps and baked ambient occlusion for what does not move, probes for what does, and light baked into the albedo where a stylized look wants it (not checked at a source; stated here since September 2026). So the real decision is **which** light information bakes and which stays dynamic, and it blurs into material authoring on purpose.
- **Each room owns its key and fill lights:** the source project's case, and the check by a render toggled on and off, are in `unity.md`, "Materials and lighting".

## Mobile 3D performance QA (the scene-authoring side)

Scoped to a fixed camera with custom shaders and bloom, and checkable from the editor and from screenshots, with no device:

- **A ladder of levels of detail does nothing for a fixed camera,** which never changes its viewing distance. Do not import that item from generic mobile advice, and reopen the decision if a camera ever gains real changes of distance (I: the source project's earlier skill decided it for its three rooms).
- **Shared geometry and materials batch.** A prop that breaks a shared material without need, with its own texture where a shared one serves, costs a draw call for no visual gain: the palette rule applied to GPU state (I).
- **Cap stacked alpha-blended and glowing surfaces,** because overdraw costs on mobile (not checked at a source; stated here since September 2026). A budgeted hero effect is a deliberate exception; **a second glow layer added "for richness" is a rejection, not a preference.**
- **Hunt artifacts in every material or lighting pass:** normal seams at mirrored or duplicated geometry, specular popping when a camera or a light moves, and stretched textures on rescaled kit pieces. Each shows in a targeted sweep of screenshots (I).
