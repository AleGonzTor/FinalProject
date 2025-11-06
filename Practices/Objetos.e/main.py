import pygame
import sys
from pygame import *
from pygame.sprite import *
from decoraciones import crear_decoraciones
pygame.init()
screen= display.set_mode((954,540))
display.set_caption("ayudaaa")
reloj=pygame.time.Clock()

decoraciones = crear_decoraciones()

while True:
    e= event.wait()
    if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((150,200,255))
    decoraciones.draw(screen)
    display.update()
    reloj.tick(60)



