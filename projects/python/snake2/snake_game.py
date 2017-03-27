'''
Snake game
CS-108 Final Project
Created by Tristan Hazlett (tdh7)
Created on 12/13/16
'''

# Imports
from tkinter import *
from random import randint
from snake import Snake
from food_square import Food_Square

class SnakeGame:

    def __init__(self, window):
        '''
        This is the initial method for the snake game
        '''
        # Make the window and canvas
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 600
        self.canvas = Canvas(self.window, bg='black',
                        width=self.width, height=self.width)
        self.canvas.configure(background='#f2f2f2')
        self.canvas.pack()
        self.terminated = False

        # Show pregame message and score
        self.pre_game()



    def pre_game(self, event=None, retry=False):
        '''
        This method shows the pregame screen
        '''
        # Delete everything from the canvas
        self.canvas.delete(ALL)

        # Unbind all the keys, just in case
        self.window.unbind('<Up>')
        self.window.unbind('<Down>')
        self.window.unbind('<Left>')
        self.window.unbind('<Right>')

        # Bind spacebar to the new game method
        self.window.bind('<KeyPress-space>', self.start_game)

        # Set the focus of the canvas so the key press actions work
        self.canvas.focus_set()

        # Print the message.  If this is a retry, then say that you lost and tell the score
        if retry:
            self.canvas.create_text(300,300, fill="#4d4d4d", font="Arial 20", anchor=CENTER, text=("You bit yourself!  Your score was " + str(self.snake._snakeLength) + "\n\nPress the spacebar to start a new game.\n\nYour high score is " + str(self.get_high_score()) + "."))
        else:
            self.canvas.create_text(300,300, fill="#4d4d4d", font="Arial 20", anchor=CENTER, text=("Press the spacebar to start.\n\nYour high score is " + str(self.get_high_score()) + "."))

    def start_game(self, event=None):
        '''
        This method starts a new game
        '''
        # Make a new snake and some food
        self.snake = Snake(self.canvas)
        self.food = Food_Square(randint(0,60), randint(0,60))

        # Unbind spacebar, just in case.  The only way to quit is to lose
        self.window.unbind('<KeyPress-space>')

        # Bind the keys that change the direction of the snake
        self.window.bind('<Up>', self.snake.turnUp)
        self.canvas.bind('<Down>', self.snake.turnDown)
        self.canvas.bind('<Left>', self.snake.turnLeft)
        self.canvas.bind('<Right>', self.snake.turnRight)

        # Set the focus of the canvas so the key press actions work
        self.canvas.focus_set()

        # Call the main render loop for the game
        self.render()

        # Start the main event loop for the game
        self.window.mainloop()

    # Render method
    def render(self):
        '''
        This method is the main logic and render loop for the game
        '''
        # Game logic only happens if not in an invalid state
        while not self.terminated and not self.snake.hasCollided:

            # Delete everything from the canvas
            self.canvas.delete(ALL)

            # Show the high score and current score
            self.canvas.create_text(580,10, fill="#4d4d4d", font="Arial 15", anchor=NE, text=("Score: %d\tBest: %s" % (self.snake._snakeLength, self.get_high_score()))) #Render the score info

            # Check for new high scores, and save them to the high score file
            if self.snake._snakeLength > int(self.get_high_score()):
                self.save_high_score(self.snake._snakeLength)

            # Call the update logic on the snake
            self.snake.update()

            # Check to see if the snake has collided with the food
            if self.snake.checkFoodCollision(self.food):

                # Grow the snake
                self.snake.grow()

                # Make a new food square
                self.food = Food_Square(randint(0,60), randint(0,60))

            # Render the food
            self.food.render(self.canvas)

            # Call the next iteration of the loop
            self.window.after(75-self.snake._snakeLength//3) # Notice the game gets faster as the score gets higher!
            self.canvas.update()

        # Check to see if the snake has collided with itself
        if self.snake.hasCollided:

            # Start a new game, and display losing message
            self.pre_game(retry=True)

    def get_high_score(self):
        '''
        This method retrieves the user's high score from the disk, or creates a new high score if needed
        '''
        try:
            # Open the high score file
            with open("high_score.txt") as file:
                high_score = file.read()
                return str(high_score)
        except Exception as e:
            # If we can't find the high score file, then make a new one
            print("Creating a new file to hold the high score, since it does not already exist.")
            self.save_high_score(0)
            return "0"

    def save_high_score(self, score):
        '''
        This method saves the user's high score
        '''
        try:
            # Save the high score to a file
            with open("high_score.txt", mode="w") as file:
                file.write(( "%d" % score ))
        except Exception as e:
            # If we can't find the high score file, then make a new one
            print("Could not save the high score out to a file.")

    def safe_exit(self):
        '''
        Turn off the event loop before closing the GUI
        '''
        self.terminated = True
        self.window.destroy()

if __name__ == '__main__':
    root = Tk()
    root.title('Snake Game')
    app = SnakeGame(root)
    root.mainloop()
  