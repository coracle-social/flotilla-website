---
title: "Billing and Payments for Your Hosted Space"
description: "How billing works for a hosted space — Lightning and card autopay, invoices, the grace period, and what happens if you do not pay."
order: 26
category: advanced
---

# Billing and Payments for Your Hosted Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

If you pay for a hosted relay, billing lives entirely in the Coracle Hosting control panel, not in Flotilla. Flotilla is where your members chat; the hosting dashboard is where you manage and pay for your plan. If you haven't set up a space yet, see [Hosting Your Space with Coracle](/articles/coracle-hosting). For changing plans and other day-to-day admin, see [Managing Your Hosted Relay in the Coracle Panel](/articles/managing-your-hosted-relay).

## How you can pay

Only two payment methods are supported: Bitcoin over the Lightning Network, and credit card through Stripe.

You can set up autopay for either, and you can use both:

- **Lightning**: paste a Nostr Wallet Connect (NWC) URL into the billing page to connect a wallet. New invoices are then paid automatically from it.
- **Card**: from the billing page, click through to a Stripe-hosted portal to add a card. Stripe handles the card details and redirects you back when you're done.

## How an invoice gets collected

When an invoice comes due, it's collected in order of least friction:

1. Your connected Lightning wallet, if you've set one up for autopay
2. Your saved card, if you have one on file
3. A manual pay link

If both automatic methods fail — or you never connected either — you'll get an encrypted direct message from the hosting platform's billing identity, with a link to pay the invoice yourself by Lightning or card.

## Invoices and your billing history

The billing page keeps a full history of your invoices: each one's status — draft, open, paid, or void — its amount, the billing period it covers, and how it was paid. You'll also see a live "draft" invoice, a running total of what you've accrued so far this period before it's finalized into a real invoice. Any invoice, the draft included, can be printed or downloaded as an itemized PDF. Lightning-paid invoices show a Bitcoin-equivalent line alongside the fiat amount.

## Billing cycle and proration

Billing runs in monthly cycles anchored to the date of your first billable activity, not to the calendar month. Within that cycle:

- Creating a paid relay mid-month charges you only for the remaining days in the period, not a full month.
- Changing plans mid-month charges (or credits) the prorated difference between the old and new plan for the rest of the period.
- Deactivating a relay mid-month credits you for the unused remainder.
- At the start of a new period, every relay that was active on a paid plan is charged a full month.

Charges and credits net against each other, so a small credit balance can simply roll forward and offset a future invoice instead of being billed out separately.

## If you don't pay

An open invoice has a **7-day grace period** from the day it's issued. If it's still unpaid when that window closes, the account churns:

- Your active relays are marked **delinquent** and paused — the same practical effect as deactivating them yourself. Your data, settings, and members are all preserved.
- The unpaid invoice is **voided** and the balance **forgiven** — it isn't carried forward as debt you owe later.

Coming back is a clean slate. Reactivating clears the delinquency and restores your relays to active, with no old, voided invoices to settle first. The worst case for a missed payment is a pause you can reverse, not an escalating bill.
