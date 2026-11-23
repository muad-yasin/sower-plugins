# How the skills and agents in this repository are written

The standard for any text an agent loads, whether a skill, an agent file or a rules file, is The High Council's `agent-instruction-writing` skill. It is in that project's public repository (https://github.com/muad-yasin/the-high-council-mcp), under `skills/agent-instruction-writing/`. Read it first, and check every file you write here against its closing list, "Mistakes to flag". This file adds only what this repository decides for itself.

## What this repository is

Five Claude Code plugins of Sower Industries' working practice. They are extracted from one real project, a Unity mobile game whose browser build went out as a public playtest in October 2026, and generalized for Unity games, Unreal games, websites, and games embedded in websites. The four plugins of our own grade every rule by its record or its source (below). sower-writer carries copies (below).

## Keep the scar, drop the coordinates

The source project's names go: its game, its systems, its documents, its paths. The lesson underneath stays, stated so that another project can use it.

| Drop | Keep |
|---|---|
| the source project's class, character and screen names | "a system never references another system directly" |
| a bug's register number, a document's section, any path | the bug class itself, named, with its symptom and its tell |
| a project's constant and its value | "one shared helper decides it; no call site chooses, nothing opts out" |
| "run this search across these five files" | "when you write a mechanical guard, list the paraphrases before you write the pattern" |

A concrete case is often what makes a rule land. Keep it as a generic case ("a card list where every row shipped at the wrong corner radius"), never as a reference to a file the reader cannot open. Leave no path, file, class or asset name the reader cannot resolve: it reads as if there were something to look at.

## Every claim carries its grade

- **Seen**: it happened on the source project or in our later work. Its record is named in the skill's `references/evidence.md` by kind and date, never by path. An earlier skill of that project counts as the record of a case it names.
- **D**: documented in a named source, read on a date that the line or its evidence row gives.
- **I**: inferred; the sentence says from what.

A fact that moves, such as a version, a store rule or a threshold, carries the date it was read, or says that it was not checked. Make no claim that a rule improves results, and no frequency or ranking ("the most common", "the only") without a record behind it.

Each skill's `references/evidence.md` holds:
- where every rule comes from;
- the sources read;
- a table of the lines retired, with the reason each went.

## The shape of a skill

```
skills/<skill-name>/
  SKILL.md
  references/
    evidence.md
    <topic>.md      # depth that holds in any engine
    unity.md        # only where the skill has real engine specifics
    web.md
    unreal.md
```

- **SKILL.md:**
  - frontmatter with `name` (kebab-case, the folder's name), `description` and `license: MIT`;
  - a description that says what the skill covers, when to use it, and which neighbouring skill owns what it does not;
  - a body under about 5,000 tokens (bytes divided by 4), which opens with what the skill owns and hands off and closes with `## Mistakes to flag`.
- **References** open with when to read them. Every pointer to one names that condition and what the file holds.
- **Engine layers:** a paragraph that only makes sense in one engine goes into that engine's file, with a pointer from the body.

## The shape of an agent

An agent file (sower-review's `agents/`) has frontmatter with `name`, `description` and `tools`. Its text tells the agent to change nothing, and says that its tool list does not enforce that, since a shell can write. `sower-review/EVIDENCE.md` holds what each of its rules rests on, in the same grades.

## Write nothing we have not done

An `unreal.md` full of confident advice inferred from Unity would read like the real thing and be guesswork. Where a skill has no verified basis for an engine, its file asks instead of telling:

```markdown
# Unreal: not yet verified

Nothing in this file has been confirmed against a real Unreal project. It lists the questions the
Unity layer answers, so that they can be answered here the first time one is built.

## Open questions
- <the equivalent question, stated precisely>
```

The same holds inside any file: an inference says so in its own sentence.

## The writer plugin's skills are copies

sower-writer's five skills are copies of The High Council's public writing skills, at the commit recorded in `sower-writer/SOURCE.json`. Change them at the source, never here. Then:
- copy them with `scripts/copy-writer-skills.py`;
- run `scripts/check-copies.py` with the source's checkout.

The same check compares the four rules the two quality-check agents share, word for word.

## Done, for every change

The commands are the ones Claude Code's documentation gave on 23 November 2026; read it again if one fails.

1. Every SKILL.md parses, its body is under the budget, and it carries `## Mistakes to flag`.
2. **The search for leftovers finds nothing:** the source project's names, private paths, session names and addresses. Keep that list of names outside the repository, since a public file that lists them publishes them.
3. Every claim has its grade, and every moving fact its date.
4. **The plugins validate:** `claude plugin validate .` and `claude plugin validate ./<plugin>` pass, and `python3 scripts/check-copies.py <source checkout>` ends with OK.
5. **Each plugin loads:** `claude --plugin-dir ./<plugin> plugin list --json` shows it as `<plugin>@inline` with no errors.
