import pygame
import sys
from pygame import *
from pygame.sprite import *
from objetos import Objectinmapa
pygame.init()
screen= display.set_mode((954,540))
display.set_caption("ayudaaa")
reloj=pygame.time.Clock()

mapa= Objectinmapa()

while True:
    e= event.wait()
    if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((150,200,255))
    mapa.dibujar(screen)
    display.update()
    reloj.tick(60)



