# The search landscape in 2026: dated figures, and where each came from

*Open this file when a task needs a current figure about search. Every figure here carries its source and the date it was read. Read it again before you act on it: these numbers move within months, and a figure older than a quarter or two is history, not a fact about today.*

**Grades.** **D** = read in the named source on the date given. **I** = inferred, with the reason in the sentence. Vendors' figures are not kept here: they disagree with each other and move. Where each line comes from: `evidence.md`, its section on this file.

## Ranking updates of 2025 and 2026

The Google Search Status Dashboard lists each update with the day it started and how long it ran. As read on 22 November 2026 (D):

| Update | Started | Ran for |
|---|---|---|
| November 2026 core update | 10 Nov 2026 | no length shown when read |
| September 2026 spam update | 24 Sep 2026 | 13 days, 16 hours |
| August 2026 spam update | 18 Aug 2026 | 2 days, 16 hours |
| June 2026 spam update | 24 Jun 2026 | 2 days, 1 hour |
| May 2026 core update | 21 May 2026 | 11 days, 21 hours |
| March 2026 core update | 27 Mar 2026 | 12 days, 4 hours |
| March 2026 spam update | 24 Mar 2026 | 19 hours, 30 minutes |
| February 2026 Discover update | 5 Feb 2026 | 21 days, 17 hours |
| December 2025 core update | 11 Dec 2025 | 18 days, 2 hours |
| August 2025 spam update | 26 Aug 2025 | 26 days, 15 hours |
| June 2025 core update | 30 Jun 2025 | 16 days, 18 hours |
| March 2025 core update | 13 Mar 2025 | 13 days, 21 hours |

The dashboard gives names, dates and lengths; it does not say what an update did to any site. A figure about traffic lost or won in an update is someone's case data: name whose it is and its date. For any update after 22 November 2026, read the dashboard itself.

## AI summaries and clicks: one independent measurement, and your own numbers

- **An independent measurement** (Pew Research Center, "Google users are less likely to click on links when an AI summary appears in the results", published 22 July 2025, read 22 November 2026, D). It used the browsing data of 900 adults in the United States in March 2025: of 68,879 Google searches, 12,593 showed an AI summary. Where a summary appeared, people clicked a traditional result in 8% of visits; where none did, in 15%. A link inside the summary was clicked in 1% of visits to pages with one, and the session ended after 26% of pages with a summary against 16% without. It is one country and one month of 2025, and it compares visits with and without a summary; it does not test what caused the difference (I).
- **Your own numbers.** Search Console's Generative AI performance report (its help page read 22 November 2026, D) counts how often links to your site were shown in AI Overviews and AI Mode, by page, country, date and device, with a filter for text and image searches; by 31 August 2026 it had reached every site. It counts impressions; the help page does not mention clicks. Its data is part of the "Web" search type of the main Performance report. A site with too few impressions, or one that has opted out (below), may not see the report.

## Being shown or cited in AI answers

Google's guide "Optimizing your website for generative AI features on Google Search" (last updated 10 July 2026, read 22 November 2026, D) says what matters most is content that is unique and not a commodity: a first-hand view, where a summary of what already exists adds nothing (SKILL.md section 2 builds on the same point). It also lists what Search ignores, so a vendor's offer of one of these is a claim to check:

- llms.txt and other special files, markup or Markdown: Search does not use them, and keeping them for other services neither helps nor harms a site there;
- cutting content into small chunks for AI: not needed, and there is no ideal page length;
- rewriting content in a special way for AI: not needed;
- chasing mentions on other sites that are not genuine: its ranking systems look for quality content and other systems block spam, and its AI features rely on both;
- leaning on structured data: not required for these features, and no special schema.org markup is needed, though it still helps a page qualify for rich results.

The same guide warns that making separate pages for every way a question might be asked, mainly to manipulate rankings or AI answers, falls under the scaled content policy, and that no third-party tool has access to Google's internal ranking or AI systems: weigh a tool that claims otherwise against the official guidance.

**What a site controls** (each from the page named, read 22 November 2026, D):

- crawling for Search: robots.txt rules for Googlebot ("AI features and your website", last updated 10 December 2025);
- what is shown from a page: nosnippet, data-nosnippet, max-snippet and noindex (the same page);
- inclusion in AI features: Search Console's setting "Search generative AI" (its help page). The default includes the site, and the guide says a site must be included to appear in these features at all. Excluding it keeps its links and content out of AI Overviews, AI Mode and Discover's AI features, and takes effect within a few days; the help page says the setting is not used as a ranking or inclusion signal for the rest of Search;
- training: the Search generative AI setting does not change it; Google-Extended is the control both pages name for limiting how Google's models are trained on a site's content;
- a change to a preview control takes effect only after a recrawl, which may take days or months; the URL Inspection tool shows the HTML Googlebot received, so you can see whether the control reached it.

## What this file does not cover

Local search, the structured data of online shops, and the technical search problems of particular platforms (pages rendered by a headless CMS, a site built on JavaScript that crawlers must render) were not researched for it; Google's guide has a section on local and shop details that was not read. If a task needs one of them, read fresh instead of stretching this file's general advice.
