# Animation: what is settled, what is open, and how to judge motion

*Open this file when animation is scoped, proposed, researched or attempted for the first time; when deciding whether a motion belongs in a DCC at all rather than in a shader, a tween or a static pose swap; and before judging any motion from a screenshot.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence. **Proposed** marks the protocol for judging motion: a synthesis nobody has validated.

## Read this first: the mechanism is settled, the scope is not

The source project has no animation: no clips and no animation controller anywhere, and its characters are static rigged meshes held in named sets of absolute local joint rotations, applied where they are used. "No animation system" is its standing rule (Seen, as of its character pipeline of August 2026).

How motion data reaches a rebound rig is answered below. Whether the product wants an animation system, what animation is for and where clip data would live are decisions, not findings: **the items under "Still OPEN" are open. Do not close one by guessing; propose it and get a decision.**

**The default until a case defeats it: what moves on the source project moves without an animation system.** Since August 2026 two small components and a set of time-driven shaders run every frame while one of its screens is open (Seen). None of it is an animation clip.

## SETTLED: how motion data reaches a rebound rig

**A generic clip binds each curve to an object by its transform path.** The binding's path is "the transform path of the object that is animated" (D, Unity 6000.6 scripting reference, `EditorCurveBinding.path`, read 2026-11-22), and a curve's path is "formatted similar to a pathname, e.g. "root/spine/leftArm"" (D, the same reference, `AnimationClip.SetCurve`, read 2026-11-22). That each curve then writes its joint's local value every frame is our reading of how the binding applies (I).

**No bindpose takes part in that path** (I): a mesh's bindposes belong to skinned deformation, apart from the curve data. So what looks like a landmine is avoidable by construction:

> **Never import the character file's animation. Author clips whose curve paths are the live rebound rig's own joint names, in that rig's own rest orientation.** The imported armature is then irrelevant to animation for the same reason the rebinder makes it irrelevant to skinning (I).

**The one real caveat, and the reason the naive route fails:** curves act in each joint's local frame, so the same local rotation values give a different pose when the authored skeleton's rest orientation differs from the target's (I). That is why an imported armature with baked bone rotations does not fit, and why authoring against the live hierarchy avoids it. **Rest orientation must match; nothing else about the rig has to.** Validate it with one test clip before building content on it (below).

This is what `SKILL.md` means by clips and code as two front-ends onto one backend: writing a named rotation set onto named joints and a clip writing local rotation onto the same joints are the same operation, per frame in the clip's case (I).

**Two options are wrong, not merely costly:**

- **Retargeting through a humanoid avatar.** Retargeting needs each model to use the Humanoid animation type with a configured Avatar (D, Unity 6000.6 manual, "Retarget humanoid animation", read 2026-11-22). A 14-joint custom rig has none, and forcing it through the Humanoid system adds a rest-pose remapping that fights a design built on absolute local rotations (I). **Generic, or legacy, is the animation type for such a rig** (I).
- **Changing the rebind to keep the imported bones so that clips "just work".** That brings back the baked-orientation problem the rebinder exists to remove, and would break the poses, offsets and shoulder splay that survived the source project's full mesh migration byte-identical (Seen for the migration; I for the consequence). It trades a solved problem for an unsolved one.

**Two paths are viable, and they share the backend:**

- **Generic clips against the live joint paths, built by a committed editor script**, so that the pipeline stays deterministic and diffable the way a mesh generator is (I). The fence: `AnimationClip.SetCurve` "will only work at runtime for legacy animation clips. For non-legacy AnimationClips it is an editor-only function" (D, Unity 6000.6 scripting reference, read 2026-11-22). A clip can play without a controller asset through the Playables API (not checked at a source; stated here since September 2026).
- **Joints driven from code**, which is how everything that moves on the source project already works (Seen).

**The cheap experiment before any content:** build one trivial clip in code, a head turning a few degrees, bind it by path, play it on a rebound character, and look for orientation artifacts. **Author no animation content before it passes**: a wrong rest orientation raises no error, it gives a figure that bends the wrong way (I).

## Two constraints that bound what is possible

- **Rigid weights, one bone per vertex at weight 1.0, chosen on purpose** (Seen; `blender-authoring.md`). For motion it means **no soft deformation at any joint: a bend is a hard hinge** (I). A shoulder or a waist that has to deform smoothly asks for a re-weight, which is a decision with its own risk, not a free upgrade.
- **The measured on-screen size**, 44 x 93 pixels in one room and 91 x 244 in another (Seen). Motion that cannot be seen at 44 pixels wide is not worth authoring, and the measurement that settled character detail settles animation ambition too (I).

## Still OPEN

1. **Clips or code: reframed, not decided.** Both are front-ends onto one backend, which removes the architectural fork but not the choice. The argument for code: David Rosen's "An Indie Approach to Procedural Animation" (Wolfire Games, GDC 2014 Animation Bootcamp) shows procedural techniques that make character animation responsive from a handful of keyframes, in three indie games (D, its GDC Vault session overview, session 1020583, read 2026-11-22). At small sizes that makes code the default to beat, **as an argument, not a decision** (I). What would flip it: many distinct, readable, character-specific performances rather than ambient motion, or characters drawn much larger on screen (I).
2. **What is animation for here?** Answer it before the others: a pipeline built before a use case is a solution shopping for a problem, and the question is one of scope before it is technical (I).
3. **Where does clip data live?** Narrower now: clips built in code put the data in a committed editor script rather than a scene or an export file, matching "the script is the asset". Nothing has tested it. If code wins item 1, the question goes away (I).
4. **Mobile cost is unmeasured on real hardware**, while the documented settings below cost nothing to apply (I).
5. **Prop and machine motion may want a different answer from character motion.** Shaders and per-frame components already drive the source project's machine-like effects, its coils and flares (Seen), and nothing suggests machinery needs a skeleton (I).

## Mobile settings that need no device pass

Each item is a setting or a documented cost, not a measurement, which is what makes it usable where a device pass is not on the table.

- **Bones.** Unity's manual gives no bone count for mobile. Its example: 15 bones added to a rig of 30 take Unity 50% more operations to solve in Generic mode (D, Unity 6000.6 manual, "Creating models for optimal performance", read 2026-11-22). The source project's rig has 14 joints (Seen).
- **One Skinned Mesh Renderer per character**: two in place of one "could roughly double the rendering time" (D, the same page).
- **Linear blend skinning with at most four influences per vertex** (D, the same page). The source project's rigid weights use one (Seen).
- **IK nodes are baked into FK on import**, and left in the model they still cost calculation: delete them, or keep IK and FK hierarchies apart while modelling (D, the same page).
- **If a controller is ever wired:** Unity's advice is the animator's Culling Mode at Cull Completely and the skinned mesh renderer's Update When Offscreen turned off (D, Unity 6000.6 manual, Mecanim Animation system, "Performance and optimization", read 2026-11-22). **That collides with the source project's rule**, which requires Update When Offscreen on every character, because local bounds bake from the bind pose and its seated set rotated hips by -90 and knees by +90, so figures popped out at the frame's edges (Seen). Flag the conflict and re-derive the bounds rather than taking the optimisation (I). The same goes for Optimize Game Objects, recommended in general and kept off there because it strips the bone objects poses are set on (Seen).
- **If clips ever ship:** Optimal compression lets Unity choose between keyframe reduction and a dense format, for Generic and Humanoid rigs; the error tolerances are an angle in degrees for rotation and a percentage for position and scale (D, Unity 6000.6 manual, the model import settings' Animation tab, read 2026-11-22). Pick the tolerances by looking at the clip at its real size (I).
- **`SkinnedMeshRenderer.BakeMesh`** "creates a snapshot" of the skinned mesh into a static mesh (D, Unity 6000.6 scripting reference, read 2026-11-22). A sequence of snapshots trades memory for the skinning work, which is worth knowing for a crowd of tiny figures with short motions (I).

## Animation craft: what better judgement looks like

- **Two books anchor the craft**: Thomas and Johnston's *The Illusion of Life*, with its twelve principles, and Richard Williams' *The Animator's Survival Kit* (not checked at a source; stated here since September 2026). Learn a few principles at a time on short exercises, not whole scenes (I).
- **A ladder of judgement** (I): a novice produces floaty, evenly spaced motion, over-animates, and has no feel for silhouette or staging; a competent animator handles weight, arcs, overlap and clean loops, and controls spacing through curve tangents in the graph editor rather than through poses alone; a master exercises restraint, with strong staging, silhouettes that read in motion, and economy.
- **Restraint is the band that matters at small sizes.** At 44 x 93 pixels master-tier judgement and the right engineering answer coincide: the least motion that reads, which is `SKILL.md`'s rule (I). A novice's instinct to add secondary motion is wrong here.
- **Game animation is not film animation.** Real-time constraints, blending, loops and mobile budgets decide it (I). **An idle loop lives or dies on its seam: the first and last frames must match**, and the defects to look for there are a popping shoulder, a jump in the fingers' curl and a sliding foot (I). A seated idle at a fixed camera would be a natural first motion on a project like the source one, and the seam is what would break it (I).
- **Graph-editor fluency is both the mark of skill and the largest risk for a model** (next section). That tension argues for code: there, curves become named easing functions that can be read, diffed and versioned, instead of tangent handles a model authors blind (I).

## Weaknesses of models specific to animation authoring

The general DCC failures of `llm-failure-modes.md`, version drift, spatial imprecision and ambiguous destructive targets, apply here unchanged; these are the additional angles. No study of a model authoring animation clips was read for this file.

- **Practitioners name animation and rigging as the weak spot.** Assessments of model-driven DCC work list animation and rigging, and animation curves and timing, among what fails or needs heavy human correction, and report rigged character animation with weights, constraints and IK as not realistic through a tool bridge today (not checked at a source; stated here since September 2026). That argues for a trivially simple first attempt, and for clips built in code over clips authored in a DCC (I).
- **A wrong but valid curve does not throw: it plays, badly.** A geometry error tends to show as an exception or a visibly wrong shape; a timing error shows as motion that no still frame can catch. **The difference is the gap in verification, not the error rate** (I).
- **The counter has the same shape as the geometry one: shrink what the model has to get right blind.** Named easing functions in code, or curves generated from a few stated parameters, are safer than hand-authored tangents (I). **Anything the model would tune by feel without seeing the result is wrong until verified.**

## Judging motion with a vision model: a proposed protocol

**Proposed**: a synthesis of documented model limits and of studio practice, not an established verification practice. Do not present it as settled.

This is the moving-picture sibling of `../../visual-craft/references/critique-and-vlm-qa.md`, whose findings concern still images: visual sycophancy, and a question's framing that changes how much the model looks at the image. Before sending frames to a model, open that file for its counters too, since every frame sent is a still image. **The failure here is a different one: reasoning over time.**

**The deficit is documented.**

- An analysis of video benchmarks finds questions that models answer without watching the video, and questions they answer as well with the frames shuffled, which it calls shuffling invariance (D, arXiv 2505.14321, "Breaking Down Video LLM Benchmarks", abstract read 2026-11-22).
- A stress-test benchmark of 12 video-language models found most of them below chance on probes that humans solve at 78 to 100% accuracy, and under assertive prompts a model's output barely changed between a real video and random noise (D, arXiv 2602.11244, REVEAL, version 2 of 16 September 2026, abstract read 2026-11-22).

**The consequence, and the point of this section: a vision model can describe a broken animation as fine, because it never registered the defect in time. That includes you**: a session looking at frames is the model described (I).

**The protocol: replace "is this good motion?" with frame-anchored checks a model can make.** It mirrors what studios do with playblasts, frame-accurate notes, side-by-side versions and rows of thumbnail poses (not checked at a source; stated here since September 2026):

- **A filmstrip, or contact sheet**: N evenly spaced frames tiled in order into one image, each labelled with its frame number. Ask about the progression of poses and the arcs, not about quality.
- **The first frame against the last, explicitly, for any loop.** A seam that pops reads as broken at any size, and the check reduces to whether two still images match, the kind of question the still-image counters are built for (I).
- **Curve-editor screenshots instead of rendered frames** where the question is spacing or easing: the model checks the curves' structure without having to perceive motion at all (I).
- **Discrete, checkable properties**: does the last pose match the first, does the silhouette read, does any joint flip or pop, do the feet sink or float, does the contact frame land where stated. **Never "does this look good".**
- **A person stays the final judge**: the documented deficit says a model misses defects in time that a person catches at once (I). This is a triage instrument, not a director.

It does not replace the existing rule: judge motion at real size, in Play Mode, from the target camera. A still-capture standard cannot certify motion: **say so rather than certifying an animation from a screenshot** (I).

## General principles that hold regardless

- **Author in the script, not in the session.** A live GUI session's state is lost, and an interactive bridge is for exploration whose result is folded back into a committed file. The same holds for a clip built in code: **the builder is the asset, the clip file the artifact** (I).
- **Bake before you export.** Unity bakes IK nodes into FK on import (D, above), and Blender's FBX exporter can bake animation so that the result looks as it does in Blender (D, Blender 5.3 manual, "FBX (Legacy)", read 2026-11-22). Do not expect a constraint or a driver to arrive as one: export baked keys (I). With clips built in code the question does not arise, one more argument for that route.
- **Anything exported from a DCC keeps the mesh's axis convention.** A clip exported under another convention than the mesh it drives is a certain mismatch (I).
- **Generic on import, for three reasons** (I): it is what surfaces clips at all; its "none" value is the one that drops skinning; and its binding by path is what makes the reconciliation above work. **For the character file, leave "import animation" off entirely** and never take clips from it.
- **Loop points are content, not a checkbox.** Check the first frame against the last explicitly, and prefer the diff above to an impression (I).
- **Deterministic re-authoring.** If running the builder again does not reproduce the same clip, the clip is not really under version control (I).

## Standing rules on the source project that bind this area

- **Poses are static rotation sets, and that is a written standing rule there** (Seen). Introducing an animation system reverses it, so the reversal is written down with its reasoning where the old rule lives, in the session it happens (I). Time-varying absolute local rotations on named joints continue the pose mechanism rather than replace it: a small per-frame component nudging joints is arguably no reversal, a full animation controller is one. **Say which one is being proposed** (I).
- **A new subsystem goes through the planning skill's scope gate first**, this one especially: no named use case, a real run-time cost on a mobile target, and it touches the one asset class already rebuilt from scratch once (I).
- **Device passes are the owner's to raise.** On the source project the owner ruled on 3 August 2026 that an agent never proposes one, in any form, not even as "a quick check on a real screen" (Seen). Whether that holds for your project is its owner's call; the mobile settings above let animation cost be handled from the documentation either way (I).

## Mistakes to flag

- Treating the items under "Still OPEN" as settled: the mechanism is settled, the scope is not.
- Building an animation pipeline before a feature asks for animation.
- Reaching for humanoid retargeting on a small custom rig: a wrong answer, not an option with a cost.
- Proposing to keep the imported rig bones so that clips "just work": that is the problem the rebinder exists to remove.
- Authoring animation content before one trivial test clip has played on the rebound rig without orientation artifacts.
- Importing animation from the character file at all.
- Reaching for an animation controller when a shader or a small per-frame component is what everything that moves already uses.
- Asking for smooth deformation without acknowledging that the rig is rigidly weighted by choice.
- Authoring motion finer than the measured on-screen size can show, or adding secondary motion at that size because an animator "should".
- Certifying an animation from a still capture, or from a vision model's read of frames without the check of the loop seam: the deficit in time is documented.
- Taking the advice to turn Update When Offscreen off without noticing that the project requires it on, for a recorded reason.
- Trusting recalled curve-API names without the version pinned: the version-drift rule applies with a worse failure signature, because a bad curve plays instead of throwing.
