---
title: "Using a Custom Domain for Your Hosted Space"
author: "Jon Staab"
pubDate: 2026-07-14
description: "Point your own domain at a Coracle-hosted space, including the exact DNS record and the apex-domain gotcha."
order: 27
category: advanced
---

# Using a Custom Domain for Your Hosted Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Every space hosted with Coracle comes with a subdomain by default, something like `myspace.spaces.coracle.social`. That works fine on its own. But if you'd rather your community lived at your own domain — `chat.mycommunity.com`, say — you can point that domain at your hosted relay instead. You set this up in the Coracle hosting panel, not in Flotilla: it's a property of the relay, not of the chat app.

## Adding the domain

On your relay's detail page in the Coracle panel, find the "Custom Domain" section and click **Update**. (You can also reach it from the relay's action menu, under **Manage custom domain**.) Enter the domain you want to use — it has to be one you actually control, like `relay.example.com` — and click **Save domain**.

Saving doesn't make the domain live right away. First the panel needs to confirm that your domain really points at your relay before it will serve traffic there.

## Creating the DNS record

Once you've saved a domain that isn't verified yet, the Custom Domain section shows a status banner: "Not yet verified — add this DNS record, then verify." Below it is the exact record to create, already filled in with your domain and your relay's canonical subdomain:

```
yourdomain.com CNAME yourspace.spaces.coracle.social
```

Add that record wherever you manage DNS for your domain. There's no guessing involved — the panel always shows the specific subdomain your relay was provisioned with.

## The apex domain problem

CNAME records only work on a subdomain (`relay.example.com`), never on a bare apex or root domain (`example.com`). This is a DNS-wide rule, not a Coracle limitation: the DNS spec won't let a CNAME coexist with the other records — like MX — that usually live at a domain's root.

To use your root domain, you'll need an **ALIAS** or **ANAME** record instead. Most providers that support them (Cloudflare, Route 53, and others) let you create one that behaves like a CNAME but is legal at the apex. If your provider doesn't offer ALIAS or ANAME, or you'd rather not bother, the simpler path is a subdomain like `relay.yourdomain.com` — it's the same CNAME setup described above, and it sidesteps the apex issue entirely.

## Verification isn't instant

Once the DNS record is in place, verification runs in the background. The panel checks periodically to see whether your domain resolves to your relay, and updates the status on its own once it does. You can also click **Verify DNS record** in the banner to trigger a check right away instead of waiting.

Until the banner reads verified, your custom domain isn't serving traffic yet, so don't send anyone there. Your space keeps working normally on its original subdomain the whole time, so there's no risk of an outage while you wait.

If a while has passed and the domain still shows "not yet verified," it's almost always one of two things:

- **DNS hasn't propagated yet.** Depending on your provider and the record's TTL, changes can take anywhere from a few minutes to considerably longer to show up everywhere.
- **The record is wrong.** Check that you created a CNAME (or an ALIAS/ANAME at the apex) pointing at the exact subdomain shown in the panel, with no typos.

## Changing or removing it

To switch to a different domain, open the Custom Domain dialog, enter the new one, and save — verification then starts over for the new domain. To drop a custom domain and fall back to your default subdomain, open the same dialog and click **Remove custom domain**.

## Related reading

For the rest of what you can configure on a hosted relay — plan, feature toggles, access policy — see [Managing Your Hosted Relay in the Coracle Panel](/articles/managing-your-hosted-relay). If you haven't set up hosting yet, start with [Hosting Your Space with Coracle](/articles/coracle-hosting). For questions about invoices or payment, see [Billing and Payments for Your Hosted Space](/articles/hosting-billing).
