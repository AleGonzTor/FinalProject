import pygame
from constants import *
from obstacle import *

class Obstacle_v(Obstacle):
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom >= HEIGHT or self.rect.top<=0:
            self.speed*=-1
