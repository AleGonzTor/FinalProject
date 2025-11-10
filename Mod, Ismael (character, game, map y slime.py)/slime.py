import pygame
from constants import *
from obstacle import *

class Slime(Obstacle):
    def __init__(self, x, y, speed, pic="./Sprites/Slime.png", damage=0, guy="slime"):
        super().__init__(x, y, speed, pic, damage, guy)
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left<=0:
            self.speed*=-1
