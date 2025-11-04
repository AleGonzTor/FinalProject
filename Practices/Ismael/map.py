import pygame
import constantes
from object import Object
from character import Character


class Ground (pygame.sprite.Sprite):
    def __init__(self,x, y, widht, height, square_image):
        super().__init__()
        self.image_square = pygame.image.load(square_image).convert_alpha()
        self.image_square =  pygame.transform.scale(self.image_square, (constantes.TILES_AREA, constantes.TILES_AREA))
        square_x =int(widht // constantes.TILES_AREA)
        square_y = int(height // constantes.TILES_AREA)
        self.image = pygame.Surface((square_x * constantes.TILES_AREA, square_y * constantes.TILES_AREA), pygame.SRCALPHA)
        for i in range(square_x):
            for j in range (square_y):
                self.image.blit(self.image_square, (i * constantes.TILES_AREA, j * constantes.TILES_AREA ))
                
        self.rect = self.image.get_rect(topleft= (x, y))

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, widht, heigth, square_image):
        super().__init__()
        self.image_square = pygame.image.load(square_image).convert_alpha()
        self.image_square =  pygame.transform.scale(self.image_square, (constantes.TILES_AREA, constantes.TILES_AREA))
        square_x = int(widht // constantes.TILES_AREA)
        square_y = int(heigth // constantes.TILES_AREA)
        self.image = pygame.Surface((square_x * constantes.TILES_AREA, square_y * constantes.TILES_AREA), pygame.SRCALPHA)
        
        for i in range(square_x):
            for j in range(square_y):
                self.image.blit(self.image_square, (i * constantes.TILES_AREA, j * constantes.TILES_AREA ))
        
        self.rect = self.image.get_rect(topleft =  (x, y))

class Background:
    def __init__(self):
        self.background = pygame.image.load("images/Tilemap/tilemap-backgrounds_packed.png")
        self.background = pygame.transform.scale(self.background, (constantes.WITH_SCREEN, constantes.HIGH_SCREEN))
        