#! /usr/bin/env python
import socket
import time
import string
import IRCLISTS
import cmds
import parse

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
		self.LoginPassword="erc333"
		if "#" not in self.Location:
			if len(self.args)==5:
				if self.args[4].lower()==self.LoginPassword:
					if self.Nick in IRCLISTS.OpList:
						self.iSend("Error, you are already in the op list")
					else:
						self.iSend("Authorized. I added you to my OpList")
						IRCLISTS.OpList.append(self.Nick)
				else:self.iSend("Incorrect Password")
			else:self.iSend(self.LengthError)
		else:self.iSend("Please use this command in PM")
	def	cmdChanMode(self, User, Mode):
		self.s.send("MODE %s %s %s%s" % (self.Location, Mode, User, self.rn))
	def cmdKick(self, User, kmsg):
		self.s.send("KICK %s %s :%s%s" % (self.Location, User, kmsg, self.rn))
	def Ban(self, su):
		if self.Nick in IRCLISTS.OpList:
			if su=="ban":
				if len(self.args)>5:
					kmsg=" ".join(self.args[5:])
					self.cmdChanMode(self.args[4], "+b")
				if len(self.args)==5:
					kmsg="You have been banned from %s" % self.Location
					self.cmdChanMode(self.args[4], "+b")
			if su=="unban":
				if len(self.args)==5:
					self.cmdChanMode(self.args[4], "-b")
	def Kick(self):
		if len(self.args)>5:
			if self.Nick in IRCLISTS.OpList:
				self.cmdKick(self.args[4], " ".join(self.args[5:]))
		else:
			if self.Nick in IRCLISTS.OpList:
				KickMSG="You have been kicked from %s." % self.Location
				self.cmdKick(self.args[4], KickMSG)
	def UserHost(self):
		if len(self.args)==5:
			self.UserHostWho=self.args[4]
			global UserHostLocation
			UserHostLocation=self.Location
			self.s.send("USERHOST %s\r\n" % self.UserHostWho)
	def UserHost2(self):
			try:
				self.s.send("PRIVMSG %s :%s\r\n" % (UserHostLocation, self.args[3]))
				print self.args[3].split("@")[1]
			except AttributeError:
				print "Attribute ERROR"
			
			
			