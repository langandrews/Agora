'''
Mouse event demo
Created Fall 2014
Updated Fall 2015
@author: smn4
@author: ajd74
'''
from tkinter import *

class Mouse_Event_Demo:
    def __init__(self, window):

#         window.geometry('+1500+100')
        
        canvas = Canvas(window, bg='white',
                        width = 300, height = 200)
        canvas.pack()
        
        canvas.bind("<Button-1>", self.processMouseEvent)
        canvas.bind("<Button-2>", self.processMouseEvent)
        canvas.bind("<Button-3>", self.processMouseEvent)

    
    def processMouseEvent(self, event):
        print("Clicked at", event.x, event.y)
        print("Position in the screen", event.x_root, event.y_root)
        print("Which button was clicked? ", event.num)

if __name__ == '__main__':
    window = Tk()
    window.title("Mouse Events")
    app = Mouse_Event_Demo(window)
    window.mainloop()