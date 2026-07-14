---
title: "Notifications and Muting"
description: "Control what pings you: per-room and per-space notifications, alert types, and muting accounts or rooms."
order: 16
category: basics
---

# Notifications and Muting

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

By default, Flotilla notifies you about activity in every [space](/articles/spaces-and-rooms-explained) and room you belong to. That's fine for a quiet space, but once you're in a handful of active communities it's worth tuning things down to just what you care about. Flotilla gives you three separate levers: which rooms and spaces can ping you, which kinds of activity count as a notification, and who you'd rather not hear from at all.

## Per-room and per-space notifications

Every space has a header menu — tap the space name at the top of its room list — with a "Turn on/off notifications" option that flips alerts for the whole space at once. If a space is off, you can still cherry-pick a room or two to keep notifying you; if a space is on, you can turn off the one noisy room that's drowning everything else out. Either way, the rest of the space keeps whatever setting it already had.

For a single room, open it and click the info icon at the top of the screen to bring up its details. Under "Room Settings" you'll find a **Notifications** toggle for that room specifically — this is the same per-room control [joining a space](/articles/joining-a-space) points you to right after you first join.

This preference isn't just stored on your phone: it's saved as an encrypted event published to your own relays, tied to your [Nostr identity](/articles/understanding-your-nostr-identity). Log into Flotilla on another device with the same key, and your per-space and per-room notification choices come with you.

## Choosing what counts as a notification

Head to **Settings → Alerts** for the broader controls. Here you can turn on:

- A **badge** showing your unread count on the app icon
- A **notification sound** for new activity (this option only appears in the web app — the native Android and iOS apps use your phone's own sound settings)
- **Push notifications**, delivered to your device even when Flotilla isn't open

Below that, "Alert Types" lets you choose *what* triggers a notification: general activity in a space, being directly mentioned, or new [direct messages](/articles/direct-messages). These alert settings are stored on the device you configure them on, so if you use Flotilla on both your phone and a laptop, you'll want to check them in both places.

## Favoriting a room

That same room info panel has a **Favorite** toggle next to the notification one. Favoriting a room bookmarks it so it stays prominent near the top of your room list instead of getting buried under everything else in the space — handy for the couple of rooms you actually check every day.

## Muting accounts

If the problem is a specific person rather than a specific room, go to **Settings → Content** and add them under **Muted Accounts**. Once someone is muted, their messages collapse wherever you'd otherwise see them — replaced with a note that you've muted this person and a "Show anyway" link if you change your mind for a particular message. Muting doesn't remove you from a room or a space, and it doesn't notify the other person; it just keeps their content out of your way.

If it's a room rather than a person that's too noisy, you don't need to mute anything — just turn off that room's notifications from its info panel as described above, or leave its member list from the room menu if you want out entirely.

## Where these controls live

To recap:

- **Room info panel** (info icon inside a room) — per-room notifications, favoriting
- **Space menu** (tap the space name) — notifications for the whole space
- **Settings → Alerts** — badges, sound, push, and which activity types notify you
- **Settings → Content** — muted accounts

Between these, you can dial a busy space down to just the mentions and rooms you care about, or keep everything on and simply mute the people you'd rather not hear from.
