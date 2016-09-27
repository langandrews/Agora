''' This is the GUI for the game. Processing is done in player.py
Created Fall 2015
Final Project
@author: Logan Arens (lca4)
'''
# Tkinter timed stuff from http://ow.ly/UUnPj
# Pickle dumping from http://ow.ly/Vpql1
# Button command parameters from http://ow.ly/VR26u

from misc import *
import player, os.path

# Python 2/3 compatibility
try:
	from tkinter import *
except:
	from Tkinter import *

class MainWindow():
	def __init__(self):
		# Creates the window
		self.window = Tk()
		# Sets the window's title to something appropriate
		self.window.title("Bird Idle Simulator 2015")
		# Sets the window's size
		self.window.geometry("1024x720")
		# Prevents the user from resizing the window
		self.window.resizable(0,0)
		
		# Big welcome text
		Label(self.window, text="Hello, and welcome to Bird Idle Simulator 2015!", width=54, anchor=CENTER, font=("Helvetica", "24")).place(x=0,y=0)
		
		# Create the player instance
		global player
		player = player.Player()
		self.frame = 1
		
		# Create the label to display the number of seeds
		self.seedslabeltext = StringVar()
		self.updateSeeds()
		self.seedslabel = Label(self.window, textvariable=self.seedslabeltext, font=("Helvetica", "16"), width=150, anchor=W)
		self.seedslabel.place(x=0,y=630)
		
		# Create the label to display the number of seeds per click
		self.spclabeltext = StringVar()
		self.updateSPC()
		self.spclabel = Label(self.window, textvariable=self.spclabeltext, font=("Helvetica", "16"), width=150, anchor=W)
		self.spclabel.place(x=0,y=660)
		
		# Create the label to display the number of seeds per second
		self.spslabeltext = StringVar()
		self.updateSPS()
		self.spslabel = Label(self.window, textvariable=self.spslabeltext, font=("Helvetica", "16"), width=150, anchor=W)
		self.spslabel.place(x=0,y=690)
		
		# Handle finches on GUI
		self.finch1 = PhotoImage(file="img/finch.gif", format="gif -index 0")
		self.finch2 = PhotoImage(file="img/finch.gif", format="gif -index 1")
		self.finchbutton = Button(self.window, image=self.finch1, command=self.buyFinch)
		self.finchbutton.place(x=10,y=110,anchor=W)
		self.finchlabeltext = StringVar()
		self.updateNumFinches()
		self.finchlabel = Label(self.window, textvariable=self.finchlabeltext, font=("Helvetica", "12"), width=30, anchor=W)
		self.finchlabel.place(x=82,y=90)
		
		# Handle seed/clickable button
		seeds = PhotoImage(file="img/seeds.gif")
		Button(self.window, image=seeds, command=self.ClickForSeeds).place(x=512,y=360,anchor=CENTER)
		
		# Handle save button
		Button(self.window, text="Save", command=player.saveGame).place(x=0,y=0,anchor=NW)
		
		# Handle save importing checks!
		if player.checkunlockedbird("Chickadee"):
			self.drawChickadee()
		if player.checkunlockedbird("Cardinal"):
			self.drawCardinal()
		if player.checkunlockedbird("Bluejay"):
			self.drawBluejay()
			
		self.drawUpgrades()
			
		# Start the once-per-second loop
		self.updateClock()
		
		self.window.mainloop()

	def ClickForSeeds(self):
		# Give the player their current SPC, and then update the GUI
		player.clickforseeds()
		self.updateSeeds()

	def updateSeeds(self):
		# Update the GUI to reflect the current number of seeds
		self.seedslabeltext.set("Seeds: " + checkSciNote(player.get_numberofseeds()))
	
	def updateSPS(self):
		# Recalculate the SPS, and then update the GUI
		player.refreshsps()
		self.spslabeltext.set("S/sec: " + str(player.get_seedspersecond()))
		
	def updateSPC(self):
		# Recalculate the SPC, and then update the GUI
		player.refreshspc()
		self.spclabeltext.set("S/click: " + str(player.get_seedsperclick()))
		
	def updateNumFinches(self):
		# Update the GUI to reflect the current finch data
		self.finchlabeltext.set("Finches cost " + checkSciNote(player.get_birdprice(0)) + " seeds.\nYou currently have " + str(player.get_numberofbird(0)) + ".")
		
	def updateNumChickadees(self):
		# Update the GUI to reflect the current chickadee data
		self.chickadeelabeltext.set("Chickadees cost " + checkSciNote(player.get_birdprice(1)) + " seeds.\nYou currently have " + str(player.get_numberofbird(1)) + ".")
		
	def updateNumCardinals(self):
		# Update the GUI to reflect the current cardinal data
		self.cardinallabeltext.set("Cardinals cost " + checkSciNote(player.get_birdprice(2)) + " seeds.\nYou currently have " + str(player.get_numberofbird(2)) + ".")
	
	def updateNumBluejays(self):
		# Update the GUI to reflect the current bluejay data
		self.bluejaylabeltext.set("Blue Jays cost " + checkSciNote(player.get_birdprice(3)) + " seeds.\nYou currently have " + str(player.get_numberofbird(3)) + ".")
	
	def updateClock(self):
		# Check to see if the player qualifies to unlock anything
		self.checkUnlocks()
		# Check what frame we're on
		if self.frame == 1:
			self.frame += 1
			self.finchbutton.configure(image=self.finch2)
			# If the player has the bird unlocked...
			if player.checkunlockedbird("Chickadee"):
				self.chickadeebutton.configure(image=self.chickadee2)
			if player.checkunlockedbird("Cardinal"):
				self.cardinalbutton.configure(image=self.cardinal2)
			if player.checkunlockedbird("Bluejay"):
				self.bluejaybutton.configure(image=self.bluejay2)
		else:
			self.frame -= 1
			self.finchbutton.configure(image=self.finch1)
			# If the player has the bird unlocked, AND the bird's GUI elements exist...
			if player.checkunlockedbird("Chickadee"):
				self.chickadeebutton.configure(image=self.chickadee1)
			if player.checkunlockedbird("Cardinal"):
				self.cardinalbutton.configure(image=self.cardinal1)
			if player.checkunlockedbird("Bluejay"):
				self.bluejaybutton.configure(image=self.bluejay1)
		# Give the player their seeds for this second
		player.addsps()
		# Update the number of seeds on the GUI
		self.updateSeeds()
		# Wait one second before running this function again
		self.window.after(1000, self.updateClock)
		
	def checkUnlocks(self):
		# Have we unlocked Chickadees? If not, do we have enough seeds to unlock?
		if not player.checkunlockedbird("Chickadee") and player.get_numberofseeds() >= player.get_birdbaseprice(1):
			player.unlockbird("Chickadee")
			self.drawChickadee()
		# Have we unlocked Cardinals? If not, do we have enough seeds to unlock?
		if not player.checkunlockedbird("Cardinal") and player.get_numberofseeds() >= player.get_birdbaseprice(2):
			player.unlockbird("Cardinal")
			self.drawCardinal()
		# Have we unlocked Bluejays? If not, do we have enough seeds to unlock?
		if not player.checkunlockedbird("Bluejay") and player.get_numberofseeds() >= player.get_birdbaseprice(3):
			player.unlockbird("Bluejay")
			self.drawBluejay()
			
	def drawChickadee(self):
		# Handle chickadees on GUI
		self.chickadee1 = PhotoImage(file="img/chickadee.gif", format="gif -index 0")
		self.chickadee2 = PhotoImage(file="img/chickadee.gif", format="gif -index 1")
		self.chickadeebutton = Button(self.window, image=self.chickadee1, command=self.buyChickadee)
		self.chickadeebutton.place(x=10,y=180,anchor=W)
		self.chickadeelabeltext = StringVar()
		self.updateNumChickadees()
		self.chickadeelabel = Label(self.window, textvariable=self.chickadeelabeltext, font=("Helvetica", "12"), width=30, anchor=W)
		self.chickadeelabel.place(x=82,y=160)
		
	def drawCardinal(self):
		# Handle cardinals on GUI
		self.cardinal1 = PhotoImage(file="img/cardinal.gif", format="gif -index 0")
		self.cardinal2 = PhotoImage(file="img/cardinal.gif", format="gif -index 1")
		self.cardinalbutton = Button(self.window, image=self.cardinal1, command=self.buyCardinal)
		self.cardinalbutton.place(x=10,y=250,anchor=W)
		self.cardinallabeltext = StringVar()
		self.updateNumCardinals()
		self.cardinallabel = Label(self.window, textvariable=self.cardinallabeltext, font=("Helvetica", "12"), width=30, anchor=W)
		self.cardinallabel.place(x=82,y=230)
		
	def drawBluejay(self):
		# Handle bluejays on GUI
		self.bluejay1 = PhotoImage(file="img/bluejay.gif", format="gif -index 0")
		self.bluejay2 = PhotoImage(file="img/bluejay.gif", format="gif -index 1")
		self.bluejaybutton = Button(self.window, image=self.bluejay1, command=self.buyBluejay)
		self.bluejaybutton.place(x=10,y=320,anchor=W)
		self.bluejaylabeltext = StringVar()
		self.updateNumBluejays()
		self.bluejaylabel = Label(self.window, textvariable=self.bluejaylabeltext, font=("Helvetica", "12"), width=30, anchor=W)
		self.bluejaylabel.place(x=82,y=300)
		
	def drawUpgrades(self):
		# Handle cursor upgrade buttons
		if not player.checkunlockedupgrade("Cursor1"):
			self.cursorup1 = PhotoImage(file="img/cursorup1.gif")
			self.cursorup1button = Button(self.window, image=self.cursorup1, command= lambda: self.buyUpgrade("Cursor1"))
			self.cursorup1button.place(x=700,y=110,anchor=W)
		if not player.checkunlockedupgrade("Cursor2"):
			self.cursorup2 = PhotoImage(file="img/cursorup2.gif")
			self.cursorup2button = Button(self.window, image=self.cursorup2, command= lambda: self.buyUpgrade("Cursor2"))
			self.cursorup2button.place(x=770,y=110,anchor=W)
		if not player.checkunlockedupgrade("Cursor3"):
			self.cursorup3 = PhotoImage(file="img/cursorup3.gif")
			self.cursorup3button = Button(self.window, image=self.cursorup3, command= lambda: self.buyUpgrade("Cursor3"))
			self.cursorup3button.place(x=840,y=110,anchor=W)
		if not player.checkunlockedupgrade("Cursor4"):
			self.cursorup4 = PhotoImage(file="img/cursorup4.gif")
			self.cursorup4button = Button(self.window, image=self.cursorup4, command= lambda: self.buyUpgrade("Cursor4"))
			self.cursorup4button.place(x=910,y=110,anchor=W)
	
		# Handle finch upgrade buttons
		if not player.checkunlockedupgrade("Finch1"):
			self.finchup1 = PhotoImage(file="img/finchup1.gif")
			self.finchup1button = Button(self.window, image=self.finchup1, command= lambda: self.buyUpgrade("Finch1"))
			self.finchup1button.place(x=700,y=180,anchor=W)
		if not player.checkunlockedupgrade("Finch2"):
			self.finchup2 = PhotoImage(file="img/finchup2.gif")
			self.finchup2button = Button(self.window, image=self.finchup2, command= lambda: self.buyUpgrade("Finch2"))
			self.finchup2button.place(x=770,y=180,anchor=W)
		if not player.checkunlockedupgrade("Finch3"):
			self.finchup3 = PhotoImage(file="img/finchup3.gif")
			self.finchup3button = Button(self.window, image=self.finchup3, command= lambda: self.buyUpgrade("Finch3"))
			self.finchup3button.place(x=840,y=180,anchor=W)
		if not player.checkunlockedupgrade("Finch4"):
			self.finchup4 = PhotoImage(file="img/finchup4.gif")
			self.finchup4button = Button(self.window, image=self.finchup4, command= lambda: self.buyUpgrade("Finch4"))
			self.finchup4button.place(x=910,y=180,anchor=W)

	def buyFinch(self):
		# Do we have enough seeds to buy the finch?
		if player.get_birdprice(0) <= player.get_numberofseeds():
			player.buybird(0)
			self.updateNumFinches()
			self.refreshScreen()

	def buyChickadee(self):
		# If the player has enough seeds to buy a chickadee...
		if player.get_birdprice(1) <= player.get_numberofseeds():
			player.buybird(1)
			# Update GUI elements that deal with chickadees
			self.updateNumChickadees()
			# Update GUI elements that have anything to do with seeds
			self.refreshScreen()
			
	def buyCardinal(self):
		# If the player has enough seeds to buy a cardinal...
		if player.get_birdprice(2) <= player.get_numberofseeds():
			player.buybird(2)
			# Update GUI elements that deal with cardinals
			self.updateNumCardinals()
			# Update GUI elements that have anything to do with seeds
			self.refreshScreen()
			
	def buyBluejay(self):
		# If the player has enough seeds to buy a blue jay...
		if player.get_birdprice(3) <= player.get_numberofseeds():
			player.buybird(3)
			# Update GUI elements that deal with blue jays
			self.updateNumBluejays()
			# Update GUI elements that have anything to do with seeds
			self.refreshScreen()
			
	def buyUpgrade(self, upgrade):
		# Placeholder for upgrades
		print(upgrade)
			
	def refreshScreen(self):
		# Redraw the labels in the lower left (for seeds)
		self.updateSeeds()
		self.updateSPS()
		self.updateSPC()
		
	def getWindow(self):
		return self.window