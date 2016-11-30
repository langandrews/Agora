'''Models the food
Created on Dec 3, 2014
Final Project
@author: Hannah Ludema (hel7)
'''
#Imports TKinter for testing
from tkinter import *
#Imports the random module
import random

class Food:
    def __init__(self, canvas):
        #Initializes the canvas instance variable
        self.canvas = canvas 
        
        #Creates random coordinates for the food
        self.x = random.randint(20,600)
        self.y = random.randint(20,500)
        
        #Makes sure the food is in the proper spot do the snake can get it
        if self.x % 20 != 0:
            self.x = self.x - (self.x % 20)   
        if self.y % 20 != 0:
            self.y = self.y - (self.y % 20)

        #Draws the food
        self.canvas.create_rectangle(self.x, self.y, self.x-20, self.y-20, tag = "food", fill = "red")
   
   
        
        
if __name__ == '__main__':
    #Creates a window for testing
    window = Tk()
    window.title("Test")   
    canvas = Canvas(window)
    canvas.pack()  
    
    #Calls the class
    f = Food(canvas)
    
    #Checks that the random numbers are in the proper range
    assert 20 <= f.x <= 600
    assert 20 <= f.y <= 500
    
    #Checks that the coordinates are divisible by 20
    assert (f.x % 20) == 0
    assert (f.y % 20) == 0
    
    print("All Food tests passed!")
    
    
    
    
    

    
    
    
    