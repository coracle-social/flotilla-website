---
title: "Backing Up and Upgrading Your Self-Hosted Relay"
author: "Jon Staab"
pubDate: 2026-07-14
description: "What to back up on a self-hosted zooid relay, how to do it safely, and how to upgrade without losing data."
order: 31
category: advanced
---

# Backing Up and Upgrading Your Self-Hosted Relay

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

If you followed [Self Hosting a Space](/articles/self-hosting-a-space) to stand up your own zooid relay, keeping it backed up and up to date is now your job. zooid does neither automatically, and mistakes here can genuinely hurt: lose the wrong file and your relay changes identity; copy the wrong file at the wrong moment and you get a corrupt database. This article covers both, specifically for zooid.

## What to back up

Your zooid deployment writes to three volumes, and each needs different handling.

### `config/` — your relay's identity

Every `.toml` file in `config/` holds that relay's `secret` in cleartext. This isn't just a credential — it *is* the relay's Nostr identity. zooid uses it to sign the events it generates (invites, ban lists, member and role mirrors) and to fill in its NIP-11 `self` field. If you lose it, you can't just generate a new one and carry on. To every client and every member, a relay with a different secret is a *different relay*, full stop. Back up `config/` before anything else, and guard the backup as carefully as the live file — it's just as sensitive.

### `data/` — the event database

zooid stores everything in a single WAL-mode SQLite database at `data/db`, shared by every relay you run on that instance. WAL mode means the database is really three files: `db`, `db-shm`, and `db-wal`. Copy `db` on its own while the relay is running and you can end up with an inconsistent, unrestorable backup, because recent writes may still be sitting in the `-wal` file. Always back up all three files together, or checkpoint the database first so everything is flushed into `db` before you copy.

### `media/` — uploaded files

If you've enabled Blossom with the local storage adapter, uploaded media lives on disk under `media/<schema>/<sha256>`. Back this up too. The exception is the S3 adapter, where your media already lives in the bucket and isn't part of your local volumes.

## Backing up safely

The simplest reliable approach is to stop the relay briefly before copying:

```bash
podman compose stop zooid
tar czf zooid-backup-$(date +%F).tar.gz volumes/zooid/config volumes/zooid/data volumes/zooid/media
podman compose start zooid
```

If you'd rather not take the relay offline, and you have the `sqlite3` CLI available, checkpoint the database first so the `-wal` file merges into `db`, then copy all three files (plus `config/` and `media/`) as a unit:

```bash
sqlite3 volumes/zooid/data/db "PRAGMA wal_checkpoint(TRUNCATE);"
tar czf zooid-backup-$(date +%F).tar.gz volumes/zooid/config volumes/zooid/data volumes/zooid/media
```

Either way, store the archive somewhere other than the server itself — a second machine, or encrypted cloud storage — since it contains your relay's secret key.

## Upgrading zooid

Upgrades are refreshingly simple. zooid's schema changes are additive only (new tables use `CREATE TABLE IF NOT EXISTS`), and the released code has no destructive migrations. So there's no migration step to run — pulling a new image and restarting is the whole upgrade:

```bash
podman compose pull zooid
podman compose up -d zooid
```

Take a backup first anyway. "No destructive migrations today" isn't a promise for every future release, and being safe costs you nothing.

## The hot-reload footgun

zooid watches `config/` continuously and reloads a relay the moment its file changes — no restart needed for config edits. The catch: reload tears the relay down *before* rebuilding it from the new file. Save an edit with a typo or invalid TOML and that relay goes absent and unreachable until you fix the file and save again, with no fallback to the last-good config in between. Edit config files in a copy, validate them, and move the finished file into place — don't hand-edit the live file line by line.

## If you need import/export tools

zooid's source includes `bin/import` and `bin/export` for dumping or restoring events as JSONL, but neither ships in the published Docker image — only `bin/zooid` itself is built into the container. If your backup and restore needs go beyond copying the `data/` files directly, you'll need to build zooid from source to get these tools.

Questions about your setup? [Join our space](/articles/community-and-support) and ask.
