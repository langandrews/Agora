'''
Model a single particle
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
'''
import math
from helpers import *

class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas
    '''

    def __init__(self, x = 50, y = 50, velX = 10, velY = 15, radius = 15, color = '#663977'):
        '''
        Constructor
        '''
        self._x = x
        self._y = y
        self._velX = velX
        self._velY = velY
        self._radius = radius
        self._color = color
       
    def render(self, canvas):
        canvas.create_oval(self._x - self._radius, self._y - self._radius, self._x + self._radius, self._y + self._radius, fill = self._color)
        
    def move(self, canvas):
        self._x += self._velX
        self._y += self._velY
        if self._x + self._radius > canvas.winfo_reqwidth() or self._x - self._radius < 0:
            self._velX =-self._velX
        if self._y + self._radius > canvas.winfo_reqwidth() or self._y - self._radius < 0:
            self._velY =-self._velY
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_radius(self):
        return self._radius
     
    def hits(self, other):
        if (self == other):
            # I can't collide with myself.
            return False
        else:
            # Determine if I overlap with the target particle.
            return (self._radius + other.get_radius()) >= distance(self._x, self._y, other.get_x(), other.get_y())
            
     
    def bounce(self, target):
        ''' This method modifies this Particle object's velocities based on its
            collision with the given target particle. It modifies both the magnitude
            and the direction of the velocities based on the interacting magnitude
            and direction of particles. It only changes the velocities of this
            object; an additional call to bounce() on the other particle is required
            to implement a complete bounce interaction.
      
            The collision algorithm is based on a similar algorithm published by K.
            Terzidis, Algorithms for Visual Design.
      
            target  the other particle
         '''
        DAMPENING_FACTOR = 0.88
        if self.hits(target):
            angle = math.atan2(target.get_y() - self._y, target.get_x() - self._x)
            targetX = self._x + math.cos(angle) * (self._radius + target.get_radius())
            targetY = self._y + math.sin(angle) * (self._radius + target.get_radius())
            ax = targetX - target.get_x()
            ay = targetY - target.get_y()
            self._velX = (self._velX - ax) * DAMPENING_FACTOR
            self._velY = (self._velY - ay) * DAMPENING_FACTOR
    