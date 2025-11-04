import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, pic = "Sprites\Platform.png"):
        super().__init__()
        self.image = pygame.image.load(pic).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    