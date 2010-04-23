#! /usr/bin/env python
import socket
import time
import string
import IRCLISTS
import socket

class Spanish(object):
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
			self.location=self.Nick
		self.iSend=iSend
	def Conjugate(self):
		Languages=["spanish"]
		Tenses=["present"]
		if len(self.args)==7 and self.Nick in IRCLISTS.OpList:
			Verb=self.args[4].lower()
			VerbBase=Verb[:len(Verb)-2]
			VerbEnding=Verb[len(Verb)-2:]
			if self.args[5].lower() in Languages:
				if self.args[5].lower()=="spanish":
					if self.args[6].lower() in Tenses:
						if self.args[6].lower()=="present":
							if VerbEnding=="ar":
								Answer="%so, %sas, %sa, %samos, %sais, %san" % (VerbBase,VerbBase,VerbBase,VerbBase,VerbBase,VerbBase)
								self.iSend(Answer)
							if VerbEnding=="er":
								Answer="%so, %ses, %se, %semos, %seis, %sen" % (VerbBase,VerbBase,VerbBase,VerbBase,VerbBase,VerbBase)
								self.iSend(Answer)
							if VerbEnding=="ir":
								Answer="%so, %ses, %se, %simos, %sis, %sen" % (VerbBase,VerbBase,VerbBase,VerbBase,VerbBase,VerbBase)
								self.iSend(Answer)
		