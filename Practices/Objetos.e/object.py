import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pic=None, layer=0):
        # Inicializa el sprite
        super().__init__()

        # Si hay una imagen, la carga
        if pic:
            self.image = pygame.image.load(pic).convert_alpha()
        else:
            # Si no hay imagen, crea un cuadrado gris como marcador
            self.image = pygame.Surface((18,18))
            self.image.fill((150, 150, 150))

        # Crea el rectángulo (posición del objeto)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.layer=layer




        

