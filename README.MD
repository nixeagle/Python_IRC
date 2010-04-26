Python IRC
==========

Written by Cam1337, the bot's source can be found on
[github](http://github.com/Cam1337/Python_IRC).

Commands
========

Python IRC supports a number of commands, all case insensitive.

Commands all must be prefixed with the bot's comchar. This is a single
character that gets prefixed to all commands. If the comchar is `!` then
all irc messages starting with that char will be treated by the bot as a
potential command. For the purposes of this documentation, the comchar
will always be `!` for simplicity.

For example the following shows a command example:
    !<command> <some arg description> <another arg description> => result


Login
-----

Authenticates bot admins to the bot and must be sent vie a PM.
    !login <password>

Admins have the ability to use higher level channel management commands as
well as additional special commands on the bot. The password for each
admin is configured in the configuration file.

list
----

Lists the current authenticated admins.
    !list => <authed admins>

lookup
------

This one does two things:

Lookup a hostname given an IP.
    !lookup <IP> => <hostname>

Lookup the website's IP given a hostname. Hostnames here mean website
names like `yahoo.com`, `google.com`, and so on.
    !lookup <hostname> => <IP>

up and down
-----------

Gives requesting user ops.
    !up

Remove ops from requesting user.
    !down

voice and devoice
-----------------

Gives requesting user voice.
    !voice

Removes voice from requesting user.
    !devoice

kick
----

Lets admins kick channel trolls with an optional message.
    !kick <troll> [<message>]

conj
----

Conj - A little project that will likely get it's data from the web, for
now, it conjugates all spanish present verbs that end in "er","ar","ir" in
the correct form. Usage - +conj hablar spanish present / MUST have the
"spanish present" on the end.

join
----

Tells the bot to join a channel. Can only be used by admins.
    !join <channel>

part
----

Make the bot part the channel when told to do so by an admin.
    !part [<channel>]

ban
---

Ban hostmask of a troll with optional ban message
    !ban <troll> [<message>]

unban
-----

Removes a user ban done by the bot. Can only be used by admins.
    !unban <user>

ud
---

Returns word's definition from the *Urban Dictionary*
    !ud <word>

dict
----

Looks up word in a dictionary and returns its definition.
    !dict <word>

Configuration
=============

The configuration file is in `config.py`.

Example
-------

> #! /usr/bin/env python
> HOST="irc.freenode.net"
> PORT=6667
> NICK="<your nick here>"
> IDENT="Cam-Bot"
> DefaultChannel="<your channel>"
> Bot_Password="<your bots password>" # Optional, for NickServ authorization.
> REALNAME="Written by Cam"
> OpPassword="<your operator password>"

Bugs, Problems, Suggestions
===========================

Please report all bugs, problems and suggestions to the
[github issues tracker](http://github.com/Cam1337/Python_IRC/issues).
