---
title: "Direct Messages"
description: "Starting encrypted one-on-one and group conversations outside of any space."
order: 13
category: basics
---

# Direct Messages

Not every conversation belongs in a room. Flotilla also gives you direct messages (DMs) — private conversations with one other person or a small group, completely separate from any [space](/articles/spaces-and-rooms-explained). You don't need to share a space with someone to message them; all you need is their Nostr identity.

## Starting a conversation

DMs live in their own "Chats" section of the app, apart from your list of spaces and rooms. Open it and click "Start New Chat" to begin. From there you can add people in two ways:

- **Search an existing contact** by name, if you already follow them or have interacted with them before.
- **Paste an npub or hex pubkey** directly if you know someone's Nostr identity but don't yet have a contact entry for them — Flotilla recognizes the pasted key and adds them to the conversation automatically.

You can add more than one person before starting the chat. Adding just one person creates a one-on-one conversation; adding several creates a small group chat. Once you've added everyone you want, create the chat and start typing.

## As you type: drafts are saved automatically

If you start composing a message and get pulled away — a notification, a tab switch, closing the app — you won't lose it. Flotilla saves your in-progress message as a draft tied to that specific conversation, so when you come back to it, your unsent text is still sitting in the composer, ready to finish and send.

## How DMs differ from room chat

Room chat in a space is meant to be seen by other members of that space, and it lives on whatever relay hosts the space. Direct messages are different in a few important ways:

- **They're end-to-end encrypted.** Flotilla uses the NIP-17 standard for DMs, so the content of your conversation isn't readable by relays or anyone else it passes through. For the full picture of what that encryption does and doesn't guarantee — and how it compares to the privacy model of spaces — see [Is Flotilla Private?](/articles/is-flotilla-private).
- **They're not scoped to a space.** A DM exists independently of any community; you can message someone you've never shared a space with, as long as you have their key.
- **They include a small proof-of-work step.** Before a DM is sent, your device does a bit of extra computational work attached to the message. This is a spam-mitigation measure — it makes it cheap to send a normal volume of messages but expensive to blast out large amounts of unwanted mail.

## Where to go from here

If you want to understand exactly what the encryption behind DMs protects — and its real limits, like the lack of forward secrecy — read [Is Flotilla Private?](/articles/is-flotilla-private). For the everyday mechanics of chatting inside a space instead, see [Chatting in a Space](/articles/chatting-in-a-space). And if you'd rather not be pinged every time someone messages you, [Notifications and Muting](/articles/notifications-and-muting) covers how to control that.
