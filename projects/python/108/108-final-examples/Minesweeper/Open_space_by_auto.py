'''
Opens spaces because of how the board is
Updated Fall 2015
@author: ajd74
'''


class OpenSpaceByAuto:
    def __init__(self, affected_board, unaffected_board):
        x=0
        while x<len(affected_board)*len(affected_board[0]):
            x=x+1 
            i=0
            while i<len(affected_board):
                j=0
                while j<len(affected_board[i]):
                    if affected_board[i][j]=='o' and unaffected_board[i][j]=="'":
                        if affected_board[max(i-1,0)][max(j-1,0)]!="f":
                            affected_board[max(i-1,0)][max(j-1,0)]='o'
                        if affected_board[max(i-1,0)][j]!="f":
                            affected_board[max(i-1,0)][j]='o'
                        if affected_board[max(i-1,0)][min(j+1,len(affected_board[0])-1)]!="f":
                            affected_board[max(i-1,0)][min(j+1,len(affected_board[0])-1)]='o'
                        if affected_board[i][max(j-1,0)]!="f":
                            affected_board[i][max(j-1,0)]='o'
                        if affected_board[i][j]!="f":
                            affected_board[i][j]='opened'
                        if affected_board[i][min(j+1,len(affected_board[0])-1)]!="f":
                            affected_board[i][min(j+1,len(affected_board[0])-1)]='o'
                        if affected_board[min(i+1,len(affected_board)-1)][max(j-1,0)]!="f":
                            affected_board[min(i+1,len(affected_board)-1)][max(j-1,0)]='o'
                        if affected_board[min(i+1,len(affected_board)-1)][j]!="f":
                            affected_board[min(i+1,len(affected_board)-1)][j]='o'
                        if affected_board[min(i+1,len(affected_board)-1)][min(j+1,len(affected_board[0])-1)]!="f":
                            affected_board[min(i+1,len(affected_board)-1)][min(j+1,len(affected_board[0])-1)]='o'
                    j=j+1
                i=i+1
                        
if __name__ == '__main__': 
    list_1=[["'", "'", '1', 'b', '1', '1', 'b', '1', "'"], ['1', '1', '1', '1', '1', '1', '1', '1', "'"], ['b', '1', "'", "'", "'", "'", '1', '2', '2'], ['1', '2', '1', '1', "'", '1', '2', 'b', 'b'], ["'", '1', 'b', '1', "'", '1', 'b', '3', '2'], ["'", '1', '1', '2', '2', '3', '2', '1', "'"], ["'", "'", "'", '1', 'b', 'b', '1', "'", "'"], ['1', '1', "'", '1', '2', '2', '1', "'", "'"], ['b', '1', "'", "'", "'", "'", "'", "'", "'"]]
    list_2=[["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "o", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"]]
    app = OpenSpaceByAuto(list_2,list_1)
    print(list_2)
