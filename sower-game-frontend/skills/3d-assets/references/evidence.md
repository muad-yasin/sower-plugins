# Evidence for 3d-assets (dated)

*Read this file before a figure or an incident from `SKILL.md` or one of its reference files is relied on or quoted. It says where each rule and line comes from, so that whoever maintains the skill can tell when one may go. Engines and tools change: read the page again before you rely on a version-bound line.*

**Grades.** **Seen** = it happened on the source project, a Unity mobile game whose browser build went out as a public playtest in October 2026, and whose records and earlier skills this skill was written from: an incident, a measurement or a decision, with its record named. An earlier skill counts as the record of a case it names. "Shipped" in a note is that project's own word: the change was in the game's committed build. **D** = documented in a named source, read on the date given. Several D rows rest on our research report of 2026-08-26, which quoted its sources; those sources were not read again for this file, and the row says so. **I** = inferred; the row says from what. A rule that an earlier skill states without naming a case is graded I, and a figure an earlier skill gives for how well a method worked is not kept without the record of its measurement. **The old file's statement** = an outside fact kept from the file as it stood before November 2026 and not read again: the line says "not checked at a source" and keeps no figure. **Proposed** = a synthesis nobody has validated; "(questions)" marks lines that ask rather than claim. Nothing here was measured: no project was built with and without a rule.

## Sources read for the reference files

| Source | Read | What was read |
|---|---|---|
| Unity manual 6000.6, "Creating models for optimal performance" (docs.unity.com) | 2026-11-22, the raw page by script | no polygon band; the bone example; one skinned renderer per character; four influences per vertex; IK baked into FK on import |
| Unity manual 2022.3, "Modeling characters for optimal performance" (docs.unity3d.com/2022.3) | 2026-11-22, the raw page by script | whether an older version carried a polygon band: it does not |
| Unity manual 6000.6: the model import settings' Animation tab; the Mecanim Animation system's "Performance and optimization"; "Retarget humanoid animation"; "Check whether a GameObject is compatible with the SRP Batcher in URP"; "Remove SRP Batcher compatibility for GameObjects in URP" | 2026-11-22, the raw pages by script | compression and its tolerances; culling and Update When Offscreen; the Humanoid type and Avatar; the MaterialPropertyBlock requirement; instancing against the batcher |
| Unity scripting reference 6000.6: `EditorCurveBinding.path`, `AnimationClip.SetCurve`, `SkinnedMeshRenderer.BakeMesh` | 2026-11-22, the raw pages by script | the transform path; the pathname format and the run-time fence; the snapshot |
| Unity, "Best practices for profiling game performance" (unity.com/how-to) | 2026-11-22, the raw page by script | the idle time of about 35% and the two frame budgets |
| Blender Python API 5.1 and 5.3, `bpy.ops.export_scene` (docs.blender.org/api) | 2026-11-22, the raw pages by script | `bake_space_transform`'s warning and `use_mesh_modifiers`, the same in both versions |
| Blender 5.3 manual: "FBX", "FBX (Legacy)" and "Decimate Modifier" (docs.blender.org/manual) | 2026-11-22, the raw pages by script | export through the add-on; its axes and what it bakes; the three decimation modes and Planar's delimits |
| P3D-Bench (arXiv 2606.11152, version 4) and 3D-PreMise (arXiv 2401.06437) | 2026-11-22, their HTML texts by script | P3D-Bench's summary of findings; 3D-PreMise's error analysis with its setup and its program-level findings |
| arXiv 2505.14321, 2602.11244, 2603.26779, 2606.01057 (3DCodeBench) and 2504.01786 (BlenderGym) | 2026-11-22, the abstract pages by script | the abstracts |
| GDC Vault session pages 1022323 and 1025557 | 2026-11-22, the raw pages by script | title, company, year and overview |
| Khronos, "glTF" (khronos.org/gltf); Epic, Unreal Engine 5.9 documentation, "Pixel Streaming in Unreal Engine" | 2026-11-22, the raw pages by script | the format's description; what Pixel Streaming does |
| The Blender 5.1 manual's command-line arguments; the Blender 5.1 API's "Gotchas: Using Operators" and `Context` | 2026-11-12 and 2026-10-05, in earlier research rounds of ours | not read again for these files |

## Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Characters in a DCC | Seen | the source project, 2026-08-03: the owner moved characters to Blender after characters built from engine cylinders had failed five review rounds; every cylinder on the old rig had exactly two vertex rings, so a deformer could only make cone frusta |
| Room shells in parametric shapes; props on the recorded line, or ask | Seen, I | the source project, 2026-10-05: the owner reopened the August carve-out, and new props for three rooms are authored in Blender while the room shells already built stay as they are (the project's pipeline document). That either pipeline can carry props is this file's reading |
| A carve-out is a recorded decision; read it before widening it | Seen | the decisions of 2026-08-03 and 2026-10-05, each recorded as the owner's own call in the project's pipeline document |
| A new character is a new mesh on the existing rig | Seen | the source project: one skinned renderer per figure, bound to the joints of an existing character template |
| Blockout first; one instance before duplicates | I | the source project's earlier asset skill states the rule |
| Prefer shapes with a proven record | Seen | the source project's pipeline document records the shape findings, July 2026: Cube, Cylinder, Sphere and Cone exact to their bounds, Arch not, bevelling's normals bug; they are kept in `references/unity.md` |
| Piece count settled per prop | Seen | the source project, July 2026: a single console, first rebuilt with the racks' four pieces, still read badly (a round pedestal with a flat panel on top) and was rebuilt with seven on 14 July; the racks' ceiling had come from their twelve copies |
| Copy an existing material; a fresh shape has no working default | Seen | the source project: a shader's default smoothness gave black specular streaks in a room with no skybox, so its flat recipe sets low smoothness and no metal explicitly, and a new prop copies an existing material |
| The layer set and read back, taken from a sibling renderer | Seen | the source project: new rack pieces took their group's default layer, which the room camera culled, while a property dump said all fifteen pieces existed, were active and sat in place. The record calls it the third instance of the trap in that room |
| Bounds, not transforms; the temporary pivot | Seen | the source project, July 2026: its pipeline document records the temporary pivot, placed at a group's real centre read from a child's bounds because the containers had arbitrary origins, and used twice on 14 July 2026, in two rounds of that day, each result checked by a live position query |
| Edits made during play are lost | Seen | the source project: work lost this way four separate times, as a plan of 1 August 2026 records |
| The headless script is the asset | Seen | the source project's committed generator script for its characters |
| `--python-exit-code 1`, placed before `--python` | D | the Blender 5.1 manual's command-line entries (the flag takes the exit code to use; arguments run in the order given), read on 2026-11-12 in an earlier research round of ours; not read again for this file |
| One summary line per object | I | the old file's rule: a headless run that half-fails can exit 0 and pass |
| A rigged import is never left on the type none; which type it takes is a choice | Seen, D, I | the source project, August 2026: with the type set to none, a skinned export imported as a plain static mesh although the file, checked first, held the weights. An earlier note, measured on an export without skin, had said the opposite. The choice between generic and humanoid is `references/animation.md`'s, with Unity's retargeting page behind the humanoid half |
| Material-slot order is not submesh order | Seen | the source project: indexing by authoring order once gave a figure a cream torso and red legs |
| What the benchmarks report | D | VoxelCodeBench (arXiv 2604.02580), 3DCodeBench (arXiv 2606.01057) and BlenderGym (arXiv 2504.01786): their abstracts, read on 2026-10-05 in an earlier research round of ours, report between them that running code is easier for the models tested than spatially correct code, and that systems combining vision and language struggle with tasks that are easy for people who use Blender; that round recorded the findings together, not paper by paper. P3D-Bench (arXiv 2606.11152): the abstract of version 4 (revised 14 October 2026), read on 2026-11-22, reports models that capture what an object is and its rough form while missing the exact dimensions the input asks for |
| Consistent coordinates are no evidence of the shape | I | from the findings above |
| A polygon budget against measured size; no LOD chains under a fixed camera | Seen | the source project measured a figure at 44x93 pixels in one room (the camera's elevation foreshortens it) and 91x244 in another, with meshes of 1,420 to 1,480 triangles |
| A unique material is a batch boundary | I | the source project's earlier skill states the rule; the batching facts are in `references/unity.md`, sourced there to Unity's manual and to the source project's effect |
| Licence, style, spend and size before any outside model | Seen | the source project's toolchain carried 3D marketplace and generator tools, and no 3D model it shipped came from them, as its earlier skill records; the four questions are that skill's |
| Generated meshes: their topology | I | second-hand: our research report of 2026-08-26 quotes two vendors' cleanup guides on how far raw generated meshes exceed a game-ready triangle count. The guides were not read, so no count is used, here or in the skill |
| The test bar for a generator (about fifteen minutes of cleanup) | I | the earlier skill's bar; no generator has been tested against it |
| Animation unscoped until a feature asks | Seen | the source project had shipped no animation when its earlier skill was written, and its research report of August 2026 left the scope questions open |
| A clip binds each curve by transform path | D | Unity's scripting reference, `EditorCurveBinding.path` (version 6000.6), read on 2026-11-22: the field is the transform path of the animated object |
| Clips and code as two front-ends onto one backend | I | from the binding above and the source project's pose system, which writes absolute local rotations onto named joints |
| Fluid character animation from very few keyframes | D | David Rosen (Wolfire Games), "An Indie Approach to Procedural Animation", GDC 2014 Animation Bootcamp, GDC Vault session 1020583: its session overview, read on 2026-11-22, describes procedural techniques that make character animation responsive from a handful of keyframes, shown in three indie games (Overgrowth, Receiver, Black Shades) |
| The least motion that reads | I | from the measured sizes above |
| A capture is the ground truth; its recipe | Seen | the source project's capture standard in its pipeline document, August 2026, as `references/unity.md` states it in "The capture standard" |
| A clean console is not "visible" | Seen | the source project: a signage wordmark sat behind its panel's front face and never showed in the build, while that session's verification reported zero console errors |
| Count what went in and what came out | I | a practice of a public skills repository (htdt/godogen) read in our research round of 2026-11-11 and 2026-11-12; carrying it to every export is our inference |
| Check the neighbours after a layout change | Seen | the source project's pipeline document: dressing placed relative to a grid outlived the grid |

## Retired in November 2026

| Line | Why it went |
|---|---|
| "this is the most repeated invisible-geometry bug there is" | a claim beyond the record, which counts three instances in one room |
| "hit at least four separate times on one project, including twice inside single sessions" | the record counts four; "twice inside single sessions" was not found |
| "the carve-out itself, where it exists, is usually a recorded override of two written rules" | one project's case stated as a usual pattern |
| P3D-Bench's "~0.8 on semantic alignment but only ~0.35 on geometric" | an earlier version's figures: the paper's fourth version, read in full, gives about 0.7 and about 0.5, as `references/llm-failure-modes.md` now states |
| "3D-PreMise found spatial-precision errors the most frequent class" | left to the reference, which now gives it with its setup from the paper's full text |
| "a documented claim rather than self-deprecation"; "the dominant measured error class" | claims beyond the sources read |
| "the mandatory decimate-retopo-re-UV-rebind pass erases the generator's entire speed advantage" | "entire" had no measure behind it; the cost argument stays |
| "the strongest published solo-dev precedent" | a superlative nobody measured |
| "Still the top animation item" | a ranking with no basis |
| "only 13 keyframes in total" for the talk | the session's overview gives no number; the figure was the research report's |
| The counts of generated triangles in the main file | second-hand; the cleanup guides were not read |
| "You, the agent driving these pipelines, are the least reliable component in them" | a comparison no benchmark made; the section is now "Why every step ends in a check" |
| The heading "Mistakes to actively flag" | now "Mistakes to flag", as in the other skills |
| "A rigged import needs the generic animation type (not humanoid, not none)" | the record shows what the type none loses; generic is the source project's rig, and retargeting clips between models needs the humanoid type (an outside review of this repository, November 2026) |
| "Generation is usually paid" | a frequency with no record; the rule is the condition |

## references/unity.md

| Line | Grade | Behind it |
|---|---|---|
| The bridge's tools; an 18-mesh rig from more than 54 round trips to 3 | Seen | the source project's pipeline document; a later line of the same document counts 19 meshes for the figures that rig built |
| Cube, Cylinder, Sphere and Cone exact; Arch not; bevelling's normals bug | Seen | the pipeline document's shape findings, July 2026 |
| Plain primitives for the room shells; new props in Blender since October 2026 | Seen | the pipeline document, July 2026 and its entry of 2026-10-05 |
| Bounds over a container's position; `modify` writes the local position; a created shape is centred on its position; a pivot that moves | Seen | the pipeline document, July 2026: monitor containers whose children alone sat on the desk; a cylinder centred on its creation position |
| The temporary pivot | Seen | the pipeline document: used twice on 14 July 2026, each result checked by a live position query |
| The material recipe | Seen | the pipeline document: URP/Lit declares 0.5, the recipe sets 0.15 |
| The culture bug | Seen | the milestone history, 13 July 2026: six props white, seen in the first screenshot after the batch, confirmed by a value query, fixed with literals |
| The layer case; layer 0 on import | Seen | the pipeline document: the third instance in one room, fifteen pieces present and invisible; the character pipeline, August 2026 |
| The slot order as it arrived; the rebind; Update When Offscreen | Seen | the pipeline document, August 2026 |
| Work lost in Play Mode four times | Seen | a plan of 1 August 2026 |
| Editor-menu tools run old code | Seen | the source project's glossary: four distinct ways |
| The capture recipe; `ScreenCapture`; `ResetAspect()`; the harness and renderer features | Seen | the pipeline document's capture standard, August 2026, including its finding of 3 August 2026 on a light-shafts feature |
| A `MaterialPropertyBlock` and the SRP Batcher; instancing against the batcher | D | the two Unity manual pages named in the lines |
| The 200 segments and about 18 draw calls | Seen | the pipeline document's section on the effect, August 2026 |
| Marketplaces and generators unused | Seen | the earlier asset skill, August 2026 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "the single most-repeated invisible-geometry bug (three separate instances in one room alone)" | a ranking beyond the record, which calls it the third instance in one room |
| "the most-recurring trap on one project, hit at least four separate times including twice inside single sessions" | the record counts four; the rest was not found |
| "shipped six blown-out white props - and the stored values looked plausible on paper, so only a screenshot caught it" | the record: the first screenshot after the batch showed it, a value query confirmed it, and float literals fixed it |
| "The SRP Batcher is the first-line win under URP" | a ranking; the manual's requirement and its note on instancing replace it |

## references/unreal.md

| Line | Grade | Behind it |
|---|---|---|
| What carries over | I | this file's reading of which parts of the skill do not depend on an engine |
| The open questions | (questions) | the Unity layer's findings, each asked of Unreal |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "carry the room/prop half of the carve-out" | the source project moved new props to Blender in October 2026; the question now asks about room shells |
| "That failure is the most expensive one in the Unity layer and its Unreal shape is the highest-value first answer" | a ranking nobody measured; the question still comes first, for its silent failure |
| "Nanite changes the poly-budget conversation fundamentally on capable hardware, and is differently available on mobile" | a claim with no source in a file of questions; now a question |
| "Generic-vs-humanoid has no obvious Unreal counterpart" | a claim; now a question |

## references/web.md

| Line | Grade | Behind it |
|---|---|---|
| The browser build as a public playtest in October 2026; no glTF pipeline | Seen | the source project's notes on its web build |
| glTF's description; FBX's | D | the Khronos page and the Blender manual named in the line |
| Draco and KTX2; a browser tab's memory and Safari | the old file's statement | not read again; no figure kept |
| Pixel Streaming | D | Epic's page named in the line |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "We have not shipped 3D content to a browser" | the browser build went out as a public playtest in October 2026 |
| "iOS Safari enforces a WebGL heap limit in roughly the 300-500 MB range", with its link to a practitioner's blog | one practitioner's figure, not read again |
| "they trade CPU decode time for bytes. *Inference, not measured by us:* on a low-end phone that trade is not always favourable" | kept as an inference, without the claim that Draco and KTX2 are "the two levers" |

## references/blender-authoring.md

| Line | Grade | Behind it |
|---|---|---|
| The three artifacts; the script is the asset | Seen | the source project's character pipeline, August 2026 |
| Blender 5.1.1 and Unity 6000.5 | Seen | the pipeline plan of August 2026 |
| `--python-exit-code 1` before `--python` | D | the Blender 5.1 manual's command-line arguments, in an earlier research round of ours; not read again |
| The export call and its flags; the armature moved to the origin | Seen | the generator script, August 2026 |
| `bake_space_transform`'s warning; `use_mesh_modifiers` | D | Blender's Python API reference, 5.1 and 5.3 |
| The eight figures passed with that flag | Seen | the milestone history of 3 August 2026, written in the same commit as the script's export call: joints identical to the old rig, no empty material slot |
| Why the flag did no harm there | I | the rebind discards the imported bones, and no animation plays |
| Without the armature the exporter emits no skin deformer | Seen | the generator script's own note on its export function |
| The markers in a correct export, 14 clusters | Seen | the pipeline document and the milestone history, August 2026 |
| The rebind and its reason; the ±5° splay | Seen | the pipeline document |
| The four traps: 649,183, 128,415 and 111,323 lines; layer 0; Update When Offscreen | Seen | the pipeline document's character pipeline |
| Older releases' names in recall; undo across a bridge | the old file's statement | not read again |
| Operators, their poll and `Context.temp_override` | D | the Blender 5.1 API pages named in the line, in an earlier research round of ours |
| Rigid weights; the face texture; the sizes; a new mesh, not a variant | Seen | the pipeline document |
| A prop with no rig | Seen, I | the pipeline document's entry of 2026-10-05; the earlier asset skill, August 2026, for the shape |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "read its module docstring first" | the reader has no such script; the rule is now to state the conventions at the top of one |
| "Recall defaults to ~2.9x-era conventions" | a version figure from a practitioner's log, not read again |
| "`bpy.context.temp_override(...)` on 4.x+" | a version claim not read; the 5.1 API's name kept |
| "(built X, exported Y, N verts)" | the main file's fields now: name, triangles, file written |
| "Sanity-check the exported file before blaming the importer. A correct one greps for ... (one per joint)" as a general claim | kept as the source project's export; whether binary files can be searched this way in general was not verified |

## references/llm-failure-modes.md

| Line | Grade | Behind it |
|---|---|---|
| P3D-Bench; 3D-PreMise | D | the passages named in the lines |
| 3DCodeBench; BlenderGym | D | their abstracts, as named in the lines |
| The rotation paper | D | its abstract, as named in the line |
| Blender's axes | D | the Blender 5.3 manual named in the line |
| Version drift; destructive targets; undo; node graphs | the old file's statement | not read again |
| Each family's counter | I | as each line says |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Academic benchmarks ... and practitioner logs of LLM-driven DCC work converge on one pattern" | each benchmark now gives its own finding |
| P3D-Bench's "~0.8" and "~0.35" | an earlier version's figures; version 4 gives about 0.7 and about 0.5 |
| "CodeGen-3D" | no paper id given, none found |
| "This is the dominant measured error class" | 3D-PreMise reports the most frequent category in its own analysis of one model, not a dominance measured across studies |
| "The most common DCC-side first-run failure" | a ranking nobody measured |
| "3DCodeBench found traceback feedback a clean, capacity-independent win" | the abstract credits test-time scaling, higher thinking budgets and multi-turn refinement; "capacity-independent" is not in it |
| "One practitioner log reports version-pinning cutting first-run errors from ~40% to ~5%" | an informal estimate from a source not read again |
| "Spatial reasoning does not improve with more thinking"; "Frontier models fail to simulate rotation even when handed an external rotation tool" | the rotation paper's own result replaces both; it did not test more thinking, and 3DCodeBench found higher thinking budgets to help |
| "the classic FBX failure" | a frequency claim |
| "the documented ambiguous-target error" | not documented in what was read |

## references/budgets-and-craft.md

| Line | Grade | Behind it |
|---|---|---|
| The frame budget | D | Unity's profiling guide named in the line |
| No polygon band from Unity | D | the 6000.6 page named in the line, and the 2022.3 page, which has none either |
| The measured band, 1,420 to 1,480 triangles at 44 x 93 and 91 x 244 pixels | Seen | the pipeline document and the milestone history, August 2026 |
| Spending the band; tripwires; texel density | I | as each line says |
| The Decimate modifier's modes | D | the Blender 5.3 manual named in the line |
| How to use each mode | I | from the modes |
| No LODs under a fixed camera; the decision reopens with a moving camera | Seen | the sizes measured; the decision, its reason and its condition recorded in the earlier asset skill |
| The craft ladder | the old file's statement, I | the career-ladder sources not read again; the reading is ours, the cases Seen |
| *Sunset Overdrive*; *Far Cry 5* | D | their GDC Vault session pages |
| Applying modifiers at export | D | the Blender FBX page named in the line |
| Node graphs changing between versions | the old file's statement | not read again |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "the frame budget and the per-mesh triangle band are the engine vendor's own mobile guidance"; "the mobile band is 300-1,500 tris per mesh" | the band is on neither Unity's current page nor its 2022.3 page |
| "but mobile has no active cooling" | the guide's own reason is that the chips need time to cool |
| "Scene-level tripwires: ~100k tris on screen, <100 draw calls" | a practitioner guide's figures, not read |
| "Draw calls are the real mobile bottleneck"; "Mobile GPUs are bandwidth-bound" | claims not read at a source |
| "~512 px/m is the mobile baseline consensus, hero assets up to ~1,024"; "Keep any atlas <=2048x2048" | figures from sources not read again |
| "Planar mode (2-3° threshold)"; "Collapse (start ratio 0.5, symmetry on)"; "merge-by-distance (0.0001)" | starting values from a source not read again; the manual's modes replace them |
| "decimation is fast but blind - it knows nothing about UV islands, material boundaries or silhouette edges" | the manual's Planar mode can keep material borders, seams and UV edges |
| "treat the structure as consensus and the year-counts as noise; the strongest primary sources are the GDC Technical Artist Bootcamp talks and the Volition technical-artist essay" | a consensus and a ranking not checked |
| "a ~1,400x2,400 m city with 8-12 environment artists" | not on the session page |
| "Houdini plus its engine bridge"; "*Far Cry 5*'s map built itself every night" | the session page names no tool and says the terrain changed every day |

## references/animation.md

| Line | Grade | Behind it |
|---|---|---|
| No animation on the source project; the standing rule | Seen | its pipeline document (August 2026) and its task archive (no character driven by an animator, July 2026) |
| What moves, moves without an animation system | Seen | the pipeline document, August 2026 |
| The binding by transform path; the pathname format | D | the Unity scripting reference pages named in the line |
| Each curve writes its joint's local value; no bindpose in the path; the rest-orientation caveat | I | from the binding and from curves acting in each joint's local frame |
| The humanoid route is wrong for the rig | D, I | Unity's retargeting page named in the line; the rest is our reading |
| Keeping the imported bones is wrong | Seen, I | the migration's byte-identical joints; the consequence is our reading |
| `SetCurve`'s run-time fence | D | the scripting reference named in the line |
| Playing a clip without a controller | the old file's statement | not read again |
| The test clip | I | the old file's proposal |
| Rigid weights; the measured sizes | Seen | the pipeline document |
| Item 1 of "Still OPEN" | D | Rosen's session overview, also behind the main file |
| The mobile settings | D, Seen | the Unity pages named in the lines; the collision with the source project's rules, its pipeline document |
| The craft canon; the practitioners on animation and rigging; studio practice | the old file's statement | not read again |
| The ladder, the seam, restraint, the counters | I | as each line says |
| The two video-model papers | D | their abstracts, as named in the lines |
| The protocol | Proposed | a synthesis nobody has validated |
| Baking before export | D, I | Unity's character page and Blender's FBX page; the rest is our reading |
| Device passes | Seen | the source project's standing rules: the owner's call of 3 August 2026 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| The grade scheme *Strong*, *Consensus*, *Inferential*, *Proposed* | the skill's grades now; *Proposed* kept for the protocol |
| "The reference project has shipped zero animation" | worded to the records, with their date |
| "The research independently reached the same conclusion for figures at the measured on-screen sizes" | the research report is neither a record nor a source here |
| "stores ABSOLUTE LOCAL values that overwrite the joint every frame", graded strong | the reference documents the path; the overwrite is our reading |
| "formatted like a pathname" for the binding's path | the pathname format is on `SetCurve`'s page |
| "Retargeting requires a humanoid bone set with a configured avatar in a T-stance" | the manual names the Humanoid type and a configured Avatar, no T-stance |
| "roughly 13 keyframes total across three games"; "the strongest published solo-dev precedent there is" | retired in the main file too |
| "Unchanged and still the most important open item" | a ranking; the question is asked first |
| "desktop rigs at 15-60 bones ... below thirty for mobile"; "Cost scales roughly linearly" | not on Unity's current page |
| "set culling mode to based on renderers" | the manual's advice is Cull Completely |
| "One bone per vertex is the cheapest skinning tier" | not on the page read |
| "Default keyframe reduction at 0.5° rotation / 0.5% position error roughly halves size"; "17 KB optimal vs 43.6 KB" | not on the page; the source of the walk figure was never named |
| "casual/mobile idles are short (2-4s)"; "short 10-30s exercises" | figures from sources not read again |
| "A seated idle at a fixed camera is the most likely first motion" | a frequency claim |
| "There is essentially no published study of an LLM authoring clip data" | an absence nobody checked; the file now says what was read |
| "what reliably fails or needs heavy human correction" | the frequency word |
| Text-to-motion research's "catastrophic neglect" | no paper named |
| "remarkably stable" scores; "humans hit ~95% while a frontier model collapses to ~30%"; "56.2% spatial to 2.8% temporal"; FPS-Bench's figures | not in the abstracts read; FPS-Bench was given no id |
| "the defect that most reliably reads as broken"; "a comparison the static-image evidence says models are genuinely good at" | a ranking, and a claim the evidence read does not make |
| "Still the top item" | a ranking with no basis |
| The heading "Mistakes to actively flag" | now "Mistakes to flag" |
