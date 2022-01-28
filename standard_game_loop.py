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
                print(pos)
                for obj in scene.objects:
                    print(obj.click(pos),(obj.x, obj.y, obj.size))
                    if obj.click(pos):
                        print("clicked")
                        obj.on_click()
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
