'''
Square class
CS-108 Final Project
Created by Tristan Hazlett (tdh7)
Created on 12/13/16
'''

class Square:

    def __init__(self, grid_x, grid_y):
        '''
        This is the init method for a square
        '''
        self._grid_x = grid_x
        self._grid_y = grid_y

        # If the square is off the screen, then correct by wrapping it around the grid
        self._grid_x = self._grid_x % 60
        self._grid_y = self._grid_y % 60

    def __str__(self):
        '''
        This method makes a string representation of the square, for comparison
        '''
        return(str(self.getGridX) + " " + str(self.getGridY))

    def getPositionOnScreen(self, grid_x, grid_y):
        '''
        This method converts from grid coordinates to pixel values
        '''
        return(grid_x*10, grid_y*10)

    def getGridX(self):
        '''
        This method returns the grid value
        '''
        return self._grid_x

    def getGridY(self):
        '''
        This method returns the grid value
        '''
        return self._grid_y
