"""
gravitysim adds simulated gravity with a pygame window
"""
from gravityObject import GravityObject
import pygame as pg
import math

"""
Effectively "G" in newtonian calculations, if precision is required, change it to the proper value
"""
GRAVITY_SIZE = 0.00001

"""
If the program should show arrows of where it is going, can be turned off
"""
SHOW_ARROW = True

"""
If the program should show speed, can be turned on
"""
SHOW_SPEED = False


pg.init()
SCREEN = pg.display.set_mode((1280, 720))
CLOCK = pg.time.Clock()
DT = 0
pg.font.init()
my_font = pg.font.SysFont('Arial', 20)
zoom = 1.0
gravity_objects:list[GravityObject] = []

def userInput():
    global zoom
    keys = pg.key.get_pressed()
    if keys[pg.K_UP]:
        zoom *= 1.01
    if keys[pg.K_DOWN]:
        zoom /= 1.01

def gravityCalculation():
    for i in range(len(gravity_objects)):
        for j in range(i + 1, len(gravity_objects)):
            direction = pg.math.Vector2(gravity_objects[j].pos - gravity_objects[i].pos)
            distance = direction.length()
            direction = direction.normalize()

            force = GRAVITY_SIZE * gravity_objects[i].mass * gravity_objects[j].mass / (distance * distance)
            gravity_objects[i].velocity += direction * force / gravity_objects[i].mass
            gravity_objects[j].velocity -= direction * force / gravity_objects[j].mass
            gravity_objects[i].pos += gravity_objects[i].velocity
            gravity_objects[j].pos += gravity_objects[j].velocity

def screenShowcase(offset):
    i = 1
    for GravityObject in gravity_objects:
        GravityObject.show(zoom, offset)
        if(SHOW_SPEED):
            a = math.sqrt(GravityObject.velocity[0]**2 + GravityObject.velocity[1]**2)
            text_surface = my_font.render('{0} -> {1}'.format(GravityObject.color,a), True, "white")
            SCREEN.blit(text_surface, (0, i*22))
            i+=1

"""
Adds an object, with parameters
width: int - visible size of the object
mass: int - actual mass of the object, used in gravity calculation
color: str - use either e.g. "red", or rgb values to string
pos: Vector2 - starting position, recommended to use relatively to the screen
x: float - starting speed on the x axis
y: float - starting speed on the y axis
"""
def addObject(width:int,mass:int,color:str,pos:pg.Vector2,x:float=0,y:float=0) -> None:
    gravity_objects.append(GravityObject(SCREEN,width,mass,color,pos,x,y,SHOW_ARROW))

"""
Starts the program, call after all objects have been added with addObject
"""
def start() -> None:
    running = True

    while running:
        SCREEN.fill("black")
        userInput()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        gravityCalculation()
        offset = gravity_objects[0].pos - pg.Vector2(SCREEN.get_width() / 2, SCREEN.get_height() / 2) /zoom
        screenShowcase(offset)

        pg.display.flip()
        DT = CLOCK.tick(60) / 1000
    pg.quit()

