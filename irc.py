#! /usr/bin/env python
import socket
import time
import string
import parse
import cmds
import opcmds
import IRCLISTS
import ccmds
import spanish

class IRCConnect(object):
	def __init__(self, HOST, PORT, NICK, IDENT, REALNAME, JoinChannel, readbuffer, s):
		self.HOST=HOST
		self.PORT=PORT
		self.NICK=NICK
		self.IDENT=IDENT
		self.REALNAME=REALNAME
		self.JoinChannel=JoinChannel
		self.s=s
		self.readbuffer=readbuffer
	def Start(self):
		self.s.connect((self.HOST, self.PORT))
		self.s.send("NICK %s\r\n" % self.NICK)
		self.s.send("USER %s %s bla :%s\r\n" % (self.IDENT, self.HOST, self.REALNAME))
		self.s.send("PRIVMSG NICKSERV :IDENTIFY PASSWORD\r\n")
		time.sleep(2)
		self.s.send("JOIN %s\r\n" % (self.JoinChannel))
	def ReadBuffer(self):
		readbuffer=self.readbuffer+self.s.recv(1024)
		self.temp=string.split(readbuffer, "\n")
		readbuffer=self.temp.pop()
		for line in self.temp:
			line=string.rstrip(line)
			self.args=string.split(line)
			if len(self.args)>1:
				if self.args[0] == "PING": self.s.send("PONG %s\r\n" % self.args[1])
		if len(self.args)>=4:
			self.line=line
			self.CMD=(self.args[3])[1:].lower()
			self.TotalString=" ".join(self.args[3:])[1:]
			self.Nick=(self.args[0].split("!")[0])[1:]
			self.Location=self.args[2]
			Parse=parse.Parse(self.Nick, self.Location, self.TotalString, self.CMD, self.line, self.args, self.s)
			Parse.Parse()
			if self.Nick=="Cam":
				if self.CMD=="!r":
					reload(parse)
					reload(cmds)
					reload(opcmds)
					reload(IRCLISTS)
					reload(ccmds)
					reload(spanish)



HOST="irc.freenode.net"
PORT=6667
NICK="Cam`"
IDENT="CamBot"
REALNAME="Owned by Cam"
PM="PRIVMSG"
JoinChannel="##bottest[cam]"
readbuffer=""
s=socket.socket()


Connect_IRC=IRCConnect(HOST, PORT, NICK, IDENT, REALNAME, JoinChannel, readbuffer, s)
Connect_IRC.Start()
while 1:
	Connect_IRC.ReadBuffer()
	print Connect_IRC.line