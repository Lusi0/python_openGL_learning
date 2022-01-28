from typing import Text
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random
from my_rects import *
from scene_logic import *
from standard_game_loop import *


main_menu = scene("main_menu", [])

myplayer = player(0, 0, (1, 1), (1, 0, 0), "player",bounce_collision,1,1,0.5 ,pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 0.1)

main_game = gravity_scene("main_game", 
[
    rectangle(-4, -2, (6,.1), (1,0,0), "ground",default_collision),
    physicsObject(-2-0.3, 2, (1, 1), (0, 0, 1), "physicsObject2",bounce_collision,1,1,0.6),
physicsObject(-2-0.1, 1, (1, 1), (0.2, 0, 0.5), "physicsObject2",bounce_collision,1,1,0.6),
physicsObject(-2, -1, (1, 1), (1, 0.2, 0), "physicsObject",bounce_collision,1,1,0.6),
], 
-0.001)

def onclick():
    print("click")

button_test = scene("button_test", [button(-2, -2, (1, 1), (1, 0, 0), "button",default_collision,"click me",(1,0,1),onclick()),
])

test_bounce = gravity_scene("test_bounce", [rectangle(-2, -4, (.1,6), (1,0,0), "ground",default_collision),rectangle(2, 4, (.1,6), (1,0,0), "ground",default_collision),rectangle(4, 2, (6,.1), (1,0,0), "ground",default_collision),rectangle(-4, -2, (6,.1), (1,0,0), "ground",default_collision),physicsObject(0,0,(1,1),(1,0,0), "box",bounce_collision,1,1,1)], -0.001)

test_screen = gravity_scene("text_screen", [],0.00)

test_screen.add_object(rectangle( -4,-2, (.1,6), (1,0,0), "left",default_collision))

test_screen.add_object(rectangle( 3,-2, (.1,6), (1,0,0), "right",default_collision))


test_screen.add_object(rectangle( -4,-2, (7,0.1), (1,0,0), "down",default_collision))

test_screen.add_object(rectangle( -4,4, (7.1,0.1), (1,0,0), "up",default_collision))

test_screen.add_object(physicsObject(1,1,(2,2),(1,0,0), "box",bounce_collision,1,1,1))

test_screen.objects[-1].velocity = [0.03,0.01]


global memory 
memory = 0
def create_cube(scene):
    # random x and y locations between -2 and 2
    x = random.randint(-2, 2)
    y = random.randint(-2, 2)
    cube = physicsObject(x,y,(1,1),(1,0,0), "box",bounce_collision,1,1,1)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_c] and memory == 0:
        memory = 1
        return cube
    else:
        memory = 0
        return None

gameloop(button_test,[],[])