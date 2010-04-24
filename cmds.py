#! /usr/bin/env python
import socket
import time
import string
import socket
import config
import re

class Commands(object):
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
	def List(self):
		x="OpList: %s" % config.OpList
		self.iSend(x)
		
	def LookUp(self):
		if len(self.args)==5:
			if self.IsInt(self.args[4].split(".")[0])==1:
				try:
					LookupAnswer=socket.gethostbyaddr(self.args[4])[0]
					self.iSend("%s, the hostname for %s is: %s" % (self.Nick, self.args[4], LookupAnswer))
				except socket.gaierror:
					self.iSend("I cannot find the Hostname for that.")
			else:
				try:
					LookupAnswer=socket.gethostbyname(self.args[4])
					self.iSend("%s, the IP for %s is: %s" % (self.Nick, self.args[4], LookupAnswer))
				except socket.gaierror:
					self.iSend("I cannot find the IP for that.")		
	def IsInt(self, str):
		ok = 1
		try:
			num = int(str)
		except ValueError:
			ok = 0
		return ok
	def LeetSpeak(self):
		if len(self.args)>=5:
			LeetSpeekText=" ".join(self.args[4:]).lower()
			LeetSpeekText=LeetSpeekText.replace("before","b4")
			LeetSpeekText=LeetSpeekText.replace("leet","1337")
			LeetSpeekText=LeetSpeekText.replace("a","4")
			LeetSpeekText=LeetSpeekText.replace("e","3")
			LeetSpeekText=LeetSpeekText.replace("i","1")
			LeetSpeekText=LeetSpeekText.replace("o","0")
			LeetSpeekText=LeetSpeekText.replace("s","5")
			LeetSpeekText=LeetSpeekText.replace("t","7")
			self.iSend(LeetSpeekText)
	def Action(self):
		if self.Nick in config.OpList or self.Nick=="Curtis":
			if len(self.args)>=5:
				if "|" not in self.args:
					a=" ".join(self.args[3:len(self.args)-1])[2:]
					self.s.send("PRIVMSG %s :\x01ACTION %ss %s\x01\r\n" % (self.Location, a, self.args[len(self.args)-1]))
				else:
					wt=self.args.index("|")
					if len(self.args[2:wt]) == 2:
						a=" ".join(self.args[3:wt])[2:]
						self.s.send("PRIVMSG %s :\x01ACTION %ss with %s \x01\r\n" % (self.Location, a, self.args[wt+1]))
					else:
						a=" ".join(self.args[3:wt-1])[2:]
						self.s.send("PRIVMSG %s :\x01ACTION %ss %s (with %s)\x01\r\n" % (self.Location, a, self.args[wt-1], " ".join(self.args[wt+1:])))
			else:
				a=(self.args[3])[2:]
				self.s.send("PRIVMSG %s :\x01ACTION %ss \x01\r\n" % (self.Location, a))
				
	def PyEvaluator(self):
		if self.Nick=="Cam":
			if len(self.args)>=5:
				a=" ".join(self.args[4:])
				if a in config.Banned_Eval:
					self.iSend("Error: Item in string caused error")	
				else:
					try:
						sa=eval(a)
						self.iSend("%s" % sa)
					except (AttributeError, SyntaxError, IndexError, NameError, ArithmeticError), e:
						self.iSend("Error: %s" % e)

	def Regex(self):
		if self.Nick=="Cam":
			if len(self.args)>=5:
				a=" ".join(self.args[4:])
				try:
					p = re.compile(a, re.IGNORECASE)
				except (sre_constants.error), e:
					pass
