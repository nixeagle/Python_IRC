#! /usr/bin/env python

from BeautifulSoup import BeautifulSoup
import re
import urllib2

class Web(object):
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
	def UD(self):
		if len(self.args)>=5:
			try:
				definition = "The Definition for %s is: %s" % (" ".join(self.args[4:]),"".join(BeautifulSoup(urllib2.urlopen("http://www.urbandictionary.com/define.php?term=%s" % " ".join(self.args[4:]))).find("div", { "class" : "definition" })))
			except (TypeError, IndexError):
				definition="I cannot find the definition for \"%s\"" % " ".join(self.args[4:])
			self.iSend(definition)
			
	def Dict(self):
		if len(self.args)==5:
			try:
				definition = "The definition for %s is: %s " % ("".join(self.args[4:]),(str(BeautifulSoup(urllib2.urlopen("http://dictionary.reference.com/browse/%s" % ("".join(self.args[4:])))).find("div", { "class" : "dndata" }))).split(">")[1].split("<")[0])
			except (TypeError, IndexError):
				definition="I cannot find the definition for \"%s\"" % " ".join(self.args[4:])
			self.iSend(definition)
		else:self.iSend("Please only search for one word")
		
