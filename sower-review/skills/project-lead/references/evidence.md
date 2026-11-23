# Evidence for project-lead (dated)

*Read this file before a figure, a threshold or an incident from `SKILL.md` or one of its reference files is relied on or quoted. It says where each rule and line comes from, so that whoever maintains the skill can tell when one may go. Store rules change every year: read the page again before you rely on one.*

**Grades.** **Seen** = it happened in our own work: on the source project, a Unity mobile game whose browser build went out as a public playtest in October 2026 and whose records and earlier skills this skill was written from, or in later work, with the month. It is an incident, a measurement or a decision, with its record named; an earlier skill counts as the record of a case it names. "Shipped" in a note is the source project's own word: the change was in the game's committed build. **D** = documented in a named source, read on the date given. A D row about a public skill names it as our research round of 2026-11-11 and 2026-11-12 recorded it, at a commit or on a dated page; those sources were not read again for this file. **I** = inferred; the row says from what. A rule that an earlier skill states without naming a case is graded I, and a figure an earlier skill gives for how well a method worked is not kept without the record of its measurement. Nothing here was measured: no project was run with and without a rule. **The old file's statement** = an outside fact kept from the file as it stood before November 2026 and not read again: the line says "not checked at a source" and keeps no figure, or keeps it as the old file's. **(pointer)** marks a line that sends the reader to another file, which holds the content.

## Sources read for the reference files

| Source | Read | What was read |
|---|---|---|
| Bent Flyvbjerg, "From Nobel Prize to Project Management: Getting Risks Right" (arxiv.org/abs/1302.3642) | 2026-11-22, the abstract page by script (and 2026-11-21 for `sower-review/EVIDENCE.md`) | the abstract |
| Gary Klein, "Performing a Project Premortem", Harvard Business Review, September 2007 | 2026-11-21, the page's summary, for `sower-review/EVIDENCE.md` | what the method asks; no figure for its effect |
| Play Console Help: "Target API level requirements for Google Play apps", "Play Console technical quality requirements", "Release app updates with staged rollouts" (support.google.com/googleplay/android-developer) | 2026-11-22, the raw pages by script | the floors from 31 August 2026 and the extension; the vitals thresholds and the plans for 2027; what a staged rollout is, and that it is for updates only |
| Play Console Help: "App testing requirements for new personal developer accounts" (support.google.com/googleplay/android-developer) | 2026-11-23, the raw page by script | the closed test for personal accounts created after 13 November 2023; more testing for too few testers or too little engagement |
| Play Console Help: "User Data" (support.google.com/googleplay/android-developer) | 2026-11-23, the raw page by script | the privacy policy section: a link in Play Console and a link or text in the app, for all apps; an app that accesses no personal and sensitive user data must still submit one |
| Android developers: "Meet Google Play's target API level requirement", "Android vitals", "ANRs" (developer.android.com) | 2026-11-22, the raw pages by script | the floors; the thresholds; the 5-second input timeout |
| Apple Developer: the news of 9 September 2025, "App Privacy Details", guideline 5.1.1(v) on account deletion, the App Store Review Guidelines (developer.apple.com) | 2026-11-22, the raw pages by script | the SDK required from April 2026; the privacy answers; the deletion rule |
| Steamworks documentation: "Steam Direct Fee", "Coming Soon", "Onboarding" (partner.steamgames.com) | 2026-11-22, the raw pages by script | the fee and its recoupment; the two weeks; the 21 days and the review of 1 to 5 days |
| Google Search Central, "Understanding Core Web Vitals and Google search results" (developers.google.com/search) | 2026-11-22, the raw page by script | the three thresholds and their tie to ranking |
| W3C, "What's New in WCAG 2.2" (w3.org/WAI/standards-guidelines/wcag/new-in-22) | 2026-11-22, the raw page by script | the date it became a Recommendation |

## Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Read every file the plan touches before writing it | Seen | the source project's earlier version of this skill names four plans in which this read caught gaps before any code: two migrations, a purchase feature and an achievements feature |
| The spec's four parts; three to five scope items, more than five a reason to look for a second milestone; success criteria as what a user can do | I | the source project's earlier version of this skill states its spec format, with Must, Should, Could and Won't for a hard cut and a success criterion from the game itself as the example. The five-item limit is that project's rule; no incident behind the number was recorded, and the `scope-gate` agent treats it as advisory, so the skill does too |
| The goal names how its completion is checked; an activity is not a goal | D | the "Define Goal" skill of openai/skills (`skills/.curated/define-goal/SKILL.md` at commit 49f948fa) rejects goals that name only an activity; read 2026-11-12, when the repository's README marked it deprecated |
| Every outcome the request asked for stands in the scope, or is deferred with the requester's agreement noted | D, I | the Unlazy skill (Leonxlnx/unlazy at commit 16671491) and its issue #23: every declared gate passed while the set of gates had left out a requested deliverable; read 2026-11-12. That a deferral needs the requester's agreement is our inference: an outside review of this repository in November 2026 walked a requested outcome into the non-goals, and the earlier wording let it pass |
| The builder's read before approval | D | obra/superpowers, the release notes of its v7.0.0 ("Brainstorming", `RELEASE-NOTES.md` at commit 22f0b463): a fresh agent reads a design as its builder and lists what it would still ask; read 2026-11-12 |
| Order by risk; milestone size; micro-goals; blocking decisions first; "spec now, build later" | Seen | the source project's earlier version of this skill; "spec now, build later" has its precedent there, a late stage fully specified and held until a polish pass and an economy retune had landed, so that its numbers were not tuned twice |
| One-way steps named while the work is ordered | D | the "pr" skill of mattpocock/skills (`skills/engineering/pr/SKILL.md`, its section "Merge Danger", at commit 4ae2317d) names whether a change is a one-way or a two-way door and how far its effects reach; read 2026-11-12 |
| The six questions of the inline gate | Seen | the source project's scope gate, in its earlier planning skill; the product lens was added in July 2026, when the three-role review became a standing agent |
| A "needs changes" verdict is the review doing its work; the reviewer says which check settled the verdict | Seen, I | the source project, July 2026: two gate passes ran on one plan before it was approved, neither a rubber stamp, and the first caught an early draft's income figures about 60 times off. The same project's earlier skill names three more specs that came back "needs changes"; it says what those passes caught for the four together, not for each. The record counts no clean passes, so the skill names no expected verdict; that the reviewer should say which check settled it is our inference |
| Claims rot: every amendment is checked against the repository | Seen | the source project, July 2026: a re-check of one gate's accepted amendments against the code found three that the code no longer bore out or that understated the work, one citing behaviour removed four days earlier; a second gate on the corrected plan found one more of the same kind |
| A criterion dropped on the way counts as not met unless the requester took it out | D, I | the row on requested outcomes above; reporting a dropped one as not met is our inference from it |
| A narrow pass states what it does not close | Seen | the source project's earlier version of this skill names two such passes: a visual pass on the interface chrome alone, and an achievements checklist that did not track progression |
| A recurring mistake earns a mechanical guard | Seen | the source project: a coverage test was built after a soft-lock bug recurred, and the phrase search on living documents after the rule had been broken a fourth time while it was only remembered; the rows below |
| An override is recorded with its reasoning | Seen, I | the source project's earlier skill names three overrides recorded this way, among them an exception to a paid tier's promise, and its glossary four; its instructions file records later calls of the owner the same way, each with its date and its reason. That an override without its reasoning reads as an accident is the old file's reason, not an incident |
| File the build narrative in the same session | Seen | the source project, July 2026: the debt came back three times before it became a rule |
| A living document gets a pointer, not the paragraph | Seen | the source project: after each of the three splits its records name, narrative crept back into the file that had been split, because it was written inline instead of as a pointer |
| List the paraphrases first; extend the guard's file list with every split | Seen | the source project, August 2026: one pattern's synonym hole opened twice, the second within a day of the first widening |
| Pair a phrase check with a size check | Seen | the source project, July 2026: a status line reached 17,913 characters without tripping the phrase search |
| A carve-out needs its own bound | Seen | the source project: the fourth instance, in which stubs allowed "a short note stating what is true today" grew back into essays |
| One ledger for scattered caveats | Seen | the source project's design document holds one consolidated ledger of untuned numbers, the precedent its earlier skill names |
| A root instructions file of about 200 lines | D | Claude Code's documentation, its page on memory (code.claude.com/docs/en/memory), sets a target of under 200 lines per instruction file; read 2026-11-12 in an earlier research round of ours, not read again for this file |
| Code-complete is not "can go live"; the named block of manual steps | Seen | the source project's earlier skill and its task list's release block (the store listing, the in-app product and its key, the ad network's keys, a device build) |
| Store thresholds checked by a fresh search before use | Seen | our later work, November 2026: reading the pages again changed figures the old file carried, among them Steam's wait (21 days, not 30) and Apple's requirement (the SDK from April 2026, not Xcode from 28 April). `references/release-readiness.md` gives each figure its source and the date it was read, or says that it was not checked |
| One window owns the editor | Seen | the source project's earlier skill, a rule added in July 2026 together with the two hazards below |
| A compile error makes the editor's tools run the last good build | Seen | the source project's glossary records four ways this bit, stale prefab rebuilds twice in one milestone among them |
| Parse the approved review file with a script | Seen | the source project, 22 July 2026: the 57 edits of an approved sweep were applied by parsing the review file, with no retyping drift, then checked by a script for length and dashes; how a sweep applied by hand would have compared was not recorded |
| The honesty mandate; a contradiction with a recorded decision is the finding | Seen | the source project's developer asked for real assessments over encouragement (its earlier skill records the request); the contradiction rule: the gate's rows in `../../../EVIDENCE.md` |
| A hand-carried tally of something on disk | Seen | the source project: one running count was corrected twice and then removed; another read 59, then 61, then 70, each correction found by a checkup |
| A true statement next to a prohibition | Seen | the source project, August 2026: a ban kept in one file was broken twice on the next day, because the always-loaded instructions said the banned thing was routine |
| No speculative batches of assets | I | the source project's earlier skill states the rule: small batches tied to what is being built, for paid image generation and later for free downloads too |
| No time estimate without a measured base rate | I | a number with no base rate behind it reads as a forecast it is not; the old file's rule |

## Retired in November 2026

| Line | Why it went |
|---|---|
| "Four migrations in a row" | the record names four plans of different kinds, two of them migrations |
| "race conditions" beside the arithmetic error and the missed call sites | not traced to a record; the record of that gate's first pass names the two missed call sites it caught by searching (July 2026) |
| "~150-200 lines" | now "about 200", with its source |
| "Should we build X" claimed as this skill's job in the description | the `scope-gate` agent now answers it in full; this skill keeps the inline gate and names the agent |
| "More than five means cut, or split into two milestones; never accept it as one" | a number with no incident behind it, stated as a refusal while the gate treats it as advisory |
| A requested outcome that stands "in the scope, the non-goals or a stated assumption" as enough | moving it to the non-goals met the rule without the requester deciding anything |
| "A 'needs changes' verdict is the expected outcome" and "a gate that always comes back clean is more likely a rubber stamp" | the record holds four specs that came back and no count of clean passes, and the gate is told to say GO when the plan is sound |
| The heading "Mistakes to actively flag" | now "Mistakes to flag", as in the other skills |

## references/specs-and-ordering.md

| Line | Grade | Behind it |
|---|---|---|
| The one-page spec; a minute to read; three to five items | I | the source project's earlier skill states the rules; no incident behind the numbers |
| Success criteria about what a user can do; the milestone named after a class | I | the earlier skill names the smell |
| Non-goals as claims; Must, Should, Could, Won't; the written parking lot | I | the earlier skill's method and the old file's reasoning |
| The forms of the ordering mistake | I | the old file's examples |
| Spec now, build later: the late stage held until a polish pass and a retune | Seen | the session log, July 2026; the stage later shipped in full |
| Micro-goals as a same-day signal | I | the earlier skill's rule |
| The same header across the split and the archive | Seen | the split of 22 July 2026 and the archive of 4 September 2026 |
| The stubs that grew into essays | Seen | the instructions' archive of working-agreement lessons: the carve-out of 31 July 2026 and its size check |
| The destination that arrived bloated | Seen | the checkup's lessons: the audit of 22 July 2026 |
| One ledger of untuned numbers, checked in full | Seen | the ledger added 11 July 2026; the checkup's rule, widened from a sample to every constant on 22 July 2026 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "can be checked, by one person, in two minutes" | a duration nobody measured |
| "the most common spec smell" | a frequency with no record |
| "a decision with a deadline attached" | nothing behind it |
| "the cheapest available detector for silent scope creep" | a ranking with no record |
| "a root instructions file, seven skill files and four agent briefs" | those are file counts of the project, not counts of references to milestone headers, and later grew |
| "Verifying a rotating sample instead was tried on the source project and rejected" | the record: a sample was adopted, then widened to every constant the same day; drift was a named risk, not an observed one |

## references/scope-gate-and-estimation.md

| Line | Grade | Behind it |
|---|---|---|
| Why a gate exists | I | the old file's reasoning |
| The knockout items | (pointer) | `sower-review/agents/scope-gate.md`, which holds them in full |
| The outside view | D, I | Flyvbjerg's abstract, as the line gives it; "this one is different" is our inference |
| The pre-mortem | D | Klein's summary, as the line gives it |
| The tags on assumptions; reuse | I | the old file's method |
| The verdicts and the two kinds of NEEDS-SPEC | (pointer) | the agent's verdict section |
| KILL-DESCOPE returned once, on a rework whose premise the gate checked and found false | Seen | the task archive, September 2026 |
| Two bugs caught in two plans | Seen | the milestone history and a plan of 22 July 2026 |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "it is the *only* place a bad plan gets caught before it becomes code" | an effect nobody measured |
| "≤5 scope items" as a knockout | the agent makes more than five an advisory finding |
| "Content is safe" as item 4, and no item on one-way steps | the items now follow the agent |
| "the documented cure for the planning fallacy" and the method's three steps | worded to the abstract read; the steps were not read |
| "The belief that a project is unique is itself correlated with overrun" | our inference, not a finding |
| "The commonly cited figure is a ~30% improvement", with its two links | the effect was not found in what was read, and one link led to the reference-class paper |
| "3 of that gate's own accepted amendments already false"; "The same pass caught two real pre-implementation bugs" | the record: three that the code no longer bore out or that understated the work; the two bugs came from the same discipline in two plans |
| More than five scope items "usually means two milestones" | a frequency with no record; the count is a reason to look |

## references/review-checkpoint-and-docs.md

| Line | Grade | Behind it |
|---|---|---|
| Small features hide creep | I | the earlier skill's rule |
| The polish pass that touched only the chrome | Seen | the pipeline document, flagged by the owner |
| The checklist-only feature | I | the earlier skill's example |
| The coverage test after the soft-lock class | Seen | the glossary; the navigation stack's test replaced it |
| The synonym hole; widened on 5 August 2026 | Seen | the working-agreement lessons, August 2026 |
| A document outside the guard's list until 8 August 2026 | Seen | the same lessons. They say "eight weeks", but the rule they name dates from 12 July 2026, so the line gives no duration |
| 17,913 characters | Seen | as in the rows of `SKILL.md` above |
| An existing rule over an invented search | I | the old file's advice |
| The filing debt, three times | Seen | the instructions file: the rule of 11 July 2026 |
| Narrative destinations exempt from the guard | Seen | the instructions file, 23 August 2026, and two later exceptions |
| The three splits that drifted back | Seen | the checkup's lessons |
| The carve-out's shape | I | the old file's reasoning; the case is `SKILL.md`'s |
| About 90,000 tokens; two files most agents never used; about 47,000 after | Seen | the working-agreement lessons and the reduction plan's second phase, 23 August 2026 |
| A fresh session for the check; the rollback line | Seen, I | the reduction plan's observation of 23 August 2026; the rollback is the old file's advice |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Nobody skips a review of a big feature." | nothing behind it |
| "Two observed shapes" | the earlier skill gives both as examples; only the polish pass has an incident |
| "That property is the entire value." | an effect nobody measured |
| "the next reader is usually a future automated pass" | a frequency with no record |
| "Observed on every split the source project performed, without exception." | the record names three splits; later ones show no record of drift |
| "Documented four separate times on one project." | the record counts the fourth instance of one drift pattern, inside a carve-out |
| "One status line reached ~18,000 characters" | the record's figure is 17,913 |
| "content that only one kind of task ever needed" | the record: two of the four files served tasks most agents never do |
| "subject to a rule for eight weeks" | the records say eight weeks, but the rule they name dates from 12 July 2026, four weeks before the fix |

## references/release-readiness.md

| Line | Grade | Behind it |
|---|---|---|
| The manual steps as a named block | Seen | the earlier skill and the task archive's release block |
| Staged rollouts for updates only | D | Play's page named in the line |
| 5 to 10% as a first stage; .aab, IL2CPP and ARM64; the listing's minimum | the old file's statement | not read again |
| 48 hours, twice a day; what earns a hotfix | I | the earlier skill's rules, from research of July 2026 that names no source |
| The late stage shipped before the beta | Seen | the earlier skill and the session log, which calls the order a pattern of individually reasonable choices made explicit after the fact |
| The reading frame for reviews | I | the source project's player-reception research of August 2026, adopted in its design guardrails before the game had store reviews to read. Its retention reading is worded as a guess to test: the figures say that people leave and not why, and that research says such benchmarks apply once real player data exists |
| The target API levels; the vitals thresholds; ANRs; memory from February 2027 | D | the Play and Android pages named in the lines |
| The closed-testing gate | D | Play's page named in the line |
| A privacy policy for every app | D | Play's "User Data" page named in the line |
| The SDK from April 2026; App Privacy; account deletion | D | Apple's pages named in the lines |
| The fee; the 21 days and the two weeks; the review | D | the Steamworks pages named in the lines |
| No total; pay the fee early | I | the pages give the parts only; the 21 days count from the payment |
| Core Web Vitals; WCAG 2.2's date | D | the pages named in the lines |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Every number in this file carries the date it was verified" under headings "verified 2026-09-06" | no record of that check; every figure now carries its own read, or says it was not checked |
| "it is the only thing that turns a bad build from an incident into an inconvenience" | an effect nobody measured |
| "a phased release on iOS; a limited beta branch on Steam" | not read |
| "Verified as of 2026-08 on the source project" for the closed-testing gate | that date is the source project's own decision, not a check of Play's rule, which is now read at its page |
| "a reachable privacy policy once an ad or purchase SDK ships" | Play's page asks every app for one |
| Weak returns with long sessions "mean the loop works and the early pacing is slow" | figures that say that people leave, not why; now a guess to test |
| "**Organization accounts (D-U-N-S verified) are exempt.**" | Play's page sets the rule for personal accounts and says nothing of organization accounts |
| "A Data Safety mismatch is a common solo-developer takedown cause." | a frequency with no record |
| "from **April 28, 2026**, apps uploaded to App Store Connect must be built with Xcode 26" | Apple's page says the SDK, from April 2026 |
| "(since 2022-06-30) and is a frequent privacy-category rejection" | not on the page read |
| "Most-cited rejection causes" and "Review turnaround is commonly reported around 24-48 hours" | not read |
| "**There is a mandatory 30-day wait**" | Valve's onboarding page says 21 days, for the first few titles |
| "a standalone demo or DLC published as its own app pays its own fee" | not on the fee page read |
| "Practical minimum from account creation to launch is around 4-6 weeks." | from the two blogs, with the 30-day wait; Valve's pages give no total |
| "reviewed, for accuracy, stability and transparency. Capsule art and screenshots must represent actual gameplay." | not on the pages read |
| The two blogs cited for Steam | replaced by Valve's own pages |
| "each evaluated at the **75th percentile of real user data**" and "a confirmed page-experience ranking signal" | not on Google's page read; worded to it |
| "WCAG 2.2 AA is the common contractual and public-sector bar" | nothing read behind it |
| "their certification requirements are substantially stricter than any store above" | a comparison with no source |
