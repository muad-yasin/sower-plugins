# sower-game-frontend

Sower Industries' interface practice, extracted from one real project (a Unity mobile
game) and generalized. Four skills covering the whole path from "what should this screen do" to
"why does this prop look wrong", plus the 3D asset and animation pipeline underneath it.

Install from this repository's marketplace, in a Claude Code session (this repository's root README says which version this form needs):

```
/plugin install sower-game-frontend --marketplace muad-yasin/sower-plugins
```

## The four skills, and the order they run in

The ownership boundaries are the point. They are what stops these four from colliding, and each
skill's `description` states its own.

| Skill | Owns | Runs |
|---|---|---|
| **ux-design** | Flow, wireframe, screen states, accessibility, notification tiers, dark-pattern screening, UI copy - **the what and where** | **First.** Anything newly shown to a player. |
| **ui-implementation** | Implementation correctness - layout, data binding, input, navigation, states actually rendering, importing a mockup literally | **Second.** Takes ux-design's flow + wireframe + states list as its input. |
| **visual-craft** | Composition, palette, materials, typography, staging, lighting, asset QA - **does it actually look right** | **Third.** Only once flow and implementation are already correct. |
| **3d-assets** | Building geometry and motion: pipeline choice, authoring loop, budgets, import/rebind, animation | Alongside the others. **It never judges its own output** - visual-craft is its acceptance gate. |

## What it assumes

- **A solo or very small team.** Several rules exist specifically because there is no design team
  to push back, no QA department, and no second pair of eyes. Where a rule is about compensating
  for that, it says so.
- **Mobile-first, portrait, Android as the reference platform.** Where a rule is platform-specific
  (safe areas, target sizes, store requirements) it names the platform and gives the web figure
  alongside.
- **An agent is doing much of the work.** Much of this material is about the ways an agent gets
  interface and 3D work wrong. Some are measured, and the files name each study with its setup:
  low contrast in the output of AI design tools, code that handles only the happy path, imprecise
  geometry in authored 3D, and blindness to motion over time. Others are the source project's
  records, not measurements, such as culture-sensitive number formatting.

## Engine layering

Every skill's `references/` folder carries up to three engine files:

- **`unity.md`: from the source project.** uGUI and TextMeshPro, canvas scaling, layout on first activation,
  prefab builder scripts, safe areas, the navigation stack, ProBuilder, the Blender-to-engine
  rebind, the capture standard.
- **`web.md`: smaller, and dated.** The DOM, CSS and canvas versions of the same questions, plus
  **a Unity or Unreal build embedded in a web page**: canvas sizing, input focus, load and failure
  states, mobile browser memory and autoplay. Mostly documentation; the source project's own
  browser build went out as a public playtest in October 2026.
- **`unreal.md`: not yet verified, and labelled so in every file.** None of these files rests on
  an Unreal project. They hold **open questions only**: the questions the Unity layer answers,
  stated so that they can be answered the first time an Unreal project is built. They hold no
  Unreal guidance inferred from Unity, because it would read exactly like the real thing.

Beside the engine files, each of the four skills carries `references/evidence.md`: where each rule
of the skill comes from, its record or source, graded, with the date it was read. Open it before a
figure or an incident from the skill is quoted.

## What is still a stub

- **All four `unreal.md` files.** Questions, no answers; among them, whether Unreal's text widget
  lets wrapping text overflow its rect, and which colour space its renderer works in.
- **Animation, everywhere.** The clip-to-rig binding *mechanism* is settled and written as
  load-bearing content. **The scope questions are open on purpose** - whether an animation
  subsystem is wanted at all, what animation is for, where clip data lives. `3d-assets` marks them
  OPEN and says not to close one by guessing.
- **`ux-design/references/web.md` and `ui-implementation/references/web.md`** describe an embedded
  game page mostly from documentation; the source project's own browser build went out as a public
  playtest in October 2026. Each says in its last section what rests on that build and what does
  not.
- **The vision-model protocol for judging motion** is explicitly labelled *proposed and
  unvalidated*. The temporal-blindness evidence behind it is measured; the protocol is a synthesis.
- Some verification items in `ui-implementation/references/timing-and-verification.md` §5 are
  marked as *proposals*, not existing practice. Do not write about them as if they were installed.

## House rules baked in

- **A fact read at its source carries the source and the date it was read; an inference says that
  it is one.**
- **Never write authoritative guidance for something we have not done.** Where a line rests on
  inference, it says so in its own sentence.
