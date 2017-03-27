''' Logic Class for Mastermind game
12/04/14
Final Project
@author: Cara Alexander (cea6)
'''



import random 

class Logic:
    """
    Class to model mastermind logic 
    optional parameter to specify solution sequence, default creates random sequence of the 6 colors
    """
    
    def __init__(self, r = True):
        """constructor"""
        #randomly choose sequence of colors and set as solution
        #seq = ['pink','green','blue','red','yellow','orange']
        seq = ['#FF6CB5','green','#59ACFF','red','yellow','#FF8330']
        if r == True:
            self.solution = [random.choice(seq),random.choice(seq),random.choice(seq),random.choice(seq)]
        else:
            self.solution = ['green','green','yellow','red']
    
    
    #method to check a guess, returns list of white and black pins
    def check(self, guess):
        """
        Method to compare the input guess with the solution
        guess (list of colors) -> pins (list of pin colors)
        """
        self.guess = guess
        pins = []
        
        #initialize boolean variables to False for if that peg in the solution (n) or the guess (g) has not been found to match something and assigned a pin
        n0=False
        n1=False
        n2=False
        n3=False
        
        g0=False
        g1=False
        g2=False
        g3=False
       
       
        #check for white pins
        if self.guess[0] == self.solution[0]:
            pins.append('white')
            n0=True
            g0=True
        if self.guess[1] == self.solution[1]:
            pins.append('white')
            n1=True
            g1=True
        if self.guess[2] == self.solution[2]:
            pins.append('white')
            n2=True
            g2=True
        if self.guess[3] == self.solution[3]:
            pins.append('white')
            n3=True
            g3=True
      
      
        #check for black pins, I originally had a loop but that would not work with the set of boolean variables,n0 to n3 and g0 to g3, I used to let the system handle using the same color twice
        n=0
        if self.guess[0] == self.solution[1] and n1==False and g0==False:
                    pins.append('black')
                    n1=True
                    g0=True
                    #testing purposes only print(n,'guess',1,'sol')
        elif self.guess[0] == self.solution[2] and n2==False and g0==False:
                    pins.append('black')
                    n2=True
                    g0=True
                    #testing purposes only print(n,'guess',2,'sol')
        elif self.guess[0] == self.solution[3] and n3==False and g0==False:
                    pins.append('black')
                    n3=True
                    g0=True
                    #testing purposes only print(n,'guess',3,'sol')
        n=1
        if self.guess[1] == self.solution[0] and n0==False and g1==False:
                    pins.append('black')
                    n0=True
                    g1=True
                    #testing purposes only print(n,'guess',0,'sol')
        elif self.guess[1] == self.solution[2] and n2==False and g1==False:
                    pins.append('black')
                    n2=True
                    g1=True
                    #testing purposes only print(n,'guess',2,'sol')
        elif self.guess[1] == self.solution[3] and n3==False and g1==False:
                    pins.append('black')
                    n3=True
                    g1=True
                    #testing purposes only print(n,'guess',3,'sol')
        n=2
        if self.guess[2] == self.solution[0] and n0==False and g2==False:
                    pins.append('black')
                    n0=True
                    g2==True
                    #testing purposes only print(n,'guess',0,'sol')
        elif self.guess[2] == self.solution[1] and n1==False and g2==False:
                    pins.append('black')
                    n1=True
                    g2=True
                    #testing purposes only print(n,'guess',1,'sol')
        elif self.guess[2] == self.solution[3] and n3==False and g2==False:
                    pins.append('black')
                    n3=True
                    g2=True
                    #testing purposes only print(n,'guess',3,'sol')
        n=3
        if self.guess[3] == self.solution[0] and n0==False and g3==False:
                    pins.append('black')
                    n0=True
                    g3=True
                    #testing purposes only print(n,'guess',0,'sol')
        elif self.guess[3] == self.solution[1] and n1==False and g3==False:
                    pins.append('black')
                    n1=True
                    g3=True
                    #testing purposes only print(n,'guess',1,'sol')
        elif self.guess[3] == self.solution[2] and n2==False and g3==False:
                    pins.append('black')
                    n2=True
                    g3=True
                    #testing purposes only print(n,'guess',2,'sol')
        
        #for my testing purposes only
        #print(self.solution)
        #print(self.guess)
        #print(pins)
        
        return pins
        
#tests
if __name__ == "__main__":
    l = Logic()
    x = l.check(['green','green','green','green'])
    assert len(x)<=4
    for n in range(len(x)):
        assert x[n]=='white'
    s = Logic(False)
    y = s.check(['green','green','yellow','red'])
    assert y==['white','white','white','white']
    z = s.check(['green','#59ACFF','yellow','red'])
    assert z==['white','white','white']
    q = s.check(['green','yellow','green','red'])
    assert q==['white','white','black','black']
    w = s.check(['green','green','green','green'])
    assert w==['white','white']
    e = s.check(['#59ACFF','#59ACFF','#59ACFF','#59ACFF'])
    assert e==[]
    r = s.check(['red','yellow','green','green'])
    assert r==['black','black','black','black']
    print('passed all tests!')  
        
        