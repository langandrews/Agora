''' This is the player's savedata!
This should be accessed by, AND ONLY BY, player.py
player.py has the ability to modify, save, and load this.
Created Fall 2015
Final Project
@author: Logan Arens (lca4)
'''
class Data():
	def __init__(self):
		# These are all the default values for a new save.
		self.numberofseeds = 0
		self.seedsperclick = 10
		self.spsmultiplier = 1
		self.spcmultiplier = 1
		self.seedspersecond = 0
		# Finch, Chickadee, Cardinal, Bluejay, Bird5, Bird6, Bird7
		self.baseprices = [250, 1500, 5000, 30000, 100000, 2500000, 1000000000]
		self.prices = [250, 1500, 5000, 30000, 100000, 2500000, 1000000000]
		self.birdcounts = [0, 0, 0, 0, 0, 0, 0]
		self.birdmultipliers = [1, 1, 1, 1, 1, 1, 1]
		self.unlockedbirds = ["Finch"]
		self.unlockedupgrades = []