#! /usr/bin/env python
import socket
import time
import string
import config
import cmds
import parse
import config

class OpCommands(object):
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
	def Login(self):
		LoginPassword=config.OpPassword
		if "#" not in self.Location:
			if len(self.args)==5:
				if self.args[4].lower()==LoginPassword:
					if self.Nick in config.OpList:
						self.iSend("Error, you are already in the op list")
					else:
						self.iSend("Authorized. I added you to my OpList")
						self.iSend("You can now use +up, +down, +voice and +devoice")
						config.OpList.append(self.Nick)
				else:self.iSend("Incorrect Password")
			else:self.iSend(self.LengthError)
		else:self.iSend("Please use this command in PM")
	def	cmdChanMode(self, User, Mode):
		self.s.send("MODE %s %s %s%s" % (self.Location, Mode, User, self.rn))
	def cmdKick(self, User, kmsg):
		self.s.send("KICK %s %s :%s%s" % (self.Location, User, kmsg, self.rn))
	def cmdBan(self, User, Mode):
		self.s.send("MODE %s %s *!*%s%s" % (BanLocation, str(Mode), User, self.rn))

	def Ban(self, su):
		global BanLocation
		BanLocation=self.Location
		if self.Nick in config.OpList:
			if su=="ban":
				if len(self.args)>5:
					self.uHost(self.args[4], "+b")
				if len(self.args)==5:
					self.uHost(self.args[4], "+b")
			if su=="unban":
				if len(self.args)==5:
					self.uHost(self.args[4], "-b")
	def Kick(self):
		if self.Nick in config.OpList:
			if len(self.args)>5:
				self.cmdKick(self.args[4], " ".join(self.args[5:]))
			elif len(self.args)==5:
				KickMSG="You have been kicked from %s." % self.Location
				self.cmdKick(self.args[4], KickMSG)
				
	def uHost(self, a, ub):
		self.s.send("USERHOST %s\r\n" % a)
		global ubd
		ubd=ub
		
	def ReturnUserHost(self):
		HostName=self.args[3]
		HostName=HostName.split("~")[1]
		self.cmdBan(HostName, ubd)