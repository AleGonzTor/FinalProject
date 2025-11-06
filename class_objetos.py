import pygame
from constants import*
from objetos_t import*

class ObstaculoVertical(Obstaculo):
    def update(self):
        self.rect.y += self.speed
        if self.rect.right >= WIDTH or self.rect.left<=0:
            self.speed*=-1

class ObstaculoHorizontal(Object):
    def update(self):
        self.rect.x += self.speed
        if self.rect.bottom >= HEIGHT or self.rect.top<=0:
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
