# Web: delivering 3D to a browser

*Open this file before you plan 3D content for a browser. It is thin: the source project's browser build went out as a public playtest in October 2026, as a Unity build with its 3D rooms inside it, and it built no glTF pipeline (Seen). The rest is documentation or inference, labelled as such; treat it as a starting map, not a pipeline.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## What carries over from the core skill

The authoring discipline does not depend on the medium (I): blockout before detail, one built and checked before duplicates, a material copied rather than created from the shader, bounds checked rather than transforms, and **no script's own coordinates trusted without a render.** The failure families of `llm-failure-modes.md` are about the authoring step and apply to any target.

## What changes

- **Download size becomes a budget of its own.** An installed app pays for its geometry, textures and runtime once; a page pays for them on every first load, in front of a visitor who can leave (I). Draw calls stay a budget too.
- **glTF, not FBX, is the format to deliver to a browser** (I, from the two descriptions that follow). Khronos describes glTF as a royalty-free specification "for the efficient transmission and loading of 3D scenes and models by engines and applications" (D, the Khronos glTF page, read 2026-11-22); Blender's manual describes FBX as a format for exchanging 3D data between applications (D, Blender 5.3 manual, "FBX (Legacy)", read 2026-11-22). Draco for geometry and KTX2 for textures are the usual compression options (not checked at a source; stated here since September 2026). Both trade decode time on the device for bytes on the wire, and on a low-end phone that trade may not pay: measure it rather than assume it (I).
- **A browser tab has far less memory than an installed app, and iOS Safari is the tight case** (not checked at a source; stated here since September 2026). A scene that fits an installed build can fail to load in a browser.
- **There are two ways to deliver an engine build, and they set different budgets.** A Unity Web build runs on the visitor's device, so the budgets above bind. Unreal's Pixel Streaming runs the application on a server and streams "its rendered frames and audio to browsers and mobile devices over WebRTC" (D, Unreal Engine 5.9 documentation, "Pixel Streaming in Unreal Engine", read 2026-11-22). There the client's budget is a video decode and the asset budget is the server's (I): do not carry a mobile polygon budget into a pixel-streamed project.

## Open questions for a first real web 3D project

- What is the capture standard? The Play Mode RenderTexture recipe of `unity.md` has no direct counterpart; a headless browser at a pinned viewport and device pixel ratio is the obvious candidate, and it has not been tried.
- Does the invisible-geometry class (a layer, not a position) have a web counterpart: a scene-graph layer mask, a render order, a frustum-culling surprise?
- Where does the material recipe live so that it cannot drift: a shared material definition, or a convention?
- What replaces piece-count budgeting per prop, when instancing and merged geometry cost differently than in an engine build?
