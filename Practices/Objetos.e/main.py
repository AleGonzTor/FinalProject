import pygame
import sys
from pygame import *
from pygame.sprite import *
from objects import Decoration 
pygame.init()
screen= display.set_mode((954,540))
display.set_caption("ayudaaa")
reloj=pygame.time.Clock()

# Grupo de sprites
decoraciones = pygame.sprite.Group()

# Crea decoraciones (x, y, tipo)
arbol = Decoration(100, 300, 1)
arbusto = Decoration(300, 320, 2)
pasto = Decoration(500, 340, 3)
cartel = Decoration(700, 350, 4)
hongos = Decoration(850, 310, 5)
arbol2 = Decoration(400, 300, 1)

# Agrega al grupo
decoraciones.add(arbol, arbusto, pasto, cartel, hongos, arbol2)

while True:
    e= event.wait()
    if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((150,200,255))
    decoraciones.draw(screen)
    display.update()
    reloj.tick(60)



