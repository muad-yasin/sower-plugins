# Sower Plugins

Claude Code plugins that bring a second opinion and a working method into your session: agents that review a plan, hunt bugs and check quality, and skills for planning, writing and search content. Two more plugins are for building games.

In the four plugins written here, every rule says what it rests on: something that happened in our own work, a source read on a stated date, or an inference marked as one. The fifth, sower-writer, holds copies of The High Council's public writing skills.

## For any software project

| Plugin | You ask | What answers |
|---|---|---|
| **sower-review** | "Is this plan ready to build?" | `scope-gate`: GO, NEEDS-SPEC or KILL-DESCOPE, with what would change the verdict |
| | "Is this a good idea?" | `design-review`: a senior engineer, a product manager and a CEO on a feature, a price or a piece of copy |
| | "Is this code actually correct?" | `bug-audit`: a bug hunt that reports only what it can trace to a trigger |
| | "Where do we stand?" | `quality-check-quick`: a status check at the end of a session |
| | "Is this actually good?" | `quality-check-deep`: a craft review with quoted specifics |
| | "What do we build next, and is it done?" | `project-lead`: a written spec before code, work ordered by risk, a review checkpoint, release readiness |
| **sower-writer** | a draft, an edit, a check of the facts | five writing skills, from the brief to an independent final read |
| **sower-marketing** | "What should we blog, and why?" | `seo-operator`: what is worth writing on a small site, the brief for it, and the checks before it ships |

The five agents read and report. They are told to change nothing, and sower-review's README says how to enforce that.

## For games

| Plugin | What it covers |
|---|---|
| **sower-game-frontend** | `ux-design`, `ui-implementation`, `visual-craft`, `3d-assets`: from the player's flow to the built screen, whether it looks right, and its 3D assets |
| **sower-game-systems** | `game-systems`: rules, state, saves and their migration, economy and balance math |

Their engine detail is for Unity and for games on the web. For Unreal they hold questions, not answers: no Unreal project stands behind them.

Not building a game? The general versions of these design and engineering skills, `ux-design`, `visual-craft`, `frontend-developer` and `backend-developer` among them, are in [The High Council](https://github.com/muad-yasin/the-high-council-mcp)'s plugin.

## Install

In a Claude Code session, v2.1.275 or later (its install page, read on 23 November 2026):

```
/plugin install sower-review --marketplace muad-yasin/sower-plugins
```

Or add the marketplace once and install from it:

```
claude plugin marketplace add muad-yasin/sower-plugins
claude plugin install sower-review@sower-plugins
```

## Where it comes from

One solo developer's skill files, written and rewritten over months of building a Unity mobile game whose browser build went out as a public playtest in October 2026. The review agents were also run on a command-line tool, a Python tool, a second game and a website project. Nothing here was measured on a project run with and without a rule.

How the files are written, and what binds a contribution: [AUTHORING.md](AUTHORING.md). MIT, held by Sower Industries: [LICENSE](LICENSE).
