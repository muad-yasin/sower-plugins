# Evidence behind the review agents

An agent file holds its rules and, where a rule needs it, the incident behind it in one line. This file holds where each rule comes from, so that whoever maintains an agent can tell when a rule may go: when the failure it guards against no longer happens, when the tool changed, or when the source it rests on was withdrawn.

**Grades.** **Seen** = it happened in our own work; the round is named. **D** = documented in the named primary source, read on the date given, with how much of it was read. **I** = inferred; the row says from what. A **D** row about a public skill names it as our research round of 2026-11-11 and 2026-11-12 recorded it, at a commit or on a dated page; those sources were not read again for this file. Nothing here was measured: no audit was run with and without a rule to compare the two.

## The rounds behind "Seen"

- **The source project.** A Unity mobile game, whose browser build went out as a public playtest in October 2026. The defect classes and the C# and Unity tells come from its bug register, and the culture class's count also from two audits of July and August 2026; "shipped" in an agent file is that register's own word: a defect of that class was in the game's committed build.
- **September 2026.** Three rounds of `bug-audit`: 12 audits across two code bases, then 7 and 6 agents on a Node.js command-line tool and server. The session that ran the first round checked each audit's top findings against the code before filing them.
- **October 2026.** Two rounds on the same tool with prompts written for the round: six agents on a frozen commit with a re-audit of the fixes, then three lanes that filed every finding into a register.
- **November 2026.** Sixteen agents on one pull request of that tool, with a script that looked up every quoted line; five audits of a Python tool; and one read-only run of the rewritten `bug-audit` on one module of that Python tool at a fixed commit, set beside an outside review of the same commit whose author had run the tool with crafted inputs.
- **Gate and panel runs, July to November 2026.** `design-review` on the source project's designs (July and August 2026); `scope-gate` and `design-review` on the milestone plans of a game project and on the page, price and copy specs of a website project (September to November 2026); and a comparison of five reviews of one plan on another project (October 2026). Their reports, and the decision records that took up their amendments. A row names the kind of project and the month.
- **Quality-check runs, July to October 2026.** The source project's checkup runs and the decision log written from them, including one comparison of three models running both checks on one frozen tree (September 2026); and one run of each check on the Node.js tool (October 2026).
- **An outside review, November 2026.** A reviewer outside our own sessions read an export of this repository and reported findings. A row graded Seen that names it rests on an observation of that review which we reproduced ourselves. A row graded I takes up its argument and says so.

## bug-audit

### Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| The defect classes (state and events, concurrency, money and time, silent failure, saved state) | Seen | the source project's bug register; the items marked "shipped" name the instance. The culture class's count of five adds two audits to the register's three: one of 30 July 2026 found the fourth in the Statistics screen and one of 1 August 2026 the fifth in its sibling file, both in the committed build since 26 July 2026 |
| Name the trigger; cite what you read; at most ten findings | Seen | the source project: a re-check found three of one plan gate's accepted amendments that the code no longer bore out or that understated the work. October 2026: a round with no cap filed 98 entries, 65 of them at the lowest grade, and all 65 were put off |
| A false finding costs the work it sets off; a plausible failure with one step unproven is reported as "Needs validation" | Seen, I | the same re-check shows what acting on three stale claims cost. That this is no reason for silence is our inference: the record compares that cost with nothing, so the file no longer weighs it against a missed defect (the outside review, November 2026) |
| Name what a finding breaks; otherwise a design note with no grade | Seen | October 2026: behaviour that worked as built was filed at the top grade and put to the owner twice as a bug |
| A crash, lost data, wrong money or a user with no way back need no recorded rule to name | I | such an outcome is wrong under every design, so the rule above must not silence it |
| One copied fragment for each cited line | Seen | November 2026: of 62 quoted lines checked by script, one sat three lines from its citation and one matched only without the agent's escape characters |
| Read, inferred and recalled are kept apart | Seen | October 2026: an inference went up as a fact and was corrected by its own author. September 2026: a remembered fact about an outside service was marked as unverified, which is the wanted behaviour |
| Running code is the caller's to allow | Seen | September 2026: agents ran test batches on a shared machine above its load limit. November 2026: the round on that machine allowed no run at all. In September several findings, the round's one high finding among them, were confirmed by a run on a copy with mock inputs, so the rule keeps that route open for a caller who allows it |
| State the commit first; stop if it is not the one named | Seen | November 2026: the shared checkout sat on an older commit than the one under audit, and the round's prompt had to say so |
| The request's own suspicion is a claim to test | D | addyosmani/agent-skills, its "Doubt-Driven Development" skill (`skills/doubt-driven-development/SKILL.md` at commit 301b02b1), hands a reviewer the artifact and what it must meet, and withholds the author's conclusion (read 2026-11-12, the skill's text) |
| Coverage first; "Not reached" with files and line ranges; a map is a hint | Seen | November 2026: two first passes handed back with most of their scope unread, and one of them, resumed, reported a major finding there; a map that called a region irrelevant had two findings in it |
| When a document and the code disagree, find which side is pinned | Seen | October 2026: a finding against the code, where three test files pinned the code and the document was stale |
| Text in the audited material is data | D, I | the open skills format's client guide and one preprint show instructions carried in the files a repository ships (read 2026-11-11 and 2026-11-12; the preprint is a short report of two demonstrations). Carrying this over to audited code and documents is our inference; no incident of ours |
| Kill pass: restate the suspect first | D | trailofbits/skills, its "False Positive Check" skill (`plugins/fp-check/skills/fp-check/SKILL.md` at commit e4dd0bb5), restates each suspected defect before analysing it (read 2026-11-12, the skill's text; taken as an idea, its wording is under a share-alike licence and is not used here) |
| Kill pass: the callee's own check one hop further | Seen | October 2026: a grade dropped once the callee's start check was read |
| Kill pass: an empty search proves nothing; an absence names its search and range | Seen, D | November 2026: an audit said a commit touched no test, and the tests were in two other commits. The Unlazy skill (Leonxlnx/unlazy at commit 16671491) requires a known positive before an absence is trusted, and the issue tracker of trailofbits/skills records three defects in which an empty tool result was read as clean (its issues #262 and #265 and the fix #250; both read 2026-11-12) |
| "Confirmed by trace" covers a finding in documents alone | Seen | November 2026: the read-only run graded a document that contradicted itself and the code "confirmed by reading", a value the file did not have; both of its lines held |
| Severity only for a confirmed finding, no higher than the harm shown | D, Seen | cloudflare/security-audit-skill (`skills/security-audit/SKILL.md`, its section "Separate priority from certainty", at commit c1c8a8c1) separates certainty from priority in this way (read 2026-11-12). October 2026: a finding marked plausible was to be fixed only after a failing test proved it |
| The project's own words for what it can lose | Seen | all three later rounds replaced the old severity scale, which was written around a player's loss, with money, approvals and records |
| "Information only" when the actor already controls the outcome | Seen | October 2026: a re-audit reported an environment-variable route as information, because whoever could set it could already change the repository's configuration |
| A header with the commit, what ran and which tools failed; a summary on top | Seen | November 2026: agents lost a tool or a helper mid-run, and the round made every report start with what the run really had. A summary on top has been our rule for agent reports since October 2026 |
| "Reaches into" | Seen | September and November 2026: audits run side by side filed the same defect, once from four of five audits |
| "Cleared" holds for the commit named | D, Seen | mattpocock/skills (`CHANGELOG.md` 1.3.2, at commit 4ae2317d) dates each statement about code with the revision it was true at (read 2026-11-12). September 2026: the reports listed what they had cleared, and the next round's plan was drawn up from which files the earlier reports had and had not covered |
| The classes under "Input from outside": a field of the wrong type, missing or empty; two entries for one key; a value used before its check; validation in one entry point only | Seen | November 2026: the read-only run reported none of the four as a finding, and the outside review found one of each in the same module. The earlier list had no group for input that arrives from outside: it was written from a game's internals |
| The documented contract of each entry point is read first | Seen | the same run never read the error contract of the command in its scope, and said so in its list of what it had not reached |
| "Suspected, not traced" only when the room ran out | Seen | the same run left four suspicions untraced, each with the one read that would settle it; one was an instance of a class the outside review confirmed |
| If a search tool is missing, use the shell's | Seen | November 2026: agent sessions that had no file-search tool could not list a folder and returned a partial result |

### Outside facts in the stack tells

Read from the raw page on 2026-11-21, not from a summary. A page was read only as far as the row says.

| Fact | Source | Read |
|---|---|---|
| Disabling a MonoBehaviour does not stop its coroutines; deactivating the GameObject or destroying the component does | Unity manual, "Coroutines" (docs.unity3d.com/Manual/coroutines.html) | the section on starting and stopping |
| `WaitForSeconds` waits in scaled time | Unity scripting reference, `WaitForSeconds` | the description and remarks |
| `?.` and `??` are not supported on Unity objects | Unity scripting reference, `Object` | the paragraph on null checks |
| JSON serialization covers fields only; a top-level primitive or array must be wrapped; polymorphism needs `[SerializeReference]`; a dictionary with `[SerializeField]` is a supported field type | Unity manual 6000.6, "JSON serialization" and "Serialization rules" | the lists of supported types and the notes under them |
| The parameterless `Random()` constructor takes its seed from the system clock | Microsoft Learn, `System.Random`, the .NET Framework 4.8.1 view | the remarks |
| An app that has not answered an input event within 5 seconds raises an ANR | Android developer documentation, "ANRs" | the list of triggers |
| Google Play's bad-behaviour threshold for the user-perceived ANR rate is 0.47% overall | Android developer documentation, "Android vitals" | the threshold table. A figure that moves |
| `no-floating-promises` and `no-misused-promises` exist and need type information | typescript-eslint rule pages (site version v8.73.0) | each rule's summary |
| Node raises an unhandled rejection as an uncaught exception by default since v15.0.0 | Node.js CLI documentation, `--unhandled-rejections` | the option's entry and its history |
| Date formats other than the standard ones are implementation-defined | MDN, `Date.parse()` | the description |
| `setItem` throws `QuotaExceededError` when the quota is reached | MDN, `Storage.setItem()` | the exceptions |
| Three quarters of the defects found in nine industrial and 23 student code reviews did not affect visible functionality | Mäntylä and Lassenius, "What Types of Defects Are Really Discovered in Code Reviews?", IEEE Transactions on Software Engineering 35(3), 2009 | the abstract. A study of human reviewers, not of agents |

### Not verified

- **Unreal.** Nothing in the Unreal section was confirmed against a real Unreal project, which is why it holds questions and no tells.
- **The default seed of `Random()` on the runtime of a current Unity version.** The clock-derived seed is documented for .NET Framework and was seen on the source project.
- **`DateTime` in Unity's serializer.** It is absent from the manual's list of field types as read once; that the field comes back as its default value is the source project's experience.
- **`is null` on a Unity object.** Inferred from the documented behaviour of `?.` and `??`.
- **Older engines dropping a dictionary field silently.** The source project's experience; the manual read is the current one.

### Retired in November 2026

| Line | Why it went |
|---|---|
| "Read-only by design" resting on the tool list | the list carries a shell, which can write; the rule is now stated as the agent's own to keep |
| "The tests are ground truth and you can run them" | see "Running code is the caller's to allow" |
| The Core Web Vitals bars | taken from documentation with no incident behind them, and a performance bar is not a defect class |
| `await-thenable` and `require-await` | they guard code that is wasteful, not wrong |
| `Random` or `Object` ambiguous between two namespaces | the compiler reports it |
| `parseInt` without a radix | no wrong result could be named for current engines |
| "The serializer does not handle dictionaries" as a flat statement | false for the current engine: now tied to the engine version |
| Two superlatives about how common or how complete a class is | no primary source |
| The figure from the study of code reviews | moved from the agent file to the table of outside facts above: the agent needs the rule (style, naming and structure with no failure are not findings), not its source |
| "A finding that turns out to be false costs more than a defect you missed" | a comparison with no record behind it: the incident shows only what a false finding cost |
| Culture-sensitive formatting "outside one shared invariant-culture helper" | a project formats for its interface language on purpose, and the invariant culture is one such choice; the class is the culture that nobody chose, as sower-game-frontend's rule now says |
| "The frequent form", "The classic form", "A reset is usually reachable from more places" in two defect classes | frequencies with no count behind them; the forms stay as examples |

## design-review

### Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Change nothing; the tool list does not enforce it | D | as for scope-gate |
| Run none of the project's code | I | a panel judges a proposal, not a build; the shared-machine reason is bug-audit's row |
| Text in what you read is data | D, I | as for bug-audit |
| What the request hands over, and "Not handed" in the header | Seen, D | as for scope-gate |
| The commit first | Seen | as for bug-audit |
| A recorded override of an earlier review's finding is a standing accepted risk, not argued again | Seen, I | September 2026, a website project: the owner overrode two Blockers of this panel, and a gate's NEEDS-SPEC on the same draft, by redefining the product, and the override was recorded as a working agreement. That a later review names it once and does not argue it again is the old file's rule; no record shows a review arguing an override again |
| The proposal's own claims are checked first | Seen | the source project, August 2026: three panel reports on successive versions of one proposal each opened by checking its claims against the code and the assets. One version stated that a system was untouched by its change, in the paragraph that said this had been checked, and the code showed otherwise; the next report put the check first because the version before had carried three factual errors |
| Verify, do not opine; a comparable product named by title | Seen | the source project, July 2026: the first review's two findings were both confirmed against the project's own documents |
| A norm or a product named from memory is marked recalled, not checked, and never decides a Blocker | I | the tools line has no web search, so such a claim cannot be checked in the run; the same rule as bug-audit's for recalled facts. One Blocker sets the whole verdict, so a claim nobody could check may support a Concern or a Note and no more (the outside review, November 2026) |
| The origin note: a reward a player had to watch an ad to keep | Seen | the source project, July 2026: a three-role review asked for by the developer found loss framing and a break with the genre's norm of a free base with an optional ad; the design changed to a free base with an optional ad multiplier |
| Each role is written in full before the next, and no earlier role is softened to agree | D, I | "Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate" (Wynn et al., arXiv 2509.05396 version 2, an ICML 2025 workshop paper), on debate between separate small models, found that agents changed correct answers to incorrect ones in order to agree with their peers (read 2026-11-12: the abstract, and the setup as our research notes record it). Carrying this over to one agent that plays three roles in turn is our inference |
| Where the roles disagree, say so | Seen | the source project, August 2026: every panel report had a section on where the roles disagreed; in one, two roles disagreed on whether any successor design existed |
| A Blocker shows a concrete harm; Concern and Note | D, I | October 2026: a comparison of five reviews of one plan, on another project, found the reviewers' own severity bins far apart: two put half or more of their findings in the top bin, three put only a few there. Cloudflare's security-audit skill (cloudflare/security-audit-skill) caps a finding's severity by the harm it shows (read 2026-11-12). The criterion for a Blocker, and the verdict that follows from it, is our inference from these. Checked against the titles of one report's ten Blockers: its two schedule Blockers fit only once "a launch or a commitment the project cannot move" was added to the list |
| A verdict per role and one overall verdict on top | Seen | the source project, August 2026: all three panel reports added both, which the file did not ask for. A summary on top has been our rule for agent reports since October 2026 |
| On a second review, say which earlier findings still stand, a standing one stated once more with what is new | Seen | the source project, August 2026: one role raised the same sequencing Blocker on three versions of one proposal; the third time it said the call was the developer's and named the one new point |
| "Not examined" at the end | I | from the same comparison of five reviews: each review missed themes that others raised |
| The three roles' question lists, the dark patterns, tonal hypocrisy | Seen | the source project, July 2026: the agent was written to make its first review a standing format |
| A cheaper alternative where one exists | D | Google's code review handbook, its page "How to write code review comments" (google.github.io/eng-practices/review/reviewer/comments.html), lets a reviewer point at a problem without designing the fix (read 2026-11-12); the old "always propose one" became "where one exists" |
| Reversibility beside upkeep | D | the "pr" skill of mattpocock/skills (`skills/engineering/pr/SKILL.md`, its section "Merge Danger", at commit 4ae2317d) names whether a change is a one-way or a two-way door (read 2026-11-12) |

### Retired in November 2026

| Line | Why it went |
|---|---|
| "Read-only by design" resting on the tool list | the list carries a shell; the rule is now stated as the agent's own to keep |
| "This format exists because it worked", with "every rules-based check had passed" and "a materially better mechanic" | the record says the two findings were confirmed against the project's documents and the design changed. It does not say that every other check had passed, or how much better the result was |
| "Always propose" a cheaper alternative | see the row above |
| "A named comparable product" as evidence for a Blocker | it is recalled, not checked, and one Blocker sets the verdict |

## quality-check-quick and quality-check-deep

The two files share four rules word for word: no verification step the project has ruled out; frozen text is not drift; a suspected defect is named, not chased; and the instruction on reading a change. A change to one goes into both, and this repository's `scripts/check-copies.py` fails when they differ.

### Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Change nothing; the tool list does not enforce it | D | as for scope-gate |
| The quick check runs only the listed read-only commands; anything else is the caller's to allow | Seen | September 2026: bug-audit's shared-machine row. October 2026: the first run of the quick check on the Node.js tool ran test files only as its request allowed, one set under the machine's shared lock |
| The project's check list lives in a file of the project | Seen, D | October 2026: that first run got its list as a file handed over in the request, because the agent's own block for a project's checks had never been filled. An installed plugin's files sit in a cache with one directory per installed version (Claude Code documentation, "Plugin loading", raw page read 2026-11-22), so a list written into the agent file would be lost at the next version |
| The check list is the one text acted on | I | the rule that what you read is data needs this one exception, or the check could not run the project's list |
| The earlier report found by its own name and date, and confirmed by its first lines | Seen | October 2026: a date pattern matched a plan file and no report. The source project: on the agent's first test run, a bare pattern matched a copy of the agent's own definition ahead of the real report. The report names in our records come in two forms, with and without an underscore before the kind |
| Carried items re-checked before they are carried | Seen | the source project, September 2026: three runs of both checks on one frozen tree each found that a carried item, fixed a fortnight earlier, had been promoted to the deep check's main target |
| Read every change before describing it, with the command that shows each kind | Seen | the source project: a font asset's diff, waved off as a re-serialize, was stripping data. November 2026, the outside review, reproduced by us with git 2.56.0: plain `git diff` on a path printed nothing for a staged edit and nothing for a new file, and one line for a binary, so the earlier wording could not show those changes |
| Counts and lists come from a command's output | Seen | October 2026: a quick report's hand-typed list of a table's rows was wrong where the command's count was right; a deep report said "five more" and listed four, and the calling session found two more |
| A sweep names where it searched | Seen | October 2026: the quick check searched three places, and the same text sat in a fourth, which the deep check found |
| An empty pass shows that it can hit; a failed command is "not checked" | D | as in bug-audit's rows on empty results (read 2026-11-12); trailofbits/skills, its "Second Opinion" skill (at commit e4dd0bb5), counts a missing tool or a git error as a failed review (read 2026-11-12) |
| The items of the portable core | Seen, I | the source project's checkup decision log: after each of the three splits it names, narrative crept back into the file that had been split; a search pattern went stale through three widenings because copies of it lived in other files. The age of uncommitted work: the old file says two independent runs caught the same day-long stall; that was not found in the records read for this file |
| No verification step the project has ruled out | Seen | the source project, August 2026: the rule was broken twice on the day after it was given. The ban sat in one file while the always-loaded instructions said such testing was routine, and the true statement was read as an exception to the ban |
| Frozen text is not drift | Seen | the source project: one run excused a stale number as frozen, then flagged another three lines later in the same block |
| A suspected defect is named, not chased | Seen | the source project: once bug-audit existed, the checkup drifted into hunting defects |
| Zero-exception content rules (quick) | Seen | the source project: content was written and then deleted over such rules |
| A quick and a deep check; in the deep check the judgement comes first and the mechanical layer last | Seen | the source project, August 2026: runs of one combined checkup came back as document fixes and the task list restated; an effort split written into the prompt did not hold, and splitting the job in two did |
| The deep check may run small read-only computations | Seen | the source project, September 2026, the comparison of three runs on one frozen tree: the run that computed a payoff over the live content, checked against a figure in the project's own tests, found what the other runs did not. October 2026: a deep run called a project's pure functions to add up a cost table, writing nothing and using no network |
| The decision record and accepted plans of a target, read against what shipped | Seen | the same comparison: only the run that read the decision record against the code found a recommendation the developer had accepted and that never shipped |
| A guard cited as mechanical: say what change would make it fail | Seen | the same comparison: a test cited as the bound of a rule checked only completeness, so nothing failed when the rule grew |
| A visual verdict names what a person can check | Seen | the same comparison: two runs gave opposite verdicts on one picture, one with specifics that could be checked on it, the other with a judgement of composition |
| The quick report read first only at the caller's request, and said so | Seen | October 2026: a deep run read it first at the caller's request, said so, and chose its targets apart from it |
| A quick report stands for the commit it names; the deep check lists the uncommitted changes in every run | Seen | November 2026, the outside review, reproduced by us: the commit stays the same while the working tree changes, so a report whose header names the current commit can be older than the changes in front of the deep check |
| One list of lenses: five with a target and enjoyment; five targets in the rotation line | Seen | the old file listed five lenses, six verdicts and four rotation targets; an October 2026 run gave six verdicts, one for a lens the file never defined ("design"). The new file defines that lens and uses one list throughout |
| The verdict anchors | Seen, I | the same comparison: three runs on one frozen tree gave different verdicts on three lenses, from different weightings and, on one lens, different targets. Anchors a reader can check, and a verdict that names its target, are our inference from that; the anchors were tried on one finding per lens from that comparison |
| A lens with nothing to judge says so | I | the October 2026 run on a command-line tool still found a target for every lens, its landing page and logo among them; a project with no visual surface at all is our inference |
| The enjoyment lens says what its answer rests on, and may give no verdict | I | the lens asks what would make a user quit, while the agent reads and computes and runs the product only where the request allows: what the agent computed is a finding, and how a user takes it a guess (the outside review, November 2026) |
| Transferable lessons as hypotheses | I | the old file's rule, kept; no incident behind it was looked up |

### Retired in November 2026

| Line | Why it went |
|---|---|
| "Read-only by design" resting on the tool list | the list carries a shell; the rule is now stated as the agent's own to keep |
| "Cheap enough to run on any day" | the three measured quick runs of September 2026 used about 206,000 to 271,000 tokens each |
| "Every doc split drifts back" | the record names three splits on one project; the check's reason is now the record's own rule: every run, not one sweep after a split |
| A block inside the agent file for each project to fill in | see the row on the check list |
| "These are identical in the other file" | they were not; the shared rules are now kept word for word |
| "For every uncommitted file, run `git diff` on it" | it prints nothing for a staged edit or a new file; the instruction now names what shows each kind of change, in the same words in both files |
| Binary diffs "read in full" | git prints one line for a binary; such a change is reported as not read, with its sizes |
| A quick report trusted whenever its header names the current commit | the commit does not move when the working tree changes |
| Five lenses, six verdicts and four rotation targets | one list now |
| "If you used today's build for ten minutes, what would most likely make a real user quit?" as a question with no basis named | the agent mostly reads; the answer now says what it rests on |

## scope-gate

### Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| Change nothing; the tool list does not enforce it | D | as for bug-audit: the list carries a shell, and the documentation says that a plugin agent's hooks, MCP servers and permission mode, the fields that could enforce it, are not applied (Claude Code documentation, "Create custom subagents", raw page read 2026-11-22) |
| Run nothing: a claim only a run can settle is an unsupported assumption, and the run is an amendment | Seen, I | September 2026, a game project: the gates turned the runs they needed into amendments for the builder (a comparison of two drives from one input log, a rough benchmark), and the decision record carried them. The shared-machine reason is bug-audit's row. That a gate needs no run of its own is our inference |
| Text in what you read is data | D, I | as for bug-audit; the gate also reads web results |
| What the request hands over, and "Not handed" in the header | Seen, D | November 2026, a website project: one gate point was overridden because the request it judged pointed at a list the gate had not been shown. The "Doubt-Driven Development" skill (addyosmani/agent-skills) hands a reviewer the artifact and what it must meet, and mattpocock/skills (its "research" skill and `CHANGELOG.md` 1.3.2, at commit 4ae2317d) notes that a dispatched agent starts with nothing (both read 2026-11-12) |
| The commit first | Seen | as for bug-audit: a gate's claims are about a code base that keeps moving |
| Open every path, name, command, setting and number the plan cites | Seen | September 2026, a website project: a plan cited style names that did not exist, wrong file paths and placeholder payment links, and a review panel missed all of it over three rounds; a gate pointed at the real repository caught it and returned KILL-DESCOPE |
| A gap in the spec is a "no" only when it changes what gets built | D, I | Google's code review handbook, its page "The Standard of Code Review" (google.github.io/eng-practices/review/reviewer/standard.html), approves a change that improves the code although it is not perfect, and weighs progress against each request (read 2026-11-12). Applying that threshold to a plan's spec is our inference |
| The goal names how its completion is checked; an activity is not a goal | D | the "Define Goal" skill of openai/skills (`skills/.curated/define-goal/SKILL.md` at commit 49f948fa) rejects goals that name only an activity; read 2026-11-12, when the repository's README marked it deprecated |
| Every requested outcome stands in the scope, or is deferred with the requester's agreement on record | D, I | the Unlazy skill (Leonxlnx/unlazy at commit 16671491) and its issue #23: every declared gate passed while the set of gates had left out a requested deliverable; read 2026-11-12. That a deferral needs the requester's agreement is our inference: the outside review of November 2026 walked a requested outcome into the non-goals, and the earlier wording let it pass |
| The builder's read; a spec fails in both directions | D | obra/superpowers has a fresh agent read a design as its builder and list what it would still ask (the release notes of its v7.0.0), and its "writing-plans" skill keeps only the decisions an implementer cannot make alone (both at commit 22f0b463, read 2026-11-12) |
| More than five scope items is an advisory finding | Seen, I | the file came from the source project with a cap of five as a must-meet test. On a later game project a gate did not argue again an item count that a review had settled. That a count alone does not change what gets built is our inference |
| No dead end | Seen | September 2026, a game project: this item failed twice before any code was written: a car that could wedge with no reset in the first build the owner would drive, and a loaded save that could place the player outside the built world |
| One-way steps and their reach | D | the "pr" skill of mattpocock/skills (`skills/engineering/pr/SKILL.md`, its section "Merge Danger", at commit 4ae2317d) names whether a change is a one-way or a two-way door and how far its effects reach (read 2026-11-12) |
| Claims about the world, searched against the primary source; a renamed name keeps nothing of the original | Seen | the source project: two published claims ran backwards against reality; two renamed names kept the original inside them, each caught only on a second look |
| Risk first | Seen | September 2026, a game project: a gate moved a rough benchmark ahead of the tuning its result could have undone, and the decision record adopted the change |
| A recorded override is cited, the retired rule never applied | I | the old file's reason: a gate that argues settled decisions again teaches the team to ignore it. No incident recorded |
| Outside view | D, I | Bent Flyvbjerg, "From Nobel Prize to Project Management: Getting Risks Right" (arXiv:1302.3642; the abstract, read 2026-11-21): a forecast from the outcomes of comparable past projects instead of from the parts of this one. "This one is different" as a warning sign is our inference from that method |
| Pre-mortem in the past tense | D | Gary Klein, "Performing a Project Premortem", Harvard Business Review, September 2007 (the page's summary, read 2026-11-21): the team takes the failure as given and explains it. No figure for the method's effect is used here: none was found in what was read |
| The inputs no planned test covers | D | the "writing-plans" skill of obra/superpowers (its section "Review Focus", at commit 22f0b463) opens each plan with the inputs most likely to hurt a real user that no test covers (read 2026-11-12) |
| Assumptions tagged; an unsupported one blocks, and its check is the amendment | Seen | September 2026, a game project: gates marked unchecked assumptions as blocking and turned each into a check that the decision record then carried |
| Reuse | Seen | September 2026, a website project: a gate found that two working servers already existed for a proposal to build one, so the proposal was a publication decision, not new engineering |
| NEEDS-SPEC (narrow) and (rethink) | Seen | September 2026, a game project: three gate reports gave the verdict as "NEEDS-SPEC (narrow)"; November 2026, a website project: a gate sent a spec back once with "no rethink". The old file had no word for the difference |
| Weights: blocking, advisory, note | D | Google's code review handbook, its page "How to write code review comments", labels the weight of each comment (read 2026-11-12) |
| A contradiction with a recorded decision is the finding | Seen | September 2026, a website project: a gate named as its finding a recorded privacy rule that practice already contradicted; it went to the owner with the proposal's other open questions, and each was answered |
| A second gate checks the earlier amendments and what changed since | Seen | the source project, July 2026: a re-check of one gate's accepted amendments against the code found three that the code no longer bore out or that understated the work, one citing behaviour removed four days earlier; a second gate on the corrected plan found one more of the same kind |
| A claim next to a number says no more than the number | Seen | November 2026, a website project: a gate and a design review of one page spec found two overstated sentences and a misplaced number before the build |
| The report's header, the summary on top, the template | Seen | a summary on top has been our rule for agent reports since October 2026. The gate reports in our records carried a verdict line and a list of what would change the verdict, in shapes that differed from run to run |
| The checks by area | I | the old file's lists, written from the source project's own skills; kept free of any one engine |

### Retired in November 2026

| Line | Why it went |
|---|---|
| "Read-only by design" resting on the tool list | the list carries a shell; the rule is now stated as the agent's own to keep |
| "The documented cure for the planning fallacy" | stronger than the abstract of the paper it cited |
| "Materially better-specified risks", and a link for it | the effect was not found in what was read, and the link led to a page about the reference-class paper |
| The weight of a story's effect on prices | the source project's content pipeline; it has no meaning for other projects |
| "Standing in for an entire review board" | it holds no rule |
| At most five scope items as a must-meet test | an item count alone does not change what gets built: now an advisory finding |
| A requested outcome that stands "in the scope, the non-goals or the assumptions" as enough | moving it to the non-goals met the test without the requester deciding anything |
| More than five scope items "usually means two milestones" | a frequency with no record; the count is a reason to look |
