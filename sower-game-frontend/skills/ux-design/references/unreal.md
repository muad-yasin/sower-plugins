# Unreal: not yet verified

Nothing in this file has been checked against a real Unreal project. It lists the questions the Unity file answers, so that they can be answered here the first time we build in Unreal. Do not carry an inference over from the Unity file: the two engines' interface stacks do not share an architecture.

## Open questions

- **What is the canvas contract?** Unity's is "width fixed at the design reference, height varies by up to 600 units". What does Unreal's interface scaling and anchoring hand a designer: a fixed authoring resolution, a curve-driven scale, or something else, and where does surplus space go by default?
- **Does the vertical-slack failure exist here at all?** In Unity an unrelated flexible height silently takes the surplus. Is there an equivalent silent absorber in Unreal's layout slots, or does its anchoring make it impossible?
- **How is the safe area or display cutout surfaced to a designer?** Is there a container for it, and does it letterbox by default or paint to the edge? On Android an app that targets Android 15 is drawn edge to edge, into the cutout area, whatever the engine (SKILL.md and its evidence), so the question is only what the engine does about it.
- **What is the states deliverable?** In a Unity project that builds its screens by script, the states list is the builder's argument list. What is the equivalent artifact in Unreal: named indices of a widget switcher, states in an animation track, or convention only?
- **Where does the line between Blueprint and C++ fall for interface work,** and does it change what a design handoff should contain? If a designer can wire the flow in Blueprint directly, the handoff may be a prototype instead of a document, which would change this skill's output.
- **How does Unreal's own model for a stack of activatable widgets affect navigation design?** Whether it removes the hide-list class of bug by construction, the way a navigation stack does in our Unity work, is unknown.
- **Is there a real convention for notifications and transient surfaces,** the way there is a toast or ticker convention elsewhere, or is each one bespoke?
- **What does an accessibility pass look like:** is there a way to check contrast and target sizes, or is it all manual?
