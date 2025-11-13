import pygame
from constants import *
from obstacle import *
from sounds import sound_manager

class Obstacle_h(Obstacle):
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left<=0:
            self.speed*=-1
            sound_manager.play("hit")

