# Web: visual-craft specifics

*Open this file before you judge a web page or the page around an embedded game build. Our web experience is smaller than our Unity experience: what comes from documentation is dated, and what is ours or an inference is marked.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

## What transfers unchanged

Value before colour, one dominant focal read, palette discipline, the consistency rules for an icon set, the contact sheet, colour never alone, the critique ritual and the vision-model protocol do not depend on the medium; nothing in them assumes an engine.

## What is different

- **The browser's colour management is not the engine's.** `hsl()` and `hwb()` work in sRGB, while `oklch()` works in Oklab, whose lightness "is the perceived lightness", unlike the L of `hsl()` (D, MDN, "oklch() CSS function", read 2026-11-22). So a ramp built in `oklch()` keeps even steps where one built in `hsl()` does not, which makes "vary value and saturation within a few hues" directly expressible (I).
- **The engine's alpha correction does not carry over.** The source project's records say that a CSS mockup composites in gamma while the game renders in linear, which is why a mockup's low alpha had to be measured again in the engine (Seen: the records' statement). In the browser a CSS alpha looks like its number, so do not carry the engine's correction to a page (I).
- **`devicePixelRatio` is the density story.** It is the ratio of physical pixels to CSS pixels: how many of the screen's pixels draw one CSS pixel (D, MDN, "Window: devicePixelRatio property", read 2026-11-22). At a ratio of 3 a 1 px CSS line is three device pixels wide, and a line meant to be one device pixel is a third of a CSS pixel, which can vanish or shimmer (I). Check line art at ratios of 1, 2 and 3: the web form of checking legibility at the real render size.
- **Font rendering differs per platform and cannot be normalised away.** Where text sits in its box depends on the font's vertical metrics; a font carries several sets of them, and each browser or program picks which to rely on (D, type.today, "Vertical metrics", read 2026-11-22). So a pixel diff between a browser mockup and an engine render has a floor on text-heavy regions: expect a nonzero mismatch there, and judge it by eye (I).
- **Prefer a real capture tool to a screenshot of your own window.** A headless browser at a pinned viewport and pixel ratio is reproducible; a manual screenshot carries the browser's chrome, the system's scaling and any scrollbar an extension injected (I).
- **Dark mode is a second full palette,** not a filter. Where both exist the contact sheet doubles: every set is checked in both, together, or one of them drifts (I).

## Judging the page around an embedded game build

Two visual layers with different owners, judged separately:

- **The page frame:** the loading state, the letterbox bars, the fullscreen control, the failure state. This is ordinary web visual craft, and the rules above apply.
- **The game canvas,** judged by the engine's standards at the size it actually renders in the page, which is often smaller than the design canvas: an interface authored for a phone canvas 1080 units wide and shown in an embed 480 px wide is judged at less than half its intended size (I).

Do not let the letterbox colour default to black without a decision: it is a large field of colour on the page, and it belongs either to the game's world or to the site's (I).

## What the source project shipped, and what it did not

Its browser build went out as a public playtest in October 2026 (Seen); no visual-QA pass of that page is on record. The colour-management and pixel-ratio items are documentation and inference, not its incidents.
