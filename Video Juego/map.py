import pygame
import constantes
from character import Character

class Ground (pygame.sprite.Sprite):
    def __init__(self,x, y, withd, hight):
        super().__init__()
        self.image = pygame.Surface((withd, hight))
        self.image.fill ((128, 64, 0))
        self.rect = self.image.get_rect(topleft= (x, y))


class Background:
    def __init__(self):
        self.background = pygame.image.load("fondo.png")
        self.background = pygame.transform.scale(self.background, (constantes.WITH_SCREEN, constantes.HIGH_SCREEN))
        