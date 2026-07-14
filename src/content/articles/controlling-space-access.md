---
title: "Controlling Who Can Join Your Space"
description: "Who can join your space — invite links, adding members by pubkey, and the open-vs-private access policy."
order: 32
category: advanced
---

# Controlling Who Can Join Your Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

A new space starts locked down: until you say otherwise, only people you specifically invite or add can read or post in it. Opening things up, or controlling exactly how people get in, touches all three parts of the Flotilla stack — this article walks through each one from the space owner's side.

## Invite-only by default

When a space's relay has no access policy configured, it is fully closed: nobody but the owner can read or write until they're invited. This is the default whether your space runs on a freshly [self-hosted zooid relay](/articles/self-hosting-a-space) or one provisioned through [Coracle Hosting](/articles/coracle-hosting) — a space never opens itself up by accident. If you're just getting your first members in, this default is exactly what you want: it keeps the space private until you decide otherwise.

## Invite links are reusable, not single-use

The easiest way to bring someone in is an invite link. From a space's main menu, click "Create Invite" to generate a link — and, if your relay supports it, an invite code — that you can copy, share, or present as a QR code. Whoever opens it is walked through login or onboarding and then offered the chance to join your space.

This is the single most important thing to understand about invites: **an invite link or code is reusable, not single-use.** Redeeming it doesn't consume it or invalidate it for anyone else — the same link keeps working for whoever has it, indefinitely, until you revoke it. That makes an invite link function like a shared secret rather than a one-time ticket: anyone who receives it can join, and anyone who receives it can pass it along to someone you never intended to invite. Only share an invite link with people you actually want in your space. If one leaks, treat it as a real access problem and revoke it rather than assuming it "already got used."

If a space is invite-only and you don't have a link, contact the space's moderator directly and ask for an invite — Flotilla's discovery page can point you to a space, but getting in still requires that invite from someone with admin access.

## Adding members directly

Instead of, or alongside, invite links, an admin can add a member directly by their Nostr public key. This lives in the same members panel you use to view your space's membership and manage bans — see [Managing a Space](/articles/managing-a-space) for the full membership and moderation workflow. Adding someone by pubkey is useful when you already know exactly who you want in and don't need them to go through the invite-link flow at all.

## Opening your space up

Making a space fully or partially public — so people don't need an invite at all — isn't something you toggle from inside Flotilla's chat interface. It's an access-policy setting on the relay itself, and where you change it depends on how your space is hosted.

**On Coracle Hosting**, open your relay's page in the hosting dashboard and look at its access policy toggles: **public read** (anyone can read without joining), **public write** (anyone can post without joining), and **public join** (anyone can join without an invite at all). Flip only the ones you actually want — for most communities, public read with everything else off is a reasonable "come see what we're about" middle ground.

**On a self-hosted zooid relay**, the equivalent settings live in the `[policy]` block of your relay's config file: `public_read`, `public_write`, and `public_join`, all of which default to `false`. Turning on `public_join` lets anyone self-join without ever going through an invite — see [Self Hosting a Space](/articles/self-hosting-a-space) for how to edit and reload that config.

Either way, `public_join` is the setting that matters most for this article: it's the difference between "invite-only" and "open to anyone who finds the link."

Note that the hosting dashboard itself doesn't have a members list to approve, reject, or invite people from — it only shows a live member count against your plan's cap. Invites, adding by pubkey, and bans all happen in Flotilla against the relay; the dashboard (or your zooid config) only controls the policy that decides whether an invite is required in the first place.

## Removing someone

Controlling who gets *in* is only half the picture. Getting someone back out after they've already joined is a separate action — a ban, not an un-invite — and it's covered along with reports and room-level permissions in [Managing a Space](/articles/managing-a-space).
