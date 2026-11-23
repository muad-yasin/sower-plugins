# sower-marketing

SEO strategy, and briefing SEO and content work to AI agents and checking what comes back, for small
and new sites with little content, not for an established blog.

This plugin's job is upstream of prose: deciding whether a page is worth writing at all, briefing
an agent so that its output is not generic, checking SEO work before it ships, and saying plainly
where an agent cannot do the job.

Install from this repository's marketplace, in a Claude Code session (this repository's root README says which version this form needs):

```
/plugin install sower-marketing --marketplace muad-yasin/sower-plugins
```

## What's in it

One skill:

- **`seo-operator`**: works out what search and content work is worth doing on a small or new site
  and puts it to the person who decides, briefs the chosen work to an agent so that the result is
  not generic, and checks SEO work before it ships, for classic search results and AI answers
  alike, against the search engine's own documentation. It says what to measure, and where an
  agent cannot do the job.

With four reference files, loaded on demand:

| File | Read it when |
|---|---|
| `2026-search-landscape.md` | you need a current figure: the ranking updates of 2025 and 2026, one independent measurement of clicks beside AI summaries, the Search Console report on AI features, and what a site can control. Each figure carries its source and the date it was read; **read it again before you rely on it** |
| `briefing-and-verification.md` | writing a brief for an agent, or checking whether agent-produced SEO work is real before it ships |
| `content-clusters-small-sites.md` | planning what to blog on a site that has little or no content yet |
| `evidence.md` | before anything from `SKILL.md` is quoted: where each rule comes from, the search engine's pages read and their dates, and the retired lines |

## What it assumes

- A small operator or small team, not an in-house SEO department - the delegation guidance is
  written for someone handing work to an AI agent, not to a hired specialist.
- A site that is new or content-light today. The cluster-planning advice in particular is written
  for "we have nothing yet," not "we have a large existing blog to restructure."
- That the operator (or the person reviewing this skill's output) can tell a real first-hand fact
  from a generic one - the skill's central check depends on that judgment existing somewhere in the
  loop.

## What is still a stub

- No local-SEO, e-commerce-structured-data, or headless-CMS/SPA-crawlability guidance - out of
  scope for this pass, not silently assumed covered.
- The figures in `2026-search-landscape.md` were read on 22 November 2026, each from its source;
  none should be quoted as current without reading the source again.

## Related plugins

`sower-writer` (drafting, sourcing, editing, and warm coverage; this skill hands finished briefs to
its drafting skill) · `sower-review` (the project-lead skill and the review agents, for deciding
what to build and checking it before and after).

MIT licensed.
