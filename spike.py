import pygame
from obj import*

class Spike(Object):
    def __init__ (self, x, y, pic_type = 0, pic="Spike"):
        super(). __init__(x,y,pic)
        
        self.tile_image = self.image.copy()
        
        self.image = pygame.transform.rotate(self.tile_image, -90 * (pic_type % 4))
        
        self.rect = self.image.get_rect(topleft=(x * 18, y * 18))

    def update(self):
        pass

        

