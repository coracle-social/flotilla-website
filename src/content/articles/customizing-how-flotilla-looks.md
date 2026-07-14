---
title: "Customizing How Flotilla Looks and Feels"
description: "Adjust Flotilla's appearance and reading experience: light/dark theme, font size, sensitive-content blur, media/link previews, and the send delay, plus exactly where each setting lives."
order: 17
category: basics
---

# Customizing How Flotilla Looks and Feels

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Flotilla ships with a handful of display and reading-comfort settings that are easy to miss because they're split across two different places: a quick toggle in the settings menu, and a fuller set of controls on the Content settings page. This article walks through both.

## Theme: light or dark

The first time you open Flotilla, it picks light or dark automatically based on your device or browser's own light/dark preference. From there, it's a simple two-way switch — there's no separate "system" option to select. If you want to override it, look for the **Theme** button in the settings menu (next to About and Log Out). Tapping it flips you straight from light to dark or dark to light; run it again and you're back where you started.

Note that this toggle lives in the settings menu itself, not on one of the settings *pages* — you won't find it under Settings → Content or Settings → Privacy.

## Font size

If the default text size is too small or too large for you, go to **Settings → Content** and look under the **Accessibility** section. A slider there lets you scale reading text up or down from the default, so you can make a busy room easier to read without changing anything about your device's own system font size.

## Hiding sensitive content

Authors can flag their own posts as sensitive, and by default Flotilla blurs anything flagged that way until you choose to look at it. This isn't limited to images — it applies to any content the author marked sensitive, whatever form it takes. The control is **Settings → Content → "Hide sensitive content?"**. Turn it off if you'd rather see everything unblurred by default; turn it on (the default) to keep flagged content hidden until you tap to reveal it. For what revealing actually looks like message-by-message as you're reading a room, see [Chatting in a Space](/articles/chatting-in-a-space).

## Media and link previews

Also on the Content page, **"Show media?"** controls whether Flotilla renders link previews and inline images/video at all. Switch it off and messages with links or media show up as plain text instead of expanding into previews and embedded content — useful if you're on a limited connection, want a less cluttered chat view, or just don't want images loading automatically. (There's also a privacy angle to turning this off — loading a preview or a remote image means a request to whatever server is hosting it — but the full reasoning for that lives in [Privacy Settings](/articles/privacy-settings) rather than here.)

## Send delay

Under **Settings → Content → Editor Settings**, you'll find a **Send Delay** slider. It adds a short pause between hitting send and your message actually going out, giving you a brief window to catch a typo, a message sent to the wrong room, or something you change your mind about, and cancel it before it's actually published. It's off (no delay) by default; drag the slider to add anywhere up to a few seconds of buffer. Treat it as a small safety net rather than a scheduling feature — once the delay passes, the message sends normally.

## Where everything lives

To recap, since these settings are split across two different UI locations:

- **Settings menu** (the popup with About/Log Out) — the **Theme** button, a plain light/dark toggle.
- **Settings → Content** — font size (under Accessibility), "Hide sensitive content?", "Show media?", and Send Delay (under Editor Settings).

Two things worth flagging so you don't go looking in the wrong place: none of this lives under **Settings → Privacy** — that page is about relay authentication and telemetry, covered in [Privacy Settings](/articles/privacy-settings). And **Muted Accounts**, while it does sit on the same Content page as the settings above, is a different kind of control — it's about who you hear from, not how things look — so it's covered separately in [Notifications and Muting](/articles/notifications-and-muting).
