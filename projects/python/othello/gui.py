'''This will create the board for Reversi.
CS 108 Final Project
@author: Rachel Swierenga (rms32)'''

from tkinter import *
from othello import BoardState
from Square import Square


class Board_Game:
    '''This holds the GUI to create the Othello board and the tokens.'''
    
    def __init__(self):
        window = Tk()
        window.title("Let's play Othello!")
        
        #Create an instance of BoardState
        self.bs = BoardState()
        
        self.canvas = Canvas(window, width = 600, height = 600)
        self.canvas.pack(side = LEFT)
        
        #Create a button for a user to pass on their turn 
        Button(window, text = "Forfeit turn", command = self.player_pass_button).pack()
        
        #Create a label to announce whose turn it is
        self.labeltitle = StringVar()
        Label(window, textvariable = self.labeltitle).pack() 
        self.labeltitle.set("It is Player 1 (black)'s turn.")
        
        #Create a label to announce if a spot is a valid token spot or not.
        self.valid_spot_label = StringVar()
        Label(window, textvariable = self.valid_spot_label).pack()
        self.valid_spot_label.set("")
        
        self.rows = 8
        self.columns = 8
        self.size = 75 
        
        #idea for using a nested list to create a 2D array of squares comes from Reuben Niewenhuis
        #Create a matrix of all the squares; mark each with a 0
        self.tile_matrix = [[0 for x in range(8)] for y in range(8)] 
        
        #Player 1's score
        self.score1 = Label(window, text = 'Player 1 score: ').pack()
        self.player1_result = StringVar()
        Label(window, textvariable = self.player1_result).pack()
        self.player1_result.set('2')
       
        #Player 2's score      
        self.score2 = Label(window, text = 'Player 2 score: ').pack()
        self.player2_result = StringVar()
        Label(window, textvariable = self.player2_result).pack()
        self.player2_result.set('2')
        
        #Label to announce how many times players have passed
        self.passlabel = StringVar()
        Label(window, textvariable = self.passlabel).pack() 
         
        #Button to print a matrix to the console
        Button(window, text = 'Print current matrix', command = self.print_matrix).pack(side = BOTTOM)
              
        #Button for a new game 
        Button(window, text = 'New game', command = self.defaultBoard).pack(side = BOTTOM)
        
        #Bind the mouse click with placing a token
        self.canvas.bind("<Button-1>", self.placeToken)
        
        self.defaultBoard()
        
        window.mainloop()
 
    
    def placeToken(self, event):
        '''This allows a user to add a token to the board.'''
        x = (event.x // self.size) * self.size
        xa = (event.x // self.size)
        y = (event.y // self.size) * self.size
        ya = (event.y // self.size)
        
        if self.bs.get_player() == 1:
            tokencolor = 'black'
            self.labeltitle.set("It is Player 2 (white)'s turn.")
            if self.isLegalTokenSpot(event) == True:
                Square.player1count += 1
                self.player1_result.set(Square.player1count)
            owner = 1
        else:
            tokencolor = 'white'
            self.labeltitle.set("It is Player 1 (black)'s turn.")
            if self.isLegalTokenSpot(event) == True:
                Square.player2count += 1
                self.player2_result.set(Square.player2count)
            owner = 2
                  
        #Check if this is a legal spot to place a token before placing one
        if self.isLegalTokenSpot(event) == True:
            
            #Create a token of the player's color and place it wherever the user clicks.
            self.canvas.create_oval(x, y, x + self.size, y + self.size, fill = tokencolor, tag = 'token')
            self.valid_spot_label.set("That was a valid token spot.")
            
            #Update the matrix so that it knows there's a token in that spot
            self.tile_matrix[ya][xa] = Square(xa, ya, player = owner)
            
        else:
            self.valid_spot_label.set("That was not a valid token spot. \nYour turn has been forfeited.")
        
        #Switch player so that the next token is the next player's color.        
        self.bs.switchPlayer(self.labeltitle)

        #If the board is full, end the game and show the scores; reset to new game automatically
        if (Square.player2count + Square.player1count) >= 64: 
            self.passlabel.set('Game is now over. \nScores are above.')
            self.end_game() 
        
            
    def player_pass_button(self):   
        self.bs.player_pass(self.labeltitle)
        self.passlabel.set('Number of times someone has passed: ' + str(BoardState.timespassed))
        self.valid_spot_label.set("")
        
        #if players pass a total of 6 times, the game is over.
        if BoardState.timespassed >= 6:
            self.passlabel.set('Game is now over. \nScores are above.')
            self.end_game()
     
    
    def defaultBoard(self):
        '''This method creates a default board.
        Tokens, times passed, scores, and default matrix is reset to defaults.'''
        
        #clear canvas
        self.canvas.delete('token')
        self.valid_spot_label.set("")
        self.bs = BoardState()
        
        #default scores
        Square.player1count = 2
        Square.player2count = 2
        
        #set scores to defaults
        self.player1_result.set(Square.player1count)
        self.player2_result.set(Square.player2count)
        
        #Create a grid on the canvas made of 64 rectangles
        for row in range(self.rows):
            for column in range(self.columns):
                newSquare = Square(row, column, player=0)
                self.tile_matrix[row][column] = newSquare
                x1 = (column * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill= 'dark green', activefill = 'light green')

        
        #token spots for default board
        self.canvas.create_oval(225, 225, 300, 300, fill = 'black')
        self.canvas.create_oval(300, 225, 375, 300, fill = 'white')
        self.canvas.create_oval(300, 300, 375, 375, fill = 'black')
        self.canvas.create_oval(225, 300, 300, 375, fill = 'white') 
        
        #Add these default spots to the board matrix 
        self.tile_matrix[3][3] = Square(3,3,1) 
        self.tile_matrix[4][3] = Square(4,3,2) 
        self.tile_matrix[3][4] = Square(3,4,2) 
        self.tile_matrix[4][4] = Square(4,4,1) 
        
        
    def isLegalTokenSpot(self, event):
        '''This method will return True or False, depending on if where the user clicks is a legal token placement or not.'''
        
        #Create selected row/column variables based on event variables from user
        sel_col = (event.x//self.size)
        sel_row = (event.y//self.size)
        
        #define global variables
        global col_right
        global col_left
        global row_above
        global row_below
        global diag1
        global diag2
        global diag3
        global diag4
        
        #set defaults
        col_right = False
        row_above = False
        row_below = False
        col_left = False
        diag1 = False
        diag2 = False
        diag3 = False
        diag4 = False
             
        #This checks if the selected square has already been selected. if the owner is 0, no one owns it, and you can continue through checks.
        repeat = (self.tile_matrix[sel_row][sel_col].get_player() == 0)
        
        #This checks if the selected square is in the column to the right of an existing square. 
        try:
            col_right = (self.tile_matrix[sel_row][sel_col + 1].get_player() != 0)
        except:
            if ((sel_col == 7) and (self.tile_matrix[sel_row][sel_col-1].get_player() != 0)): 
                col_right == True
            else:
                col_right == False
                
        #This checks if the selected square is in the column to the left of an existing square.       
        try:            
            col_left = (self.tile_matrix[sel_row][sel_col - 1].get_player() != 0) 
        except:
            if ((sel_col == 0) and (self.tile_matrix[sel_row][sel_col+1].get_player() != 0)):
                col_left == True
            else:
                col_left == False
        
        #This checks if the selected square is in the row above an existing square.
        try:             
            row_above = (self.tile_matrix[sel_row + 1][sel_col].get_player() != 0)
        except:
            if ((sel_row == 7) and (self.tile_matrix[sel_row-1][sel_col].get_player() != 0)):
                row_above == True 
            else:
                row_above == False
        
        #This checks if the selected square is in the row below an existing square.        
        try:
            row_below = (self.tile_matrix[sel_row - 1][sel_col].get_player() != 0)
        except:
            if ((sel_row == 0) and (self.tile_matrix[sel_row+1][sel_col].get_player() != 0)):
                row_below == True
            else:
                row_below == False
        
        #This checks if the selected square is in the diagonal to the upper right of an existing square.
        try:               
            diag1 = (self.tile_matrix[sel_row + 1][sel_col - 1].get_player() != 0)
        except:
            if ((sel_row == 0 and sel_col == 7) and (self.tile_matrix[sel_row + 1][sel_col-1].get_player() != 0)):
                diag1 == True
        
        #This checks if the selected square is in the diagonal to the lower right of an existing square.
        try:
            diag2 = (self.tile_matrix[sel_row - 1][sel_col - 1].get_player() != 0)
        except:
            if ((sel_row == 7 and sel_col == 7) and (self.tile_matrix[sel_row-1][sel_col-1].get_player() != 0)):
                diag2 == True
        
        #This checks if the selected square is in the diagonal to the lower left of an existing square.
        try:         
            diag3 = (self.tile_matrix[sel_row - 1][sel_col + 1].get_player() != 0)
        except:
            if ((sel_row == 7 and sel_col == 0) and (self.tile_matrix[sel_row-1][sel_col+1].get_player() != 0)):
                diag3 == True 
        
        #This checks if the selected square is in the diagonal to the upper left of an existing square.
        try:   
            diag4 = (self.tile_matrix[sel_row + 1][sel_col + 1].get_player() != 0)
        except:
            if ((sel_row == 0 and sel_col == 0) and (self.tile_matrix[sel_row+1][sel_col+1].get_player() != 0)):
                diag4 == True
        
        #if the square is unowned, and if there is a token next to or  diagonally across from the selected square, return true.          
        if repeat:
            if (col_right or col_left or row_above or row_below or diag1 or diag2 or diag3 or diag4):
                return True
            else:
                return False
        else:
            return False
 

    def print_matrix(self):
        '''This method will print the matrix to the console if the user requests it.'''
        lineVar = ""
        for i in range (0,8):
            for j in range (0,8):
                lineVar += self.tile_matrix[i][j].__str__()
            print (lineVar + "\n")
            lineVar = ""


    def end_game(self):
        '''This method will clear the screen.'''
        #unbind the mouse so the user can't click anymore
        self.canvas.unbind("<Button-1>")
        self.canvas.delete(ALL)
     
      
bg = Board_Game()
 
 
#testing
if __name__ == '__main__':
     
    board1 = Board_Game()
    try:
        assert board1.tile_matrix[4][3].get_player() == 2
    except:
        assert False
     
     
    print('All tests pass!')
