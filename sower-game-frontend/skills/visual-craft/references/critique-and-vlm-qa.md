# Critique process and vision-model QA reliability

*Open this file before any formal critique or self-review of visual work, and before you ask any vision-capable model whether something looks right. That includes you: a session judging a screenshot is such a model. This extends the verification in `SKILL.md`; it never replaces it. The text-side sibling is `../../ux-design/references/judgment-discipline.md` (sycophancy on design recommendations); this file covers sycophancy on pixels.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## Critique, don't criticize (the self-review ritual)

- **Define the problem before proposing the fix, and give the reasoning behind the judgement.** Not "the composition is bad" but the experience: "my eye is not led from the primary focal point to the secondary one; it sticks on the light shape on the shirt." A named problem can be checked again; a verdict can only be repeated (not checked at a source; stated here since September 2026, after a GDC talk of 2016 by Jeff Hesser of Harmonix).
- **Batch scattered small notes and look for the one root theme.** "Move the volcano back", "the trees are too big" and "shrink the rug" can resolve to one cause, "the space reads shallow" (I). Fixing notes one by one without finding the theme is how a scene absorbs ten edits and still reads wrong.
- **First reaction, then reflection, then rephrasing.** A first reaction is data, badly phrased; the reflection is where "ugly" becomes a claim you can address (I).
- **Four steps, in this order: description** (objective, no value words), **analysis** (how the elements relate), **interpretation** (what it communicates), **judgement** (does it succeed, on the strength of the first three). The order is the point: starting objective prevents the premature "looks fine", and it is also the skeleton of the prompt in the vision-model section below (I: the source project's earlier skill gives the method).
- **Restraint is a behaviour:** know which buttons not to press; predict where a scene will read wrong before you build it, say the prediction, then check it in the capture; and when a scene is busy, cut one *attractive* element. Removing something good, not something obviously bad, is where restraint starts (I). Taste is built by deliberate comparison with a reference: open the actual reference file again.

## Showcase scenes and review triage

- **A standing showcase scene is the durable form of the contact sheet in `SKILL.md`:** a grid of every prop, a grid of materials under the scene's real lights and a sheet of the interface, reviewed for palette, silhouette and detail **as a set**. The drift exists only in the comparison, and a showcase makes that comparison a screenshot instead of a project. Its companion is a periodic pass that flags props nothing uses: fewer props to polish means more polish for the rest (not checked at a source; stated here since September 2026, after a talk by Charles Boury).
- **Triage review time by hero and kit.** A hero prop, used once and carrying a room's identity, earns its own critique; kit props such as desks, chairs and racks are reviewed as a family in the showcase. Hero-grade attention spent on everything runs a solo review out of time before it reaches the thing that matters (I).

## Vision-model visual QA: a measurement instrument, not a taste authority

What two dated studies show (D, both abstracts read 2026-11-22):

- **MLLM-as-a-Judge** (arXiv 2402.04788, version 3, ICML 2024): multimodal models judging vision-language tasks showed "diverse biases, hallucinatory responses, and inconsistencies in judgment, even in advanced models such as GPT-4V". They came close to people when comparing two items and diverged from them when scoring or ranking.
- **Tinted Frames** (arXiv 2603.19203, version 2, March 2026): vision-language models are "selectively blind". The framing of the question changes how much they attend to the image; constrained framings such as multiple choice and yes or no give substantially lower attention to it, which the authors find is the main cause of lower accuracy and of answers that change with the framing.

**Visual sycophancy** is this skill's name for the failure both point at: a verdict that follows the framing of the question, or what the asker seems to want, more than the pixels (I). The counters lie in how the question is built, not in effort:

- **Diff, don't judge.** Put the reference or anchor image beside the render and ask where they diverge. That turns "is this good?" into "do these match?", the comparison of two items on which the first study found models closest to people (I: the pair case).
- **Name the heuristic.** Point the check at rules that can be checked, such as the spacing grid, a contrast ratio, one dominant value mass or the five procedural tells; never "does it feel right" (I).
- **Describe before judging.** Ask an open question for an objective description of what is in the capture before any verdict: a yes-or-no or multiple-choice question is the framing the second study found makes the model look less (D).
- **Ask more than once on anything that matters,** and treat what several reads agree on as a lead to check, not as a confirmation: the verdicts are inconsistent, and agreement does not make them right (I).
- **Respect the hard limits.** Images are resized to a limit that depends on the model and has changed between generations of models: check the current one, and **crop to the component under review** instead of sending a whole scene (I). Counts and coordinates are approximate, so never rely on a model to count repeated small props. A screenshot is ground truth only for the one state, frame and viewport it captures, so capture the states that matter on purpose.
- **The gap, stated so that it is not overstated:** these studies measured judging tasks and visual reasoning, not artistic taste (I: neither abstract measures it). Treat a model's read as useful for "these two diverge here" and as **unverified** for "this reads as one coherent style". A person's eye stays the gate on style; if a model's verdicts start to diverge from it on coherence, use the model for drift detection only.

## Consistency in generated assets: which levers your pipeline has

The levers generative pipelines use for consistency are structural control, reference or identity conditioning, a trained style and a fixed seed (not checked at a source; stated here since September 2026). They are worth listing only if your pipeline has them, so **find out which it has: some have none.** On the source project no image model of its provider accepted an image input for style conditioning, only a prompt, a size and an aspect ratio, so a reference file path written into a prompt draft was inert; its owner caught the draft before it cost anything (Seen, July 2026). Where the levers are absent, consistency comes from two things that cost nothing:

- **Locked written prompt recipes**, the art bible made executable. Describe the target technique positively: on the source project a portrait recipe's list of exclusions fought traits the model was always going to produce, and describing those traits positively is what let the next rounds converge (Seen). For one subject a targeted correction can still work: a correction that described the shape and named what it was not fixed an icon that had come out as a soft blob, on its second try (Seen).
- **A contact sheet of every batch against the shipped neighbours.**

If the pipeline gains structural control or style training, those levers are the adoption checklist. Until then, proposing them is tooling for tooling's sake (I).
