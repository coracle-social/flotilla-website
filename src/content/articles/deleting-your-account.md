---
title: "Can I Delete My Account or Data?"
description: "Why there is no account to close on Nostr, what deleting a message or clearing your profile actually does, and why anything you publish is best treated as permanent."
order: 21
category: basics
---

# Can I Delete My Account or Data?

"Delete my account" is a normal thing to want, and on Nostr the honest answer is more complicated than a button. There's no platform account behind your Flotilla identity — see [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) for what your key actually is. That means there's nothing for Flotilla, or anyone else, to close, suspend, or erase on your behalf. What Flotilla *can* do is delete the content you've published and ask relays to stop serving it. Here's exactly what that does and doesn't accomplish.

## There's no account to revoke

Your identity is a cryptographic key pair, not a row in a database. No one — not Flotilla, not a space you belong to, not even you — can revoke or invalidate the key itself. There's no password reset and no support desk that can process a takedown on your identity, the same way there isn't one to recover a lost key. Deleting data is a separate question from the key existing, and the key keeps existing either way.

## Deleting a single message

Open the menu on one of your own messages in a space's room and choose **Delete Message**. Flotilla shows a confirmation — "This will send a request to delete this message. Be aware that not all relays may honor this request." — before it sends a standard deletion request to that room's relay. It's a request, not a guarantee: a relay that doesn't honor deletion requests, or anyone who already saved a copy, can keep the message around regardless.

Space admins have a stronger, separate tool: they can hard-delete *any* message from their own relay (covered in [Managing a Space](/articles/managing-a-space)). That only removes it from that one relay, and it's an action the owner takes — not something available to you for content you don't control.

## Deleting your whole profile

Go to **Settings > Profile**, expand **Advanced**, and tap **Delete your profile**. Despite the button's name, this opens a much broader confirmation screen titled "Delete your account," and it does more than clear your profile fields. You have to type the exact phrase "permanently delete my nostr account" to proceed. Once confirmed, Flotilla:

1. Publishes a blanked profile (your name replaced with "[deleted]"), in case a relay doesn't support the deletion methods below.
2. Sends a "right to vanish" request, asking relays to remove everything tied to your key.
3. Sends individual deletion requests for every event of yours it knows about — every message, reaction, and other post — in batches until it's worked through all of them.

These go out to your configured write relays, the network's indexer relays, and the relay of every space you're a member of — a broad, defined set, not literally every relay anywhere that might have ever seen your content. When it finishes, Flotilla logs you out automatically. As the confirmation screen itself notes: not all relays may honor the request, and if your content keeps showing up somewhere, you'd need to contact that relay directly.

## Treat anything you publish as permanent

Because Nostr events are signed, their authenticity can be proven even after you've asked for them to be deleted — see [Is Flotilla Private?](/articles/is-flotilla-private) for what that means for deniability. A relay outside the set above, or anyone who already copied your content before you deleted it, has no obligation to honor a request they never received. The safe assumption is that anything you post is effectively permanent, deletion tools included — think of them as damage control, not an undo button.

## Bottom line

If you want to walk away from an identity: delete the individual messages you regret, use "Delete your profile" to blank your profile and request removal of everything Flotilla knows you've published, and then simply stop using that key. There's no way to guarantee removal everywhere, and no way to make the key itself stop existing — you can only stop giving it new activity.
