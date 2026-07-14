---
title: "Billing and Payments for Your Hosted Space"
author: "Jon Staab"
pubDate: 2026-07-14
description: "How billing works for a paid hosted space — how you pay, the grace period, and proration — at a glance."
order: 26
category: advanced
---

# Billing and Payments for Your Hosted Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

If you pay for a hosted relay, billing lives on the hosting side, not in Flotilla. The details below apply to Coracle Hosting; the panel has its own documentation, but here's what's worth knowing before you rely on a paid space. If you haven't set one up yet, start with [Hosting Your Space with Coracle](/articles/coracle-hosting).

## How you pay

Two payment methods are supported, and you can use either or both with autopay:

- **Lightning** — connect a wallet with a Nostr Wallet Connect (NWC) URL, and new invoices are paid automatically from it.
- **Card** — add a card through Stripe, which handles the card details.

When an invoice comes due, it's collected in order of least friction: your Lightning wallet first, then a saved card, then a manual pay link — sent to you as an encrypted direct message if both automatic methods are missing or fail.

## Billing cycle and proration

Billing runs in monthly cycles anchored to your first billable activity, not the calendar month. Within a cycle, charges are prorated: creating a paid relay mid-month only charges for the remaining days, changing plans charges or credits the difference, and deactivating a relay credits the unused remainder. Credits net against charges, so a small balance can simply roll forward to offset a future invoice.

## If you don't pay

An open invoice has a **7-day grace period**. If it's still unpaid when that window closes, your relays are paused — the same effect as deactivating them yourself, with your data, settings, and members all preserved — and the unpaid invoice is voided and forgiven rather than carried forward as debt. Reactivating later is a clean slate, with no old invoices to settle first. The worst case for a missed payment is a pause you can reverse, not an escalating bill.
