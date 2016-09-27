'''
Created on Dec 3, 2014
This is the Artificial Intelligence that can play tic-tac-toe (hopefully decently)
@author: Ethan Giles (etg5)
'''
try:
    from tictactoe import *
    from random import randint, shuffle
except ImportError as err:
    print('Import Error!',err)

def get_turn(grid):
    '''
    This function returns either x or o depending on who's turn it is
    '''
    num_x = 0
    num_o = 0
    for x in range(3):
        for y in range(3):
            if grid.get_slot(x,y).get() == 'x':
                num_x += 1
            if grid.get_slot(x,y).get() == 'o':
                num_o += 1
    if num_x == num_o:
        return 'x'
    else:
        return 'o'

def move(grid, team):
    coords = process_grid(grid, team)
    if grid.get_slot(coords[0], coords[1]).get() == 'n':
        grid.set_slot(coords[0], coords[1], team)
    else:
        print('Error! Program recommended an illegal move!\nrow: %i\ncol: %i' % (coords[0], coords[1]))

def process_grid(grid, team):
    '''
    AI Basic Structure:
    
    Step 1 - Convert the grid into strings for each row, column and diagonal
    There was a step 2 here but I ended up getting rid of it later on and I don't feel like changing all the steps.
    Step 3 - Check for imminent wins (spaces that would win the game instantly if the AI claimed them)
    Step 4 - Check for imminent losses (spaces which, if not blocked this turn, would allow the opponent to win)
    Step 5 - Check for rows or columns that have one friendly square and no enemy squares
    Otherwise - Pick a random empty square
    '''
    
    #Read in the grid as rows and columns (and diagonals)
    rows = []
    cols = []
    turn = 0
    for x in range(3):
        rows.append(grid.get_slot(x,0).get()+grid.get_slot(x,1).get()+grid.get_slot(x,2).get())
        cols.append(grid.get_slot(0,x).get()+grid.get_slot(1,x).get()+grid.get_slot(2,x).get())
        turn += rows[x].count('x')
        turn += rows[x].count('o')
    diags = [
            (grid.get_slot(0,0).get()+grid.get_slot(1,1).get()+grid.get_slot(2,2).get()),
            (grid.get_slot(0,2).get()+grid.get_slot(1,1).get()+grid.get_slot(2,0).get())
            ]
        
    
    #Define who the opponent is
    if team == 'x':
        opp = 'o'
    else:
        opp = 'x'
        
    '''
    Scanning For Imminent Wins
    
    The program will check each possible combination of 3 slots
    If the line has 1 empty space (n) and 2 friendly spaces, the computer claims the empty space and ends its turn
    '''
    #Rows first, then columns
    for x in range(3):
        if 'n' in rows[x] and rows[x].count(team) == 2:
            return [x,rows[x].find('n')]
        if 'n' in cols[x] and cols[x].count(team) == 2:
            return [cols[x].find('n'),x]
    #Now those annoying diags...
    if 'n' in diags[0] and diags[0].count(team) == 2:
        return [diags[0].find('n'),diags[0].find('n')]
    if 'n' in diags[1] and diags[1].count(team) == 2:
        if diags[1].find('n') == 0:
            coords = [0,2]
        if diags[1].find('n') == 1:
            coords = [1,1]
        if diags[1].find('n') == 2:
            coords = [2,0]
        return [coords[0],coords[1]]
    
    '''
    Scanning For Imminent Losses
    
    Basically the same as last time, but instead of checking friendly squares it checks enemy squares
    Yes, this could be optimized. It's on my todo list.
    '''
    for x in range(3):
        if 'n' in rows[x] and rows[x].count(opp) == 2:
            return [x,rows[x].find('n')]
        if 'n' in cols[x] and cols[x].count(opp) == 2:
            return [cols[x].find('n'),x]
    #Now those annoying diags...
    if 'n' in diags[0] and diags[0].count(opp) == 2:
        return [diags[0].find('n'),diags[0].find('n')]
    if 'n' in diags[1] and diags[1].count(opp) == 2:
        if diags[1].find('n') == 0:
            coords = [0,2]
        if diags[1].find('n') == 1:
            coords = [1,1]
        if diags[1].find('n') == 2:
            coords = [2,0]
        return [coords[0],coords[1]]

    '''
    If the game is in its early stages, the program will take specific measures to not be forked
    '''
    if turn == 0:
        list = [(0,0), (0,2), (2,0), (2,2)]
        shuffle(list)
        return list[0]
        
    if turn == 1:
        if grid.get_slot(1,1).get() == 'n':
            return [1,1]
        else:
            list = [(0,0), (0,2), (2,0), (2,2)]
            shuffle(list)
            return list[0]
        
    if turn == 3:
        if (grid.get_slot(0,0).get() == grid.get_slot(2,2).get() == opp) or (grid.get_slot(0,2).get() == grid.get_slot(2,0).get() == opp):
            list = [(0,1),(1,0),(1,2),(2,1)]
            shuffle(list)
            return list[0]
        
    '''
    If there are no immediate threats, the program will look for a row with 2 n's and 1 friendly
    For the sake of variance, all viable moves will be accumulated in a list and then one will be chosen randomly
    '''
    possibles = []
    for x in range(3):
        if team in rows[x] and rows[x].count('n') == 2:
            for y in range(3):
                if rows[x][y] == 'n':
                    possibles.append([x,y])
        if team in cols[x] and cols[x].count('n') == 2:
            for y in range(3):
                if cols[x][y] == 'n':
                    possibles.append([y,x])
    if team in diags[0] and diags[0].count('n') == 2:
        for y in range(3):
            if diags[0][y] == 'n':
                possibles.append([y,y])
    if team in diags[1] and diags[1].count('n') == 2:
        if diags[1][0] == 'n':
            possibles.append([0,2])
        if diags[1][1] == 'n':
            possibles.append([1,1])
        if diags[1][2] == 'n':
            possibles.append([2,0])
    #Pick one of the possible options
    if len(possibles) > 0:
        shuffle(possibles)
        #Corners are better
        #Then middle square, then the other ones
        for option in possibles:
            if option == [0,0] or option == [0,2] or option == [2,0] or option == [2,2]:
                return option
        if [1,1] in possibles:
            return [1,1]
        return possibles[0]
            
    '''
    Otherwise, just pick a random empty square
    '''
    randslot = [randint(0,2), randint(0,2)]
    while grid.get_slot(randslot[0], randslot[1]).get() != 'n':
        randslot = [randint(0,2), randint(0,2)]
    return randslot
       
#Testing is my favorite thing evaar
if __name__ == '__main__':
    '''
    Okay so this test allows me to create a board configuration for the computer to play the next turn against
    Each row has to be a string of 3 characters that are either x, o or n
    Make sure there aren't more o's than x's because even though the computer could handle it, it won't happen in a real game
    '''
    row0 = input('Row 0: ')
    row1 = input('Row 1: ')
    row2 = input('Row 2: ')
    grid = test_game(row0, row1, row2)
    print(grid)
    team = get_turn(grid)
    move(grid, team)
    grid.update()
    print(grid)
    