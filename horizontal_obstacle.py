import pygame
from constants import *
from obstacle import *

class Obstacle_h(Obstacle):
    hit_sound = None
    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left<=0:
            self.speed*=-1
            if Obstacle_h.hit_sound is None:
                Obstacle_h.hit_sound = pygame.mixer.Sound("Sounds/hit1.wav")
            Obstacle_h.hit_sound.play()
