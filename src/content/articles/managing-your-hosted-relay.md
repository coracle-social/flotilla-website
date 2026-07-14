---
title: "Managing Your Hosted Relay in the Coracle Panel"
description: "Day-to-day operation of a hosted space: plans, feature toggles, access policy, and deactivation."
order: 25
category: advanced
---

# Managing Your Hosted Relay in the Coracle Panel

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Once your space is live (see [Hosting Your Space with Coracle](/articles/coracle-hosting)), the Coracle hosting panel is where you operate the relay itself — plan, features, access policy, and billing status. This is separate from Flotilla, which is where members actually chat. Keep that boundary in mind: a few things you might expect to find in the hosting panel, like approving or banning members, live in Flotilla instead. More on that below.

## The Relay Detail Page

Each relay you host has a detail page showing its current status, plan, connection (WSS) URL, and a live member count. That count is measured against your plan's member cap, so you can see at a glance how close you are to needing an upgrade.

## Changing Your Plan

You can change plans — Free, Basic, or Growth — at any time from the relay detail page. Upgrades take effect right away. Downgrades have one important restriction: if your current member count exceeds the limit of the plan you're downgrading to, the change is blocked. If you hit this, you have two options: reduce your member count in Flotilla first, or stay on (or choose) a plan with a higher cap.

## Feature Toggles

Every relay, regardless of plan, has access to three toggles: Rooms, the management API, and Push. Two features are gated to paid plans: media storage and video calls. If you're on the Free plan and want members to share images or use voice/video rooms, you'll need to upgrade to Basic or Growth first.

## Access Policy

Access policy controls who can read from and write to your relay at the network level:

- **Public read** — anyone can read content from the relay, even without being a member.
- **Public write** — anyone can publish to the relay, not just members.
- **Public join** — anyone can join the space without an invite.
- **Strip signatures** — removes signature data before serving events publicly.

Leaving these off keeps your space invite-only and closed to outsiders; turning them on opens it up in stages. If you're deciding how open your space should be, see [Controlling Who Can Join Your Space](/articles/controlling-space-access).

## Deactivating and Reactivating

Deactivating a relay takes it offline and pauses billing. It sounds destructive, but it isn't: all of your data, settings, and members are preserved while the relay is deactivated. Reactivating brings the space back exactly as it was. This makes deactivation a reasonable option if you need to pause a community temporarily rather than commit to deleting it — just know that while deactivated, members won't be able to connect.

## An Activity Log, and Room for More Than One Space

The relay detail page keeps an activity log recording events like creation, updates, activation, deactivation, and sync — useful if you need to trace back when a setting changed. You're also not limited to a single space: you can run more than one hosted relay under the same Coracle account, each with its own plan, features, and access policy.

## Member Moderation Happens in Flotilla, Not Here

The hosting panel does **not** have an interface for approving, banning, or removing members — despite what you might expect. What you'll find on the relay detail page is a read-only member count, nothing more. There is no member-management screen in the hosting panel today.

Actual moderation — adding members by pubkey, banning and restoring them, reviewing reports — happens in Flotilla, against the relay itself. See [Managing a Space](/articles/managing-a-space) for that workflow. If you're looking for moderation controls and can't find them in the hosting panel, this is why: you're in the right product, just the wrong one for that job.

## Where to Go Next

For questions about invoices, payment methods, or what happens if a bill goes unpaid, see [Billing and Payments for Your Hosted Space](/articles/hosting-billing). To point your own domain at your space instead of the default subdomain, see [Using a Custom Domain for Your Hosted Space](/articles/custom-domain).
