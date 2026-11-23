# Release readiness

*Open this file when shipping is in view: the depth behind `SKILL.md` section 6. It covers the practice that does not depend on a platform, then the current gates for Google Play, the Apple App Store, Steam and the web.*

**Grades.** **Seen** = it happened on the source project, with its record named in `evidence.md`. **D** = documented in a named source, read on the date given. **I** = inferred, with the reason in the sentence.

> **Every number here carries the date it was read, or says that it was not checked.** Platforms revise these every year and sometimes in between: **read the page again before you act on one.** A stale threshold quoted with confidence is the failure this file exists to prevent (I).

## The practice, independent of platform

### Code-complete and can-go-live

`SKILL.md` section 6 holds the rule. The steps only a person can do have no code, and so no test (I):

- the store console account, the developer's identity verification, the tax and banking details;
- the store listing: title, description, categories, content and age ratings;
- in-app products created and priced in the console (code that refers to a product the console lacks compiles, and fails at runtime);
- the signing keys or the upload keystore, and where the key's backup lives;
- the ad network's or the analytics' app keys and placement ids;
- a privacy policy at a live, reachable address.

On the source project these were a named block in its task list, checked against the live project configuration (Seen).

### Ship updates as a staged rollout

Start small and step up only while each stage stays stable. On Play a staged rollout sends an update to a percentage of users that you raise over time, and "Staged rollouts can only be used for app updates, not when publishing an app for the first time" (D, Play Console Help, "Release app updates with staged rollouts", read 2026-11-22). A first stage of 5 to 10% is this file's figure since September 2026, not checked at a source. The small first stage is the window in which a bad build can still be stopped (I). Gate each promotion on whatever automated pre-launch signal the platform gives you for free, with the same standing as green tests (I).

### The watch after launch

For the first 48 hours after any rollout step, check the crash and error rates twice a day (I: the source project's earlier skill states it, from research it adopted in July 2026). **Hotfix at once, and pause the rollout, only for** a spike in crashes, corrupted data or saves, failing purchases or a hard block in progression; everything else waits for the next planned release (I). **A hotfix never carries unrelated changes:** its value is a diff small enough to reason about under pressure.

### Beta ends on written criteria, not a feeling

Declare the exit criteria before the beta starts: a crash-free threshold, no known blocker of data, saves or progression, the platform's gates cleared. A criterion that keeps failing is a scoping conversation, and a discovery that breaks no criterion goes to the backlog for after launch (I: the earlier skill's rule). Raise the order of beta and release at natural boundaries, or content sessions default past it: on the source project a whole late-game stage shipped before the beta because no session forced the question, and its log later called the order a pattern of individually reasonable choices made explicit after the fact (Seen).

### Reading beta and store feedback

Store reviews are the loud minority, skewed negative: read them against retention data, never instead of it, and read the shape of a complaint, not its words (I: the source project's player-reception research of August 2026 proposed this frame, and the project adopted it before it had store reviews to read).

In the same frame, weak returns on the first and seventh day with long sessions are read first as a loop that works behind an opening that is too slow. That reading is a guess to test: the two figures say that people leave, not why. Before a change is planned on it, locate the drop: the session, or the step, after which they stop. "Boring" outweighing "greedy" asks for more content, never for more monetization, and any mention of greed or ads calls for an audit of the ads the same day.

## Google Play

- **The target API level** (D, Play Console Help, "Target API level requirements for Google Play apps", read 2026-11-22): since 31 August 2026 new apps and updates must target Android 16 (API level 36) to be submitted; Wear OS and Android Automotive OS apps, Android 15 (API 35); Android TV and Android XR apps, Android 14 (API 34). An extension to 1 November 2026 could be requested. An existing app must target Android 15 to stay available to new users on newer devices.
- **Android vitals' bad-behaviour thresholds** (D, Play Console Help, "Play Console technical quality requirements", and Android's "Android vitals" page, read 2026-11-22): a user-perceived crash rate of 1.09% overall and 8% on any one phone model, and a user-perceived ANR rate of 0.47% overall and 8% on any one phone model, judged on the last 28 days. An ANR is raised when an app has not answered an input event within 5 seconds (D, Android's "ANRs", read 2026-11-22), so input and output on the main thread is a vitals problem, not only one of feel (I). From February 2027 Play adds thresholds for memory use, announced on 26 August 2026 (D, the technical quality page).
- **Ship an Android App Bundle (.aab);** for Unity, IL2CPP and ARM64 (not checked at a source; stated here since September 2026).
- **The closed-testing gate** (D, Play Console Help, "App testing requirements for new personal developer accounts", read 2026-11-23): a personal developer account created after 13 November 2023 must run a closed test with at least 12 testers opted in continuously for at least 14 days before it can apply for production access, and Play can ask for more testing when there were fewer than 12 testers or too little engagement. The page sets this for personal accounts and says nothing of organization accounts.
- **A privacy policy, for every app** (D, Play Console Help, "User Data", read 2026-11-23): a link in its field in Play Console, and a link or the text inside the app. An app that accesses no "personal and sensitive user data" still has to submit one, so this check belongs to the first release, not to the day an ad or purchase SDK ships.
- **The listing's minimum:** an icon, a feature graphic, screenshots of real gameplay, an honest content rating, and Data safety answers that match what the SDKs actually collect (not checked at a source; stated here since September 2026). The UX design skill's store reference, where that plugin is installed, has Play's rule for screenshots, read and dated.

## Apple App Store

Sourced reading, not the experience of a shipped submission.

- **The SDK:** "Starting April 2026", apps uploaded to App Store Connect must be built with the iOS 26 and iPadOS 26 SDK or later, and with the 26 SDKs for tvOS, visionOS and watchOS (D, Apple Developer news of 9 September 2025, read 2026-11-22).
- **App Privacy details:** explaining how the app handles user data is part of submitting it, the answers cover the data that third-party partners collect as well as yours, and you keep them accurate (D, Apple, "App Privacy Details", read 2026-11-22).
- **Account deletion in the app:** an app that supports account creation "must also let people initiate deletion of their account within the app", automatically created guest accounts included (D, App Review guideline 5.1.1(v), read 2026-11-22).
- Review times and the commonest reasons for rejection were not read for this file. Budget at least one round of rejection on a first submission (I).

## Steam

From Valve's Steamworks documentation, read 2026-11-22 (D):

- **The Steam Direct fee** is $100 for each new app, not refundable, and recouped in the payment after the product has at least $1,000 of adjusted gross revenue.
- **Two calendar constraints.** Before your first few titles can release, "A 21-day waiting period between when you paid the app fee and when you can release that game" (the Onboarding page); and for new products, a Coming Soon page that is up "for at least two weeks before releasing" (the Coming Soon page). Effort cannot compress either: schedule them (I).
- **The review:** before a store page or a build goes live, Valve runs the game and checks the store page, which takes between 1 and 5 days.

Valve's pages give no total from creating the account to a launch. The 21 days count from the payment, so pay the fee as early as you can (I).

## Web

There is no gatekeeper, which removes the calendar risk and puts in its place a quality bar nobody enforces and everyone measures (I).

- **Core Web Vitals:** a good experience means a Largest Contentful Paint within the first 2.5 seconds, an Interaction to Next Paint under 200 milliseconds and a Cumulative Layout Shift under 0.1, and good vitals, with the other aspects of page experience, align with what Google's core ranking systems "seek to reward" (D, Google Search Central, "Understanding Core Web Vitals and Google search results", read 2026-11-22).
- **Field data, not lab data:** a perfect local audit says nothing about real devices and networks (I).
- **Accessibility:** WCAG 2.2 has been a W3C Recommendation since 5 October 2023 (D, W3C, "What's New in WCAG 2.2", read 2026-11-22). Check the level the relevant jurisdiction requires before you commit to one in writing.
- **The web's counterparts of the platform checklist:** a real privacy policy and cookie handling that match what the analytics do, a reachable contact route, working metadata and share cards, and a tested 404 and error path (I).

## What this file does not cover

Console certification (Nintendo, PlayStation, Xbox) and any storefront that requires a publisher: out of scope, and nothing here should be extrapolated to them.
