from typing import Text
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

class square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def draw(self):
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)
        glVertex2f(self.x + self.size, self.y)
        glVertex2f(self.x + self.size, self.y + self.size)
        glVertex2f(self.x, self.y + self.size)
        glEnd()

    def transform(self, x, y):
        self.x = x
        self.y = y




test = square(-1, 0, 1)


def main():
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
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        test.transform(test.x+0.01, 0)
        test.draw()
        pygame.display.flip()
        pygame.time.wait(100)
main()







