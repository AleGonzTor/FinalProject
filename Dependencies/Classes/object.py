import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pic=None):

        #Se inicializa primero la superclase
        super().__init__()
        
        self.layer = 0
        #Si hay imagen, la carga
        if pic:
            self.image = pygame.image.load(pic).convert_alpha()
        #Si no hay imagen, crea un surface
        else:
            self.image = pygame.Surface((32, 32))
            self.image.fill((150, 150, 150))
        
        #Crea un rectangulo
        self.rect = self.image.get_rect(topleft=(x, y))