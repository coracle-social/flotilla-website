---
title: "Finding Messages and Recent Activity"
author: "Jon Staab"
pubDate: 2026-07-14
description: "Use a space's Recent Activity feed to catch up and the Search Content dialog to find old messages, and understand why search results depend on the space's own relay."
order: 15
category: basics
---

# Finding Messages and Recent Activity

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

A busy [space](/articles/spaces-and-rooms-explained) can outpace you fast — a dozen rooms, a handful of threads, maybe a poll or two, all moving at once. Flotilla gives you two tools for keeping up and digging back through it all: **Recent Activity**, a feed that gathers everything new in one place, and **Search Content**, a dialog for finding something specific you remember seeing.

## Catching up with Recent Activity

Every space has a Recent Activity page, reachable from its sidebar. Instead of making you click into each room and content type one by one, it gathers what's new across all of them into a single scrollable feed: the latest message in each room you haven't seen, plus anything else that's stirred lately — a new thread post or comment, a classified listing, a fundraising goal, a calendar event, a poll. Each item shows where it happened and how recently, so you can decide what's worth opening and what to skip.

Think of it as your space's front door after you've been away for a while. Rather than piecing together what you missed by hopping between rooms, you get one feed, sorted freshest first, covering roughly the last few months.

## Finding something specific with Search Content

Recent Activity is for browsing what's new; when you already have a rough idea of what you're after, search instead. From the Recent Activity page, tap the magnifier icon in the top bar to open the **Search Content** dialog. Type into the "Search this space..." box and Flotilla searches messages and other content across the whole space, grouping matches by how recent they are (last 24 hours, last 7 days, older) so you can spot the one you want quickly.

If you already know which room the message was in, skip the space-wide dialog — open that room and use its own search. It works the same way, just narrowed to that one room's messages.

## The most important thing to understand about search

Search results only include what the space's own relay actually holds and is willing to return. When you search, Flotilla isn't reaching out to some global Nostr index — it queries that one relay, over that one connection, for events matching your term. If the relay doesn't store a message — because it expired, was deleted, or was never on that relay to begin with — search can't find it, no matter how sure you are it existed. And if the relay doesn't support full-text search at all, the box may come back empty even when the content is sitting right there in the relay's normal chat history.

In practice this rarely matters for an active member of a well-run space — messages you've seen recently are almost certainly still on the relay and searchable. But it helps to know when a search comes up empty and you're sure you saw the message: the gap is usually in what the relay stored or supports, not a bug in Flotilla, and not proof the message never existed.

## Related tools

Recent Activity and search cover chat, threads, and the other content types all mixed together, but two other parts of a space have their own dedicated search, separate from this feed:

- The [Library](/articles/featured-content-and-library) — a space's curated collection of pinned links and events — has its own search across just those pinned items.
- The [member directory](/articles/spaces-and-rooms-explained) is searchable too, for finding a specific person rather than a specific message.

Between Recent Activity for browsing and Search Content for looking something up, you should rarely have to scroll a room from the top just to find a message you know is in there somewhere.
