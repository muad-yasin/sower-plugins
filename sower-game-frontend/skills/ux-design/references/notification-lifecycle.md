# Notification tiers and the lifecycle of a transient surface

*Open this file before you design a notification, badge, ticker, banner, toast or any surface that appears on its own and is meant to go away again. SKILL.md names the tiers and the rule; this file holds the cases behind them.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **I** = inferred, with the reason in the sentence. Where each line comes from: `evidence.md`, its section on this file.

## The three tiers, cheapest to loudest

- **Badge:** a dot or a count on a persistent element. It never blocks, and the person decides when to look; right for background unlocks such as unread mail. On the source project a badge that stayed on read as a nag, and a one-off pulse on the same element was the honest alternative, at the cost that a pulse can be missed and has no replay (Seen). State that trade-off: it is not a free win.
- **A strip or ticker** that appears when something fires, passes once and hides itself: right for information that is time-sensitive but not critical. Keep it tappable even during an operation it might interrupt, and let the existing navigation resolve the conflict instead of abort code of its own (a screen's disable hook already cancels a run when something is pushed over it). The one exception on the source project: the ticker cannot be reached while a verdict card is on screen, because a tap on it had thrown that card away unread (Seen, fixed September 2026).
- **Full takeover:** for genuine scripted beats only, and even those behind an explicit tap, never a cold pop-up.

Match the tier to how urgent the information is, not to how keen the feature is to announce itself.

## Several triggers on one surface

When independent triggers share one surface, design the gap between them, and who waits for whom, before any of them fires. On the source project scripted and natural headlines landing within seconds of each other drew a playtest complaint (Seen). Its first answer, worth copying in shape (Seen):

- a minimum gap between headlines: 45 seconds at first, then 30 seconds with an interval schedule from 7 August 2026;
- a scripted beat registers pending intent and comes next, guaranteed, while the routine source pauses;
- the beats of a chained story are spread over a window of the next few headlines instead of taking consecutive slots.

Since 20 August 2026 a fill bar on the ticker is the schedule itself: a headline fires each time the bar fills (two minutes of play, less when the player completes deliveries), and the 30 seconds survive only as a floor under scripted beats (Seen).

Before you build the gate (register the intent, poll a may-fire gate, release a count-based pending flag on teardown), open `../../ui-implementation/references/timing-and-verification.md`.

## One recorded exception: a reveal card that waits

The rule: a transient surface owns its exit and does not sit waiting for the user (SKILL.md). The exception on the source project: on the reveal that pays off a whole trade, the auto-close was deleted, not retuned (Seen, August 2026). Its length had been raised twice in two days, from 3 to 4 to 8 seconds, against one complaint, that there was no real time to read the screen; and no single length suits both the player who wants the verdict and the one reading the four-row ledger. What keeps it from being the failure the rule guards against is structural:

- the card has two exits and neither is a timer: a tap anywhere, armed after 0.6 seconds against the reflex re-press of a player who has just been pressing that spot, and the hardware back button;
- nothing is pending behind it: the money settled before it appeared, so waiting costs nothing, once no other surface can dismiss it unread (the ticker could, until September 2026).

Scope: one card, a terminal reveal with nothing running behind it. It is no licence for a toast, a banner or a notification to freeze in place.

## A lock shown as a disabled surface reads as breakage

On the source project a ticker set non-interactive during an operation took on the shared disabled tint, and the playtest flagged it: the strip turned visibly grey during a run, which nobody had meant (Seen). The fix kept it live and let the existing navigation resolve the conflict, with no new abort code. If a surface must be unavailable, say so in words. One recorded exception shows what it takes: a key shown disabled during one short, consented, skippable walkthrough, decided knowing the rule (Seen).
