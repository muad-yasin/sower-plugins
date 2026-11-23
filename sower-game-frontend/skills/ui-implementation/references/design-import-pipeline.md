# Importing an external design mockup: literal extraction, not visual reproduction

*Open this file before any pass that imports an external design deliverable. Skip it for a small in-engine tweak with no mockup behind it.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

**The mockup's inline styles are the spec.** Pointed at a mockup and asked to "build this screen", an agent reproduces it *visually*: it reads the render, estimates a radius or a spacing by eye, and ships something close (I). A value nobody took from the spec drifts the same way when a shared helper supplies it: on the source project a surface helper hard-coded a card radius of its own, so the game showed two card radii side by side for as long as the helper had adopters, and it put an inset hairline on every card that nobody had chosen, until the hairline was removed on 23 August 2026 (Seen).

## The seven steps

**1. Find the real spec file.** In a design delivery, a zip for example, the file that matters is the HTML mockup, not a screenshot or a rendered preview. Open the raw file. Do not judge it by how it renders in a browser preview, and do not work from a screenshot someone took of it.

**2. Literal extraction.** Before writing any conversion, pull every distinct visual token in scope into a table, one row each:

- hex colour, with the alpha noted **separately** (the colour-space trap below);
- border radius in px;
- padding, margin and gap in px;
- font family, weight, size and line height;
- box shadow: offset, blur, spread, colour, opacity;
- gradient stops: colour, position, direction.

Grep the literal attribute values. **Never estimate a number from how a rendered element looks**: a value read off a screenshot is already a reproduction, not an extraction.

**Declared CSS is not the whole spec; resolved layout geometry is a separate input.** Grepping inline styles gives the *declared* values a layout algorithm consumes, never the *resolved* position and size after flexbox runs. On the source project two import rounds verified every value and still fell short of the mockup as a whole; the milestone history's diagnosis was that the pipeline verified elements, never the screen's type scale, density and spacing as a system, and a research note of the same month named the gap between declared and resolved values (Seen, August 2026). Close it with a headless-browser script that loads the mockup at the project's reference canvas width and dumps **every element's resolved rect and computed style, in canvas-local px**, to JSON (I). Run it beside the grep, not instead of it: the grep gives the declared values step 4 converts, the dump gives the resolved numbers step 7 checks the built layout against.

**3. Copy the assets.** Every image, icon or font file the mockup references is copied in verbatim before conversion starts. **A regenerated or approximated version of the same asset is a different asset.**

**4. Convert.** Map every extracted value to its engine equivalent, one line per token, and **write down the mapping, not only the result**, so that a reviewer can check the conversion itself:

- CSS px to engine units, against the project's canvas reference.
- **Hex and alpha to engine colour, measured again, never copied.** A renderer that works in **linear** colour space lifts a low alpha well above what the sRGB pair seems to describe. On the source project the mockup gave a gold card border an alpha of 0.10; six candidate alphas were composited over a real lit card and read back pixel by pixel, and 0.025 matched (24 August 2026). When the card fill changed three days later, the border was measured again, at 0.020 (Seen). A literal copy would have shipped a hard bright edge.
- **CSS border radius to one of the project's existing radius tiers**, or a codified height-based override. A radius that matches no tier is a decision point for the written plan: **never a new tier, and never an override at one call site** (I).
- **CSS flex and grid to the project's own settled layout patterns.** Reuse the matching one; do not invent another to follow the mockup's DOM more closely.
- **A font family to the project's real type roles.** A mockup naming a font the project does not use asks for the nearest real role, not a new font import. Flag it if the choice is ambiguous.

**5. Write the plan.** Before any engine work: per screen and per component, the exact converted values, which existing prefab, controller or builder each lands in, and, just as important, **which parts of the mockup are illustrative and deliberately not taken.** On the source project the plan for one import named the constants of a mechanic's geometry as locked by its behaviour, and nothing in the plan touched them (Seen, August 2026). **A plan that does not name its exclusions invites the accidental value copy** (I).

**6. Review.** Route the plan through a rules gate (does any converted value break a binding constraint: the radius tiers, the shadow tiers, a locked mechanic's geometry?) and the owner's sign-off for anything that touches copy. **Do it even for a pass that feels small** (I).

**7. Implement.** Only now, from the reviewed plan's converted values. An agent "improving" or reinterpreting a value while it builds, even in a direction that looks better, departs from the plan; the change goes back through steps 5 and 6 instead of shipping silently.

## Checking the text is not checking the screen

On the source project one import ran this pipeline in full, and two rounds of the rules gate on its plan caught real drift each time (Seen, August 2026). **Neither caught the headline defect**: a dark ring on the tall primary buttons. Its cause was two baked sprites with different corner radii, a glow at 30 and a button fill at 39, each right on its own and wrong together; a dedicated pass of real screenshots against the mockup found it, only after eight more screens had been built on top, and a glow baked for that tier fixed it (Seen). Reading code or CSS more carefully does not find that; rendering the two on top of each other does.

**The lesson that project recorded: check a screenshot against the mockup, by pixels, right after any shared or foundational visual change**, such as a button system, a chrome primitive or a type-scale change, **before any other screen is built on top of it** (Seen). Do not defer all visual checking to one pass at the end of a multi-screen import: that tells you how much rework you now owe, not how much you could have avoided. Content changes per screen can still ride the end-of-pass sweep; the raised risk is in shared infrastructure (I).

**"By pixels" means a numeric diff, not an eyeball comparison.** Comparisons that were two images read by a person or an agent are what let two individually verified rounds stay wrong in a row (I: the source project's earlier skill states it). Run a real pixel delta against the handoff's own mockup images, so that no separate ground-truth capture is needed; the source project built one in August 2026 to replace its comparisons by eye (Seen). Report a mismatch percentage and a diff image that marks where the drift is. It does not replace human review: a nonzero mismatch on text-heavy regions is expected (I). Where text sits in its box depends on the font's vertical metrics, a font carries several sets of them, and each browser or program picks which to rely on (D, type.today, "Vertical metrics", read 2026-11-22); TextMeshPro sets a font asset's line metrics itself when the asset is generated, most of them relative to the baseline (D, TextMeshPro package manual 3.2.0-pre.15, "Line metrics", read 2026-11-22). The delta turns "does this look right" into a number to start from.

## What this replaces

The old default was "launch an agent, point it at the mockup, review the result", which puts the check of literal against reproduced *after* the build, when a drift is a diff against working code rather than a line in a plan nobody has touched yet. This moves that check before implementation (I). `visual-craft`'s check after the build, whether it actually looks right, is unchanged and still runs after step 7: it catches composition and staging, not fidelity to the spec, which is what steps 2 to 6 are for.
