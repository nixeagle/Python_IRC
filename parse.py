#! /usr/bin/env python
import socket
import time
import string
import cmds
import opcmds
import ccmds
import spanish
import web

class Parse(object):
	def __init__(self, Nick, Location, TotalString, CMD, line, args, s):
		self.Nick=Nick
		self.Location=Location
		self.TotalString=TotalString
		self.CMD=CMD
		self.line=line
		self.args=args
		self.s=s
		self.PM="PRIVMSG"
		self.rn="\r\n"
		if self.Location=="Cam`":
			self.Location=self.Nick
		self.mod_cmds=cmds.Commands(self.Nick, self.Location, self.TotalString, self.CMD, self.line, self.args, self.s, self.iSend)
		self.op_cmds=opcmds.OpCommands(self.Nick, self.Location, self.TotalString, self.CMD, self.line, self.args, self.s, self.iSend)
		self.chan_cmds=ccmds.Chan_Commands(self.Nick, self.Location, self.TotalString, self.CMD, self.line, self.args, self.s, self.iSend)
		self.spanish=spanish.Spanish(self.Nick, self.Location, self.TotalString, self.CMD, self.line, self.args, self.s, self.iSend)
		self.web=web.Web(self.Nick, self.Location, self.TotalString, self.CMD, self.line, self.args, self.s, self.iSend)
	
	def Parse(self):
		#Start Parsing commands
		if len(self.args)>=4:
			if self.CMD==".login":self.op_cmds.Login("add")
			elif self.CMD==".admindelete":self.op_cmds.Login("del")
			elif self.CMD==".list":self.mod_cmds.List()
			elif self.CMD==".lookup":self.mod_cmds.LookUp()
			elif self.CMD==".up":self.chan_cmds.Up()
			elif self.CMD==".down":self.chan_cmds.Down()
			elif self.CMD==".leet":self.mod_cmds.LeetSpeak()
			elif self.CMD==".voice":self.chan_cmds.Voice()
			elif self.CMD==".devoice":self.chan_cmds.DeVoice()
			elif self.CMD==".kick":self.op_cmds.Kick()
			elif self.CMD==".conj":self.spanish.Conjugate()
			elif self.CMD==".j":self.chan_cmds.ChannelJP("join")
			elif self.CMD==".p":self.chan_cmds.ChannelJP("part")
			elif self.CMD==".ban":self.op_cmds.Ban("ban")
			elif self.CMD==".unban":self.op_cmds.Ban("unban")
			elif self.CMD==".ud":self.web.UD()
			elif self.CMD==".dict":self.web.Dict()
			elif self.CMD==".py":self.mod_cmds.PyEvaluator()
			elif self.CMD==".np":self.mod_cmds.NowPlaying()
			elif self.CMD==".quit":self.op_cmds.Quit()
			elif "=+~" in self.args[3]:self.op_cmds.ReturnUserHost()
			
			
			elif self.CMD==".git" or self.CMD==".source":self.iSend("My source code is: http://github.com/Cam1337/Python_IRC")
			try:
				if self.CMD[0]==">":self.mod_cmds.Action()
			except IndexError, e:
				pass
			
	#iSend function	
	def iSend(self, msg):
	   x="%s %s :%s %s" % (self.PM, self.Location, msg, self.rn)
	   self.s.send(x)
	   print(x)
		
