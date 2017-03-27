'''Driver Class for Mastermind game (code breaker game GUI)
12/04/14
Final Project
@author: Cara Alexander (cea6)
'''

from logic import *
from tkinter import *
 

class Thing():
    """
    class to drive the GUI
    """
    def __init__(self):
        self.window = Tk()
        self.window.title('Mastermind')
        
        #initialize guess to blank
        self.guess=['','','','']

        #initialize self.color
        self.color='white'
        
        # Row and Column Counter
        self.row = 0;
        self.column = 0;
        
        #frame stuff
        frame = Frame(self.window)
        frame.grid(row=1,column=1)
    
        #canvas stuff
        self.canvas = Canvas(self.window,bg = '#CFFFE7', width = 650, height = 700)
        self.canvas.grid(row=2,column=1, columnspan=20, rowspan=20)
        
        #draw board
        rec = self.canvas.create_rectangle(290, 0, 545, 655, fill = '#663300')
        
        #draw holes
        for j in range(10):
            
            for i in range(4):
                circ = self.canvas.create_oval(300 + 33.3*2*i, 10+33.3*2*j, 333.3 + 33.3*2*i, 43.3+33.3*2*j, fill = 'white')
       
        #display instructions
        Label(text="Welcome to Mastermind!\n  You have 10 tries to guess\n the secret code of 4 colors.\n  To make a guess, click on\n the color you want and\n then on the select button below the\n spot where you want to place it.\n  When you are happy\n with your guess, click Try.\n  The white dots mean you had the\n right color in the right spot.\n  The black dots mean you had\n the right color in the wrong spot.\n  The clear dots mean you\n had the wrong color.\n  The order of the little dots is\n not the order of the colors,\n and colors can be used multiple times.", bg='#CFFFE7').grid(row=16,column=1,columnspan=3)
        
        #start 1 round of logic
        l = Logic()
        self.l=l
        
        #color buttons 
        r=Button(self.window, text = 'red', activebackground = '#CC0000', bg = 'red', command=self.cred)
        r.grid(row=4,column=3)
        
        b=Button(self.window, text = 'blue', activebackground = '#509BE6', bg = '#59ACFF', command=self.cblue)
        b.grid(row=3,column=2)
        
        g=Button(self.window, text = 'green', activebackground = '#00B800', bg = 'green', command=self.cgreen)
        g.grid(row=3,column=3)
        
        y=Button(self.window, text = 'yellow', activebackground = '#E6B800', bg = 'yellow', command=self.cyellow)
        y.grid(row=4,column=1)
        
        o=Button(self.window, text = 'orange', activebackground = '#E66916', bg = '#FF8330', command=self.corange)
        o.grid(row=4,column=2)
        
        p=Button(self.window, text = 'pink', activebackground = '#E661A3', bg = '#FF6CB5', command=self.cpink)
        p.grid(row=3,column=1)
        
# select buttons        
        s4=Button(self.window, text = 'select', command=self.select_column4)
        s4.grid(row=21,column=11)
         
        s3=Button(self.window, text = 'select', command=self.select_column3)
        s3.grid(row=21,column=10)
         
        s2=Button(self.window, text = 'select', command=self.select_column2)
        s2.grid(row=21,column=9)
        
        s1=Button(self.window, text = 'select', command=self.select_column1)
        s1.grid(row=21,column=8)
        
        
#try button
        btry=Button(self.window, text = 'Try', command=self.t)
        btry.grid(row=5,column=2)
        
        
        self.window.mainloop()
        
#reset button
        #again=Button(self.window, text = '     Restart    ',command=self.again)
        #again.grid(row=6,column=1, columnspan=6)

#method for try button  
    def t(self):
        """ method to do stuff that happens when you hit try """
    
        if self.guess[0] != '' and self.guess[1] != '' and self.guess[2] != '' and self.guess[3] != '':
            
            pins=self.l.check(self.guess)
            
            #show pins
            self.canvas.create_oval(570, 10+33.3*2*self.row, 580, 20+33.3*2*self.row)
            self.canvas.create_oval(593.3, 10+33.3*2*self.row, 603.3, 20+33.3*2*self.row)
            self.canvas.create_oval(570, 30+33.3*2*self.row, 580, 40+33.3*2*self.row)
            self.canvas.create_oval(593.3, 30+33.3*2*self.row, 603.3, 40+33.3*2*self.row)
            if len(pins)>=1:
                self.canvas.create_oval(570, 10+33.3*2*self.row, 580, 20+33.3*2*self.row, fill = pins[0])
            if len(pins)>=2:
                self.canvas.create_oval(593.3, 10+33.3*2*self.row, 603.3, 20+33.3*2*self.row, fill = pins[1])
            if len(pins)>=3:
                self.canvas.create_oval(570, 30+33.3*2*self.row, 580, 40+33.3*2*self.row,fill=pins[2])
            if len(pins)>=4:
                self.canvas.create_oval(593.3, 30+33.3*2*self.row, 603.3, 40+33.3*2*self.row,fill=pins[3])
                
            #accumulate row
            self.row+=1
            
            #clear guess
            self.guess=['','','','']
            
            #test if won
            if pins == ['white','white','white','white']:
                #do win stuff
                again=Button(self.window, text = 'Congratulations, you win! Play Again?',command=self.again)
                again.grid(row=6,column=1, columnspan=6)
                self.lagain=again
            
            #test if lost
            if self.row>=10:
                #do loose stuff
                lagain=Button(self.window, text = ' Better luck next time! Play Again? ',command=self.again)
                lagain.grid(row=6,column=1, columnspan=6)
                self.lagain=lagain
            
      
    
    
    #Column Selector/ methods for select buttons
    def select_column1(self):
        """draw peg of color self.color in 1st column"""
        if self.row<10:
            self.column = 0
            self.canvas.create_oval(300 + 33.3*2*self.column, 10+33.3*2*self.row, 333.3 + 33.3*2*self.column, 43.3+33.3*2*self.row, fill = self.color)
            self.guess[0]=self.color
    def select_column2(self):
        """draw peg of color self.color in 2nd column"""
        if self.row<10:
            self.column = 1
            self.canvas.create_oval(300 + 33.3*2*self.column, 10+33.3*2*self.row, 333.3 + 33.3*2*self.column, 43.3+33.3*2*self.row, fill = self.color)
            self.guess[1]=self.color
    def select_column3(self):
        """draw peg of color self.color in 3rd column"""
        if self.row<10:
            self.column = 2
            self.canvas.create_oval(300 + 33.3*2*self.column, 10+33.3*2*self.row, 333.3 + 33.3*2*self.column, 43.3+33.3*2*self.row, fill = self.color)
            self.guess[2]=self.color
    def select_column4(self):
        """draw peg of color self.color in 4th column"""
        if self.row<10:
            self.column = 3
            self.canvas.create_oval(300 + 33.3*2*self.column, 10+33.3*2*self.row, 333.3 + 33.3*2*self.column, 43.3+33.3*2*self.row, fill = self.color)
            self.guess[3]=self.color
    
    
    #methods for Color Changers
    def cred(self):
        """change color of peg to place to red"""
        self.color = 'red'
    def cblue(self):
        """change color of peg to place to blue"""
        self.color = '#59ACFF'
    def cpink(self):
        """change color of peg to place to pink"""
        self.color = '#FF6CB5'
    def cgreen(self):
        """change color of peg to place to green"""
        self.color = 'green'
    def corange(self):
        """change color of peg to place to orange"""
        self.color = '#FF8330'
    def cyellow(self):
        """change color of peg to place to yellow"""
        self.color = 'yellow'
        
        
    #method for play again button
    def again(self):
        """method for play again button to set up a new round"""
        
        #reset row
        self.row = 0
        
        #clear holes
        for j in range(10):
            
            for i in range(4):
                circ = self.canvas.create_oval(300 + 33.3*2*i, 10+33.3*2*j, 333.3 + 33.3*2*i, 43.3+33.3*2*j, fill = 'white')
        #clear pins
        rec = self.canvas.create_rectangle(660, 0, 545, 655, fill = '#CFFFE7',outline='#CFFFE7')
        
        
        #clear play again button
        self.lagain.destroy()
        
        #clear pins
        rec = self.canvas.create_rectangle(660, 0, 545, 655, fill = '#CFFFE7',outline='#CFFFE7')
        
        #start one round of logic
        l = Logic()
        self.l=l


        
Thing()
        
