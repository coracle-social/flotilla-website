---
title: "Using a Custom Domain for Your Hosted Space"
description: "Point your own domain at a Coracle-hosted space, including the exact DNS record and the apex-domain gotcha."
order: 27
category: advanced
---

# Using a Custom Domain for Your Hosted Space

Every space hosted with Coracle gets a subdomain by default, something like `myspace.spaces.coracle.social`. That works fine on its own, but if you'd rather your community live at your own domain — `chat.mycommunity.com`, say — you can point that domain at your hosted relay instead. This is set up in the Coracle hosting panel, not in Flotilla; it's a property of the relay, not of anything in the chat app itself.

## Adding the domain

From your relay's detail page in the Coracle panel, find the "Custom Domain" section and click **Update** (you can also get there from the relay's action menu via **Manage custom domain**). Enter the domain you want to use — it needs to be a domain you actually control, like `relay.example.com` — and click **Save domain**.

Saving it doesn't make it live right away. The panel now needs to confirm that your domain actually points at your relay before it will serve traffic there.

## Creating the DNS record

Once you've saved a domain that isn't verified yet, the Custom Domain section shows a status banner: "Not yet verified — add this DNS record, then verify." Underneath it is the exact record to create, filled in with your domain and your relay's canonical subdomain:

```
yourdomain.com CNAME yourspace.spaces.coracle.social
```

Add that record with whoever manages DNS for your domain. You don't have to guess the target — the panel always shows the specific subdomain your relay was provisioned with.

## The apex domain problem

CNAME records can only be used on a subdomain (`relay.example.com`), not on a bare apex/root domain (`example.com`). That's a DNS-wide rule, not a Coracle limitation — the DNS spec doesn't allow a CNAME to coexist with the other records (like MX) that typically live at the root of a domain.

If you want to use your root domain, you'll need an **ALIAS** or **ANAME** record instead — most DNS providers that support them (Cloudflare, Route 53, and others) let you create one that behaves like a CNAME but is legal at the apex. If your provider doesn't support ALIAS/ANAME, or you'd rather not deal with it, the simpler path is to just use a subdomain like `relay.yourdomain.com` — it's the same CNAME setup described above and avoids the apex issue entirely.

## Verification isn't instant

After the DNS record is in place, verification happens in the background — the panel checks periodically to see whether your domain resolves to your relay, and updates the status automatically once it does. You can also click **Verify DNS record** in the banner to trigger a check right away rather than waiting.

Until the banner shows verified, your custom domain is not yet serving traffic — don't point anyone at it yet. Your space keeps working normally on its original subdomain the entire time, so there's no risk of an outage while you wait.

If it's been a while and the domain still shows "not yet verified," it's almost always one of two things:

- **DNS hasn't propagated yet.** Depending on your provider and the record's TTL, changes can take anywhere from a few minutes to a while longer to become visible everywhere.
- **The record is wrong.** Double-check you created a CNAME (or ALIAS/ANAME at the apex) pointing at the exact subdomain shown in the panel, with no typos.

## Changing or removing it

To switch to a different domain, open the Custom Domain dialog, enter the new one, and save — verification starts over for the new domain. To drop a custom domain entirely and fall back to your default subdomain, open the same dialog and click **Remove custom domain**.

## Related reading

For the rest of what you can configure on a hosted relay — plan, feature toggles, access policy — see [Managing Your Hosted Relay in the Coracle Panel](/articles/managing-your-hosted-relay). If you haven't set up hosting yet, start with [Hosting Your Space with Coracle](/articles/coracle-hosting). For questions about invoices or payment, see [Billing and Payments for Your Hosted Space](/articles/hosting-billing).
