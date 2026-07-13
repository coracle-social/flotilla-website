---
title: "Setting Up Your Profile"
description: "Edit your display name, avatar, bio, and website, add an optional Nostr address (NIP-05), and share your profile QR code so others can find you and start a DM."
order: 9
category: basics
---

# Setting Up Your Profile

Once you're signed in, you can change how you show up to everyone else at any time — your name, picture, bio, and a couple of optional extras. None of this touches your underlying Nostr key; it's just the public information attached to it. Here's where to find it and what each field actually does.

## Where to edit it

Go to **Settings > Profile**. Near the top you'll see how you currently appear, with an edit (pencil) button next to it — tap that to open the profile form. From there you can set:

- **Nickname** — what you'd like people to call you.
- **About You** — a short bio or introduction.
- **Avatar** — your profile picture.
- **Website** — a link to your site, portfolio, or wherever else you want to point people.

All of these are optional, and you can leave any of them blank. Save your changes and they take effect immediately, everywhere you're signed in.

It's worth knowing what "public" means here: your profile is stored the same way your posts are — as a signed piece of Nostr data that any relay you use can hold, which means anyone able to read that relay can see it. See [Is Flotilla Private?](/articles/is-flotilla-private) for the fuller picture of what's public versus what's actually protected.

## Adding a Nostr Address (NIP-05)

The profile form also has a **Nostr Address** field, with a "What is a nostr address?" link next to it if you want the in-app explanation. A Nostr address (also called a NIP-05) is optional and looks like an email address — something like `you@example.com` — but it isn't an email account. It's a human-readable pointer to your public key, hosted on a domain, that makes it easier for people to find and confirm you instead of matching a long string of characters.

Flotilla doesn't issue, host, or verify a Nostr address for you — it's just a field for one you've already set up through an external provider or your own domain. If you don't have one, leave it blank; it's a convenience, not a requirement, and it's entirely separate from your key. See [Nostr Terms Explained](/articles/nostr-terms-explained) for how it fits alongside the other Nostr-specific words you'll run into.

## Sharing your profile

Flotilla shows a small menu wherever it displays someone's profile — a member's card in a space's directory, for instance — with two options: **Profile Info** and **Share**. That menu isn't limited to other people's profiles; it appears on your own profile card too, so you can open it the same way you'd open anyone else's (your own entry in a space's Member Directory is a reliable place to find it).

Tap **Share** and Flotilla shows a QR code along with a copyable link to your profile. Someone can scan the code, copy the link, or, if your device supports it, use a native share button to send it another way — any of those takes them to your profile, where they can see what you've set and start a direct message with you. It's a quick way to hand someone your identity without them having to type out or paste a raw key.

## What this doesn't change

Editing your profile only changes what people see about you — it has no effect on your key or how you log in. Your key is your actual identity; your profile is just data attached to it. See [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) for that distinction, and [Getting Started](/articles/getting-started) if you're still setting up your first profile during sign-up.

Two other things live on the same Settings > Profile screen but are covered elsewhere, since they're a different job from public-profile editing: copying your raw key again is in [Backing Up and Recovering Your Account](/articles/backing-up-and-recovering-your-account), and clearing or deleting your profile entirely is in [Can I Delete My Account or Data?](/articles/deleting-your-account).
