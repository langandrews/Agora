'''This file will hold the Square class.
CS 108 final project, Fall 2014
@author: Rachel Swierenga (rms32)'''

class Square:
    player1count = 2
    player2count = 2
    '''This class handles everything that a square on the Othello board needs to keep track of: 
    its location (an x and a y), who owns it (0 = no one, 1 = black, and 2 = white), 
    and whether it's a valid spot for a user to click on (True or False)..'''
    
    def __init__(self, x, y, player):
        '''Constructor'''
        self.x = x
        self.y = y
        self.player = player

    
    def __str__(self):    
        '''to_string method'''
        if self.get_player() == 0:
            return '-'
        if self.get_player() == 1:
            return 'b'
        if self.get_player() == 2:
            return 'w'
    
    def __repr__(self):    
        '''represent method'''
        if self.get_player() == 0:
            return '-'
        if self.get_player() == 1:
            Square.player1count += 1
            return 'b'
        if self.get_player() == 2:
            Square.player2count += 1
            return 'w'
        
         
    #accessors
    def get_x(self):
        '''This will return the x-coordinate of the location of a square.'''
        return self.x
     
    def get_y(self):
        '''This will return the y-coordinate of the location of a square.'''
        return self.y
      
    def get_player(self):
        '''This will return the owner of a square.'''
        return self.player
    
     
    #mutators 
    def setX(self, newX):
        '''This will change the x-coordinate of the location of a token.'''
        self.x = newX      
     
    def setY(self, newY):
        '''This will change the y-coordinate of the location of a token.'''
        self.y = newY
          
    def setPlayer(self, newPlayer):
        '''This will allow a token's owner (whether it is owned by Player 1 or Player 2) to change.'''
        self.player = newPlayer
        

#testing
if __name__ == '__main__':
    
    #test case 1
    sq1 = Square(150, 250, 0)
    try:
        assert sq1.get_player() == 0
        assert sq1.get_x() == 150
    except:
        assert False
    
    sq2 = Square(0, 300, 1)
    try:
        assert sq2.get_x() == 0
        assert sq2.get_y() == 300
        assert sq2.get_player() == 1
    except:
        assert False

    print('All tests pass!')
        