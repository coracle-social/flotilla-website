---
title: "Enabling Voice and Video Calls on Your Relay (LiveKit)"
description: "Operator-side setup for voice rooms and video calls: running LiveKit and wiring it into zooid."
order: 30
category: advanced
---

# Enabling Voice and Video Calls on Your Relay (LiveKit)

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Flotilla supports voice rooms and video calls with screen sharing, but you have to configure the relay before members ever see the option. This article is for relay operators — people [self-hosting zooid](/articles/self-hosting-a-space), and anyone who wants to understand what happens behind a hosted relay's feature toggles. If you just want to use voice and video as a member, see [Spaces and Rooms Explained](/articles/spaces-and-rooms-explained) instead.

## Why you need a LiveKit server

zooid doesn't run its own media server. Audio and video calls are handled by [LiveKit](https://livekit.io/), a separate open-source WebRTC toolkit. zooid simply wires your relay into it — creating rooms, tracking who's in a call, and publishing presence so Flotilla knows a call is live. So before calls work at all, you need a LiveKit server, either a self-hosted instance or a LiveKit Cloud project. From it you'll collect three values to hand to zooid: the server's `server_url`, an `api_key`, and an `api_secret`.

## Add the `[livekit]` block

Add a `[livekit]` section to the relay's TOML config file, alongside its other sections like `[policy]` and `[groups]`:

```toml
[livekit]
server_url = "wss://my-project.livekit.cloud"
api_key = "<key from your LiveKit server>"
api_secret = "<secret from your LiveKit server>"
```

Watch out for one silent failure mode. If `api_key` is left blank, zooid won't refuse to start or log a warning — the call-related endpoints just return 404 to every request. If members report that voice rooms exist but calls never connect, check this block first.

## Point a webhook back at your relay

LiveKit needs to tell your relay when someone joins or leaves a call, so the relay can publish presence and let Flotilla reflect who's actually in a room. On the LiveKit side, configure a webhook pointing at:

```
https://yourrelay.com/.well-known/nip29/livekit/webhook
```

This endpoint is authenticated by LiveKit's own request signature rather than a login, so it must be signed with the exact same `api_key`/`api_secret` pair you put in the relay's config. If they don't match, zooid rejects the webhook and presence silently stops updating.

(If you run several relays that share one LiveKit project, note that LiveKit supports only a single webhook URL. Point it at the management API's shared webhook endpoint instead of any one relay's own URL — but that requires `API_HOST` to be configured. For a single relay, the per-relay URL above is simpler, and it's what most self-hosters should use.)

## Opt a room in

Configuring `[livekit]` makes calling available to the relay, but it doesn't turn every room into a call. Each room that should support calls needs a `livekit` tag in its NIP-29 group metadata. In practice this happens automatically when an admin creates or edits a room in Flotilla and chooses the "Voice" room type. That option only appears in the room-creation form once the relay advertises LiveKit support, so getting the config right on the relay side is what makes the option show up at all. One LiveKit room maps to exactly one room in your space — calls don't span rooms or spaces.

## If your space is hosted, not self-hosted

If your space runs on [Coracle Hosting](/articles/coracle-hosting) rather than a relay you manage yourself, you don't touch any of the above directly. Video calling is one of the relay feature toggles on your relay's page in the hosting panel (see [Managing Your Hosted Relay](/articles/managing-your-hosted-relay)), and it's only available on paid plans — the Basic and Growth plans include it, and the Free plan does not. Coracle runs and configures the LiveKit server for you, so flipping the toggle is the entire setup.

## Verifying it works

Once `[livekit]` is configured and the webhook points at your relay, create or edit a room in Flotilla and confirm that "Voice" appears as a room type. If it doesn't, double-check that `api_key` isn't empty and that the config file reloaded cleanly — zooid hot-reloads config changes, but a typo in the file will leave that relay unreachable until it's fixed. If the room type appears but calls fail to connect once you join, that usually points to a webhook signature mismatch rather than the `[livekit]` block itself.

If you get stuck, [reach out to the community](/articles/community-and-support) for help.
