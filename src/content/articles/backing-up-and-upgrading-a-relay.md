---
title: "Backing Up and Upgrading Your Self-Hosted Relay"
description: "What to back up on a self-hosted zooid relay, how to do it safely, and how to upgrade without losing data."
order: 31
category: advanced
---

# Backing Up and Upgrading Your Self-Hosted Relay

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

If you followed [Self Hosting a Space](/articles/self-hosting-a-space) to stand up your own zooid relay, you now own the ongoing job of keeping it backed up and up to date. zooid doesn't do either of these for you automatically, and getting them wrong in the wrong way can genuinely hurt — losing the wrong file changes your relay's identity, and copying the wrong file at the wrong time can hand you a corrupt database. This article covers both, specifically for zooid.

## What to back up

Your zooid deployment writes to three volumes. Each needs different handling.

### `config/` — your relay's identity

Every `.toml` file in `config/` holds that relay's `secret` in cleartext. This isn't just credentials — it *is* the relay's Nostr identity. zooid uses it to sign the events it generates (invites, ban lists, member and role mirrors) and to populate its NIP-11 `self` field. If you lose it, you can't just generate a new one and carry on: to every client and every member, a relay with a different secret is a *different relay*, full stop. Back up `config/` before anything else, and treat the backup with the same care as the live file — it's just as sensitive.

### `data/` — the event database

zooid stores everything in a single WAL-mode SQLite database at `data/db`, shared by every relay you run on that instance. WAL mode means the database is really three files: `db`, `db-shm`, and `db-wal`. Copying `db` by itself while the relay is running can leave you with an inconsistent, unrestorable backup, because recent writes may still be sitting in the `-wal` file. Always back up all three files together, or checkpoint the database first so everything is flushed into `db` before you copy.

### `media/` — uploaded files

If you've enabled Blossom with the local storage adapter, uploaded media lives on disk under `media/<schema>/<sha256>`. Back this up too, unless you've configured the S3 adapter, in which case your media already lives in the bucket and isn't part of your local volumes.

## Backing up safely

The simplest reliable approach is to briefly stop the relay before copying:

```bash
podman compose stop zooid
tar czf zooid-backup-$(date +%F).tar.gz volumes/zooid/config volumes/zooid/data volumes/zooid/media
podman compose start zooid
```

If you'd rather not take the relay offline, and you have the `sqlite3` CLI available, checkpoint the database first so the `-wal` file is merged into `db`, then copy all three files (plus `config/` and `media/`) as a unit:

```bash
sqlite3 volumes/zooid/data/db "PRAGMA wal_checkpoint(TRUNCATE);"
tar czf zooid-backup-$(date +%F).tar.gz volumes/zooid/config volumes/zooid/data volumes/zooid/media
```

Either way, store the archive somewhere other than the same server — a second machine, or encrypted cloud storage, since it contains your relay's secret key.

## Upgrading zooid

Upgrades are refreshingly simple: zooid's schema changes are additive only (new tables are created with `CREATE TABLE IF NOT EXISTS`), and there are no destructive migrations in the released code. That means there's no migration step to run — pulling a new image and restarting is the entire upgrade:

```bash
podman compose pull zooid
podman compose up -d zooid
```

Take a backup first regardless. "No destructive migrations today" isn't a guarantee for every future release, and it costs you nothing to be safe.

## The hot-reload footgun

zooid watches `config/` continuously and reloads a relay the moment its file changes — no restart needed for config edits. The catch: reload tears the relay down *before* rebuilding it from the new file. If you save an edit with a typo or invalid TOML, that relay is left absent and unreachable until you fix the file and save again — there's no fallback to the last-good config in the meantime. Edit config files in a copy, validate them, then move the finished file into place, rather than hand-editing the live file line by line.

## If you need import/export tools

zooid's source includes `bin/import` and `bin/export` for dumping or restoring events as JSONL, but neither ships in the published Docker image — only `bin/zooid` itself is built into the container. If your backup and restore needs go beyond copying the `data/` files directly, you'll need to build zooid from source to get these tools.

Questions about your setup? [Join our space](/articles/community-and-support) and ask.
