import pygame
from constants import *
from obstacles import *

class Obstacle_h(Obstacle):
    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left<=0:
            self.speed*=-1

class Obstacle_v(Obstacle):
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom >= HEIGHT or self.rect.top<=0:
            self.speed*=-1

class Pincho(Object):
    def __init__(self,x,y,pic=None,damage=1,tipo="pincho"):
        super().__init__(x,y,pic)
        self.damage=damage
        self.tipo=tipo
        
    def efecto(self,Personaje):
        Personaje.vida -= self.damage
