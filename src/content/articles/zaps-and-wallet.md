---
title: "Zaps and Your Wallet"
description: "Send Lightning tips on messages, events, and community goals, and connect a wallet to Flotilla."
order: 18
category: basics
---

# Zaps and Your Wallet

A "zap" is a Lightning payment — a tip in sats (satoshis, fractions of a bitcoin) that you send directly to another person in response to something they posted. Zaps are a core part of how Nostr communities show appreciation: instead of just reacting with an emoji, you can back it up with real value. You can zap a message in a [room](/articles/chatting-in-a-space), a thread, a calendar event, or a fundraising goal.

## Sending a zap

Wherever zapping is available — on a chat message, thread post, event, or goal — you'll find a zap button (usually a lightning-bolt icon). Tapping it lets you send a preset amount with one click, or enter a custom number of sats if you want to send something different. Larger zaps can be a way of highlighting the messages or contributions you think matter most in a space.

If you don't have a wallet connected to Flotilla yet, zapping still works: Flotilla falls back to showing you a Lightning invoice, either as a QR code you scan with your own wallet app or as text you can copy and pay from anywhere. Connecting a wallet just makes the whole process faster, since you skip the scan-and-pay step every time.

## Connecting a wallet

To send and receive zaps without leaving the app, connect a wallet from your wallet settings. Flotilla supports two ways to do this:

- **Nostr Wallet Connect (NWC)** — pair a remote Lightning wallet by pasting its connection string. This works with any wallet or wallet service that speaks NWC.
- **WebLN** — connect a browser-based Lightning wallet extension.

Once a wallet is connected, your wallet settings page shows your balance, and you can send or receive sats directly — useful if someone zaps you back, or if you want to top up before a round of zapping.

## Wallet settings

From the same settings page, you can also configure:

- **A Lightning address** — so people can send sats to you outside of Flotilla too, using any Lightning wallet.
- **Default preset zap amounts** — the quick-tap amounts that show up on the zap button, so you can tune them to whatever denominations make sense for you.

## Zaps are disabled on iOS

Because of App Store policy, Flotilla's iOS build ships with zaps and the wallet turned off entirely — you won't see a zap button on messages, events, or goals, and the wallet item is hidden from settings. This is a platform-specific restriction, not a bug: the same account works fine for zapping on the web app, the installed PWA, or Android. See [Installing Flotilla on Web and Mobile](/articles/installing-flotilla) for the full rundown of what's available on each platform. If you want to zap from your phone, use the web app or PWA in a mobile browser instead of the native iOS app.

## Zap-funded goals

Some spaces run **goals** — fundraising targets tied to a specific purpose, with a visible progress bar that fills up as people zap it. Zapping a goal works the same way as zapping a message: pick a preset or custom amount, and your sats count toward the total. Goals are one of the content types a space can include alongside its rooms; see [Spaces and Rooms Explained](/articles/spaces-and-rooms-explained) for how they fit into the bigger picture.
