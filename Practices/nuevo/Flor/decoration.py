import pygame
from object import Object

class Decoration(Object):
    def __init__(self, x, y, pic, layer=0):
        super().__init__(x, y, pic, layer)

    def escala(self, ancho, alto):
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))


