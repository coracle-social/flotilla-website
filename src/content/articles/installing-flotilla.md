---
title: "Installing Flotilla on Web and Mobile"
description: "How to run Flotilla in a browser, install it as a PWA, or get the native Android and iOS apps."
order: 8
category: basics
---

# Installing Flotilla on Web and Mobile

*Part of our guide to [understanding Nostr](/articles/what-is-nostr).*

Flotilla isn't locked behind an app store account or a platform login — it's a Nostr client, so the only thing you need to bring is your key (see [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity)). How you *run* it, though, is up to you: in a browser tab, installed as an app on your home screen, or as a native download on Android or iOS.

## Use it in a browser

The simplest way to use Flotilla is to visit [app.flotilla.social](https://app.flotilla.social) in any modern browser, on desktop or mobile. There's nothing to install, and it works the same whether you're on Windows, macOS, Linux, or ChromeOS. This is a good place to start if you're just trying Flotilla out — see [Getting Started](/articles/getting-started) for the signup and login flow.

## Install it as a PWA

Flotilla is also a Progressive Web App (PWA), which means you can install it straight from your browser without going through an app store. Installing gives you a proper home-screen or desktop icon, a standalone window without browser chrome, and push notifications — useful if you want to be pinged when someone messages you without keeping a browser tab open. Most browsers offer an "Install" or "Add to Home Screen" option somewhere in their menu or address bar when you visit app.flotilla.social; the exact wording and location depend on your browser and OS.

This is also the closest thing to a desktop app today — Flotilla doesn't ship a separate native desktop application, so if you want an app-like experience on Windows, macOS, or Linux, installing the PWA is the way to do it.

## Android: get the app from Zapstore

On Android, Flotilla is distributed as a native app through [Zapstore](https://zapstore.dev), rather than the Google Play Store. The native Android app supports push notifications and can hand off signing to a native signer app like Amber (see [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) for how that works), so your key never has to live inside Flotilla itself if you'd rather keep it in a dedicated signer.

If you'd prefer not to install anything from Zapstore, the browser and PWA options above work just as well on Android.

## iOS: native app, with one caveat

Flotilla also ships a native iOS app. It works the same as the web and Android versions for chatting, spaces, rooms, and direct messages — with one notable exception: **Lightning zaps and the wallet are not available on iOS**. Apple's App Store policy doesn't permit this kind of payment flow, so the wallet settings and zap buttons you'd see elsewhere are disabled in the iOS build. If sending or receiving zaps matters to you, use Flotilla in a browser or as a PWA on iOS, or switch to Android or desktop when you need to zap. See [Zaps and Your Wallet](/articles/zaps-and-wallet) for what you're missing.

## No separate desktop app — yet

There's currently no dedicated desktop application for Windows, macOS, or Linux. For a desktop experience, use Flotilla in your browser or install it as a PWA, both of which work fully, including notifications.

## One identity, every device

However you install it, Flotilla is just a window onto your Nostr identity — it doesn't store your spaces or messages itself; those live on the relays your spaces run on. That means you can install Flotilla on your phone, log in on your laptop's browser, and add the PWA on a tablet, all with the same key, and everything — your spaces, your rooms, your direct messages — will be there on each one. There's no separate "Flotilla account" to set up per device, just the same identity logging in wherever you need it.

If you're not sure which login method fits the device you're setting up, [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) walks through the options and which is safest for each situation.
