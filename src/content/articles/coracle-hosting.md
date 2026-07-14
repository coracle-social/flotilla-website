---
title: "Hosting Your Space with Coracle"
description: "What Coracle Hosting is, how it differs from Flotilla itself, and what each plan includes."
order: 24
category: advanced
---

# Hosting Your Space with Coracle

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

If you're setting up a community, you'll end up in two different places: Flotilla, where your members actually chat, and Coracle Hosting, where you create and pay for the relay that Flotilla connects to. They look and feel completely different on purpose — they're separate products doing separate jobs — and mixing them up is the single easiest way to get confused while setting up a space.

## Two products, not one

Flotilla is a client app. It has no servers of its own and doesn't host anyone's community — it's the software you and your members use to read and post messages. [Spaces and rooms](/articles/spaces-and-rooms-explained) live on a Nostr relay, and that relay has to run somewhere.

Coracle Hosting is that somewhere. It's a separate control panel — a different site entirely — where you provision a relay, configure it, and pay a monthly bill for it. It has no chat, no rooms, and no message feed. Its whole job is relay infrastructure and billing. Once your relay is live, you'll go back to Flotilla (or another Nostr client, like Chachi or Nostrord) to actually run your community day to day — Coracle Hosting isn't where members show up.

In short: Coracle Hosting is where you buy and manage the relay; Flotilla is where you use it. Expect to visit both.

## Signing in

Coracle Hosting doesn't have email/password accounts. You sign in the same way you do everywhere else on Nostr — with your key. You can:

- Log in with a browser extension (NIP-07)
- Log in with a remote signer / bunker (Nostr Connect)
- Import an existing `nsec` or password-protected `ncryptsec` directly

There's no password reset. Whatever key you used to create your hosting account is the only way back in — if you lose it, you lose access to the dashboard that manages your relay, your billing, and your custom domain settings. See [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) if any of that is new to you, and make sure you've backed up that key before you rely on a hosted space.

## Getting a space

Setting up a hosted relay takes a few steps: pick a name and a subdomain (something like `myspace.spaces.coracle.social`), choose a plan, and log in with your Nostr key. Your relay and your hosting account are created together in that flow. If you picked a paid plan, you'll be prompted to set up payment right away.

## Plans

Coracle Hosting offers three self-service plans, priced by member cap and feature set:

| Plan | Price | Members | Media storage & video |
|---|---|---|---|
| Free | $0/mo | 10 | Not included |
| Basic | $5/mo | 100 | Included |
| Growth | $25/mo | Unlimited | Included |

Rooms, the management API, and push notifications are available on every plan, including Free. Media storage and voice/video calls only turn on once you're on Basic or Growth.

There's also a Custom plan for larger communities — a white-labeled app, dedicated support, and custom development. It isn't self-service like the other three; you book a call to work out pricing and scope directly.

## After your relay is live

Once your space is provisioned, the two products split responsibilities cleanly. Coracle Hosting is where you change plans, set your relay's access policy, add a custom domain, and handle billing — see [Managing Your Hosted Relay](/articles/managing-your-hosted-relay), [Billing and Payments](/articles/hosting-billing), and [Using a Custom Domain](/articles/custom-domain) for those. Everything a member actually experiences — joining, chatting, roles, bans, moderation — happens back in Flotilla, not in the hosting panel. If you'd rather run the relay yourself instead of paying for hosting, see [Self Hosting a Space](/articles/self-hosting-a-space).

If you're still deciding whether to host at all versus join an existing community, start with [Creating a Space](/articles/creating-a-space).
