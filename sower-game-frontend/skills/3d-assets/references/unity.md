# Unity: the 3D asset layer

*Open this file before you build, import or capture 3D assets in Unity through an editor bridge: the tools, the shape and transform findings, materials, layers, the import and rebind, Edit Mode, the capture standard and batching. It is the engine layer with the most records behind it.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence. Where each line comes from: `evidence.md`, its section on this file.

## The tools that drive this

On the source project the bridge offered a ProBuilder tool (shapes, poly shapes, mesh, vertex and face edits), a GameObject tool (create, duplicate, modify, reparent), material creation and renderer assignment, prefab and scene management, a camera tool for screenshots from a named camera, console reading, and a code-execution tool for whatever the typed tools do not cover (Seen).

**Batch the calls of a multi-piece build.** An 18-mesh rig went from more than 54 round trips to 3 batched calls (Seen), and a batch is also what makes a build re-runnable rather than a transcript (I).

## Shape reliability, measured

- **Cube, Cylinder, Sphere and Cone map exactly to their real bounds; Arch does not** (Seen). Where a dimension matters, avoid Arch, or read its bounds back and correct its scale.
- **Edge bevelling through the bridge has a normals bug**, dark diagonal streaks under real lighting (Seen). Sharp edges are a legitimate look.
- **Plain Unity primitives look the same as ProBuilder shapes for flat-coloured boxes** and avoid the pivot traps below; the source project's room shells use them (Seen). Since October 2026 it authors new props in Blender and keeps the shells it built (Seen). Where your project draws that line is its owner's recorded decision (`SKILL.md`, Step 0).
- Write your project's own findings down as they accumulate: each is an iteration somebody already paid for (I).

## Transform traps that each cost iterations

The rules are `SKILL.md`'s, Step 1, items 7 and 8; these are their Unity specifics.

- **The bounds to read are `MeshRenderer.bounds`.** On the source project two monitor containers sat away from their desk while only their children landed on it (Seen).
- **A `modify` call's `position` writes the local position, whatever its world-space flag says**, so under a parent it double-offsets. Set the position at creation and reparent, which keeps the world position (Seen).
- **A shape created with a position is centred on it**, and a later `modify` can move a fresh shape's pivot: stack pieces by their centres, and read the bounds back after the first `modify` (Seen).
- **The temporary pivot in Unity** is an empty GameObject at the group's real centre, read from a child's bounds, with the group reparented onto it with `worldPositionStays: true` and back again afterwards (Seen: used twice on 14 July 2026, each result checked by a live position query).

## Materials

**The recipe that a copied material inherits** (`SKILL.md`, Step 1, item 5): URP/Lit declares a smoothness of 0.5, while the source project's flat recipe is about 0.15 with no metal, because the default gave black specular streaks in a room with no skybox or reflection probe (Seen).

**Never build a `Color` from a parsed string inside an executed script.** On the source project a culture that did not read `.` as the decimal point turned `0.55` into `55`, and six new props rendered blown-out white (July 2026). The first screenshot after the batch showed it and a query of the stored values confirmed it; the fix wrote float literals, which removes the class instead of forcing a culture (Seen).

## Layers, and the invisible-geometry bug

The rule and its signature, a layer and not a position, are `SKILL.md`'s, Step 1, item 6. The case behind them: new rack pieces took their group's layer, which the room camera culled, while a property dump said all fifteen pieces existed, were active and sat in place; the record calls it the third instance of the trap in that room (Seen).

**An imported model lands on layer 0.** On the source project the main camera rendered that layer and the room cameras culled it, so an unset model vanished from its room and drew over the 2D interface (Seen).

## Import and rebind

The two import rules, the animation type and the material-slot order, are `SKILL.md`'s, Step 2. What this file adds:

- **The slot order as it arrived**: slots authored as Skin, Shirt, Pants, Shoes, Hair came into Unity as Shirt, Pants, Shoes, Skin, Hair, so the rebinder identifies submeshes by their vertical extent (Seen).
- **The rebind discards the imported bones**, points the `SkinnedMeshRenderer` at the joints already in the character template prefab, and recomputes the bindposes at rest. That is what makes a character change a mesh swap rather than a rig rewrite (Seen). Open `blender-authoring.md` before any re-export: the whole workflow and its four traps.
- **Set `updateWhenOffscreen = true` on a character whose pose leaves its bind-pose bounds**: trap 4 in `blender-authoring.md` (Seen).

## Edit Mode, always

Edits made during play are lost when it stops: `SKILL.md`, Step 1, item 9, from four losses on the source project by 1 August 2026 (Seen). **Read the console after every mesh or material call.**

Its sibling: **an editor-menu tool still runs when the project has compile errors**, on the last assembly that compiled, so it runs old code and reports normal success. The source project's glossary records four distinct ways it struck (Seen). Verify the output on disk, never the tool's own log line.

## The capture standard

**A capture is the ground truth, and its recipe is fixed** (Seen, the source project's capture standard, August 2026): enter Play Mode, go to the room, and render the room's own camera into a RenderTexture at the device resolution, 1080 by 1920 there, with the camera keeping its live `rect`. **Never `ScreenCapture`**: it captures the Editor window, so a room cut out of it comes at about a third of its real resolution (Seen).

**Call `ResetAspect()` after any sweep of `cam.aspect` and again right before a render**: an assigned aspect stays forced, a target texture does not clear it, and the render comes out stretched while every measured number stays right (Seen).

Two limits of that harness:

- **It is no evidence about a renderer feature or a post-processing pass.** It renders through a legacy immediate path that URP's own loop does not agree with: with a light-shafts feature on, the Game view showed a severe blowout while the harness capture looked clean (Seen, August 2026). Trust it for geometry, materials, lighting and vertex-shader animation, and check a screen-space effect against a real screenshot of the running game. **A weak reading from an unfaithful instrument is indistinguishable from a weak effect.**
- **One canvas shape is not enough when the capture judges an interface over the scene.** Before such a capture, open `../../ui-implementation/references/timing-and-verification.md`: its multi-shape capture assertions, in section 5.

## Batching

**A `MaterialPropertyBlock` takes a renderer out of the SRP Batcher** (D, Unity 6000.6 manual, "Check whether a GameObject is compatible with the SRP Batcher in URP", read 2026-11-22). On the source project a C# effect that set a block on each of 200 segments turned the 18 or so draw calls static batching had made of them into 200; with the wave moved into the vertex shader, the segments batched again (Seen).

GPU instancing does not combine with the SRP Batcher; for many identical meshes with one material, the manual says it can be the more efficient (D, Unity 6000.6 manual, "Remove SRP Batcher compatibility for GameObjects in URP", read 2026-11-22).

## Third-party and generated models

The source project's toolchain carried marketplace search and download tools and generators that make a model from text or an image, and no model in its build came from any of them, as its earlier skill recorded in August 2026 (Seen). The four things to settle first are in `SKILL.md`'s section on third-party and generated models.
