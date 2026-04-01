import gravitysim as sim
import pygame as pg

screen = sim.SCREEN
sim.SHOW_SPEED = True

    
sim.addObject(40,100000000,"red",pg.Vector2(screen.get_width() / 2, screen.get_height() / 2),0,0)
"""
sim.addObject(10,100000,"green",pg.Vector2(screen.get_width() / 3, screen.get_height() / 2),0,1.5)
sim.addObject(10,100000,"blue",pg.Vector2(screen.get_width() / 2.5, screen.get_height() / 2),0,1.8)


sim.addObject(40,100000000,"red",pg.Vector2(screen.get_width() / 2, screen.get_height() / 2),0,0)
sim.addObject(10,100000,"green",pg.Vector2(screen.get_width() / 4, screen.get_height() / 2),0.8,0.8)
sim.addObject(10,100000,"blue",pg.Vector2(screen.get_width() / 5, screen.get_height() / 2),0.8,-0.8)
sim.addObject(10,100000,"purple",pg.Vector2(screen.get_width() / 1.5, screen.get_height() / 2),-0.5,-0.5)
"""
sim.start()
