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
        self.velocity[0] += force[0] / self.mass
        self.velocity[1] += force[1] / self.mass

    def update(self):
        if self.collided:
            self.velocity[1] = 0
            # move the object away from the collision
            self.transform(self.x + self.velocity[0], self.y + self.velocity[1])
            self.collided = False
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
        self.jump_velocity = 0.05
        self.jumped = False
        self.ducked = False
        self.original_size = size
        self.duck_size = (size[0] * 1, size[1] * 0.75)
        self.collided = False
        

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
            self.duck()
        else:
            self.ducked = False
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







gameobjects.append(rectangle(-4, -2, (6,.1), (1,0,0), "ground"))
# gameobjects.append(physicsObject(0, 0, (1, 1), (1, 0, 0), "phsyics object", 1, 0.1))
gameobjects.append(player(0, 0, (1, 1), (1, 0, 0), "player", pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 0.1))

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
            if type(obj) == player:
                obj.move(0, 0)
            for other in gameobjects:
                obj.collide(other)
        for obj in gameobjects:
            for other in gameobjects:
                if myobj.collide(other):
                    pass
                #     gameobjects.append(physicsObject(random.random()/10, 1, (1, 1), (1, 0, 0), "phsyics object", 1, 0.1))
                #     myobj = gameobjects[-1]
                

        pygame.display.flip()
        pygame.time.wait(10)
main()






