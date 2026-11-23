# Unreal: not yet verified

*Open this file before you build 3D assets for an Unreal project. Nothing in it has been checked against a real Unreal project: it says what carries over from the Unity layer and lists the questions to answer the first time one is built.*

**Grades.** **I** = inferred, with the reason in the sentence. Everything below is a question unless it says I.

**What carries over, so that it is not worked out again:** the parts of this skill that are about authoring and about models, not about an engine (I): `llm-failure-modes.md`, the craft ladder and how AAA and indie pipelines differ in `budgets-and-craft.md`, the four questions of `SKILL.md`'s section on third-party and generated models, and the craft and checking sections of `animation.md`. **Only the mechanics below are unknown.**

## Open questions

**Pipeline choice**
- Are Unreal's in-engine modeling tools reliable enough to carry room shells, as parametric shapes did on the source project, or does everything go through a DCC?
- Does the question of shape reliability arise at all, or do the tools map to their bounds predictably?

**Import and rigging**
- What is the import contract for a rigged mesh, and is there a counterpart of Unity's trap where the wrong animation type drops the skinning while the file still holds the weights? Answer this one first: in Unity it fails without an error (I).
- **Is there a rebind problem at all?** The Unity layer rebinds because imported bone rotations do not fit a pose system of absolute local rotations. Unreal's skeleton asset and its retargeting may make this a non-question, or a different one.
- Does material-slot order survive import predictably, or does the rule of identifying submeshes by geometry apply here too?

**Scene organisation**
- What replaces layers under a camera culling mask for separating scenes that share world coordinates (sublevels, world partition, visibility channels), and what is its invisible-geometry signature?
- Is there a counterpart of "a container's transform is not where its mesh is"?

**Budgets**
- Where Nanite is available, how does it change the polygon budget, and is it available on the mobile targets you ship to? What are the triangle and draw-call limits there, and does the fixed-camera reasoning (author to one measured on-screen size, no LODs) survive?
- What is the batching model, and what breaks it? In Unity a `MaterialPropertyBlock` takes a renderer out of the SRP Batcher (`unity.md`).

**Verification**
- What is a reproducible capture recipe, and does it carry the limit the Unity harness has, of being no evidence about a post-processing pass?
- Do edits made during Play In Editor revert the way Unity's Play Mode edits do? If they do, the same failure class of a screenshot that lied exists.

**Animation**
- What are Unreal's counterparts of Unity's Generic and Humanoid import types, what is its binding model, and does the framing of clips and code as two front-ends onto one backend (`animation.md`) hold?
- Does the Control Rig and Animation Blueprint layer make the case for procedural code stronger or weaker at small on-screen sizes?
