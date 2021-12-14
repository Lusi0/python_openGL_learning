import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

x = 0
y = 0
verticesSquare = ((x+1,y+1),(x-1,y+1),(x-1,y-1),(x+1,y-1))



def sq(vertices):
    glBegin(GL_QUADS)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

def main():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(40, (display[0]/display[1]), 1, 10)

    glTranslate(1, 0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        x+=0.1

        sq(verticesSquare)
        pygame.display.flip()

main()







