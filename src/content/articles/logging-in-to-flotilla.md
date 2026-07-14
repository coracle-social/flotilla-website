---
title: "Ways to Log In to Flotilla"
author: "Jon Staab"
pubDate: 2026-07-14
description: "Every way to sign in to Flotilla — browser extension, mobile signer, remote bunker, email, or a raw key — and which is safest."
order: 6
category: basics
---

# Ways to Log In to Flotilla

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Flotilla has no username-and-password account. Instead, you prove who you are with a Nostr key (see [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) if you haven't already). But "using your key" isn't a single thing: the login screen offers several ways to bring that key in, and they aren't equally safe. This article walks through each one.

## Brand new to Nostr? Generate a key

No key yet? Click "Register instead" on the login screen to generate one. Flotilla creates the key, stores it in your browser, and lets you download a backup before you finish. It's the simplest first-time path, and it's covered step by step in [Getting Started](/articles/getting-started).

Everything below assumes you already have a key, or you're deciding how to store one going forward.

## Log in with a browser extension (NIP-07)

If you have a Nostr signer extension installed in your browser, Flotilla detects it automatically and shows a "Log in with Extension" button. Your secret key never leaves the extension — Flotilla asks it to sign things, and the extension does the signing itself. On a desktop browser, this is the most convenient safe option.

## Log in with a mobile signer app (NIP-55)

On Android, Flotilla can hand signing off to a separate signer app, such as Amber. If a compatible app is installed, it shows up as its own "Log in with [app name]" button. Like a browser extension, the signer app holds your key and approves each request one at a time — Flotilla itself never sees it.

## Log in with a remote signer / bunker (NIP-46)

"Log in with Remote Signer" connects to a signer running somewhere else — another device, or a hosted signing service — using a Nostr Connect ("bunker") link. There are a few ways to complete the connection:

- Paste a `bunker://` link directly into the field.
- Click "Log in with a QR code instead" to have Flotilla generate a code, then scan it with your signer app on another device.
- On iOS, tap "Open in Signer" to hand off to a signer app installed on the same device via a deep link.

As with an extension or mobile signer, your key stays on the signer's side of the connection the whole time.

## Log in by pasting a key

"Log in with Key" accepts an `nsec`, a raw 64-character hex private key, or a password-protected `ncryptsec` (which prompts for the password before decrypting). It's the most direct option, and Flotilla doesn't hide the downside: the screen warns that pasting a raw key isn't best practice and suggests a signer app instead. Treat it as a last resort, and never paste your key into a site you don't fully trust.

## Log in with email

If email login is enabled, "Log in with Email" gets you in with a familiar email-and-password flow — no key to manage directly. Forgot your password? "Log in with a one-time access code" emails you a fresh code instead. Under the hood you still have a real Nostr identity; it's just backed by social key recovery rather than a file you hold yourself. [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) covers how that recovery model works and what it trades away.

## Which one should you use?

An extension, a mobile signer, or a remote bunker all keep your secret key out of Flotilla entirely — the app only ever sees a signed result, never the key. That makes any of the three meaningfully safer than pasting your key directly into the app. Email login sits in its own category: less cryptographically self-sovereign, but a gentler landing spot if you're not ready to think about keys yet.

Whichever you choose, the identity underneath is the same. Log out and back in with a different method later, and you'll land in the same profile, the same spaces, and the same rooms — the login method is just how you unlock the door, not what's behind it.

## Not the same login as your hosting panel

This article is about signing in to Flotilla, the chat app. If you also pay to host a space, the separate control panel where you manage billing and relay settings — [Coracle Hosting](/articles/coracle-hosting) — has its own login. Signing in to one does not sign you in to the other.
