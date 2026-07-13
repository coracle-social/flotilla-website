---
title: "Is Flotilla Private?"
slug: is-flotilla-private
source: https://flotilla.social/articles/is-flotilla-private
description: "What \"private\" actually means in Flotilla, and the different guarantees that apply to community spaces versus direct messages."
order: 19
category: basics
---

# Is Flotilla Private?

The topic of digital privacy is of great importance, but also quite complex. Calling something "private" can mean different things to different people — anything from "trust me bro" to full end-to-end encrypted communications.

There are two main areas covered by Flotilla where privacy requirements and guarantees differ: community spaces and direct messages.

### Space Privacy

Flotilla approaches digital privacy through a pragmatic lens, relying primarily on self-hosted community infrastructure to protect privacy rather than encryption. This allows community organizers to have greater control over exactly what content remains private, and who has access, rather than setting the rules for your community in stone through encryption.

As a result, spaces are as private as the policies enforced by the relays that host them. If a relay administrator prefers for the space to be invite-only and private, they can enforce that. If they prefer their community content to be read-only for non-members, that's an option too. The important thing is to communicate that expectation to community members.

Groups are only as private as the least trusted member. As members join a group, the guarantee that messages won't be shared out of context weakens dramatically. Protecting the privacy of a 50-member group using encryption would be overkill, given how week the groups privacy along a *social* dimension is likely to be.

It's also worth mentioning that because Flotilla is built on the Nostr protocol which uses digital signature to verify messages, it has weak *deniability*. What this means is that if content is leaked from of the group, it can be proven that it is authentic, because it was digitally signed by the author.

For this reason,we like to describe Flotilla's groups (particularly those hosted by [Coracle Hosting](https://hosting.coracle.social/) or using the [Zooid relay implementation](https://github.com/coracle-social/zooid) as "non-public", rather than "private". Flotilla is not a solution for journalists or activists, but for small communities.

### What Is Public About You

Before splitting things into spaces versus direct messages, it's worth being explicit about what's public about *you*, on any space you join, no matter how tightly that space's policies are set.

Your public key — your [npub](/articles/understanding-your-nostr-identity) — is exactly what the name says: public. It isn't a secret, and it isn't meant to be one; anyone can see it, and it's how other people and other apps recognize you as the same person across Nostr. Every public message you send, and your [profile](/articles/setting-up-your-profile) (display name, bio, avatar, and the rest), are signed by that key and readable by anyone who can read the relay hosting them. Your membership in a space, and the reactions you leave on other people's posts, work the same way — they're visible to anyone who can read that relay, not hidden from other readers just because they weren't posted in the main chat. That doesn't mean every relay is open to outsiders: as covered above, relays are closed by default, and non-members only see what an operator has chosen to expose. But whatever an operator *does* expose, your own activity within it isn't singled out for extra protection.

It's also worth treating anything you publish as effectively permanent, even where a delete option exists. Flotilla can delete a message you posted, and a self-hosted relay running zooid can be configured to expire events automatically or let an admin hard-delete something — but none of that is a guarantee. Deletion on Nostr is a request, not a command Flotilla or a relay operator can force every other relay, or anyone who already copied your content, to obey. See [Can I Delete My Account or Data?](/articles/deleting-your-account) for exactly what Flotilla's delete tools do and don't accomplish.

One more thing shapes what you reveal: some relays challenge Flotilla to prove who you are before serving you certain content. Flotilla only does that automatically for relays already in your own relay lists — for anywhere else, a setting decides whether it authenticates on your behalf. Leaving it off means you can read from an unfamiliar relay without the operator learning your identity; turning it on trades that away for relays that require it. See [Privacy Settings: Limiting What You Leak](/articles/privacy-settings) for that toggle and the rest of Flotilla's privacy controls.

### Direct Messages

With that said, Flotilla takes a different approach for direct messages, which represent a much more private form of communication. Because direct messages don't usually include more than a handful of participants (Flotilla supports small group chats as well as one-on-one conversations), it does make sense to protect them using encryption — particularly since DMs are often stored on public infrastructure.

To that end, Flotilla uses the [NIP 17](https://github.com/nostr-protocol/nips/blob/master/17.md) standard for end-to-end encrypted direct messages. The result is that not only are service providers unable to see your conversations, you also have deniability and metadata protection.

The thing that Flotilla DMs *do not* have however is either [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy) or [post-compromise security](https://crypto.stackexchange.com/questions/80095/what-is-post-compromise-security-exactly). In simple terms, this means that if your Nostr identity is ever compromised, it can lead to the attacker having access to old messages.

This represents a compromise between user experience and security — implementing these stronger security guarantees would also mean your messages would not be available when signing into a new device.

### The Future of Messaging

In the future, Flotilla may support an emerging standard being pioneered by the team at [WhiteNoise](https://www.whitenoise.chat/) called [Marmot](https://github.com/marmot-protocol/marmot/). This new protocol has all the features of strong encryption mentioned above, as well as the ability to host larger groups.

The standard is very new, and porting many of Flotilla's more sophisticated group management functionality to it would be a long process, so for the moment we are not actively adopting it, although we hope to in the future. In the meantime, if you're looking for a solution with better privacy guarantees, try [WhiteNoise](https://www.whitenoise.chat/)!
