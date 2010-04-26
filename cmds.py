#! /usr/bin/env python
import socket
import time
import string
import socket
import config
import re
import commands

GoodSongs=[]
BadSongs=[]

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
	
		if self.Nick in config.OpList:
			if len(self.args)>=5:
				if "|" not in self.args:
					MainCMD=" ".join(self.args[3:len(self.args)-1])[2:]
					MainWho=(self.args[len(self.args)-1])
					Total="%ss %s" %(MainCMD, MainWho)
					self.ActionSend(Total)
				else:
					wLocation=self.args.index("|")
					if len(self.args[2:wLocation]) ==2:
						MainCMD=" ".join(self.args[3:wLocation])[2:]
						MainWith=" ".join(self.args[wLocation+1:])
						Total="%ss with %s" % (MainCMD, MainWith)
						self.ActionSend(Total)
					else:
						MainCMD=" ".join(self.args[3:wLocation-1])[2:]
						MainWho=self.args[wLocation-1]
						MainWith=" ".join(self.args[wLocation+1:])
						Total="%ss %s (with %s)" % (MainCMD, MainWho, MainWith)
						self.ActionSend(Total)
			else:
				MainCMD=(self.args[3])[2:]
				Total="%ss" % MainCMD
				self.ActionSend(Total)
				

	def ActionSend(self, a):
		self.s.send("PRIVMSG %s :\x01ACTION %s \x01\r\n" % (self.Location, a)) 
			
			
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
					except (AttributeError, SyntaxError, IndexError, NameError, ArithmeticError, TypeError), e:
						self.iSend("Error: %s" % e)


		
	def NowPlaying(self):
		CurrentTrack=commands.getoutput("osascript -e 'tell application \"iTunes\" to name of current track as string'")
		CurrentArtist=commands.getoutput("osascript -e 'tell application \"iTunes\" to artist of current track as string'")
		ForStorage="[%s]by[%s]" % (CurrentTrack.strip(), CurrentArtist.strip())
		if len(self.args)==4:
			if self.Nick == "Cam":
				self.iSend("Cam, you are playing \"%s\" by \"%s\"" % (CurrentTrack.strip(), CurrentArtist.strip()))
				pass
			else:self.iSend("Sorry! This only works for Cam")
		else:
			if self.Nick=="Cam":
				if self.args[4]=="like":
					GoodSongs.append(ForStorage)
					self.iSend("Cam, the current song has been added to your favorite songs list")
				elif self.args[4]=="dislike":
					BadSongs.append(ForStorage)
					self.iSend("Cam, the current song has been added to your disliked songs list")
				elif self.args[4]=="good":
					self.iSend("".join(GoodSongs))
				elif self.args[4]=="bad":
					self.iSend("".join(BadSongs))
	
				
	def Regex(self):
		if len(self.args)>=5:
			try:
				i=self.args.index("|")
				try:
					Regex=" ".join(self.args[4:i])
					Match=" ".join(self.args[i+1:])
					m=re.search(Regex, Match)
					Total="Match: %s" % m.group(0)
					self.iSend(Total)
				except AttributeError:
					self.iSend("No match")
			except:
				self.iSend("%s, you idiot, '.regex code | match text'"%self.Nick)
			
			
			
			