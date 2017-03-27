''' graphgen.py

@author: Quentin Baker (qrb2)

Created December 4, 2015
Last Modified December 15, 2015
'''
from tkinter import *
from random import randint
from prices import *
import time

#GLOBALS
reveal_step = 0
buy_amt = 0

'''BEGIN CODE'''
class GraphGui:
    def __init__(self,window):
        self.stockindex = Stock()
        
        self._buyamount = 0
        self.window = window
        self.width = 600
        self.segment = self.width/12
        self.height = 600
        
        #Text fields
        
        #USER_NET_WORTH
        '''THE FOLLOWING IS AN IMPORTANT CLASS CALL FOR ALL USER MONEY. 
        USE (self.nworth) TO STORE AND RETRIEVE ALL MONETARY VALUES.'''
        
        self.nworth = Usernetworth(tax=randint(10,35)/100) 
        
        '''THANKS.'''
        
        Label(window,text='Current Liquid Assets:').grid(row=0,columnspan = 2,sticky=S)
        
        self.nworth_val = StringVar()
        self.nw_val_label = Label(window,textvariable=self.nworth_val)
        self.nw_val_label.grid(row=1,columnspan=2,sticky=N)
        self.nworth_val.set('-----')
        
        
        #Interactive buttons go below
        self.start_button = Button(window,text='START',command=self.startgame,width=12)
        self.start_button.grid(row=2,column=0,columnspan=2) #NOTE: .grid has to be a SEPARATE line for button.config to work. This is dumb.
        
        self.buy_button = Button(window,text='Buy!',state=DISABLED,command=self.usr_buy,width=6)
        self.buy_button.grid(row=3,column=0,sticky=S)
        
        self.skip_button = Button(window,text='Skip',state=DISABLED,command=self.usr_skip,width=6)
        self.skip_button.grid(row=3,column=1,sticky=S)
        
        Label(window,text='Buy Percentage:').grid(row=4,columnspan=2)
        
        self.waitbutton = Button(window,text='Wait',command=self.usr_wait,state=DISABLED,width=10)
        self.waitbutton.grid(row=6,column=0,columnspan=2)
        
        self.sell_button = Button(window,text='Sell!',command=self.usr_sell,state=DISABLED,width=10)
        self.sell_button.grid(row=7,column=0,columnspan=2)
        
        self.invest_val = StringVar()
        Label(window,text='Amount Invested:').grid(row=8,columnspan = 2,sticky=S)
        
        self.inv_val_label = Label(window,textvariable=self.invest_val)
        self.inv_val_label.grid(row=9,columnspan=2,sticky=N)
        self.invest_val.set('$0')
        
        self.return_val = StringVar()
        Label(window,text='Current Return:').grid(row=10,columnspan=2,sticky=S)
        
        self.ret_val_label = Label(window,textvariable=self.return_val)
        self.ret_val_label.grid(row=11,columnspan=2,sticky=N)
        self.return_val.set('$0')
        
        self.canvas = Canvas(self.window, bg='White', width=self.width, height=self.height)
        
        self.draw_graph()
        
        self.Instruct_button = Button(window,text='Show Instructions',command=self.instruct_usr,state=DISABLED)
        self.Instruct_button.grid(row=12,column=2,columnspan=2,sticky=E)
        
        #Radio Buttons for Buy Choice
        
        self._buychoice = DoubleVar()
        self._buychoice.set(0.25)
        
        self.radio_frame = Frame(window)
        self.radio_frame.grid(row=5,columnspan=2,sticky=N)
        buy_choice = Radiobutton(self.radio_frame, text='25%', variable=self._buychoice, value=0.25)
        buy_choice.grid()
        
        buy_choice = Radiobutton(self.radio_frame, text='50%', variable=self._buychoice, value=0.5)
        buy_choice.grid(row=0,column=1,sticky=W)
        
        buy_choice = Radiobutton(self.radio_frame, text='75%', variable=self._buychoice, value=0.75)
        buy_choice.grid(row=1)
        
        buy_choice = Radiobutton(self.radio_frame, text='100%', variable=self._buychoice, value=1)
        buy_choice.grid(row=1,column=1,sticky=W)
        
        ####graph initialization is below.####
            #draw grid lines
        for i in range(12):
            self.canvas.create_line(self.segment*i,0,self.segment*i,self.width, width = 2, fill = '#CCCCCC',tags='graphgrid')
        for i in range(12):
            self.canvas.create_line(0,self.segment*i,self.width,self.segment*i, width = 2, fill = '#CCCCCC',tags='graphgrid')
        
            #Graph Scale goes here
        self.canvas.create_text(18,300,text='1x',fill='#666666',activefill='#000000',font='arial')
        
        for i in range(5): #negative logs (1^-1,1^-2, etc.)
            logtxt = '1/'+str(i+2)+'x'
            self.canvas.create_text(18,self.segment*(i+7),text=logtxt,fill='#666666',activefill='#000000',font='arial')
            
        for i in range(5): #positive logs (1^+1,etc.)
            logtxt = str(6-i)+'x'
            self.canvas.create_text(18,self.segment*(i+1),text=logtxt,fill='#666666',activefill='#000000',font='arial')   
            #Months
        self._mtxt = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        for i in range(12):
            self.canvas.create_text((self.segment*(i+1)-25),580,text=self._mtxt[i],fill='#666666',font='arial')
            
        
        self.canvas_clean()
        
        #cover
        self.canvas.create_rectangle(0,0,650,600,fill='White',width=0,tags='instrcover')
        self.canvas.create_rectangle(0,0,650,600,fill='White',width=0,tags='cover')
        
        ###GAME INTRO AND INSTRUCTIONAL TEXT. Note that I put each line of text in a separate function to allow custom line spacing.###
        self.canvas.create_text(300,75,text='Hello, and welcome to Q\'s STOCK MARKET GAME!',tags='starttext', fill='#a90000',font=('impact',20))
        self.canvas.create_text(300,115,text='The goal is simple: Get to 1 MILLION dollars, using the stock graph,',tags='starttext')
        self.canvas.create_text(300,130,text='your intuition, and a bit of LUCK.',tags='starttext')
        self.canvas.create_text(100,30,text='Click "START" when you are ready!',tags='starttext')
        self.canvas.create_line(20,38,0,120,width=2,tags='starttext')
        
        self.canvas.create_text(300,160,text='This game\'s CAPITAL GAINS TAX is '+str(round(self.nworth.get_taxrate()*100))+'%, and is applied automatically',tags='starttext')
        self.canvas.create_text(300,175,text='if you sell less than SIX MONTHS after buying.',tags='starttext') 
        self.canvas.create_text(300,190,text='The game\'s calculated return does NOT take this into account by design.',tags='starttext')
        self.canvas.create_text(300,205,text='If you want to be an expert trader, you will want to take this into account manually!',tags='starttext')
        

        #GAME INSTRUCTIONS
        self.canvas.create_text(300,100,text='How to Play',font=('impact', 50 ),tags='infotext',state=HIDDEN)
        self.canvas.create_text(300,295,text='---INSTRUCTIONS: Buying Stock---',fill='#009419',tags='infotext')
        self.canvas.create_text(300,335,text='Press the START button to begin. Part of a graph will be revealed.\
 Based on what you see, you may BUY using the BUY button, or SKIP using the SKIP button. If you BUY, use the four "radio buttons" with their\
 listed percentages to choose how much of your Liquidity to invest. If you SKIP, a new graph will be generated, which you may also BUY or SKIP.',tags='infotext',width=550)
        
        self.canvas.create_text(300,390,text='---INSTRUCTIONS: Selling Stock---',tags='infotext',fill='#009419')
        self.canvas.create_text(300,435,text='So now you own stock. Great! You may now SELL your stock at any time using the SELL button. This\
 will sell ALL of your currently invested stock, and your Liquid Assets will be credited with the value listed at the bottom left of the window,\
 under "Current Return". Remember that CAPITAL GAINS may apply, which will result in less money than is actually listed. Note: If you reach the\
 end of the graph, both WAIT and SELL will act as a SELL button, meaning you MUST sell after 12 months of waiting.',tags='infotext',width=550)
        
        self.canvas.create_text(300,495,text='---ENDING THE GAME---',tags='infotext',fill='#009419')
        self.canvas.create_text(300,535,text='You automatically WIN the game if the game detects you have over 1 MILLION dollars in your Liquid\
 Assets. Conversely, if at any time your Liquid Assets drop below 100 dollars, you will go BANKRUPT, and lose. In both occurrences, you have the\
option to re-start the game with 10 Thousand dollars in Liquid Assets.',tags='infotext',width=550)
        self.canvas.create_text(450,575,text='Good Luck!',tags='starttext',fill='#009419',font=('impact',15))
        
        self.canvas.grid(row=0,column=2,rowspan=12,columnspan=2)
        #self.canvas.create_line(0,400,600,400-(8*self.segment))

        
    def reveal(self):
        '''This function reveals the generated graph on the GUI canvas in 12 50 pixel steps. 
            No arguments are passed except the obligatory "self" used in classes.'''
        global reveal_step
        print(reveal_step)
        print(self._buyamount)
        if reveal_step < 599:
            for cover in range(50):
                self.waitbutton.config(state = DISABLED)
                self.canvas.delete('cover')
                self.canvas.create_rectangle(reveal_step+1,0,650,600,fill='White',width=0,tags='cover')
                reveal_step += 1
                self.canvas.after(10)
                self.canvas.update()
                if self._buyamount != 0:
                    self.waitbutton.config(state = NORMAL)
                else:
                    self.waitbutton.config(state = DISABLED)
        elif reveal_step >= 599:
            self.waitbutton.config(state = DISABLED)
            self.canvas.delete('cover')
            self.usr_sell()
        
    def draw_graph(self):
        '''The core of the GUI is this function. It takes the trend generated in prices.py (1 or 0, representing 
            upward, or downward trends respectively), then creates a graph with a positive or negative slope, that
            has each point given variance through a randomized intercept value. I chose to use the actual y position
            of the graph to reflect the users gains (or losses) by returning the list of multiples to the Usernetworth
            class in prices.py'''
        
        self._multipliers = []
        self.stockindex.set_trend()
        trendSP = self.stockindex.get_trend_spike()
        #print('trend slope:',trendSP)
        for v in range(13):
            if v == 0:
                last = [0,300]
                new = [0,300]
            else:
                new = [self.segment*v,300-(trendSP*v*self.segment)+(randint(-2,2)*self.segment)]#REMINDER: 0,0 is at TOP RIGHT of window.
                
                '''The following if-else statement is what applies the graph to the user's investment.'''
                if 600-new[1] > 300:
                    self._netret = round(((300-new[1])/self.segment)+2,2) #self._netret == NET RETurns
                    self._multipliers.append(self._netret)
                    #print(round(new[1]),'return of:',self._netret)
                    '''if self._buyamount != 0:
                        self.nworth.set_returns(self._netret*self._buyamount)'''
                else:
                    self._netret = round(1/(((new[1]-300)/self.segment)+1),2)
                    self._multipliers.append(self._netret)
                    #print(round(new[1]),'return of:',self._netret)
                    '''if self._buyamount != 0:
                        self.nworth.set_returns(self._netret*self._buyamount)'''

            self.canvas.create_line(last[0],last[1],new[0],new[1],width=3,fill="#007d32",tags='graphline')
            last=new
        self.nworth.set_returns(self._multipliers)
    
    def usr_wait(self):
        '''This function fires when the "wait" button on the GUI is pressed. It uses self.reveal() in addition to
            updating the amount the user will get if they choose to sell at this point, NOT INCLUDING CAPITAL GAINS LOSSES.'''
        self.usr_returns = self.nworth.get_returns()
        self.reveal()
        print(self.usr_returns)
        self.return_val.set('$'+str(round(self.usr_returns[int((reveal_step/50)-1)]*self._buyamount,2)))
    
    def canvas_clean(self):
        '''Deletes the current graph, draws a new one, then covers it with the graph cover.'''
        global reveal_step
        reveal_step = 0
        self.canvas.delete('graphline')
        self.draw_graph()
        self.canvas.create_rectangle(0,0,600,600,fill='White',width=0,tags='cover')
    
    def usr_skip(self):
        '''Fires when user presses the "skip" button in the GUI. This generates a new graph by calling self.canvas_clean().'''
        self.skip_button.config(state = DISABLED)
        self.canvas_clean()
        self.reveal()        
        self.waitbutton.config(state = DISABLED)
        self.buy_button.config(state = NORMAL)
        self.sell_button.config(state = DISABLED)
        self.skip_button.config(state = NORMAL)
        self.checkend()
        
    def usr_buy(self):
        global reveal_step
        global buy_amt
        self.waitbutton.config(state = NORMAL)
        self.skip_button.config(state = DISABLED)
        net_value = self.nworth.get_networth()
        usr_returns = self.nworth.get_returns()
        buy_amt = self._buychoice.get()
        self._buyamount = round(net_value*buy_amt,2)
        print(str(buy_amt*100))
        self.buy_button.config(state = DISABLED)
        self.nworth_val.set('S'+str(net_value-self._buyamount))
        self.nworth.set_networth(net_value-self._buyamount)
        self.invest_val.set('$'+str(self._buyamount))
        self.nworth.set_invested(self._buyamount)
        self.sell_button.config(state = NORMAL)
        print('Amount Remaining:',self.nworth.get_networth())
        print('Amount Invested:',self.nworth.get_invested())
        print(usr_returns)
        self.return_val.set('$'+str(round(usr_returns[int(reveal_step/50)-1]*self._buyamount,2)))
        self.checkend()
    
    def checkend(self):
        if self.nworth.get_networth() <= 100 and self.nworth.get_invested() == 0:
            self.nworth_val.set('BANKRUPT')
            self.waitbutton.config(state = DISABLED)
            self.buy_button.config(state = DISABLED)
            self.sell_button.config(state = DISABLED)
            self.skip_button.config(state = DISABLED)
            self.canvas_clean()
            loser_funnies = ['Here, take a McDonald\'s application.','Repeat after me: "Would you like fries with that?"','Oh, by the way, that was real money. We borrowed it from the Russian Mob, and we did it under your name.',
                             'This is what happens when you major in the Liberal Arts.','You might want to wait on sending Warren Buffet an application...','We don\'t score this like golf.',
                             'Protip: If the bank is leaving threatening messages, call them and tell them you died from hypothermia during the sem pond jump.']
            self.canvas.create_text(300,100,text='You have gone bankrupt.\n'+loser_funnies[randint(0,len(loser_funnies)-1)],tags='endtext',width=500)
            self.start_button.config(text='RE-START',state=NORMAL)
            return True
            
        elif self.nworth.get_networth() >= 1e6:
            self.nworth_val.set('You WIN!')
            self.waitbutton.config(state = DISABLED)
            self.buy_button.config(state = DISABLED)
            self.sell_button.config(state = DISABLED)
            self.skip_button.config(state = DISABLED)
            self.canvas_clean()
            winner_funnies = ['(P.S. Can I use your house-sized hot-tub sometime?)','Spot me a few grand, would ya?','And your parents thought it was a waste of time to play games...',
                              'Savor the fact that the pretend money on the left is a REALLY BIG NUMBER.','Now that you\'ve proven yourself, try my taxes.',
                              'The good news is that this is not gonna be taxed by the federal government. The bad news is that this is all fake.']
            self.canvas.create_text(300,100,text='You have made a MILLION DOLLARS!\n'+winner_funnies[randint(0,len(winner_funnies)-1)],tags='endtext',width=500)
            self.start_button.config(text='RE-START',state=NORMAL)
            return True
        
        return False
        
    def usr_sell(self,offset=1):
        self.waitbutton.config(state = DISABLED)
        self.buy_button.config(state = NORMAL)
        self.sell_button.config(state = DISABLED)
        self.skip_button.config(state = NORMAL)
        self._taxrate = self.nworth.get_taxrate()
        self.return_val.set('$0')
        global reveal_step
        oldnetworth = self.nworth.get_networth()
        newnetworth = self.nworth.get_invested()*self._multipliers[(int(reveal_step/50)-offset)]
        if reveal_step/50 < 6:
            print('Deducting capital gains...')
            newnetworth = newnetworth - newnetworth*self._taxrate #This is where CAPTIAL GAINS tax is applied
        else:
            print('Tax free, hooray!')
            
        self.nworth.set_networth(oldnetworth+round(newnetworth,2))
        self.nworth_val.set('$'+str(self.nworth.get_networth()))
        self.invest_val.set('$0')
        self.return_val.set('$0')
        self.nworth.set_invested(0)
        
        print('Amount Remaining:',self.nworth.get_networth())
        print('Amount Invested:',self.nworth.get_invested())
        
        self.canvas_clean()
        self._buyamount = 0
        
        if not self.checkend():
            self.reveal()
            
    def startgame(self):
        self.start_button.config(text='START')
        self.nworth.set_networth(randint(1e3,1e4))
        self.nworth_val.set('$'+str(self.nworth.get_networth()))
        self.canvas.delete('starttext','endtext')
        self.canvas.itemconfig('infotext',state=HIDDEN)
        self.canvas.itemconfig('instrcover',state=HIDDEN)
        self.buy_button.config(state=NORMAL)
        self.start_button.config(state=DISABLED)
        self.waitbutton.config(state = DISABLED)
        self.skip_button.config(state=NORMAL)
        self.Instruct_button.config(state=NORMAL)
        self.reveal()
    
    '''The following function was built from code found at the following website: 
        https://www.daniweb.com/programming/software-development/code/429838/simple-tkinter-toggle-button'''
        
    def instruct_usr(self,active=[0]):
        '''Shows or hides the instructions on top of the graph.'''
        active[0] = not active[0]
        if active[0]:
            self.Instruct_button.config(text='Hide Instructions')
            self.canvas.delete('cover')
            self.canvas.itemconfig('graphline',state=HIDDEN)
            self.canvas.itemconfig('infotext',state=NORMAL)
            self.canvas.itemconfig('instrcover',state=NORMAL)
            self.sell_button.config(state=DISABLED)
            self.waitbutton.config(state=DISABLED)
            self.buy_button.config(state=DISABLED)
            self.skip_button.config(state=DISABLED)
        else:
            self.Instruct_button.config(text='Show Instructions') 
            self.canvas.create_rectangle(reveal_step,0,650,600,fill='White',width=0,tags='cover')
            self.canvas.itemconfig('infotext',state=HIDDEN)
            self.canvas.itemconfig('instrcover',state=HIDDEN)
            self.canvas.itemconfig('graphline',state=NORMAL)
            if buy_amt == 0:
                self.buy_button.config(state=NORMAL)
                self.skip_button.config(state=NORMAL)
            else:
                self.waitbutton.config(state=NORMAL)
                self.sell_button.config(state=NORMAL)
        
    '''ACCESSORS BELOW HERE'''
    def get_netreturn(self):
        return self._netret
    
    def get_multis(self):
        return self._multipliers

if __name__ == '__main__':
    root = Tk()
    root.title('Stock Graph')
    app = GraphGui(root)
    root.mainloop()