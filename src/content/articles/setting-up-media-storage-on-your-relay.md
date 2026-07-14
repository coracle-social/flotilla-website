---
title: "Setting Up Media Storage on Your Relay (Blossom)"
description: "Turn on Blossom media storage for a self-hosted zooid relay, choose local or S3 storage, and avoid the default that makes uploaded files world-readable."
order: 29
category: advanced
---

# Setting Up Media Storage on Your Relay (Blossom)

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

When someone uploads an image or file in Flotilla, it isn't stored as a regular Nostr event — it's handled by Blossom, a protocol for hosting binary media alongside a relay. On a self-hosted [zooid](/articles/self-hosting-a-space) relay, Blossom is **off by default**. If you followed the self-hosting walkthrough, its sample config already flips `[blossom].enabled = true`; this article explains what that actually turns on, and the choices hiding underneath it.

## Read this before you enable it

The most important thing to know about Blossom on zooid: **uploaded files are publicly readable by default.** The `authenticated_read` setting controls this, and it defaults to `false` — meaning anyone who has (or guesses) a file's URL can download it, whether or not they're a member of your space, and regardless of how private the room it was shared in is. Your room and membership settings don't extend to Blossom on their own. For a space that's meant to be closed or private, this is a genuine leak: locking down who can join and chat doesn't lock down who can fetch a file someone posted.

If your space isn't meant to be fully public, set `authenticated_read = true`.

## Turning it on

Add or edit the `[blossom]` block in your relay's `.toml` config file:

```toml
[blossom]
enabled = true
authenticated_read = true
```

Both keys default to `false`. Setting them explicitly, rather than relying on the defaults, means your config file documents your actual intent instead of leaving it to chance.

## Choosing a backend

Blossom can store files in two places, set with `adapter`:

```toml
[blossom]
adapter = "local"
```

- `"local"` (the default) — files are written to disk, under your relay's media volume.
- `"s3"` — files go to an S3-compatible bucket: AWS S3, MinIO, Cloudflare R2, or Linode Object Storage.

The value has to be spelled exactly `"local"` or `"s3"`, lowercase — it's case-sensitive. Get it wrong and that one relay fails to load; zooid rejects the config at startup rather than falling back to a default. If you're running several spaces from the same server, the others are unaffected — only the mistyped relay goes dark. Check your container logs for a line like `invalid blossom adapter` or `Failed to make instance` if a space stops connecting right after you edit its config; a typo in `adapter` is a likely culprit.

If you choose S3, add a `[blossom.s3]` block:

```toml
[blossom.s3]
region = "us-east-1"
bucket = "my-relay-media"
access_key = "..."
secret_key = "..."
# endpoint = "https://minio.example.com"
# key_prefix = "media/"
```

`region`, `bucket`, `access_key`, and `secret_key` are required. Leave `endpoint` unset for AWS; set it for MinIO, R2, or Linode — doing so also forces path-style bucket addressing, which those providers expect. `key_prefix` is optional, useful if several relays share one bucket. As with your relay's `secret`, these credentials sit in cleartext in the TOML file, so treat the config file itself as sensitive.

One tradeoff worth knowing before you pick S3: it loses HTTP range-request support, since each file is fully read into memory rather than streamed in byte ranges from the bucket. That's invisible for a small image, but it means large files and video lose the ability to seek or resume a partial download the way they can from local disk.

## Fixed limits

A few things aren't configurable, on either backend:

- **10 MiB per file.** There's no setting to raise this — anything larger is rejected outright.
- **Only relay members can upload, list, or delete media**, and it's all-or-nothing: there's no per-room permission. If you're a member at all, you have full Blossom access across the whole relay.

## Backing it up

If you're using the local adapter, uploaded files live in your relay's media volume alongside your other data and need to be backed up the same way — see [Backing Up and Upgrading Your Self-Hosted Relay](/articles/backing-up-and-upgrading-a-relay) for how. If you're using S3, your media already lives in the bucket, so it isn't part of your local backup at all.

## If your space is hosted, not self-hosted

None of the above applies if your space runs on [Coracle Hosting](/articles/coracle-hosting) rather than a relay you manage yourself. There, media storage is one of the relay feature toggles on your space's page in the hosting dashboard — available on the Basic and Growth plans, not on Free — and you don't get to touch `authenticated_read` or choose an S3 backend yourself; Coracle Hosting handles storage behind the toggle. See [Managing Your Hosted Relay](/articles/managing-your-hosted-relay) for where that switch lives.
