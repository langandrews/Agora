'''
Opens spaces because of how the board is
Updated Fall 2015
@author: ajd74
'''


class SuccessEvaluation:
    def __init__(self, affected_board, unaffected_board):
        self.affected_board = affected_board
        self.unaffected_board = unaffected_board
        self.bomb_num = self.bomb_counter()
        self.success_evaluation=''
        self.success_test()
        self.failure_test()

        
    def failure_test(self):
        i=0
        while i<len(self.affected_board):
            j=0
            while j<len(self.affected_board[i]):
                if self.affected_board[i][j]=='o' and self.unaffected_board[i][j]=="b":
                    self.success_evaluation='Failure'
                j=j+1
            i=i+1
            
    def success_test(self):
        count=0
        i=0
        while i<len(self.affected_board):
            j=0
            while j<len(self.affected_board[i]):
                if self.unaffected_board[i][j]!="b" and (self.affected_board[i][j]=='o' or self.affected_board[i][j]=='opened'):
                    count = count+1
                j=j+1
            i=i+1   
        space_num=len(self.affected_board)*len(self.affected_board[0])
        if count==space_num-self.bomb_num:
            self.success_evaluation='Success'
            
    def bomb_counter(self):
        return 10
                                
    def get_evaluation(self):
        return self.success_evaluation
                           
if __name__ == '__main__': 
    list_1=[["'", "'", '1', 'b', '1', '1', 'b', '1', "'"], ['1', '1', '1', '1', '1', '1', '1', '1', "'"], ['b', '1', "'", "'", "'", "'", '1', '2', '2'], ['1', '2', '1', '1', "'", '1', '2', 'b', 'b'], ["'", '1', 'b', '1', "'", '1', 'b', '3', '2'], ["'", '1', '1', '2', '2', '3', '2', '1', "'"], ["'", "'", "'", '1', 'b', 'b', '1', "'", "'"], ['1', '1', "'", '1', '2', '2', '1', "'", "'"], ['b', '1', "'", "'", "'", "'", "'", "'", "'"]]
    list_2=[["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "o", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"]]
    app = SuccessEvaluation(list_2,list_1)
    print(app.get_evaluation())