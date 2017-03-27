'''
Minesweepeer Program
Updated Fall 2015
@author: ajd74
'''
import copy
from random import randint
from datetime import *
from tkinter import *
from board_2_0 import *
from BoardPrinter import *
from Open_or_Flag_space_by_click import *
from Open_space_by_auto import *
from Success_Evaluater import *

class Minesweepeer:
    def __init__(self, window):
        # Start Program
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.terminated = False
        self.homescreen()
        
    def homescreen(self):
        self.button_play = Button(self.window, text='Play', command=self.playgame)
        self.button_play.grid(row=0, column=0,)
        
    def playgame(self):    
        self.button_play.grid_remove()
        self.canvas = Canvas(self.window, bg='white', width = 450, height = 450)
        self.canvas.grid(row=1, columnspan=5)
        self._result = StringVar()
        result_label = Label(self.window, text='Time:')
        result_label.grid(row=0, column=2, sticky=E)
        result_value_label= Label(self.window, textvariable=self._result, anchor=W)
        result_value_label.grid(row=0, column=3, sticky=W)
        self.time_start=datetime.now()
        self.drawboard()
        
        
    def drawboard(self):
        self.boards=['board2_9x9.txt']
        self.board_maker= Board(self.boards[randint(0,len(self.boards)-1)])
        self.board_unaffected=self.board_maker.get_board()
        self.board_unaffected_2=copy.deepcopy(self.board_unaffected)
        self.open_or_flager=OpenOrFlagSpaceByClick(self.canvas, self.board_unaffected_2)
        while self.terminated == False:
            self.canvas.delete(ALL)
            # Board
            self.board_affected=self.open_or_flager.get_list()
            OpenSpaceByAuto(self.board_affected,self.board_unaffected)
            self.priter=BoardPrinter(self.canvas, self.board_affected, self.board_unaffected)
            # Time 
            self.time_current=datetime.now()
            self.time_difference=self.time_current-self.time_start
            self.time_diff_min=divmod(self.time_difference.days * 86400 + self.time_difference.seconds, 60)[0]
            self.time_diff_sec=divmod(self.time_difference.days * 86400 + self.time_difference.seconds, 60)[1]
            if self.time_diff_sec<10:
                self._result.set(str(self.time_diff_min)+':0'+str(self.time_diff_sec))
            else:
                self._result.set(str(self.time_diff_min)+':'+str(self.time_diff_sec))
            # Success Conditions
            self._success_evaluater=SuccessEvaluation(self.board_affected, self.board_unaffected)
            if self._success_evaluater.get_evaluation()=='Success':
                self.terminated = True
            elif self._success_evaluater.get_evaluation()=='Failure':
                self.terminated = True
            self.canvas.after(50)
            self.canvas.update()
 
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title('Minesweeper')    
    app = Minesweepeer(root)
    root.mainloop()
    print()