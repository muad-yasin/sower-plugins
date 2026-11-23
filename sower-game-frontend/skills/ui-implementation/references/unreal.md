# Unreal: not yet verified

*Open this file before you build an interface in Unreal. Nothing in it has been confirmed against a real Unreal project: it lists the questions the Unity layer answers, so that they are answered here the first time one is built.*

**Do not infer an Unreal answer from the Unity file.** The two interface stacks need not share an architecture, and a plausible-sounding transfer is the failure this file exists to prevent (I).

## Open questions

**Layout and scaling**
- What is the canvas and DPI-scaling contract, and what does a screen get handed across aspect ratios? Is there an equivalent of the vertical-slack failure, a silent destination for surplus space, or does the anchoring model make it unrepresentable?
- Do the text widget's defaults let wrapping text overflow its rect rather than clip, as TextMeshPro's do in Unity? Answer this one first: in Unity the class recurred and failed without an error (`unity.md`, "TextMeshPro").
- How is the safe area or the display cutout surfaced, and does it inset or keep out?

**Architecture and the code boundary**
- **Where does the line between Blueprint and C++ sit for the interface, and what is the review rule?** "UI is never logic" has a clean home in Unity because the interface is C# either way; a Blueprint graph makes it easier to put game rules in a widget, so what enforces the boundary?
- Does Unreal have a stack that owns back and input routing the way a navigation stack does in the Unity file, and does it remove the hide-list bug class by construction?
- Is there an idiomatic reactive binding, or is polling every tick the default that has to be argued against?
- What is the counterpart of the builder script? The Unity screens are built by idempotent editor scripts. Is the equivalent a widget edited by hand, a C++ base class, or something else, and does that change what a design handoff contains?

**Performance**
- What is the counterpart of the Unity cost model, where one change dirties the whole canvas's batch? What costs, and what is the counterpart of a sub-canvas?

**Verification**
- What is the counterpart of driving a real hit test rather than invoking a handler?
- Do edits made during Play In Editor revert the way Unity's Play Mode edits do?
- What automated harness can render a widget at several screen shapes, for the multi-shape capture rule?

**Release**
- What is the packaging checklist's shape, and is there a counterpart of the crash from stripping plus reflection?
