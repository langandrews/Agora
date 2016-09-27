''' This file contains any miscellaneous functions
Created Fall 2015
Final Project
@author: Logan Arens (lca4)
'''
# Scientific notation formatting from http://ow.ly/UVhMb

def checkSciNote(num):
	# If number would be shorter to display using scientific notation, do so
	if num >= 10000000:
		return("{:.2e}".format(num))
	else:
		return str(num)