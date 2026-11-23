# Evidence for visual-craft (dated)

*Read this file before a figure or an incident from `SKILL.md` or one of its reference files is relied on or quoted. It says where each rule and line comes from, so that whoever maintains the skill can tell when one may go. Standards and engines change: read the page again before you rely on a version-bound line.*

**Grades.** **Seen** = it happened on the source project, a Unity mobile game whose browser build went out as a public playtest in October 2026, and whose records and earlier skills this skill was written from: an incident, a measurement or a decision, with its record named. An earlier skill counts as the record of a case it names. "Shipped" in a note is that project's own word: the change was in the game's committed build. **D** = documented in a named source, read on the date given. **I** = inferred; the row says from what. A rule that an earlier skill states without naming a case is graded I, and a figure an earlier skill gives for how well a method worked is not kept without the record of its measurement. Nothing here was measured: no scene was reviewed with and without a rule. **The old file's statement** = an outside fact kept from the file as it stood before November 2026 and not read again: the line says "not checked at a source" and keeps no figure. **(questions)** marks lines that ask rather than claim, and **(pointer)** a line that sends the reader to another file for its figures. A few D rows rest on an earlier research round of ours; the row gives that date.

## Sources read for the reference files

| Source | Read | What was read |
|---|---|---|
| W3C, Web Content Accessibility Guidelines (WCAG) 2.2, W3C Recommendation of 12 December 2024 (w3.org/TR/WCAG22) | 2026-11-22, the raw page by script | the definitions of relative luminance and contrast ratio |
| W3C, "Understanding Success Criterion 1.4.3: Contrast (Minimum)" (w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | 2026-11-22, the raw page by script | the rationale for 3:1, 4.5:1 and 7:1 |
| W3C Accessibility Guidelines (WCAG) 3.0, Working Draft of 10 September 2026 (w3.org/TR/wcag-3.0) | 2026-11-22, the raw page by script | its status and its note on the contrast algorithm |
| National Eye Institute, "Color Blindness" (nei.nih.gov) | 2026-11-22, the raw page by script | the share of men, and the most common type |
| Machado, Oliveira and Fernandes, "A Physiologically-based Model for Simulation of Color Vision Deficiency", IEEE Transactions on Visualization and Computer Graphics 15(6), 2009 (the authors' page at inf.ufrgs.br) | 2026-11-22, the raw page by script | the model's scope |
| MDN, "Window: devicePixelRatio property" and "oklch() CSS function" (developer.mozilla.org) | 2026-11-22, the raw pages by script | what the ratio is; Oklab's perceived lightness against hsl()'s |
| arXiv 2402.04788 (MLLM-as-a-Judge, version 3) and 2603.19203 (Tinted Frames, version 2) | 2026-11-22, the abstract pages by script | the abstracts |
| type.today, "Vertical metrics" (type.today/en/journal/verticalmetrics) | 2026-11-22, the raw page by script, read for `ui-implementation` | where text sits, and which metrics a program relies on |
| anthropics/skills, `skills/frontend-design/SKILL.md` at commit 2c5958ec, lines 34 to 45 (github.com/anthropics/skills) | 2026-11-12, in a research round of ours | the generic looks AI-generated pages cluster on |

## Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Open the reference file, never memory of it | Seen, I | the source project: its written art direction was corrected from flat and top-down to isometric and soft-shaded once three real reference images were adopted; the record is one line, of 8 July 2026 (Seen). That memory of a reference drifts is the old file's reasoning (I) |
| Extend what exists | I | the source project's earlier visual skill states the rule |
| Camera and perspective as a presentation layer | Seen | the source project, August 2026: two of its three rooms moved to a near-top-down perspective camera after every alternative that kept the isometric view had been measured and rejected, while the third stayed isometric; its design document recorded the art direction as unchanged, framing and not style |
| Name the layer of a complaint | I | the old file's rule |
| The three generic default looks | I | the old file's statement, which called them scene-level; the defaults and their tells are in `references/originating-a-new-surface.md`, not checked against records for this file. The list behind them is about generated pages, so the files call them looks and send environment work to `references/procedural-environments.md` |
| Value before colour; one dominant focal read | I | the old file's craft rules; the vocabulary is in `references/staging-and-lighting.md` |
| Palette discipline | I | the source project's earlier visual skill states the rule |
| Materials agree; plausible base colours | Seen | a plan of September 2026 diagnosed the source project's near-white walls: above the plausible range for a non-metal, clipping under the key light, reading as paper |
| Style in values, palette, geometry and proportion | I | the old file's synthesis |
| Tabular figures for live numerals | I | the old file's rule; no incident of a jittering price was found |
| The world-to-viewport mapping | Seen, I | the source project, July 2026: rounds of placement requests in one session, the first two built, as the record says, on sampling the camera's world-to-viewport projection at the floor's corners (Seen). That this is a gap the work keeps hitting is the old file's reading (I) |
| Conflicting axes; say so | Seen | the same work: a desk moved toward the bottom-left stopped short of the room's extreme point, which lay inside another prop's footprint, and the trade-off was written down |
| Gestalt grouping; figure-ground | I | the old file's staging vocabulary, in `references/staging-and-lighting.md` |
| Icon sets, render size, shared chrome | I | the source project's earlier visual skill states the rule |
| Contrast computed, from a capture wherever a colour is translucent or blended; the four-to-five-fold lift | Seen, D, I | the source project renders in linear colour space, which lifts a low gold or cream alpha over a dark card roughly four to five times over what the stored constant suggests. One border's 0.10 in a mockup measured 0.025 on 24 August 2026, and 0.020 when measured again on 27 August over a new card surface; the code carries 0.020 with the second probe's readings. The record is a translucent colour: for an opaque pair the stored values are the colours, and W3C's page on the contrast criterion takes them from the browser or the styles (read 2026-11-22). Sampling a capture off the flat of a glyph is our inference from that page's note on antialiasing |
| A capture is the ground truth | Seen | a signage wordmark sat behind its panel's front face while that session's verification reported no console errors; a batch of new materials parsed "0.55" as 55 and rendered white, which the first screenshot after the batch showed and a query of the stored values (55, 32, 22) confirmed (July 2026) |
| A capture from a live play session | Seen | the source project, July 2026: a desk moved during play, while it was checked against live screenshots, lost the move when play stopped and sat 1.5 to 2 m from its hotspot through several later verification passes; the hotspot, created separately outside play, never moved, so every click test passed |
| More than one distance; sets checked together; drift over time | I | the old file's review practice |
| Every real state | I | the source project's earlier visual skill states the rule |
| Vision-model reads | D | "MLLM-as-a-Judge" (Chen et al., ICML 2024, arXiv 2402.04788, version 3), abstract read on 2026-11-22: in its authors' tests, multimodal models judging vision-language tasks were biased, invented details and gave inconsistent verdicts, the strongest model tested among them, and agreed with people more when comparing two items than when scoring or ranking. "Tinted Frames" (arXiv 2603.19203, version 2), abstract read on 2026-11-22: a constrained question (yes or no, multiple choice) makes a model attend to the image less than an open one |
| The counters | D, I | describing in an open question before judging follows the second paper (D); comparing with a reference applies the first paper's pair result to captures, and asking more than once follows from its inconsistency (I); naming a heuristic and cropping are the old file's, from `references/critique-and-vlm-qa.md` (I) |
| A second, less invested read | I | the old file's rule |
| The five tells of a generic environment, put as questions | Seen, I | the source project: the owner rejected a regenerated, bigger city map as generic; the diagnosis was strong detail per block and no identity in the structure (a filled-diamond silhouette, no geography, an invisible road hierarchy, parks sprinkled uniformly, one material family), and the generator was reworked over about ten bakes. That one tell alone does not settle a rejection is our inference from that one map |
| A mockup tool earns its cost on two things | I | the old file's conclusion from a research pass that included the cost of a design tool |
| A reference library | I | the old file's rule |
| A licence check per generator tier | Seen | the source project's licensing rule: output of a free web tier was for personal use only and public, so only the paid API's output could become a game asset |

## Retired in November 2026

| Line | Why it went |
|---|---|
| "one real project's art direction had to be formally reset after months of work off a remembered description" | the record shows a correction against three reference images; "months" was not found |
| "without the art direction changing at all, because 'isometric' was never the style" | reworded to the record's own terms: the design document says the art direction stayed, and calls the change framing, not style |
| "half of 'this looks wrong' is a framing problem wearing a style problem's clothes" | a proportion nobody measured |
| "The most-repeated real gap in this work" | a superlative; the record shows three rounds of requests |
| "Trust it over intuition every time; the two have disagreed more than once" | the disagreements were not found; the rule to trust the mapping stays |
| "the likeliest failure in a busy scene" | a ranking with nothing behind it |
| "geometry that existed but rendered fully hidden behind an opaque disc at the same depth" | the earlier skill names it without a record of its own; the wordmark behind its panel, which has one, makes the same point |
| "masking that the visible geometry had drifted 1.5-2m" | left out: the records give about 1.5 to 2 m, and the rule does not need the figure |
| "A dedicated mockup tool earns its cost on exactly two things" | "exactly" had nothing behind it; graded as an inference |
| "the room lighting rig" in the engine pointer | the Unity layer holds the lights each room needs, not a rig section |
| "while the *stored* values looked plausible on paper" (the locale-parsing bug) | the record says a query of the stored values showed 55, 32, 22, which confirmed the bug |
| "the first city bake" | the record names a regenerated, bigger map |
| "Visual sycophancy" as the failure's name in the main file | the two abstracts read describe the failure without the term; `references/critique-and-vlm-qa.md` keeps it, and 3d-assets' references cite it there |
| The old description, which a strict YAML parser could not read (a colon followed by a space inside it) | rewritten |
| The heading "Mistakes to actively flag" | now "Mistakes to flag", as in the other skills |
| Contrast "never from stored constants" | the record is a translucent colour in a linear colour space; for an opaque pair the stored values are the colours, and the interface skill computes those from the palette (an outside review of this repository, November 2026, found the two files giving opposite verdicts) |
| The five tells, "each a reason to reject on its own" | the record is one rejected map with all five together |
| "the three generic defaults at the scene level" | the list behind them is about generated pages |

## references/color-accessibility.md

| Line | Grade | Behind it |
|---|---|---|
| The contrast formula and its range | D | WCAG 2.2's definitions, named in the line |
| The thresholds | (pointer) | `ux-design` holds them, from the same Recommendation |
| Why 4.5:1; the acuity of elders at roughly 80 | D | "Understanding Success Criterion 1.4.3", named in the line |
| WCAG 3's open contrast measure | D | the Working Draft named in the line |
| A stored value answers only for an opaque pair; a translucent or blended colour is taken from a capture, off the flat of a glyph | I, D | from the measured cases in `references/unity.md`; W3C's page on the contrast criterion for where a web page's colours are taken from, and for its note on antialiasing |
| About 1 in 12 men; red and green | D | the National Eye Institute's page |
| Machado's model | D | the authors' page |
| Viénot's and Brettel's models; colour-matrix filters | the old file's statement | not read again |
| The broker app's trade numbers with signs or arrows | Seen | the design archive's rule for trade feedback, a recorded decision; its one named exception is to the rule of no effects, not to the pairing |
| 60/30/10 | I | the earlier skill states it, after a research note's advice; no case found (our search: 60/30/10 over the project's documents) |
| Naming the harmony | I | the old file's reasoning |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Thresholds (WCAG 2.2, the current standard)" with their figures | `ux-design` holds the figures, read on 2026-11-22 |
| APCA "is a candidate for WCAG 3.0 and was pulled from the July 2023 working draft" | not read; WCAG 3's draft of 10 September 2026 says that its contrast algorithm is yet to be determined |
| "1 in 200 women"; deuteranomaly as "the most common single type", "~5% of men" | not on the page read |
| "for tritanopia only **Brettel 1997** is considered solid" | now the old file's statement, worded as the usual choice |
| "a mockup's `0.10` had to be *measured* at `0.025`" | measured again at 0.020 after the card fill changed; `references/unity.md` gives both |
| "A ± sign on every number is this rule already working" | the record is the broker app's trade numbers |
| "Compute against what renders, not against the constant in code" for every pair | scoped to a translucent or blended colour; an opaque pair is its stored values |

## references/critique-and-vlm-qa.md

| Line | Grade | Behind it |
|---|---|---|
| Define the problem before the fix | the old file's statement | after a GDC talk of 2016 by Jeff Hesser, not read |
| Batching notes; reaction, reflection, rephrasing; restraint | I | the old file's practice |
| The four steps in order | I | the earlier skill gives the method; its author's first name is not on file |
| The showcase scene and the pass for unused props | the old file's statement | after a talk by Charles Boury, not read |
| Hero and kit | I | the old file's reasoning |
| MLLM-as-a-Judge; Tinted Frames | D | the two abstracts named in the lines |
| "Visual sycophancy" | I | this skill's name for what both studies point at |
| The counters | I, D | from the two studies, as each line says |
| The limit on image size | I | it depends on the model; the old figures went |
| The generators' levers | the old file's statement | not read again |
| No image input; the inert path in a prompt draft | Seen | the asset-generation notes, July 2026: a draft caught before it cost anything |
| Positive description; the icon fixed by a correction | Seen | the asset-generation notes: the portrait recipe, and an icon fixed on its second try |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Perceptual Judgment Bias" / visual sycophancy (Park et al. 2026) | the paper could not be found (an earlier research round of ours searched for it on 2026-10-01); the section rests on two papers read |
| "including cases where it perceives correctly under a direct query but defers anyway" | the same paper's claim |
| "describing an image as clear, then rating it poor" | not in the abstract read |
| "a measurement it demonstrably can" | "demonstrably" had nothing behind it |
| "trust only the defects the reads agree on" | agreement makes a lead to check, not a confirmation |
| "downscaled past roughly 1.6k tokens (a 1080p screenshot arrives at about 819x1456)" | a limit that depends on the model and has changed between generations |
| ControlNet-class, IP-Adapter-class, a style LoRA; "the real mechanism at scale is a deterministic, re-runnable graph" | not read; the file keeps the levers without the names |
| "a mistake worth naming because it has been made twice" | the record shows one prompt draft |
| "never as an exclusion list, because exclusion-only prompts do not reliably hold" | "never" and "reliably" went beyond the portrait recipe, and a negation fixed one icon |

## references/originating-a-new-surface.md

| Line | Grade | Behind it |
|---|---|---|
| The three defaults | D | anthropics/skills' frontend-design skill, as the line names it, read 2026-11-12 in a research round of ours |
| The broadsheet's pull on a product built around news | I | the earlier skill states it for the source project |
| Dark fintech as the cliché of trading apps | I | no source read |
| The recorded dark foundation | Seen | the design archive's entry on the re-skin |
| The siblings | (pointers) | `../../ux-design/references/new-visual-directions.md`; `procedural-environments.md` |
| What of the three looks applies to a room or to props | I | two of the three are palettes, the dark ground with one bright accent and the warm cream with a clay accent; the broadsheet is a layout and a type treatment, which a room does not have |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Any product built around news, articles or documents is pulled toward this constantly" | "constantly" had nothing behind it |
| "The visual cliché of every real trading app" | "every" had nothing behind it |
| "Warm cream with a terracotta accent" | the page read says clay |
| "These three are defaults of environments and scenes"; "scene-level" in the title | the list they come from is about generated pages; environment structure is `procedural-environments.md`'s |

## references/procedural-environments.md

| Line | Grade | Behind it |
|---|---|---|
| The map read as texture in a window of about 1080 by 420; the coarser blocks; the clipped window | Seen | the milestone history, July 2026 |
| The palette as a criterion | I | the old file's rule |
| The five tells, as questions; the generic carpet | Seen, I | the milestone history: the rework of 22 July 2026, one map with all five together. That one tell alone does not settle a rejection is our inference from that |
| Anchor elements and a quirk per asset | I | the earlier skill states the rule |
| The anchored parks; two framings over about ten bakes; framing on projected vertices and the 40% | Seen | the same rework |
| A log of risky positions | I | the earlier skill's rule |
| 2 bridges, quality over count, the two knobs | Seen | the milestone history and the task archive, 22 July 2026 |
| Instrument before iterating; 93% | Seen | the rework's fight over the bridges |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "One city map's fine-grid buildings read as noise at ~1080x420 despite a clean 4096px canvas" | the canvas was 3072 by 3072 then; 4096 belongs to a later version |
| "generators drift toward mid-value, low-commitment colour" | the record is about image prompts, not procedural generation |
| "one palette family everywhere" | the record says one material family |
| "One real first bake failed all five" | the record names a regenerated, bigger map |
| "3-5 deliberately placed, non-repeating anchor elements" | a count with no record |
| "2 bridges shipped against a target of 4" | no target of 4 was found |
| The five tells, "each a reason to reject on its own" | the record is one map with all five together; they are questions now, and the rejection rests on the criteria written before generating |

## references/staging-and-lighting.md

| Line | Grade | Behind it |
|---|---|---|
| Gestalt grouping; the kit workflow; framing; negative space; greybox first | I | the old file's reasoning |
| Valorant and de_cache | the old file's statement | not read |
| Four light types; a box of hacks | the old file's statement | after a talk by Robert Yang, not read |
| Three-point lighting under a fixed camera; motivated light; mood | I | the old file's reasoning |
| Lighting as texture on mobile | the old file's statement | not read again |
| Levels of detail under a fixed camera | I | the earlier skill decided it for three rooms; no record of the decision in the project's documents (our search: LOD, as a word, over them) |
| Batching; artifacts | I | the old file's rules |
| Overdraw | the old file's statement | not read again |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Figure-ground is the principle most likely to fail in a busy scene" | a ranking; `SKILL.md` holds the test |
| "The canonical industry evidence ... Trust it: consensus, not house quirk." | not read |
| "Four light types are the complete basic toolbox" | "complete" had nothing behind it |
| "stylized productions frequently bake light and AO straight into the albedo"; "On mobile, lighting is often authored *as* texture" | frequencies nobody measured |
| A light belonging to "the scene" "lights the wrong thing invisibly" | the record: hiding the first room's root would have left the others dark; the claim about rooms lighting each other was an Edit Mode finding, corrected |
| "Overdraw is the mobile killer" | a ranking |
| Negative space as "the most useful classical idea for prop work" | a ranking with no record |

## references/typography-and-spatial-mapping.md

| Line | Grade | Behind it |
|---|---|---|
| Ten named tiers in place of 21 sizes, later seven | Seen | the milestone history (the typography pass of 15 July 2026) and the milestone specs (the redesign's seven tiers) |
| The diegetic type stack; the three roles | I | the source project's phone is its interface; the claim about type is ours |
| The hero tier at two call sites | Seen | the design archive and the milestone specs, 24 August 2026 |
| Tabular figures baked into the font | Seen | the redesign plan of 5 August 2026 (a plan; its outcome was not looked up) |
| The procedure through three rounds; the corner sampling of the first two | Seen | the session log and the pipeline document, July 2026 |
| The desk short of the extreme point | Seen | the pipeline document |
| The modular kit | I | the earlier skill's rule |
| The arch primitive | Seen | the milestone history, 10 July 2026 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "The most-repeated real gap in this work" | four records give that superlative to four different things |
| "proven three times in one session" | three rounds of requests, with the sampling recorded for two |
| "the two have disagreed more than once" | the record is a labelling mismatch before any coordinate math |
| "yields dozens of distinct-reading objects" | a count nobody made |

## references/unity.md

| Line | Grade | Behind it |
|---|---|---|
| The linear lift and its condition; the multiplier of 0.40; 0.025 and 0.020 | Seen | the design archive, the milestone history and the builder's code comment, August 2026 |
| Contrast from captures; alphas measured again | I | from the measured cases |
| A baked sprite takes a multiplier; the primary button | Seen | the design archive: the defect that closed a milestone |
| The capture recipe and the harness's limit | Seen | the source project's capture standard, August 2026 (`3d-assets`'s `references/unity.md` holds it whole) |
| The wordmark behind its panel | Seen | the milestone history |
| The layer signature; layer 0 | Seen | the pipeline document: the third instance in one room; the character pipeline |
| The default smoothness and the 0.15 recipe | Seen | the milestone history, 10 July 2026, and the pipeline document |
| Each room's key and fill | Seen | the pipeline document, 10 July 2026 |
| The toggled render; four additional lights; the Edit Mode scope | Seen | the pipeline document: a finding of 18 July 2026, its scope corrected on 1 August |
| Bloom all or nothing | Seen | the pipeline document, 2 August 2026 |
| The desk, 1.5 to 2 m, the passes and the click tests | Seen | the milestone history, July 2026 |
| The radius table; the hairline removed on 23 August 2026 | Seen | the design archive and the milestone history |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "a low alpha reads roughly 4-5x brighter on screen", without its condition | the record: a light colour over a dark surface; white over bright gold shipped untinted |
| "re-measured at `0.025`" as the standing value | measured again at 0.020 |
| "and no shipping phone produces it" | the records disagree |
| "reported clean for an entire build" | the record: that session's verification reported zero console errors |
| "the single most-repeated invisible-geometry bug" | a ranking; four records call four different things the most repeated |
| "a comma-decimal culture turned `0.55` into `55` and shipped six blown-out white props", and the stored values | `3d-assets`'s `references/unity.md` words the case to its record |
| A light belonging to "the scene" "lights the wrong room invisibly" | as in `references/staging-and-lighting.md` |
| Bloom "can silently differ between them" | the record's trap is all three or nothing |
| "looked correct across several later verification screenshots" | the record: verification passes and click tests |
| "kept coming back for months" | no duration in the record |
| The heading "Invisible geometry is usually a layer, not a position" | the record is three cases in one room; the heading now gives the check |

## references/web.md

| Line | Grade | Behind it |
|---|---|---|
| Oklab's lightness; hsl() and hwb() in sRGB | D | MDN's page named in the line |
| The alpha correction does not carry over | Seen, I | the records' statement that CSS composites in gamma |
| `devicePixelRatio` | D | MDN's page named in the line |
| Vertical metrics | D | type.today, read for `ui-implementation` |
| Capture tools; dark mode; the page and the canvas; the letterbox | I | the old file's reasoning |
| The public playtest; no visual-QA pass on record | Seen | the notes on the web build (our search: letterbox, embed, visual QA, in those notes and the release overview for itch.io: only lines on canvas size) |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "CSS colours are sRGB unless you opt into a wider space" | worded to MDN's page |
| "a 1px hairline at DPR 3 is a third of a physical pixel" | inverted: at a ratio of 3 one CSS pixel spans three device pixels |
| "because they read metrics from different font tables" | worded to type.today's page |
| "it is the single largest colour field on the page" | a superlative |
| "We have not run a production web visual-QA pass" | the browser build went out as a public playtest in October 2026; no visual-QA pass of the page is on record |

## references/unreal.md

| Line | Grade | Behind it |
|---|---|---|
| The open questions | (questions) | the Unity layer's findings, each asked of Unreal |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Master material plus material instances appears to be the idiom" | not read; now a question |
| "This is the highest-value first answer" | a ranking; the question still comes first, for what depends on it |
| "Unity's most-repeated invisible-geometry bug" | a ranking |
| "Lumen and virtual shadow maps change the baked-vs-dynamic calculus" | not read; now a question |
| "UMG's brush/tint model" | not read |
| "this is the sentence that will save someone a week" | a claim nobody measured |
