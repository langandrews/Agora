
###DEPRECIATED CODE. THIS CLASS HAS BEEN MERGED INTO prices.py. ORIGINAL CODE IS BELOW FOR DOCUMENTATION PURPOSES###



'''usernet.py
@author: Quentin Baker (qrb2)

This module holds the User's net worth, and victory/loss conditions for the GUI to display.
Created December 10 2015

'''
from graphgen import GraphGui#,GameStart

class Usernetworth:
    def __init__(self,networth=1e4,netwin=1e6,loss=0):
        self._networth = networth
        self._netwin = netwin
        self._loss = loss
        
        
