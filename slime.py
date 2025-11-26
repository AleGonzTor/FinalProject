import pygame
from constants import *
from obstacle import *

class Slime(Obstacle):
    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed *= -1
        
        self.image = pygame.transform.flip(self.tile_image, self.speed > 0, False)
