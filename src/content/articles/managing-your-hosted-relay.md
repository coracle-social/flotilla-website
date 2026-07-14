---
title: "Managing Your Hosted Relay in the Coracle Panel"
description: "Day-to-day operation of a hosted space: plans, feature toggles, access policy, and deactivation."
order: 25
category: advanced
---

# Managing Your Hosted Relay in the Coracle Panel

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Once your space is live (see [Hosting Your Space with Coracle](/articles/coracle-hosting)), the Coracle hosting panel is where you run the relay itself: plan, features, access policy, and billing status. That's separate from Flotilla, where members actually chat. Keep the boundary in mind. A few things you might expect in the hosting panel, like approving or banning members, live in Flotilla instead. More on that below.

## The Relay Detail Page

Each relay you host has a detail page showing its current status, plan, connection (WSS) URL, and a live member count. That count is measured against your plan's member cap, so you can see at a glance how close you are to needing an upgrade.

## Changing Your Plan

You can switch plans — Free, Basic, or Growth — at any time from the relay detail page. Upgrades take effect right away. Downgrades come with one restriction: if your current member count exceeds the cap of the plan you're moving to, the change is blocked. When that happens, you have two choices: reduce your member count in Flotilla first, or stay on (or choose) a plan with a higher cap.

## Feature Toggles

Every relay, on any plan, has three toggles: Rooms, the management API, and Push. Two more features are reserved for paid plans: media storage and video calls. On the Free plan, if you want members to share images or use voice and video rooms, you'll need to upgrade to Basic or Growth first.

## Access Policy

Access policy controls who can read from and write to your relay at the network level:

- **Public read** — anyone can read content from the relay, even without being a member.
- **Public write** — anyone can publish to the relay, not just members.
- **Public join** — anyone can join the space without an invite.
- **Strip signatures** — removes signature data before serving events publicly.

Leave these off and your space stays invite-only and closed to outsiders; turn them on and it opens up in stages. If you're deciding how open your space should be, see [Controlling Who Can Join Your Space](/articles/controlling-space-access).

## Deactivating and Reactivating

Deactivating a relay takes it offline and pauses billing. It sounds destructive, but it isn't: your data, settings, and members are all preserved while the relay is off. Reactivating brings the space back exactly as it was. So deactivation is a reasonable option when you need to pause a community for a while rather than delete it outright — just know that members can't connect while it's deactivated.

## An Activity Log, and Room for More Than One Space

The relay detail page keeps an activity log of events like creation, updates, activation, deactivation, and sync — handy when you need to trace when a setting changed. You're also not limited to a single space: you can run more than one hosted relay under the same Coracle account, each with its own plan, features, and access policy.

## Member Moderation Happens in Flotilla, Not Here

The hosting panel does **not** have an interface for approving, banning, or removing members, despite what you might expect. The relay detail page shows a read-only member count, and nothing more. There is no member-management screen in the hosting panel today.

The actual moderation — adding members by pubkey, banning and restoring them, reviewing reports — happens in Flotilla, against the relay itself. See [Managing a Space](/articles/managing-a-space) for that workflow. So if you're hunting for moderation controls in the hosting panel and coming up empty, this is why: you're in the right product for hosting, just the wrong one for that job.

## Where to Go Next

For invoices, payment methods, or what happens if a bill goes unpaid, see [Billing and Payments for Your Hosted Space](/articles/hosting-billing). To point your own domain at your space instead of the default subdomain, see [Using a Custom Domain for Your Hosted Space](/articles/custom-domain).
