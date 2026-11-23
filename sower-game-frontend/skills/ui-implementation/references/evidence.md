# Evidence for ui-implementation (dated)

*Read this file before a figure or an incident from `SKILL.md` or one of its reference files is relied on or quoted. It says where each rule and line comes from, so that whoever maintains the skill can tell when one may go. Engines, browsers and platforms change: read the page again before you rely on a version-bound line.*

**Grades.** **Seen** = it happened on the source project, a Unity mobile game whose browser build went out as a public playtest in October 2026, and whose records and earlier skills this skill was written from: an incident, a measurement or a decision, with its record named. An earlier skill counts as the record of a case it names. "Shipped" in a note is that project's own word: the defect was in the game's committed build. **D** = documented in a named source, read on the date given. A few D rows rest on an earlier research round of ours; the row gives that date and says the source was not read again. **I** = inferred; the row says from what. A rule that an earlier skill states without naming a case is graded I, and a figure an earlier skill gives for how well a method worked is not kept without the record of its measurement. **The old file's statement** = an outside fact kept from the file as it stood before November 2026 and not read again: the line says "not checked at a source" and keeps no figure. **(questions)** marks lines that ask rather than claim. Nothing here was measured: no project was built with and without a rule.

## Sources read for the reference files

| Source | Read | What was read |
|---|---|---|
| Unity manual 6000.6, "Comparison of UI systems in Unity" (docs.unity.com) | 2026-11-22, the raw page by script | the runtime recommendation and the table of features |
| Unity manual 6000.6, "Managed code stripping" (docs.unity.com) | 2026-11-22, the raw page by script | the linker's static analysis, the configurable level, the annotations that preserve code |
| Unity scripting reference 6000.6, `Screen.safeArea` (docs.unity.com) | 2026-11-22, the raw page by script | the description, the note on the application window, Android 15, the origin at the bottom-left corner |
| Unity manual 6000.6, "Configure a Web Canvas size" (docs.unity3d.com) | 2026-11-22, the raw page by script, read for `ux-design` | the default sync of CSS and render size, the two settings |
| TextMeshPro package manual 3.2.0-pre.15, "UI Text GameObjects" and "Line metrics" (docs.unity3d.com/Packages/com.unity.textmeshpro@3.2) | 2026-11-22, the raw pages by script | Auto Size and its tip; the overflow modes; the line metrics and the baseline. The source project ran Unity 6000.5 with uGUI 2.5.0 and no separate TextMeshPro package, so the manual read is the older package's |
| type.today, "Vertical metrics" (type.today/en/journal/verticalmetrics) | 2026-11-22, the raw page by script | how a text's position depends on the vertical metrics a browser or program relies on |
| Unity Learn, "Optimizing Unity UI" (learn.unity.com) | 2026-11-22: the address leads to a deprecation notice | nothing |
| Yaron Minsky, "Effective ML Revisited", Jane Street's blog, 9 March 2011 (blog.janestreet.com) | 2026-11-22, the raw page by script | the phrase and the talk it revisits |
| Alexis King, "Parse, don't validate", 5 November 2019 (lexi-lambda.github.io) | 2026-11-22, the raw page by script | what a parser is, and the difference between validating and parsing |
| arXiv 2511.21654 (EvilGenie), 2501.03572 (a case study of GPT-4o) and 2503.20197 (version 4, a study of code robustness) | 2026-11-22, the abstract pages by script | the abstracts |
| itch.io, issue 58 on its public tracker, "HTML5 game not receiving keyboard focus", opened 2014 (github.com/itchio/itch.io/issues/58) | 2026-11-22, the raw page by script | the report and the fix its thread names |
| MDN, "<length> CSS type" and "Autoplay guide for media and Web Audio APIs" (developer.mozilla.org) | 2026-11-22, the raw pages by script, read for `ux-design` | the viewport sizes and what `vh` equals; when media may play on its own, and the rejected `play()` |
| Epic, Unreal Engine 5.9 documentation, "Pixel Streaming in Unreal Engine" (dev.epicgames.com) | 2026-11-22, the raw page by script, read for `3d-assets` | what Pixel Streaming does |
| "Generated Inaccessible: Measuring WCAG Violations in AI UI Design Tools" (W4A 2026); EvilGenie's full text | 2026-10-04 and 2026-10-02, in earlier research rounds of ours | not read again for these files |
| arXiv 2412.08109 | 2026-11-22, the abstract page by script | its subject: a benchmark built from obfuscated code, to test models on code they have not seen, not a study of happy-path bias; the citation is retired (`references/timing-and-verification.md` below) |

## Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Design away the bug class: the navigation stack and the shared formatter | Seen | the source project replaced a hide-list with a navigation stack, and inline number formatting with shared formatters after the class recurred (rows below) |
| Comments eight lines from the bug they record | Seen | the source project, July 2026, two builder scripts. In one, a comment recording a wrapping-text fix of 20 July sat eight lines above an element that shipped the same bug again on 26 July. In the other, an audit of 30 July found a comment describing the same fix eight lines below a call whose email subjects overflowed their slot |
| The limit: constrain what has bitten | I | the counter-argument named in `references/timing-and-verification.md` §0; no over-constrained model on the source project was looked up |
| 1. UI is never logic; a screen controller as a deep module | I | the source project's earlier frontend skill states the rule, as its first hard rule |
| 2. Events, not polls; unsubscribe; a lazy peer lookup; a one-time sync | I | the source project's earlier frontend skill states the rule; the ordering incidents are in the next row |
| 2. No assumed initialization order | Seen | the source project: three separate times by July 2026 (a reveal on the HUD, a poll of offline income, a gap in a screen's reveal), as its earlier systems skill records them; its session log of 7 August 2026 counts a fourth, in a tutorial's overlay and pop-up |
| 3. One owned unit per screen | I | the source project's earlier frontend skill states the rule |
| 4. One named destination for surplus space, never a text element | Seen | the source project, September 2026: one screen's line text had a flexibility flag so that auto-sizing had a box to shrink in, and took the surplus. Its box measured 142 units at the 1080x1920 design canvas and 622 on a 20:9 phone, a hole of about 450 units |
| 5. Input abstracted once; the hit area apart from the art | I | the source project's earlier frontend skill states the rule and describes that project's input this way: one set of tap zones defined in one place, invisible hotspots over 3D props |
| 5. One idempotent reset for every release path of a hold | I | the release paths were listed in a plan's amendment when the source project built its first hold input (July 2026); no record of a held action left running was found |
| 6. Follow settled patterns | Seen, I | the five settled layout choices in `references/timing-and-verification.md` §2: four rest on a named case of the source project, and the two-element row on its earlier skill's rule alone |
| 6. Read the toolchain before applying a rule | D, I | the idea comes from a public skills repository (vercel-labs/agent-skills) read in our research round of 2026-11-11 and 2026-11-12; carrying it over to engine settings is our inference |
| 7. Throttle a polled walk; split slow data; guard hot-path logging | Seen | the source project, July 2026: a new per-frame poll computed net worth up to seven times in one frame; after the owner asked what it cost it was throttled to about once a second, and the sweep the owner asked for found two more, an identical unthrottled call in another trigger and a per-frame scan over every stock and position |
| 8. No wrapping text in a fixed-size container | Seen | the source project, July 2026: three instances shipped on 26 July (a company blurb, an article's header slot, a deep-link button) on top of two fixed on 20 July, five in all by that day; an audit four days later found the class again, in two email subjects, and later checks found more: a hire panel's name slot on 1 August, and 34 of 83 dialogue lines overflowing their card in early August. A news row whose own comment assumed three lines were enough needed four for real headlines. The measured cases: `references/unity.md`, "TextMeshPro" |
| 8. TextMeshPro's default overflow mode does not clip | Seen, D | the source project's measured cases; its records name Overflow as the default. TextMeshPro's manual (3.2.0-pre.15, read 2026-11-22) describes the Overflow mode and does not say which mode is the default |
| 9. An overflow effect clipped by a masked parent | Seen | the source project, August 2026: a new glow first overlapped its neighbours; a smaller spread read as a muddy band and a tighter mask as a frame, and both were reverted. A list row's glow was then cut off by its scroll viewport's mask until the mask's padding was widened, and a scoped audit the same day found no other site with the risk |
| All states, with loading | I | the states list is `ux-design`'s; loading was missing from the old file's list and is on that one |
| A sign that a new element can be tapped | Seen | the source project: a review plan of July 2026 records that the rule had bitten twice |
| One state value over accumulated booleans | I | the old file's rule; no incident was looked up |
| One shared formatter that names its culture; a machine-written value parsed invariant; never parse a literal | Seen, I | the source project, July 2026: a batch of new materials parsed "0.55" as 55 under a culture where the point is not the decimal separator, and rendered blown-out white. Its bug audit file records the class as shipped three times; audits of 30 July and 1 August 2026 found a fourth and a fifth case, after the shared formatters existed. That project's interface has one language, and its formatters name the invariant culture; that the rule for any project is the interface language's culture, and never the machine's, is our inference, made when an outside review of November 2026 asked whose style the rule sets |
| Displayed value equals credited value; one call for two readouts | Seen | the source project, August 2026: both delivery cards' fee previews left out a multiplier the payout applied (found and fixed on 7 August), and a building's income line per track left out a multiplier its own total included (found and fixed on 20 August; the multiplier itself was removed the next day, and the fix stands as one formula for both readouts) |
| Colour never carries meaning alone | Seen | the source project: a plain coloured badge was read as a rendering glitch twice and was removed |
| A glyph missing from the font atlas | Seen | the source project, by August 2026: four instances, three fixed by hand and the fourth caught by a new guard test on its first run. One record says a missing glyph gives no console warning and another names a glyph warning in the console, so the skill claims neither |
| Write a text only when its shown value changes | Seen | the source project's bug register: a fix that compares with the last value written before writing |
| Right-sizing; no framework migration mid-project | I | the source project's earlier skill states the rule; the framework choice and its reasons: `references/unity.md` |
| Hit-testing off on elements that take no input | I | the source project's earlier skill states the rule, in its Unity layer |
| The study of AI UI design tools | D | "Generated Inaccessible: Measuring WCAG Violations in AI UI Design Tools", Web for All conference (W4A) 2026: 54 designers, six AI UI design tools, 21,880 assessments over five WCAG criteria; 29.0% compliance overall; specifying accessibility in the prompt lowered it. Its page was read on 2026-10-04, in an earlier research round of ours, and not again for this file. It measured design tools, not code-writing agents |
| Accessibility as computed checks | I | from the study above: asking did not raise compliance, so the check is computed |
| A hit-tested click, never an invoked handler | Seen | the source project's earlier skill and its verification plans: a raycast, with a frame boundary after activation |
| The agent that wrote a check does not certify it | I | the reward-hacking benchmark behind it is in `references/timing-and-verification.md` §4, with its figures from our research register (read 2026-10-02) and its abstract (read 2026-11-22) |
| A capture at one screen shape | Seen | the source project, September 2026: every capture harness rendered only 1080x1920, and six visual passes and a conformance sweep read that shape while the hole of rule 4 sat on real phones |
| Activation and `Start()` | Seen | the source project, August 2026: a click test read a builder's placeholder text because it activated the screen and clicked in the same call; a later call read the real text |
| Force a layout pass before reading measured positions | Seen | the source project's standing lesson in its milestone specs: Unity defers UI layout, so a rect read on a screen's first activation can be stale or zero, and an element activated in the same editor tick sat at its pre-layout position, invisible to the raycaster |
| Edits during a live play session revert | Seen | the source project: work lost this way four separate times, as a plan of 1 August 2026 records; the first two, in consecutive sessions, were a desk moved and then a camera tweaked, each against a live screenshot |
| A hidden screen's camera | Seen | the source project: a disable ran before the rig reference resolved and did nothing, so the camera kept rendering; separately, a room camera rendered behind the whole intro tutorial until a fix in September 2026 |
| Projected every frame; the size in the position's space | Seen | the source project, August 2026: hotspots placed by projection but sized as a fraction of their area overlapped on taller screens, where a tap fired the later sibling; two earlier repairs had measured the constants again at one shape |
| A lifecycle handler that fires twice | Seen | the source project, September 2026: a bug audit confirmed that a recap set on resume, which no screen ever showed, froze the save's time anchor, so the player's next real launch paid a full capped offline recap twice (rated high, reachable in routine play). An August audit had found a related path through failed saves |
| An editor tool runs the last good build | Seen | the source project: four ways, recorded in its glossary (stale prefab rebuilds twice in one milestone; a recurrence that passed a check of play mode and an empty console and was caught only by reading the rebuilt prefab, which the milestone history dates to 5 August 2026; two map bakes that ran old code while a second session's compile errors sat in the shared editor, July 2026) |
| A measurement taken once | Seen | the source project, September 2026: a root controller capped the layout against a stale canvas rect and kept the cap |
| The mockup's literal values are the spec | Seen | the source project's design import rounds of August 2026, from which the pipeline in `references/design-import-pipeline.md` was written |
| A radius snaps to an existing tier | Seen | the source project, August 2026: a new surface helper hard-coded its own corner radius while older screens kept a 16-pixel frame, so two card radii shipped side by side until a migration ended it |
| Alpha measured in the renderer's colour space | Seen | the source project, August 2026: a border's alpha of 0.10 in the mockup measured 0.025 in the engine on 24 August, the lift of a linear colour space, and 0.020 when measured again on 27 August over a new card surface; the code carries 0.020 with the second probe's readings |

## Retired in November 2026

| Line | Why it went |
|---|---|
| "a leaked subscription is the classic UI bug in every engine" | a claim about every engine with no source; the rule now says what a leak does |
| "the symptom is always silence rather than an error" | "always" claimed more than three cases show; the three are named |
| The target sizes in rule 5 (48x48dp, 44x44pt, and WCAG's 24x24 as "a legal floor") | `ux-design` holds the numbers; "a legal floor" had no source |
| "one of the most widely reproduced C#/Unity bugs there is, which is exactly why it is also the default an LLM reaches for" | a claim and an inference stated as fact; the reference keeps the graded version |
| "LLM UI output has measured weaknesses ... the strongest argument they are load-bearing" | the study measured design tools, not code-writing agents, and nothing measured which argument is strongest |
| The four weaknesses with their figures in the main file (26.8%, 19.2%, "benchmarked at material rates") | the study's headline stays, with its scope; the other figures and the benchmark are in `references/timing-and-verification.md` §4 |
| "two card radii side by side for weeks", and "That shortcut is what produced" them | the record gives no duration, and it shows a helper that brought its own radius, not an agent that built by eye |
| "found twice in post-hoc reviews" | the record says the rule had bitten twice, not how each case was found |
| "the finger sliding off a button leaving the game permanently accelerating" as the named failure | no record of it happening was found; the rule now states the consequence |
| "Disable interactive elements during in-flight operations" | no record of a double fire was found, and a rule with no failure behind it goes |
| A missing glyph "renders as a silent blank or box, with no console warning" | the records disagree about the warning |
| "In the engine we have measured" | the engine is named |
| The pointer that put layout groups in `references/unity.md` | they are in `references/timing-and-verification.md` §2; rule 6 points there |
| The heading "Mistakes to actively flag" | now "Mistakes to flag", as in the other skills |
| "one shared formatter with a fixed culture" (the invariant one) as the rule for every project | the invariant culture is the source project's choice for its one language; another interface language, or a localized product, formats for that language on purpose |
| "implement the others" for every state a request leaves out | a state nothing can put the element in was built as dead interface; the rule now asks what can cause each state |

## references/unity.md

| Line | Grade | Behind it |
|---|---|---|
| uGUI with builder scripts; the argument for staying | Seen, I | the earlier frontend skill records the choice; a research note of 26 August 2026 gives the argument |
| Unity's comparison of UI systems; the safe area's origin for UI Toolkit | D | the two Unity pages named in the lines |
| Events and builder scripts in place of a view-model layer | I | from the comparison's row on a data binding system |
| The canvas: 1080 by 1920, `matchWidthOrHeight` at 0 or 1, the cap at 1080, the heights | Seen | the source project's glossary |
| The blend of 0.5, and the grid of 984 units in a canvas of 966 | Seen | the session log of 4 August 2026 |
| The slack contract's mechanics, the spacer helper and the guard | Seen | the glossary and the guard tests it names |
| The flag that opened the hole of rule 4 | Seen | the glossary; the hole's own row is in the table above |
| One change dirties the whole Canvas | the old file's statement | after a Unite talk of 2017, not read; Unity's tutorial on its UI now leads to a deprecation notice |
| Sub-canvases, disabling, one font asset and preset | I | from that cost model |
| Raycast Target: a cost per touch; the 36 entries | Seen | an audit of 1 August 2026 |
| Auto Size; the Overflow mode | D | TextMeshPro's manual, as the lines name it; the default mode is the source project's records', not the page's |
| Five instances by 26 July 2026; the later audits; 34 of 83 dialogue lines | Seen | the glossary (the five, with their sizes); audits of 30 July and 1 August 2026; the session log of early August |
| The text component reports its own height; the deletion the audit of 30 July prescribed | Seen | the audit of 30 July 2026, which names the two earlier fixes in the same file |
| The procedure for measuring | Seen | the audit of 30 July 2026, whose first attempt read a prefab's rects as authored and reported all 247 headlines overflowing |
| The navigation stack and its coverage test | Seen | the glossary |
| The full-sweep helper | I | the earlier skill states it |
| Back presses, and the two audits that changed them | Seen | the design archive, 16 August 2026; the bug register, 20 August and 3 September 2026 |
| Builders overwrite; peers found in `Start()`; the scene-side data | Seen | the earlier frontend skill |
| A builder runs the last compiled assembly | Seen | the glossary: four ways |
| The layout pass on first activation, and its two limits | Seen | a verification plan of 31 July 2026; the session log of 4 August 2026 (the fitter); the 3D pipeline notes, July 2026 (the depth of -1) |
| The bottom inset, the top keep-out and its guard; the bars removed on 30 August 2026 | Seen | the earlier frontend skill and the milestone history |
| Tap zones defined once | I | the earlier skill describes the project's input |
| The hold component and its release paths | Seen | the milestone history, July 2026 |
| `IPointerExitHandler` without a pointer up | the old file's statement | not read again |
| A cancelled touch through the pointer-up handler | I | the milestone history states it, July 2026; not tested on its own |
| The hit area from the bounds; the hotspot rig; a prefab cannot reference a scene object | I | the old file's rules |
| The raycast click; stepping frames in an editor driven through a bridge | Seen | the earlier skill; the 3D pipeline notes |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "every rule here is attached to something that happened" | several of its rules are graded I |
| UI Toolkit "has no uGUI-parity animation story" | Unity's comparison now says which animation features each system has |
| "~2400 on the modal Android phone" | no count of phone shapes stands behind "modal"; the line gives 20:9 |
| "(Dundore/Harkness, "Squeezing Unity", Unite Europe 2017 - Unity's own guidance)" | the talk was not read, and the line says so |
| "a free win against per-frame raycaster cost" | the record: the cost is per touch, not per frame |
| Auto Size "thrashes the font atlas" | the manual says it lays out the text several times; the atlas claim was not found |
| A missing glyph renders "with no console warning" | the records disagree; `SKILL.md` keeps the rule without the claim |
| "the most-repeated soft-lock bug class in the project's history" | a ranking; two records each call a different thing the most repeated |
| "A builder rebuild run mid-Play (or during a compile)" | the record names compile errors and unfinished recompiles |
| "The Device Simulator is the only in-editor surface that reproduces real notch shapes"; "A correct fix was reverted once" | the records disagree; `references/release-hardening.md` gives what the later record says |
| "A raw `:F2` ships a comma decimal on any non-English locale" and the rest of the formatting section | `SKILL.md`'s data-binding rule holds it, in words the record supports |
| The paragraph on the thin-wrapper test for builder scripts | `SKILL.md` holds it |

## references/web.md

| Line | Grade | Behind it |
|---|---|---|
| What transfers; never parse a formatted string | I | the core skill's rules, read for the DOM |
| `100vh` is the large viewport | D | MDN's page named in the line |
| Layout thrash | the old file's statement | not read again |
| WebGL2, decided 9 September 2026; about 167 MB for the first export; one uncompressed build, 5 October 2026; the public playtest in October 2026 | Seen | the source project's notes on its web build. At the commit the itch.io build was made from, the setting reads 2 with the decompression fallback off, which the notes confirmed as Disabled through the API; their status line of 8 October calls the upload gzip, which by the section it points to is itch.io's own compression on demand |
| Pixel Streaming; the canvas size settings | D | the pages named in the lines |
| The pixel ratio as a cheap first try | I | from the canvas page; nothing was measured |
| Keyboard focus in an iframe | D | the itch.io issue named in the line |
| The three parts of the fix | I | the old file's method |
| A Brotli build needs the header | the old file's statement | not read again |
| iOS Safari's WebGL memory; the safe area inside a canvas | the old file's statement | not read again; no figure kept |
| Autoplay and the rejected `play()` | D | MDN's guide named in the line |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "a `useEffect` without a cleanup is its most common modern shape" | a ranking with no source |
| "`parseFloat` on a localized string is the same trap wearing different syntax" | not read at a source; the rule now says what never to parse |
| "None of `svh`/`dvh`/`lvh` respond to the virtual keyboard", with its link to a practitioner's blog | not on MDN's page; the blog was not read again |
| "24x24 CSS px or 24px spacing" and the platform figures | `ux-design` holds the figures, with WCAG's exception for spacing |
| "since UE 5.2 the frontend is a modular TypeScript library" | not on the page read |
| "renders at 2-3x the pixels for no visible gain"; "usually the right first move" | a figure and a frequency nobody measured |
| "Input focus - the most-reported embedded-game bug" | a ranking with no source |
| "A build is tens of megabytes" | the record gives about 167 MB for the first export |
| "a misconfigured server silently falls back to serving the compressed file as-is" | no record of it; the project's decision is kept |
| "300-500 MB", "256 MB", "384 MB", and audio occupying "hundreds of MB" in Safari | a practitioner's figures, not read again |
| "We have not shipped a production embedded game page" | the browser build went out as a public playtest in October 2026 |

## references/unreal.md

| Line | Grade | Behind it |
|---|---|---|
| The open questions | (questions) | the Unity layer's findings, each asked of Unreal |
| Do not infer an Unreal answer from the Unity file | I | the two stacks need not share an architecture; nobody compared them |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| The paragraph naming UMG, Slate, CommonUI and `BindWidget`, "Established from documentation only" | not read; `SKILL.md` says the file holds open questions only |
| "UMG property binding is documented as evaluated per frame" | not read |
| "This is the most expensive Unity bug in this plugin; finding its Unreal shape ... is the highest-value first answer" | a ranking nobody measured; the question still comes first, for its silent failure |
| "the two UI stacks do not share an architecture" | stated as a fact; now "need not", graded I |
| "Is there a Retainer Box / invalidation-panel discipline worth writing down?" | it names Unreal features nobody read about; the performance question stays |

## references/timing-and-verification.md

| Line | Grade | Behind it |
|---|---|---|
| Minsky's phrase; King's method | D | the two pages named in the line |
| Feldman's talk; Goedecke's counter-argument | the old file's statement | not read |
| The stack and the formatters as the two cases; five occurrences by August 2026 | Seen | the rows of `SKILL.md` above |
| A guard against raw format calls | I | the rule follows from the two later recurrences; the source project's edit-mode tests scan source code for missing glyphs and for flat fills, and for no format call |
| A covered camera; the camera on from startup | Seen | the bug register, 3 September 2026 |
| The output on disk; partial-write staleness | Seen | the source project's glossary |
| What hid the first play-mode loss, and what caught the second | Seen | the source project's archived instructions |
| A placeholder string means "too early" | Seen | a decision log of August 2026 |
| The trigger that registers intent; the count-based flag | Seen | the news plan of 22 July 2026, and the earlier skill, which names the built shape |
| A hold never released | Seen | the bug register, 22 September 2026 |
| An unbalanced clear | I | the earlier skill names it; no case was found |
| (a) the shell filled once | Seen | the earlier skill names the case |
| (b) the two-element row | I | the earlier skill states the rule with no case; the fix by direct anchoring is (d)'s second case |
| (c) the fixed group that compresses | Seen | an audit of 1 August 2026: the third tier panel, without the scroll shell its siblings had, measured against the line box (a retraction in the same audit puts the ink at about 75 to 80% of it); the same file records the fix |
| (d) zero flexibility, and its two cases | Seen | the milestone history: a header and a controls row; later, a card stretched from 250 px to 798 px |
| (e) the overlay exception | Seen | the bug register's scoped audit of 10 August 2026 |
| The vertex count, the negative width and the screenshot; the hand-rolled header | Seen | the session log of 26 July 2026 |
| The atlas's sampling point size | the old file's statement | our research synthesis of August 2026 quoted it from a developer's blog; not read |
| The study of AI UI design tools | D | read 2026-10-04 in an earlier research round of ours, as the line says |
| The case study of GPT-4o; the study of code robustness | D | the abstracts named in the lines |
| EvilGenie | D | the full text as our research register read it (2026-10-02) and the abstract (2026-11-22) |
| Magic-number layout | I | practitioners' reports, as the line says |
| §5: the four shapes, and the shape in between that was dropped; the two traps | Seen | the session log of September 2026 |
| Pseudolocalization | I | the method; no figure kept |
| Screenshots as a signal | I | from §3 and §4 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "The practitioner career ladder converges from the other direction ..." | an opinion with no source, which nothing in the skill acts on |
| "the single most-repeated soft-lock bug class in one project's history" | a ranking with no record |
| Inline formatting "recurred three separate times before a shared formatter became the only route" | the record counts five by August 2026, the last two after the formatters existed |
| "Every rule in the core skill is attached to a real incident" | the core skill grades several rules I |
| "one builder script documents its own earlier wrapping-text fix eight lines above an element" | there were two scripts, as `SKILL.md` says |
| The camera's cost "not scene size or geometry complexity" | a comparison nobody measured |
| Play-mode edits "bit one project twice" | four times, as `SKILL.md` says |
| Activation's callback "fires on the next tick" | `SKILL.md` words it for `Start()`, as the record shows |
| (b)'s "repeated squeeze/overlap results that read as random" as a case | the earlier skill names none; the line says so |
| §4's grades "STRONG", "MODERATE-STRONG", "MODERATE" and "THIN" | this skill's grades replace them |
| "arXiv 2412.08109 among them" | that paper is a benchmark built from obfuscated code, not a study of happy-path bias |
| The `float.Parse` class as "one of the most widely reproduced C#/Unity indie bugs" | a ranking with no source |
| EvilGenie's "rates reaching 44% (Codex) and 33% (Claude Sonnet 4)" | the rates are on 9 ambiguous problems, our reading does not assign them to agents, and the agents were Codex, Claude Code and Gemini CLI |
| "ImpossibleBench and TRACE show related behaviours"; "an independent third-party comparison, not a vendor self-study" | not read |
| "the highest-value item on the list" | a ranking |
| The contrast ratios "4.5:1" and "3:1" | `ux-design` holds the figures |
| "which no shipping phone produces" | the records disagree |
| Pseudolocalization's "~35%" and "20-35% string expansion" | figures not read at a source, and another reading of ours gives about 40% |
| The quoted limit of visual regression, that it "will not catch the bug where a correctly-rendered element is placed incorrectly inside a parent container" | a near-verbatim quote of an unnamed source, and a diff against a correct baseline would show such an element |
| "A device simulator reproduces notch shapes where a plain game view does not" | the records disagree; `references/release-hardening.md` gives what the later record says |
| "Contrast is fully determined by two colour values" with "one pass covers every screen" | true for an opaque pair; the visual skill's record is a translucent colour whose stored value was four to five times off, so the two files now draw the same line |
| "This is often done by hand" (driving every state) | a frequency with no record; and the states driven are those the screen can reach, as `SKILL.md` now says |

## references/design-import-pipeline.md

| Line | Grade | Behind it |
|---|---|---|
| The mockup's styles are the spec; an agent builds by eye | I | the old file's reasoning |
| The helper's own radius; the hairline removed on 23 August 2026 | Seen | the milestone specs and history, August 2026 |
| The seven steps | Seen | the milestone history: the pipeline was written for the second design import |
| Two rounds that fell short; the diagnosis; the gap between declared and resolved values | Seen | the milestone history, August 2026; a research note of 28 August 2026 |
| The headless-browser dump | I | the research note's proposal; the project built it on 30 August 2026 |
| The alpha measured twice | Seen | the session log of 24 August 2026; the builder's code comment of 27 August |
| Radius tiers, layout patterns, type roles; review even a small pass | I | the old file's rules; the reason it gave for a small pass was not found |
| The locked geometry left alone | Seen | the second import's plan, August 2026 |
| The dark ring: two sprites at 30 and 39, found after eight more screens, fixed with a bake for that tier | Seen | the milestone history and the second import's verification report; a later plan counts the eight screens |
| Check by pixels right after a shared change | Seen | the lesson the milestone history records |
| Comparisons by eye let two rounds stay wrong | I | the earlier skill states it; the third round's comparison also used an automated review agent |
| The pixel delta the project built | Seen | the milestone history, 30 August 2026 |
| Vertical metrics; TextMeshPro's line metrics | D | the two pages named in the line |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Close is exactly how one project shipped two card radii side by side for weeks and kept re-growing an inset hairline nobody had chosen" | the record: a helper's own radius, no duration, and a hairline the helper added, not an agent's estimate |
| "That gap is exactly the bug class behind a ~210px vertical gap" | the gap's later root cause was a play area's dynamic sizing |
| The border's alpha as 0.025 | measured again at 0.020 after the card fill changed |
| The minigame rework "explicitly refused its literal marker/band pixel coordinates" | the plan names the locked constants; it does not say that the mockup's coordinates were refused |
| "both incidents in this file's opening survived multiple sessions specifically because they read as too minor to plan-and-review first" | a cause no record gives |
| "a glow radius freshly derived from the mockup's own math, and a button-fill sprite's corner radius set by an earlier, unrelated, also-correct decision" | the record: the glow radius was fixed at 30 for the smallest button, and the fill's corner was 39 |
| "Every comparison round through one project's third import was two PNGs read by a person or an agent" | the third round also ran an automated review agent; the line keeps the earlier skill's lesson, graded I |
| "a `pixelmatch`-class diff" | the library's page was not read |
| "a browser and a game engine resolve font metrics from different font tables by design" | worded to the two pages read |
| "A design delivery is usually a zip" | a frequency with no record |

## references/release-hardening.md

| Line | Grade | Behind it |
|---|---|---|
| Device passes are the owner's to raise | Seen | the source project's archived instructions: its owner's call of 3 August 2026 |
| The three-device matrix; an animation component dirties the interface | the old file's statement | not read again |
| A simulator first; the build settings as booleans; the store's floor; one profiling pass on the device | I | the old file's rules |
| The linker's static analysis and its annotations; the safe area's page | D | the two Unity pages named in the lines |
| The reflection crash; the desktop smoke test; developing at the level you ship | I | from the linker page; no such crash was found in the source project's records (searched: link.xml, managed stripping, reflection) |
| The stripping level left unset before release | Seen | the release audit of 20 September 2026; no later line changes it (searched: managedStrippingLevel, stripping level) |
| The safe-area fix reverted in July 2026 | Seen | the milestone history: the later record calls the "no visible change" a false alarm and says such a fix can be confirmed only on a device build |
| The touch edge cases | I | the old file's checks |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "managed stripping at medium or above"; "keep stripping at **medium during development**" | the source project's own release audit kept the level unset and advised against raising it before release |
| "Each of these is a common first-release rejection or crash source" | a frequency with no source |
| "enable rendering outside the safe area" | on Android 15 and later the setting has no effect, by Unity's page |
| "a device simulator is the only in-editor surface that reproduces real notch shapes"; "One correct fix was reverted" | the later record: such a fix can be confirmed only on a device build, and it does not call the fix correct |
| "Three mitigations in cost order" | an order stated without its costs; the line now says which to do first |
| "Five-minute manual checks" | a duration nobody measured |
