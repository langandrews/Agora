'''
Created on Dec 2, 2014
The GUI and graphics for Super Tic-Tac-Toe
@author: Ethan
'''
try:
    from tkinter import *
    from tictactoe import *
    import AI
except ImportError as err:
    print('Import Error! Oh noes!',err)

def draw_x(canvas, x, y, size, color='black', thickness=4):
    canvas.create_line(x,y,x+size,y+size, width=thickness, fill=color)
    canvas.create_line(x+size,y,x,y+size, width=thickness, fill=color)
    
def draw_o(canvas, x, y, size, color='black', thickness=4):
    canvas.create_oval(x,y,x+size,y+size, width=thickness, outline=color)

def draw_grid(canvas, grid, x, y, size, color='black', thickness=3):
    onethirdsize = int(size * 0.33)
    #Draw the lines of the grid
    canvas.create_line(x,y+onethirdsize,x+size,y+onethirdsize, width=thickness, fill=color)
    canvas.create_line(x,y+(2*onethirdsize),x+size,y+(2*onethirdsize), width=thickness, fill=color)
    canvas.create_line(x+onethirdsize,y,x+onethirdsize,y+size, width=thickness, fill=color)
    canvas.create_line(x+(2*onethirdsize),y,x+(2*onethirdsize),y+size, width=thickness, fill=color)
    #Draw the x's and the o's
    for i in range(3):
        for j in range(3):
            if grid.get_slot(i, j).get() == 'x':
                draw_x(canvas, x+(onethirdsize*i), y+(onethirdsize*j), onethirdsize, 'red')
            if grid.get_slot(i, j).get() == 'o':
                draw_o(canvas, x+(onethirdsize*i), y+(onethirdsize*j), onethirdsize, 'blue')
                
    if grid.is_finished():
        if grid.get_winner() == 'x':
            draw_x(canvas, x, y, size, color='red', thickness=8)
        elif grid.get_winner() == 'o':
            draw_o(canvas, x, y, size, color='blue', thickness=8)
                
def draw_supergrid(canvas, supergrid, x, y, size):
    thirdsize = int(size * 0.33)
    #Draw the smaller grids
    for i in range(3):
        for j in range(3):
            if supergrid.get_playable_slot() == 'all' or supergrid.get_playable_slot() == [i, j]:
                color = 'red'
            else:
                color = 'black'
            draw_grid(canvas, supergrid.get_grid(i, j), x+(thirdsize*i), y+(thirdsize*j), thirdsize, color)
    draw_grid(canvas, supergrid, x, y, size, color='blue', thickness=8)

class Player:
    def __init__(self, team, type='human'):
        if team == 'x' or team == 'o':
            self._team = team 
        else:
            raise ValueError('Error creating player: invalid team')
        if type == 'human' or type == 'computer':
            self.type = type
        else:
            raise ValueError('Error creating player: invalid type')
        
    def get(self):
        return self._team

class RegularGame:
    '''
    This class is a graphical representation of the basic grid class. Rather than muck up my
    tictactoe module with a bunch of positional data, this class should handle all the drawing and shtuff
    '''
    def __init__(self):
        self.grid = Grid() 
        self.size = 400
        self.thirdsize = int(self.size * 0.33)
        self.players = [Player('x', 'human'), Player('o', 'human')]
        self.current_player = 0
        self.window = Tk()
        self.window.title('Tic-Tac-Toe')
        self.window.protocol('WM_DELETE_WINDOW', self.exit)
        
        #Setup the new game buttons
        tempframe = Frame(self.window)
        sp_rb = Button(tempframe, text='1-Player', command=self.new_1p)
        tp_rb = Button(tempframe, text='2-Player', command=self.new_2p)
        np_rb = Button(tempframe, text='0-Player', command=self.new_0p)
        for rb in [sp_rb, tp_rb, np_rb]:
            rb.pack(side=LEFT, padx=10)
        tempframe.pack()
        
        self.canvas = Canvas(self.window, 
                             width=self.size, 
                             height=self.size)
        self.canvas.bind('<Button-1>', self.mouseclick)
        self.canvas.pack(padx=50)
        
        #Game vars
        self.xwins = 0
        self.owins = 0
        self.draws = 0
        
        self.xwins_txt = StringVar()
        self.xwins_txt.set(str(0))
        self.owins_txt = StringVar()
        self.owins_txt.set(str(0))
        self.draws_txt = StringVar()
        self.draws_txt.set(str(0))
        
        #Pack the information labels into frames and add the frames to the window
        frames = [Frame(self.window, width=self.size) for x in range(3)]
        Label(frames[0], text='X Wins:').pack(side=LEFT)
        xwins_label = Label(frames[0], textvariable=self.xwins_txt)
        xwins_label.pack(side=LEFT, padx=10)
        frames[0].pack()
        Label(frames[1], text='O Wins:').pack(side=LEFT)
        owins_label = Label(frames[1], textvariable=self.owins_txt)
        owins_label.pack(side=LEFT, padx=10)
        frames[1].pack()
        Label(frames[2], text='Draws: ').pack(side=LEFT)
        draws_label = Label(frames[2], textvariable=self.draws_txt)
        draws_label.pack(side=LEFT, padx=10)
        frames[2].pack()
        
        #Main menu button
        back_button = Button(self.window, text='Main Menu', command=self.back_button)
        back_button.pack()
        
        self.running = True
        self.mainloop()
        
        self.window.mainloop()
        
    def mainloop(self):
        while self.running:
            #Draw everything
            self.canvas.delete(ALL)
            draw_grid(self.canvas,self.grid,0,0,self.size)
            self.canvas.after(30)
            self.canvas.update()
            
            '''
            If the current player is a computer, process the turn and switch players
            '''
            if self.players[self.current_player].type == 'computer':
                if self.players[0].type == self.players[1].type == 'computer':
                    self.canvas.after(50)
                else:
                    self.canvas.after(750)
                AI.move(self.grid, self.players[self.current_player].get())
                if self.current_player == 0:
                    self.current_player = 1
                else:
                    self.current_player = 0
            
            self.grid.checkwin()
            if self.grid.is_finished():
                if self.grid.get_winner() == 'x':
                    self.xwins += 1
                    self.xwins_txt.set(str(self.xwins))
                elif self.grid.get_winner() == 'o':
                    self.owins += 1
                    self.owins_txt.set(str(self.owins))
                else:
                    self.draws += 1
                    self.draws_txt.set(str(self.draws))
                draw_grid(self.canvas,self.grid,0,0,self.size)
                self.canvas.update()
                self.canvas.after(2000)
                self.reset()    
            
    def mouseclick(self, event):
        if self.players[self.current_player].type == 'human':
            targ_slot = None
            for i in range(3):
                for j in range(3):
                    if (self.thirdsize*i) <= event.x <= (self.thirdsize*(i+1)) and (self.thirdsize*j) <= event.y <= (self.thirdsize*(j+1)):
                        targ_slot = [i, j]
                        break
            if targ_slot != None and self.grid.get_slot(targ_slot[0], targ_slot[1]).get() == 'n':
                self.grid.set_slot(targ_slot[0], targ_slot[1], self.players[self.current_player].get())
                self.grid.checkwin()
                self.canvas.delete(ALL)
                draw_grid(self.canvas,self.grid,0,0,self.size)
                self.canvas.after(30)
                self.canvas.update()
                if not self.grid.is_finished():
                    if self.current_player == 0:
                        self.current_player = 1
                    else:
                        self.current_player = 0
    
    def new_1p(self):
        self.grid.reset()
        self.players[0] = Player('x', 'human')
        self.players[1] = Player('o', 'computer')
        self.current_player = 0
        
    def new_2p(self):
        self.grid.reset()
        self.players[0] = Player('x', 'human')
        self.players[1] = Player('o', 'human')
        self.current_player = 0
        
    def new_0p(self):
        self.grid.reset()
        self.players[0] = Player('x','computer')
        self.players[1] = Player('o','computer')
        self.current_player = 0
                        
    def reset(self):
        self.grid.reset()
        self.current_player = 0
        
    def back_button(self):
        self.running = False
        self.window.destroy()
        MainMenu()
    
    def exit(self):
        self.running = False
        self.window.destroy()
        
class SuperGame:
    def __init__(self):
        self.SIZE = 600
        self.THIRDSIZE = int(self.SIZE * 0.33)
        self.supergrid = SuperGrid()
        self.window = Tk()
        self.window.title('Super Tic Tac Toe')
        self.window.protocol('WM_DELETE_WINDOW', self.exit)
        self.window.focus_set()
        
        self.canvas = Canvas(self.window, width=self.SIZE, height=self.SIZE)
        self.canvas.bind('<Button-1>', self.mouseclick)
        self.canvas.pack(padx=50)
        
        #Sets up x as the current player
        self.current_player = 'x'
        self.current_player_text = StringVar()
        self.current_player_text.set('x')
        
        #Add a Label for the current player
        tempframe = Frame(self.window)
        Label(tempframe, text='Current Player:').pack(padx=10, side=LEFT)
        Label(tempframe, textvariable=self.current_player_text).pack(side=LEFT)
        tempframe.pack()
        
        #Back button
        back_button = Button(self.window, text='Main Menu', command=self.back_button)
        back_button.pack()
        
        self.running = True
        self.mainloop()
        
        self.window.mainloop()
        
    def mainloop(self):
        while self.running:
            self.canvas.delete(ALL)
            draw_supergrid(self.canvas, self.supergrid, 0, 0, self.SIZE)
            if self.supergrid.is_finished():
                self.canvas.after(30)
                self.canvas.update()
                self.canvas.after(2000)
                self.supergrid.reset()
            else:
                self.canvas.after(30)
                self.canvas.update()
            
    def mouseclick(self, event):
        targ_grid = None
        targ_slot = None
        #Check which grid was clicked on
        for i in range(3):
            for j in range(3):
                width = [(self.THIRDSIZE*i), (self.THIRDSIZE*(i+1))]
                height = [(self.THIRDSIZE*j), (self.THIRDSIZE*(j+1))]
                if width[0] < event.x < width[1] and height[0] < event.y < height[1]:
                    targ_grid = [i,j]
                    break
        if targ_grid != None:
            if self.supergrid.get_playable_slot() == 'all' or self.supergrid.get_playable_slot() == targ_grid:
                ninthsize = int(self.THIRDSIZE * 0.33)
                for i in range(3):
                    for j in range(3):
                        width = [(self.THIRDSIZE * targ_grid[0])+(ninthsize*i), (self.THIRDSIZE*targ_grid[0])+(ninthsize*(i+1))]
                        height = [(self.THIRDSIZE*targ_grid[1])+(ninthsize*j), (self.THIRDSIZE*targ_grid[1])+(ninthsize*(j+1))]
                        if width[0] < event.x < width[1] and height[0] < event.y < height[1]:
                            targ_slot = [i, j]
                            break
        if targ_slot != None:
            try:
                self.supergrid.move(self.current_player, targ_grid, targ_slot)
            except:
                print('Invalid Move')
            else:
                if self.current_player == 'x':
                    self.current_player = 'o'
                    self.current_player_text.set('o')
                else:
                    self.current_player = 'x'
                    self.current_player_text.set('x')
    
    def back_button(self):
        self.running = False
        self.window.destroy()
        MainMenu()              
    
    def exit(self):
        self.running = False
        self.window.destroy()
        
class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.title('Super Tic-Tac-Toe')
        self.window.focus_set()
        self.photo = PhotoImage(file='images/TitleScreen.gif')
        
        #Set up the window
        canvas = Canvas(self.window, width=600, height=400)
        canvas.create_image(300,200, image=self.photo)
        canvas.pack()
        reg_button = Button(self.window, text='Regular Game', command=self.new_reg)
        sup_button = Button(self.window, text='Super Game', command=self.new_sup)
        reg_button.pack()
        sup_button.pack()
        
        self.window.mainloop()
        
    def new_reg(self):
        self.window.destroy()
        RegularGame()
        
    def new_sup(self):
        self.window.destroy()
        SuperGame()
      
        
#Every time I test my program I find new problems, therefore testing causes problems. Right?
if __name__ == '__main__':
    MainMenu()