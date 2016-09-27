'''
Compiles boards for Minesweeper
Created Fall, 2015
@author: ajd74
'''

class Board:
    

    def __init__(self, doc):
        '''
        Constructor
        '''
        with open(doc)as f:
            board=f.read().split()
        f.close()
        self._board=[]
        self._bomb_num=int(board[0][6]+board[0][7])
        # makes lists for the columns
        i=0
        while i<int(board[0][0]+board[0][1]):
            i+=1
            self._board.append([])
        
        # add the values to the lists
        while len(board)>1:
            self._board[0].append(board.pop(1)) 
            self._board[1].append(board.pop(1))
            self._board[2].append(board.pop(1))
            self._board[3].append(board.pop(1))
            self._board[4].append(board.pop(1))
            self._board[5].append(board.pop(1))
            self._board[6].append(board.pop(1))
            self._board[7].append(board.pop(1))
            self._board[8].append(board.pop(1))
       
    def get_board(self):
        return self._board
    
    def get_bomb_num(self):
        return self._bomb_num
    
    def __str__(self):
        return str(self._board)
        
if __name__ == '__main__':
    app = Board('board_test.txt')
    print(app)   