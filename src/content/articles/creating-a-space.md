---
title: "Creating a Space"
author: "Jon Staab"
pubDate: 2026-07-14
slug: creating-a-space
source: https://flotilla.social/articles/creating-a-space
description: "Flotilla doesn't host your community — this explains what a space really is and how to get one, hosted or self-run."
order: 23
category: advanced
---

# Creating a Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

One of the things that makes Flotilla special is that we don't host your community. We only provide the software you use to access it.

Instead, your space lives on a server you control — either through a hosting provider or on a server you run yourself. Flotilla spaces are also Nostr relays, so you get the benefits of the whole Nostr app ecosystem for free.

### Hosted Spaces

To get started, decide how you want to host your space. To keep things simple, Flotilla's parent company Coracle offers a hosting service, which you can sign up for [here](https://hosting.coracle.social/).

Several other options exist too. To find them, click "Add a Space", then "Create a Space".

![](/images/YpWKXWBpYZjOTmWOwNg6gtgQlA.png)

We recommend clicking through a few providers so you can decide which one is the right fit for your community.

Once you've chosen a provider, follow their instructions. They may reach out over Nostr direct message, offer a web interface for managing your relay, or work with you personally to set up infrastructure on your own server.

### Self Hosting

If you'd rather manage the server infrastructure yourself, you can go the self-hosting route. There are dozens of Nostr relay implementations out there, but we recommend [Zooid by Coracle](https://github.com/coracle-social/zooid), which was built specifically to work with Flotilla. Another good option is [Pyramid](https://nostrapps.com/pyramid), which offers a dashboard and its own relay policies.

When you're ready to begin, see our [guide](/articles/self-hosting-a-space) for a step-by-step walk through.

Down the road, you may want to move your relay to another server, relay implementation, or domain name. For now that's a fairly manual process, but we're building tools to make it easier.

If you've set up a relay and need a hand, join our [space](https://app.flotilla.social/join?r=meta.spaces.coracle.social&c=LE7S3IA2) and we'll be happy to help.
