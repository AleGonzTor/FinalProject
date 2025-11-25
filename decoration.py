from obj import *
from constants import *
import pygame

class Decoration(Object):
    
    dictionary = { 
        1: {"picture": "Sign", "layer": 1},  
        2: {"picture": "Burguer", "layer": 1},
        3: {"picture": "Bush", "layer": 1},
        4: {"picture": "Clouds", "layer": 1},
        5: {"picture": "Mushrooms", "layer": 1},
        6: {"picture": "Grass", "layer": 1},
        7: {"picture": "Idk", "layer": 1}
        }

    def __init__(self, x, y, obj=0):
        
        config = self.dictionary.get(obj)

        if config:
            super().__init__(x, y, config["picture"])
            self.layer = config["layer"]
        else:
            
            super().__init__(x, y)
            self.layer = 0
        if obj == 7:
            
            self.tile_image = self.image
            self.image = pygame.Surface((10 * TILE_SIZE, 5 * TILE_SIZE), pygame.SRCALPHA)

            self.duplicate(10, 5)
            self.image.fill((200, 200, 200), special_flags=pygame.BLEND_RGBA_MULT)  
            self.rect = self.image.get_rect(topleft=(x * 18, y * 18))
    def duplicate(self, w, h):
        
        for i in range(h):
            for j in range(w):
                self.image.blit(self.tile_image, (j * TILE_SIZE, i * TILE_SIZE))

    def scale(self, scale):
        self.image = pygame.transform.scale(self.image, (self.rect.width * scale, self.rect.height * scale))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
