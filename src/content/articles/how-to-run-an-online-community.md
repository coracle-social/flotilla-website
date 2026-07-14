---
title: "How to Run an Online Community You Actually Own"
description: "A practical, plain-English guide to starting, hosting, growing, and moderating an online community you truly own."
order: 0
category: basics
---

# How to Run an Online Community You Actually Own

Starting an online community is easy. Keeping one that is truly yours — where no company can bury your posts, suspend your account, or switch the whole thing off — takes a little more thought. This guide walks you through starting, hosting, growing, and moderating a community you actually own, in plain language, with no prior knowledge assumed.

## Why where you build matters

When you run a community on a big social platform, you are a tenant, not an owner. The platform owns the space your members gather in, the archive of everything you have ever said, and the switch that turns it all off. That works fine right up until it doesn't — a rule changes, an algorithm buries your posts, an account gets suspended by mistake, or the company decides your kind of community is no longer worth hosting. When that happens, there is usually no appeal and no way to take your people with you.

The alternative is to build somewhere you actually own. Your identity isn't an account a company issues and can revoke — it's yours, and it works the same across different apps, so no single platform can lock you or your members in or shut you out. The place your community lives answers to you, the organizer, rather than to a company's business model. If you ever want to move, you can, and your members and history can come along.

That ownership also changes what the space is for. Big platforms make money by showing ads and studying what you do so they can sell attention. A community you own has no reason to do either: no ads, no feed quietly reordering itself to keep people scrolling, no business built on watching your members. Flotilla is free to use and to join, and it earns nothing from watching you. The only optional costs live on the hosting side, which we come back to below.

Privacy follows from the same idea. How private your space is comes down to the policies you and your host choose to enforce — invite-only, members-only, or open — rather than rules a distant platform sets for you. It's a good fit for small communities that want to control who is in the room. It is not a tool for high-stakes anonymity, and it helps to be honest with your members about that from the start.

**Learn more:**
- [Understanding Your Identity](/articles/understanding-your-nostr-identity)
- [Is Flotilla Private?](/articles/is-flotilla-private)
- [Is Flotilla Free?](/articles/is-flotilla-free)

---

## Getting set up

Flotilla is software for running your own online community — think of it as an alternative to Discord, except nobody can take your community away from you.

Getting started takes a few minutes. Head to [app.flotilla.social](https://app.flotilla.social) and click "Create an Account." Flotilla sets up your identity, walks you through a short profile (all of it optional), and then lets you download a small backup file. Keep that file somewhere safe, like a password manager — it is how you prove the account is yours, so if you lose it you lose access. Unlike a normal login, this identity belongs to you, not to any platform, so no one else's decision can lock you out. (It runs on an open technology called Nostr, but you never have to think about that to use Flotilla — if you're curious how it works under the hood, see [What is Nostr?](/articles/what-is-nostr).)

Once you have an account, the next step is to create your community. In Flotilla, a community is called a "space." Here is the part that surprises most people: Flotilla doesn't host your space for you. The app is just the software you and your members use to get in — the space itself lives on a server you control. That is exactly what keeps the community yours.

You have two ways to get a space, and the difference comes down to who keeps that server running. The easy path is a hosting provider that runs it for you: click "Add a Space," then "Create a Space," and browse the available providers. Flotilla's parent company, Coracle, offers a managed option that's a simple place to start. The other path is running the server yourself, which gives you the most control. We compare both, including costs, in the hosting section below. Either way, once your space is set up you can invite people and start talking.

**Learn more:**
- [What is Flotilla?](/articles/what-is-flotilla)
- [Getting Started](/articles/getting-started)
- [Creating a Space](/articles/creating-a-space)

---

## Shaping your space

Your community lives in a space, and inside that space the day-to-day conversation happens in rooms. Rooms are just channels, like the ones in Slack or Discord. Set up as many as you need, each with its own name, icon, and purpose, so members always know where a conversation belongs. Most rooms are text chat, and some spaces add voice rooms for live audio. A space can hold more than chat, too: threads for longer discussions, a calendar of events, a library of pinned links, polls, and more. Turn on what fits your community and leave the rest.

By default, a new space is locked down. Until you say otherwise, only people you specifically invite or add can read or post — exactly what you want while you're getting your first members in. The simplest way to bring someone in is an invite link, created from the space's main menu. The one thing to remember is that an invite link is reusable, not single-use: redeeming it doesn't use it up, so treat it like a shared secret and only pass it to people you actually want in. If a link ever leaks, revoke it. You can also add someone directly if you already know exactly who belongs.

Opening a space up so people don't need an invite at all is a separate decision. You can allow anyone to read, anyone to post, or anyone to join outright. This isn't a toggle inside the chat itself; it's a setting where your community is hosted. For most communities, "anyone can read, but joining still takes a step" is a comfortable middle ground between fully private and wide open.

Part of making a space feel like yours is simply the shape you give it: the rooms you name, the icons you choose, the labels you assign to members, and which features you use. Flotilla also lets each member tune their own reading comfort — switching between light and dark, or adjusting text size — so the app stays pleasant no matter who's reading.

**Learn more:**
- [Spaces and Rooms Explained](/articles/spaces-and-rooms-explained)
- [Controlling Who Can Join Your Space](/articles/controlling-space-access)
- [Customizing How Flotilla Looks and Feels](/articles/customizing-how-flotilla-looks)

---

## Choosing your hosting

Every online community has to live somewhere — on a server that stays online, holds your messages, and lets members connect. As we saw, you have two ways to handle that: let someone run it for you, or run it yourself. Most organizers should start with managed hosting and only consider the second path if they have a specific reason to.

Managed hosting means you pay a small monthly fee and someone else keeps the machine running, updated, and online. With Coracle Hosting there are three plans you can set up yourself. The Free plan costs nothing and supports up to 10 members, but doesn't include image or video sharing. Basic is $5/month for up to 100 members with media included, and Growth is $25/month for an unlimited number of members. There's also a custom plan for larger communities, arranged by booking a call. You manage all of this from a separate control panel, not from the chat app your members use day to day.

Running it yourself is the other option, and it's the one place in this guide where "own your server" is literal. You rent a plain virtual server (a basic one runs around $11/month), install the community software on it, and point a domain at it. It gives you the most control, but it also makes you responsible for keeping the server updated, secure, and backed up. It's genuinely doable if you're comfortable following technical steps, and worth it if your community needs infrastructure fully under your own control — but for most organizers, managed hosting is the calmer choice.

Either way, you can give your community its own web address. A managed space comes with a default address out of the box (something like `myspace.spaces.coracle.social`), and you can swap in your own domain — `chat.mycommunity.com`, say — by adding one DNS record with whoever manages your domain. Using a subdomain like `chat.` is the simplest setup; pointing a bare root domain at your space is fiddlier and worth avoiding unless you have a reason to.

**Learn more:**
- [Hosting Your Space with Coracle](/articles/coracle-hosting)
- [Managing Your Hosted Space](/articles/managing-your-hosted-relay)
- [Billing and Payments for Your Hosted Space](/articles/hosting-billing)
- [Using a Custom Domain](/articles/custom-domain)
- [Self-Hosting a Space](/articles/self-hosting-a-space)

---

## Growing and engaging your community

With the space set up and hosted, the work shifts to keeping people coming back. A community stays alive when there's a reason to return. Chat is the heartbeat, but conversation moves fast and useful things get buried within a day. Give people anchors that outlast the scroll: highlight your welcome message or ground rules where new members see them first, and keep a searchable collection of the links, guides, and recurring event details worth finding again. That's the difference between a newcomer scrolling back through weeks of history and simply landing on "start here."

Vary how people can gather. Text is the default, but some spaces set up live voice rooms where members can drop in to talk, turn on a camera, or share a screen for a walkthrough or a casual hangout. Regular events give quieter members a low-pressure way to show up. The healthiest communities also point people back to the real world, so treat online activity as a way to coordinate gatherings and support, not a substitute for them.

Make it easy for members to feel their contributions matter. One simple way is a "zap": a small tip you send directly to someone in response to something they posted, instead of just reacting with an emoji. You can tip a message, a post, or an event, and some communities run funding goals with a progress bar that fills as people chip in toward a shared purpose. It's an optional touch, but a friendly way to say "this was worth something" with more than a thumbs-up. (Tipping is turned off on the iPhone app due to App Store rules; it works on the web and on Android.)

Finally, help people manage the firehose so they don't burn out and drift away. As a community grows, members can tune notifications down to just the rooms and mentions they care about, favorite the handful of rooms they check daily, and mute anyone they'd rather not hear from. When staying involved feels manageable, people stay involved.

**Learn more:**
- [Featured Content and the Library](/articles/featured-content-and-library)
- [Using Voice and Video Calls](/articles/using-voice-and-video-calls)
- [Zaps and Your Wallet](/articles/zaps-and-wallet)
- [Notifications and Muting](/articles/notifications-and-muting)
- [Running a Community](/articles/running-a-community)

---

## Moderating and keeping it healthy

Moderation gets easier when you are not doing it alone, and Flotilla gives you a few tools to share the load. Open your space's member list from the main menu ("View Members") to see who is in — the same panel where you add people. Removing someone is a separate action from un-inviting them: you ban them, either from the members list or from their profile. Banning removes their access, and depending on where your community is hosted, it can also clear out their past messages. Anyone you ban can be restored later from the same screen, so a ban isn't permanent unless you want it to be.

You don't have to catch every problem yourself. Any member can flag a post by opening the menu next to a message and reporting it, which sends it to you with a bit of context about what's wrong. Admins can review everything in one place ("View Reports") and, for each one, dismiss it, delete just the offending message, or ban the person outright. Letting members surface problems means you're not the only set of eyes on the room, which matters as a community grows.

To make your team visible, you can create custom, color-coded roles with a label, a description, and a color, then assign them to members. Roles show up next to people's names, so newcomers can tell at a glance who the moderators or hosts are. One thing worth being clear about: roles are labels, not powers. Giving someone a "Moderator" role marks them as one, but it does not by itself let them ban members or change room settings. Actual moderation ability is granted separately, at the level of the server where your community lives, so make sure the people wearing the badge also have the access to back it up.

A healthy community is partly about the tools working quietly in your favor. Because a space stays closed until you open it, nothing goes public by accident. It's also worth pointing members toward their own privacy controls so they understand what they share and can adjust it. None of this is set-and-forget, but the tools are built to let you run things steadily without hovering over every message.

**Learn more:**
- [Managing a Space](/articles/managing-a-space)
- [Controlling Who Can Join Your Space](/articles/controlling-space-access)
- [Privacy Settings](/articles/privacy-settings)

---

## Leveling up your setup

Everything so far works out of the box on managed hosting. This section is for the smaller number of organizers who run the server themselves and want to turn on a few extras by hand. If your community lives on managed hosting, you can safely skip ahead — these options are either handled for you or available as a simple on/off switch.

The first extra is media storage: where the images and files your members share actually get kept. If you run your own server you can store them on the same machine your community lives on, or hand them off to a cloud storage service instead. One thing genuinely worth knowing: by default, uploaded files can be opened by anyone who has the link, even people outside your community. If your space is meant to be private, that's a setting you'll want to change. There's also a fixed 10 MB limit per file.

The second is voice and video calls. Calls with screen sharing are supported, but they rely on a separate piece of software that handles the live audio and video. On your own server you set that up and connect it yourself; on managed hosting it's one toggle and the rest is done for you. Either way, once it's switched on, a room only becomes a call room when an admin creates it as a "Voice" room.

The last is backups. If you run the server yourself, keeping copies of your community's data and identity is your job — nothing does it automatically, and losing the wrong file can mean losing the community's identity entirely. Set up a routine early and store a copy somewhere other than the server itself. Managed hosting takes care of this for you.

**Learn more:**
- [Setting Up Media Storage on Your Server](/articles/setting-up-media-storage-on-your-relay)
- [Enabling Voice and Video Calls on Your Server](/articles/enabling-voice-and-video-calls-on-your-relay)
- [Backing Up Your Self-Hosted Server](/articles/backing-up-and-upgrading-a-relay)

---

## Ready to start?

You don't need to plan the whole thing before you begin. Create your account, spin up a space, and invite a few people — you can shape rooms, open things up, and add features as you go. When you're ready to pick a hosting plan, the [pricing page](/pricing) lays out the options side by side.

Start your community at [app.flotilla.social](https://app.flotilla.social).
