"""
Sim adds simulated gravity with a pygame window
"""
import pygame as pg
print("Thank you for using my gravity simulator module!")
import math
import sys
GRAVITY_SIZE = 0.00001
SHOW_ARROW = True
pg.init()
SCREEN = pg.display.set_mode((1280, 720))
CLOCK = pg.time.Clock()
SHOW_SPEED = False
DT = 0
pg.font.init()
my_font = pg.font.SysFont('Arial', 20)
class object:
    def __init__(self, width:int,mass:int, color:str, pos:pg.Vector2,x:float = 0, y:float = 0):
        self.width = width
        self.color = color
        self.pos = pos
        self.mass = mass
        self.velocity = pg.math.Vector2(x, y)
    def show(self,zoom, offset = pg.math.Vector2(0,0)):
        pos = (self.pos - offset) * zoom
        width = self.width * zoom
        pg.draw.circle(SCREEN, self.color, pos, width)
        if(SHOW_ARROW):
            end_pos = self.pos + self.velocity * 20
            pg.draw.line(SCREEN, self.color, (self.pos - offset) * zoom, (end_pos - offset) * zoom, 3)
            arrow_angle = self.velocity.angle_to(pg.Vector2(1, 0))
            left_angle = arrow_angle + 135
            right_angle = arrow_angle - 135
            arrowhead_length = 10 / zoom
            left_pos = end_pos + pg.Vector2(arrowhead_length, 0).rotate(-left_angle)
            right_pos = end_pos + pg.Vector2(arrowhead_length, 0).rotate(-right_angle)
            pg.draw.polygon(SCREEN, self.color, [(end_pos - offset) * zoom, (left_pos - offset) * zoom, (right_pos - offset) * zoom],int(3*zoom))
        
"""
An array of objects, call with: object(size, mass, color, position, speed vector x, speed vector y)
"""
objects = []
def start():
    zoom = 1.0
    running = True
    while running:
        SCREEN.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            zoom *= 1.01
        if keys[pg.K_DOWN]:
            zoom /= 1.01


        for i in range(len(objects)):
            for j in range(i + 1, len(objects)):
                direction = pg.math.Vector2(objects[j].pos - objects[i].pos)

                distance = direction.length()

                direction = direction.normalize()

                force = GRAVITY_SIZE * objects[i].mass * objects[j].mass / (distance * distance)

                objects[i].velocity += direction * force / objects[i].mass
                objects[j].velocity -= direction * force / objects[j].mass

                objects[i].pos += objects[i].velocity
                objects[j].pos += objects[j].velocity


        offset = objects[0].pos - pg.Vector2(SCREEN.get_width() / 2, SCREEN.get_height() / 2) /zoom
        i = 1
        for object in objects:
            object.show(zoom, offset)
            if(SHOW_SPEED):
                a = math.sqrt(object.velocity[0]**2 + object.velocity[1]**2)
                text_surface = my_font.render('{0} -> {1}'.format(object.color,a), True, "white")
                SCREEN.blit(text_surface, (0, i*22))
                i+=1
        pg.display.flip()


        DT = CLOCK.tick(60) / 1000


    pg.quit()

