import pygame
import sys
from constants import*


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Decoraciones")
clock = pygame.time.Clock()


from nivel_1_decoraciones import decoraciones_1
all_sprites = pygame.sprite.LayeredUpdates()
for decoracion in decoraciones_1:
    all_sprites.add(decoracion)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)









