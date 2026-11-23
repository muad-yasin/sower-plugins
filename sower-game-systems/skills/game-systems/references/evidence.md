# Evidence for game-systems (dated)

*Read this file before a figure or an incident from `SKILL.md` or one of its reference files is relied on or quoted. It says where each rule and line comes from, so that whoever maintains the skill can tell when one may go. Engines, browsers and libraries change: read the page again before you rely on a version-bound line.*

**Grades.** **Seen** = it happened on the source project, a Unity mobile game whose browser build went out as a public playtest in October 2026, and whose records and earlier skills this skill was written from: an incident, a measurement or a decision, with its record named. An earlier skill counts as the record of a case it names. A row may also rest on our later work on these plugins; it then says so and gives the month. "Shipped" in a note is that project's own word: the defect was in the game's committed build. **D** = documented in a named source, read on the date given. A D row about a public source rests on the notes of our own research round of 2026-11-11 and 2026-11-12 unless it gives another date. **I** = inferred; the row says from what. A rule that an earlier skill states without naming a case is graded I, and a figure an earlier skill gives for how well a method worked is not kept without the record of its measurement. **The old file's statement** = an outside fact kept from the file as it stood before November 2026 and not read again: the line says "not checked at a source" and keeps no figure. "(questions)" marks lines that ask rather than claim. Nothing here was measured: no project was built with and without a rule.

## Sources read for the reference files

| Source | Read | What was read |
|---|---|---|
| The Linux manual pages `rename(2)` and `fsync(2)` (man7.org) | 2026-11-22 (`fsync(2)` for the main file too), the raw pages by script | atomic replacement of an existing target; the directory sync |
| Microsoft Learn: C runtime "rename, _wrename"; Win32 `MoveFileEx` and `ReplaceFile` | 2026-11-22, the raw pages by script | that `rename` refuses an existing target; the replace and write-through flags; replacing with a backup |
| Unity scripting reference, `Application.persistentDataPath` (the 6000.6 page, docs.unity.com) | 2026-11-23, the raw page by script | the Web entry: the path is formed with an MD5 hash of the URL of the directory that contains the page, and the file name and query parameters do not alter it |
| npm/write-file-atomic, issue 64 (github.com) | 2026-11-22, the raw page by script | its title |
| MDN: "Storage quotas and eviction criteria", "Using IndexedDB", `Math.random()`, `Map`; WebKit blog, "Updates to Storage Policy" (10 August 2023) | 2026-11-22, the raw pages by script | best-effort and persistent storage and the quotas; a transaction aborted by an error, the version and `onupgradeneeded`; the seed; insertion order; Safari 17's quotas and eviction |
| Android Developers, "Back up user data with Auto Backup"; Apple Developer, "Optimizing your app's data for iCloud Backup" (through the page's data file) | 2026-11-22, by script | what each backs up and leaves out; the 25 MB quota |
| Unity manual and scripting reference 6000.6: "Assembly Definition Inspector window reference", "Enter Play mode without domain reload", "JSON serialization", "Serialization rules", `MonoBehaviour.Update` | 2026-11-22, the raw pages by script | No Engine References; the default and the reset attributes; fields not properties, wrapping, missing values, dictionaries; Update and activation |
| Anthony Pecorella, "The Math of Idle Games, Part I" (Game Developer, 13 October 2016); his deck "Quest for Progress" (media.gdcvault.com, under gdceurope2016) | 2026-11-22, the page by script and the PDF's text | the series and its spreadsheet models; the deck's title and author |
| Blizzard News, "Diablo III Auction House Update" (17 September 2013) | 2026-11-22, the raw page by script | the reason given and the shutdown date |
| Gaffer On Games, "Floating Point Determinism" | 2026-11-22, the raw page by script | the conditions under which results match across machines |
| React, `useEffect`; dependency-cruiser; ESLint, `no-restricted-imports`; TypeScript, `lib`; Stryker; FsCheck; fast-check; Hypothesis | 2026-11-22, the raw pages by script | when an Effect runs; what each tool is for; the languages each covers |
| Unity 6000.3 and 6000.6 on domain reload (the default for new projects) | 2026-10-05, in an earlier research round of ours | not read again for these files |

## Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| A rule pushed until the bug class is impossible | I | the old file's attribution of two ideas to their authors (strategic over tactical programming, John Ousterhout; making illegal states unrepresentable); neither source was read for this file, and nothing rests on them but the names |
| Contract first | I | the source project's earlier systems skill states the rule |
| 1. Systems run with no scene; a boundary the build enforces | Seen | the source project kept its systems in an assembly that cannot reference the engine, checked by a search in its quality checks |
| 2. Tunables are data with defaults; config is never save state | I | the source project's earlier systems skill states the rule and names four of that project's configuration assets built this way |
| 2. A config asset edited while the game runs can persist; where the Unreal reference only asks, a value is changed on a spare asset and the result noted | I | the source project's earlier systems skill states it: an asset field changed in Play Mode keeps its value after Play stops, the opposite of a scene edit. Work lost to scene edits made during play is recorded four times by a plan of 1 August 2026, after an earlier count of twice in as many sessions; no incident of the asset direction was found. The engine detail: `references/unity.md`, "ScriptableObjects, and the two Play Mode traps" |
| 2. An authored judgement is content | Seen | the source project's world rules, August 2026: a story's price direction follows its moral read wherever the company did something, with no economic override; a story with no act by the company prices on its own terms. A September 2026 quality check that found the library leaning to one direction recommended pinning the figure, not balancing the library |
| 3. No just-in-case fields | Seen | the source project's earlier skill, with its own example: a placeholder that stayed in the interface until its feature was scoped |
| 4. Simulation is game-like | Seen | the source project's rule of fun over realism |
| 5. Derive from the player's checkpoints, against a self-contained anchor | Seen | the source project, July 2026: a draft of a retune derived its income figures against an upgrade ladder's full-ceiling multiplier, reachable only after spending far more than the gate it was to protect. The formula came out about 60 times off; the first of two gate passes caught it before any code, and the numbers were derived again against breakeven hours per tier and the time to the gate with no multiplier |
| 5. Never quote a threshold from memory | Seen | the source project's earlier systems skill once quoted four thresholds, and all four went stale as gates were retuned, lowered or retired; after that it quoted none |
| 6. Derive on read; three tiers of state | I | the source project's earlier skill states the rule; its save schema was not read for this file. The tiers in full: `references/architecture-and-state.md` |
| 7. Events over references; the composition root | Seen | the source project's composition root, which held 86 subscriptions in one file when it was audited in July 2026 |
| 7. A singleton is a direct reference by another name | Seen | the source project's instructions ask before any static singleton is added |
| 7. A project that already wires its systems another way keeps its pattern | Seen | a decision in our later work on these plugins, November 2026, made when an outside review asked whether the rule binds a game that already calls between its systems; no incident behind it. The review plugin's scope gate already checked the rule only where the project's pattern is events or one composition root |
| 8. No assumed listener order; a one-shot sync for startup events | Seen | the source project: three separate times by July 2026 (a reveal on the HUD, a poll of offline income, a gap in a screen's reveal), as its earlier skill records them; its session log of 7 August 2026 counts a fourth, in a tutorial's overlay and pop-up, and a placement race of the same kind was closed on 13 August |
| 9. Raise an event only after the state is committed; diff the side effects of two entry points | Seen | the source project: an unlock that failed every time. A story's event was raised before the call that recorded the story as shown, so the check the event existed to trigger read false, and the unlock waited for an unrelated later event; the fix was to record first |
| 10. No hard lock | Seen | the source project's rule that some income or route forward always stays open |
| 11. Seeded, injectable randomness | I | the source project's earlier skill states the rule; how far that project tested against closed forms and fixed seeds was not looked up for this file |
| 12. A stricter entry point is a wrapper that adds a policy | I | the source project's earlier skill states the rule |
| 13. An asymmetry need not be fixed by the change that found it | Seen | the source project, July 2026: grounding a trading change in the real formulas showed that buying a dip out-levered shorting a crash, because a short's payout is capped at twice the stake. Asked directly, the owner kept the stake the same for buying and shorting and left any rebalancing to a later pass with the existing knobs; the rule its earlier skill drew from it is to record the asymmetry and never special-case the change that found it |
| 14. A gate paired with a loud check on its output invariant | Seen | the source project, July 2026: a tightened curvature gate rejected every candidate site, placed no bridges, pruned most road nodes and split the delivery route graph in half; it was caught only by reading the bake log by hand |
| 15. Throttle per-frame polls and sweep for the same shape | Seen | the source project, July 2026: a new per-frame poll computed net worth up to seven times in one frame; after the owner asked what it cost, it was throttled to about once a second, and the wider sweep the owner asked for found two more, an identical unthrottled call in another trigger and a per-frame scan over every stock and position |
| 16. Silence is a defect until a comment justifies it | I | the source project's earlier skill; that such code passes a casual review is the old file's reason, not a measurement |
| The atomic write: an interrupted write leaves a complete save; on a file system temporary file, flush, rename, and a sync of the directory where the runtime allows it; in a browser the form of `references/web.md` | D, I | the Linux `fsync(2)` manual page (man7.org, read 2026-11-22): a sync of a file does not necessarily put the entry in its directory on disk, and an explicit sync of the directory is needed for that. That some managed runtimes give no handle on a directory, and that the write site then says so, is `references/save-and-persistence.md`'s rule. Stating the requirement before either form is our wording, and the browser's form is `references/web.md`'s |
| "Delete the save" means every file that matches its name | Seen | the source project: an instruction to clear the save named one file, and the loader's fallback to the backup silently restored the previous session four times in one session |
| Golden saves: a new build loads the saves older builds wrote | I | the source project's earlier skill states the rule and called it forward compatibility; a new reader of old data is backward compatibility, so the files now say what the fixture shows. Whether that project's fixtures existed was not looked up for this file |
| Anti-cheat decided once | I | the source project's earlier skill states the decision for an offline single-player game; no record of when or by whom it was made was found |
| The decoupling test is the proof | I | the source project's earlier skill states the rule |
| Find every call site by search | Seen | the source project, July 2026: a gate pass on the same retune, searching instead of assuming, found two things a read-through had missed: a debug menu action that was a third real caller of a method about to be retired, and an achievement hard-coded to a tier id the new design had to keep. One record of the pass says three, and lists the same two |
| A guard for a mistake shipped twice; list the paraphrases first | Seen | the source project, August 2026: the guard was a documentation grep, and its pattern's synonym hole opened twice, the second within a day of the first widening; its full history counts three widenings of the pattern and one hole in its file list |
| A content roster in scene data needs its own check | Seen | the source project: the class recurred four times by its own count, each found live in Play Mode or by a direct check of the scene, never by a test or a review |

## Retired in November 2026

| Line | Why it went |
|---|---|
| "A measured LLM bias" (rule 3) | no source in the old file; the rule stands without it |
| "Four stale numbers within a month" | the record says four went stale; it gives no month |
| "A real ~60x error once shipped in a draft" | the record says a gate caught it in a draft, before any code |
| "The reasoning LLMs are measurably worst at" (rule 8) | no source was found |
| "40% of the map unreachable" (rule 14) | shortened: the note keeps the route graph split in half; the record also gives 59.6% of road nodes pruned and 40% of the city unreachable |
| "The AI-authored failure mode with the strongest evidence behind it" (rule 16) | no source named |
| "Save bugs produce the worst store reviews of anything in this layer" | no source |
| A link to a blog post on crash consistency | replaced by the manual page |
| "Missed call sites are a measured LLM weakness" | no source named |
| The heading "Mistakes to actively flag" | now "Mistakes to flag", as in the other skills |
| "Your engine's reference says whether yours does" (a config asset edited while the game runs) | the Unreal reference only asks the question; the line now names the file that answers and what to do where none does (an outside review of this repository, November 2026) |
| The save recipe as temporary file and rename alone | a browser has no rename, and `references/web.md` gives another form; the requirement now stands first, then each form |
| "Golden saves prove forward compatibility" | a new build reading an old save is backward compatibility, and a set of fixtures shows it for the states it covers |

## references/architecture-and-state.md

| Line | Grade | Behind it |
|---|---|---|
| The contract's three lists; the deletion test | I | the old file's reasoning |
| No interface before its second; the wrapper that adds a policy | I, Seen | the main file's rule 12; the earlier skill names the stricter purchase method that delegates to the permissive one |
| The composition root's 86 subscriptions | Seen | the audit of July 2026 behind rule 7's row above |
| A project that wires its systems another way keeps its pattern | Seen | our decision of November 2026: rule 7's third row above |
| Shape 1, three times by July, a fourth in August | Seen | the source project's instructions file names the three: a HUD reveal on a stage-changed event, an offline-earnings poll in `Start()`, a screen root's reveal gap; the session log of 7 August 2026 names the fourth |
| Shape 2, evaluate on load | Seen | the earlier skill names the project's two unlock checks of that shape |
| Commit before you announce; the later audit | Seen | the milestone history, July 2026; the bug register |
| The external-notify path | Seen | the earlier skill's verification notes: a chain that could never arm, latent for weeks |
| Three tiers of state | I | the earlier skill states the rule |
| The gate that split the graph | Seen | the milestone history, July 2026 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "an offline-earnings panel that polled in the wrong callback, and a screen that revealed itself one frame too late" | the record names a poll in `Start()` and a reveal gap |
| "survived weeks of play because it needed a specific chain to expose it" | the record says 100% reproducible, with the unlock waiting for an unrelated later event; "latent for weeks" belongs to the external-notify case |
| "Half the map is unreachable" | the record: the graph split in half, 40% of the city unreachable |
| Rule 1 in the list of rules this file deepens | the file holds nothing on it |

## references/economy-and-balance.md

| Line | Grade | Behind it |
|---|---|---|
| The derivation comment | I | an illustration made up for the file, with no project's numbers |
| No direct study of invented formulas | I | the earlier skill's verification notes state the caveat |
| The error of about sixty times | Seen | the milestone history and the specs, July 2026 |
| Simulation close to mandatory | I | the earlier skill |
| Pecorella | D | the article and the deck named in the line |
| Diablo III's sessions that ended down gold | the old file's statement | not read again |
| Blizzard's reason and shutdown date | D | Blizzard's post named in the line |
| The additive ladder; the boundary; its test | Seen | the design archive, 13 and 23 August 2026 |
| The asymmetry | Seen | the milestone history, July 2026 |
| Live telemetry scoped out | Seen | the earlier skill records the decision |
| The monetization boundary | Seen | the source project's design review, July 2026 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| The commented example with 25,000 and 50,000 | the source project's live thresholds, in a file that quotes none; "2x cost" and "hire twice" are in no record |
| "That is the default shape of LLM-written economy code" | a frequency nobody measured |
| "The draft was internally consistent ... Nobody misread anything" | not in the record, which gives the target and the computed hours |
| "will have four wrong numbers within a month" | the record gives no month |
| "The canonical body of work"; "Evidence: strong, well-corroborated" | a ranking and a grade from a research report; the sources are now read and dated |
| "whose designer's own retrospective attributes the failure to an unchecked assumption" | not traced to a primary source |
| "a special case that would have outlived everyone's memory of why it existed" | rhetoric, not in the record |

## references/procedural-generation.md

| Line | Grade | Behind it |
|---|---|---|
| The incident: 59.6% pruned, 40% unreachable; the two hard errors | Seen | the milestone history, July 2026 |
| Golden and random seeds | I | the old file's rule |
| Blind threshold roulette, 93% | Seen | the milestone history and the glossary, July 2026 |
| The first guess at about 6% | Seen | the glossary |
| Calibrating from percentiles | I | the glossary's rule; a later re-bake kept one constant off its percentile on purpose, for the complaint it was made for |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Nothing threw. The bake reported success." | the record says the bake log showed it, and nothing of a success report |
| "Two numbers, one abort. That is the shipped shape of this rule." | not in the record |
| "The instrumentation cost less than any one of the three attempts" | an effect nobody measured |
| "it was doing essentially nothing, and looked reasonable in the source" | not in the record |
| "This is the half people skip" | a frequency claim |

## references/save-and-persistence.md

| Line | Grade | Behind it |
|---|---|---|
| The versioned envelope | the old file's statement | the practitioner guides were not read again |
| Missing fields keep their constructed values | D | Unity's JSON page |
| `rename(2)`, `fsync(2)`, the library issue; Windows | D | the pages named in the lines |
| Four fresh-save runs that were not; the origin stamp | Seen | the instructions file's archive and the project's notes on its working agreements, August 2026 |
| Golden saves, and that they do not test an older build reading a newer save; corrupt-save recovery; elapsed-time invariants | I | the earlier skill states the rules; the untested direction is our addition |
| Anti-cheat | I, the old file's statement | the earlier skill states the decision; AAA hardening was not read again |
| Saves over a network | I | moved from `references/web.md` |
| Clock manipulation; the day clock | Seen | the bug register, August 2026 |
| Mobile backup | D | the Android and Apple pages named in the line |
| The WebGL path and the fixed folder | D, Seen | Unity's scripting reference for the path (the sources table above); the web build notes of October 2026 for the fixed folder. Those notes call the hash "per-build", and the line follows Unity's page |
| Saves before 1.0 | Seen | the earlier skill and the PC build notes |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Save bugs produce the worst reviews of anything in this layer" | no source |
| "Industry-consensus shape, corroborated across independent indie practitioner sources" | the sources were not read again |
| "The single most common shipped failure these sources name" | one source's ranking, not read again |
| The link to a blog post on crash consistency | replaced by the manual pages |
| "the C-library and Windows equivalents are not [atomic]" | Microsoft's pages say the C runtime's rename refuses an existing target, and promise no atomicity either way |
| "Recovering from backup without telling anyone is how a player loses an hour" | an effect nobody measured |
| "the highest-risk economy code in the idle genre" | a ranking nobody measured |
| "the classic exploit, and the classic mitigation" | frequency words |
| "Migration matters from the first public release onward" | the recorded call is the store's release 1.0 |
| "On WebGL the path carries a hash per build" | Unity's page: the hash is made from the URL of the page's directory, so the path changes with the address and not with the build |
| "Golden saves prove forward compatibility" | see the same row above |

## references/testing-and-verification.md

| Line | Grade | Behind it |
|---|---|---|
| The decoupling test | Seen | the specs and the milestone history, July 2026 |
| The second gate pass | Seen | the session log and the specs, July 2026 |
| The guard's history | Seen | the instructions file's archive, August 2026 |
| The roster class, four times by July 2026 | Seen | the session log (13 July), the milestone history (15 July) and the project's notes on its upgrade surfaces (20 July) |
| The changed default and the copy tool; the success log | Seen | the milestone history; the glossary |
| Determinism, levels 1 and 2 | I | the old file's reasoning |
| Determinism, level 3 | D, the old file's statement | Gaffer On Games, named in the line; fixed-point lockstep was not read again |
| The tools | D | each tool's own page |
| The properties; the costs | I | the earlier skill's proposal |
| The structural review; a thousand lines; filing | I | the earlier skill states the rules |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "byte-identical payout output" | the record says tip output |
| "Missed call sites are a *measured* LLM weakness ... a meaningful share ... degrade further" | no source named, as in the main file |
| "found three callers ... a debug menu action, an achievement's hard-coded tier-id check, and a test" | the record names two things, and no test |
| A source-scanning test as the case behind the guard rule | the case was a documentation grep |
| "This has shipped broken twice in one project" | the record counts four, found live or by a direct check |
| "would have saved all three attempts" | an effect nobody measured |
| "a real and commonly missed source of divergence" | the frequency word |
| "why deterministic-lockstep RTS games historically use fixed-point integer math", with its link to an article | the article was not read; kept as the old file's statement, without "historically" |
| "worth more on a model-assisted codebase than on a hand-written one"; "Evidence for both: strong as general practice" | an effect and a grade nobody measured |

## references/unity.md

| Line | Grade | Behind it |
|---|---|---|
| No Engine References | D | Unity's page named in the line |
| The separate save assembly; the misnamed assembly; `is null` in the pure assembly | Seen | the glossary (the code audit of 22 July 2026) and the milestone history |
| The inversion on `UnityEngine.Object` | I | the earlier audit agent states the rule |
| Config never save state; the asset direction | I | the earlier skill |
| The scene direction, four times | Seen | a plan of 1 August 2026; the instructions file's archive gave the earlier count of two |
| Rosters, four times; the GUID search | Seen | as `references/testing-and-verification.md`; the glossary |
| Editor tools, four ways; the sentinel | Seen | the glossary (July 2026) and the milestone history (August 2026) |
| The mid-Play recompile | Seen | the instructions file, July 2026 |
| Domain reload | D | Unity 6000.6's page named in the line; the default's history from an earlier round of ours |
| `JsonUtility` and its edges | Seen, D | the project's use; Unity 6000.6's pages |
| `OnApplicationQuit` in the editor | Seen | the instructions file's archive |
| The two namespaces | I | the earlier skill states the rule |
| The poll and the sweep | Seen | the milestone history and the task archive, July 2026 |
| `Update` and activation | D | Unity's scripting reference |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "This is the single highest-leverage structural decision in a Unity project's systems layer" | a ranking nobody measured |
| "ours named the wrong assembly for months" | the record gives no duration |
| "or - worse - silently takes the wrong overload. A real bug shipped and was fixed on exactly this." | the record: a compile problem, found and fixed in that milestone |
| "Both directions have bitten." | no incident of the asset direction was found |
| "This shipped broken twice in one project." | the record counts four |
| "points at `[RuntimeInitializeOnLoadMethod(SubsystemRegistration)]`", with its link to the 6000.2 manual | the 6000.6 page names other attributes and a new default |
| "This is the most common first-time save bug in Unity." | a frequency nobody measured |
| "It ignores `[DefaultValue]`, has no nullable support, and cannot serialize a top-level dictionary or array." | not on the pages read; the 6000.6 rules list dictionaries with `[SerializeField]` |
| "The one that hurt was an unconditional O(stocks x positions) scan"; "this exact poll shipped twice independently" | the record's sequence: a poll throttled after the owner asked, then a sweep that found two more |

## references/unreal.md

| Line | Grade | Behind it |
|---|---|---|
| The questions | (questions) | the Unity layer's findings, asked of Unreal |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "We have zero Unreal experience." | the file now says what stands behind it |
| "In Unity the two behave oppositely, and both directions have caused real bugs" | no incident of the asset direction was found |

## references/web.md

| Line | Grade | Behind it |
|---|---|---|
| The browser build and its saves; the WebGL path and the fixed folder | Seen, D | the web build notes, October 2026; Unity's scripting reference for what the path's hash is made from |
| The boundary tools; `lib`; `useEffect` | D | the pages named in the lines |
| Storage quotas, eviction and persistence | D | MDN and WebKit |
| No export or import code; the accepted loss | Seen | the owner's decision of October 2026 in the web build notes |
| IndexedDB; `Math.random()`; `Map` | D | MDN |
| Plain objects' key order | the old file's statement | not read again |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "We have real but modest web experience: shipped sites and browser-embedded work" | no record; the file now says what the source project built |
| "we have used import boundaries in web projects but not to fence a game simulation specifically" | no record found |
| "`localStorage` is capped around 5MB ... typically several GB" | now MDN's figures, with their date |
| "which the browser clears only after clearing every best-effort origin first, and with user notification" | MDN: persistent data goes only if the user chooses; Firefox asks the user when a site requests it |
| Saving over a network | moved to `references/save-and-persistence.md`, which the main file names for it |
| "JIT tiering means the same expression may be optimized differently within one session"; "*Documented general behaviour*" | not read at a source |
| "in milliseconds" | not measured |
| "the engine's persistent path carries a hash per build, so a new upload would orphan old saves" | Unity's page: a new upload to the same directory keeps the path; a new directory changes it |
