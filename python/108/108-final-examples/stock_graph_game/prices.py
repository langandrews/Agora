'''prices.py

Generates twelve prices, in a general "upward" or "downward" pattern, one price per month.
In addition, the class Usernetworth holds nearly all monetary information for the game.

@author: Quentin Baker (qrb2)
Created December 6, 2015
Last Modified December 16, 2015
'''

from random import randint
from MAINCODE import GraphGui


class Stock:
    '''This is a psudo-random graph generator. Though random spikes occur, the graph is
        upward- or downward-trending.'''
    
    def __init__(self):
        self._trend = randint(0,1)
        
    #ACCESSORS AND MUTATORS BELOW

    def get_trend(self):
        return self._trend
    
    def set_trend(self):
        self._trend = randint(0,1)
        
    def get_trend_spike(self):
        if self._trend == 1: #Upward Trending Graph
            return 1/randint(3,5)
            
        elif self._trend == 0: #Downward Trending Graph
            return -1/randint(3,5)
        
class Usernetworth:
    '''Pretty basic class, literally just stores and returns values. 
       Useful in that creating a new instance essentially resets the
       game.'''
    def __init__(self,networth=1e4,invested=0.0,netwin=1e6,tax=0.1,net_return=[1]):
        self._networth = networth
        self._netwin = netwin
        self._tax = tax
        self._invested = invested
        self._netret = net_return
    
    def get_returns(self):
        return self._netret
    
    def set_returns(self,newret):
        self._netret = newret    
    
    def get_networth(self):
        return self._networth
    
    def set_networth(self,newnet):
        self._networth = newnet
        
    def get_invested(self):
        return self._invested
    
    def set_invested(self,new_investment):
        self._invested = new_investment
        
    def get_taxrate(self):
        return self._tax
            
if __name__ == '__main__':
    print('no test code right now.')
    #test code goes here