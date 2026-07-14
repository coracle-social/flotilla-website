---
title: "Can I Delete My Account or Data?"
author: "Jon Staab"
pubDate: 2026-07-14
description: "Why there is no account to close on Nostr, what deleting a message or clearing your profile actually does, and why anything you publish is best treated as permanent."
order: 21
category: basics
---

# Can I Delete My Account or Data?

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Wanting to delete your account is normal, but on Nostr the honest answer is more complicated than a button. There's no platform account behind your Flotilla identity — see [Understanding Your Nostr Identity](/articles/understanding-your-nostr-identity) for what your key actually is. So there's nothing for Flotilla, or anyone else, to close, suspend, or erase on your behalf. What Flotilla *can* do is delete the content you've published and ask relays to stop serving it. Here's exactly what that does and doesn't accomplish.

## There's no account to revoke

Your identity is a cryptographic key pair, not a row in a database. No one — not Flotilla, not a space you belong to, not even you — can revoke or invalidate the key itself. There's no password reset and no support desk that can take down your identity, just as there's none to recover a lost key. Deleting data is a separate question from whether the key exists, and the key exists either way.

## Deleting a single message

Open the menu on one of your own messages in a space's room and choose **Delete Message**. Before sending a standard deletion request to that room's relay, Flotilla shows a confirmation — "This will send a request to delete this message. Be aware that not all relays may honor this request." It's a request, not a guarantee: a relay that ignores deletion requests, or anyone who already saved a copy, can keep the message around.

Space admins have a stronger, separate tool: they can hard-delete *any* message from their own relay (covered in [Managing a Space](/articles/managing-a-space)). That removes it from that one relay only, and it's the owner's action to take — not something you can do to content you don't control.

## Deleting your whole profile

Go to **Settings > Profile**, expand **Advanced**, and tap **Delete your profile**. Despite the button's name, this opens a much broader confirmation screen titled "Delete your account," and it does more than clear your profile fields. To proceed, you have to type the exact phrase "permanently delete my nostr account." Once you confirm, Flotilla:

1. Publishes a blanked profile (your name replaced with "[deleted]"), in case a relay doesn't support the deletion methods below.
2. Sends a "right to vanish" request, asking relays to remove everything tied to your key.
3. Sends individual deletion requests for every event of yours it knows about — every message, reaction, and other post — in batches until it has worked through them all.

These go out to your configured write relays, the network's indexer relays, and the relay of every space you belong to — a broad but defined set, not literally every relay that might ever have seen your content. When it finishes, Flotilla logs you out automatically. As the confirmation screen itself warns, not all relays may honor the request; if your content keeps showing up somewhere, you'd have to contact that relay directly.

## Treat anything you publish as permanent

Because Nostr events are signed, their authenticity can be proven even after you've asked to delete them — see [Is Flotilla Private?](/articles/is-flotilla-private) for what that means for deniability. A relay outside the set above, or anyone who copied your content before you deleted it, has no obligation to honor a request it never received. So assume anything you post is effectively permanent, deletion tools included; treat them as damage control, not an undo button.

## Bottom line

To walk away from an identity: delete the individual messages you regret, use "Delete your profile" to blank your profile and request removal of everything Flotilla knows you've published, then simply stop using that key. You can't guarantee removal everywhere, and you can't make the key itself stop existing — you can only stop giving it new activity.
