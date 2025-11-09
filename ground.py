from obj import *
from constants import *
import pygame

class Ground(Object):
    def __init__(self, x, y, w_tiles = WIDTH, h_tiles = 1, picture = "./Sprites/Floor.png"):
        super().__init__(x, y, picture)

        self.tile_image = self.image

        self.image = pygame.Surface((w_tiles * TILE_SIZE, h_tiles * TILE_SIZE), pygame.SRCALPHA)

        for i in range(w_tiles):
            for j in range(h_tiles):
                self.image.blit(self.tile_image, (i * TILE_SIZE, j * TILE_SIZE))

        self.rect = self.image.get_rect(topleft=(x * 18, y * 18))
    
