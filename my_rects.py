from typing import Text
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

class rectangle:
    def __init__(self, x, y, size, color, id, collsion_func):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.collided = False
        self.id = id
        self.collsion_func = collsion_func
    
    def draw(self):
        glBegin(GL_QUADS)
        glColor3fv(self.color)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.size[0], self.y)
        glVertex2f(self.x + self.size[0], self.y + self.size[1])
        glVertex2f(self.x, self.y + self.size[1])
        glEnd()
        
    def update(self,*args): 
        pass

    def transform(self, x, y):
        self.x = x
        self.y = y

    def collide(self, other):
        if other != self:
            if other.x < self.x + self.size[0] < other.x + other.size[0] and other.y < self.y + self.size[1] < other.y + other.size[1]:
                self.collided = True
                self.collision_func(self, other)
                return True
            if other.x < self.x < other.x + other.size[0] and other.y < self.y + self.size[1] < other.y + other.size[1]:
                self.collided = True
                self.collision_func(self, other)
                return True
            if other.x < self.x + self.size[0] < other.x + other.size[0] and other.y < self.y < other.y + other.size[1]:
                self.collided = True
                self.collision_func(self, other)
                return True
            if other.x < self.x < other.x + other.size[0] and other.y < self.y < other.y + other.size[1]:
                self.collided = True
                self.collision_func(self, other)
                return True
        return False


class button(rectangle):
    def __init__(self, x, y, size, color, id, collision_func, text, text_color):
        super().__init__(x, y, size, color, id, collision_func)
        self.text = text
        self.text_color = text_color

    def draw(self):
        super().draw()
        glColor3fv(self.text_color)
        glRasterPos2f(self.x, self.y)
        for char in self.text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))





class physicsObject(rectangle):
    def __init__(self, x, y, size, color, id,collision_func,  mass, friction, elacitiy):
        super().__init__(x, y, size, color, id,collision_func)
        self.mass = mass
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.friction = friction
        self.collided = False
        self.curElacitiy = elacitiy
        self.elacitiy = elacitiy
        self.collision_func = collision_func


    def applyForce(self, force):
        self.velocity[0] += force[0] / self.mass
        self.velocity[1] += force[1] / self.mass

    def update(self, gravity):
        if self.collided:
            #collision_func(self, self.collided)
            self.collided = False
        else:
            self.velocity[1] += gravity
        
        
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        # friction
        self.velocity[0] *= self.friction
        self.velocity[1] *= self.friction
        self.transform(self.x + self.velocity[0], self.y + self.velocity[1])


        


class player(physicsObject):
    def __init__(self, x, y, size, color, id,collsion_func,mass, friction,elacitiy , jump_key, left_key, right_key, duck_key, speed):
        super().__init__(x, y, size, color, id, collsion_func, mass,friction,elacitiy )
        self.jump_key = jump_key
        self.left_key = left_key
        self.right_key = right_key
        self.duck_key = duck_key
        self.speed = speed
        self.jump_velocity = 0.05
        self.jumped = False
        self.ducked = False
        self.original_size = size
        self.duck_size = (size[0] * 1, size[1] * 0.75)
        self.collided = False
        self.curElacitiy = elacitiy
        self.elacitiy = elacitiy
        self.collsion_func = collsion_func
        

    def move(self, x, y):
        print(self.velocity)
        keys = pygame.key.get_pressed()
        if keys[self.jump_key]:
            self.jump()
        if keys[self.left_key]:
            self.x -= self.speed
        if keys[self.right_key]:
            self.x += self.speed
        if keys[self.duck_key]:
            self.ducked = True
            self.curElacitiy = 0
            self.duck()
        else:
            self.ducked = False
            self.curElacitiy = self.elacitiy
            self.size = self.original_size
    
    # jump function that checks if the player is on the ground and then applies a force to the player
    def jump(self):
        if self.jumped == True:
            if self.velocity[1] == 0:
                self.jumped = False
        if self.jumped == False:
            self.y += 0.1
            self.applyForce([0, self.jump_velocity])
            self.jumped = True

    def duck(self):
        print("duck")
        self.size = self.duck_size