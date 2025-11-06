import pygame
from object import*
from character import*
from classes import*

class Obstaculo(Object):
    def __init__ (self,x,y,speed,pic=None,damage=1,guy="normal"):
        super(). __init__(x,y,pic)
        self.speed=speed
        self.damage=damage
        self.guy=guy
        if not pic:
            self.rect=self.image.get_rect(topleft=(x*18,y*18))
    def update(self):
        pass
    def efecto(self,Personaje):
        Personaje.health -= self.damage
