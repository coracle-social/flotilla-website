---
title: "Backing Up and Recovering Your Account"
description: "How to back up your Nostr key, get back into your account on a new device, copy your key again from settings, and how recovery differs for email (Pomade) accounts."
order: 7
category: basics
---

# Backing Up and Recovering Your Account

Your Nostr key *is* your Flotilla account. [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) explains why that's a feature, not a bug — but it also means there's no "forgot password" link for a self-custodied key, and no support desk that can hand it back to you. This article covers the operational side: backing your key up properly, getting into your account on a new device, finding your key again later, and what recovery looks like if you signed up with email instead.

## Back it up when you sign up

During sign-up, Flotilla offers to download your key as either:

- An **encrypted backup (ncryptsec)**, protected by a password you choose. Prefer this — the file alone isn't enough to compromise your key.
- A **plaintext nsec**, usable immediately but sensitive. Treat it exactly like a password you can never change: anyone who gets it can act as you.

Whichever you pick, save it somewhere durable and private — a password manager, not a downloads folder or a chat message to yourself.

## Getting into your account on a new device

Your key doesn't sync itself between devices the way a browser bookmark might. To sign in somewhere new, you need to either bring your backed-up key with you, or sign in with the extension, mobile signer, or bunker you already use elsewhere — see [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) for how each of those works.

That said, a new device isn't a blank slate. Your spaces, rooms, and messages live on the relays that host them, not on any single device, so they're there the moment you sign in. Flotilla also syncs some read state — like which messages you've already seen — across devices. It's specifically the *key itself* that Flotilla won't hand you automatically; everything built on top of it is waiting for you once you're signed back in.

## Copying your key again from Settings

If you signed up by generating or pasting a raw key, Settings > Profile shows a masked **Private Key** field with a copy button, so you can grab your nsec again without digging up your original backup file. It's copy-only — there's no re-download button there, so paste it straight into a password manager rather than leaving it sitting on your clipboard.

That field only appears if Flotilla actually holds your raw key. If you log in with a browser extension, a mobile signer, a remote bunker, or an email (Pomade) account, your key never touches Flotilla in the first place, so there's nothing to show — those methods keep signing on their own side of the connection.

## If you signed up with email (Pomade)

Email accounts work differently under the hood. Instead of handing Flotilla a key to store, your key is split across several third-party Pomade servers at signup, so no single party (including Flotilla) ever holds the whole thing. That means Settings > Profile doesn't show a Private Key field for an email account at all — instead you'll find:

- **Update your password** — resets the password on your email account.
- **Start holding your own keys** — begins moving from email login to a self-custodied key.

That second option walks you through a recovery flow rather than a straight download: it requests your key pieces be reassembled, sends confirmation codes to your email, and asks you to paste those codes back in to confirm the request before it completes the move to self-custody. It's a "request, then confirm" process by design, so a stolen password alone can't pull your key out.

Email accounts also let you see and manage which devices are signed in. The same Signer Status area on Settings > Profile lists your other active Pomade sessions — when each was created and last active — with the option to end one you don't recognize or no longer use.

## The bottom line

If you self-custody your key, lose the device it lives on, and never made a backup, that identity is gone — permanently, along with every space, follow, and message tied to it. There's no account recovery flow to fall back on the way there is for an email account. Take the backup step seriously the first time you're offered it; for most people there isn't a second chance. If a raw key ever feels like too much responsibility, [Getting Started](/articles/getting-started) and [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) cover the email on-ramp as a gentler alternative.
