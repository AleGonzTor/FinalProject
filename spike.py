import pygame
from obj import *

class Spike(Object):
    def __init__(self,x,y,pic="./Sprites/Spike.png",damage=1,kind = 0):
        super().__init__(x, y, pic)
        self.damage = damage
        self.kind = kind
