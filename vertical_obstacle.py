import pygame
from constants import *
from obstacle import *

class Obstacle_v(Obstacle):
    hit_sound = None
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom >= HEIGHT or self.rect.top<=0:
            self.speed*=-1
            if Obstacle_v.hit_sound is None:
                Obstacle_v.hit_sound = pygame.mixer.Sound("Sounds/hit1.wav")
            Obstacle_v.hit_sound.play()
