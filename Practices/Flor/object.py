import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pic, layer=0):

        super().__init__()
        self.layer = layer
        
        self.image = pygame.image.load(pic).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x,y))
        
