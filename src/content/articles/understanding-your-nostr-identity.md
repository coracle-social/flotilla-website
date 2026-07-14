---
title: "Understanding Your Nostr Identity"
author: "Jon Staab"
pubDate: 2026-07-14
description: "What a Nostr key actually is, why it means you own your identity instead of renting an account, and how to keep it safe."
order: 4
category: basics
---

# Understanding Your Nostr Identity

*Part of our guide to [understanding Nostr](/articles/what-is-nostr).*

If you signed up for Flotilla using [Getting Started](/articles/getting-started), you already have a Nostr key. This article explains what that means, because it's the biggest difference between Flotilla and a normal app — and the one thing you can't afford to get wrong.

## An identity you own, not an account you rent

Most apps work the same way: you sign up, the platform creates an account, and that account exists at the platform's discretion. Suspend you, delete the account, or shut down, and your identity — your posts, your follows, your reputation — goes with it. You never really owned it.

Nostr flips this around. Instead of an account, you have a **key pair**: a cryptographic identity you generate yourself, one that no platform controls. Flotilla doesn't issue your identity; it just lets you use one. That's why neither Flotilla nor any space you join can deplatform you off your own identity. You can always take your key and go elsewhere.

## Public key vs. secret key

Your key pair has two halves. Mixing them up is the most common — and most dangerous — mistake a newcomer can make:

- **npub** is your *public* key. It's your Nostr name — think of it as a username or handle. Share it freely: put it in a bio, hand it to someone starting a direct message, post it anywhere. Other people and apps use your npub to find you and to confirm a message really came from you.
- **nsec** is your *secret* key. It works like a password, except no one can reset it for you. Anyone who has your nsec can post as you, read everything you can read, and fully impersonate you. Never paste it into a website you don't trust, send it to anyone, or store it in plain text somewhere public. If you're asked to "log in" somewhere by pasting your nsec, treat that as a red flag unless you specifically trust the destination.

## One identity, every app

Because your key isn't tied to Flotilla, it isn't tied to any app. The same npub and nsec work across every Nostr client, Flotilla included. If you already had a Nostr key from another app, you could have logged into Flotilla with it instead of creating a new one. Your profile, your follows, and your content aren't locked inside Flotilla — they travel with your key wherever you go. See [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) for the different ways to bring an existing key in, or to use a signer instead of pasting the raw key at all.

## Keeping your key safe

There's no "forgot password" link for a Nostr key, so backing it up properly matters more than it would for a normal account. When you create a key in Flotilla, you can download it as:

- An **encrypted backup (ncryptsec)**, protected by a password you choose — the safer option, since the file alone isn't enough to compromise your key.
- A **plaintext nsec** — usable right away, but sensitive: anyone who gets the file gets your identity.

Either way, store the download somewhere durable and private, like a password manager, rather than leaving it in a downloads folder or sending it to yourself over chat.

## No password reset

This is the tradeoff for owning your identity outright: no support team can reset it for you. Lose your key — the device it lived on breaks, or you never backed it up — and you lose that identity for good, along with every space, follow, and message tied to it. If someone else gets your nsec, they can act as you until you notice and switch to a new key. Take the backup step seriously the first time, because there usually isn't a second chance.

## An easier on-ramp: email login

If managing a raw key doesn't feel right yet, Flotilla also lets you sign up with just an email address, through a service called Pomade. Under the hood you still get a Nostr identity, but your key is split across multiple servers for social recovery rather than resting entirely on a file only you hold — a more familiar safety net while you get comfortable with how Nostr keys work. You can read more about the tradeoffs of each login method in [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla).

## Your profile isn't your key

Two things are easy to conflate, so it's worth separating them: your key is your identity, but your profile — display name, bio, avatar, website, and an optional NIP-05 Nostr address that makes your npub easier to read — is just data attached to that identity. You can change your profile freely at any time from Flotilla's settings, without touching your underlying key at all.
