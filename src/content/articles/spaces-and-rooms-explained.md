---
title: "Spaces and Rooms Explained"
description: "The mental model behind Flotilla: a Space is a community hosted on a relay, and Rooms are the channels inside it."
order: 10
category: basics
---

# Spaces and Rooms Explained

If you're coming from Discord or Slack, Flotilla will feel familiar fast — but a couple of the underlying concepts work differently, and it's worth understanding them before you dive in. The two you'll run into immediately are **Spaces** and **Rooms**.

## Term Map: Discord/Slack → Flotilla

Here's the quick version:

| Discord / Slack | Flotilla |
|---|---|
| Server | **Space** — a community |
| Channel | **Room** — text or voice |
| Your account / login | Your **Nostr key** (npub) — you own it, Flotilla doesn't issue it. See [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity). |
| DMs | DMs — same idea, kept separate from any Space |
| Roles (permission bundles) | **Roles**, but cosmetic ones: color-coded member labels, not permission bundles. Access is controlled at the Room and relay level instead. See [Managing a Space](/articles/managing-a-space). |
| Voice/video channels | **Voice Rooms** and video calls, if that Space's relay supports them — not every Space has them |
| "Someone runs the server" | Anyone can host a Space: self-host [zooid](/articles/self-hosting-a-space), or use a managed plan like [Coracle Hosting](/articles/coracle-hosting) |

## A Space Is a Community, Flotilla Is the App

A Space is a community — the people, the conversation, the shared stuff you're there for. Flotilla is just the app you use to access it. This distinction matters more on Nostr than on other platforms: a Space isn't running on Flotilla's servers, because Flotilla doesn't have any. It's hosted on a **Nostr relay**, a server that someone — the community's organizer — runs, whether that's a self-hosted [zooid](/articles/self-hosting-a-space) relay or a plan on [Coracle Hosting](/articles/coracle-hosting).

That means the Space and the app are two separate things that happen to work together. If a Space's organizer ever moved their community to a different relay, or you decided to check the same Space from a different Nostr client entirely, the community itself wouldn't change — only your window into it would. See [What is Flotilla?](/articles/what-is-flotilla) for more on why that separation is the whole point.

## Rooms Are the Channels

Inside a Space, conversation happens in **Rooms** — the direct equivalent of Discord channels or Slack channels. A Space can have as many Rooms as its organizer sets up, each with its own name, icon, and purpose: `#general`, `#random`, `#support`, whatever fits the community.

Most Rooms are text chat, but a Space can also offer voice Rooms for live audio (and video calls with screen sharing), if the relay behind it has been configured to support them. You join a Room the way you'd expect — click it in the sidebar and start reading or talking. For the details on posting, reacting, and everything else that happens inside a Room day to day, see [Chatting in a Space](/articles/chatting-in-a-space).

## A Space Is More Than Chat

Rooms cover real-time conversation, but a Space can hold a lot more than that:

- **Threads** — a forum-style board: you start a post, and others reply with comments beneath it, for discussion meant to last longer than a fast-moving chat scroll. Threads can be organized into per-room boards. Who can see and post to them is governed by the Space's access settings, not a separate thread-level permission.
- **Calendar** — scheduled events the community is running.
- **Library** — a curated collection of pinned links and posts worth keeping around (see [Featured Content and the Library](/articles/featured-content-and-library)).
- **Polls** — quick votes on a question.
- **Classifieds** — a marketplace-style listings board.
- **Goals** — fundraising targets members can [zap](/articles/zaps-and-wallet) sats toward.
- **Member directory** — a searchable list of everyone in the Space, including any roles they've been assigned.
- **Recent Activity** — a feed pulling together new activity across the Space's Rooms and other content types, so you can catch up in one place. See [Finding Messages and Recent Activity](/articles/finding-messages-and-recent-activity).

Which of these a given Space actually uses is up to its organizer — some communities lean entirely on chat, others use threads and the calendar heavily. You'll find all of it in the same sidebar navigation as the Space's Rooms.

## Direct Messages Aren't Part of a Space

It's easy to assume DMs are just a private Room, but they're not — direct messages live in their own separate section of Flotilla, outside of any Space. You can message another person whether or not you share a Space with them, and DMs are end-to-end encrypted (NIP-17) rather than visible to a relay operator the way Room messages are. See [Direct Messages](/articles/direct-messages) for how to start one, and [Is Flotilla Private?](/articles/is-flotilla-private) for exactly what that encryption does and doesn't protect against.

## One Identity, Many Spaces

Because your Nostr key is your identity rather than a per-platform account, joining a new Space doesn't mean creating a new profile or a new login. The same key gets you into every Space you're a member of, and switching between them is just a click in the sidebar. Your profile, your key, and your DMs all travel with you regardless of how many Spaces you're part of. Once this clicks, [Joining a Space](/articles/joining-a-space) is the natural next step.
