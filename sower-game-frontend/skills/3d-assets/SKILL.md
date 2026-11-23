---
name: 3d-assets
description: Builds 3D geometry and motion for a game and gets it into the engine - which pipeline an asset belongs in (in-engine parametric shapes or a DCC such as Blender), the authoring loop, driving the DCC from an agent, import and rebind, budgets, third-party and generated models, and animation from first scoping to loop checks. Use when a task builds, rebuilds, re-exports or imports a mesh, prop, room, character or rig, when a new asset's pipeline is chosen, and when animation is scoped, proposed or attempted. Not for whether the result looks right (visual-craft, this skill's acceptance gate) or for screens and layout (ux-design, ui-implementation).
license: MIT
---

# 3D Assets

You own the **making**: which pipeline an asset belongs in, and the concrete steps of driving that pipeline. **You do not judge whether the result looks good:** that is `visual-craft`'s, whose mapping from world to screen is your input and whose capture review is your acceptance gate.

Read the project's own standing 3D reference (coordinate frames, layer and renderer tables, prop tables, measured traps) **before the first tool call, not after the first thing goes wrong.**

**Evidence and grades.** **Seen** = it happened on the source project (a Unity mobile game), with the record named in `references/evidence.md`. **D** = documented in a named source, read on the date given there. **I** = inferred, with the reason in the sentence. Open `references/evidence.md` before you quote a figure or an incident from this file. This skill does not claim that following it improves a project's results.

**This skill owns:** the pipeline choice, the authoring loop, the DCC script, import and rebind, budgets as checks, generated and downloaded models, and the mechanics of motion. **It hands off:** whether it looks right, and the camera's mapping of the world, to `visual-craft`; screens and layout to `ux-design` and `ui-implementation`; whether a feature should exist at all, an animation system included, to the planning skill and its scope gate.

## Step 0: pick the pipeline

| Asset | Pipeline | Why |
|---|---|---|
| Room shells, walls, floors, markers | **In-engine parametric geometry** (in Unity, ProBuilder or plain primitives) | Reliable, free and deterministic, and it edits in the session that places it |
| Props, furniture, racks, signage | **The line the project has recorded; where there is none, ask before the first one** | Either can carry them (I): parametric shapes edit in the placing session, and a DCC models what they cannot. The source project built its props in the engine, then moved new ones to the DCC in October 2026 on its owner's call and kept the rooms already built (Seen) |
| Characters and bodies | **A DCC (Blender), then rebound onto the live rig** | A body is the one organic object. On the source project characters built from engine cylinders failed five review rounds: two vertex rings can only make cone frusta, and a shoulder is a curve (Seen) |
| Anything new that is organic, curved or needs real topology | **The DCC, and say so when you propose it** | Moving a new class of asset to the DCC is a decision, not a drift |

**Do not move an existing asset across the line without asking.** "I could do this better in Blender" is a proposal, not a licence. Where the line sits is the project owner's recorded decision: read it, and its reasoning, before you widen it.

**Before authoring anything, check whether it already exists.** Duplicating a verified shape, then moving and recolouring it, beats new geometry; a new character is a new mesh plus its material slots on the **existing** rig, never a new rig.

## Step 1: the authoring loop

1. **Blockout first, detail second, as separate passes.** Place cheap placeholder shapes and verify scale, clearance and screen read against the **real** camera; only then build detail on a placement that is already correct. A later "make this look better" pass then never solves position again.
2. **Prefer shapes with a proven record in the current pipeline** over one that fits better on paper. Some primitives map exactly to their bounds and some do not; keep the project's shape findings written down (the Unity ones: `references/unity.md`, "Shape reliability, measured").
3. **Build one instance of a repeated prop, verify it, then duplicate.** Capture it alone (neighbours hidden) and at the real camera distance, and get it approved before you make twelve. A duplicate with a position-only change keeps mesh, scale and material identical; authoring each instance again does not.
4. **Settle the piece count per prop by looking, not by a rule.** A repeated prop pays its piece count once per instance; a one-off pays it once. On the source project a single console built with the racks' four pieces still read badly, a round pedestal with a flat panel perched on it, and needed seven (Seen).
5. **Assign a real material explicitly, every time, and copy an existing project material instead of creating one from the shader**, so the recipe is inherited instead of drifting. A fresh parametric shape carries no working default.
6. **Set the layer explicitly and read it back.** Where scenes share world coordinates and only the cameras' culling masks separate them, a piece on the wrong layer is invisible. **The signature: geometry that is provably present, active and in place, and provably not on screen. That is a layer, not a position**; stop chasing coordinates when you see that pair. Take the layer from a sibling *renderer*, never from a group root (Seen: three times in one room on the source project).
7. **Verify bounds, not transforms.** A container's own position often sits away from its visible mesh. Move an authored group **by its encapsulated bounds**, never by assigning the group's position, and check the bounds again after every move.
8. **Rotate a multi-piece group around a temporary pivot**, never with trigonometry worked out by hand: parent the group to an empty at its real centre, rotate the empty, move it to the target, and reparent back keeping world positions. It composes through every child's own offsets; hand-derived math does not.
9. **Author outside a live play session, then save, and read the console after every mesh or material call.** Edits made during play are discarded when it stops; the source project lost work this way four separate times (Seen).

## Step 2: DCC work, driven from an agent

- **Headless, for anything that ships.** A committed, re-runnable, deterministic script run from the command line. **The script is the asset; the scene file is not**, so a re-export is a diff, not an excavation.
- **Make a failed run show.** Pass `--python-exit-code 1` before `--python <script>`, so that Blender exits with that code when the script raises (D). The manual does not say what the exit code is without the flag, so a zero from such a run proves nothing. Every batch also prints one summary line per object (name, triangles, file written), so a half-failed run cannot pass silently.
- **A live GUI session, for exploration only.** Work out geometry there while you do not yet know what you are building, then fold the result back into the script. Whatever exists only in a running session is lost, the same failure as an edit made during play.

Before an export or a re-export, open `references/blender-authoring.md` and `references/unity.md`: the export and import mechanics, the rebind, and the traps of every re-export. Two rules bind here, both measured on the source project:

- **A rigged import is never left on the animation type none.** Set to none, the importer silently drops the skinning and makes a plain static mesh while **the file still holds the weights**, which makes it look like an exporter bug (Seen). Which type it takes is decided before the import: generic for a custom rig posed by its own local rotations, the source project's case (I); humanoid, with a configured Avatar, where clips are retargeted from one model to another (D). `references/animation.md` has the choice. Any option that "optimizes" game objects away stays off, or the bone objects the poses are set on are stripped.
- **A DCC's material-slot order is not the engine's submesh order.** Identify submeshes **by geometry** (vertical extent, size, position), never by authoring order: indexing by order once shipped a figure with a cream torso and red legs (Seen).

## Why every step ends in a check

Published benchmarks of models that write 3D code report, between them, that running code is easier to get than spatially correct code, and that tasks easy for people who use Blender stay hard for the systems tested (D: VoxelCodeBench, 3DCodeBench, BlenderGym). One finds models getting what an object is and its rough form right and its exact dimensions wrong (D: P3D-Bench). So **coordinates that are consistent inside the script are no evidence that the shape is right**, and having computed them is exactly what makes them feel trustworthy (I). That is why every step above ends in a check that can fail.

The named families (spatial precision, rotation, API drift between DCC versions, axis conventions, ambiguous destructive targets, node graphs, silently half-failed batches), each with its counter: `references/llm-failure-modes.md`. **Read it before a first DCC session or any batched build.**

## Budgets

**Decide a polygon budget against the asset's measured size on screen, never against how the mesh looks in a DCC viewport:** the right count is the lowest that keeps silhouette, shading and visible detail at the distance the player sees it from. Under the source project's fixed cameras a figure measured 44x93 pixels in one room and 91x244 in another, so each asset is authored to one measured size and LOD chains are a reasoned non-goal there (Seen). Every unique material is also a batch boundary, which makes "copy an existing material" a draw-call rule as much as a colour rule.

Open `references/budgets-and-craft.md` before authoring a new class of asset or judging a tooling proposal: the frame and triangle bands, texel density, decimation, the craft ladder, and how AAA and indie pipelines differ.

## Third-party and generated models

Marketplaces, asset libraries and text-to-3D generators are each one tool call away. **Settle four things before you generate or download anything:**

- **Licence and provenance.** A downloaded model brings real licence and attribution terms into a commercial release. That is the owner's call, every time.
- **Style match, the hard part.** An outside asset arrives with its own topology, UVs and material response, and a scene whose materials disagree on light response looks incoherent even when each colour is right.
- **Spend.** Where generation is paid, flag the cost before a batch.
- **The measured size on screen.** Detail nobody can resolve costs draw calls and memory and buys nothing.

**Price the cleanup up front.** Vendors' own cleanup guides describe raw generated meshes as dense many times over a game-ready budget, without edge flow, with overlapping faces, duplicate vertices, flipped normals and holes (I: second-hand, from a research report's quotes). For a character with a small triangle budget, decimation, retopology, new UVs and the rebind cost what the generator saved, so a scripted pipeline stays better for characters; a one-off static prop is where a generator can pay. Until a real test passes, generated output is **a starting point to retopologize or to work from, not a shipping asset**. A workable bar for that test: a riggable, correctly scaled asset inside the triangle budget after about fifteen minutes of cleanup (I: no generator has been tested against it).

## Animation

**Treat animation as unscoped until a feature asks for it.** How motion reaches a rebound rig is answered; whether the product wants an animation system, what motion is for and where clip data lives are decisions, not findings. **Do not close one by guessing.**

- **Motion here is time-varying absolute local rotations on named joints.** A generic clip binds each curve to an object by its transform path (D), so a clip and a small per-frame component that write the same local rotations onto the same named joints are two front-ends onto one backend: "clips or code" is a delivery choice, not an architectural fork (I).
- **For small figures, code is the default to beat.** David Rosen's GDC 2014 talk builds responsive character animation from a handful of keyframes with procedural techniques (D). It is an argument, not a decision.
- **At the size the source project's figures had on screen (44 by 93 pixels in one room), the least motion that reads is the right amount** (I): secondary motion nobody can see at that size is noise.

Open `references/animation.md` before animation is scoped, proposed or attempted: the binding mechanism and its one caveat, the two options that are wrong, mobile settings that need no device, the animation-specific weaknesses of models, and a **proposed** protocol for judging motion with a vision model, with the evidence for why that is hard.

## Verification: the pass or fail gate

- **A capture is the only ground truth.** Take it from the target camera at a named canvas shape, in play mode; in Unity, the recipe and its two limits: `references/unity.md`, "The capture standard".
- **"No console errors" is not "it is visible."** On the source project a signage wordmark sat fully behind its own backing panel through a build whose verification reported no errors (Seen).
- **Count what went in and what came out.** Count the objects, meshes and materials handed to the exporter and again in the re-imported file; a difference nobody can explain is a finding, because an export can finish and leave parts out (I).
- **Check the neighbours after any layout change.** Dressing placed relative to a grid outlives the grid: it does not error or move, it sits there looking deliberate (Seen). Ask "does this object still mean anything", not only "is it where I put it".
- Then hand it to `visual-craft` for the judgement of quality: more than one distance, the whole set side by side, every real state.

## Definition of done

- The pipeline is the settled one, or its extension was raised.
- The blockout was verified against the real camera before detail was built, and one instance before any duplication.
- Materials are copies of existing project materials, assigned explicitly; layers are set and read back; bounds were checked after every move.
- Every persistent edit was made outside a live play session and saved; the console is clean.
- A capture from the target camera exists **and was looked at**.
- The asset sits inside its budget (triangles, materials, size on screen), or the overage is stated.
- DCC work lives in the committed script, its run passed the exit-code flag, and the counts match after re-import.
- The standing 3D reference is updated wherever a table, a coordinate, a layer or a measured trap changed.

## Mistakes to flag

- New geometry where a verified shape could be duplicated and recoloured; an asset class moved across the pipeline line without raising it.
- Detail built before a placeholder pass confirmed the placement; a prop duplicated twelve times before one was verified.
- A container's transform read as "where the prop is"; a new piece's layer taken from a group root.
- A position chased when the symptom is "provably present and provably invisible".
- A material created from the shader instead of copied; a new unique material where an existing one could be shared.
- DCC work that lives only in a live GUI session; a headless run without the exit-code flag, or with no summary line per object.
- A rigged file imported with the wrong animation type; submeshes indexed by authoring order.
- A downloaded or generated model treated as shippable before licence, style, spend and size are settled.
- Any persistent edit made during a live play session; a prop called done on the strength of a clean console.
- A script's own coordinates trusted as verification.
- A destructive batch run without listing its targets by name first; a recalled DCC API used unpinned.
- LOD chains, trim sheets, node graphs or other AAA-scale infrastructure proposed without the criterion they would meet here.
- An animation pipeline built before a feature asks for animation; motion certified from a still capture, or from a vision model's read of frames without a diff of the loop's first and last frames.

## Engine layers

**Before you build or import an asset for an engine, open its file:** `references/unity.md` (the depth the source project was built with: parametric tooling, layers, bounds, import settings, the rebind, the capture standard), `references/web.md` (delivering 3D to a browser, thin and labelled so) or `references/unreal.md` (**not verified**, open questions only).
