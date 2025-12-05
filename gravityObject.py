import pygame as pg

class GravityObject:
    def __init__(self,screen, width:int,mass:int, color:str, pos:pg.Vector2,x:float = 0, y:float = 0, show_arrow = True):
        self.width = width
        self.color = color
        self.pos = pos
        self.mass = mass
        self.velocity = pg.math.Vector2(x, y)
        self.show_arrow = show_arrow
        self.screen = screen

    def show(self,zoom, offset = pg.math.Vector2(0,0)):
        pos = (self.pos - offset) * zoom
        width = self.width * zoom
        pg.draw.circle(self.screen, self.color, pos, width)

        if(self.show_arrow):
            end_pos = self.pos + self.velocity * 20
            pg.draw.line(self.screen, self.color, (self.pos - offset) * zoom, (end_pos - offset) * zoom, 3)
            arrow_angle = self.velocity.angle_to(pg.Vector2(1, 0))
            left_angle = arrow_angle + 135
            right_angle = arrow_angle - 135
            arrowhead_length = 10 / zoom
            left_pos = end_pos + pg.Vector2(arrowhead_length, 0).rotate(-left_angle)
            right_pos = end_pos + pg.Vector2(arrowhead_length, 0).rotate(-right_angle)
            pg.draw.polygon(self.screen, self.color, [(end_pos - offset) * zoom, (left_pos - offset) * zoom, (right_pos - offset) * zoom],int(3*zoom))
        
