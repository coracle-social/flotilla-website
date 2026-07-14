---
title: "Managing a Space"
slug: managing-a-space
source: https://flotilla.social/articles/managing-a-space
description: "Space settings, membership, roles, bans, reports, and room permissions for community organizers."
order: 33
category: advanced
---

# Managing a Space

*Part of our guide to [running an online community you actually own](/articles/how-to-run-an-online-community).*

Flotilla comes with a number of features specifically designed to help community organizers manage membership, moderate content, and control access.

Before we get started, it's important to understand that spaces in Flotilla are always hosted by [Nostr relays](https://nostr.com/), which are a special type of server. The level of support for various management features will depend on what kind of Nostr relay you're hosting your space on — we recommend using [Zooid by Coracle](https://github.com/coracle-social/zooid), or signing up with [Hosting by Coracle](https://hosting.coracle.social/).

### Space Details

If your space relay supports Nostr's [relay management API](https://github.com/nostr-protocol/nips/blob/master/86.md) (and you have permission to use it), you'll be able to edit your space's details from within Flotilla. Just open up the main menu for the space, and click "Space Information", then "Edit". You'll then be able to edit your space's name, description, and image.

![](/images/aEJkBRBQUhOB9Vz6HgSwj7ebv8c.png)

### Space Membership

To view your space's members, open up the main space menu and click "View Members". This will show you a list of people who are advertised by the host relay as having access to your space. For how people get onto this list in the first place — invite links, adding members by pubkey, and open-vs-private access policy — see [Controlling Who Can Join Your Space](/articles/controlling-space-access).

![](/images/1FZbjuqxKjbk8fhv5l2exQzUmU.png)

### Banning Users

From the space members dialog, you can also see a list of people you've banned from your server, with the ability to restore their membership status.

![](/images/WLcL6LghMSptUZn6smnbIbSWQ.png)

You can also ban or restore members from their profile detail view.

![](/images/iYbmC9rlJ9YV9HmYZuhjWCgeldI.png)

When a user is banned, all their content may also be deleted from your relay, depending on relay implementation (Zooid by Coracle does this automatically for you).

### Reports and Moderation

You can also enlist other members of your space to help you keep things in check. Anyone in the space can "report" a post by clicking the overflow menu next to a message.

![](/images/s5HJG9pV1pOHI7R2u5EJfJwTmw.png)

This will open up a form requesting some additional information about the report. Admins can then "View Reports" from the main space menu.

![](/images/nxzgitzyUAmoirMJVQnkKlEXQ.png)

For each report, you can dismiss it, delete just the message, or you can completely ban the member from the space.

### Room Details

Every room can have its own policies as well — including default permissions, member lists, and user preferences. You can find this by joining a room, then clicking the info icon at the top of the screen.

![](/images/egs0jTA1Ys001qjfgNt7DuEsx3Y.png)

From here you can view members, control whether you receive notifications for the room, and favorite the room to make it show up higher in the space's navigation.

If you're an admin, you can also delete or edit the room, and add or remove members.

![](/images/e1MOHQl9pW03d3peS2hMQamPtNM.png)

### Room Permissions

Rooms have certain permissions that control how non-members can interact with it:

- **Restricted** rooms only accept messages from members.
- Messages posted to **Private** rooms can only be viewed by room members.
- **Hidden** rooms are entirely hidden from non-members.
- **Closed** rooms are invite-only — there's no way to request access to a closed room.

### Space Roles

Admins can create custom, color-coded roles to help organize a space's membership. From the space's member directory or member management screens, create a role with a label, a description, and a color, then assign it to whichever members it applies to. Assigned roles show up next to a member's name in the member directory, so anyone browsing the directory can see at a glance who holds which role.

It's worth being precise about what roles are and aren't. They're organizational and display labels — a way to mark out moderators, event hosts, or any other group you want to identify — not a fine-grained permission system. Assigning someone a role does not by itself grant them the ability to moderate or administer the space; that's governed separately, by the underlying relay (owners and the admins the relay recognizes). If you want someone to actually have moderation powers — banning members, editing room permissions, and the like — that's a relay-level admin grant, independent of any role label you've given them.
