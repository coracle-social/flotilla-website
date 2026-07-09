---
title: "Managing a Space"
slug: managing-a-space
source: https://flotilla.social/articles/managing-a-space
description: "Experience a new way to connect with your community online. Join an existing community space or launch your very own branded platform tailored to your audience. The decentralized Discord alternative built on the Nostr protocol."
order: 8
category: advanced
---

# Managing a Space

Flotilla comes with a number of features specifically designed to help community organizers manage membership, moderate content, and control access.

Before we get started, it's important to understand that spaces in Flotilla are always hosted by [Nostr relays](https://nostr.com/), which are a special type of server. The level of support for various management features will depend on what kind of Nostr relay you're hosting your space on — we recommend using [Zooid by Coracle](https://github.com/coracle-social/zooid), or signing up with [Hosting by Coracle](https://hosting.coracle.social/).

### Space Details

If your space relay supports Nostr's [relay management API](https://github.com/nostr-protocol/nips/blob/master/86.md) (and you have permission to use it), you'll be able to edit your space's details from within Flotilla. Just open up the main menu for the space, and click "Space Information", then "Edit". You'll then be able to edit your space's name, description, and image.

![](/images/aEJkBRBQUhOB9Vz6HgSwj7ebv8c.png)

### Space Membership

To view your space's members, open up the main space menu and click "View Members". This will show you a list of people who are advertised by the host relay as having access to your space.

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

In the future, Flotilla will include **role-based access control**, which will allow you to assign roles to users in order to delegate moderation, or grant access in bulk.

## Images

| local | original | alt | usage |
|---|---|---|---|
| /images/aEJkBRBQUhOB9Vz6HgSwj7ebv8c.png | https://framerusercontent.com/images/aEJkBRBQUhOB9Vz6HgSwj7ebv8c.png |  | inline body image |
| /images/1FZbjuqxKjbk8fhv5l2exQzUmU.png | https://framerusercontent.com/images/1FZbjuqxKjbk8fhv5l2exQzUmU.png |  | inline body image |
| /images/WLcL6LghMSptUZn6smnbIbSWQ.png | https://framerusercontent.com/images/WLcL6LghMSptUZn6smnbIbSWQ.png |  | inline body image |
| /images/iYbmC9rlJ9YV9HmYZuhjWCgeldI.png | https://framerusercontent.com/images/iYbmC9rlJ9YV9HmYZuhjWCgeldI.png |  | inline body image |
| /images/s5HJG9pV1pOHI7R2u5EJfJwTmw.png | https://framerusercontent.com/images/s5HJG9pV1pOHI7R2u5EJfJwTmw.png |  | inline body image |
| /images/nxzgitzyUAmoirMJVQnkKlEXQ.png | https://framerusercontent.com/images/nxzgitzyUAmoirMJVQnkKlEXQ.png |  | inline body image |
| /images/egs0jTA1Ys001qjfgNt7DuEsx3Y.png | https://framerusercontent.com/images/egs0jTA1Ys001qjfgNt7DuEsx3Y.png |  | inline body image |
| /images/e1MOHQl9pW03d3peS2hMQamPtNM.png | https://framerusercontent.com/images/e1MOHQl9pW03d3peS2hMQamPtNM.png |  | inline body image |
