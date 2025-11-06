from obj import *
from constants import *
import pygame

class Decoration(Object):
    
    dictionary = { 
        1: {"picture": "Sprites/Sign.png", "layer": 1},  
        2: {"picture": "Sprites/Burguer.png", "layer": 1},
        }

    def __init__(self, x, y, obj=0):
        # Busca la configuración del tipo de decoración
        config = self.dictionary.get(obj)

        if config:
            super().__init__(x, y, config["picture"])
            self.layer = config["layer"]
        else:
            # Si no existe el tipo, crea un cuadrado gris
            super().__init__(x, y)
            self.layer = 0
    
    def scale(self, scale):
        self.image = pygame.transform.scale(self.image, (self.rect.width * scale, self.rect.height * scale))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))