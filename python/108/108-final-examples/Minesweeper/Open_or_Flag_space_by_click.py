'''
Opens or flags spaces by clicking with a mouse
Updated Fall 2015
@author: ajd74
'''
from tkinter import *

class OpenOrFlagSpaceByClick:
    def __init__(self, canvas, list1):
        self._list=list1
        self._box_num_x=len(list1)
        self._box_size_x=int(canvas["width"])/self._box_num_x
        self._box_num_y=len(list1[0])
        self._box_size_y=int(canvas["height"])/self._box_num_y
        self.reset_list()
        
        canvas.bind("<Button-1>", self.openSpace)
        canvas.bind("<Button-3>", self.flagSpace)
    
    def openSpace(self, event):
        x_selected=int(event.x/self._box_size_x)
        y_selected=int(event.y/self._box_size_y)
        self._box_selected=(x_selected,y_selected)
        if self._list[x_selected][y_selected]=="o":
            pass
        elif self._list[x_selected][y_selected]=="f":
            pass
        elif self._list[x_selected][y_selected]=="q":
            self._list[x_selected][y_selected]="o"
        elif self._list[x_selected][y_selected]=="'":
            self._list[x_selected][y_selected]="o"
    
    def flagSpace(self, event):
        x_selected=int(event.x/self._box_size_x)
        y_selected=int(event.y/self._box_size_y)
        self._box_selected=(x_selected,y_selected)
        if self._list[x_selected][y_selected]=="o":
            pass
        elif self._list[x_selected][y_selected]=="f":
            self._list[x_selected][y_selected]='q'
        elif self._list[x_selected][y_selected]=="q":
            self._list[x_selected][y_selected]="'"
        elif self._list[x_selected][y_selected]=="'":
            self._list[x_selected][y_selected]="f"
    
    def reset_list(self):
        i=0
        while i<self._box_num_x:
            j=0
            while j < self._box_num_y:
                self._list[i][j]="'"
                j=j+1
            i=i+1
            
    def get_list(self):
        return self._list
    
    def __str__(self):
        return str(self._list)

if __name__ == '__main__':
    window = Tk()
    window.title("Mouse Events")
    canvas = Canvas(window, bg='white', width = 450, height = 450)
    canvas.pack()
    list1=[["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"], ["'", "'", "'", "'", "'", "'", "'", "'", "'"]]
    app = OpenOrFlagSpaceByClick(canvas,list1)
    window.mainloop()
    print(app._list)