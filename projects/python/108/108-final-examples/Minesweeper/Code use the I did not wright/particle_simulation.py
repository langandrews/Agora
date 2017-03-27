'''
GUI controller for a particle simulation
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
'''

from tkinter import *
from random import randint
from particle import *
from helpers import *

class ParticleSimulation:
    ''' Creates particle simulator '''
    
    def __init__(self, window):
        ''' Construct the particle simulator GUI '''
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 400
        self.canvas = Canvas(self.window, bg='black',
                        width=self.width, height=self.width)
        self.canvas.pack()
        self.terminated = False
        self.p1_list=[]
        self.canvas.bind('<Button-1>', self.check_remove_particle)
        self.button = Button(self.window, text='Add particle', command=self.add_particle)
        self.button.pack(sid='left')
        while self.terminated == False:
            self.canvas.delete(ALL)
            for p1 in self.p1_list:
                p1.move(self.canvas)
                p1.render(self.canvas)
                for p2 in self.p1_list:
                    p1.bounce(p2)
            self.canvas.after(50)
            self.canvas.update()
                   
    def add_particle(self):
        self.p1_list.append(Particle(randint(0,400),randint(0,400),randint(-25,25),randint(-25,25),color = get_random_color()))
    
    def check_remove_particle(self, event):
        for p in self.p1_list:
            if distance(event.x, event.y, p.get_x(), p.get_y())<=p.get_radius():
                self.p1_list.remove(p)
        
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')    
    app = ParticleSimulation(root)
    root.mainloop()
    
