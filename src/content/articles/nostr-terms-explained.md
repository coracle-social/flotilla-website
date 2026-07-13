---
title: "Nostr Terms Explained"
description: "A plain-language glossary of the Nostr words a newcomer meets in Flotilla, with each term deferring in one or two sentences to the article that fully explains it."
order: 5
category: basics
---

# Nostr Terms Explained

Flotilla is built to be usable without knowing anything about Nostr relays or cryptographic keys — but you'll still run into a handful of Nostr-specific words in the app itself, and in the rest of this knowledge base. This page isn't a deep dive into any of them; it's a quick-reference index. Each entry gives you a one- or two-sentence answer, then links out to the article that actually explains it properly.

## Space vs. Room

A **Space** is a community — the people and conversation you're there for. A **Room** is a channel inside a Space, text or voice, the way you'd expect from a Discord or Slack channel. See [Spaces and Rooms Explained](/articles/spaces-and-rooms-explained) for the full mental model, including everything a Space can hold beyond chat.

## Relay

A **relay** is the server that actually stores and serves a Space's messages — think of it as the community's backend. A Space isn't itself a relay; it's a community that's *hosted* on one, whether that relay is self-run using [zooid](/articles/self-hosting-a-space) or a plan on [Coracle Hosting](/articles/coracle-hosting). Flotilla is neither of those — it's just the app you use to reach whichever relay a Space lives on. See [Spaces and Rooms Explained](/articles/spaces-and-rooms-explained) for how the three fit together.

## Key, npub, and nsec

Your **key** is your Nostr identity — not an account any app can suspend or delete. It has two halves: **npub**, your public key, which is safe to share like a username; and **nsec**, your secret key, which you never share with anyone or paste into a site you don't trust. See [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) for what that ownership actually means and how to back your key up safely.

## Signer

A **signer** is anything that holds your key and approves sign-in requests on your behalf, so you never have to paste your raw nsec into Flotilla. It can be a browser extension, a mobile app like Amber, or a remote "bunker" signer running elsewhere. See [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) for every login method Flotilla supports and which ones are safest.

## NIP-05 / Nostr Address

A **Nostr address** (also called a NIP-05) is an optional, human-readable identifier for your key — it looks like an email address, e.g. `you@example.com`, and points back to your npub so people can find and verify you more easily. It's separate from your key itself and isn't required to use Flotilla. See [Setting Up Your Profile](/articles/setting-up-your-profile) for where to add one.

## Zap

A **zap** is a Lightning payment — a tip in sats you can send on a message, thread, event, or fundraising goal instead of (or alongside) a reaction. Zaps are optional everywhere they appear, and they're turned off entirely in the iOS app due to App Store policy. See [Zaps and Your Wallet](/articles/zaps-and-wallet) for how to send one and how to connect a wallet.

---

If a word you've seen in Flotilla isn't listed here, it's probably specific to one feature rather than the protocol itself — check the article for that feature directly, or start from [What is Flotilla?](/articles/what-is-flotilla) for the bigger picture.
