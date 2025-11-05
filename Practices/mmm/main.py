
import pygame, sys
from object import Arbol, Arbusto, Hongo, Nube

pygame.init()
rosado = (255,228,255)
size = (954,540)
screen = pygame.display.set_mode(size)
clock=pygame.time.Clock()
#color de fondo
screen.fill(rosado)

decoraciones = [
     Arbol(100,200,tile=(1,1)),
     Arbol(300,180, tile=(4,6)),
     Arbusto(500,30),
     Hongo(270,180),
     Nube(30,30, tile =(5,5))
]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(rosado)
    for i in decoraciones:
        screen.blit(i.image,i.rect)

    pygame.display.flip()
    clock.tick(60)















