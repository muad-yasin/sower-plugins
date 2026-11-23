# sower-review

Review agents and a project-lead skill: scope gating, bug auditing, design critique, and recurring quality checks.

This is Sower Industries' working practice for **deciding what to build, checking it before it is built, and checking it after it is finished**, extracted from one real project and generalized. Little of it depends on an engine: bug-audit's tells for Unity and for JavaScript and TypeScript, and the release reference's gates per store.

Install from this repository's marketplace, in a Claude Code session (this repository's root README says which version this form needs):

```
/plugin install sower-review --marketplace muad-yasin/sower-plugins
```

## What is in here

| | What it does | When to use it |
|---|---|---|
| **`project-lead`** (skill) | Specs before code, ordering by risk, the scope gate as a discipline, the review checkpoint, documentation duty, release readiness | Any planning or multi-step session; before building anything; after anything is reported finished |
| **`scope-gate`** (agent) | Six knockout items, an outside-view estimate, a pre-mortem and an assumptions check, then one verdict: GO, NEEDS-SPEC (narrow or rethink) or KILL-DESCOPE | Before a new milestone; on a new feature idea |
| **`design-review`** (agent) | Three senior roles, an engineer, a product manager and a CEO, each argued in full against a proposal | Monetization and retention mechanics; anything with stakes in user psychology |
| **`bug-audit`** (agent) | Reads code for functional defects and reports only what it can trace to a trigger: at most ten findings, most severe first | On demand; after a large feature lands |
| **`quality-check-quick`** (agent) | A short status check: where the project stands by git and by its own checks, and what went backwards since the last check | At the end of a session |
| **`quality-check-deep`** (agent) | Whether the product is well made: the craft of its code, the numbers its users live with, its interface, visuals and words, and whether it is good to use | When enough has changed to judge |

`scope-gate` and `design-review` answer different questions and may both run on the same proposal: *does this break our rules* against *is this a good idea*.

## The agents change nothing

Each agent's own text tells it to change nothing: no edit, no commit, no change to a branch or a configuration, no install. **Its tool list does not enforce this**, because the shell it carries can write. A plugin's agent cannot carry a permission mode or hooks: Claude Code ignores those fields when it loads an agent from a plugin (its documentation on sub-agents, read 2026-11-23).

To enforce the rule, copy the agent file into your project's `.claude/agents/` or into `~/.claude/agents/`, and give it a permission mode or hooks there. Permission rules in your settings work too, but they apply to the whole session, not to the agent alone (the same page).

An auditor that can fix what it finds has a reason to find things, and a reviewer that implements its own recommendation stops being a gate (I). So **filing an agent's output is the calling session's job.** An audit whose clearances are never written down gets paid for twice.

## What this plugin assumes about your project

It assumes no file names. Where the source project named its own documents, this plugin says "the project's own design docs and working agreements, wherever they live". It works better if the project has:

- a written place for design decisions and standing rules;
- a **narrative destination** for build history, apart from the documents that are read often;
- a bug register or incident log, so that `bug-audit` does not work out again what is already known;
- a reports folder, where the quality checks save `QualityCheck_Quick_YYYY-MM-DD.md` and `QualityCheck_Deep_YYYY-MM-DD.md`.

None of these is required. Without an earlier report, an agent says so and goes on.

## Give the quick check your project's checks

`quality-check-quick` runs a portable core on any project, among them:
- the uncommitted changes, each one read, and a binary reported as not read;
- the documents' sizes against their budgets;
- narrative that crept back into a living document;
- rules meant to live in one file;
- the test counts;
- how long work has sat uncommitted.

It then runs **your project's own check list**: a file the request names, or the section headed "Quality checks" in your project's root instructions file. Keep that list in your project, never in the agent file. An installed plugin sits in a cache directory named after its version, so an edit there is lost at the next update (Claude Code's plugin loading reference, read 2026-11-23).

Good candidates for the list are rules that are kept by memory today and have been broken once already.

## What each rule rests on

**Every rule is graded:**
- Seen: the source project's records, or our own later audit rounds;
- D: an outside source, with the date it was read;
- I: inferred, with the reason.

`EVIDENCE.md` names the record or the source of each rule of the agents, and `skills/project-lead/references/evidence.md` of each rule of the skill.

**Where the evidence is thin, the files say so:**
- bug-audit's Unreal section asks questions instead of listing tells;
- the release reference's Apple block is a reading of Apple's pages, not the experience of a submission;
- console certification is out of scope.

**Read a platform number again before you act on it.** Store requirements change every year, and a stale threshold quoted with confidence is the failure the dates exist to prevent.

## Layout

```
sower-review/
  README.md
  EVIDENCE.md
  skills/project-lead/
    SKILL.md
    references/
      specs-and-ordering.md
      scope-gate-and-estimation.md
      review-checkpoint-and-docs.md
      release-readiness.md
      evidence.md
  agents/
    bug-audit.md
    scope-gate.md
    design-review.md
    quality-check-quick.md
    quality-check-deep.md
```
