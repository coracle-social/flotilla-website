---
title: "Installing Flotilla on Web and Mobile"
description: "How to run Flotilla in a browser, install it as a PWA, or get the native Android and iOS apps."
order: 8
category: basics
---

# Installing Flotilla on Web and Mobile

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Flotilla isn't locked behind an app store account or a platform login. It's a Nostr client, so the only thing you need to bring is your key (see [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity)). How you *run* it is up to you: in a browser tab, installed as an app on your home screen, or as a native download on Android or iOS.

## Use it in a browser

The simplest way to use Flotilla is to visit [app.flotilla.social](https://app.flotilla.social) in any modern browser, on desktop or mobile. There's nothing to install, and it works the same on Windows, macOS, Linux, or ChromeOS. This is a good place to start if you're just trying Flotilla out — see [Getting Started](/articles/getting-started) for the signup and login flow.

## Install it as a PWA

Flotilla is also a Progressive Web App (PWA), so you can install it straight from your browser without going through an app store. Installing gives you a proper home-screen or desktop icon, a standalone window without browser chrome, and push notifications — handy if you want to be pinged when someone messages you without keeping a browser tab open. When you visit app.flotilla.social, most browsers offer an "Install" or "Add to Home Screen" option in a menu or the address bar; the exact wording and location depend on your browser and OS.

This is also the closest thing to a desktop app today. Flotilla doesn't ship a separate native desktop application, so if you want an app-like experience on Windows, macOS, or Linux, installing the PWA is the way to do it.

## Android: get it on Google Play

On Android, install Flotilla from the [Google Play Store](https://play.google.com/store/apps/details?id=social.flotilla). The native app supports push notifications and can hand off signing to a dedicated signer app like Amber (see [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) for how that works), so your key never has to live inside Flotilla itself if you'd rather keep it in a separate app.

It's also available on [Zapstore](https://zapstore.dev), an alternative app store, if you prefer — and the browser and PWA options above work just as well on Android too.

## iOS: get it on the App Store

On iPhone and iPad, install Flotilla from the [App Store](https://apps.apple.com/us/app/flotilla-chat/id6741344107). It works just like the web and Android versions for chatting, spaces, rooms, events, and direct messages. As on every platform, you can also use it straight from a browser or install the PWA if you'd rather not download anything.

## No separate desktop app — yet

There's currently no dedicated desktop application for Windows, macOS, or Linux. For a desktop experience, use Flotilla in your browser or install it as a PWA — both work fully, notifications included.

## One identity, every device

However you install it, Flotilla is just a window onto your Nostr identity. It doesn't store your spaces or messages itself; those live on the relays your spaces run on. So you can install Flotilla on your phone, log in on your laptop's browser, and add the PWA on a tablet, all with the same key, and everything — your spaces, your rooms, your direct messages — will be there on each one. There's no separate "Flotilla account" to set up per device, just the same identity logging in wherever you need it.

If you're not sure which login method fits the device you're setting up, [Ways to Log In to Flotilla](/articles/logging-in-to-flotilla) walks through the options and which is safest for each situation.
