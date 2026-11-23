# Evidence for seo-operator (dated)

*Read this file before anything from `SKILL.md` or one of its reference files is relied on or quoted. It says where each rule and line comes from and when its source was read, so that whoever maintains the skill can tell when one may go. Search documentation changes often: read a page again before you rely on it.*

**Grades.** **D** = documented in a named source, read on the date given, with how it was read. **Seen** = it happened in our own work. **I** = inferred; the row says from what. Nothing here was measured: no site was run with and without a rule.

## Sources read for this file

| Source | Read | What was read |
|---|---|---|
| Google Search Central, "Spam policies for Google web search" (developers.google.com/search/docs/essentials/spam-policies), last updated 2026-08-28 | 2026-11-22, the whole page through a reader agent, and the quoted sentences checked again in the raw page by script | the opening paragraph, the scope sentence, the definition and examples of scaled content abuse, the site reputation policy |
| Google Search Central, "AI features and your website" (developers.google.com/search/docs/appearance/ai-features), last updated 2025-12-10 | 2026-11-22, the same way, the sentences on snippets and links included | what AI Overviews and AI Mode do with links, the requirements for appearing, structured data, how the traffic is counted, the preview controls |
| Google Search Status Dashboard, the history of ranking updates (status.search.google.com) | 2026-11-22, the list of updates through a reader agent, and all twelve rows of 2025 and 2026 checked again in the raw page by script; the pages of single incidents were not read | the names, start dates and durations of the updates of 2025 and 2026 |
| Google Search Central, "Optimizing your website for generative AI features on Google Search" (developers.google.com/search/docs/fundamentals/ai-optimization-guide), last updated 2026-07-10 | 2026-11-22, the raw page by script, whole | every section; the pages it links to were not read |
| Search Console Help, "Generative AI performance report (Search)" (support.google.com/webmasters/answer/16984139) | 2026-11-22, the raw page by script | what the report counts, its dimensions and filter, the note on its rollout, why a site may not see it |
| Search Console Help, "Search generative AI control" (support.google.com/webmasters/answer/16908024) | 2026-11-22, the raw page by script | the three choices, what excluding a site does and does not do, how long a change takes |
| Pew Research Center, "Google users are less likely to click on links when an AI summary appears in the results" (pewresearch.org), published 2025-07-22 | 2026-11-22, the raw page by script | the sample and its dates, the four figures, the note that only Google was covered |
| Our own records | 2026-11-22, a name search of the site projects' markdown files | one task brief points to this skill; no record of a run was found |

## Where the rules come from

| Rule | Grade | Behind it |
|---|---|---|
| The engine judges the page, not the author | D | the spam policy: scaled content abuse is many pages made mainly to manipulate rankings and not to help users, "no matter how it's created"; one of its examples is generating many pages with generative AI tools without adding value |
| The policies cover attempts to manipulate the engine's generative AI answers | D | the spam policy's opening paragraph names attempts to manipulate generative AI responses in its search; its scope sentence says the policies apply to all web search results |
| AI features need no special file, markup or optimization | D | "AI features and your website": no additional requirements and no special optimizations; no new machine-readable files, "AI text files" or markup; no special structured data; a page must be indexed and eligible to show with a snippet. Google's guide of July 2026 adds that the site must be included in Search Console's "Search generative AI" setting, the default |
| Being cited is worth pursuing; AI Overviews often do not appear | D | the same page: the features show links to supporting sites, and AI Overviews appear only when the engine judges them additive, so they often do not |
| Ranking updates are frequent; read them on the status page | D | on 2026-11-22 the dashboard listed core updates starting 27 March, 21 May and 10 November 2026 (the last still running) and spam updates starting 24 March, 24 June, 18 August and 24 September 2026. The skill names the page, not the list, because the list changes with every update |
| Vendor figures stay out of the skill | I | the figures the old file quoted came from SEO vendors' blogs and case data, disagreed with each other, and more ranking updates followed within months of the writing; the dated reference keeps such figures with their sources |
| Cluster before volume | I | a cluster gives a reader, a crawler and an AI answer several pages of the site on one question; the old file's figures for how much faster clusters rank came from vendor blogs and are not used; the size of five to seven pieces is the old file's, with nothing measured behind it |
| No post without a first-hand fact | D, I | the scaled-content definition above; that a post needs a fact only this site has is our reading of "unoriginal content that provides little to no value". The policy itself is about many pages made mainly to rank, so the skill gives the rule as its own and keeps the policy's test apart from it |
| The three cases by shape | I | drawn from the shapes of our own small sites when this skill was written; no outcome was measured, so the cases carry no ranking of which is riskier or more common |
| Forum content is a moderation risk | I | the thin-content checks judge pages the site writes; posts by users are a different problem |
| The answer near the top; specific headings | I | a reader skimming and an answer that quotes a page both start at the top; the old file's figure for where AI citations draw from came from a vendor and is not used |
| Structured data only where it is true | D | "AI features and your website" lists making structured data match the visible text of the page among its best practices |
| The basics: a page that works on a phone, loads fast, and can be crawled and indexed | D | "AI features and your website": being indexed and eligible for a snippet is the condition for appearing at all. Google's guide of July 2026 names among the technical basics a page that displays well on every device with little latency, and content that can be crawled |
| The brief's four parts | I | the old file's claim that a bare topic produces generic output, now stated as what a topic name cannot carry; no record of ours was looked up for this file. Each limit in point 3 is written with what to do instead, as our skill on writing agent instructions asks |
| Read before write; check every number, an untraced figure flagged and kept apart from one a source shows to be wrong; test the artifact; audit a sample on a schedule | Seen, I | seen in our build and audit work, where the planning skill and the review agents carry the incidents; carrying them over to SEO work is our inference. The flag is that of the writer plugin's fact-checking skill, which flags a claim that traces nowhere and does not call it false |
| AI-feature traffic is counted inside the console's "Web" search type; the Generative AI performance report counts impressions | D | "AI features and your website": the traffic is included in the overall search traffic and reported in the Performance report within the "Web" search type. The console's help page on the Generative AI performance report: impressions in AI Overviews and AI Mode, by page, country, date and device; the page does not mention clicks |
| A drop in clicks after an AI Overview is not by itself a content failure | I | an answer shown above the results can take a click while the page still answers the query and may be cited; the size of the effect in one independent measurement is in `references/2026-search-landscape.md`; the engine's page itself claims that clicks from such results are of higher quality |
| Monthly as a floor | I | a site with little content has little to measure faster; no source measured a cadence |
| The honesty mandate | I | an agent can find that a fact is missing but cannot supply it; a page that only restates others matches the policy's "unoriginal" |
| The session prepares the judgement on topics; the person makes it, and chooses what is written and published | Seen | our decision of November 2026: the row on what a person keeps, under `references/briefing-and-verification.md` below |

## Retired in November 2026

| Line | Why it went |
|---|---|
| AI Overviews "on roughly 47-64% of queries" and a click-through cut of "30-50%" | vendor figures that disagreed with each other and moved within months |
| Sites "lost up to 94% of organic traffic within three weeks" in the March 2026 update | vendor case data; the update itself is real and dated above |
| Clusters "rank faster and hold longer", from two blogs | no primary source |
| "A large share of LLM citations draw from roughly the first third of page text" | a vendor's figure |
| Structured data "cited roughly 3x more often" | a vendor's figure, against the engine's own statement that no special structured data is needed |
| "Negative constraints move agent output further than positive ones" | a vendor's claim; our skill on agent instructions records that its sources disagree on bans and keeps a ban beside the behaviour wanted |
| "Re-check before quoting them past mid-2026" | a rule that branches on a date; each figure now carries its own date in the reference |
| A business profile for a local angle | the plugin's README says local search is not covered |
| "general delegation/scope discipline" handed to the planning skill | that skill has no such section; the one lesson borrowed from it is named where it is used |
| "The single most counterintuitive fact" and "the single highest-leverage check" | superlatives with nothing measured behind them |
| The heading "Mistakes to actively flag" | now "Mistakes to flag", as in the other skills |
| "holds one topic" among the basics of a page | Google's guide of July 2026 says its systems understand several topics on one page and that there is no ideal page length |
| "A bare topic name reliably produces generic output: it is the most common way delegated SEO work goes wrong, and the brief prevents it" | a frequency and an effect nobody measured; the reason for the brief stays, graded I |
| "a publishing cadence with nothing new to say each time is the shape the scaled-content policy describes"; "So the question is [...] does this page say something only this site could say" as what the policy asks | the policy is about many pages made mainly to rank; the first-hand-fact rule is ours, and the lines now say so (an outside review of this repository, November 2026) |
| "The wrong first move is the common one"; a new site as "the highest-risk case" | a frequency and a ranking with nothing measured behind them |
| "Treat an unchecked figure [...] as false until it is checked, the same way the fact-checking skill treats any claim" | that skill flags such a claim and does not call it false; an accurate figure with a missing source would have been corrected as wrong |
| A clean audit as "more likely a rubber stamp than an audit" | a likelihood with no count behind it; the line now asks what the report checked |
| "You decide what search and content work is worth doing" and "You decide whether a page should exist at all, which is the decision most SEO advice skips" | the skill's own reference keeps that judgement with a person, and we decided in November 2026 that the session advises; "most SEO advice" was a frequency with no record. The lines that told the reader to publish, to grant access or to supply the fact now give those to the person |

## references/2026-search-landscape.md

The file carries each figure's source and date inline, as SKILL.md promises; the rows point to the sources above and do not repeat the dates.

| Line | Grade | Behind it |
|---|---|---|
| The updates of 2025 and 2026, with start and length | D | the Google Search Status Dashboard (above) |
| An independent measurement of clicks beside AI summaries | D | Pew Research Center (above) |
| Your own numbers: the Generative AI performance report | D | its help page (above); that traffic also counts in the main report: "AI features and your website" |
| What matters most, and what Search ignores | D | Google's guide to its generative AI features (above) |
| What a site controls | D | "AI features and your website" and the help page on the Search generative AI control (above) |
| What the file does not cover | I | the old file's own account of what its research left out, and the sections of Google's guide that were not read |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "Every figure here was searched, not recalled, in September 2026" | true then; each figure now carries its own source and the date it was read |
| The May 2026 clarification of the spam policies, dated by a trade publication | the policy page itself says what the clarification said; only the month came from the publication |
| "SpamBrain does not have an 'AI-written' detector as a ranking signal", from a vendor's page | a claim about the engine's internals that the engine's own pages do not make; the policy's own test (value and scale) is in SKILL.md section 1 |
| The March 2026 update "processed in under 20 hours - the fastest turnaround in Google's update history" | the dashboard gives the March 2026 spam update 19 hours, 30 minutes and the core update 12 days, 4 hours; "the fastest" had no source |
| The AI Overview figures (47-64% of queries, a click-through cut of 30-50%); the 94% traffic loss and the fingerprint of the sites hit; the share of citations drawn from the first third of a page; structured data cited about 3x more often; clusters that rank faster, and a March 2026 weighting of topical authority | the same lines left SKILL.md for the reasons in the table above; this file carried them too. An independent measurement and the site's own report replace the AI Overview figures here |
| The practitioner advice on being cited (the answer near the top, headings shaped like questions, the same answer restated across pages and formats), from frase.io and almcorp.com | the engine's own guide now says what matters and what it ignores; the first two points stand in SKILL.md section 3 as inferences, and one answer restated across many pages comes close to the scaled content its policy describes |

## references/briefing-and-verification.md

| Line | Grade | Behind it |
|---|---|---|
| The four parts of the brief | I | the old file's template; the third part now names what to do instead of each limit, as SKILL.md section 4 does |
| What an agent may do and what a person keeps | I, Seen | the old file's split. That the session which loads this skill advises, and the person chooses what is written and what is published, is a decision made for this skill in November 2026, when an outside review found the skill's opening and this list answering that question differently |
| The four checks | Seen, I | the checks of SKILL.md section 5; our build and audit work carries the incidents behind them, in the planning skill and the review agents, and carrying them over to SEO work is our inference |
| Where this does not work well | I | the old file's reasoning; nothing measured |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "A bare topic name reliably produces generic output" | a frequency nobody measured; the reason for the brief stays, graded I |
| "Explicit negative constraints. State what the piece must NOT do", and "Negative constraints move agent output further from generic than positive instructions alone" | an effect nobody measured; each limit now names what to do instead |
| "Agents hallucinate specific numbers and citations as a routine failure mode, not a rare one" | a frequency nobody measured; the check stands without it |
| "missing schema" as a review finding | the engine says no special structured data is needed; the finding is now structured data that does not match the page |
| "an agent guessing at internal linking either over-links everything or links nothing" | a prediction with no reason given; the reason now given is that an agent does not know which pages matter most |
| `sower-writer:drafting` by its full name | the neighbour in another plugin is named by its role |

## references/content-clusters-small-sites.md

| Line | Grade | Behind it |
|---|---|---|
| The order of a cluster on a new site | I | the old file's sequence; five to seven pieces is its size, with nothing measured behind it |
| A cluster built on questions nobody asked has the shape of scaled content | D, I | the spam policy's definition (SKILL.md section 1); reading an unasked cluster that way is our inference |
| Link from the first day, to the pieces that exist, with the links back in the same step; a second cluster only once the first is real | I | the old file's reasoning. Its "at least two others" could not be met by a site's first piece |
| The pressure of a declared priority | I | the old file's reasoning |
| Community content as a separate surface | I | the old file's rule; SKILL.md section 2 states the same case |

Retired from this file in November 2026:

| Line | Why it went |
|---|---|
| "An uninterlinked set of pages about the same topic gets none of the topical-authority benefit clusters are chosen for" | a ranking effect with no source |
| "A slower cadence with a real fact behind every piece outperforms a faster one without, on the evidence in `2026-search-landscape.md`" | that evidence was vendor claims, now retired there |
| "the scaled-content pattern that gets penalized (see `2026-search-landscape.md`)" | the pattern is the policy's own definition, in SKILL.md section 1 |
| "Each piece links to at least two others of the cluster when it is published" | a site with no content yet has no two others for its first piece |
| A cluster on unasked questions as "the shape" the scaled-content policy "describes"; a slower cadence justified by "the policy's own definition" | the policy is about many pages made mainly to rank; the reason given is now the skill's own rule |
