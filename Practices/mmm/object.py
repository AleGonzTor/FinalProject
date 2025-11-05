import pygame,sys
pygame.init()
tile_area= 18 
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, pic=None, layer = 0, tile=(1,1)):
        #Se inicializa primero la superclase
        super().__init__()
        self._layer = layer

        width = tile_area*tile[0]
        height = tile_area*tile[1]
        #Si hay imagen, la carga
        if pic:
            self.image = pygame.image.load(pic).convert_alpha()
        #Si no hay imagen, crea un surface
        else:
            self.image = pygame.Surface((tile_area,tile_area))
            self.image.fill((150, 150, 150))
        
        #Crea un rectangulo
        self.rect = self.image.get_rect(topleft=(x, y))
    def update(self):
        pass

class Arbol(Object):
    def __init__(self,x,y,tile=(4,6)):
        super().__init__(x,y,"arbol.png",layer=1,tile=tile)


class Arbusto(Object):
    def __init__(self, x, y, tile=(2,2)):
        super().__init__(x, y, "arbusto.png", layer=1, tile=tile)

class Hongo(Object):
    def __init__(self, x, y, tile=(1,1)):
        super().__init__(x, y, "hongo.png", layer=2, tile=tile)

class Nube(Object):
    def __init__(self, x, y, tile=(3,2)):
        super().__init__(x, y, "nube.png", layer=1, tile=tile)
        self.velocidad = 1  

    def mover(self):
        self.rect.x += self.velocidad
        #falta


