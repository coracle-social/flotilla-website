---
title: "Using a Custom Domain for Your Hosted Space"
author: "Jon Staab"
pubDate: 2026-07-14
description: "Point your own domain at a hosted space with a CNAME — including the apex-domain gotcha and why verification takes a moment."
order: 27
category: advanced
---

# Using a Custom Domain for Your Hosted Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

A hosted space comes with a default subdomain like `myspace.spaces.coracle.social`, which works fine on its own. If you'd rather your community lived at your own address — `chat.mycommunity.com`, say — you can point that domain at your hosted relay. You set this up on the hosting side, since it's a property of the relay rather than the chat app, but the mechanics that matter are all in DNS.

## The DNS record

After you add your domain in the hosting panel, it won't go live until DNS points at your relay. You create a **CNAME** record with whoever manages your domain:

```
yourdomain.com CNAME yourspace.spaces.coracle.social
```

The panel shows the exact subdomain your relay was provisioned with, so there's no guessing about the target.

## The apex domain problem

CNAME records only work on a subdomain (`relay.example.com`), never on a bare apex or root domain (`example.com`). This is a DNS-wide rule, not a hosting limitation: the spec won't let a CNAME coexist with the other records — like MX — that usually live at a domain's root.

To use a root domain, you'll need an **ALIAS** or **ANAME** record instead. Providers that support them (Cloudflare, Route 53, and others) let you create one that behaves like a CNAME but is legal at the apex. If your provider doesn't offer that, the simpler path is a subdomain like `relay.yourdomain.com` — the same CNAME setup, and it sidesteps the apex issue entirely.

## Verification isn't instant

Once the record is in place, verification runs in the background and flips to verified on its own once your domain resolves to the relay. Until then, your space keeps working normally on its original subdomain, so there's no risk of an outage while you wait.

If it stays unverified for a while, it's almost always one of two things: DNS hasn't propagated yet — depending on your provider and the record's TTL, that can take anywhere from a few minutes to considerably longer — or the record is wrong. Check that it's a CNAME (or an ALIAS/ANAME at the apex) pointing at the exact subdomain shown, with no typos.

For other hosting settings, see [Hosting Your Space with Coracle](/articles/coracle-hosting); for invoices and payment, see [Billing and Payments for Your Hosted Space](/articles/hosting-billing).
