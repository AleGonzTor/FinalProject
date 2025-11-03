from constants import *
from character import *
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('PVJ')
clock = pygame.time.Clock()

fondo = pygame.image.load("Sprites\Back.png").convert()
fondo = pygame.transform.scale(fondo, (width, height))

floor = height - 120
                                                                                                                                                                                                                              

caballero = Personaje()
sprt = pygame.sprite.Group(caballero)

while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                caballero.movement[0] = True
            if event.key == pygame.K_d:
                caballero.movement[1] = True
            if event.key == pygame.K_s:
                caballero.movement[2] = True
            if event.key == pygame.K_w:
                caballero.jump(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                caballero.movement[0] = False
            if event.key == pygame.K_d:
                caballero.movement[1] = False
            if event.key == pygame.K_s:
                caballero.movement[2] = False


    caballero.update_pos(dt)
    screen.fill((150,200,255))
    screen.blit(fondo, (0, 0))
    sprt.draw(screen)
    pygame.display.update()
    
