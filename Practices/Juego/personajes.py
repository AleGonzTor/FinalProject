import pygame
import sys
pygame.init()
pygame.display.set_caption("Personaje con png")
class Personaje(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("personaje.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.center = (600,600)
personaje = Personaje()
grupo_sprites = pygame.sprite.Group(personaje)