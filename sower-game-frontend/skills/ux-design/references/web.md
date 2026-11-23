# Web: design-side specifics, including a game build embedded in a page

*Open this file before you design a web page, whether responsive or holding an embedded game build. Our web experience is smaller than our Unity experience: what comes from documentation is dated, and what is ours or an inference is marked.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = read in the named source on the date given. **I** = inferred, with the reason in the sentence. Where each line comes from: `evidence.md`, its section on this file.

## Responsive design changes what "states" means

The mobile canvas contract (a fixed design width, a variable height) has no web equivalent: **both axes move, continuously.** So the wireframe gains one column: for each region, what happens at a narrow width, and in which order things reflow. Naming the breakpoints is cheaper than discovering them.

- **A full-height layout needs the right viewport unit.** CSS has three viewport sizes: small (the browser's bars shown), large (bars retracted) and dynamic (whichever is current). Size a layout that must fit with the bars showing to the small viewport, `svh`; use the dynamic `dvh` only where you want the layout to change as the bars come and go (MDN, "<length> CSS type", its viewport units, read 22 November 2026, D).
- **Targets:** WCAG 2.2 asks for 24 by 24 CSS pixels, or enough spacing, at level AA (2.5.8), and 44 by 44 at level AAA (2.5.5) (read 22 November 2026, D). On a page used mostly on phones, design to the platform figures of SKILL.md anyway: the AA figure is a conformance level, not a usability target.
- **Hover does not exist on touch.** An affordance carried only by `:hover` is missing for every touch user; this is the web form of SKILL.md's rule that a new interactive element needs a visible sign it can be tapped.

## Designing the page around an embedded game build

This case is worth writing down, because the page is a design problem even when the game inside it is not.

**Two ways to deliver, and they are different design problems.**

- **A Unity Web build** runs the game on the player's device: no cost per player, load time is the price, and a low-end phone is a real way to fail. The source project built its web version on WebGL2, not WebGPU, because in September 2026 WebGPU worked reliably only in Chrome (Seen).
- **Unreal's Pixel Streaming** renders on a server and streams the frames; the page holds a video element and an input channel, inside an iframe or a page of its own (not checked at a source; stated here since September 2026, after Epic's documentation). Latency and a GPU cost per session then replace load time and the device's power, and a "waiting for a free session" state exists that a shipped build does not have (I).

### Canvas size (Unity Web)

By default Unity keeps the canvas's CSS size and its render size in step, and resizes the render target when the page changes the CSS size. `matchWebGLToCanvasSize = false` in the template's `index.html` leaves the render size to you; the `devicePixelRatio` setting overrides the DPI scale, and `devicePixelRatio = 1` forces low-DPI rendering (Unity's manual for 6000.6, "Configure a Web canvas size", read 22 November 2026, D).

**The design decision this forces:** a fixed-aspect frame, letterboxed, or a canvas that fills its container and lets the game's own layout absorb the difference. Pick one at wireframe time. The source project's first web build showed its portrait game in a landscape window, which its own playtest flagged, and its second build brought a page template of its own (Seen). If a "fullscreen" control is the way out, it needs a real state, with an exit, like any transient surface.

### The loading state is a screen, not a spinner

The source project's first web export was about 167 MB before compression (Seen). Design the loading state as a real screen: a progress indicator that shows real progress wherever the loader reports bytes, a first frame with the game's identity so that the wait is branded, not blank, and an honest failure state ("your browser or device could not run this") with a next step.

### Input focus is a designed interaction

A game in an iframe can get mouse input and no keyboard input until the frame has focus: one report on itch.io's tracker describes exactly that (D, itch.io issue 58, opened in 2014, read 2026-11-22). So the page gives the canvas a `tabIndex` and focuses it on click, stops the keys the game uses from scrolling the page, and releases held keys when focus is lost; otherwise a player who switches away mid-press comes back to a game that thinks a key is still down (I). On the design side, say what happens when focus is lost (a pause, an overlay, nothing), and make "click to play" an explicit first state instead of a hidden prerequisite.

### Mobile browser limits that change the design, not only the build

- **Memory:** iOS Safari allows a page much less WebGL memory than a desktop browser does (not checked at a source; stated here since September 2026, after a practitioner's page whose figures are not kept). That limits what the game can hold, so it belongs in the design conversation, not only in the build settings. Test on a real iPhone before you promise it.
- **Sound:** a browser blocks audible media from playing on its own until the user has interacted with the site, unless the media is muted or the site is allowlisted (MDN, "Autoplay guide for media and Web Audio APIs", read 22 November 2026, D). Make the first tap something real, a PLAY button or an interaction on the title screen, instead of pretending the audio will just start.
- **Safe area:** no safe-area interface does the work inside a canvas; the page's CSS `env(safe-area-inset-*)` covers the page around the game, not the game's own layout (not checked at a source; stated here since September 2026).

## What the source project shipped, and what it did not

Its browser build went out as a public playtest in October 2026 (Seen). The rest of this file is documentation and practitioner sourcing, not its scars: trust the shape of the advice, and expect to pay for at least one specific nobody has listed.
