---
title: "Billing and Payments for Your Hosted Space"
description: "How billing works for a hosted space — Lightning and card autopay, invoices, the grace period, and what happens if you do not pay."
order: 26
category: advanced
---

# Billing and Payments for Your Hosted Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

If you're paying for a hosted relay, billing lives entirely in the Coracle Hosting control panel — not in Flotilla. Flotilla is where your members chat; the hosting dashboard is where you manage your plan and pay for it. See [Hosting Your Space with Coracle](/articles/coracle-hosting) if you haven't set up a space yet, or [Managing Your Hosted Relay in the Coracle Panel](/articles/managing-your-hosted-relay) for changing plans and other day-to-day admin.

## How you can pay

Only two payment rails are supported: Bitcoin over the Lightning Network, and credit card through Stripe. Nothing else.

You can set up autopay for either, and you're not limited to just one:

- **Lightning**: connect a wallet by pasting a Nostr Wallet Connect (NWC) URL into the billing page. New invoices are then paid automatically from that wallet.
- **Card**: click through to a Stripe-hosted billing portal from the billing page to add a card. Stripe handles the card details; the portal redirects you back when you're done.

## How an invoice gets collected

When an invoice comes due, it's collected in order of least friction:

1. Your connected Lightning wallet, if you've set one up for autopay
2. Your saved card, if you have one on file
3. A manual pay link

If both automatic methods fail — or you never connected either one — you'll receive an encrypted direct message from the hosting platform's billing identity with a link to pay the invoice yourself, by Lightning or card. That DM is the most common reason you'd suddenly be asked to pay by hand: it usually means autopay wasn't configured, or the method on file didn't go through. If a payment fails, the platform keeps retrying automatically rather than giving up — a failed method just gets flagged so you know something needs attention, and the flag clears itself the next time that method succeeds.

## Invoices and your billing history

The billing page keeps a full history of invoices with their status — draft, open, paid, or void — the amount, the billing period covered, and how it was paid. You'll also see a live "draft" invoice: a running total of charges accrued so far in the current period, before it's finalized into a real invoice. Any invoice, including the draft, can be printed or downloaded as an itemized PDF; Lightning-paid invoices include a Bitcoin-equivalent line alongside the fiat amount.

Exact plan prices are described in [Hosting Your Space with Coracle](/articles/coracle-hosting) as of this writing — treat the amount on your actual invoice as authoritative rather than assuming it always matches the listed plan price exactly.

## Billing cycle and proration

Billing runs in monthly cycles anchored to the date of your first billable activity, not the calendar month. Within that cycle:

- Creating a paid relay mid-month charges you only for the remaining days in that period, not a full month.
- Changing plans mid-month charges (or credits) the prorated difference between the old and new plan for the rest of the period.
- Deactivating a relay mid-month credits you for the unused remainder.
- At the start of a new period, every relay that was active on a paid plan is charged a full month.

Charges and credits net against each other, so a small credit balance can simply roll forward and offset a future invoice instead of being billed out separately.

## If you don't pay

An open invoice has a **7-day grace period** from when it's issued. If it's still unpaid once that window passes, the account churns:

- Your active relays are marked **delinquent** and paused — the same practical effect as deactivating them yourself. Your data, settings, and members are preserved throughout.
- The unpaid invoice is **voided** and the balance **forgiven** — it is not carried forward as debt you owe later.

Coming back is a clean slate: reactivating clears the delinquency and restores your relays to active without requiring you to settle any old, voided invoices. In other words, the worst case for a missed payment is a pause you can reverse, not an escalating bill.
