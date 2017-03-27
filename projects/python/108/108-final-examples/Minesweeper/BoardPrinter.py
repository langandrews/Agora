'''
GUI controller for a particle simulation
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
'''

from tkinter import *


class BoardPrinter:
    ''' Prints the board simulator '''
    
    def __init__(self, canvas, affected_board, unaffected_board):
        self.canvas = canvas
        self.canvas_width=int(canvas["width"])
        self.canvas_height=int(canvas["height"])
        self.column_num=len(unaffected_board)
        self.row_num=len(unaffected_board[0])
        self.unit_width=self.canvas_width//self.column_num
        self.unit_height=self.canvas_height//self.row_num
        column=0
        while column < self.column_num:
            row=0
            while row < self.row_num:
                self.add_unit(x = self.unit_width*column, y = self.unit_height*row, width = self.unit_width, height = self.unit_height, color1 = affected_board[column][row], color2 = unaffected_board[column][row])
                row=row+1
            column=column+1

#         self.add_unit(color1="o", color2="1")
#         self.add_unit(50, color1="o", color2="2")
#         self.add_unit(100, color1="o", color2="3")
#         self.add_unit(150, color1="o", color2="4")
#         self.add_unit(200, color1="o", color2="5")
#         self.add_unit(250, color1="o", color2="6")
#         self.add_unit(300, color1="o", color2="7")
#         self.add_unit(350, color1="o", color2="8")
#         self.add_unit(400, color1="o", color2="b")
#         self.add_unit(0,50, color1="o", color2="'")
#         self.add_unit(50,50, color1="'", color2="'")
#         self.add_unit(100,50, color1="f", color2="'")
#         self.add_unit(150,50, color1="q", color2="'")
        
        
    def add_unit(self, x = 0, y = 0, width = 50, height = 50, color1 = "'", color2 = "'"):
        '''
        Constructor
        color1 is ["'", "f", "q", "o", 'opened']
        color2 is ["'", 'b', '1', '2', '3', '4', '5', '6', '7', '8']
        '''
        c_x=x+width//2
        c_y=y+height//2
        
        if color1=="'":
            self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = 'white')
        elif color1=='f':
            self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = 'white')
            self.canvas.create_polygon(10+x,35+y,10+x,40+y,40+x,40+y,40+x,35+y,33+x,35+y,33+x,30+y,26+x,30+y,26+x,20+y,24+x,20+y,24+x,30+y,17+x,30+y,17+x,35+y, fill = 'black')
            self.canvas.create_polygon(26+x,25+y,26+x,10+y,15+x,17+y, fill='red')
        elif color1=='q':
            self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = 'white')
            self.canvas.create_polygon(19+x,9+y,29+x,9+y,29+x,10+y,30+x,10+y,30+x,11+y,31+x,11+y,31+x,12+y,32+x,12+y,32+x,14+y,33+x,14+y,33+x,19+y,32+x,19+y,32+x,21+y,31+x,21+y,31+x,22+y,30+x,22+y,30+x,23+y,29+x,23+y,29+x,24+y,28+x,24+y,28+x,25+y,27+x,25+y,27+x,30+y,23+x,30+y,23+x,22+y,24+x,24+y,24+x,22+y,25+x,22+y,25+x,21+y,26+x,21+y,26+x,20+y,27+x,20+y,27+x,19+y,28+x,19+y,28+x,18+y,29+x,18+y,29+x,15+y,28+x,15+y,28+x,14+y,27+x,14+y,27+x,13+y,20+x,13+y,20+x,14+y,19+x,14+y,19+x,15+y,18+x,15+y,18+x,17+y,15+x,17+y,15+x,13+y,16+x,13+y,16+x,12+y,17+x,12+y,17+x,11+y,18+x,11+y,18+x,10+y,19+x,10+y, fill = 'black')
            self.canvas.create_polygon(27+x,33+y,23+x,33+y,23+x,38+y,27+x,38+y, fill = 'black')
        elif color1=='o' or color1=='opened':
            if color2=="'":
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
            elif color2=="b":
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                size_x=3*width//50
                size_y=3*height//50
                self.canvas.create_polygon(c_x-3*size_x,c_y-3*size_y,c_x-3*size_x,c_y+3*size_y,c_x+3*size_x,c_y+3*size_y,c_x+3*size_x,c_y-3*size_y, fill = 'Black')
                self.canvas.create_polygon(c_x-size_x//2,c_y-6*size_y,c_x-size_x//2,c_y+6*size_y,c_x+size_x//2,c_y+6*size_y,c_x+size_x//2,c_y-6*size_y, fill = 'Black')
                self.canvas.create_polygon(c_x-6*size_x,c_y-size_y//2,c_x-6*size_x,c_y+size_y//2,c_x+6*size_x,c_y+size_y//2,c_x+6*size_x,c_y-size_y//2, fill = 'Black')
                self.canvas.create_polygon(c_x-4*size_x,c_y-2*size_y,c_x-4*size_x,c_y+2*size_y,c_x+4*size_x,c_y+2*size_y,c_x+4*size_x,c_y-2*size_y, fill = 'Black')
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x-2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y,c_x+2*size_x,c_y-4*size_y, fill = 'Black')
                self.canvas.create_polygon(c_x-4*size_x,c_y-3*size_y,c_x-4*size_x,c_y-4*size_y,c_x-3*size_x,c_y-4*size_y,c_x-3*size_x,c_y-3*size_y, fill = 'Black')
                self.canvas.create_polygon(c_x-4*size_x,c_y+3*size_y,c_x-4*size_x,c_y+4*size_y,c_x-3*size_x,c_y+4*size_y,c_x-3*size_x,c_y+3*size_y, fill = 'Black')
                self.canvas.create_polygon(c_x+4*size_x,c_y+3*size_y,c_x+4*size_x,c_y+4*size_y,c_x+3*size_x,c_y+4*size_y,c_x+3*size_x,c_y+3*size_y, fill = 'Black')
                self.canvas.create_polygon(c_x+4*size_x,c_y-3*size_y,c_x+4*size_x,c_y-4*size_y,c_x+3*size_x,c_y-4*size_y,c_x+3*size_x,c_y-3*size_y, fill = 'Black')
            elif color2=='1':
                color3='#000066'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                self.canvas.create_polygon(c_x-4*size_x,c_y+4*size_y,c_x+4*size_x,c_y+4*size_y,c_x+4*size_x,c_y+3*size_y,c_x-4*size_x,c_y+3*size_y, fill = color3)    
                self.canvas.create_polygon(c_x-3*size_x,c_y-4*size_y,c_x,c_y-4*size_y,c_x,c_y-3*size_y,c_x-3*size_x,c_y-3*size_y, fill = color3)
                self.canvas.create_polygon(c_x,c_y-4*size_y,c_x+1*size_x,c_y-4*size_y,c_x+1*size_x,c_y+4*size_y,c_x,c_y+4*size_y, fill = color3)
            elif color2=='2':
                color3='#330066'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                # bottom
                self.canvas.create_polygon(c_x-2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+3*size_y,c_x-2*size_x,c_y+3*size_y, fill = color3)    
                # top
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-3*size_y,c_x-2*size_x,c_y-3*size_y, fill = color3)
                # middle
                self.canvas.create_polygon(c_x-2*size_x,c_y,c_x+2*size_x,c_y,c_x+2*size_x,c_y-1*size_y,c_x-2*size_x,c_y-1*size_y, fill = color3)
                # top right
                self.canvas.create_polygon(c_x+2*size_x,c_y-4*size_y,c_x+size_x,c_y-4*size_y,c_x+size_x,c_y,c_x+2*size_x,c_y, fill = color3)
                # bottom left
                self.canvas.create_polygon(c_x-2*size_x,c_y-size_y,c_x-size_x,c_y-size_y,c_x-size_x,c_y+4*size_y,c_x-2*size_x,c_y+4*size_y, fill = color3)
            elif color2=='3':
                color3='#660066'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                # bottom
                self.canvas.create_polygon(c_x-2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+3*size_y,c_x-2*size_x,c_y+3*size_y, fill = color3)    
                # top
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-3*size_y,c_x-2*size_x,c_y-3*size_y, fill = color3)
                # middle
                self.canvas.create_polygon(c_x-2*size_x,c_y,c_x+2*size_x,c_y,c_x+2*size_x,c_y-1*size_y,c_x-2*size_x,c_y-1*size_y, fill = color3)
                # top right
                self.canvas.create_polygon(c_x+2*size_x,c_y-4*size_y,c_x+size_x,c_y-4*size_y,c_x+size_x,c_y,c_x+2*size_x,c_y, fill = color3)
                # bottom right
                self.canvas.create_polygon(c_x+2*size_x,c_y-size_y,c_x+size_x,c_y-size_y,c_x+size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y, fill = color3)
            elif color2=='4':
                color3='#660033'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                # middle
                self.canvas.create_polygon(c_x-2*size_x,c_y,c_x+2*size_x,c_y,c_x+2*size_x,c_y-1*size_y,c_x-2*size_x,c_y-1*size_y, fill = color3)
                # top left
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x-size_x,c_y-4*size_y,c_x-size_x,c_y,c_x-2*size_x,c_y, fill = color3)
                # top right
                self.canvas.create_polygon(c_x+2*size_x,c_y-4*size_y,c_x+size_x,c_y-4*size_y,c_x+size_x,c_y,c_x+2*size_x,c_y, fill = color3)
                # bottom right
                self.canvas.create_polygon(c_x+2*size_x,c_y-size_y,c_x+size_x,c_y-size_y,c_x+size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y, fill = color3)
            elif color2=='5':
                color3='#660000'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                # bottom
                self.canvas.create_polygon(c_x-2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+3*size_y,c_x-2*size_x,c_y+3*size_y, fill = color3)    
                # top
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-3*size_y,c_x-2*size_x,c_y-3*size_y, fill = color3)
                # middle
                self.canvas.create_polygon(c_x-2*size_x,c_y,c_x+2*size_x,c_y,c_x+2*size_x,c_y-1*size_y,c_x-2*size_x,c_y-1*size_y, fill = color3)
                # top left
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x-size_x,c_y-4*size_y,c_x-size_x,c_y,c_x-2*size_x,c_y, fill = color3)
                # bottom right
                self.canvas.create_polygon(c_x+2*size_x,c_y-size_y,c_x+size_x,c_y-size_y,c_x+size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y, fill = color3)
            elif color2=='6':
                color3='#990000'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                # bottom
                self.canvas.create_polygon(c_x-2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+3*size_y,c_x-2*size_x,c_y+3*size_y, fill = color3)    
                # top
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-3*size_y,c_x-2*size_x,c_y-3*size_y, fill = color3)
                # middle
                self.canvas.create_polygon(c_x-2*size_x,c_y,c_x+2*size_x,c_y,c_x+2*size_x,c_y-1*size_y,c_x-2*size_x,c_y-1*size_y, fill = color3)
                # top left
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x-size_x,c_y-4*size_y,c_x-size_x,c_y,c_x-2*size_x,c_y, fill = color3)
                # bottom left
                self.canvas.create_polygon(c_x-2*size_x,c_y-size_y,c_x-size_x,c_y-size_y,c_x-size_x,c_y+4*size_y,c_x-2*size_x,c_y+4*size_y, fill = color3)
                # bottom right
                self.canvas.create_polygon(c_x+2*size_x,c_y-size_y,c_x+size_x,c_y-size_y,c_x+size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y, fill = color3)
            elif color2=='7':
                color3='#CC0000'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                # top
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-3*size_y,c_x-2*size_x,c_y-3*size_y, fill = color3)
                # top right
                self.canvas.create_polygon(c_x+2*size_x,c_y-4*size_y,c_x+size_x,c_y-4*size_y,c_x+size_x,c_y,c_x+2*size_x,c_y, fill = color3)
                # bottom right
                self.canvas.create_polygon(c_x+2*size_x,c_y-size_y,c_x+size_x,c_y-size_y,c_x+size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y, fill = color3)
            elif color2=='8':
                color3='#FF0000'
                size_x=width//10
                size_y=height//10
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = '#7F7F7F')
                # bottom
                self.canvas.create_polygon(c_x-2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y,c_x+2*size_x,c_y+3*size_y,c_x-2*size_x,c_y+3*size_y, fill = color3)    
                # top
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-4*size_y,c_x+2*size_x,c_y-3*size_y,c_x-2*size_x,c_y-3*size_y, fill = color3)
                # middle
                self.canvas.create_polygon(c_x-2*size_x,c_y,c_x+2*size_x,c_y,c_x+2*size_x,c_y-1*size_y,c_x-2*size_x,c_y-1*size_y, fill = color3)
                # top left
                self.canvas.create_polygon(c_x-2*size_x,c_y-4*size_y,c_x-size_x,c_y-4*size_y,c_x-size_x,c_y,c_x-2*size_x,c_y, fill = color3)
                # top right
                self.canvas.create_polygon(c_x+2*size_x,c_y-4*size_y,c_x+size_x,c_y-4*size_y,c_x+size_x,c_y,c_x+2*size_x,c_y, fill = color3)
                # bottom left
                self.canvas.create_polygon(c_x-2*size_x,c_y-size_y,c_x-size_x,c_y-size_y,c_x-size_x,c_y+4*size_y,c_x-2*size_x,c_y+4*size_y, fill = color3)
                # bottom right
                self.canvas.create_polygon(c_x+2*size_x,c_y-size_y,c_x+size_x,c_y-size_y,c_x+size_x,c_y+4*size_y,c_x+2*size_x,c_y+4*size_y, fill = color3)
            else:
                self.canvas.create_polygon(x,y,x+width,y,x+width,y+height,x,y+height, outline='black', fill = 'black')

if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')
    canvas = Canvas(root, bg='white', width = 450, height = 450)
    canvas.pack()
    unboard=[["'", "'", '1', 'b', '1', '1', 'b', '1', "'"], ['1', '1', '1', '1', '1', '1', '1', '1', "'"], ['b', '1', "'", "'", "'", "'", '1', '2', '2'], ['1', '2', '1', '1', "'", '1', '2', 'b', 'b'], ["'", '1', 'b', '1', "'", '1', 'b', '3', '2'], ["'", '1', '1', '2', '2', '3', '2', '1', "'"], ["'", "'", "'", '1', 'b', 'b', '1', "'", "'"], ['1', '1', "'", '1', '2', '2', '1', "'", "'"], ['b', '1', "'", "'", "'", "'", "'", "'", "'"]]
    board=[['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o']]
    app = BoardPrinter(canvas,board,unboard)
    root.mainloop()
    
