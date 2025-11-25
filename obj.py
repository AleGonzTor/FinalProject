import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pic=None):

        super().__init__()
        
        self.layer = 0

        if pic:
            self.image = pygame.image.load("./Sprites/" + pic + ".png").convert_alpha()

        else:
            self.image = pygame.Surface((18, 18))
            self.image.fill((150, 150, 150))
        
        self.rect = self.image.get_rect(topleft=(x * 18, y * 18))
