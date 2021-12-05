import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(40, (display[0]/display[1]), 1, 1)

    glTranslatef(0, 0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pygame.display.flip()
        pygame.time.wait(10)

main()