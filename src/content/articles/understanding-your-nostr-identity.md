---
title: "Understanding Your Nostr Identity"
description: "What a Nostr key actually is, why it means you own your identity instead of renting an account, and how to keep it safe."
order: 4
category: basics
---

# Understanding Your Nostr Identity

If you've used [Getting Started](/articles/getting-started) to sign up for Flotilla, you already have a Nostr key. This article explains what that actually means, because it's the single biggest difference between Flotilla and a normal app — and the one thing you can't afford to misunderstand.

## An identity you own, not an account you rent

Every other app you've used probably works the same way: you sign up, the platform creates an account for you, and that account exists at the platform's discretion. If the platform suspends you, deletes your account, or shuts down, your identity — your posts, your follows, your reputation — goes with it. You never really owned it.

Nostr flips this around. Instead of an account, you have a **key pair**: a cryptographic identity that you generate yourself and that no platform controls. Flotilla doesn't issue your identity — it just lets you use one. That's what makes it impossible for Flotilla, or any single space you join, to deplatform you off your own identity. You can always take your key and go somewhere else.

## Public key vs. secret key

Your key pair has two halves, and mixing them up is the most common — and most dangerous — mistake a newcomer makes:

- **npub** is your *public* key. It's your Nostr name — think of it like a username or handle. You can share it freely: put it in a bio, hand it to someone starting a direct message with you, post it anywhere. Other apps and other people use your npub to find you and verify that a message really came from you.
- **nsec** is your *secret* key. It works like a password, except there's no one to reset it for you. Anyone who has your nsec can post as you, read anything you can read, and fully impersonate you. It should never be pasted into a website you don't trust, sent to anyone, or stored in plain text somewhere public. If you're ever asked to "log in" somewhere by pasting your nsec, treat that as a red flag unless you specifically trust the destination.

## One identity, every app

Because your key isn't tied to Flotilla, it isn't tied to any single app. The same npub and nsec work across every Nostr client — Flotilla included. If you already had a Nostr key from another app, you could have logged into Flotilla with it instead of creating a new one. Your profile, your follows, and your content aren't locked inside Flotilla; they travel with your key wherever you go. See [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) for the different ways you can bring an existing key in, or use a signer instead of pasting the raw key at all.

## Keeping your key safe

Because there's no "forgot password" link for a Nostr key, backing it up properly matters more than it would for a normal account. When you create a key in Flotilla, you're given the option to download it as:

- An **encrypted backup (ncryptsec)** protected by a password you choose — the safer option, since the file alone isn't enough to compromise your key.
- A **plaintext nsec** — usable immediately, but sensitive: anyone who gets the file gets your identity.

Either way, store the download somewhere durable and private, like a password manager, rather than leaving it in a downloads folder or sending it to yourself over chat.

## No password reset

This is the tradeoff for owning your identity outright: there's no support team who can reset it for you. If you lose your key — the device it lived on breaks, or you never backed it up — you lose access to that identity for good, along with every space, follow, and message tied to it. If someone else gets your nsec, they can act as you until you notice and move to a new key. Take the backup step seriously the first time, because there usually isn't a second chance.

## An easier on-ramp: email login

If managing a raw key doesn't feel right for you yet, Flotilla also supports signing up with just an email address, via a service called Pomade. Under the hood you still get a Nostr identity, but your key is split across multiple servers for social recovery instead of resting entirely on a file only you hold — a more familiar safety net while you get comfortable with how Nostr keys work. You can read more about the tradeoffs of each login method in [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla).

## Your profile isn't your key

It's worth separating two things that are easy to conflate: your key is your identity, but your profile — display name, bio, avatar, website, and an optional NIP-05 Nostr address that makes your npub easier to read — is just data attached to that identity. You can change your profile freely at any time from Flotilla's settings without affecting your underlying key at all.
