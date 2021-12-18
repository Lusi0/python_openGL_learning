from typing import Text
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

gravity = -0.001

gameobjects = []

class rectangle:
    def __init__(self, x, y, size, color, id):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.collided = False
        self.id = id
    
    def draw(self):
        glBegin(GL_QUADS)
        glColor3fv(self.color)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.size[0], self.y)
        glVertex2f(self.x + self.size[0], self.y + self.size[1])
        glVertex2f(self.x, self.y + self.size[1])
        glEnd()
        
    def update(self):
        pass

    def transform(self, x, y):
        self.x = x
        self.y = y

    def collide(self, other):
        if other.x < self.x + self.size[0] < other.x + other.size[0] and other.y < self.y + self.size[1] < other.y + other.size[1]:
            self.collided = True
            return True
        if other.x < self.x < other.x + other.size[0] and other.y < self.y + self.size[1] < other.y + other.size[1]:
            self.collided = True
            return True
        if other.x < self.x + self.size[0] < other.x + other.size[0] and other.y < self.y < other.y + other.size[1]:
            self.collided = True
            return True
        if other.x < self.x < other.x + other.size[0] and other.y < self.y < other.y + other.size[1]:
            self.collided = True
            return True


class physicsObject(rectangle):
    def __init__(self, x, y, size, color, id,  mass, friction):
        super().__init__(x, y, size, color, id)
        self.mass = mass
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.friction = friction
        self.collided = False


    def applyForce(self, force):
        self.acceleration[0] += force[0] / self.mass
        self.acceleration[1] += force[1] / self.mass

    def update(self):
        if self.collided:
            self.velocity[1] = 0
        else:
            self.velocity[1] += gravity
        
        
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.transform(self.x + self.velocity[0], self.y + self.velocity[1])


        


class player(physicsObject):
    def __init__(self, x, y, size, color, id , jump_key, left_key, right_key, duck_key, speed):
        super().__init__(x, y, size, color, id, 1, 0.1)
        self.jump_key = jump_key
        self.left_key = left_key
        self.right_key = right_key
        self.duck_key = duck_key
        self.speed = speed
        self.jump_velocity = 0.5
        self.ducked = False
        self.duck_size = size * 0.5
        self.duck_y = y + self.duck_size
        self.duck_color = [0.5, 0.5, 0.5]
        self.collided = False

        

    def move(self, x, y):
        if pygame.key.get_pressed()[self.jump_key]:
            self.jump()
    
    def jump(self):
        if not self.ducked:
            self.y_velocity += self.jump_velocity






gameobjects.append(rectangle(-4, -2, (6,.1), (1,0,0), "ground"))
gameobjects.append(physicsObject(0, 0, (1, 1), (1, 0, 0), "phsyics object", 1, 0.1))


def main():
    myobj = gameobjects[1]
    pygame.init()
    display = (500, 500)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(50, (display[0]/display[1]), 1, 100)

    glTranslate(1, 0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClearColor(0.0,0.0,0.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for num,obj in enumerate(gameobjects):
            obj.update()
            obj.draw()
            for other in gameobjects:
                obj.collide(other)
        for obj in gameobjects:
            for other in gameobjects:
                if myobj.collide(other):
                    gameobjects.append(physicsObject(random.random()/10, 1, (1, 1), (1, 0, 0), "phsyics object", 1, 0.1))
                    myobj = gameobjects[-1]
                

        pygame.display.flip()
        pygame.time.wait(10)
main()







