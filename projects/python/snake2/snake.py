'''
Snake class
CS-108 Final Project
Created by Tristan Hazlett (tdh7)
Created on 12/13/16
'''

# Imports
from snake_square import Snake_Square

class Snake:

    def __init__(self, canvas):
        '''
        This is the init method for the snake
        '''
        # Set up the variables for the snake
        self._square_list = [] # List for snake squares
        self._square_list.append(Snake_Square(30, 30)) #Initial head square
        self._snakeLength = 1
        self._direction = "right"
        self._canvas = canvas
        self.hasCollided = False #Flag for if the snake has collided with itself

    def update(self):
        '''
        This method updates the snake at each move
        '''
        # Determine which direction the snake is going, then add a new square in that direction
        if self._direction == "up":
                self._square_list.append(
                Snake_Square(self._square_list[-1].getGridX(),
                             self._square_list[-1].getGridY() - 1))
        elif self._direction == "down":
                self._square_list.append(
                Snake_Square(self._square_list[-1].getGridX(),
                             self._square_list[-1].getGridY() + 1))
        elif self._direction == "left":
                self._square_list.append(
                Snake_Square(self._square_list[-1].getGridX() - 1,
                             self._square_list[-1].getGridY()))
        elif self._direction == "right":
                self._square_list.append(
                Snake_Square(self._square_list[-1].getGridX() + 1,
                             self._square_list[-1].getGridY()))

        # Trim the end of the snake to the length it is supposed to be
        while len(self._square_list) > self._snakeLength:
            self._square_list.pop(0)

        # Check to see if the snake has collided with itself
        counter = 0
        for s in self._square_list:
            new_list = list(self._square_list)
            new_list.pop(counter)
            for j in new_list:
                # Collision means the X and Y of more than one square are the same
                if s.getGridX() == j.getGridX() and s.getGridY() == j.getGridY():
                    self.hasCollided = True
            counter += 1

        # Render all the squares
        for s in self._square_list:
            s.render(self._canvas)

    def checkFoodCollision(self, food):
        '''
        This method checks to see if the snake has picked up food
        '''
        head = self._square_list[-1]
        # Collision means the X and Y of the head and the food are the same
        if head.getGridX() == food.getGridX() and head.getGridY() == food.getGridY():
            return True
        return False

    def grow(self):
        '''
        This method makes the snake longer
        '''
        # Make the snake longer
        self._snakeLength += 1

    def turnUp(self, event):
        '''
        This method changes the snake's direction
        '''
        # Turn the snake in an up direction, unless the opposite direction already
        if self._direction == "down":
            return
        self._direction = "up"

    def turnDown(self, event):
        '''
        This method changes the snake's direction
        '''
        # Turn the snake in a down direction, unless the opposite direction already
        if self._direction == "up":
            return
        self._direction = "down"

    def turnLeft(self, event):
        '''
        This method changes the snake's direction
        '''
        # Turn the snake in a right direction, unless the opposite direction already
        if self._direction == "right":
            return
        self._direction = "left"

    def turnRight(self, event):
        '''
        This method changes the snake's direction
        '''
        # Turn the snake in a right direction, unless the opposite direction already
        if self._direction == "left":
            return
        self._direction = "right"
