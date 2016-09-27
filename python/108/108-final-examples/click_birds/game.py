''' All this does is launch the GUI so the game can start.
Created Fall 2015
Final Project
@author: Logan Arens (lca4)
'''

import gui

# Python 2/3 compatibility
try:
	from tkinter import *
except:
	from Tkinter import *

# Creates the game window
window = gui.MainWindow().getWindow()
