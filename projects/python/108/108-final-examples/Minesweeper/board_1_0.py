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
        self._board=[]
        i=-1
        while len(board)>1:
            i+=1
            self._board.append([])
            j=0
            while j<int(board[0][0]+board[0][1]):
                self._board[i].append(board.pop(1))
                j+=1
       
    def get_board(self):
        return self._board
    
    def __str__(self):
        return str(self._board)
        
if __name__ == '__main__':
    app = Board('board1.txt')
    print(app)   