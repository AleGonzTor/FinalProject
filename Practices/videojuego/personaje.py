import pygame, sys
pygame.init()
class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rusell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (0,500)
personaje = Personaje()
grupo_sprites = pygame.sprite.Group(personaje)





