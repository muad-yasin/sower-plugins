# Web: the implementation layer, including a game build in a page

*Open this file before you implement a web interface or embed a game build in a page. Our web experience is smaller than our Unity experience: what comes from documentation is dated, and what is ours or an inference is marked. The design side of the same page is in `ux-design`'s `references/web.md`.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## What transfers unchanged from the core skill

These are not engine rules, and they hold in the DOM as written:

- UI is never logic; a component is a deep module with a small surface.
- React to state, and unsubscribe on unmount. A leaked listener is the same bug in another language; in React, an effect that subscribes and returns no cleanup is one shape of it.
- Every state on `ux-design`'s list that the element can reach, empty and error included, and a visible sign on anything that can be tapped.
- Never colour alone, and compute contrast instead of judging it by eye.
- Never format a number with the ambient locale by accident: `Intl.NumberFormat` with an explicit locale is the web form of the shared-formatter rule. Never parse a number back out of a string formatted for display (I: the same trap as `SKILL.md`'s `float.Parse` case).

## What is different

- **Both axes are variable.** There is no design-width canvas, so the contract of `SKILL.md` rule 4 does not transfer as written, but its lesson does: name where the surplus space goes, per breakpoint, instead of letting the first `flex: 1` in the tree take it by accident (I).
- **`100vh` is the large viewport.** MDN: "vh is equivalent to lvh", the unit based on the large viewport, the size with the browser's bars retracted, so a `100vh` layout runs under the bars while they are shown (D, MDN, "<length> CSS type", read 2026-11-22). Use `100svh` for a full height that stays put, and `100dvh` only where you want the layout to change as the bars come and go.
- **Target sizes** are `ux-design`'s figures. Implement its minimum on the hit area, as `SKILL.md` rule 5 says.
- **Layout thrash is the web form of the canvas-rebuild cost.** Reading a layout property such as `offsetHeight` or `getBoundingClientRect()` after a write makes the browser compute the layout at once (not checked at a source; stated here since September 2026). Batch the reads, then the writes.

## A game build in a page

The page and the game are two interfaces that have to agree about focus, size and failure (I).

### Two ways to deliver

- **A Unity Web build** runs on the player's device: no cost per player; load time and the device's power are the price. The source project built for WebGL2, not WebGPU, by a decision of 9 September 2026 (Seen); the reason is in `ux-design`'s web file.
- **Unreal's Pixel Streaming** runs the application on a server and streams its rendered frames and audio to browsers over WebRTC, through a frontend embedded in a web page (D, Epic's documentation for Unreal Engine 5.9, "Pixel Streaming in Unreal Engine", read 2026-11-22). Latency and a GPU cost per session then replace load time, and a state with no free session exists that a downloaded build does not have (I). The source project made no Pixel Streaming build.

### Canvas size (Unity Web)

By default Unity keeps the canvas element's CSS size and its render size in step, and resizes the render target when the page changes the CSS size. Setting `matchWebGLToCanvasSize = false` in the template's `index.html` leaves the render size to you, and `devicePixelRatio = 1` forces low-DPI rendering (D, Unity manual 6000.6, "Configure a Web Canvas size", read 2026-11-22).

On a high-DPI phone a full-window canvas renders more pixels than the player can see the benefit of, at a real cost per frame; pinning `devicePixelRatio` to 1, or to a cap, is a cheap first thing to try for a phone-shaped game (I).

### Keyboard focus

A game in an iframe can get mouse input and no keyboard input until the frame has focus: one report on itch.io's tracker describes exactly that, and focusing the frame fixed it (D, itch.io issue 58, opened in 2014, read 2026-11-22). The fix has three parts (I):

1. give the canvas a `tabIndex` and `focus()` it on click;
2. call `preventDefault()` on the keys the game consumes, or the arrow keys and the space bar scroll the page under the game;
3. **release held keys when focus is lost**, or a player who switches away mid-press comes back to a game that thinks a key is still down. That is the web form of `SKILL.md` rule 5's one idempotent reset.

Inside an iframe, focus lives with the iframe: the parent page must not take it back, and a click-to-play overlay sets it on purpose. The overlay is a state on `ux-design`'s list (I).

### Loading and compression

The source project's first web export, a development build, was about 167 MB uncompressed (Seen, September 2026). Build the loading screen as a real screen with the states `ux-design`'s web file names: real progress wherever the loader reports bytes, a branded first frame, and an unsupported-device state with a next step.

A Brotli build needs a host that sends the matching `Content-Encoding` header (not checked at a source; stated here since September 2026). The source project's build had its decompression fallback off, and itch.io does not send that header, so it chose one uncompressed build for both its own site and itch.io, which compresses files on demand (Seen, 5 October 2026). Find out what your host sends before you pick a compression format (I).

### Mobile browser limits

- **Memory:** iOS Safari allows a page much less WebGL memory than a desktop browser does (not checked at a source; stated here since September 2026, after a practitioner's page whose figures are not kept). Set the build's memory size on purpose, and test on a real iPhone before you promise the game runs there (I).
- **Audio:** a browser blocks audible media from playing on its own until the user has interacted with the site, unless the media is muted or the site is allowlisted, and a blocked `play()` rejects its promise with a `NotAllowedError` (D, MDN, "Autoplay guide for media and Web Audio APIs", read 2026-11-22). Start the audio from the first real interaction, and handle the rejection: a blocked start is an error you can catch, not a silence you have to notice.
- **Safe area:** no safe-area interface does the work inside the canvas; the page's CSS `env(safe-area-inset-*)` covers the page around the game, not the game's own layout (not checked at a source; stated here since September 2026).

## What the source project shipped, and what it did not

Its WebGL2 build went out as a public playtest on itch.io and on its developer's own site in October 2026 (Seen). The rest of this file is documentation and inference, not its incidents: expect to pay for at least one specific that is not listed here, and add it when you do.
