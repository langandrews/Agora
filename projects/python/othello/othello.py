'''This file will hold the game logic for Othello.
CS 108 Final Project, Fall 2014
@author: Rachel Swierenga (rms32) 
'''

#global variables/constants
black = 1
white = 2
empty = 0

class BoardState:
    '''
    This holds the state of the board.
    Invariants:
        board has 8 rows and 8 columns (0 <= x <= 7), (0 <= y <= 7)
     
    '''
    timespassed = 0
    def __init__(self, current_game = None):
        #if there's stuff on the board, leave it as is
        if current_game: 
            #This holds a player's turn
            self.player = current_game.player
     
        else:
            #the first time the file is opened, it is black's turn
            self.player = 1

            
    #accessors
    def get_player(self):
        '''This method will return whose turn it is.'''
        return self.player

    def get_times_passed(self):
        '''This will return the number of times the users have passed.'''
        return BoardState.timespassed
      


    def player_pass(self, lblTitle): 
        '''This will allow a player to pass (forfeit a turn) by adding 1 to the pass counter, switching the 'whose turn' label, and the token color.''' 
        BoardState.timespassed += 1
        self.switchPlayer(lblTitle)
    
    def blackPlayer(self):
        return self.player == 1
    
       
    def switchPlayer(self, lblTitle):
        '''This method will switch the player and set the label title text for the GUI.'''
        if self.blackPlayer():
            self.player = 2
            lblTitle.set("It is Player 2 (white)'s turn.")
        else:
            self.player = 1
            lblTitle.set("It is Player 1 (black)'s turn.")
    
