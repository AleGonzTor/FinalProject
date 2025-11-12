import pygame
from obj import*

class Obstacle(Object):
    def __init__ (self,x,y,speed = 10,pic="./Sprites/Enemy.png",damage=1,guy="normal"):
        super(). __init__(x,y,pic)
        self.speed=speed
        self.damage=damage
        #self.guy=guy
        

    def update(self):
        pass

    def efecto(self,character):
        character.health -= self.damage
        

