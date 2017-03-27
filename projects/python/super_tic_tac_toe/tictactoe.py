'''
Created on Dec 2, 2014
This is all the different classes involved in Super Tic Tac Toe other than the Driver
@author: Ethan


Note: It has been brought to my attention that the following code:

import itertools
for i, j in itertools.product(range(x), range(y)):
    # Stuff...
    
...is a much neater looking alternative to nested for loops, which this program uses CONSTANTLY
So I might switch that later on if I have time
'''
try:
    from random import randint
    from tkinter import PhotoImage
except ImportError as err:
    print('Import Error!',err)


#Debugging: Set up a custom game
def test_game(row0, row1, row2):
    grid = Grid()
    for x in range(3):
        grid.get_slot(0,x).set(row0[x])
        grid.get_slot(1,x).set(row1[x])
        grid.get_slot(2,x).set(row2[x])
    return grid

class Slot:
    '''
    The most basic unit of the game: a single space in a tic-tac-toe grid.
    Can be one of three values: x, o, or n.
    '''
    def __init__(self):
        self._content = 'n'
        
    def set(self, content):
        if content == 'x' or content == 'o' or content =='n':
            self._content = content 
        else:
            raise ValueError('Set content error: Invalid content')
        
    def get(self):
        return self._content
    
    def __str__(self):
        if self._content == 'n':
            return '[ ]'
        else:
            return '['+self._content+']'
    
class Grid:
    def __init__(self):
        self._slots = [[Slot() for x in range(3)] for x in range(3)]
        self._finished = False
        self._winner = 'n'
        
    def __str__(self):
        temp = ''
        for x in range(3):
            for y in range(3):
                temp = temp+'['+self._slots[x][y].get()+']'
            temp = temp + '\n'
        if self._finished:
            temp += self._winner+' wins!'
        return temp
            
    def checkwin(self):
        #Check the rows and columns
        for i in range(3):
            #Rows first
            if self._slots[i][0].get() == self._slots[i][1].get() == self._slots[i][2].get():
                if self._slots[i][0].get() != 'n':
                    self._winner = self._slots[i][0].get()
                    self._finished = True
            #Don't forget those sexy columns
            if self._slots[0][i].get() == self._slots[1][i].get() == self._slots[2][i].get():
                if self._slots[0][i].get() != 'n':
                    self._winner = self._slots[0][i].get()
                    self._finished = True
        #Finally, the diagonals
        if self._slots[0][0].get() == self._slots[1][1].get() == self._slots[2][2].get():
            if self._slots[0][0].get() != 'n':
                self._winner = self._slots[0][0].get()
                self._finished = True
        if self._slots[0][2].get() == self._slots[1][1].get() == self._slots[2][0].get():
            if self._slots[0][2].get() != 'n':
                self._winner = self._slots[0][2].get()
                self._finished = True
        #Just kidding. Still have to check if the game is a draw
        draw = True
        for i in range(3):
            for j in range(3):
                if self._slots[i][j].get() == 'n':
                    draw = False
                    break
        if draw:
            self._winner = 'n'
            self._finished = True
    
    def get_slot(self, row, col):
        if (0 <= row < 3) and (0 <= col < 3):
            return self._slots[row][col]
        
    def set_slot(self, row, col, value):
        if (0 <= row < 3) and (0 <= col <= 3):
            try:
                self._slots[row][col].set(value)
            except ValueError as err:
                print(err)
    
    def get_winner(self):
        return self._winner
        
    def is_finished(self):
        if self._finished:
            return True
        else:
            return False
        
    def reset(self):
        self._finished = False
        self._winner = 'n'
        self._winning_slots = []
        for i in range(3):
            for j in range(3):
                self._slots[i][j].set('n')
        
    def random_game(self):
        '''
        Debugging only. Unless I end up using this as the AI (God forbid)
        '''
        current_player = 'x'
        self.reset()
        while not self._finished:
            tempcoords = [randint(0,2), randint(0,2)]
            while self._slots[tempcoords[0]][tempcoords[1]].get() != 'n':
                tempcoords = [randint(0,2), randint(0,2)]
            self._slots[tempcoords[0]][tempcoords[1]].set(current_player)
            if current_player == 'x':
                current_player = 'o'
            else:
                current_player = 'x'
            self.checkwin()
        print(str(self))
        print(self._winner+' wins\n')
        print('Winning slots: '+str(self._winning_slots))
        
        
class SuperGrid(Grid):
    def __init__(self):
        self._grids = [[Grid() for x in range(3)] for x in range(3)]
        self._slots = [[Slot() for x in range(3)] for x in range(3)]
        self._finished = False
        self._winner = 'n'
        self._playable_slot = 'all'
        
    def get_grid(self, row, column):
        return self._grids[row][column] 
    
    def get_playable_slot(self):
        return self._playable_slot
        
    def checkwin(self):
        for i in range(3):
            for j in range(3):
                self._grids[i][j].checkwin()
                if self._grids[i][j].is_finished():
                    self._slots[i][j].set(self._grids[i][j].get_winner())
        super().checkwin()
        
    def reset(self):
        self._grids = [[Grid() for x in range(3)] for x in range(3)]
        self._slots = [[Slot() for x in range(3)] for x in range(3)]
        self._finished = False
        self._winner = 'n'
        self._playable_slot = 'all'
                    
    def move(self, team, gridsquare, slot):
        if self._playable_slot == 'all' or gridsquare == self._playable_slot:
            if self._grids[gridsquare[0]][gridsquare[1]].get_slot(slot[0], slot[1]).get() == 'n':
                self._grids[gridsquare[0]][gridsquare[1]].set_slot(slot[0], slot[1], team)
                self._grids[gridsquare[0]][gridsquare[1]].checkwin()
                if self._grids[slot[0]][slot[1]].is_finished():
                    self._playable_slot = 'all'
                else:
                    self._playable_slot = slot
                self.checkwin()
            else:
                raise Exception('Invalid move.')
        else:
            raise Exception('Invalid Move')

#ERRYBODY LOVES TESTING RIGHT GUYS? ...right guys?
if __name__ == '__main__':
    grid = Grid()
    print(str(grid))
    while True:
        user_choice = input('Would you like to run a randomized game? (y/n): ')
        if user_choice == 'y':
            grid.random_game()
        else:
            break
