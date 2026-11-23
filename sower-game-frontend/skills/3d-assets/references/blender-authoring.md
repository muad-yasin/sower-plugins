# Blender authoring: the concrete workflow

*Open this file before you write or run a Blender script for an asset, and before any export or re-export. The engine side, import and rebind, is in `unity.md`.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence. The source project ran Blender 5.1.1 and Unity 6000.5 (Seen); a flag below that names no version is that project's.

## The shape of the pipeline

Three artifacts, and the split between them is the design (Seen, the source project's character pipeline):

| Artifact | Job |
|---|---|
| A committed generator script | Authors the mesh and the export armature: a plain script with no GUI state, deterministic and re-runnable |
| An editor-side rebinder | Binds an imported mesh onto the live rig's joints and assigns materials **by geometry** |
| The exported model files | Regenerable artifacts, not sources |

**The script is the asset.** Run it headless from the command line, and state its conventions at the top of the script, where the next person looks first: the axis convention, the measured proportions and the warning about material-slot order (I).

**Make a failed run show.** Put `--python-exit-code 1` before `--python <script>`: the flag sets the code Blender exits with when a script given on the command line raises an exception (D, the Blender 5.1 manual's command-line arguments, read 2026-11-12). The manual does not say what the exit code is without it, so a zero from a run without the flag proves nothing (I). **Every batch also prints one summary line per object: its name, its triangle count and the file written**, so a half-failed run cannot pass silently (I).

## The export call, and why each flag is there

The source project's call (Seen, its generator script, August 2026):

```python
bpy.ops.export_scene.fbx(
    filepath=path, use_selection=True,
    axis_forward='-Z', axis_up='Y', global_scale=1.0, apply_unit_scale=True,
    bake_space_transform=True, add_leaf_bones=False,
    object_types={'MESH', 'ARMATURE'}, mesh_smooth_type='FACE',
    use_mesh_modifiers=False,   # never apply the Armature modifier into the mesh
)
```

- **`bake_space_transform=True` with an armature goes against Blender's own warning**: "experimental option, use at own risk, known to be broken with armatures/animations", in the 5.1 and 5.3 API references alike (D, Blender Python API, `bpy.ops.export_scene.fbx`, read 2026-11-22). The source project's eight figures were exported with it and passed their recorded checks: joints identical to the old rig, no empty material slot (Seen, August 2026). Our reading of why it did no harm there: the rebind discards the imported bones, and the project plays no animation (I). A rig that keeps its bones or carries animation has neither excuse: prove the flag on one engine import, or leave it off.
- **The armature is exported although the engine side discards it**: without it the exporter emits no skin deformer at all, as the script's own note says (Seen). The rebind throws the imported copy away afterwards.
- **`use_mesh_modifiers=False` keeps the skin as a skin.** The script's own comment gives the reason: never apply the Armature modifier into the mesh (Seen). The API reference says the flag applies modifiers to mesh objects "except Armature ones" and warns that it "prevents exporting shape keys" (D, the same reference, read 2026-11-22).
- The script moves the armature to the origin for the export and restores it afterwards (Seen).
- **Never improvise this flag set per export.** Axis confusion is a named failure family (`llm-failure-modes.md`), and one fixed set is the structural counter (I).

## Before blaming the importer

The import settings are in `unity.md`, "Import and rebind". This file adds one check: **read the exported file before you blame the importer.** On the source project a correct export held a `Deformer`, a `Skin`, one `Cluster` per joint (14) and a `BindPose`, and the importer's setting was the fault (Seen).

## The rebind, step by step

1. Import the model file.
2. Run the rebinder against the target prefab or instance. It:
   - **discards the imported bones** and points the skinned renderer at the joints already in the live rig template;
   - recomputes the bindposes as `joint.worldToLocalMatrix * meshRoot.localToWorldMatrix` **at rest**;
   - assigns materials **by geometry**: shoes, trousers and shirt by vertical extent, then skin from hair by which reaches further down, since skin owns the hands.
3. Set the renderer's layer explicitly and read it back.
4. Set "update when offscreen" on (trap 4).
5. Capture from the target camera at the standard shape (`unity.md`, "The capture standard").

### Why the rebind exists

An imported armature comes back with **baked bone rotations**, a pelvis at +90 on X and a hip at 0/180/180, because Blender's bones point along their own axis and the exporter bakes that orientation into the local rotation. Where a project's poses are **absolute local rotations**, writing `hip.localRotation = Euler(-90,0,0)` onto a bone whose bind rotation is `(0,180,180)` does not flex a hip. **Discarding the imported bones is what let every measured offset and the ±5° shoulder splay survive a full mesh replacement byte-identical** (Seen).

## Four traps that will bite on the next re-export

1. **A mesh built with `Instantiate()` does not persist.** Bindposes live on the mesh, so the rebind needs its own copy, and an unsaved one comes back null after the next reload, as the first migration run showed. Bindposes depend only on the rest pose, which was the same for every character there, so **one shared, saved rebound-mesh asset per style serves them all.** Never write bindposes onto the imported mesh: a reimport reverts them without a word (Seen).
2. **Deleting mesh children does not delete their prefab overrides.** One scene stayed at 649,183 lines after a migration until **128,415 orphaned property modifications** were filtered out, which brought it to 111,323. Drop the entries whose target is null and write the list back; reverting the instance would have destroyed poses and materials (Seen).
3. **The default layer is a trap.** An imported model lands on layer 0, which the source project's main camera rendered while the room cameras culled it, so an unset character **vanished from its room and drew over the 2D interface** (Seen).
4. **"Update when offscreen" is required.** Local bounds bake from the bind pose, and the seated set rotates hips by -90 and knees by +90, so figures popped out at the frame's edges without it (Seen). Unity's own performance advice is to turn it off: `animation.md` has that collision.

## Driving bpy without stepping on the known traps

- **State the version before authoring**, the release and its Python API: models tend to recall older releases' names (not checked at a source; stated here since September 2026). Check recalled names against a committed script known to work on the installed binary, and on a crash **feed the real traceback into the next attempt** (I).
- **Build from `bpy.data`, not from operators.** An operator's poll fails where the API call would raise, its return value only says finished or cancelled, and a needed operator gets its context explicitly through `Context.temp_override` (D, Blender 5.1 API, "Gotchas: Using Operators" and `Context`, read 2026-10-05). Build meshes from data (`bmesh`, `from_pydata`); the export operator is the exception and gets its context deliberately.
- **In a live bridge session, save before anything destructive or batched.** Undo across bridge operations is unreliable (not checked at a source; stated here since September 2026), so reverting the file is the real rollback, and it only helps if the last save came before the mistake (I). **Name deletion targets exactly, never "the extras".**

## Standing constraints on the source project's figures

- **Weights are rigid, one bone per vertex at weight 1.0, and that is a decision** (Seen): the figures they replaced were already rigid, and it sidesteps the risk the pipeline plan ranked first, smooth weights collapsing at the 90° hip flex every seated figure holds. **Anything that needs real deformation is a new decision, not an implementation detail.**
- **The face is a texture that multiplies the skin tone**, not geometry: white texels change nothing, one image serves every skin tone, and the hands map to a blank corner (Seen). The marks sit higher on the skull than anatomy would put them, because both room cameras look down (Seen). Place marks for the camera, not for anatomy.
- **Argue about detail against the measured on-screen sizes**: 44 x 93 pixels in one room and 91 x 244 in another, with meshes of 1,420 to 1,480 triangles (Seen). Never argue from how a mesh looks in a DCC viewport.
- **A new character is a new mesh plus its material slots**, not a prefab variant: the variant route existed only while there were 19 renderers to override (Seen).

## A prop with no rig

Since 5 October 2026 the source project authors new props in Blender (Seen). Its earlier skill set out their shape in August, before any was built (I: the source project's earlier skill states the rule): no rig, so no rebind and an ordinary FBX import; the same committed script and axis flags; the animation type None; the layer set explicitly; the project's material recipe instead of Blender's materials; and the characters' measured size budget. Blender's warning on `bake_space_transform` names armatures and animations, so for a static mesh prove the flag on the first engine import (I). A prop moved to Blender widens the recorded line: ask first (`SKILL.md`, Step 0).
