'''Creates a snake game. The snake is controlled by the user and tries to get the food. 
If the snake gets the food it gets longer and your score increases. If the snake runs into
itself the game ends.
Created on Dec 3, 2014
Final Project
@author: Hannah Ludema (hel7)
'''
#Imports the TKinter, food, and snake modules
from tkinter import *
from food import *
from snake import *

class Driver:
    def __init__(self):
        #Creates a window using tkinter
        self.window = Tk()
        self.window.title("Snake")
        
        #Exits cleanly
        self.window.protocol('WM_DELETE_WINDOW', self.exitClean)
        self.terminate = False
        
        #Initializes the variable that ends the game
        self.end = False
        
        #Creates a frame on the window for the canvas
        self.game = Frame(self.window)
        self.game.pack()
        #Creates a canvas on the frame
        self.canvas = Canvas(self.game, bg = "black", width = 600, height = 500)
        self.canvas.grid(row = 1 , column = 0, rowspan = 2)
        
        
        #Creates a frame on the window for the speed buttons
        self.speedBts = Frame(self.window)
        self.speedBts.pack()
        #Initializes the canvas pause time
        self.pausetime = 300
        #Creates a label and slow, medium and fast buttons on the frame, each with a command
        Label(self.speedBts, text = "Speeds:").grid(row = 1)
        self.slowBt = Button(self.speedBts, text = "Slow", command = self.set_slow)
        self.slowBt.grid(row = 1, column = 1)
        self.mediumBt = Button(self.speedBts, text = "Medium", command = self.set_medium )
        self.mediumBt.grid(row = 1, column = 2)
        self.fastBt = Button(self.speedBts, text = "Fast", command = self.set_fast)
        self.fastBt.grid(row = 1, column = 3)
        
        
        #Creates a frame for the window for the edges buttons
        self.edgesBts = Frame(self.window)
        self.edgesBts.pack()
        #Creates a variable that is a DoubleVar so you can only choose one of the radio buttons
        self.goThroughEdges = DoubleVar()
        self.goThroughEdges.set(True)
        #Creates a label and an on and off button on the frame
        Label(self.edgesBts, text = "Go through edges:").grid(row = 1)
        self.onBt = Radiobutton(self.edgesBts, text = "On", variable = self.goThroughEdges, value = True)
        self.onBt.grid(row = 1, column = 1)
        self.offBt = Radiobutton(self.edgesBts, text = "Off", variable = self.goThroughEdges, value = False)
        self.offBt.grid(row = 1, column = 2)
        
        
        #Creates a food object
        self.newfood = Food(self.canvas)
        
        #Creates a snake object
        self.newsnake = Snake(self.canvas)
        
        #Initialized the score variable
        self.score = 0
        
        #Makes the snake move right as default
        self.processVars = [self.newsnake.move_right, self.newsnake.move_right,self.newsnake.move_right, self.newsnake.move_right, self.newsnake.move_right]
        self.process = self.newsnake.move_right
        self.animate()
        
        if self.terminate == False:
            #Creates a game over message and puts the score on the screen when your lose
            Label(self.game, text = "Game Over!", fg = "red", bg = "black", font = ("Helvetica", 60)).grid(row = 1, column = 0, sticky = S)
            Label(self.game, text = "Your score was: " + str(self.score), fg = "blue", bg = "black", font = ("Helvetica", 20)).grid(row = 2, column = 0, sticky = N)
            
        #Creates an event loop
        self.window.mainloop()
        
        
    def set_slow(self):
        #Makes the screen update at a slower rate so the snake moves slow
        self.pausetime = 300
    def set_medium(self):
        #Makes the screen update at a medium rate so the snake moves at a medium speed
        self.pausetime = 200
    def set_fast(self):
        #Makes the screen update at a faster rate so the snake moves fast
        self.pausetime = 100
     
     
    def animate(self):
        #Creates an animation loop
        while not self.terminate:
            #Deletes the last square make of the snake
            self.canvas.delete("snake")
            
            #Makes it so you can only choose left or right when going up or down and vice versa
            if (self.processVars[0] == self.newsnake.move_right and self.process == self.newsnake.move_left):
                self.process = self.newsnake.move_right
            if self.processVars[0] == self.newsnake.move_left and self.process == self.newsnake.move_right:
                self.process = self.newsnake.move_left
            if self.processVars[0] == self.newsnake.move_up and self.process == self.newsnake.move_down:
                self.process = self.newsnake.move_up
            if self.processVars[0] == self.newsnake.move_down and self.process == self.newsnake.move_up:
                self.process = self.newsnake.move_down
                
            #Sets the direction process for each square
            for index in range(len(self.processVars)-1,-1, -1):
                if index != 0:
                    self.processVars[index] = self.processVars[index - 1]    
                else:
                    self.processVars[index] = self.process
                    
            #Calls the direction process for each square
            for index in range(len(self.processVars)):
                self.processVars[index](index)
                
            #Creates the squares on the canvas
            self.newsnake.render()
           
            
            #Binds the up, down, left and right buttons to make the snake move in the corresponding direction
            self.canvas.bind('<Up>',  self.processUp)
            self.canvas.bind('<Down>', self.processDown)
            self.canvas.bind('<Right>', self.processRight)
            self.canvas.bind('<Left>', self.processLeft)
            self.canvas.focus_set()
            
            #Checks to see if the snake runs into itself
            self.checkCollision()
            #Checks if the snake gets the food
            self.checkFood()
            #Checks to see if the snake runs into the edge
            self.checkEdges()
            
            
            #Pauses the canvas and updates it
            self.canvas.after(self.pausetime)
            self.canvas.update()
             
            #Ends the loop and the game if the variable is True 
            if self.end == True:
                break
       
     
    def processUp(self, event):
        #Sets the process to make the snake move up
        self.process = self.newsnake.move_up
    def processDown(self, event):
        #Sets the process to make the snake move down
        self.process = self.newsnake.move_down
    def processRight(self, event):
        #Sets the process to make the snake move right
        self.process = self.newsnake.move_right
    def processLeft(self, event):
        #Sets the process to make the snake move left   
        self.process = self.newsnake.move_left
   
   
   
    def checkCollision(self):
        #Goes through each square in the snake except for the first one
        for each in range(len(self.newsnake.x_coordinates)-1, 0, -1):
            #Checks if the first square runs into itself
            if self.newsnake.x_coordinates[each] == self.newsnake.x_coordinates[0] and self.newsnake.y_coordinates[each] == self.newsnake.y_coordinates[0]:
                #Ends the game
                self.end = True
        
    def checkFood(self):
        if self.newsnake.x_coordinates[0] == self.newfood.x and self.newsnake.y_coordinates[0] == self.newfood.y:
            #Deletes the food and makes a new one
            self.canvas.delete("food")
            self.newfood = Food(self.canvas)
             
            #Increases the score
            self.score +=1
            
            #Creates a new square  to make the snake longer by creating a new x coordinate, y coordinate, and direction process
            self.processVars.append(self.processVars[-1])
            if self.processVars[-1] == self.newsnake.move_right:
                self.newsnake.x_coordinates.append(self.newsnake.x_coordinates[-1]-20)
                self.newsnake.y_coordinates.append(self.newsnake.y_coordinates[-1])        
            elif self.processVars[-1] == self.newsnake.move_left:
                self.newsnake.x_coordinates.append(self.newsnake.x_coordinates[-1]+20)
                self.newsnake.y_coordinates.append(self.newsnake.y_coordinates[-1])        
            elif self.processVars[-1] == self.newsnake.move_up:
                self.newsnake.x_coordinates.append(self.newsnake.x_coordinates[-1])
                self.newsnake.y_coordinates.append(self.newsnake.y_coordinates[-1]+20)
            else:
                self.newsnake.x_coordinates.append(self.newsnake.x_coordinates[-1])
                self.newsnake.y_coordinates.append(self.newsnake.y_coordinates[-1]-20)
       
        
    def checkEdges(self):
        #Checks if the snake can go through the edges
        if self.goThroughEdges.get() == True:
            #Resets the coordinates to make the snake come back through the other side
            if self.newsnake.x_coordinates[0] >= 600:
                for each in range(len(self.newsnake.x_coordinates)):
                    self.newsnake.x_coordinates[each] -= 600
            if self.newsnake.x_coordinates[0] <= 0:
                for each in range(len(self.newsnake.x_coordinates)):
                    self.newsnake.x_coordinates[each] += 600
            if self.newsnake.y_coordinates[0] >= 500:
                for each in range(len(self.newsnake.y_coordinates)):
                    self.newsnake.y_coordinates[each] -= 500
            if self.newsnake.y_coordinates[0] <= 0:
                for each in range(len(self.newsnake.y_coordinates)):
                    self.newsnake.y_coordinates[each] += 500
        else:
            #Ends the game if the snake runs into the edges
            if self.newsnake.x_coordinates[0] == 600 or self.newsnake.x_coordinates[0] == 0:
                self.end = True
            if self.newsnake.y_coordinates[0] == 500 or self.newsnake.y_coordinates[0] == 0:
                self.end = True 
        
            
    def exitClean(self):
        #Exits the screen cleanly
        self.terminate = True
        self.window.destroy()

#Calls the driver class        
Driver()


