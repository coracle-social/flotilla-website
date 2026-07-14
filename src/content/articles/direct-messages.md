---
title: "Direct Messages"
author: "Jon Staab"
pubDate: 2026-07-14
description: "Starting encrypted one-on-one and group conversations outside of any space."
order: 13
category: basics
---

# Direct Messages

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Not every conversation belongs in a room. Flotilla also gives you direct messages (DMs) — private conversations with one person or a small group, kept separate from any [space](/articles/spaces-and-rooms-explained). You don't have to share a space with someone to message them. All you need is their Nostr identity.

## Starting a conversation

DMs live in their own "Chats" section, apart from your spaces and rooms. Open it, click "Start New Chat," and add people in one of two ways:

- **Search an existing contact** by name, if you already follow them or have interacted before.
- **Paste an npub or hex pubkey** directly, if you know someone's Nostr identity but don't have a contact entry for them yet. Flotilla recognizes the key and adds them to the conversation.

You can add more than one person before you start. Add one person for a one-on-one conversation, or several for a small group chat. Once everyone's in, create the chat and start typing.

## As you type: drafts are saved automatically

If you start writing and get pulled away — a notification, a tab switch, closing the app — you won't lose your work. Flotilla saves your in-progress message as a draft tied to that specific conversation. When you come back, your unsent text is still in the composer, ready to finish and send.

## How DMs differ from room chat

Room chat is meant for other members of a space, and it lives on whatever relay hosts that space. Direct messages work differently in a few important ways:

- **They're end-to-end encrypted.** Flotilla uses the NIP-17 standard for DMs, so the content of your conversation can't be read by relays or anyone else it passes through. For the full picture of what that encryption does and doesn't guarantee — and how it compares to the privacy model of spaces — see [Is Flotilla Private?](/articles/is-flotilla-private).
- **They're not scoped to a space.** A DM exists independently of any community. You can message someone you've never shared a space with, as long as you have their key.
- **They include a small proof-of-work step.** Before a DM is sent, your device does a bit of extra computation attached to the message. This is a spam-mitigation measure: sending a normal volume of messages stays cheap, but blasting out large amounts of unwanted mail gets expensive.

## Where to go from here

To understand exactly what the encryption behind DMs protects — and its real limits, like the lack of forward secrecy — read [Is Flotilla Private?](/articles/is-flotilla-private). For the everyday mechanics of chatting inside a space, see [Chatting in a Space](/articles/chatting-in-a-space). And if you'd rather not be pinged every time someone messages you, [Notifications and Muting](/articles/notifications-and-muting) covers how to control that.
