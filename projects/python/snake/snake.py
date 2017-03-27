'''Models a snake
Created on Dec 3, 2014
Final Project
@author: Hannah Ludema (hel7)
'''
#Imports TKinter for testing
from tkinter import *
#Imports the squares module
import squares

class Snake:
    def __init__(self,canvas):
        #Initializes the canvas
        self.canvas = canvas
        #Gets the x and y coordinates from the squares class to initialize the variables
        self.snakeSquares = squares.Squares()
        self.x_coordinates = self.snakeSquares.squares_x_list
        self.y_coordinates = self.snakeSquares.squares_y_list
        
        
    def render(self):
        #Draws out each of the squares
        for each in range(len(self.x_coordinates)):
            self.canvas.create_rectangle(self.x_coordinates[each], self.y_coordinates[each], self.x_coordinates[each]-20, self.y_coordinates[each]-20, tag = "snake", fill = "green")
            
    def move_right(self, index):
        #Adds to the x coordinate of a square to make it move right
        self.x_coordinates[index] += 20
        
    def move_left(self, index):
        #Subtracts from the x coordinate of a square to make it move left
        self.x_coordinates[index] -= 20
        
    def move_up(self, index):
        #Subtracts from the y coordinate of a square to make it move up
        self.y_coordinates[index] -= 20
        
    def move_down(self, index):
        #Adds to the y coordinate of a square to make it move down
        self.y_coordinates[index] += 20
        



if __name__ == '__main__':  
    #Creates a window for testing
    window = Tk()
    window.title("Test")   
    canvas = Canvas(window)
    canvas.pack()  
    
    #Calls the Snake class
    s = Snake(canvas)
    #Checks that the coordinates are initialized properly
    assert s.x_coordinates == [280, 260, 240, 220, 200]
    assert s.y_coordinates == [260, 260, 260, 260, 260]
    
    #Checks that move_right moves x0 right
    s.move_right(0)
    assert s.x_coordinates[0] == 300 
    
    #Checks that move_left moves x1 left
    s.move_left(1)
    assert s.x_coordinates[1] == 240 
    
    #Checks that move_up moves x2 up
    s.move_up(2)
    assert s.y_coordinates[2] == 240 
    
    #Checks that move_down moves x3 down
    s.move_down(3)
    assert s.y_coordinates[3] == 280 
    
    print("All Snake tests passed!")
    
    
    
    
    
    