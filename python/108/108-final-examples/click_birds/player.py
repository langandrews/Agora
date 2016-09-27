''' This file contains everything that interacts with the player's data.
Created Fall 2015
Final Project
@author: Logan Arens (lca4)
'''
import savedata, pickle

class Player():
	def __init__(self):
		try:
			with open('bis15.sav', 'rb') as newsavedata:
					self.savedata = pickle.load(newsavedata)
		except:
			# Something went wrong. Did they import a Python 3 save into Python 2, or an outdated save?
			print("Save did not exist, or was corrupted.")
			self.savedata = savedata.Data()
		
	def clickforseeds(self):
		self.savedata.numberofseeds += self.savedata.seedsperclick
		
	def refreshsps(self):
		# Set SPS to the number of finches (1 sps/bird)
		self.savedata.seedspersecond = (self.savedata.birdcounts[0]) * self.savedata.birdmultipliers[0]
		# Add SPS for chickadees (5 sps/bird)
		self.savedata.seedspersecond += (self.savedata.birdcounts[1])* 5 * self.savedata.birdmultipliers[1]
		# Add SPS for cardinals (20 sps/bird)
		self.savedata.seedspersecond += (self.savedata.birdcounts[2])* 20 * self.savedata.birdmultipliers[2]
		# Add SPS for bird4 (50 sps/bird)
		self.savedata.seedspersecond += (self.savedata.birdcounts[3])* 50 * self.savedata.birdmultipliers[3]
		# Add SPS for bird5 (150 sps/bird)
		# Add SPS for bird6 (500 sps/bird)
		# Add SPS for bird7 (2500 sps/bird)
		# Finally, multiply the SPS by the multiplier
		self.savedata.seedspersecond *= self.savedata.spsmultiplier
	
	def refreshspc(self):
		# Set SPC to the default (10)
		self.savedata.seedsperclick = 10
		# Add a hundredth of the SPS to the SPC
		self.savedata.seedsperclick += int(self.savedata.seedspersecond/100)
	
	def removeseeds(self, num):
		self.savedata.numberofseeds -= num
		
	def addsps(self):
		self.savedata.numberofseeds += self.savedata.seedspersecond * self.savedata.spsmultiplier
		
	def buybird(self,num):
		# Remove the number of seeds that the bird cost
		self.removeseeds(self.savedata.prices[num])
		# Increase the number of that type of bird by one
		self.savedata.birdcounts[num] += 1
		# Recalculate the new price
		self.savedata.prices[num] = int(self.savedata.baseprices[num] * (1.15 ** self.savedata.birdcounts[num]))
		
	def get_numberofseeds(self):
		return self.savedata.numberofseeds
		
	def get_seedsperclick(self):
		return self.savedata.seedsperclick
		
	def get_spsmultiplier(self):
		return self.savedata.spsmultiplier
		
	def get_seedspersecond(self):
		return self.savedata.seedspersecond
		
	def get_birdprice(self,num):
		return self.savedata.prices[num]
		
	def get_birdbaseprice(self,num):
		return self.savedata.baseprices[num]
		
	def get_numberofbird(self,num):
		return self.savedata.birdcounts[num]
		
	def unlockbird(self, bird):
		self.savedata.unlockedbirds += [bird]
		
	def checkunlockedbird(self, bird):
		if bird in self.savedata.unlockedbirds:
			return True
		return False
		
	def unlockupgrade(self, upgrade):
		self.savedata.unlockedupgrades += [upgrade]
		
	def checkunlockedupgrade(self, upgrade):
		if upgrade in self.savedata.unlockedupgrades:
			return True
		return False
		
	def saveGame(self):
		with open('bis15.sav', 'wb') as oldsavedata:
			pickle.dump(self.savedata, oldsavedata)