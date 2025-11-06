import pygame
import constantes
class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,pic=None):
        super().__init__()
        self.layer = 0
        if pic:
            self.image = pygame.image.load(pic).convert_alpha()
        else:
            self.image = pygame.Surface((18,18))
            self.image.fill((150,150,150))
        self.rect = self.image.get_rect(topleft=(x*18,y*18))
    def update(self):
        pass
class Obstaculo(Object):
    def __init__ (self,x,y,speed,pic=None,damage=1,guy="normal"):
        super(). __init__(x,y,pic)
        self.speed=speed
        self.damage=damage
        self.guy=guy
        if not pic:
            self.rect=self.image.get_rect(topleft=(x*18,y*18))
    def efecto(self,Personaje):
        Personaje.vida -= self.damage
class ObstaculoVertical(Obstaculo):
    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= constantes.ANCHO_VENTANA or self.rect.left<=0:
            self.speed*=-1

class ObstaculoHorizontal(Object):
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom >= constantes.ALTO_VENTANA or self.rect.top<=0:
            self.speed*=-1

class Pincho(Object):
    def __init__(self,x,y,pic=None,damage=1,tipo="pincho"):
        super().__init__(x,y,pic)
        self.damage=damage
        self.tipo=tipo
        if not pic:
            self.image=pygame.Surface((18,18))
            self.image.fill((0,0,200))
        self.rect=self.image.get_rect(topleft=(x*18,y*18))
    def efecto(self,Personaje):
        Personaje.vida -= self.damage
