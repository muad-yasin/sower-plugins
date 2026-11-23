# Unreal: not yet verified

*Open this file before you judge visuals in an Unreal project. Nothing in it has been checked against a real Unreal project: it lists the questions the Unity layer answers, so that they are answered here the first time one is built. The craft that does not depend on an engine (value before colour, focal hierarchy, Gestalt staging, the critique ritual, the vision-model protocol, the contrast formula) is in `SKILL.md` and its other references, and applies as written: only the engine mechanics below are unknown.*

## Open questions

**Colour and material**
- What colour space does the default renderer work in? Does the Unity correction apply, where a light colour at a low alpha over a dark surface shows brighter than its stored value, or a different one? Answer this first: every contrast check and every import of a mockup depends on it.
- What is the counterpart of "copy an existing material instead of creating one from the shader"? Which parameters does the engine's material model expose to a variant, and what stops a one-off variant from drifting away from its family?
- Is there a counterpart, in the tint model of Unreal's interface widgets, of the defect where a baked sprite is multiplied by a colour set at runtime?

**Scene separation and visibility**
- In Unity a new piece on the wrong layer is invisible under camera culling. What is the counterpart in Unreal (sublevels, world partition, the visibility settings of actors), and what is *its* signature of "provably present and provably not on screen"?

**Capture and verification**
- What is the reproducible capture recipe? Is there a counterpart of the RenderTexture harness, and is it as unfaithful to post-processing?
- Do changes made during Play In Editor revert the way Unity's Play Mode changes do? If they do, the failure of the screenshot that lied exists here too.
- How would a sweep of captures at several screen shapes and aspects be built?

**Lighting**
- What is cheap on a mobile Unreal target, and does the advice to author light as texture, baking ambient occlusion into the albedo to unify a stylized look, still apply?
- Does the advantage of a rim light under a fixed camera hold the same way?

**Chrome**
- Is there a shared style system for Unreal's interface comparable to a generated set of chrome sprites, and does it carry the same hazard, that a decoration applied automatically is how unwanted chrome appears?
