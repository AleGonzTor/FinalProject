import pygame
from constants import *
from obstacle import *
from sounds import sound_manager

class Obstacle_v(Obstacle):
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom >= HEIGHT or self.rect.top<=0:
            self.speed*=-1
            sound_manager.play("hit")

