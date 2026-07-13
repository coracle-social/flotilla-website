---
title: "Privacy Settings: Limiting What You Leak"
description: "Walk through Flotilla's privacy controls: relay auto-authentication, error/usage reporting opt-out, your media server choice, and why link previews and remote media can expose your IP."
order: 20
category: basics
---

# Privacy Settings: Limiting What You Leak

[Is Flotilla Private?](/articles/is-flotilla-private) covers what "private" means for your published content and messages. This article is the practical follow-up: the actual controls in Flotilla that limit what you leak to relays and third parties without meaning to.

## Where to find them

Most of these live under **Settings → Privacy**. A couple of related controls that affect the same kind of leakage sit under **Settings → Content** instead, and are noted below.

## Relay auto-authentication

Some relays challenge clients to prove who they are before serving certain content — this is how a relay can tell your key apart from an anonymous reader. Flotilla always does this for the relays already in your own relay lists, since it needs to identify itself there anyway. The question is what happens with relays you haven't added: an unknown relay you happen to read from, for instance, because a link or a space points you at it.

The **"Authenticate with unknown relays?"** toggle controls that. By default it's **Conservative** (off): Flotilla withholds your identity from relays that aren't in your configured lists, so browsing an unfamiliar relay doesn't automatically tell its operator who you are. Turning it on switches to **Aggressive**, where Flotilla authenticates freely with any relay that asks.

The practical case for leaving it Conservative: on a public-read relay, you can read without disclosing your identity to whoever runs it. Turn it on only if you're running into relays that refuse to serve you content until you authenticate, and you're comfortable with those relays knowing your key.

## What loading a preview reveals

Link previews and inline images or video aren't just rendered locally — showing them means Flotilla makes an HTTP request to whatever server is hosting that content. That server, which could be anyone's, sees the request and the IP address it came from. This applies whether it's a preview card for a shared link or a remote image or video embedded in a message.

There's no setting in the Privacy page for this specifically — the control is the **"Show media?"** toggle under **Settings → Content**, which turns off link previews and inline image/video rendering entirely. See [Customizing How Flotilla Looks and Feels](/articles/customizing-how-flotilla-looks) for the full rundown of that toggle and the rest of the display settings. The reasoning here is just why you might want it off: it's the one everyday habit (clicking into chat, scrolling past a shared link) most likely to quietly hand your IP to a server you didn't choose to talk to.

## Choosing your media server

Also under **Settings → Content**, the **"Media Server"** field lists the Blossom-compatible server (or servers) your own uploads go to when you attach a file or image to a message. This is about where content *you* upload ends up, separate from the preview/media-rendering question above — you can add more than one server here if you want redundancy for your uploads.

## Opting out of error and usage reporting

Back on the Privacy page, two more toggles: **"Report errors?"** and **"Report usage?"**. Both let Flotilla send data back to help diagnose problems and understand how the app is used. Neither is required for Flotilla to work, so if you'd rather not send anything, switch them off.

## What's covered elsewhere

Muting a person so their messages stop showing up for you is a content-visibility control, not a leakage one — see [Notifications and Muting](/articles/notifications-and-muting) for how that works. The chat send delay, also under Settings → Content, is about giving you a moment to catch a mistake before it sends rather than limiting what's exposed; it's covered along with the rest of the display settings in Customizing How Flotilla Looks and Feels.

Taken together, these controls won't make Flotilla anonymous — your published content and relay memberships still work the way [Is Flotilla Private?](/articles/is-flotilla-private) describes. What they do is close off the smaller, easier-to-miss leaks: an unknown relay learning your identity because you never changed a default, or a link preview quietly reporting your IP to a server you never meant to contact.
