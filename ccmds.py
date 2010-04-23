#! /usr/bin/env python
import socket
import time
import string
import IRCLISTS
import socket

class Chan_Commands(object):
	def __init__(self, Nick, Location, TotalString, CMD, line, args, s, iSend):
		self.Nick=Nick.capitalize()
		self.Location=Location
		self.TotalString=TotalString
		self.CMD=CMD
		self.line=line
		self.args=args
		self.s=s
		self.PM="PRIVMSG"
		self.rn="\r\n"
		self.LengthError="Not enough parameters"
		if self.Location=="Cam`":
			self.Location=self.Nick
		self.iSend=iSend
	def Up(self):
		if len(self.args)==5:
			if self.Nick == "Cam":
				self.cmdChanMode(self.args[4], "+o")
		if len(self.args)==4:
			if self.Nick in IRCLISTS.OpList:
				self.cmdChanMode(self.Nick, "+o")
	def Down(self):
		if len(self.args)==5:
			if self.Nick == "Cam":
				self.cmdChanMode(self.args[4], "-o")
		if len(self.args)==4:
			self.cmdChanMode(self.Nick, "-o")
	def	cmdChanMode(self, User, Mode):
		self.s.send("MODE %s %s %s%s" % (self.Location, Mode, User, self.rn))
	def Voice(self):
		if self.Nick in IRCLISTS.OpList:
			if len(self.args)==5:
				self.cmdChanMode(self.args[4], "+v")
			if len(self.args)==4:
				self.cmdChanMode(self.Nick, "+v")
	def DeVoice(self):
		if len(self.args)==5:
			if self.Nick in IRCLISTS.OpList:
				self.cmdChanMode(self.args[4], "-o")
		if len(self.args)==4:
			self.cmdChanMode(self.Nick, "-v")
	def ChannelJP(self, jp):
		if jp=="join":
			if len(self.args)==5:
				if self.Nick in IRCLISTS.OpList:
					self.s.send("JOIN :%s%s" % (self.args[4], self.rn))
		elif jp=="part":
			if len(self.args)==5:
				if self.Nick in IRCLISTS.OpList:
					self.s.send("PART :%s%s" % (self.args[4], self.rn))
			elif len(self.args)==4:
				if self.Nick in IRCLISTS.OpList:
					self.s.send("PART :%s%s" % (self.Location, self.rn))
		
		