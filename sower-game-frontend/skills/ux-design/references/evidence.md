# Evidence for ux-design (dated)

*Read this file before a figure or an incident from `SKILL.md` or one of its reference files is relied on or quoted. It says where each rule and line comes from, so that whoever maintains the skill can tell when one may go. Platform numbers change: read the page again before you rely on one.*

**Grades.** **Seen** = it happened on the source project, a Unity mobile game whose browser build went out as a public playtest in October 2026, and whose records and earlier skills this skill was written from: an incident, a measurement or a decision, with its record named. An earlier skill counts as the record of a case it names. "Shipped" in a note is that project's own word: the change was in the game's committed build. **D** = documented in a named source, read on the date given. **I** = inferred; the row says from what. A rule that an earlier skill states without naming a case is graded I, and a figure an earlier skill gives for how well a method worked is not kept without the record of its measurement. **The old file's statement** = an outside fact kept from the file as it stood before November 2026 and not read again: the line says "not checked at a source" and keeps no figure. Nothing here was measured: no design was tested with and without a rule.

## Sources read for this file

| Source | Read | What was read |
|---|---|---|
| W3C, Web Content Accessibility Guidelines (WCAG) 2.2, W3C Recommendation of 12 December 2024 (w3.org/TR/WCAG22) | 2026-11-22, the criteria named here, by script from the page | 1.4.3, 1.4.11, 2.3.3, 2.5.5, 2.5.8 |
| Apple, Human Interface Guidelines, "Accessibility" (developer.apple.com) | 2026-11-22, the page's data by script | the table of control sizes and the paragraph on padding |
| Android Developers, "Make apps more accessible" (developer.android.com) | 2026-11-22, by script | the paragraph on touch target size |
| Android Developers, "Behavior changes: Apps targeting Android 15 or higher" (developer.android.com) | 2026-11-22, by script | edge-to-edge enforcement and the display cutout |
| Nielsen Norman Group, "10 Usability Heuristics for User Interface Design" | 2026-11-12, in an earlier research round of ours; the sixth again on 2026-11-23, from the raw page by script | its summary and the first, third, fifth and sixth heuristics |
| European Commission, "Digital Fairness Act" (commission.europa.eu/law/law-topic/consumer-protection-law/digital-fairness-act_en) | 2026-11-22, the raw page by script | the proposal's date and its targets |
| Cheng et al., "Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence" (arxiv.org/abs/2510.01395) | 2026-11-22, the raw page by script | the abstract of its first version |
| Jakob Nielsen, "Parallel & Iterative Design + Competitive Testing = High Usability" (nngroup.com), 2011 | 2026-11-22, the raw page by script | the study's three figures |
| Zagal, Björk and Lewis, "Dark Patterns in the Design of Games", Foundations of Digital Games 2013 (gup.ub.gu.se/file/101018) | 2026-11-22, the PDF's text by script | its section on temporal dark patterns |
| Play Console Help, "Add preview assets to showcase your app" (support.google.com/googleplay/android-developer/answer/9866151) | 2026-11-22, the raw page by script | the requirements for screenshots |
| MDN, "<length> CSS type" (developer.mozilla.org/en-US/docs/Web/CSS/length) | 2026-11-22, the raw page by script | the small, large and dynamic viewport sizes |
| MDN, "Autoplay guide for media and Web Audio APIs" (developer.mozilla.org/en-US/docs/Web/Media/Guides/Autoplay) | 2026-11-22, the raw page by script | when a browser allows media to play on its own |
| Unity manual 6000.6, "Configure a Web Canvas size" (docs.unity3d.com) | 2026-11-22, the raw page by script | the default sync of CSS and render size, the two settings |
| itch.io, issue 58 on its public tracker, "HTML5 game not receiving keyboard focus", opened 2014 (github.com/itchio/itch.io/issues/58) | 2026-11-22, the raw page by script | the report and the fix its thread names |
| EUR-Lex (the Digital Services Act), the FTC's site (its staff report), the ACM Digital Library (King et al.) | 2026-11-22: no page served to an automated read, and none retried | nothing |

## Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Flow before visuals; the hand-off of flow, wireframe and states list | I | the source project's earlier design skill states the rule |
| Nothing narrative fires on its own | Seen | the source project's rule, with two recorded overrides: the intro tutorial (August 2026, the owner's call, reaffirmed twice) and a guided walkthrough of one feature (August 2026); `references/first-session-and-store.md` |
| Check what already teaches before writing a tutorial | Seen | the source project: an onboarding pass found two of three suspected gaps already taught by what existing screens showed (a persistent explainer for one mechanic, plain costs and results on the panels for the other), and shipped one static caption instead of three |
| One primary action; thumb reach | I | the source project's earlier design skill states the rule |
| Target sizes and padding | D | Android: touch targets of at least 48x48 dp. Apple: a default control size of 44x44 pt on iOS and iPadOS (the table also lists a minimum of 28x28 pt), about 12 pt of padding around a control with a bezel and about 24 pt around one without. WCAG 2.2: 2.5.8 (AA), 24 by 24 CSS pixels or enough spacing; 2.5.5 (AAA), 44 by 44 |
| Name where the surplus goes; the hole of about 450 units | Seen | the source project's canvas (1080 design units wide, about 1920 to 2520 tall) and the hole of September 2026, its record named in `ui-implementation`'s evidence |
| The top keep-out | D, Seen | Android 15's behaviour changes: an app targeting API level 35 is edge to edge by default on Android 15, and a non-floating window's cutout mode is treated as always. The source project kept content out of two named shapes by a guard over its screens, and one wide left-aligned heading crossed the camera box (the section on `references/unity.md` below) |
| The states list | I | the source project's earlier design skill states the rule |
| The mystery-lock rule | Seen | the source project: a physical prop in a room was mystery-locked on the owner's own call (August 2026, recorded as a reversal), while the screen listing the upgrades stays transparent, its design document calling it a planning screen, not a discovery mechanic |
| Four things for a locked or empty state | I | the source project's earlier design skill states the rule |
| A sign that a new element can be tapped | Seen | the source project: a review plan of July 2026 records that the rule had bitten twice |
| Inviting and informative signals | I | the old file attributes the distinction to Celia Hodent's game-UX writing, and the source project's research notes name it under her framework; her work was not read, so the skill states the distinction without the name |
| Undo or ask first; the four questions before handoff | D, I | the four heuristics read (visibility of system status, user control and freedom, error prevention, recognition rather than recall); the questions restate them for a wireframe, and the remedies are this skill's. On confirmations the skill is narrower than the source: it keeps a question for what cannot be taken back, and the question says what will be lost |
| Ground every proposal in the frozen tokens | I | the old file's reasoning that a model's first idea regresses to the generic; `references/new-visual-directions.md` |
| Palette, spacing scale, two font sizes | I | the source project's earlier design skill states the rule |
| Diegetic consistency and the layer of a new surface | I | the source project's design rules state it; no incident behind it was looked up |
| Restraint on outcome feedback; the live-instrument exception | Seen | the source project's design guardrails, with one recorded exception for a minigame's live window (August 2026) |
| Never colour alone | Seen, D | `ui-implementation`'s evidence: the badge read as a rendering glitch, and the study of AI design tools |
| Contrast | D | WCAG 2.2: 1.4.3 (AA), 4.5:1, and 3:1 for large text; 1.4.11 (AA), 3:1 for the cues that make a component and its state recognizable, and for the graphic parts the content depends on |
| Motion as an accessibility axis | D, I | WCAG 2.2: 2.3.3 (AAA), motion triggered by interaction can be switched off unless essential. That such motion can make people ill is WCAG's reason in its own guidance, which was not read for this file |
| Notification tiers; a transient surface's exit | Seen | the source project: the tiers in `references/notification-lifecycle.md`, the recorded exception that waits without a timer (August 2026), and the ticker that playtested as broken when it was disabled |
| Dark patterns as compliance | I | the skill now asks for the current law of each market instead of stating it; the legal background as last read is in `references/dark-patterns.md`, with its dates |
| No feature sells the recovery from a player's mistake | Seen | the source project's own boundary, in its instructions file |
| Lampoon, never deploy | I | the source project's earlier design skill states the rule, for a satirical game |
| A second look: design-review where installed, otherwise another reviewer; the reviewer says which check settled the verdict | Seen, I | the review plugin's agent; the source project ran such panels on its designs in July and August 2026, as `sower-review/EVIDENCE.md` records. That the reviewer says which check settled it is our inference: the records count no clean passes, so the skill names no expected verdict |
| Copy is half the design | I | the source project's earlier design skill states the rule |
| Push back; never invent a statistic | I | the source project's earlier design skill states the rule; the evidence on models' agreeableness is in `references/judgment-discipline.md`, dated there |

## Retired in November 2026

| Line | Why it went |
|---|---|
| "Touch targets >= 48x48dp (Material 3)" | the number holds on Android's own accessibility page; the Material page was not read |
| "~8pt of spacing between adjacent targets" | Apple's page gives about 12 pt around a control with a bezel; the 8 had no source |
| "on Android 15+ an app targeting SDK 35 is forced into LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS" | reworded to what the page says, for an app that targets Android 15; later versions were not read |
| "The distinction is Celia Hodent's games-UX framing" | the attribution was not checked; the distinction stays, without the name |
| "a documented motion-sickness trigger" | WCAG's guidance gives the reason, but it was not read; the criterion itself was |
| "the EU Digital Services Act Art. 25 applies now, and the Commission's Digital Fairness Act, expected to be tabled in Q4 2026" | the act was proposed on 11 November 2026 (`references/dark-patterns.md`, read again and dated there); the forecasts of its adoption and application had no source |
| "Found missing twice in post-hoc reviews of shipped work, both times because the wireframe never listed it" | the record says twice; the cause was not found |
| "validating a mediocre direction is the most expensive way it can fail" | a ranking with nothing measured |
| The heading "Mistakes to actively flag" | now "Mistakes to flag", as in the other skills |
| "a left-aligned header already clears it" in `SKILL.md` | `references/unity.md` had the counter-case and its section here had retired the claim: one wide heading crossed the box |
| The fourth wireframe question as "does any screen rely on remembering something from the screen before?" | its good answer was "no" where the other three pass on "yes", so "each no is a finding" flagged the screens that pass (an outside review of this repository, November 2026) |
| "A 'needs changes' verdict is the expected outcome of a real review" | an expectation with no count behind it; the planning skill's evidence has the record |
| "Use before building or changing anything a player sees" in the description | it also matched a change of look alone, which the same line leaves to `visual-craft` |

## references/dark-patterns.md

Dates of the sources the file read again are in the file; the rows do not repeat them.

| Line | Grade | Behind it |
|---|---|---|
| The Digital Fairness Act, a proposal | D | the European Commission's page on the act, read from the raw page by script |
| The Digital Services Act and the FTC's staff report | the old file's statement | EUR-Lex and the FTC's site served no page to an automated read on 2026-11-22, so neither was read again |
| A predatory satire is read as the thing it mocks | Seen | the source project's design guardrails |
| The six categories | I | second-hand: the source project's research notes cite the study as a survey of players (Proc. ACM HCI, DOI 10.1145/3611053), with a count of respondents that is not kept; the publisher's page served no automated read |
| The endowment-effect setup, stopped in review | Seen | the source project's history: a design review before building dropped the idea of gating an offline recap behind an ad, and at that stage the recap stayed free |
| Temporal dark patterns | D | Zagal, Björk and Lewis, Foundations of Digital Games 2013, the full text, its section on temporal patterns |
| A schedule that clamps | Seen | the source project's economy model, August 2026 |
| Two recorded overrides | Seen | the source project's design guardrails: an opt-in ad that cannot be skipped once started, and the shop and settings as the only screens written straight |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| The Digital Fairness Act "expected to be tabled Q4 2026", with "adoption around late 2027 and staggered application from 2028" | it was proposed on 11 November 2026; the forecasts had no source read for this file |
| "the EU Digital Services Act Art. 25 has applied since February 2024", as a rule for the reader | whom it binds was not read; the file names it as the old file's statement |
| "A satirical product about greed gets zero benefit of the doubt, and neither does anything aimed at a young audience" | an effect nobody measured; the guardrails' argument stays |
| "six categories observed in real 3D-gameplay contexts" | the study surveyed what players perceived |
| "subtle enough to arrive by accident" | the recorded case was an idea stopped in review |
| "a review that always comes back clean is a signal to question its rigor" | it was the planning skill's rule, which has gone from there too: no count of clean passes stands behind it. This file points to the second look |
| "a store page written deliberately straight" | the record is the shop and settings screens inside the game |

## references/judgment-discipline.md

| Line | Grade | Behind it |
|---|---|---|
| Models affirm users' actions more than people do | D | Cheng et al., arXiv 2510.01395, the abstract of its first version, read from the raw page |
| Dropping a correct answer under pressure | I | the old file's reasoning; the source project's research notes call it regressive sycophancy |
| The habits | I | the old file's practice, and SKILL.md's rule |
| Twice as the threshold | I | this skill's choice; the source project's research notes advise writing it down at the first correction |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "AI affirmed users' actions ~49% more often than humans did (Cheng, Jurafsky et al., Science 2025)" | the abstract read gives 50%; the journal version was not read |
| "validating a mediocre direction is the most expensive way it can fail" | a ranking with nothing measured, retired from SKILL.md too |
| "A one-shot design that skips its own critique loop is where both the generic look and the missing state come from" | a cause nobody showed |
| "A correction made twice is a rule that was not written down", as a fact | the threshold is this skill's choice |

## references/new-visual-directions.md

| Line | Grade | Behind it |
|---|---|---|
| The generic first idea | I | the old file's reasoning; nothing measured |
| The parallel-design figures | D | the article by Jakob Nielsen (2011), read from the raw page |
| A pick against the plan | Seen | the source project's design archive: a three-way render, and the owner's pick was not the recommended option |
| The job card's reveal timing | Seen, I | the source project's history (the card shows only the guaranteed fee); the delivery-app reasoning is the project's own |
| The rating repeated on the result screen | Seen | the source project's milestone specs and history: the run screen echoed the customer's pre-rolled rating, with no connection to the run, until a real rating for each run replaced it |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "no clever one-shot prompt escapes it" | a claim nobody tested |
| "Parallel-then-pick measurably beats a single first idea", and "it keeps producing this result in practice" | the study compares the best of four with the average of four; the source project holds one case |
| "works because that is exactly how real gig-delivery apps sequence the same information" | the project's reasoning, now graded I |
| "Two similarly-styled displays read as connected, even when nothing links them", and "Nothing in the code linked them; the styling did all the lying" | the record shows one number reused on a result screen, not two numbers read as one |
| "A 3D scene or a new environment has defaults of its own, covered in" the visual skill's new-surface file | that file holds three looks from a list about generated pages; environment structure is in its `procedural-environments.md`, which the pointer now names |

## references/notification-lifecycle.md

| Line | Grade | Behind it |
|---|---|---|
| The badge and the pulse | Seen | the source project's design archive and design document |
| The ticker, and its one exception | Seen | the source project's bug register: a tap on the ticker threw away a verdict card unread; fixed in September 2026 |
| The headline gap and its history; pending intent; a chained story's window; the fill bar | Seen | the source project's milestone specs, and its economy model for the fill bar of 20 August 2026 |
| The auto-close deleted; the arm of 0.6 seconds | Seen | the source project's session log, August 2026 |
| Nothing pending behind the card | Seen | the same log, and the bug register's fix |
| The disabled tint; the one exception | Seen | the source project's history: the ticker playtested as broken when disabled; a key shown disabled in one short, consented, skippable walkthrough was a recorded reversal |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "a minimum gap (~45s) between natural events", as the live value | 45 seconds was the first version, 30 seconds came on 7 August 2026, and a fill bar has been the schedule since 20 August 2026 |
| "Design it fully tappable *everywhere*" | the ticker cannot be reached while a verdict card is up |
| "three beats landing within seconds ... and a milestone beat gets buried by a routine one" | the record is headlines landing within seconds of each other |

## references/first-session-and-store.md

| Line | Grade | Behind it |
|---|---|---|
| 15 to 30 seconds to meaningful feedback | Seen | the source project's design guardrails |
| A lock-out tutorial as a repeated complaint | I | the source project's market research of August 2026, from players' discussions |
| Override 1 | Seen | the intro tutorial's plan of 5 August 2026 and its second round of review findings; the rebuild from scratch on the owner's call, 10 August 2026 |
| Override 2; rule of three | Seen | the source project's session log, August 2026 |
| The first week | I | the old file's framing; nothing measured |
| The gap between thresholds | Seen | the source project's design guardrails: found and fixed once |
| Google Play's screenshots | D | Play Console Help, "Add preview assets to showcase your app", read from the raw page |
| Screenshot order; experiments | I | the old file's reasoning |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Install day is where most churn happens", and the vendor guidance tying the first 60 to 90 seconds to D1 retention | a frequency, and a vendor's figure not read at its source |
| "both softenings then produced real defects - a player could grind past the beat meant to advance them, and the guarded control could be wandered away from" | both defects belonged to one softening; the other had its own |
| "the two clones' duplicated shield/highlight geometry" | the intro's geometry and its one clone |
| "it is also the idle/tycoon genre's own retention engine" | a claim about the genre with no source |
| "roughly 90% of visitors never scroll past them" | no source found |
| "Google Play requires 4+ real-gameplay screenshots at 1080px or better, never mockups" | the help page asks for 2 to 8 phone screenshots of 320 to 3,840 pixels; at least 4 is for large screens |
| "a mid-session progress reset is unshippable" | now "in the middle of a game": the intro restarts from its start, where that is harmless |

## references/unity.md

| Line | Grade | Behind it |
|---|---|---|
| The canvas contract | Seen | the source project's glossary and session log |
| The dialogue box's hole, six passes, every harness at one shape | Seen | the session log of September 2026 |
| Tablets as a phone with margins | Seen | the session log: the interface is a phone inside the fiction |
| The black bar across three rounds; the keep-out shapes; one wide heading | Seen | the milestone specs and the history |
| The safe area in the Editor, and the reverted fix | Seen | the task archive: a fix of July 2026 reverted over "no visible change", confirmable only on a device |
| The Device Simulator | the old file's statement | not read again |
| The builder overwrites the screen; a shell filled once | Seen | the earlier frontend skill names both cases; the session log |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "1080x1920 is the common choice" | a frequency nobody measured; the file says what the source project used |
| "~2400 (the modal Android phone)" | no census of shapes was found; 20:9 is the shape |
| "and which no shipping Android phone produces" | the records disagree with each other |
| "tablets need no separate layout ... tall phones, which is all of them" | true for a product whose interface is a phone inside the fiction |
| "a left-aligned header already clears the camera box" | one wide heading crossed it |
| "One dialogue dock" | a dialogue box, as SKILL.md says |

## references/unreal.md

| Line | Grade | Behind it |
|---|---|---|
| The open questions | - | questions, not facts |
| An app that targets Android 15 is drawn edge to edge | D | Android's page, in the table "Sources read for this file" above |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| The paragraph naming UMG, Slate and CommonUI as "factually established from documentation only" | not read; SKILL.md says this file holds open questions only |
| "SDK 35 forcing `LAYOUT_IN_DISPLAY_CUTOUT_MODE_ALWAYS`" | worded to Android's page, as in SKILL.md |

## references/web.md

| Line | Grade | Behind it |
|---|---|---|
| Viewport units | D | MDN, "<length>", read from the raw page |
| WCAG 2.2 targets | D | in the table "Sources read for this file" above |
| WebGL2 over WebGPU; the landscape window; about 167 MB; what was shipped | Seen | the source project's notes on its web build, September and October 2026 |
| Pixel Streaming; iOS memory; the safe area in a canvas | the old file's statement | not read again; no figure kept |
| Keyboard focus in an iframe | D | itch.io issue 58, read from the raw page |
| The canvas size settings | D | Unity's manual for 6000.6, read from the raw page |
| Autoplay | D | MDN's autoplay guide, read from the raw page |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "None of the `svh`/`dvh`/`lvh` units are affected by the virtual keyboard" | not on MDN's page; the practitioner's blog was not read again |
| "or 24px spacing" | WCAG's wording is enough spacing |
| "the AA floor is a legal minimum" | a conformance level |
| "half the traffic" | a share nobody measured |
| "letterboxing it inside a landscape page is usually correct" | the record shows what the project did, not what is usual |
| "A game build is tens of megabytes" | the record gives about 167 MB for the first export |
| "the single most-reported problem with embedded browser games" | a ranking with no source |
| "roughly the 300-500 MB range", "target a 256 MB memory size", "some devices fail above ~384 MB" | a practitioner's figures, not read again |
| "We have not shipped a production embedded game page" | the browser build went out as a public playtest in October 2026 |

