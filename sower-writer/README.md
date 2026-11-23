# sower-writer

Writing, from brief to publish, in five skills.

Install from this repository's marketplace, in a Claude Code session (this repository's root README says which version this form needs):

```
/plugin install sower-writer --marketplace muad-yasin/sower-plugins
```

On anything drawn from real events, the facts come first:

```
fact-checking  ->  drafting  ->  line-editing  ->  final-read  ->  the person who signs off
```

`good-news-writing` is the warm register the four hand off to, for positive coverage of a real
subject; the same sourcing and final read apply to it.

- **`drafting`** - copywriting and drafting from scratch. The brief, the one true sentence a piece
  exists to say, register selection, structure, the closer. Owns getting to a first complete draft.
- **`fact-checking`** - the claim-by-claim audit of a piece of writing, the rules on quotes and real
  names, the fact line, and the legal risk check.
- **`line-editing`** - manual line editing, and removing the tells of AI-written prose. Rejects
  drafts; never prescribes one.
- **`final-read`** - the independent adversarial pass before anyone else sees the work. An armed
  fact-check that re-searches every load-bearing claim, then a reading panel. Verdicts only, never
  edits.
- **`good-news-writing`** - warm, positive coverage of a real person, company or organisation doing
  something good, without press-release tone, invented villains or backhanded praise. The sourcing
  of `fact-checking` and the `final-read` pass apply to it unchanged.

## Where these skills come from, and the skills they name

The five are copies of the writing skills in The High Council's public repository, at the commit
recorded in `SOURCE.json`. This repository's `scripts/copy-writer-skills.py` makes the copy. Its
`scripts/check-copies.py` compares the copies with their record and, given a checkout of the source,
with the source; without one, it reports that comparison as not checked. Change them at the source,
never here.

They name six skills this plugin does not carry: `research-and-sourcing`,
`verification-and-critique`, `tool-and-action-discipline`, `task-scoping`, `frontend-developer`
and `backend-developer`. Those are in the same repository's `skills/` folder. Copy the folders you
want into your project's `.claude/skills/` or into `~/.claude/skills/`, or add that repository as
a plugin:

```bash
claude plugin marketplace add muad-yasin/the-high-council-mcp
claude plugin install the-high-council@the-high-council
```

The `ux-design` skill they name is in this repository's `sower-game-frontend` plugin.

## What this is built from

Their cases come from the work their own files describe: a long-running content project of several
hundred short pieces, and text shipped inside an app. They are written for any kind of text:
marketing copy, store listings, documentation, dialogue, web copy.

## What it assumes

- **A human signs off before anything publishes.** Every skill here is built to make that sign-off
  faster and better aimed. None of them replaces it.
- **You can search the web while writing.** `fact-checking` and `final-read` are both built around
  re-searching claims rather than trusting recall. Without search, the first pass of `final-read` cannot do
  its one job: re-searching every load-bearing claim.
- **The writer and the reviewer may be the same session.** `final-read` runs by default in the
  session that wrote the piece. That holds for its first pass, which re-searches every load-bearing
  claim. Its second pass degrades when self-run: the skill marks it as self-run and runs a lineup
  against real pieces, and a piece that matters unusually gets a fresh context.

## Legal content: read this

`fact-checking/references/legal-guardrail.md` states legal principles and cites real cases and
statutes, from two frameworks that disagree in places: Germany with the EU, and the United States.
**It is general information to help you spot risk early. It is not legal advice, and it is not a
substitute for a lawyer.** Its statutes and court decisions were checked against their primary text
in September and October 2026, and the items that rest on secondary reports say so.

Anything commercial that satirises identifiable real people or companies should get a media and IP
lawyer's review before launch.

## What is still a stub

- **Nothing here is engine-specific.** There are no `unity.md` / `web.md` / `unreal.md` reference
  files, because writing craft has no engine layer and inventing one would be padding. The one place
  a delivery medium genuinely changes the writing - character ceilings, narrow columns, text a
  player meets once and cannot re-read - is `drafting/references/in-product-copy.md`, which is
  written from shipping text inside an app, and says plainly where it stops.
- **Store-listing and app-store metadata rules are not covered.** Character limits and review
  policies change per store and per year; a stale copy of them here would be worse than none.
- **Localization is not covered.** No verified experience to draw on.
