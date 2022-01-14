from typing import Text
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random
from my_rects import *
from scene_logic import *
from collision_logic import *


def gameloop(scene, input_scene, input_none):
    pygame.init()
    display = (1000, 1000)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(90, (display[0]/display[1]), 1, 100)

    glTranslate(1, 0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    for obj in main_game.objects:
                        if obj == button:
                            if obj.collide(pos):
                                print("clicked")
                                obj.color = (1, 0, 0)
                            else:
                                obj.color = (0, 0, 1)
        for funct in input_scene:
            k = funct(scene)
            if k is scene:
                scene = k
            elif k is not None:
                scene.objects.append(k)

        for func in input_none:
            k = func()
            if k is scene:
                scene = k
            elif k is not None:
                scene.objects.append(k)
            
        

        glClearColor(0.0,0.0,0.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        scene.update()
        scene.draw()        

        pygame.display.flip()
        pygame.time.wait(10)
