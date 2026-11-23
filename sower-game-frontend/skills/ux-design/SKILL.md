---
name: ux-design
description: Runs the design pass before any interface is built - the player's flow, a text wireframe, every screen state (locked, first-time, empty, loading, active, error), information hierarchy, accessibility, notification tiers and how transient surfaces leave, onboarding, monetization UX and dark-pattern screening, and the words on screen. Use before building or changing the path a player takes, the regions of a screen, its states or its words, including small requests like "add a button" or "show X to the user", even when the request never uses a design word. Hands ui-implementation a confirmed flow, a wireframe and a complete states list. Not for a change of look alone or for whether the built result looks right (visual-craft), or for building geometry and motion (3d-assets).
license: MIT
---

# UX Design

You own the **what and where**: the path a person takes, the regions of the screen, every state the screen can be in, and the words in it. Hand off **a confirmed flow, a wireframe and a complete states list**; anything newly shown to a player runs this pass first.

**Flow before visuals.** Never jump to layout or style before the path is mapped.

**Evidence and grades.** **Seen** = it happened on the source project (a Unity mobile game), with the record named in `references/evidence.md`. **D** = documented in a named source, read on the date given there. **I** = inferred, with the reason in the sentence. Open `references/evidence.md` before you quote a figure or an incident from this file. This skill does not claim that following it improves a project's results.

**This skill owns:** the flow, the wireframe, the states list and the mystery-lock rule, the numbers for accessible targets and contrast, notification tiers, dark-pattern screening, and what each control, state and error says. **It hands off:** the build to `ui-implementation`; whether it looks right to `visual-craft`; the judgement of a design with stakes in player psychology or money, after this skill's own screen, to the `design-review` agent of the review plugin where it is installed, and otherwise to a reviewer who did not design it.

## Step 1: Map the flow (always first)

- What is the person trying to do, and which emotional beat of the product does it serve? If the product has a stage or arc structure, name the stage this serves.
- The steps in order, from entry to goal, and the fewest taps to value: cut steps.
- Decision points and branches ("if they can't afford it, show X").
- Where it lives in the existing structure. Extend an existing surface before you justify a new top-level one.
- **Nothing narrative fires on its own.** A story beat, a character scene, a pitch or an offer is gated behind an explicit tap (an inbox message with an action button is the cheap, reusable pattern), never a cold open at a threshold. A forced sequence is a deliberate override with a written reason, not a default.
- **Before scoping a tutorial or a hint, check whether an existing persistent element already teaches it.** One onboarding pass on the source project found two of three suspected gaps already taught by what the screens showed, and shipped one caption instead of three (Seen).

Open `references/first-session-and-store.md` before scoping any onboarding, tutorial or early beat, or a store listing: the first-session yardstick, the two forced sequences that earned their override and the fence around a third, the first seven days, and the store page.

## Step 2: Wireframe and states

A text wireframe: regions, elements, hierarchy. No visual style yet.

- **One primary action per screen.** If two compete, restructure.
- **Primary actions in thumb reach** (the bottom third on a phone). Touch targets take the platform's number, never the smallest one you can cite: 48x48 dp on Android, and on iPhone and iPad Apple's default control size of 44x44 pt, with about 12 pt of padding around a control that has a bezel (D). WCAG 2.2's floor is 24x24 CSS pixels, or that much spacing, at level AA, and 44x44 at level AAA (D). This skill holds these numbers for the frontend skills.
- **Compose for a range of screen shapes, and say in the wireframe where the surplus goes.** On a phone a design-width canvas fixes the width and the height varies: up to about 600 surplus design units between 16:9 and 21:9 on the source project's canvas. Name a scrolling region, a spacer or a background, the way you list states; left unnamed, the surplus lands wherever an unrelated flexible element sits. On the source project a dialogue box's line text took it and left a hole of about 450 units on 20:9 phones, unseen because every capture used the shortest canvas (Seen). "It centres" is a fine answer; it only has to be chosen. In Unity, the mechanics: `references/unity.md`.
- **Keep text and tap targets out of the top keep-out.** Phones are edge to edge, with a camera cutout and rounded corners, and an app that targets Android 15 is drawn edge to edge, into the cutout area (D). Treat the keep-out as an authoring rule, not a container the engine hands you. A header's alignment is no guarantee: left-aligned, it clears the camera box only while it stays short of the centre, and on the source project one wide heading crossed it (Seen). Say in the wireframe how wide each element of the top row can get, and give anything new at the top centre a deliberate look.
- **The states list: every state, named.** Locked or teaser, first-time, empty, loading, active, error. Say what each one tells the player about what comes next.
- **The mystery-lock rule: choose mystery-lock or full transparency per screen, on purpose.** A screen whose job is discovery may hide locked content entirely; a screen whose job is planning or investment shows names, costs and prerequisites up front, because seeing the whole shape is the point. Say which you picked and why. A worked split: a physical prop in a world scene can be a mystery object that does nothing until it unlocks; the menu screen listing the same upgrades cannot, because it is a planning surface.
- **Every locked or empty state needs four things**, not just a greyed-out control: a short headline for what lives there, a one-line reason it is unavailable, a visual cue, and a next step where one honestly exists. Where none exists, plain dimmed chrome with no caption beats a caption that points nowhere. Pick one of the two; do not invent a third.
- **A newly interactive element needs a visible sign that it can be tapped** (an icon, a highlight, a chevron, a caption), specified here and not left for the implementation to notice; the source project found it missing twice (Seen).
- **Say which job each visual signal does:** *inviting* (a glow, a pulse, a badge: it draws attention) or *informative* (a label, a count, a chip: legible but receding). Naming the job at wireframe time stops an informative element being animated into a nag, or an inviting one styled too quietly to invite. If a control needs a caption to explain its own verb, question the control before writing the caption.
- **A consequential action can be undone, or the player is asked before it runs, and undo is the better of the two.** A question before every routine action trains people to tap through it, so keep it for what cannot be taken back, and say in it what will be lost (D, I: the heuristics below; the remedies are this skill's).
- **Before handoff, walk the wireframe with four questions:** can the player always see what state the game is in; is there a marked way out of every screen and every transient surface; can each consequential action be undone, or is the player asked first; does every screen show what the player needs from the one before, or keep it within reach? Each "no" is a finding while it is cheap to fix (D: four of Jakob Nielsen's usability heuristics, restated for a wireframe).

## Step 3: Visual decisions (only after steps 1 and 2)

- **Ground every proposal in the frozen token set** (the real corner radii, the surface ladder, the type scale, the palette constants) **and in what neighbouring screens actually render, never in what "a nice dark fintech app" looks like in the abstract.** A model's first idea regresses to the generic; grounding beats that default and no clever prompt does (I).
- A small, consistent palette and a spacing scale (multiples of 4 or 8) reused across surfaces. A new colour needs a stated reason tied to meaning. At most two font sizes or weights per screen unless there is a stated reason.
- **Diegetic consistency.** If the product wears a fiction, every surface obeys it: mail looks like mail, a broker looks like a trading app. Name the *layer* of a genuinely new surface at spec time: an in-fiction screen, the world or 3D scene, or a deliberate fourth-wall screen (a store page, real-money prices, settings). The layer decides pipeline, voice and chrome before a pixel is drawn; a surface that cannot name its layer is the "outside the fiction" mistake in embryo.
- **Restraint on outcome feedback.** Signed numbers and pacing carry emotional weight; confetti and screen shake do not, and screen shake is an accessibility problem besides (Step 4). A live *instrument* the player operates while an outcome is still undecided is a different thing from feedback on a result: that is the only kind of exception worth granting, and it is written down when granted (Seen: the source project recorded one, for a minigame's live window).
- **A genuinely new direction has its own discipline:** open `references/new-visual-directions.md` before proposing a new screen, layout or direction. A reskin, or a conformance pass whose structure is locked, does not need it.

## Step 4: Accessibility (never skipped, not even in a prototype)

- **Never rely on colour alone.** Every colour-coded state also carries a sign, an arrow, an icon, a shape or a word, as a structure and not as a review item (the measured reason: `../ui-implementation/references/timing-and-verification.md` §4).
- **Contrast, computed, never eyeballed:** WCAG 2.2 at level AA asks 4.5:1 for normal text and 3:1 for large text, and 3:1 for the visual cues that show what a control is and which state it is in, and for the graphic parts a player needs in order to understand the content (criteria 1.4.3 and 1.4.11; the second is the one people forget) (D). The formula and the colour-blindness protocol: `../visual-craft/references/color-accessibility.md`.
- Visible labels on inputs, never placeholder-only.
- Touch targets and spacing checked at the smallest supported size.
- **Motion is an accessibility axis.** Screen shake and large parallax can make people ill, so restraint on feedback is accessibility, not only taste (I). WCAG 2.2 asks at level AAA that motion triggered by interaction can be switched off unless it is essential (D): if viewport-scale motion is ever needed, design its reduced-motion version alongside it, never as a retrofit. Sustained small motion (a pulse, a crawl) should read as noticeable, not nagging.

## Step 5: Notifications, trust and dark patterns

- **Pick the intrusiveness tier on purpose; do not default to the loudest.** Cheapest to loudest: a **badge** on a persistent element for background unlocks; a **strip or ticker** for something time-sensitive but not critical; a **full takeover** only for genuine scripted beats, and even those gated behind a tap (Step 1). Match the tier to how urgent the information is, not to how excited the feature is to announce itself. A joke does not buy a louder tier.
- **A transient surface owns its exit, designed as an explicit state:** exactly when it goes (once consumed, after one full pass, never "frozen in place") and whether it replays on reload. One with no designed exit is the one somebody reads as a bug. Open `references/notification-lifecycle.md` before designing any notification, ticker, banner, toast or badge: the tiers' behaviour, the policy for several triggers on one surface, the one recorded exception that waits without a timer, and the case where locking a surface by disabling it read as breakage.
- **Screen for dark patterns before you finalize any design with a monetization or engagement angle, and treat it as compliance, not taste:** check the current law of the markets you ship to before relying on a pattern being allowed. The taxonomy, the patterns of the time axis, and the legal background as last read (read it again before you rely on it): `references/dark-patterns.md`. One rule binds without it: **no feature may ever SELL the recovery from a player's own mistake** (Seen: the source project's own boundary). A product may *lampoon* these patterns in its fiction; it never deploys one on the player.
- **Anything with real stakes in player psychology or money gets a second look before it is built**, after this screen and not instead of it: the `design-review` agent of the review plugin where it is installed, otherwise a reviewer who did not design it. Have the reviewer say which check settled the verdict and what it showed, for a pass as much as for an objection; a "needs changes" is the review doing its work, not friction.

## Copy is half the design

Tone governs how something sounds; these govern whether it works. Both bind.

- **An action keeps one name through the whole flow.** The control that says SELL produces a confirmation that says SOLD, not "Transaction complete": a word that changes mid-flow makes someone check whether they did what they meant. The name is the specific verb: a button that commits money says what it commits, never a bare "OK". Counts pluralize correctly; a wrong plural is exactly the size of tell that reads as templated.
- **Name things by what the player controls, not by how the system is built.** No "handler", "controller" or "state" in a label: an implementation noun leaking into in-fiction copy is as much a defect as a missing empty state.
- **An error says what happened and what to do next, in the interface's voice:** the locked-and-empty recipe, applied to failure. "Something went wrong" is a stub, not copy.
- **Each element does exactly one job.** A label labels, a caption explains, an example demonstrates. A label carrying a joke *and* the only statement of a rule is a design bug: whoever skims the joke loses the rule. Split it into two lines.
- **Where a joke and clarity conflict, clarity wins on anything acted on.** Voice lives in flavour text, prose, notifications and app names; not in the word on a button that commits money, or in the sentence explaining why something failed.

## Judgment discipline: push back, don't validate

**When the asked-for direction is weaker than one you can see, say so before executing, and present the alternative with its trade-offs.** On a solo project with no design team, this skill *is* the pushback. Hold the recommendation under mild pushback while the reasoning still stands; fold at once on a *decision*, record it as an override, and never re-litigate a settled call. **Never invent a UX statistic or cite an unnamed "study":** a fake number launders opinion as evidence. Open `references/judgment-discipline.md` before presenting a recommendation someone is expected to weigh: the reasoning, the evidence on models' agreeableness, and the self-critique loop.

## Mistakes to flag

- Visuals or mockups requested before a flow exists: produce the flow first.
- More than one competing primary action on a screen.
- A new visual pattern inconsistent with established surfaces, with no stated reason.
- UI placed outside the product's own fiction, or a new surface that cannot name its layer.
- Accessibility skipped because "it's just a prototype".
- A narrative beat designed to fire off a threshold instead of behind a tap.
- A locked or empty state that is only a greyed-out control, with no headline, reason or next step.
- An interactive element with no visible sign that it can be tapped.
- A screen that never says where its surplus height goes.
- A notification pitched louder (or quieter) than the information's urgency.
- A design with stakes in psychology or money that skips the second look.
- A consequential action with neither undo nor a question first that says what is lost; a question before every routine action.
- An action whose name changes between the control, the confirmation and the result.
- An error that says what failed without saying what to do next; a label carrying both a joke and the only statement of a rule.
- An in-fiction label that leaks an implementation noun.
- A UX claim propped up by an invented statistic or an unnamed "study".
- A direction validated because it was asked for, when a visibly stronger alternative went unmentioned.
- The same design correction absorbed twice without being written down.

## Engine layers

**Before you design screens for an engine or a page, open its file:** `references/unity.md` (the canvas contract, the safe area, and states in a project that builds its screens by script), `references/web.md` (responsive design, and designing the page around an embedded game build) or `references/unreal.md` (**not verified**, open questions only).
