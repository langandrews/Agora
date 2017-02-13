'''
Food Square class
CS-108 Final Project
Created by Tristan Hazlett (tdh7)
Created on 12/13/16
'''
from square import Square

class Food_Square(Square):

    def __init__(self, grid_x, grid_y):
        '''
        This is the init method for a square
        '''
        super().__init__(grid_x, grid_y)


    def render(self, canvas):
        '''
        This method renders the square
        '''
        # Convert the grid position to X and Y pixels
        x = self.getPositionOnScreen(self._grid_x, self._grid_y)[0]
        y = self.getPositionOnScreen(self._grid_x, self._grid_y)[1]
        # Draw the square on the screen in a red color
        canvas.create_rectangle(x, y, x+10, y+10, fill = "#ff3333")
