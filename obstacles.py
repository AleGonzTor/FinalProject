import pygame
from object import*

class Obstacle(Object):
    def __init__ (self,x,y,speed,pic=None,damage=1,guy="normal"):
        super(). __init__(x,y,pic)
        self.speed=speed
        self.damage=damage
        #self.guy=guy

    def update(self):
        pass

    def efecto(self,Personaje):
        Personaje.health -= self.damage
